"""问卷流程测试与真实数据描述统计。依赖 pandas openpyxl Pillow；不改写输入。"""
import argparse
import csv
import hashlib
import json
import random
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
SIM = '模拟数据，仅供流程测试'

def schema():
    return json.loads((BASE / 'questionnaire.json').read_text(encoding='utf-8'))

def write_csv(path, rows, fields=None):
    with path.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields or list(rows[0]))
        w.writeheader()
        w.writerows(rows)

def parse(value, q):
    s = str(value).strip()
    if not s:
        return []
    # 优先完整匹配选项，避免选项内部的中文标点被切分。
    lookup = {}
    for k, label in q['options'].items():
        for form in (k, label, f'{k}. {label}', f'{k}.{label}', f'{k}、{label}'):
            lookup[form] = k
    if s in lookup:
        return [lookup[s]]
    tokens = re.split(r'[;；|┋\n]+', s)
    result = []
    for token in tokens:
        token = token.strip()
        if token not in lookup:
            raise ValueError('未知选项或未配置的多选分隔形式：' + token)
        result.append(lookup[token])
    return result

def validate(row, questions):
    answers, errors = {}, []
    for q in questions:
        key = q['id']
        if q['type'] == 'text':
            answers[key] = row.get(key, '').strip()
            continue
        try:
            answers[key] = parse(row.get(key, ''), q)
        except ValueError as e:
            answers[key] = []
            errors.append(f'{key}: {e}')
    for q in questions:
        key = q['id']
        if q['type'] == 'text':
            continue
        a = answers[key]
        if not a:
            errors.append(f'{key}: 必答题缺失')
        if len(a) != len(set(a)):
            errors.append(f'{key}: 重复选择')
        if len(a) > q['max']:
            errors.append(f'{key}: 超过最多{q["max"]}项')
        if q.get('exclusive') in a and len(a) > 1:
            errors.append(f'{key}: 互斥项与其他项并选')
        other = row.get(key+'_other', '').strip()
        if q.get('other') in a and not other:
            errors.append(f'{key}: 其他选项未填写说明')
        if other and q.get('other') not in a:
            errors.append(f'{key}: 未选其他但有说明')
    return ('invalid' if errors else 'inexperienced' if answers['Q1'] == ['D'] else 'creator'), answers, errors

def generate(output):
    rng = random.Random(20261017)
    questions = schema()['questions']
    rows = []
    # 所有受访者填写全部必答题；固定种子仅保证流程可复现。
    for i in range(30):
        row = {'record_id': f'SIM-{i+1:03}', 'data_origin': SIM}
        for q in questions:
            key = q['id']
            row[key] = ''
            if q.get('other'):
                row[key+'_other'] = ''
            if q['type'] == 'text':
                row[key] = f'{SIM}：开放题示例，不代表用户意见。' if i % 3 == 0 else ''
                continue
            pool = list(q['options'])
            first = rng.choice(pool)
            if q['type'] == 'single' or first == q.get('exclusive'):
                choices = [first]
            else:
                pool = [c for c in pool if c != q.get('exclusive')]
                n = rng.randint(1, min(q['max'], len(pool)))
                choices = [first] + rng.sample([c for c in pool if c != first], n-1)
            row[key] = ';'.join(sorted(choices))
            if q.get('other') in choices:
                row[key+'_other'] = f'{SIM}：其他选项填空校验示例。'
        rows.append(row)
    assert all(validate(r, questions)[0] != 'invalid' for r in rows)
    write_csv(output, rows)

