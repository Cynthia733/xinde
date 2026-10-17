> 内部版本标识：V0.3，毕业论文最终完成态口吻的摘要预稿（不是当前完成情况的事实报告）。
> 内部备注（最终不放入论文正文）：V0.3采用毕业论文最终完成态进行预写。系统实际开发和第6章测试完成后，必须逐项核对摘要中所有‘已实现’‘已完成’‘测试’及结论性表述；若实际实现或测试结果与预稿不一致，以真实结果为准进行修改。

# 基于 Spring Boot + Vue 大语言模型的小说智能辅助创作系统设计与实现

## 摘要

大语言模型逐渐应用于文本生成与辅助创作。小说创作篇幅长、过程持续，涉及人物与世界观设定，作者可能面临资料分散、情节构思与正文续接困难、前后内容一致性难以兼顾等问题。本文面向小说创作者，设计并实现了网页端智能辅助创作系统，旨在衔接创作资料管理、正文写作与智能辅助。

系统采用Spring Boot与Vue前后端分离架构，围绕作品及卷章节管理、人物与世界观及大纲管理、正文编辑组织创作流程，配套写作计划与创作统计。智能辅助部分调用外部大语言模型，通过Writing Skill组织大纲规划、人物塑造、情节构思、上下文续写、文本润色和一致性检查。上下文管理机制按任务组织作品设定、大纲、人物及前文章节，MCP提供相关创作资源与只读工具的规范化访问。生成内容作为候选，由作者决定修改、采用和保存。

系统实现后，开展了功能测试、非功能测试和智能创作辅助专项测试，并验证了MCP资源读取与工具调用链路。测试围绕核心业务、候选内容确认及上下文访问流程展开，用于检验功能完整性和主要流程的正确性。本研究形成了以作者决策为核心、连接创作资料与智能辅助任务的系统实现。

关键词：Spring Boot；Vue；大语言模型；智能辅助创作；MCP

# Design and Implementation of an Intelligent Novel Writing Assistance System Based on Spring Boot, Vue, and a Large Language Model

## Abstract

Large language models are increasingly used for text generation and writing assistance. Novel writing involves lengthy texts, sustained work, and numerous character and world-building details. Authors may encounter scattered reference materials, difficulties with plot development and text continuation, and challenges in maintaining consistency. This thesis presents the design and implementation of a web-based intelligent writing assistance system for novelists, aiming to connect the management of creative materials, manuscript writing, and intelligent assistance.

The system adopts a frontend–backend separation architecture using Spring Boot and Vue. It organizes the writing workflow around the management of works, volumes, chapters, characters, world-building information, and outlines, alongside manuscript editing, writing plans, and writing statistics. The intelligent assistance component calls an external Large Language Model (LLM). Writing Skill organizes six tasks: outline planning, character development, plot ideation, context-aware continuation, text polishing, and consistency checking. Context Management assembles story settings, outlines, character information, and preceding chapters according to each task. The Model Context Protocol (MCP) provides standardized access to relevant creative resources and read-only tools. Generated content remains a candidate for authors to revise, adopt, and save at their discretion.

Following implementation, functional tests, non-functional tests, and targeted tests of intelligent writing assistance were conducted, together with verification of the MCP resource-reading and tool-calling chain. The tests covered core business functions, candidate content confirmation, and context access to examine functional completeness and the correctness of the main workflows. The work produced a system implementation that connects creative materials with intelligent assistance tasks while keeping authors in control of decisions.

Key words: Spring Boot; Vue; Large Language Model; Intelligent Writing Assistance; MCP

---

## 内部自检与事实核验清单（不属于摘要正文）

- 中文摘要3段，共470个非空白字符，其中汉字401个；统计不含标题、关键词、空格、换行及内部备注。英文字母与标点计入总字符数。中英文均保持3段。
- V0.2至V0.3：第1段末句由“设计”改为“设计并实现了”；第2段中文保持不变，英文删除“system design”中的设计限定；第3段整体改为测试活动与系统实现的完成态叙述。标题和五项关键词不变。
- 以下句子均属于最终完成态预写（含第2段现在时描述的已运行机制），必须在实际开发及第6章测试完成后逐项复核；英文对应句同步复核：

1. **待事实核验：**本文面向小说创作者，设计并实现了网页端智能辅助创作系统，旨在衔接创作资料管理、正文写作与智能辅助。
2. **待事实核验：**系统采用Spring Boot与Vue前后端分离架构，围绕作品及卷章节管理、人物与世界观及大纲管理、正文编辑组织创作流程，配套写作计划与创作统计。
3. **待事实核验：**智能辅助部分调用外部大语言模型，通过Writing Skill组织大纲规划、人物塑造、情节构思、上下文续写、文本润色和一致性检查。
4. **待事实核验：**上下文管理机制按任务组织作品设定、大纲、人物及前文章节，MCP提供相关创作资源与只读工具的规范化访问。
5. **待事实核验：**生成内容作为候选，由作者决定修改、采用和保存。
6. **待事实核验：**系统实现后，开展了功能测试、非功能测试和智能创作辅助专项测试，并验证了MCP资源读取与工具调用链路。
7. **待事实核验：**测试围绕核心业务、候选内容确认及上下文访问流程展开，用于检验功能完整性和主要流程的正确性。
8. **待事实核验：**本研究形成了以作者决策为核心、连接创作资料与智能辅助任务的系统实现。

核验材料应覆盖：实际功能与代码、六类任务执行、上下文组装、MCP Resource/Tool真实调用记录、候选确认与保存行为，以及第6章各类测试记录。出现“验证了”只预写执行过验证活动，不表示已全部通过或达到任何效果目标；若该活动未实际开展，须删除或按事实改写。

- 数据与效果审校：未写任何响应时间、并发量、通过率、准确率、提升比例、满意度或显著性；未以“结果表明”宣称性能、质量或效率改善。末句仅总结预设的系统实现与作者决策定位，不声称主体性或体验已获实证改善。
- 真实性状态：不存在虚构的量化结果或预设的效果改善结论；存在用户明确授权的、尚未得到实际完成证据支持的实现与测试活动预写，不能作为当前事实或未经核验直接提交。
- 关键词保持Spring Boot、Vue、大语言模型、智能辅助创作、MCP；英文逐项对应、顺序一致。MCP首次出现英文全称，未赋予其生成质量改善结论。
- 本轮仅新建V0.3，V0.1/V0.2、项目基线、研究规划、目录及文献文件保持不变；不开展系统开发或其他章节写作。
