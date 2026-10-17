> 当前版本：V0.1。系统尚未完成开发和测试，摘要中的结果与结论部分将在系统实现和第6章测试完成后根据真实结果重新修订。

# 基于 Spring Boot + Vue 大语言模型的小说智能辅助创作系统设计与实现

## 摘要

针对小说创作中设定资料组织、正文续接与内容一致性核查的需求，本文面向小说创作者，提出网页端智能辅助创作系统方案。方案采用Spring Boot与Vue前后端分离架构，拟将作品资料管理、正文编辑、创作进度反馈与辅助生成融入创作工作流。智能创作体系由大语言模型（LLM）、Writing Skill、Context Management和MCP构成：Writing Skill编排大纲规划、人物塑造、情节构思、上下文续写、文本润色与一致性检查；Context Management选择和组织设定、大纲及前文，MCP负责创作资源与只读工具的标准化访问，后端调用外部LLM生成候选。作者决定是否修改、采用和保存候选内容。当前形成的是总体方案，尚未获得完整实现与测试结果。后续将开展功能、非功能及智能创作辅助专项测试，并核验MCP调用链路，以判断方案对创作需求的满足程度及适用边界，实际辅助效果仍待验证。

关键词：Spring Boot；Vue；大语言模型；小说创作；MCP

# Design and Implementation of an Intelligent Novel Writing Assistance System Based on Spring Boot, Vue, and a Large Language Model

## Abstract

To address the needs for organizing story settings, continuing manuscript text, and checking content consistency in novel writing, this thesis presents a design for a web-based intelligent writing assistance system for novelists. The proposed system uses Spring Boot and Vue in an architecture that separates the frontend from the backend. It is intended to integrate project material management, manuscript editing, writing progress feedback, and assisted generation into the writing workflow. Its AI architecture comprises a Large Language Model (LLM), Writing Skill, Context Management, and the Model Context Protocol (MCP). Writing Skill orchestrates six tasks: outline planning, character development, plot ideation, context-aware continuation, text polishing, and consistency checking. Context Management selects and organizes story settings, outlines, and preceding text. MCP provides standardized access to creative resources and read-only tools, while the backend calls an external LLM to generate candidate content. Authors decide whether to revise, adopt, and save that content. At this stage, the work has produced an overall design, without a complete implementation or test results. Functional testing, non-functional testing, and targeted tests of intelligent writing assistance are planned, together with verification of the MCP call chain. These tests will assess how well the design meets writing needs and identify its limits. Its practical effectiveness remains to be evaluated.

Key words: Spring Boot; Vue; Large Language Model; Novel Writing; MCP

---

## V0.1自检记录（不属于摘要正文）

1. **篇幅：**中文摘要正文392个非空白字符（汉字、标点、英文字母逐字符计数；不含题目、关键词及版本说明），其中汉字275个。学校指导未指定中英文混排的具体计数算法，最终Word排版时按学校采用的统计口径复核。本记录不把英文字母计数称为纯汉字数。
2. **四要素：**第1句为目的；第2—4句为技术方案及作者确认机制；第5句报告当前仅形成总体方案这一阶段性结果；第6句说明验证计划与结论边界。结果和结论尚不是学校终稿所需的实测成果，按本轮要求暂以阶段状态与待验证判断表述。
3. **暂定表述：**“拟将作品资料管理、正文编辑、创作进度反馈与辅助生成融入创作工作流”；“当前形成的是总体方案，尚未获得完整实现与测试结果”；“后续将开展功能、非功能及智能创作辅助专项测试，并核验MCP调用链路，以判断方案对创作需求的满足程度及适用边界，实际辅助效果仍待验证”。其余机制描述受开头“方案”限定，不表示已完成全部功能。
4. **完成度审校：**未使用测试通过、稳定运行、性能达标、准确率、满意度或提效结论；中英文均明确没有完整实现和测试结果。
5. **双语对应：**两版均覆盖目的、网页端创作者定位、Spring Boot/Vue分离架构、工作流、四项AI组成、六类任务、上下文与MCP分工、作者确认、当前进度及后续验证，无新增英文成果。
6. **关键词：**五项依次对应；Spring Boot、Vue、Large Language Model、Novel Writing、MCP与中文五项相同，均可在摘要找到对应概念。英文首次出现MCP已展开全称。
7. **基线一致性：**遵守PROJECT_CONTEXT.md v1.5及已确认目录V1.0。摘要只概括主要业务，不表示省略的激励、沉浸体验等既定功能被删除。未将Writing Skill、Context Management写成某篇文献提出或已验证的系统方案，未声称MCP提升生成质量。
8. **完成系统后必须回修：**核对实际实现的功能、模型接入和MCP链路；用第6章真实测试对象、条件及结果替换计划表达；据实际观察给出有范围的结论并同步修改英文。没有用户研究就不增加满意度或效率改善结论。

写作依据：PROJECT_CONTEXT.md v1.5；RESEARCH_PLAN.md第12节；既有12篇全文阅读卡与证据矩阵。学校《软件工程论文写作指导(1).pdf》第1页规定四要素及300—400字；往届《基于Spring Boot的在线学习平台设计与实现（仅供参考）.docx》摘要仅参考目的—方案—结果的组织，不复制其开场、测试结论或英文表达。已读文献用于限定问题与迁移边界，不在摘要展开综述，不将其数据移作本系统结果。P04/P11/P12未处理。