def load_rows(path, mapping_path=None, sheet=0):
    import pandas as pd
    if path.suffix.lower() == '.csv':
        df = pd.read_csv(path, dtype=str, keep_default_na=False, encoding='utf-8-sig')
    elif path.suffix.lower() == '.xlsx':
        df = pd.read_excel(path, sheet_name=sheet, dtype=str, keep_default_na=False)
    else:
        raise ValueError('仅支持UTF-8 CSV和.xlsx；旧.xls请另存为.xlsx，保留原件。')
    config = json.loads(mapping_path.read_text(encoding='utf-8')) if mapping_path else {}
    mapping = config.get('columns', {})
    rows = []
    for index, source in enumerate(df.to_dict('records'), 2):
        row = {'record_id': f'ROW-{index}', 'data_origin': str(source.get('data_origin', ''))}
        for q in schema()['questions']:
            for key in [q['id']] + ([q['id']+'_other'] if q.get('other') else []):
                spec = mapping.get(key, key)
                if isinstance(spec, dict):
                    # 问卷星多选拆列：映射选项编码到原始列名；正负值明确配置。
                    yes = [str(x) for x in spec.get('selected_values', ['1'])]
                    no = [str(x) for x in spec.get('unselected_values', ['0', ''])]
                    picked = []
                    for code, column in spec['option_columns'].items():
                        if column not in source:
                            raise ValueError(f'映射列不存在：{column}')
                        value = str(source[column]).strip()
                        if value in yes:
                            picked.append(code)
                        elif value not in no:
                            raise ValueError(f'第{index}行{column}非配置的二值：{value}')
                    row[key] = ';'.join(picked)
                else:
                    if spec not in source:
                        if key.endswith('_other'):
                            row[key] = ''
                            continue
                        raise ValueError(f'缺少列：{spec}。请配置mapping.json，不猜测列顺序。')
                    value = str(source[spec]).strip()
                    row[key] = config.get('value_maps', {}).get(key, {}).get(value, value)
        rows.append(row)
    return rows

