"""合成边界用例，仅验证程序，不是额外调查答卷。"""
import csv
import copy
import tempfile
from pathlib import Path
import pandas as pd
from analyze import BASE, schema, validate, load_rows, parse

qs = schema()['questions']
with (BASE/'SIMULATED_30.csv').open(encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 30
assert all(validate(r,qs)[0] != 'invalid' for r in rows)
assert any(r['Q1']=='D' for r in rows)
assert all(all(r[f'Q{i}'] for i in range(1,15)) for r in rows)
base = rows[3]
checks = 0
for key,value in [('Q6','A;B;C;D'),('Q8','G;A'),('Q9','F;B'),('Q1','A;B'),('Q4','A;A'),('Q12','Z'),('Q2','')]:
    row=copy.deepcopy(base)
    row[key]=value
    assert validate(row,qs)[0]=='invalid',(key,value)
    checks+=1
row=copy.deepcopy(base); row['Q1']='D'
assert validate(row,qs)[0]=='inexperienced'; checks+=1
row['Q15']='合法的选填文本'
assert validate(row,qs)[0]=='inexperienced'; checks+=1
row['Q2']=''
assert validate(row,qs)[0]=='invalid'; checks+=1
row=copy.deepcopy(base); row['Q2']='G'; row['Q2_other']=''
assert validate(row,qs)[0]=='invalid'; checks+=1
assert parse('A┋B',qs[3])==['A','B']; checks+=1
assert parse(qs[3]['options']['A'],qs[3])==['A']; checks+=1
# 实测.xlsx读取路径，不将导入测试文件保存为调查数据。
with tempfile.TemporaryDirectory(dir=BASE) as tmp:
    file=Path(tmp)/'fixture.xlsx'
    pd.DataFrame(rows).to_excel(file,index=False)
    imported=load_rows(file)
    assert [validate(r,qs)[0] for r in imported]==[validate(r,qs)[0] for r in rows]
    checks+=1
with (BASE/'simulation_results/statistics.csv').open(encoding='utf-8-sig') as f:
    stats=list(csv.DictReader(f))
for group,pool in [('全体有效受访者',rows),('有创作经历（A/B/C）',[r for r in rows if r['Q1']!='D']),('无创作经历（D）',[r for r in rows if r['Q1']=='D'])]:
    for q in qs[:-1]:
        values=[s for s in stats if s['题号']==q['id'] and s['群体']==group]
        assert len(values)==len(q['options'])
        for s in values:
            n=sum(s['编码'] in r[q['id']].split(';') for r in pool)
            assert int(s['频数'])==n
            assert int(s['百分比分母'])==len(pool)
            assert float(s['百分比'])==round(n/len(pool)*100,2)
        if q['type']=='single':assert sum(int(s['频数']) for s in values)==len(pool)
    values=[s for s in stats if s['题号']=='Q15' and s['群体']==group]
    assert sum(int(s['频数']) for s in values)==len(pool)
    assert int(values[0]['有效答题人数'])==sum(bool(r['Q15']) for r in pool)
for q in qs[:-1]:
    for code in q['options']:
        v=[s for s in stats if s['题号']==q['id'] and s['编码']==code]
        assert int(v[0]['频数'])==sum(int(s['频数']) for s in v[1:])
print(f'PASS: {checks} boundary/import checks; all three groups, frequencies and denominators reconciled.')
