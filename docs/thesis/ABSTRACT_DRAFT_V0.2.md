> 当前版本：V0.2。当前为阶段性摘要，系统实现和第6章测试完成后必须根据真实结果修订为最终版。

# 基于 Spring Boot + Vue 大语言模型的小说智能辅助创作系统设计与实现

## 摘要

大语言模型逐渐应用于文本生成与辅助创作。小说创作篇幅长、过程持续，涉及人物与世界观设定，作者可能面临资料分散、情节构思与正文续接困难、前后内容一致性难以兼顾等问题。本文面向小说创作者，设计网页端智能辅助创作系统，旨在衔接创作资料管理、正文写作与智能辅助。

系统采用Spring Boot与Vue前后端分离架构，围绕作品及卷章节管理、人物与世界观及大纲管理、正文编辑组织创作流程，配套写作计划与创作统计。智能辅助部分调用外部大语言模型，通过Writing Skill组织大纲规划、人物塑造、情节构思、上下文续写、文本润色和一致性检查。上下文管理机制按任务组织作品设定、大纲、人物及前文章节，MCP提供相关创作资源与只读工具的规范化访问。生成内容作为候选，由作者决定修改、采用和保存。

目前已明确系统需求、总体架构与核心智能创作机制，开发与测试尚未完成。后续将结合实际实现开展功能测试、非功能测试、智能创作辅助专项测试及MCP调用链路验证，依据真实结果判断系统对预定功能需求的满足程度与辅助创作机制的适用范围。

关键词：Spring Boot；Vue；大语言模型；智能辅助创作；MCP

# Design and Implementation of an Intelligent Novel Writing Assistance System Based on Spring Boot, Vue, and a Large Language Model

## Abstract

Large language models are increasingly used for text generation and writing assistance. Novel writing involves lengthy texts, sustained work, and numerous character and world-building details. Authors may encounter scattered reference materials, difficulties with plot development and text continuation, and challenges in maintaining consistency. This thesis presents the design of a web-based intelligent writing assistance system for novelists, aiming to connect the management of creative materials, manuscript writing, and intelligent assistance.

The system design adopts a frontend–backend separation architecture using Spring Boot and Vue. It organizes the writing workflow around the management of works, volumes, chapters, characters, world-building information, and outlines, alongside manuscript editing, writing plans, and writing statistics. The intelligent assistance component calls an external Large Language Model (LLM). Writing Skill organizes six tasks: outline planning, character development, plot ideation, context-aware continuation, text polishing, and consistency checking. Context Management assembles story settings, outlines, character information, and preceding chapters according to each task. The Model Context Protocol (MCP) provides standardized access to relevant creative resources and read-only tools. Generated content remains a candidate for authors to revise, adopt, and save at their discretion.

System requirements, the overall architecture, and the core mechanisms for intelligent writing assistance have been defined, while development and testing remain incomplete. Functional tests, non-functional tests, targeted tests of intelligent writing assistance, and verification of the MCP call chain will be conducted as implementation progresses. Actual results will be used to assess whether the system meets its specified functional requirements and to determine the scope of applicability of its writing assistance mechanisms.

Key words: Spring Boot; Vue; Large Language Model; Intelligent Writing Assistance; MCP

---

## V0.2自检记录（不属于摘要正文）

1. 中文摘要为3个自然段，无段内小标题。
2. 正文共449个非空白字符，其中汉字382个。总字符数包含标点、英文字母，不包含题目、关键词、空格与换行。学校300—400字要求仍作为终稿约束：本版汉字数量在该范围内，但按全部字符统计略超过400；不以两种口径互相替代宣称已满足最终排版要求，定稿时按学校实际统计口径复核。
3. 第1段承担背景、实际问题与研究目的；第2段先描述Web业务，再描述六类任务、上下文、MCP及作者确认；第3段记录已明确的需求和机制，并说明后续验证与结论边界。
4. 无虚构实现或测试结果。“目前已明确”指现有需求基线与总体机制，不表示已经完成全部详细设计、代码、接口或测试。第2段为系统设计描述，英文以“system design”对应。未采用“已完成需求分析”这一可能被理解为第3章或完整需求规格说明书已完成的表述。
5. 中英文均为3段，依次对应问题与目的、系统设计、阶段状态与验证计划；英文未增加效果结论。
6. 关键词保留5项，顺序逐项对应：Spring Boot、Vue、大语言模型、智能辅助创作、MCP。“小说创作”较强调领域，“智能辅助创作”更突出本文的辅助系统定位；小说领域已在题目和摘要明确，因此本版选择后者。中文正文中的“智能辅助创作系统”提供对应概念。
7. 相比V0.1，补充长篇持续写作的实际问题，增加完整Web业务的概括，将一段拆为三段；以中文“上下文管理机制”替代中文摘要中的英文名称，保留Writing Skill与MCP；减少“方案”“拟将”，不把设计叙述升级为完成结果。
8. 第3段属于阶段性表述，系统实现和第6章测试完成后须据实际功能、测试条件、结果与限制整体重写，并同步修改英文第3段；第2段也须核对实际采用的技术及实现情况。V0.1保留，项目基线、研究规划、目录、文献名单及阅读记录均不修改，本轮不开展其他章节写作或开发。