def analyze(path, out, mode, mapping=None, sheet=0):
    rows = load_rows(path, mapping, sheet)
    if mode == 'real' and any(SIM in str(v) or 'SIM-' in str(v) for r in rows for v in r.values()):
        raise ValueError('发现模拟标识，禁止作为真实数据分析。')
    out.mkdir(parents=True, exist_ok=False)
    label = SIM if mode == 'simulation' else '真实导入数据：结果需人工核查'
    questions = schema()['questions']
    checked = [validate(r, questions) for r in rows]
    counts = {s: sum(c[0] == s for c in checked) for s in ('creator', 'inexperienced', 'invalid')}
    audit = [{'数据性质': label, '原始行': i+2, '分类': c[0], '问题': '；'.join(c[2])} for i,c in enumerate(checked)]
    write_csv(out/'validation.csv', audit, ['数据性质','原始行','分类','问题'])
    stats, summary, texts = [], [], []
    groups = {'全体有效受访者': ('creator','inexperienced'), '有创作经历（A/B/C）': ('creator',), '无创作经历（D）': ('inexperienced',)}
    for group, members in groups.items():
        for q in questions:
            key = q['id']
            eligible = [c[1][key] for c in checked if c[0] in members]
            valid = [a for a in eligible if a]
            n = len(valid)
            summary.append({'数据性质':label,'群体':group,'题号':key,'题目':q['title'],'符合答题条件人数':len(eligible),'有效答题人数':n,'选填未答人数':len(eligible)-n,'整卷无效排除人数':counts['invalid']})
            if q['type'] == 'text':
                for i,c in enumerate(checked):
                    if c[0] in members and c[1][key]:
                        texts.append({'数据性质':label,'群体':group,'原始行':i+2,'题号':key,'文本':c[1][key]})
                for name, num in [('已填写',n),('未填写',len(eligible)-n)]:
                    stats.append({'数据性质':label,'群体':group,'题号':key,'编码':'','选项':name,'频数':num,'有效答题人数':n,'百分比分母':len(eligible),'百分比':round(100*num/len(eligible),2) if eligible else ''})
            else:
                for code, name in q['options'].items():
                    num = sum(code in a for a in valid)
                    stats.append({'数据性质':label,'群体':group,'题号':key,'编码':code,'选项':name,'频数':num,'有效答题人数':n,'百分比分母':n,'百分比':round(100*num/n,2) if n else ''})
                if q.get('other'):
                    for i,(r,c) in enumerate(zip(rows, checked)):
                        if c[0] in members and r.get(key+'_other'):
                            texts.append({'数据性质':label,'群体':group,'原始行':i+2,'题号':key+'_other','文本':r[key+'_other']})
    write_csv(out/'statistics.csv', stats)
    write_csv(out/'question_counts.csv', summary)
    write_csv(out/'open_text.csv', texts, ['数据性质','群体','原始行','题号','文本'])
    from PIL import Image, ImageDraw, ImageFont
    from xml.sax.saxutils import escape
    font_path = Path('C:/Windows/Fonts/simsun.ttc')
    if not font_path.exists():
        raise FileNotFoundError('请将图表font_path改为本机可用中文字体路径')
    for key in ['Q4','Q8','Q12']:
        chart_group = '有创作经历（A/B/C）' if key == 'Q4' else '全体有效受访者'
        entries = [s for s in stats if s['题号'] == key and s['群体'] == chart_group]
        width, height, scale = 1400, 820, 2
        im = Image.new('RGB',(width*scale,height*scale),'white')
        draw = ImageDraw.Draw(im)
        svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">', '<rect width="100%" height="100%" fill="white"/>']
        def text(x,y,t,size=25,center=False):
            font=ImageFont.truetype(str(font_path),size*scale)
            draw.text((x*scale,y*scale),t,font=font,fill='black',anchor='mm' if center else 'lm')
            svg.append(f'<text x="{x}" y="{y}" font-family="SimSun,serif" font-size="{size}" dominant-baseline="central" text-anchor="{"middle" if center else "start"}">{escape(t)}</text>')
        def line(x1,y1,x2,y2):
            draw.line((x1*scale,y1*scale,x2*scale,y2*scale),fill='black',width=2)
            svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="black"/>')
        text(700,35,f'{key} 选项分布｜{chart_group}',32,True)
        text(700,80,label,30,True)
        maximum=max([s['频数'] for s in entries]+[1])
        left,plotwidth=750,450
        for i,s in enumerate(entries):
            y=150+i*65
            text(20,y,s['编码']+'. '+s['选项'])
            w=plotwidth*s['频数']/maximum
            if w:
                draw.rectangle((left*scale,(y-19)*scale,(left+w)*scale,(y+19)*scale),fill='#cccccc',outline='black',width=2)
                svg.append(f'<rect x="{left}" y="{y-19}" width="{w}" height="38" fill="#ccc" stroke="black"/>')
            pct=str(s['百分比'])+'%' if s['百分比']!='' else '不适用'
            text(left+w+10,y,f'{s["频数"]}（{pct}）',23)
        bottom=150+(len(entries)-1)*65+35
        line(left,120,left,bottom)
        line(left,bottom,left+plotwidth,bottom)
        for val in sorted(set([0,maximum//2,maximum])):
            x=left+plotwidth*val/maximum
            line(x,bottom,x,bottom+7)
            text(x,bottom+25,str(val),22,True)
        text(left+plotwidth/2,bottom+60,'选择人数（人）',24,True)
        text(700,760,f'{label}；有效答题人数 n={entries[0]["有效答题人数"]}',25,True)
        text(700,795,'百分比分母为本题有效答题人数；多选百分比合计可超过100%。',24,True)
        im.save(out/f'{key}.png',dpi=(300,300))
        (out/f'{key}.svg').write_text('\n'.join(svg+['</svg>']),encoding='utf-8')
    manifest = {'标识':label,'总答卷':len(rows),'有效创作者答卷':counts['creator'],'有效无创作经历答卷':counts['inexperienced'],'有效答卷':counts['creator']+counts['inexperienced'],'无效答卷':counts['invalid'],'输入SHA256':hashlib.sha256(path.read_bytes()).hexdigest(),'schemaSHA256':hashlib.sha256((BASE/'questionnaire.json').read_bytes()).hexdigest(),'scriptSHA256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'规则':'所有人回答Q1—14；Q15选填；整卷校验；各题按全体有效、A/B/C、D分别统计；无数据百分比留空。'}
    (out/'run_summary.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    (out/'RESULTS.md').write_text('# '+label+'\n\n'+json.dumps(manifest,ensure_ascii=False,indent=2)+'\n\n统计为描述性频数，不作人群推断、因果判断或系统有效性证明。模拟分布无研究意义。开放题保留原文，不自动编造主题频数。\n',encoding='utf-8')
    print(json.dumps(manifest,ensure_ascii=False))

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest='command',required=True)
    g = sub.add_parser('simulate')
    g.add_argument('--output',type=Path,default=BASE/'SIMULATED_30.csv')
    a = sub.add_parser('analyze')
    a.add_argument('--input',type=Path,required=True)
    a.add_argument('--output',type=Path,required=True)
    a.add_argument('--mode',choices=['simulation','real'],required=True)
    a.add_argument('--mapping',type=Path)
    a.add_argument('--sheet',default='0')
    args = p.parse_args()
    if args.command == 'simulate':
        if args.output.exists():
            raise FileExistsError('不覆盖现有模拟原始数据')
        generate(args.output)
    else:
        analyze(args.input,args.output,args.mode,args.mapping,int(args.sheet) if args.sheet.isdigit() else args.sheet)
