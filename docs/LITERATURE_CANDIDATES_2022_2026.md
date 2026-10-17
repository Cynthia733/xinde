# 2022—2026 年候选文献检索与题录核验记录

论文题目：《基于 Spring Boot + Vue 大语言模型的小说智能辅助创作系统设计与实现》

## 1. 本轮范围与证据边界

- 检索与核验日期：**2026-09-10**。时间窗口严格为 **2022-01-01—2026-09-10**，覆盖本轮所有方向；不沿用研究规划中允许追溯更早文献的例外。
- 工作依据：已完整阅读 [PROJECT_CONTEXT.md](../PROJECT_CONTEXT.md) 和 [RESEARCH_PLAN.md](RESEARCH_PLAN.md)，遵循当前 v1.3 基线。本文件是阶段1的候选资料，不是最终参考文献表、完成的文献综述或论文正文。
- 使用 ARS-Codex academic-research-suite 的检索、题录核验和证据边界方法。执行公开网络检索、官方论文页读取与 Crossref 元数据查询；没有运行模型实验、用户实验或系统代码审计。
- 纳入 **30篇不重复论文：27篇英文、3篇中文**。同一工作的预印本和正式版本只计一篇。正式会议论文优先采用正式年份和题名；只有预印本确认的，明确标为预印本。2026年仅纳入官方页面已经公开且标明7月的 L17。
- “已核验”指题名、作者、年份、来源及存在的 DOI 已通过下述可靠来源核对，**不等于已完成全文精读或已复现实验**。研究问题、方法、结论是依据官方摘要及部分可读全文所做的简要提取；后续精读必须补充页码、方法细节和限制。
- 每篇的“与本论文的关系”“具体支撑内容”和“使用注意”是针对本项目的研究判断，不是原论文直接评价本系统的结论。建议章节仅用于定位，尚未冻结最终目录。
- 英文论文中文译题为工作译名；中文论文保留中文原题，不把自译英文冒充官方英文原题。未发现 DOI 仅表示本轮可靠记录中未发现，不断言永远不存在。
- 提供 DOI 和公开全文两个入口。ACM、Science 部分页面直访受限，已通过 **Crossref官方API**核验正式题录，并提供 arXiv、PMC或作者全文替代入口。L02全文为已打开并核对首页的第三方PDF镜像；其真实性另由Crossref核验。
- 中文期刊官网题录和摘要可访问，但三篇全文均未取得；明确保留为“题录核验通过、全文待获取”的候选，不声称开放全文。OpenReview直访遇浏览器验证，相关会议论文通过arXiv原页核验，并保留版本限制。链接访问状态反映本次环境，不能承诺所有网络环境均无登录或地区限制。

### 1.1 与需求基线的对应

研究主线仍是“结构化作品资料 → 六类 Writing Skill 组织任务和上下文 → 作者确认候选 → 工程与AI评价”。六类任务为大纲规划、人物塑造、情节构思、上下文续写、文本润色、一致性检查。

- D1、D2、D3、D4、D6重点服务RQ2/RQ3及作者交互部分；D5、D8服务RQ1/RQ4的工程论证。
- 音乐、禅模式、计划、签到、灵石、兑换、装扮、拼字与行业趋势仍属于正式系统范围。文献缺口不删减功能；论文未证明某项效果，也不意味着不能实现该功能。
- 文献中的知识图谱、微调、代码执行、视觉编排或完整自动生成只作为相关工作，不转为本项目新需求。RAG、向量库、MCP、多Agent、同步协议、奖励参数、行业采集平台及Prompt联动细节均不因本轮检索被确定。
- 写作助手文献不能证明Spring Boot/Vue架构最优；叙事一致性与数据库事务一致性属于不同问题，不混用同一个“一致性”概念。

## 2. 实际检索与筛选记录

### 2.1 方法

先用中英文主题组合发现工作，再按精确题名查找官方页面；通过ACL、arXiv、期刊官网或Crossref核对完整题录。ACM相关正式记录采用 `https://api.crossref.org/works/{DOI}` 查询，DOI来自已发现记录，未依据题名猜测。检索摘要只用于发现；只有取得可靠题录记录的论文才进入下列候选。

这是**第一轮定向检索**，不是穷尽式系统综述。未记录可重复的全部搜索引擎命中数，因此不编造命中量、排除数量或PRISMA计数。以下为本轮执行过的代表性检索及跟进方向，不是未执行的关键词建议。

| 方向 | 已执行的检索示例/精确题名跟进 | 本轮结果与处理 |
|---|---|---|
| D1 | `human AI co-writing creative writing 2022 2023 2024`；`Wordcraft Story Writing With Large Language Models`；`CoAuthor`；`professional writers AI writing assistant` | 找到协同写作系统、专业作家访谈和设计空间；用Crossref/arXiv/ACL核验 |
| D2 | `long form story generation outline memory`；`Re3`；`DOC Improving Long Story Coherence`；`DOME story generation` | 获得长篇规划、动态记忆、上下文位置和长摘要研究 |
| D3 | `structured prompting story understanding`；`PromptChainer`；`CoEdIT`；`CoRRPUS` | 分清提示编排、结构化推理与指令微调，限制迁移结论 |
| D4 | `narrative consistency plot hole detection LLM`；`Lost in Stories`；`Finding Flawed Fictions`；`SNaC` | 获得情节漏洞、长故事缺陷及叙事摘要错误研究 |
| D6 | `story generation human evaluation benchmark`；`HANNA`；`STORYSUMM`；`FABLES`；`BooookScore`；`Do Language Models Enjoy Their Own Stories` | 获得人工维度、摘要忠实性与模型评分边界文献 |
| D5 | `"writing" "system" "Spring Boot" "2024"`；`"document editing" "data management" 2022` | 结果包括技术博客及非创作场景文章；本轮未找到足够合适文献 |
| D7 | `gamification creative writing goal feedback 2022`；`"gamification" "creative writing" 2022` | 发现学校写作教学、目标干预等邻近研究，不能直接支撑小说作者的签到灵石或音乐收益，未纳入凑数 |
| D8 | `idempotency reward points transaction consistency 2023 2024 paper`；`"real-time" "state synchronization" 2022` | 返回区块链奖励、支付或网络数字孪生等偏题结果；本轮未找到足够合适文献 |
| D9/中文 | `"网络文学" "题材" "2025" site:cnki.net`；`网络文学 题材 趋势 2024 site:wanfangdata.com.cn`；AI网络文学精确题名跟进 | 核验中文期刊官网的网络文学影响与年度报告解读；不是实时数据源选型 |
| 中文核心补检 | `大语言模型 故事生成 site:jos.org.cn`；`故事生成 大语言模型 2024 site:cqvip.com` | 返回期刊目录、主题或检索入口，未获得足以纳入的具体核心技术论文题录 |

### 2.2 纳入、排除与访问限制

纳入条件：时间合规、可靠题录可核验、对本研究主线有直接价值或明确的必要支撑价值。可接受预印本，但标明证据成熟度；未获得全文的真实中文论文保留候选资格，后续全文筛选可排除。

排除处理：2022年前工作、重复版本、图像/视频人物一致性等不同任务、只有二手摘要而无可靠题录的记录，以及仅因为包含“Spring Boot”“游戏化”“奖励”就看似相关的论文，不列入正式候选。Wordcraft的2021早期版本不另计；2023预印本与2024会议稿等不重复计数。

D7确实检索到教育场景的目标反馈研究，例如出版社页面 [Integrating goal-setting and automated feedback to improve writing outcomes: a pilot study](https://www.tandfonline.com/doi/full/10.1080/17501229.2022.2077348) 和 [Individualizing goal-setting interventions using automated writing evaluation to support secondary school students’ text revisions](https://www.sciencedirect.com/science/article/pii/S0959475223001160)。本轮未完成其完整题录核验且场景迁移较弱，**仅作排除/待扩检线索，不编号、不算正式候选、不作为论据**。音乐及禅模式的直接证据仍需下一轮聚焦补检。

知网期刊官网三篇记录的题名、作者、刊期和摘要可核验，页面提示全文需访问cnki.net；没有据此虚构全文内容。万方、维普本轮未取得可可靠核对的相关具体论文记录；不能推断数据库没有此类论文，也不声称已检索其全部订阅内容。

## 3. 逐篇候选文献

下列链接分别承担题录溯源与全文获取作用。正式 DOI 优先显示；arXiv DOI明确只标识公开预印本版本。没有公开全文的条目不填写虚假PDF地址。

### L01 CoAuthor: Designing a Human-AI Collaborative Writing Dataset for Exploring Language Model Capabilities

- **编号：** L01
- **所属研究方向：** D1、D6
- **相关程度：** 核心

**英文原题：** CoAuthor: Designing a Human-AI Collaborative Writing Dataset for Exploring Language Model Capabilities

**中文译题：** CoAuthor：用于探索语言模型能力的人机协同写作数据集设计

**作者：** Mina Lee; Percy Liang; Qian Yang

**年份：** 2022

**文献类型：** 会议

**期刊或会议：** CHI 2022

**卷(期)/页码：** 1–19

**DOI：** [10.1145/3491102.3502030](https://doi.org/10.1145/3491102.3502030)

**官方链接：** [DOI官方入口](https://doi.org/10.1145/3491102.3502030)；[可靠题录/官方原页](https://arxiv.org/abs/2201.06796)；[Crossref核验记录](https://api.crossref.org/works/10.1145/3491102.3502030)

**公开全文链接：** [公开全文](https://arxiv.org/pdf/2201.06796)

**主要研究问题：** 如何通过真实协作过程理解语言模型的写作辅助能力？

**研究方法：** 采集人机写作会话、模型建议及作者交互，分析协作数据。

**主要结论：** 交互记录提供了仅观察最终文本无法覆盖的模型使用与协作分析视角。

**与我的毕业论文的关系：** 关联作者主导的人机协作及辅助价值评价，服务RQ1/RQ2的交互与评价论证。

**具体可以支撑我论文中的什么内容：** 支撑作者选择、修改、采纳候选的交互设计，以及过程指标和文本指标分开评价。

**建议使用位置：** 第1章研究现状；第4章交互设计；第6章AI功能评价

**使用注意：** 数据集包含不同写作任务；不能用其结果证明本系统提升效率，也不能声称本系统已经采集同等规模数据。

**核验状态：** 题录核验通过。Crossref 核对正式题名、全体作者、2022年、会议、页码及 DOI；arXiv 原页核对版本和公开全文入口。

### L02 Wordcraft: Story Writing With Large Language Models

- **编号：** L02
- **所属研究方向：** D1、D3、D6
- **相关程度：** 核心

**英文原题：** Wordcraft: Story Writing With Large Language Models

**中文译题：** Wordcraft：使用大语言模型进行故事写作

**作者：** Ann Yuan; Andy Coenen; Emily Reif; Daphne Ippolito

**年份：** 2022

**文献类型：** 会议

**期刊或会议：** 27th International Conference on Intelligent User Interfaces（IUI 2022）

**卷(期)/页码：** 841–852

**DOI：** [10.1145/3490099.3511105](https://doi.org/10.1145/3490099.3511105)

**官方链接：** [DOI官方入口](https://doi.org/10.1145/3490099.3511105)；[可靠题录/官方原页](https://dl.acm.org/doi/10.1145/3490099.3511105)；[Crossref核验记录](https://api.crossref.org/works/10.1145/3490099.3511105)

**公开全文链接：** [公开全文](https://3dvar.com/Yuan2022Wordcraft.pdf)

**主要研究问题：** 如何将语言模型融入作者的故事创作与局部编辑？

**研究方法：** 实现编辑器、预设和自然语言自定义请求，并比较短故事写作条件。

**主要结论：** 研究中工具支持灵感、改写与续写；有用建议不一定被原样采纳。

**与我的毕业论文的关系：** 关联Writing Skill的任务化输入、规则与输出组织，服务RQ2。

**具体可以支撑我论文中的什么内容：** 支撑六类 Writing Skill 的任务化入口、候选结果交互和辅助价值评价。

**建议使用位置：** 第1章研究现状；第4章Writing Skill；第6章AI功能评价

**使用注意：** 不能将短故事用户研究推广为长篇小说质量保证。不要与2021年同名早期版本混列。

**核验状态：** 题录核验通过。Crossref 核验正式题名、四位作者、年份、IUI及页码、DOI；可访问PDF首页再次核对。ACM直访受限；全文链接是第三方镜像，非题录核验的唯一依据。

### L03 Creative Writing with an AI-Powered Writing Assistant: Perspectives from Professional Writers

- **编号：** L03
- **所属研究方向：** D1、D6
- **相关程度：** 核心

**英文原题：** Creative Writing with an AI-Powered Writing Assistant: Perspectives from Professional Writers

**中文译题：** 使用AI写作助手进行创意写作：专业作家的视角

**作者：** Daphne Ippolito; Ann Yuan; Andy Coenen; Sehmon Burnam

**年份：** 2022

**文献类型：** 预印本

**期刊或会议：** arXiv:2211.05030

**卷(期)/页码：** 无/不适用

**DOI：** [10.48550/arXiv.2211.05030](https://doi.org/10.48550/arXiv.2211.05030)（arXiv版本DOI）

**官方链接：** [可靠题录/官方原页](https://arxiv.org/abs/2211.05030)

**公开全文链接：** [公开全文](https://arxiv.org/pdf/2211.05030)

**主要研究问题：** 专业作家如何使用并评价AI写作助手？

**研究方法：** 让专业作家使用Wordcraft，结合访谈和使用记录分析体验。

**主要结论：** 工具可辅助构思和细节探索，但文风、作者意图及深层故事理解仍构成限制。

**与我的毕业论文的关系：** 关联作者主导的人机协作及辅助价值评价，服务RQ1/RQ2的交互与评价论证。

**具体可以支撑我论文中的什么内容：** 支撑作者主导定位、保留人工修改，以及评价中纳入可用性与创作控制感。

**建议使用位置：** 第1章研究现状；第4章交互设计；第6章AI功能评价

**使用注意：** 属于预印本，未核实后续正式发表；访谈结论不能等同于随机实验的因果效果。

**核验状态：** 题录核验通过。arXiv原页核验题名、作者、2022-11-09首次提交和arXiv DOI；未将未核实会议补入题录。

### L04 Co-Writing Screenplays and Theatre Scripts with Language Models: Evaluation by Industry Professionals

- **编号：** L04
- **所属研究方向：** D1、D2、D6
- **相关程度：** 核心

**英文原题：** Co-Writing Screenplays and Theatre Scripts with Language Models: Evaluation by Industry Professionals

**中文译题：** 与语言模型协同创作影视及戏剧剧本：行业专业人士评价

**作者：** Piotr Mirowski; Kory W. Mathewson; Jaylen Pittman; Richard Evans

**年份：** 2023

**文献类型：** 会议

**期刊或会议：** CHI 2023

**卷(期)/页码：** 1–34

**DOI：** [10.1145/3544548.3581225](https://doi.org/10.1145/3544548.3581225)

**官方链接：** [DOI官方入口](https://doi.org/10.1145/3544548.3581225)；[可靠题录/官方原页](https://arxiv.org/abs/2209.14958)；[Crossref核验记录](https://api.crossref.org/works/10.1145/3544548.3581225)

**公开全文链接：** [公开全文](https://arxiv.org/pdf/2209.14958)

**主要研究问题：** 层次化生成如何支持专业剧本创作？

**研究方法：** Dramatron分层组织故事元素，结合专业人士协作体验和访谈。

**主要结论：** 系统展示了层次化协作的用途，同时暴露编辑需求和创作控制等局限。

**与我的毕业论文的关系：** 关联大纲、上下文与章节记忆组织，服务RQ2的任务和输入设计。

**具体可以支撑我论文中的什么内容：** 支撑大纲、人物等创作资料在生成前组织，以及专业反馈式评价。

**建议使用位置：** 第1章研究现状；第4章上下文组织；第6章AI功能评价

**使用注意：** 剧本不同于中文小说；不能承诺自动生成可发表作品。预印本2022年，正式会议2023年，仅计一篇。

**核验状态：** 题录核验通过。Crossref核验2023正式题名、作者、会议、页码和DOI；arXiv核验公开版本。预印本标题含“An Evaluation”，正式题名无An，本文按正式记录。

### L05 Unmet Creativity Support Needs in Computationally Supported Creative Writing

- **编号：** L05
- **所属研究方向：** D1
- **相关程度：** 重要支撑

**英文原题：** Unmet Creativity Support Needs in Computationally Supported Creative Writing

**中文译题：** 计算机支持的创意写作中尚未满足的创作支持需求

**作者：** Max Kreminski; Chris Martens

**年份：** 2022

**文献类型：** 会议研讨会

**期刊或会议：** First Workshop on Intelligent and Interactive Writing Assistants（In2Writing 2022）

**卷(期)/页码：** 74–82

**DOI：** [10.18653/v1/2022.in2writing-1.11](https://doi.org/10.18653/v1/2022.in2writing-1.11)

**官方链接：** [DOI官方入口](https://doi.org/10.18653/v1/2022.in2writing-1.11)；[可靠题录/官方原页](https://aclanthology.org/2022.in2writing-1.11/)

**公开全文链接：** [公开全文](https://aclanthology.org/2022.in2writing-1.11.pdf)

**主要研究问题：** 现有工具还遗漏哪些创作支持需求？

**研究方法：** 结合创作相关理论与计算叙事工具讨论需求。

**主要结论：** 创作支持需要关注一致性、情节、读者体验和表达意图，而不限于克服写作阻塞。

**与我的毕业论文的关系：** 关联作者主导的人机协作及辅助价值评价，服务RQ1/RQ2的交互与评价论证。

**具体可以支撑我论文中的什么内容：** 支撑把功能需求转化为作者控制、叙事约束等研究问题。

**建议使用位置：** 第1章研究背景与研究现状

**使用注意：** 观点与需求分析不能证明任何具体功能的效果；不得据此增添基线外功能。

**核验状态：** 题录核验通过。ACL Anthology页面核验题名、作者、年份、会议、页码及DOI；已查看摘要，未完成全文精读。

### L06 A Design Space for Intelligent and Interactive Writing Assistants

- **编号：** L06
- **所属研究方向：** D1、D6
- **相关程度：** 重要支撑

**英文原题：** A Design Space for Intelligent and Interactive Writing Assistants

**中文译题：** 智能交互式写作助手的设计空间

**作者：** Mina Lee; Katy Ilonka Gero; John Joon Young Chung; Simon Buckingham Shum; Vipul Raheja; Hua Shen; Subhashini Venugopalan; Thiemo Wambsganss; David Zhou; Emad A. Alghamdi; Tal August; Avinash Bhat; Madiha Zahrah Choksi; Senjuti Dutta; Jin L.C. Guo; Md Naimul Hoque; Yewon Kim; Simon Knight; Seyed Parsa Neshaei; Antonette Shibani; Disha Shrivastava; Lila Shroff; Agnia Sergeyuk; Jessi Stark; Sarah Sterman; Sitong Wang; Antoine Bosselut; Daniel Buschek; Joseph Chee Chang; Sherol Chen; Max Kreminski; Joonsuk Park; Roy Pea; Eugenia Ha Rim Rho; Zejiang Shen; Pao Siangliulue

**年份：** 2024

**文献类型：** 会议

**期刊或会议：** CHI 2024

**卷(期)/页码：** 1–35

**DOI：** [10.1145/3613904.3642697](https://doi.org/10.1145/3613904.3642697)

**官方链接：** [DOI官方入口](https://doi.org/10.1145/3613904.3642697)；[可靠题录/官方原页](https://arxiv.org/abs/2403.14117)；[Crossref核验记录](https://api.crossref.org/works/10.1145/3613904.3642697)

**公开全文链接：** [公开全文](https://arxiv.org/pdf/2403.14117)

**主要研究问题：** 如何系统描述和比较写作助手的设计选择？

**研究方法：** 综述写作助手研究，从任务、用户、技术、交互和生态等方面构建设计空间。

**主要结论：** 提供跨系统比较与发现研究空白的分类框架。

**与我的毕业论文的关系：** 关联作者主导的人机协作及辅助价值评价，服务RQ1/RQ2的交互与评价论证。

**具体可以支撑我论文中的什么内容：** 支撑相关工作比较表和本系统的目标作者、辅助范围及交互定位。

**建议使用位置：** 第1章研究现状；第3章需求分析

**使用注意：** 分类框架不是某种架构或交互优于其他方案的实验证据。

**核验状态：** 题录核验通过。Crossref核验正式作者顺序、题名、2024年、会议页码和DOI；arXiv核验公开版本。作者姓名及顺序按正式Crossref记录，未混用预印本差异。

### L07 TaleBrush: Sketching Stories with Generative Pretrained Language Models

- **编号：** L07
- **所属研究方向：** D1、D3
- **相关程度：** 重要支撑

**英文原题：** TaleBrush: Sketching Stories with Generative Pretrained Language Models

**中文译题：** TaleBrush：通过草图控制生成式预训练语言模型的故事创作

**作者：** John Joon Young Chung; Wooseok Kim; Kang Min Yoo; Hwaran Lee; Eytan Adar; Minsuk Chang

**年份：** 2022

**文献类型：** 会议

**期刊或会议：** CHI 2022

**卷(期)/页码：** 1–19

**DOI：** [10.1145/3491102.3501819](https://doi.org/10.1145/3491102.3501819)

**官方链接：** [DOI官方入口](https://doi.org/10.1145/3491102.3501819)；[可靠题录/官方原页](https://dl.acm.org/doi/10.1145/3491102.3501819)；[Crossref核验记录](https://api.crossref.org/works/10.1145/3491102.3501819)

**公开全文链接：** [公开全文](https://johnr0.github.io/assets/publications/CHI2022-TaleBrush.pdf)

**主要研究问题：** 作者如何直观控制故事发展？

**研究方法：** 以绘制主人公境遇曲线的交互控制故事生成，并开展用户研究。

**主要结论：** 展示了作者控制信号与模型生成结合的创作方式。

**与我的毕业论文的关系：** 关联Writing Skill的任务化输入、规则与输出组织，服务RQ2。

**具体可以支撑我论文中的什么内容：** 支撑可控生成和明确任务约束的设计动机。

**建议使用位置：** 第1章研究现状；第4章Writing Skill

**使用注意：** 草图是该文特定交互，本系统不因此新增曲线绘图功能；不据此保证文本提示效果相同。

**核验状态：** 题录核验通过。Crossref核验题名、全体作者、年份、CHI页码及DOI；作者托管公开PDF可访问并核对首页，ACM直访受限。

### L08 Re3: Generating Longer Stories With Recursive Reprompting and Revision

- **编号：** L08
- **所属研究方向：** D2、D3、D4
- **相关程度：** 核心

**英文原题：** Re3: Generating Longer Stories With Recursive Reprompting and Revision

**中文译题：** Re3：通过递归重提示与修订生成更长的故事

**作者：** Kevin Yang; Yuandong Tian; Nanyun Peng; Dan Klein

**年份：** 2022

**文献类型：** 会议

**期刊或会议：** EMNLP 2022

**卷(期)/页码：** 4393–4479

**DOI：** [10.18653/v1/2022.emnlp-main.296](https://doi.org/10.18653/v1/2022.emnlp-main.296)

**官方链接：** [DOI官方入口](https://doi.org/10.18653/v1/2022.emnlp-main.296)；[可靠题录/官方原页](https://aclanthology.org/2022.emnlp-main.296/)

**公开全文链接：** [公开全文](https://aclanthology.org/2022.emnlp-main.296.pdf)

**主要研究问题：** 长故事生成如何持续遵循总体计划和既有内容？

**研究方法：** 结构化计划、反复注入当前状态、候选重排序与事实修订。

**主要结论：** 在其人评条件下，较直接生成改善长故事连贯性和前提相关性。

**与我的毕业论文的关系：** 关联结构化创作资料、叙事约束和一致性检查，是RQ2/RQ3的相关研究依据。

**具体可以支撑我论文中的什么内容：** 支撑续写时组合大纲、已有内容与约束；为上下文消融比较提供思路。

**建议使用位置：** 第4章上下文组织；第6章AI功能评价

**使用注意：** 整体框架含排序和修订，不能把全部收益归于一条提示；无需照搬所有组件。页码按官方记录保留。

**核验状态：** 题录核验通过。ACL Anthology官方页核验题名、全体作者、年份、刊会、页码及DOI，并提供公开PDF；研究信息依据官方摘要，尚未完成全文精读。

### L09 DOC: Improving Long Story Coherence With Detailed Outline Control

- **编号：** L09
- **所属研究方向：** D2、D3、D4
- **相关程度：** 核心

**英文原题：** DOC: Improving Long Story Coherence With Detailed Outline Control

**中文译题：** DOC：通过详细大纲控制改善长故事连贯性

**作者：** Kevin Yang; Dan Klein; Nanyun Peng; Yuandong Tian

**年份：** 2023

**文献类型：** 会议

**期刊或会议：** ACL 2023，Volume 1: Long Papers

**卷(期)/页码：** 3378–3465

**DOI：** [10.18653/v1/2023.acl-long.190](https://doi.org/10.18653/v1/2023.acl-long.190)

**官方链接：** [DOI官方入口](https://doi.org/10.18653/v1/2023.acl-long.190)；[可靠题录/官方原页](https://aclanthology.org/2023.acl-long.190/)

**公开全文链接：** [公开全文](https://aclanthology.org/2023.acl-long.190.pdf)

**主要研究问题：** 更细的大纲及生成控制能否改善长故事？

**研究方法：** 层次化详细大纲生成器与段落生成控制器，和Re3比较并开展人评。

**主要结论：** 在所评任务中改善连贯性、相关性及趣味性。

**与我的毕业论文的关系：** 关联结构化创作资料、叙事约束和一致性检查，是RQ2/RQ3的相关研究依据。

**具体可以支撑我论文中的什么内容：** 支撑章节目标与细分情节作为续写约束，并比较不同大纲粒度。

**建议使用位置：** 第4章Writing Skill及上下文组织；第6章AI功能评价

**使用注意：** 全文自动生成任务不同于作者逐章续写；其性能不是本系统测试结果。页码按官方记录保留。

**核验状态：** 题录核验通过。ACL Anthology官方页核验题名、全体作者、年份、刊会、页码及DOI，并提供公开PDF；研究信息依据官方摘要，尚未完成全文精读。

### L10 Generating Long-form Story Using Dynamic Hierarchical Outlining with Memory-Enhancement

- **编号：** L10
- **所属研究方向：** D2、D4
- **相关程度：** 核心

**英文原题：** Generating Long-form Story Using Dynamic Hierarchical Outlining with Memory-Enhancement

**中文译题：** 利用记忆增强的动态层次化大纲生成长篇故事

**作者：** Qianyue Wang; Jinwu Hu; Zhengping Li; Yufeng Wang; Daiyuan Li; Yu Hu; Mingkui Tan

**年份：** 2025

**文献类型：** 会议

**期刊或会议：** NAACL 2025：Nations of the Americas Chapter，Human Language Technologies，Volume 1: Long Papers

**卷(期)/页码：** 1352–1391

**DOI：** [10.18653/v1/2025.naacl-long.63](https://doi.org/10.18653/v1/2025.naacl-long.63)

**官方链接：** [DOI官方入口](https://doi.org/10.18653/v1/2025.naacl-long.63)；[可靠题录/官方原页](https://aclanthology.org/2025.naacl-long.63/)

**公开全文链接：** [公开全文](https://aclanthology.org/2025.naacl-long.63.pdf)

**主要研究问题：** 静态计划与遗忘问题如何影响长篇生成？

**研究方法：** DOME结合动态层次化大纲、时间知识图谱记忆和时间冲突分析。

**主要结论：** 其评测报告了故事流畅性与连贯性方面的改善。

**与我的毕业论文的关系：** 关联结构化创作资料、叙事约束和一致性检查，是RQ2/RQ3的相关研究依据。

**具体可以支撑我论文中的什么内容：** 支撑区分大纲、角色状态和章节记忆的研究动机，以及时序冲突用例。

**建议使用位置：** 第1章研究现状；第4章上下文组织；第6章AI功能评价

**使用注意：** 知识图谱是该文方法，不是本系统既定功能；不得据此增加图数据库或声称已复现DOME。

**核验状态：** 题录核验通过。ACL Anthology官方页核验题名、全体作者、年份、刊会、页码及DOI，并提供公开PDF；研究信息依据官方摘要，尚未完成全文精读。

### L11 Creating Suspenseful Stories: Iterative Planning with Large Language Models

- **编号：** L11
- **所属研究方向：** D2、D3
- **相关程度：** 重要支撑

**英文原题：** Creating Suspenseful Stories: Iterative Planning with Large Language Models

**中文译题：** 使用大语言模型迭代规划创作悬念故事

**作者：** Kaige Xie; Mark Riedl

**年份：** 2024

**文献类型：** 会议

**期刊或会议：** EACL 2024，Volume 1: Long Papers

**卷(期)/页码：** 2391–2407

**DOI：** [10.18653/v1/2024.eacl-long.147](https://doi.org/10.18653/v1/2024.eacl-long.147)

**官方链接：** [DOI官方入口](https://doi.org/10.18653/v1/2024.eacl-long.147)；[可靠题录/官方原页](https://aclanthology.org/2024.eacl-long.147/)

**公开全文链接：** [公开全文](https://aclanthology.org/2024.eacl-long.147.pdf)

**主要研究问题：** 如何通过规划让生成故事形成悬念？

**研究方法：** 依据叙事与认知思路进行零样本迭代规划，结合人工评价。

**主要结论：** 在其条件下增强故事悬念体验。

**与我的毕业论文的关系：** 关联大纲、上下文与章节记忆组织，服务RQ2的任务和输入设计。

**具体可以支撑我论文中的什么内容：** 支撑情节相关Skill使用明确叙事目标及规划步骤。

**建议使用位置：** 第4章Writing Skill；第6章AI功能评价

**使用注意：** 悬念只是叙事目标之一，不得新增第七个Skill，也不能推广到所有题材。

**核验状态：** 题录核验通过。ACL Anthology官方页核验题名、全体作者、年份、刊会、页码及DOI，并提供公开PDF；研究信息依据官方摘要，尚未完成全文精读。

### L12 MoPS: Modular Story Premise Synthesis for Open-Ended Automatic Story Generation

- **编号：** L12
- **所属研究方向：** D2、D3
- **相关程度：** 重要支撑

**英文原题：** MoPS: Modular Story Premise Synthesis for Open-Ended Automatic Story Generation

**中文译题：** MoPS：面向开放式自动故事生成的模块化故事前提合成

**作者：** Yan Ma; Yu Qiao; Pengfei Liu

**年份：** 2024

**文献类型：** 会议

**期刊或会议：** ACL 2024，Volume 1: Long Papers

**卷(期)/页码：** 2135–2169

**DOI：** [10.18653/v1/2024.acl-long.117](https://doi.org/10.18653/v1/2024.acl-long.117)

**官方链接：** [DOI官方入口](https://doi.org/10.18653/v1/2024.acl-long.117)；[可靠题录/官方原页](https://aclanthology.org/2024.acl-long.117/)

**公开全文链接：** [公开全文](https://aclanthology.org/2024.acl-long.117.pdf)

**主要研究问题：** 如何产生丰富的故事前提以支持开放式生成？

**研究方法：** 将背景和人物等模块组织为嵌套字典，通过键路径组合和模型生成前提。

**主要结论：** 其评测支持模块化前提合成对故事构思的价值。

**与我的毕业论文的关系：** 关联大纲、上下文与章节记忆组织，服务RQ2的任务和输入设计。

**具体可以支撑我论文中的什么内容：** 支撑把人物、背景和情节条件明确组织为任务输入。

**建议使用位置：** 第4章Writing Skill及上下文组织

**使用注意：** 前提丰富性不等于后续章节一致性；不需要为此新增模块商店或自动世界生成能力。

**核验状态：** 题录核验通过。ACL Anthology官方页核验题名、全体作者、年份、刊会、页码及DOI，并提供公开PDF；研究信息依据官方摘要，尚未完成全文精读。

### L13 Lost in the Middle: How Language Models Use Long Contexts

- **编号：** L13
- **所属研究方向：** D2
- **相关程度：** 重要支撑

**英文原题：** Lost in the Middle: How Language Models Use Long Contexts

**中文译题：** 迷失在中间：语言模型如何使用长上下文

**作者：** Nelson F. Liu; Kevin Lin; John Hewitt; Ashwin Paranjape; Michele Bevilacqua; Fabio Petroni; Percy Liang

**年份：** 2024

**文献类型：** 期刊

**期刊或会议：** Transactions of the Association for Computational Linguistics（TACL）

**卷(期)/页码：** 12：157–173；期号无/不适用

**DOI：** [10.1162/tacl_a_00638](https://doi.org/10.1162/tacl_a_00638)

**官方链接：** [DOI官方入口](https://doi.org/10.1162/tacl_a_00638)；[可靠题录/官方原页](https://aclanthology.org/2024.tacl-1.9/)

**公开全文链接：** [公开全文](https://aclanthology.org/2024.tacl-1.9.pdf)

**主要研究问题：** 输入位置和长度如何影响模型利用信息？

**研究方法：** 在多文档问答和键值检索中改变相关信息位置及上下文长度。

**主要结论：** 所评模型的信息利用受位置影响，中间位置表现可能较差。

**与我的毕业论文的关系：** 关联大纲、上下文与章节记忆组织，服务RQ2的任务和输入设计。

**具体可以支撑我论文中的什么内容：** 支撑上下文选择、排序和长度预算需要实测，不能简单堆积所有章节。

**建议使用位置：** 第2章相关技术；第4章上下文组织；第6章AI功能评价

**使用注意：** 不是小说生成实验；不能断言2026年所有模型同样退化，也不能证明摘要一定更好。

**核验状态：** 题录核验通过。ACL Anthology官方页核验题名、全体作者、年份、刊会、页码及DOI，并提供公开PDF；研究信息依据官方摘要，尚未完成全文精读。

### L14 PromptChainer: Chaining Large Language Model Prompts through Visual Programming

- **编号：** L14
- **所属研究方向：** D3
- **相关程度：** 重要支撑

**英文原题：** PromptChainer: Chaining Large Language Model Prompts through Visual Programming

**中文译题：** PromptChainer：通过可视化编程串联大语言模型提示

**作者：** Tongshuang Wu; Ellen Jiang; Aaron Donsbach; Jeff Gray; Alejandra Molina; Michael Terry; Carrie J Cai

**年份：** 2022

**文献类型：** 会议扩展摘要

**期刊或会议：** CHI Conference on Human Factors in Computing Systems Extended Abstracts（2022）

**卷(期)/页码：** 1–10

**DOI：** [10.1145/3491101.3519729](https://doi.org/10.1145/3491101.3519729)

**官方链接：** [DOI官方入口](https://doi.org/10.1145/3491101.3519729)；[可靠题录/官方原页](https://arxiv.org/abs/2203.06566)；[Crossref核验记录](https://api.crossref.org/works/10.1145/3491101.3519729)

**公开全文链接：** [公开全文](https://arxiv.org/pdf/2203.06566)

**主要研究问题：** 复杂任务如何分解为可检查的提示步骤？

**研究方法：** 构建可视化提示链原型，探索中间结果处理和调试。

**主要结论：** 展示了分步组织模型调用及检查中间结果的设计可能性。

**与我的毕业论文的关系：** 关联Writing Skill的任务化输入、规则与输出组织，服务RQ2。

**具体可以支撑我论文中的什么内容：** 支撑Skill内部步骤、输入输出约定和失败定位的设计解释。

**建议使用位置：** 第2章相关技术；第4章Writing Skill

**使用注意：** 扩展摘要与小规模探索证据有限，且非小说效果实验；不要求新增可视化编排器或多Agent。

**核验状态：** 题录核验通过。Crossref核验题名、作者、2022年、扩展摘要刊会、页码和DOI；arXiv原页核验公开版本。

### L15 CoEdIT: Text Editing by Task-Specific Instruction Tuning

- **编号：** L15
- **所属研究方向：** D3、D6
- **相关程度：** 重要支撑

**英文原题：** CoEdIT: Text Editing by Task-Specific Instruction Tuning

**中文译题：** CoEdIT：通过任务专用指令微调实现文本编辑

**作者：** Vipul Raheja; Dhruv Kumar; Ryan Koo; Dongyeop Kang

**年份：** 2023

**文献类型：** 会议

**期刊或会议：** Findings of EMNLP 2023

**卷(期)/页码：** 5274–5291

**DOI：** [10.18653/v1/2023.findings-emnlp.350](https://doi.org/10.18653/v1/2023.findings-emnlp.350)

**官方链接：** [DOI官方入口](https://doi.org/10.18653/v1/2023.findings-emnlp.350)；[可靠题录/官方原页](https://aclanthology.org/2023.findings-emnlp.350/)

**公开全文链接：** [公开全文](https://aclanthology.org/2023.findings-emnlp.350.pdf)

**主要研究问题：** 模型如何遵循不同或组合编辑指令？

**研究方法：** 使用任务化编辑指令数据进行模型微调，评价编辑与指令泛化。

**主要结论：** 实验显示任务指令训练对所测编辑任务及部分组合指令有帮助。

**与我的毕业论文的关系：** 关联Writing Skill的任务化输入、规则与输出组织，服务RQ2。

**具体可以支撑我论文中的什么内容：** 支撑润色等任务的目标区分、编辑约束和评价维度。

**建议使用位置：** 第4章Writing Skill；第6章AI功能评价

**使用注意：** 该文包含模型微调，不能作为本系统仅使用提示模板即可取得同等效果的证据；本项目不因此增加训练。

**核验状态：** 题录核验通过。ACL Anthology官方页核验题名、全体作者、年份、刊会、页码及DOI，并提供公开PDF；研究信息依据官方摘要，尚未完成全文精读。

### L16 CoRRPUS: Code-based Structured Prompting for Neurosymbolic Story Understanding

- **编号：** L16
- **所属研究方向：** D3、D4
- **相关程度：** 重要支撑

**英文原题：** CoRRPUS: Code-based Structured Prompting for Neurosymbolic Story Understanding

**中文译题：** CoRRPUS：面向神经符号故事理解的代码式结构化提示

**作者：** Yijiang River Dong; Lara J. Martin; Chris Callison-Burch

**年份：** 2023

**文献类型：** 会议

**期刊或会议：** Findings of ACL 2023

**卷(期)/页码：** 13152–13168

**DOI：** [10.18653/v1/2023.findings-acl.832](https://doi.org/10.18653/v1/2023.findings-acl.832)

**官方链接：** [DOI官方入口](https://doi.org/10.18653/v1/2023.findings-acl.832)；[可靠题录/官方原页](https://aclanthology.org/2023.findings-acl.832/)

**公开全文链接：** [公开全文](https://aclanthology.org/2023.findings-acl.832.pdf)

**主要研究问题：** 结构化状态表示能否帮助故事理解与推理？

**研究方法：** 使用代码式提示和符号状态追踪，在故事推理任务中评价。

**主要结论：** 展示了结构化提示与状态推理结合的应用价值。

**与我的毕业论文的关系：** 关联结构化创作资料、叙事约束和一致性检查，是RQ2/RQ3的相关研究依据。

**具体可以支撑我论文中的什么内容：** 支撑人物属性和状态应明确表达，以及一致性检查需要对照证据。

**建议使用位置：** 第2章相关技术；第4章Writing Skill及一致性检查

**使用注意：** 代码式神经符号方法不同于普通JSON输入；不能声称二者效果等价，也不增加执行模型代码功能。

**核验状态：** 题录核验通过。ACL Anthology官方页核验题名、全体作者、年份、刊会、页码及DOI，并提供公开PDF；研究信息依据官方摘要，尚未完成全文精读。

### L17 Lost in Stories: Consistency Bugs in Long Story Generation by LLMs

- **编号：** L17
- **所属研究方向：** D4、D6、D2
- **相关程度：** 核心

**英文原题：** Lost in Stories: Consistency Bugs in Long Story Generation by LLMs

**中文译题：** 迷失在故事中：大语言模型长故事生成的一致性缺陷

**作者：** Junjie Li; Xinrui Guo; Yuhao Wu; Roy Ka-Wei Lee; Hongzhi Li; Yutao Xie

**年份：** 2026

**文献类型：** 会议

**期刊或会议：** Findings of ACL 2026

**卷(期)/页码：** 8400–8428

**DOI：** [10.18653/v1/2026.findings-acl.410](https://doi.org/10.18653/v1/2026.findings-acl.410)

**官方链接：** [DOI官方入口](https://doi.org/10.18653/v1/2026.findings-acl.410)；[可靠题录/官方原页](https://aclanthology.org/2026.findings-acl.410/)

**公开全文链接：** [公开全文](https://aclanthology.org/2026.findings-acl.410.pdf)

**主要研究问题：** 如何系统识别和评估长故事中的一致性缺陷？

**研究方法：** 提出ConStory-Bench及缺陷分类，结合证据定位分析长故事错误。

**主要结论：** 所评故事仍存在事实和时序等一致性问题，错误分布与故事位置有关。

**与我的毕业论文的关系：** 关联结构化创作资料、叙事约束和一致性检查，是RQ2/RQ3的相关研究依据。

**具体可以支撑我论文中的什么内容：** 支撑一致性检查的错误分类、证据引用和长文本测试用例设计。

**建议使用位置：** 第1章研究现状；第4章一致性检查；第6章AI功能评价

**使用注意：** 基准结论不代表本系统检出率；需用本系统题材、语言和模型另测，不把检测说成保证消除矛盾。

**核验状态：** 题录核验通过。ACL官方页面核验完整题录、DOI及公开PDF，明确标注2026年7月，早于2026-09-10；不是推测未来会议。

### L18 Finding Flawed Fictions: Evaluating Complex Reasoning in Language Models via Plot Hole Detection

- **编号：** L18
- **所属研究方向：** D4、D6
- **相关程度：** 核心

**英文原题：** Finding Flawed Fictions: Evaluating Complex Reasoning in Language Models via Plot Hole Detection

**中文译题：** 发现有缺陷的虚构故事：通过情节漏洞检测评价语言模型的复杂推理

**作者：** Kabir Ahuja; Melanie Sclar; Yulia Tsvetkov

**年份：** 2025

**文献类型：** 会议

**期刊或会议：** COLM 2025（arXiv公开版本）

**卷(期)/页码：** 无/不适用；未核实正式连续页码

**DOI：** [10.48550/arXiv.2504.11900](https://doi.org/10.48550/arXiv.2504.11900)（arXiv版本DOI）

**官方链接：** [可靠题录/官方原页](https://arxiv.org/abs/2504.11900)

**公开全文链接：** [公开全文](https://arxiv.org/pdf/2504.11900)

**主要研究问题：** 情节漏洞检测如何揭示复杂叙事推理能力？

**研究方法：** 构造并筛选包含情节漏洞的故事，评价模型检测及长度影响。

**主要结论：** 所评模型仍难以稳定识别漏洞，长文本构成额外挑战。

**与我的毕业论文的关系：** 关联结构化创作资料、叙事约束和一致性检查，是RQ2/RQ3的相关研究依据。

**具体可以支撑我论文中的什么内容：** 支撑已知矛盾注入、检出与误报分开统计、要求给出冲突证据。

**建议使用位置：** 第4章一致性检查；第6章AI功能评价

**使用注意：** 合成漏洞不覆盖所有自然小说问题；漏检与误报不能仅靠一个总分掩盖。

**核验状态：** 题录核验通过。arXiv原页核验题名、作者、2025年及DOI和会议版本信息；COLM官方PDF搜索记录交叉印证，OpenReview直访遇浏览器验证。DOI属于arXiv版本，未发现会议DOI。

### L19 SNaC: Coherence Error Detection for Narrative Summarization

- **编号：** L19
- **所属研究方向：** D4、D6
- **相关程度：** 重要支撑

**英文原题：** SNaC: Coherence Error Detection for Narrative Summarization

**中文译题：** SNaC：叙事摘要的连贯性错误检测

**作者：** Tanya Goyal; Junyi Jessy Li; Greg Durrett

**年份：** 2022

**文献类型：** 会议

**期刊或会议：** EMNLP 2022

**卷(期)/页码：** 444–463

**DOI：** [10.18653/v1/2022.emnlp-main.29](https://doi.org/10.18653/v1/2022.emnlp-main.29)

**官方链接：** [DOI官方入口](https://doi.org/10.18653/v1/2022.emnlp-main.29)；[可靠题录/官方原页](https://aclanthology.org/2022.emnlp-main.29/)

**公开全文链接：** [公开全文](https://aclanthology.org/2022.emnlp-main.29.pdf)

**主要研究问题：** 如何定位叙事摘要中的连贯性错误？

**研究方法：** 建立错误类别与片段级人工标注，训练和评价检测器。

**主要结论：** 细粒度标注与定位为分析叙事摘要连贯性提供了可操作方法。

**与我的毕业论文的关系：** 关联结构化创作资料、叙事约束和一致性检查，是RQ2/RQ3的相关研究依据。

**具体可以支撑我论文中的什么内容：** 支撑一致性报告引用具体片段，以及章节记忆摘要的错误标注。

**建议使用位置：** 第4章一致性检查；第6章AI功能评价

**使用注意：** 摘要内部连贯性不等于对原文事实忠实，也不等于人物设定一致；其训练检测器非本系统已实现模型。

**核验状态：** 题录核验通过。ACL Anthology官方页核验题名、全体作者、年份、刊会、页码及DOI，并提供公开PDF；研究信息依据官方摘要，尚未完成全文精读。

### L20 STORYSUMM: Evaluating Faithfulness in Story Summarization

- **编号：** L20
- **所属研究方向：** D4、D6、D2
- **相关程度：** 核心

**英文原题：** STORYSUMM: Evaluating Faithfulness in Story Summarization

**中文译题：** STORYSUMM：评价故事摘要的忠实性

**作者：** Melanie Subbiah; Faisal Ladhak; Akankshya Mishra; Griffin Thomas Adams; Lydia Chilton; Kathleen McKeown

**年份：** 2024

**文献类型：** 会议

**期刊或会议：** EMNLP 2024

**卷(期)/页码：** 9988–10005

**DOI：** [10.18653/v1/2024.emnlp-main.557](https://doi.org/10.18653/v1/2024.emnlp-main.557)

**官方链接：** [DOI官方入口](https://doi.org/10.18653/v1/2024.emnlp-main.557)；[可靠题录/官方原页](https://aclanthology.org/2024.emnlp-main.557/)

**公开全文链接：** [公开全文](https://aclanthology.org/2024.emnlp-main.557.pdf)

**主要研究问题：** 如何可靠判断故事摘要是否忠实原文？

**研究方法：** 构建局部忠实性标签与错误解释，对人工及自动评价进行分析。

**主要结论：** 故事摘要错误容易被遗漏；现有自动评价存在限制。

**与我的毕业论文的关系：** 关联结构化创作资料、叙事约束和一致性检查，是RQ2/RQ3的相关研究依据。

**具体可以支撑我论文中的什么内容：** 支撑章节记忆需要对照原文核验，不能直接把模型摘要当作事实。

**建议使用位置：** 第4章上下文组织；第6章AI功能评价

**使用注意：** 短故事摘要与长篇续写不同；错误分类需结合本系统场景调整，不能将摘要质量当成续写质量。

**核验状态：** 题录核验通过。ACL Anthology官方页核验题名、全体作者、年份、刊会、页码及DOI，并提供公开PDF；研究信息依据官方摘要，尚未完成全文精读。

### L21 FABLES: Evaluating faithfulness and content selection in book-length summarization

- **编号：** L21
- **所属研究方向：** D2、D4、D6
- **相关程度：** 核心

**英文原题：** FABLES: Evaluating faithfulness and content selection in book-length summarization

**中文译题：** FABLES：评价整本书摘要的忠实性与内容选择

**作者：** Yekyung Kim; Yapei Chang; Marzena Karpinska; Aparna Garimella; Varun Manjunatha; Kyle Lo; Tanya Goyal; Mohit Iyyer

**年份：** 2024

**文献类型：** 会议

**期刊或会议：** COLM 2024（arXiv公开版本）

**卷(期)/页码：** 无/不适用；未核实正式连续页码

**DOI：** [10.48550/arXiv.2404.01261](https://doi.org/10.48550/arXiv.2404.01261)（arXiv版本DOI）

**官方链接：** [可靠题录/官方原页](https://arxiv.org/abs/2404.01261)

**公开全文链接：** [公开全文](https://arxiv.org/pdf/2404.01261)

**主要研究问题：** 书籍级摘要会出现哪些事实错误和内容选择偏差？

**研究方法：** 对近期书籍的模型摘要进行主张级人工标注并分析自动评价。

**主要结论：** 事件、人物状态及内容遗漏构成重要问题，自动评判也有不足。

**与我的毕业论文的关系：** 关联结构化创作资料、叙事约束和一致性检查，是RQ2/RQ3的相关研究依据。

**具体可以支撑我论文中的什么内容：** 支撑章节记忆保留人物状态与关键事件，并分别评价遗漏和事实错误。

**建议使用位置：** 第4章上下文组织；第6章AI功能评价

**使用注意：** 整书摘要任务不等于增量章节记忆；不能把自洽当作忠实原文。

**核验状态：** 题录核验通过。arXiv原页核验题名、作者、2024年、DOI及Journal reference中的COLM 2024；官方OpenReview PDF记录交叉发现，直访受浏览器验证限制。DOI是arXiv版本DOI。

### L22 BooookScore: A systematic exploration of book-length summarization in the era of LLMs

- **编号：** L22
- **所属研究方向：** D2、D6
- **相关程度：** 重要支撑

**英文原题：** BooookScore: A systematic exploration of book-length summarization in the era of LLMs

**中文译题：** BooookScore：大语言模型时代书籍级摘要的系统探索

**作者：** Yapei Chang; Kyle Lo; Tanya Goyal; Mohit Iyyer

**年份：** 2024

**文献类型：** 会议

**期刊或会议：** ICLR 2024（arXiv公开版本）

**卷(期)/页码：** 无/不适用；未核实正式连续页码

**DOI：** [10.48550/arXiv.2310.00785](https://doi.org/10.48550/arXiv.2310.00785)（arXiv版本DOI）

**官方链接：** [可靠题录/官方原页](https://arxiv.org/abs/2310.00785)

**公开全文链接：** [公开全文](https://arxiv.org/pdf/2310.00785)

**主要研究问题：** 如何生成和评价书籍级连贯摘要？

**研究方法：** 比较层次合并和增量更新，建立连贯性错误类别与自动评价方法。

**主要结论：** 揭示摘要策略在细节保留和连贯性上的取舍。

**与我的毕业论文的关系：** 关联大纲、上下文与章节记忆组织，服务RQ2的任务和输入设计。

**具体可以支撑我论文中的什么内容：** 支撑章节记忆更新策略的比较，以及摘要错误分类。

**建议使用位置：** 第4章上下文组织；第6章AI功能评价

**使用注意：** BooookScore不能代替对照原文的忠实性检查；不能把其自动指标直接当作本系统唯一验收标准。

**核验状态：** 题录核验通过。arXiv原页核验题名、作者、DOI及ICLR 2024 camera-ready说明；2023首次预印本、2024会议版本只计一篇。OpenReview直访验证受限，DOI仅指arXiv版本。

### L23 Of Human Criteria and Automatic Metrics: A Benchmark of the Evaluation of Story Generation

- **编号：** L23
- **所属研究方向：** D6
- **相关程度：** 核心

**英文原题：** Of Human Criteria and Automatic Metrics: A Benchmark of the Evaluation of Story Generation

**中文译题：** 人工标准与自动指标：故事生成评价基准

**作者：** Cyril Chhun; Pierre Colombo; Fabian M. Suchanek; Chloé Clavel

**年份：** 2022

**文献类型：** 会议

**期刊或会议：** COLING 2022

**卷(期)/页码：** 5794–5836

**DOI：** 未发现 DOI

**官方链接：** [可靠题录/官方原页](https://aclanthology.org/2022.coling-1.509/)

**公开全文链接：** [公开全文](https://aclanthology.org/2022.coling-1.509.pdf)

**主要研究问题：** 自动指标与人的故事质量判断如何对应？

**研究方法：** HANNA收集故事的多维人评，比较多种自动指标与人评相关性。

**主要结论：** 评价需区分质量维度，自动指标不能不经验证地替代人工判断。

**与我的毕业论文的关系：** 关联作者主导的人机协作及辅助价值评价，服务RQ1/RQ2的交互与评价论证。

**具体可以支撑我论文中的什么内容：** 支撑相关性、连贯性、共情、惊喜、吸引力和复杂度等候选维度，再按六类Skill选用。

**建议使用位置：** 第6章AI功能评价；第1章研究现状

**使用注意：** 不是每个Skill都适合全部维度；不能把相关性写成因果关系或直接套用他人分数。

**核验状态：** 题录核验通过。ACL官方页核验题名、作者、2022年、COLING及页码，核对PDF相关内容；官方DOI字段为空，未发现DOI，不按ACL编号猜测。

### L24 Do Language Models Enjoy Their Own Stories? Prompting Large Language Models for Automatic Story Evaluation

- **编号：** L24
- **所属研究方向：** D6、D3
- **相关程度：** 核心

**英文原题：** Do Language Models Enjoy Their Own Stories? Prompting Large Language Models for Automatic Story Evaluation

**中文译题：** 语言模型喜欢自己的故事吗？通过提示大语言模型进行自动故事评价

**作者：** Cyril Chhun; Fabian M. Suchanek; Chloé Clavel

**年份：** 2024

**文献类型：** 期刊

**期刊或会议：** Transactions of the Association for Computational Linguistics（TACL）

**卷(期)/页码：** 12：1122–1142；期号无/不适用

**DOI：** [10.1162/tacl_a_00689](https://doi.org/10.1162/tacl_a_00689)

**官方链接：** [DOI官方入口](https://doi.org/10.1162/tacl_a_00689)；[可靠题录/官方原页](https://aclanthology.org/2024.tacl-1.62/)

**公开全文链接：** [公开全文](https://aclanthology.org/2024.tacl-1.62.pdf)

**主要研究问题：** 提示方式如何影响LLM故事评分与人评的一致程度？

**研究方法：** 比较提示条件、模型评分、传统自动指标与人工判断。

**主要结论：** 部分系统级评价具有价值，但解释质量和评价可靠性仍有限。

**与我的毕业论文的关系：** 关联Writing Skill的任务化输入、规则与输出组织，服务RQ2。

**具体可以支撑我论文中的什么内容：** 支撑固定评分量表和提示、人工校准、避免把模型评分作为唯一依据。

**建议使用位置：** 第6章AI功能评价

**使用注意：** 系统级相关不能直接保证单篇评分可靠；生成模型自评存在需要检查的偏差。

**核验状态：** 题录核验通过。ACL Anthology官方页核验题名、全体作者、年份、刊会、页码及DOI，并提供公开PDF；研究信息依据官方摘要，尚未完成全文精读。

### L25 Art or Artifice? Large Language Models and the False Promise of Creativity

- **编号：** L25
- **所属研究方向：** D6、D1
- **相关程度：** 核心

**英文原题：** Art or Artifice? Large Language Models and the False Promise of Creativity

**中文译题：** 艺术还是伪饰？大语言模型与创造力的虚假承诺

**作者：** Tuhin Chakrabarty; Philippe Laban; Divyansh Agarwal; Smaranda Muresan; Chien-Sheng Wu

**年份：** 2024

**文献类型：** 会议

**期刊或会议：** CHI 2024

**卷(期)/页码：** 1–34

**DOI：** [10.1145/3613904.3642731](https://doi.org/10.1145/3613904.3642731)

**官方链接：** [DOI官方入口](https://doi.org/10.1145/3613904.3642731)；[可靠题录/官方原页](https://arxiv.org/abs/2309.14556)；[Crossref核验记录](https://api.crossref.org/works/10.1145/3613904.3642731)

**公开全文链接：** [公开全文](https://arxiv.org/pdf/2309.14556)

**主要研究问题：** 如何从创造力维度比较人类与模型故事？

**研究方法：** 以TTCW测试和专家评价分析人类及模型故事，并检查模型评判能力。

**主要结论：** 在所评条件下模型的创造力表现及自动判断与专家之间仍存在差距。

**与我的毕业论文的关系：** 关联作者主导的人机协作及辅助价值评价，服务RQ1/RQ2的交互与评价论证。

**具体可以支撑我论文中的什么内容：** 支撑创意质量需要细分维度和人工判断，避免宣称AI全面超越作者。

**建议使用位置：** 第1章研究现状；第6章AI功能评价

**使用注意：** 论文题名不能被当成所有LLM没有创造力的普遍结论；与人机协作研究的对象不同。

**核验状态：** 题录核验通过。Crossref核验正式题名、作者、2024年、CHI页码及DOI；arXiv原页核验2023预印本与2024更新，只计正式2024一篇。

### L26 Generative AI enhances individual creativity but reduces the collective diversity of novel content

- **编号：** L26
- **所属研究方向：** D1、D6
- **相关程度：** 核心

**英文原题：** Generative AI enhances individual creativity but reduces the collective diversity of novel content

**中文译题：** 生成式AI提升个体创造力，但降低新创内容的群体多样性

**作者：** Anil R. Doshi; Oliver P. Hauser

**年份：** 2024

**文献类型：** 期刊

**期刊或会议：** Science Advances

**卷(期)/页码：** 10(28)：eadn5290；文章号，无传统页码

**DOI：** [10.1126/sciadv.adn5290](https://doi.org/10.1126/sciadv.adn5290)

**官方链接：** [DOI官方入口](https://doi.org/10.1126/sciadv.adn5290)；[可靠题录/官方原页](https://www.science.org/doi/10.1126/sciadv.adn5290)；[Crossref核验记录](https://api.crossref.org/works/10.1126/sciadv.adn5290)

**公开全文链接：** [公开全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532/)

**主要研究问题：** AI提供创意对个人作品与群体多样性有何影响？

**研究方法：** 随机分配短故事写作中的AI创意辅助条件，评价作品及相似性。

**主要结论：** 研究中辅助提高个体作品部分评价，同时作品之间趋于相似。

**与我的毕业论文的关系：** 关联作者主导的人机协作及辅助价值评价，服务RQ1/RQ2的交互与评价论证。

**具体可以支撑我论文中的什么内容：** 支撑同时考虑辅助收益和同质化风险，区分个体质量与跨作品多样性。

**建议使用位置：** 第1章研究背景及现状；第6章AI功能评价

**使用注意：** 英文novel content指新创内容，不等于长篇小说；短任务、非专业样本不能直接推广为小说系统效果。

**核验状态：** 题录核验通过。Crossref核验题名、两位作者、2024-07-12、期刊卷期、文章号及DOI；PMC公开全文可访问并交叉核对，Science直访受限。

### L27 A Survey on LLMs for Story Generation

- **编号：** L27
- **所属研究方向：** D1、D2、D3、D4、D6
- **相关程度：** 核心

**英文原题：** A Survey on LLMs for Story Generation

**中文译题：** 大语言模型故事生成研究综述

**作者：** Maria Teleki; Vedangi Bengali; Xiangjue Dong; Sai Tejas Janjur; Haoran Liu; Tian Liu; Cong Wang; Ting Liu; Yin Zhang; Frank Shipman; James Caverlee

**年份：** 2025

**文献类型：** 会议综述论文

**期刊或会议：** Findings of EMNLP 2025

**卷(期)/页码：** 13954–13966

**DOI：** [10.18653/v1/2025.findings-emnlp.750](https://doi.org/10.18653/v1/2025.findings-emnlp.750)

**官方链接：** [DOI官方入口](https://doi.org/10.18653/v1/2025.findings-emnlp.750)；[可靠题录/官方原页](https://aclanthology.org/2025.findings-emnlp.750/)

**公开全文链接：** [公开全文](https://aclanthology.org/2025.findings-emnlp.750.pdf)

**主要研究问题：** LLM故事生成的任务、方法和评价如何组织？

**研究方法：** 按生成与作者辅助等维度梳理方法、数据和评价研究。

**主要结论：** 提供故事生成领域的分类框架与研究问题地图。

**与我的毕业论文的关系：** 关联结构化创作资料、叙事约束和一致性检查，是RQ2/RQ3的相关研究依据。

**具体可以支撑我论文中的什么内容：** 支撑研究现状结构，帮助回溯核心一手研究并定位作者辅助系统。

**建议使用位置：** 第1章研究现状；第2章相关技术

**使用注意：** 综述不能替代原论文支撑具体效果；其中早于2022年的引用本轮不列正式候选。

**核验状态：** 题录核验通过。ACL Anthology官方页核验题名、全体作者、年份、刊会、页码及DOI，并提供公开PDF；研究信息依据官方摘要，尚未完成全文精读。

### L28 人工智能生成内容技术环境下内容生产的版权审视与主体反思——基于AI使用者在AI小说《天命使徒》中智力投入的考察

- **编号：** L28
- **所属研究方向：** D1
- **相关程度：** 一般支撑

**英文原题：** 不适用：中文原文；官方英文题名未核实

**中文译题：** 人工智能生成内容技术环境下内容生产的版权审视与主体反思——基于AI使用者在AI小说《天命使徒》中智力投入的考察（中文原题，非译题）

**作者：** 刘惠凤；于文

**年份：** 2025

**文献类型：** 期刊

**期刊或会议：** 中国数字出版

**卷(期)/页码：** 3(04)：75–82

**DOI：** 未发现 DOI

**官方链接：** [可靠题录/官方原页](https://shcb.cbpt.cnki.net/portal/journal/portal/client/paper/a199d990cc294cd0920ff770a3a9fd55)

**公开全文链接：** 未发现可核验的公开全文；上列官方题录页提供数据库全文入口，获取可能需要权限。

**主要研究问题：** AI小说创作中人的投入与主体作用如何理解？

**研究方法：** 基于相关创作团队访谈与案例，对人的智力投入和创作主体进行分析。

**主要结论：** 摘要强调AI使用者的创作投入及主体问题，提供中国语境的讨论。

**与我的毕业论文的关系：** 关联作者主导的人机协作及辅助价值评价，服务RQ1/RQ2的交互与评价论证。

**具体可以支撑我论文中的什么内容：** 支撑作者主导、人工决定是否采用结果的背景论述。

**建议使用位置：** 第1章国内外研究现状

**使用注意：** 仅核验题录与摘要，全文未取得；不作为现行法律结论或本系统版权归属证明，也不证明模型创作质量。

**核验状态：** 题录核验通过。知网提供技术支持的期刊官网核验中文题名、两位作者、2025-07-15、卷期页码；DOI字段为空，未发现DOI。全文入口提示访问cnki.net，公开全文未核实。

### L29 人工智能对网络文学的影响：主体危机、镜像扩容及数据依赖

- **编号：** L29
- **所属研究方向：** D1、D9
- **相关程度：** 一般支撑

**英文原题：** 不适用：中文原文；官方英文题名未核实

**中文译题：** 人工智能对网络文学的影响：主体危机、镜像扩容及数据依赖（中文原题，非译题）

**作者：** 李玉萍

**年份：** 2025

**文献类型：** 期刊

**期刊或会议：** 山东师范大学学报（社会科学版）

**卷(期)/页码：** 70(02)：44–54

**DOI：** [10.16456/j.cnki.1001-5973.2025.02.005](https://doi.org/10.16456/j.cnki.1001-5973.2025.02.005)

**官方链接：** [DOI官方入口](https://doi.org/10.16456/j.cnki.1001-5973.2025.02.005)；[可靠题录/官方原页](https://sdss.cbpt.cnki.net/portal/journal/portal/client/paper/eeed46b499dacc9ef1e3f475549cd7eb)

**公开全文链接：** 未发现可核验的公开全文；上列官方题录页提供数据库全文入口，获取可能需要权限。

**主要研究问题：** AI如何影响网络文学创作主体、内容形态和数据依赖？

**研究方法：** 理论分析AI与网络文学的关系及相关创作现象。

**主要结论：** 摘要讨论主体性、内容扩展及数据依赖等影响。

**与我的毕业论文的关系：** 关联网络文学场景及行业趋势的研究边界；不承担系统数据源已选定的证明。

**具体可以支撑我论文中的什么内容：** 支撑中文网络文学场景中的创作主体与同质化问题讨论。

**建议使用位置：** 第1章研究背景及国内外研究现状

**使用注意：** 非题材趋势数据集、非系统效果实验；不能用其推导当前热度排名或训练数据授权。

**核验状态：** 题录核验通过。知网期刊官网核验题名、作者、正式刊期2025、卷页及DOI。页面另列2024-12-06发布信息，正式引用为2025年，保留差异；全文未取得。

### L30 新大众文艺崛起 多价值生态重构——基于《2024年度中国网络文学发展报告》的解读

- **编号：** L30
- **所属研究方向：** D9
- **相关程度：** 重要支撑

**英文原题：** 不适用：中文原文；官方英文题名未核实

**中文译题：** 新大众文艺崛起 多价值生态重构——基于《2024年度中国网络文学发展报告》的解读（中文原题，非译题）

**作者：** 冯思然；李慧楠；岑振唯；李弘

**年份：** 2025

**文献类型：** 期刊

**期刊或会议：** 中国数字出版

**卷(期)/页码：** 3(04)：83–97

**DOI：** 未发现 DOI

**官方链接：** [可靠题录/官方原页](https://shcb.cbpt.cnki.net/portal/journal/portal/client/paper/38d7fbb3f32eb5aa09c3a087fc1014d2)

**公开全文链接：** 未发现可核验的公开全文；上列官方题录页提供数据库全文入口，获取可能需要权限。

**主要研究问题：** 年度行业报告反映了哪些网络文学产业和题材特征？

**研究方法：** 对《2024年度中国网络文学发展报告》进行解读，梳理题材、作者、用户及产业等信息。

**主要结论：** 摘要提出网络文学业态及价值结构变化的解释。

**与我的毕业论文的关系：** 关联网络文学场景及行业趋势的研究边界；不承担系统数据源已选定的证明。

**具体可以支撑我论文中的什么内容：** 支撑趋势分析模块的行业背景和数据维度选择；后续回到原始报告核对具体数字及口径。

**建议使用位置：** 第1章研究背景；第3章趋势分析需求

**使用注意：** 报告解读不是实时榜单数据接口；不能据此确定采集平台、更新周期或把2024统计当作2026实时趋势。

**核验状态：** 题录核验通过。知网期刊官网核验题名、四位作者、2025-07-15、卷期页码；DOI栏为空，未发现DOI。可读题录与摘要，全文需转数据库，未发现可核验公开全文。

## 4. 候选参考文献总表

“来源”是正式刊会或预印本平台；核验入口见逐篇记录。“全文待取”不影响已核验题录的真实性，但限制后续具体论据提取。多方向交叉归类，不按方向重复计篇。

| 编号 | 年份 | 第一作者 | 论文题目 | D1–D9方向 | 相关程度 | 来源 | DOI | 官方链接 | 建议论文使用章节 | 核验状态 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| L01 | 2022 | Mina Lee | CoAuthor: Designing a Human-AI Collaborative Writing Dataset for Exploring Language Model Capabilities | D1、D6 | 核心 | CHI 2022 | [10.1145/3491102.3502030](https://doi.org/10.1145/3491102.3502030) | [原页](https://arxiv.org/abs/2201.06796) | 第1章研究现状；第4章交互设计；第6章AI功能评价 | 题录已核验；全文入口见条目 |
| L02 | 2022 | Ann Yuan | Wordcraft: Story Writing With Large Language Models | D1、D3、D6 | 核心 | 27th International Conference on Intelligent User Interfaces（IUI 2022） | [10.1145/3490099.3511105](https://doi.org/10.1145/3490099.3511105) | [原页](https://dl.acm.org/doi/10.1145/3490099.3511105) | 第1章研究现状；第4章Writing Skill；第6章AI功能评价 | 题录已核验；全文入口见条目 |
| L03 | 2022 | Daphne Ippolito | Creative Writing with an AI-Powered Writing Assistant: Perspectives from Professional Writers | D1、D6 | 核心 | arXiv:2211.05030 | [10.48550/arXiv.2211.05030](https://doi.org/10.48550/arXiv.2211.05030)（arXiv版本DOI） | [原页](https://arxiv.org/abs/2211.05030) | 第1章研究现状；第4章交互设计；第6章AI功能评价 | 题录已核验；arXiv版本DOI已注明 |
| L04 | 2023 | Piotr Mirowski | Co-Writing Screenplays and Theatre Scripts with Language Models: Evaluation by Industry Professionals | D1、D2、D6 | 核心 | CHI 2023 | [10.1145/3544548.3581225](https://doi.org/10.1145/3544548.3581225) | [原页](https://arxiv.org/abs/2209.14958) | 第1章研究现状；第4章上下文组织；第6章AI功能评价 | 题录已核验；全文入口见条目 |
| L05 | 2022 | Max Kreminski | Unmet Creativity Support Needs in Computationally Supported Creative Writing | D1 | 重要支撑 | First Workshop on Intelligent and Interactive Writing Assistants（In2Writing 2022） | [10.18653/v1/2022.in2writing-1.11](https://doi.org/10.18653/v1/2022.in2writing-1.11) | [原页](https://aclanthology.org/2022.in2writing-1.11/) | 第1章研究背景与研究现状 | 题录已核验；全文入口见条目 |
| L06 | 2024 | Mina Lee | A Design Space for Intelligent and Interactive Writing Assistants | D1、D6 | 重要支撑 | CHI 2024 | [10.1145/3613904.3642697](https://doi.org/10.1145/3613904.3642697) | [原页](https://arxiv.org/abs/2403.14117) | 第1章研究现状；第3章需求分析 | 题录已核验；全文入口见条目 |
| L07 | 2022 | John Joon Young Chung | TaleBrush: Sketching Stories with Generative Pretrained Language Models | D1、D3 | 重要支撑 | CHI 2022 | [10.1145/3491102.3501819](https://doi.org/10.1145/3491102.3501819) | [原页](https://dl.acm.org/doi/10.1145/3491102.3501819) | 第1章研究现状；第4章Writing Skill | 题录已核验；全文入口见条目 |
| L08 | 2022 | Kevin Yang | Re3: Generating Longer Stories With Recursive Reprompting and Revision | D2、D3、D4 | 核心 | EMNLP 2022 | [10.18653/v1/2022.emnlp-main.296](https://doi.org/10.18653/v1/2022.emnlp-main.296) | [原页](https://aclanthology.org/2022.emnlp-main.296/) | 第4章上下文组织；第6章AI功能评价 | 题录已核验；全文入口见条目 |
| L09 | 2023 | Kevin Yang | DOC: Improving Long Story Coherence With Detailed Outline Control | D2、D3、D4 | 核心 | ACL 2023，Volume 1: Long Papers | [10.18653/v1/2023.acl-long.190](https://doi.org/10.18653/v1/2023.acl-long.190) | [原页](https://aclanthology.org/2023.acl-long.190/) | 第4章Writing Skill及上下文组织；第6章AI功能评价 | 题录已核验；全文入口见条目 |
| L10 | 2025 | Qianyue Wang | Generating Long-form Story Using Dynamic Hierarchical Outlining with Memory-Enhancement | D2、D4 | 核心 | NAACL 2025：Nations of the Americas Chapter，Human Language Technologies，Volume 1: Long Papers | [10.18653/v1/2025.naacl-long.63](https://doi.org/10.18653/v1/2025.naacl-long.63) | [原页](https://aclanthology.org/2025.naacl-long.63/) | 第1章研究现状；第4章上下文组织；第6章AI功能评价 | 题录已核验；全文入口见条目 |
| L11 | 2024 | Kaige Xie | Creating Suspenseful Stories: Iterative Planning with Large Language Models | D2、D3 | 重要支撑 | EACL 2024，Volume 1: Long Papers | [10.18653/v1/2024.eacl-long.147](https://doi.org/10.18653/v1/2024.eacl-long.147) | [原页](https://aclanthology.org/2024.eacl-long.147/) | 第4章Writing Skill；第6章AI功能评价 | 题录已核验；全文入口见条目 |
| L12 | 2024 | Yan Ma | MoPS: Modular Story Premise Synthesis for Open-Ended Automatic Story Generation | D2、D3 | 重要支撑 | ACL 2024，Volume 1: Long Papers | [10.18653/v1/2024.acl-long.117](https://doi.org/10.18653/v1/2024.acl-long.117) | [原页](https://aclanthology.org/2024.acl-long.117/) | 第4章Writing Skill及上下文组织 | 题录已核验；全文入口见条目 |
| L13 | 2024 | Nelson F. Liu | Lost in the Middle: How Language Models Use Long Contexts | D2 | 重要支撑 | Transactions of the Association for Computational Linguistics（TACL） | [10.1162/tacl_a_00638](https://doi.org/10.1162/tacl_a_00638) | [原页](https://aclanthology.org/2024.tacl-1.9/) | 第2章相关技术；第4章上下文组织；第6章AI功能评价 | 题录已核验；全文入口见条目 |
| L14 | 2022 | Tongshuang Wu | PromptChainer: Chaining Large Language Model Prompts through Visual Programming | D3 | 重要支撑 | CHI Conference on Human Factors in Computing Systems Extended Abstracts（2022） | [10.1145/3491101.3519729](https://doi.org/10.1145/3491101.3519729) | [原页](https://arxiv.org/abs/2203.06566) | 第2章相关技术；第4章Writing Skill | 题录已核验；全文入口见条目 |
| L15 | 2023 | Vipul Raheja | CoEdIT: Text Editing by Task-Specific Instruction Tuning | D3、D6 | 重要支撑 | Findings of EMNLP 2023 | [10.18653/v1/2023.findings-emnlp.350](https://doi.org/10.18653/v1/2023.findings-emnlp.350) | [原页](https://aclanthology.org/2023.findings-emnlp.350/) | 第4章Writing Skill；第6章AI功能评价 | 题录已核验；全文入口见条目 |
| L16 | 2023 | Yijiang River Dong | CoRRPUS: Code-based Structured Prompting for Neurosymbolic Story Understanding | D3、D4 | 重要支撑 | Findings of ACL 2023 | [10.18653/v1/2023.findings-acl.832](https://doi.org/10.18653/v1/2023.findings-acl.832) | [原页](https://aclanthology.org/2023.findings-acl.832/) | 第2章相关技术；第4章Writing Skill及一致性检查 | 题录已核验；全文入口见条目 |
| L17 | 2026 | Junjie Li | Lost in Stories: Consistency Bugs in Long Story Generation by LLMs | D4、D6、D2 | 核心 | Findings of ACL 2026 | [10.18653/v1/2026.findings-acl.410](https://doi.org/10.18653/v1/2026.findings-acl.410) | [原页](https://aclanthology.org/2026.findings-acl.410/) | 第1章研究现状；第4章一致性检查；第6章AI功能评价 | 题录已核验；全文入口见条目 |
| L18 | 2025 | Kabir Ahuja | Finding Flawed Fictions: Evaluating Complex Reasoning in Language Models via Plot Hole Detection | D4、D6 | 核心 | COLM 2025（arXiv公开版本） | [10.48550/arXiv.2504.11900](https://doi.org/10.48550/arXiv.2504.11900)（arXiv版本DOI） | [原页](https://arxiv.org/abs/2504.11900) | 第4章一致性检查；第6章AI功能评价 | 题录已核验；arXiv版本DOI已注明 |
| L19 | 2022 | Tanya Goyal | SNaC: Coherence Error Detection for Narrative Summarization | D4、D6 | 重要支撑 | EMNLP 2022 | [10.18653/v1/2022.emnlp-main.29](https://doi.org/10.18653/v1/2022.emnlp-main.29) | [原页](https://aclanthology.org/2022.emnlp-main.29/) | 第4章一致性检查；第6章AI功能评价 | 题录已核验；全文入口见条目 |
| L20 | 2024 | Melanie Subbiah | STORYSUMM: Evaluating Faithfulness in Story Summarization | D4、D6、D2 | 核心 | EMNLP 2024 | [10.18653/v1/2024.emnlp-main.557](https://doi.org/10.18653/v1/2024.emnlp-main.557) | [原页](https://aclanthology.org/2024.emnlp-main.557/) | 第4章上下文组织；第6章AI功能评价 | 题录已核验；全文入口见条目 |
| L21 | 2024 | Yekyung Kim | FABLES: Evaluating faithfulness and content selection in book-length summarization | D2、D4、D6 | 核心 | COLM 2024（arXiv公开版本） | [10.48550/arXiv.2404.01261](https://doi.org/10.48550/arXiv.2404.01261)（arXiv版本DOI） | [原页](https://arxiv.org/abs/2404.01261) | 第4章上下文组织；第6章AI功能评价 | 题录已核验；arXiv版本DOI已注明 |
| L22 | 2024 | Yapei Chang | BooookScore: A systematic exploration of book-length summarization in the era of LLMs | D2、D6 | 重要支撑 | ICLR 2024（arXiv公开版本） | [10.48550/arXiv.2310.00785](https://doi.org/10.48550/arXiv.2310.00785)（arXiv版本DOI） | [原页](https://arxiv.org/abs/2310.00785) | 第4章上下文组织；第6章AI功能评价 | 题录已核验；arXiv版本DOI已注明 |
| L23 | 2022 | Cyril Chhun | Of Human Criteria and Automatic Metrics: A Benchmark of the Evaluation of Story Generation | D6 | 核心 | COLING 2022 | 未发现 DOI | [原页](https://aclanthology.org/2022.coling-1.509/) | 第6章AI功能评价；第1章研究现状 | 题录已核验；全文入口见条目 |
| L24 | 2024 | Cyril Chhun | Do Language Models Enjoy Their Own Stories? Prompting Large Language Models for Automatic Story Evaluation | D6、D3 | 核心 | Transactions of the Association for Computational Linguistics（TACL） | [10.1162/tacl_a_00689](https://doi.org/10.1162/tacl_a_00689) | [原页](https://aclanthology.org/2024.tacl-1.62/) | 第6章AI功能评价 | 题录已核验；全文入口见条目 |
| L25 | 2024 | Tuhin Chakrabarty | Art or Artifice? Large Language Models and the False Promise of Creativity | D6、D1 | 核心 | CHI 2024 | [10.1145/3613904.3642731](https://doi.org/10.1145/3613904.3642731) | [原页](https://arxiv.org/abs/2309.14556) | 第1章研究现状；第6章AI功能评价 | 题录已核验；全文入口见条目 |
| L26 | 2024 | Anil R. Doshi | Generative AI enhances individual creativity but reduces the collective diversity of novel content | D1、D6 | 核心 | Science Advances | [10.1126/sciadv.adn5290](https://doi.org/10.1126/sciadv.adn5290) | [原页](https://www.science.org/doi/10.1126/sciadv.adn5290) | 第1章研究背景及现状；第6章AI功能评价 | 题录已核验；全文入口见条目 |
| L27 | 2025 | Maria Teleki | A Survey on LLMs for Story Generation | D1、D2、D3、D4、D6 | 核心 | Findings of EMNLP 2025 | [10.18653/v1/2025.findings-emnlp.750](https://doi.org/10.18653/v1/2025.findings-emnlp.750) | [原页](https://aclanthology.org/2025.findings-emnlp.750/) | 第1章研究现状；第2章相关技术 | 题录已核验；全文入口见条目 |
| L28 | 2025 | 刘惠凤 | 人工智能生成内容技术环境下内容生产的版权审视与主体反思——基于AI使用者在AI小说《天命使徒》中智力投入的考察 | D1 | 一般支撑 | 中国数字出版 | 未发现 DOI | [原页](https://shcb.cbpt.cnki.net/portal/journal/portal/client/paper/a199d990cc294cd0920ff770a3a9fd55) | 第1章国内外研究现状 | 题录已核验；全文待取 |
| L29 | 2025 | 李玉萍 | 人工智能对网络文学的影响：主体危机、镜像扩容及数据依赖 | D1、D9 | 一般支撑 | 山东师范大学学报（社会科学版） | [10.16456/j.cnki.1001-5973.2025.02.005](https://doi.org/10.16456/j.cnki.1001-5973.2025.02.005) | [原页](https://sdss.cbpt.cnki.net/portal/journal/portal/client/paper/eeed46b499dacc9ef1e3f475549cd7eb) | 第1章研究背景及国内外研究现状 | 题录已核验；全文待取 |
| L30 | 2025 | 冯思然 | 新大众文艺崛起 多价值生态重构——基于《2024年度中国网络文学发展报告》的解读 | D9 | 重要支撑 | 中国数字出版 | 未发现 DOI | [原页](https://shcb.cbpt.cnki.net/portal/journal/portal/client/paper/38d7fbb3f32eb5aa09c3a087fc1014d2) | 第1章研究背景；第3章趋势分析需求 | 题录已核验；全文待取 |

## 5. 优先精读 TOP 10

精读顺序按“研究地图 → 作者协作 → 上下文方法 → 一致性与评价”安排，不是按被引量或刊会排名。编号对应上文及总表。

| 顺序 | 文献 | 为什么优先 | 精读时应提取 |
|---|---|---|---|
| 1 | L27 A Survey on LLMs for Story Generation | 先区分自动故事生成与作者辅助，避免研究现状结构跑偏 | 分类标准、核心一手论文、评价任务和未解决问题 |
| 2 | L02 Wordcraft | 与编辑器、任务入口、续写润色及作者采用流程最接近 | 实际提示组织、交互流程、对照条件、作者控制与评价题项 |
| 3 | L01 CoAuthor | 补足“只看最终文本”的局限，便于理解人机协作过程 | 建议请求/接受/修改记录的定义及数据采集限制 |
| 4 | L03 Professional Writers | 给出专业作者视角，帮助界定辅助的价值和失效方式 | 对文风、表达意图和控制感的反馈，区分访谈与因果结论 |
| 5 | L08 Re3 | 提供计划、已有状态和生成修订结合的具体案例 | 输入内容、重提示步骤、各组件贡献及对照条件 |
| 6 | L09 DOC | 直接对应大纲粒度如何影响长篇内容控制 | 大纲层次、控制机制、评价量表和与Re3的差别 |
| 7 | L10 DOME | 对动态大纲、记忆及时间冲突提供近期相关方案 | 记忆更新、时序约束及哪些效果依赖知识图谱，防止直接移植 |
| 8 | L17 Lost in Stories | 最新且时间已核验，最贴近长故事一致性检查 | 缺陷类别、证据格式、误报/漏报定义、基准覆盖盲区 |
| 9 | L20 STORYSUMM | 防止章节记忆把错误带入后续生成 | 忠实性标签、对照原文方法、人工核验协议和评价失效 |
| 10 | L23 HANNA | 为第6章提供多维评价基础，避免只测API可用 | 六类维度定义、评分标尺、标注一致性和自动指标相关性 |

紧随其后建议阅读：L18用于一致性测试集设计，L24用于LLM评分校准，L21/L22用于章节记忆风险。TOP10中的L03仍属预印本，精读价值不等于正式发表等级。

## 6. 按后续论文用途组织

### 6.1 “国内外研究现状”

建议按问题组织，避免按国内/国外各堆一串系统介绍：

| 研究现状主题 | 优先文献 | 写作边界 |
|---|---|---|
| 创作者主导的人机协作 | L01–L06，补充L07 | 区分系统用户研究、访谈、观点分析和综述 |
| 长故事规划与上下文控制 | L08–L13，L21–L22 | 分清长篇生成、信息检索和摘要任务 |
| 任务化与结构化提示 | L02、L14–L16 | 分清提示调用、神经符号推理和模型微调 |
| 一致性与评价困难 | L17–L25 | 连贯性、源文忠实性、情节漏洞和创造力并非同一指标 |
| AI辅助的收益与限制 | L03、L25–L26 | 自主生成与人机辅助的实验对象不同，表面不同结论不宜写成简单冲突 |
| 中国网络文学场景 | L28–L30 | 提供创作主体与行业背景，不冒充中文核心算法实证研究 |

L27用于整体框架；具体方法效果回到一手论文。不能按作者姓名或拼音推断“国内研究”；中文文献、作者机构和研究场景是不同分类，机构归属待精读核对。

### 6.2 支撑 Writing Skill 的文献

- **任务入口与作者确认：L02、L01、L03、L06。** 解释如何把模型调用放进作者操作，评价候选是否有帮助。
- **大纲规划、情节构思：L08、L09、L11、L12。** 提取任务目标、约束和分步规划；不照搬完整自动创作框架。
- **人物塑造与设定输入：L12、L16。** 支撑人物资料显式组织；人物“塑造质量”仍需本系统专门用例，不能由状态跟踪结果替代。
- **上下文续写：L08–L10、L13。** 提取上下文范围、顺序和预算的比较思路。
- **文本润色：L02、L15。** 前者更接近提示驱动交互，后者用于编辑任务分类；微调结果不能证明本系统模板效果。
- **一致性检查：L17–L20。** 提取检查对象、冲突证据和结果解释。

这些论文支持相关机制，并不证明“Writing Skill”是已有统一学术术语，也不能支撑“首次提出”。本项目仍需用实际的六类任务定义、模板、接口、上下文映射和代码证明实现。

### 6.3 支撑上下文续写

核心L08、L09、L10；背景L13；章节记忆风险与策略L20、L21、L22。建议后续明确“当前正文、人物/世界观、大纲、历史摘要”各自作用，再在相同模型、材料和预算约束下安排对照。是否采用摘要、如何生成和更新，继续遵循基线未定状态；文献本身不作实现决定。

### 6.4 支撑一致性检查

核心L17、L18；局部错误标注L19；摘要忠实性L20、L21；结构化状态相关思路L16。

需分别标注：与人物设定冲突、与世界观冲突、事件/时间冲突、合理状态变化、无法判断。该分类只是待细化的项目测试提案，不能冒充L17原文全部分类。测试集应含无冲突样本；输出需要对应冲突位置和参照资料。不能把模型给出的解释本身当作正确标签。

### 6.5 设计第6章AI功能评价

| 拟评价对象 | 文献依据 | 后续本系统需要补的证据 |
|---|---|---|
| 六类任务的相关性、遵循指令程度与适用性 | L02、L15、L23 | 固定任务与输入、预先定义量表，保留实际输出与模型版本 |
| 续写连贯性及设定符合程度 | L08–L10、L23 | 明确基线与上下文变量，多次生成，记录长度预算和采样设置 |
| 一致性检出与误报 | L17–L19 | 人工核对的有/无冲突材料、正确检出/漏检/误报记录和证据匹配 |
| 章节记忆的忠实与遗漏 | L20–L22 | 对照原文的事实核验，分别记录虚构和遗漏 |
| 作者采纳、修改与控制感 | L01–L03 | 实际交互记录或条件允许时的用户研究，不把“有确认按钮”等同于体验改善 |
| 模型评分可靠性 | L24、L25 | 人工校准样本、固定评审提示、说明自评偏差与分歧处理 |
| 创意与多样性 | L25、L26 | 若纳入评价，明确短文本/小说片段任务、评价单位与材料规模；不强制增加实验 |
| 功能及工程正确性 | 项目实际设计、代码、测试 | 保存、采用、权限、异常、统计、奖励与房间结算等测试记录，不能由上述故事论文替代 |

本阶段不确定样本量、不填写实验数值、不报告显著性。后续设计需说明材料来源及使用条件、模型/提示版本、调用日期、参数、评价人和盲评条件、评分准则与不一致处理。若样本规模有限，报告描述性结果和限制，不强行形成普遍或因果结论。

## 7. 当前缺口与补检优先级

| 优先级 | 缺口 | 当前状态 | 下一轮应解决的问题 |
|---|---|---|---|
| 高 | 中文小说/故事续写与一致性技术的一手实证论文 | 三篇中文文献均为背景或理论/报告解读，不能补足技术证据 | 通过可用的知网、万方、维普或中文期刊官网继续核验具体论文；取得全文再判相关性 |
| 高 | 人物塑造、世界观约束在中文小说场景的独立评价 | L12/L16侧重前提或状态，不足以证明人物塑造质量 | 查找直接针对文本人物设定及人物行为一致性的实验，排除图像人物一致性 |
| 高 | 本系统所选模型及提示条件下的可迁移性 | 全部效果都是他人任务和模型条件下的结果 | 由后续本系统受控测试补足；不能靠增加文献替代 |
| 中 | D5 软件架构、创作资料归属及版本管理 | **本轮未找到足够合适文献** | 围绕文档版本、事务边界和模块化设计聚焦检索；官方技术文档可补实现依据，另列为非论文资料 |
| 中 | D8 状态同步、重复请求、奖励/兑换/拼字结算 | **本轮未找到足够合适文献** | 查找直接可迁移的事务与幂等工程研究；保留协议未定，优先用状态模型和故障/并发测试支撑实际方案 |
| 中 | D7 小说创作者的目标反馈、游戏化及长期影响 | **本轮未找到足够合适文献** | 教育场景需审查迁移条件；补检无效、负面及长期研究，不据短期参与度推导长期创作质量 |
| 中 | D7 背景音乐、禅模式对写作的直接证据 | 本轮未取得可纳入的直接文献，音乐子方向仍需聚焦检索 | 区分偏好、专注、自报体验和客观表现，不提前写“显著提升效率” |
| 中 | D9 可复用的数据源、标签口径、授权与更新机制 | L30提供年度背景，未完成原始数据核验 | 回到原报告及拟选平台核验时间、样本、标签、接口与使用条件；不预定爬取方案 |
| 后续精读必做 | 全文、版本和题录终审 | 中文三篇全文未取；部分正式站直访受限 | 取得全文后标明精读页码；必要时更换入口或剔除，不能补写未见内容 |

D5/D7/D8没有正式候选并不意味着不存在相关研究；本轮是偏向AI创作核心的定向检索。在2022—2026严格时间约束下，也不擅自引入早期经典著作补位。

## 8. 从本轮候选到下一阶段的交接

1. **文献筛选**：以本文件30篇为起点，逐篇判定“保留精读/背景备用/排除”，记录与RQ、六类Skill及具体论述的关系；不预设最终引用数量。
2. **全文获取与精读**：先TOP10，再一致性与评价补充；中文三篇取得全文前只使用已核实摘要层级信息。形成含页码的阅读卡：问题、数据、方法、对照、评价、主要结果、局限、可迁移部分。
3. **证据矩阵**：一条拟写论述对应一手来源和适用条件；遇到结论差异，核对人机协作/自主生成、语言、长度、样本与模型，不能简单选支持预期的一方。
4. **文献综述**：在筛选和精读后按D1/D2/D3/D4/D6主线组织，D5/D7/D8/D9作为相应支撑；区别已有方法、未解决问题和本系统工程定位。
5. **论文目录**：结合实际代码、数据模型与测试条件确定，不由候选论文倒逼新增功能。
6. **正文与最终参考文献**：只有被正文实际引用且终审通过的文献进入最终列表，按学校格式核对卷页、DOI及版本；本文件编号L01—L30不是最终参考文献序号。

### 本轮完成状态

真实检索、可靠来源题录核验、候选分类、逐篇关联分析、总表与TOP10已完成；全文精读、完整文献综述、实验和正文写作未开始。本轮未修改需求基线与研究规划，未生成虚构引用或实验数据。

