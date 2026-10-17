# 2.5 MCP协议

MCP（Model Context Protocol，模型上下文协议）是一种连接AI应用与外部数据、工具的开放协议，通过统一的消息和能力描述方式，支持上下文资料访问与工具调用。本系统采用2025-11-25版规范作为设计依据，将MCP用于智能创作任务与系统已保存资料之间的访问衔接，使不同任务能够按需获取背景信息。[MCP规范概述](https://modelcontextprotocol.io/specification/2025-11-25)

MCP架构包含Host、Client和Server三种角色。Host是组织AI应用及管理客户端的宿主；Client位于Host内部，负责与相应Server建立协议连接并交换消息；Server提供可访问的资料与能力。[架构规范](https://modelcontextprotocol.io/specification/2025-11-25/architecture)双方先通过初始化确认协议版本、交换支持的能力，客户端收到初始化响应后发送就绪通知，再进行资源读取和工具调用。[生命周期规范](https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle)

Resource主要表达可读取的上下文资料，由URI标识，客户端通过资源读取请求取得内容。Tool则表达可调用的操作，通过工具名称和输入描述说明如何提交参数并获得结果。[Resources规范](https://modelcontextprotocol.io/specification/2025-11-25/server/resources)及[Tools规范](https://modelcontextprotocol.io/specification/2025-11-25/server/tools)本系统拟将作品概要、人物及关系、世界观、大纲、章节和已有摘要作为资源，使用get_chapter_window等查询工具按作品、章节位置和范围取得所需前文。这些是本项目的资料与查询设计，具体定义留到系统设计章节。

Streamable HTTP是MCP的传输方式之一，使用HTTP承载JSON-RPC 2.0协议消息。客户端以POST向MCP端点发送消息；对于请求，服务端可返回JSON响应或通过SSE传送消息，客户端也可通过GET请求建立接收服务端消息的SSE流。协议允许服务端不提供该GET流并返回相应状态，因此采用这种传输不要求每次调用都流式返回。[传输规范](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)HTTP负责传输，JSON-RPC组织协议方法与结果，其含义与普通业务REST接口不同。

本系统拟由Spring Boot后端的AI编排部分承担Host职责，在同一应用中集成Client与Server，通过回环HTTP完成真实协议通信。Vue仍通过普通业务接口发起创作请求，Server复用创作查询Service提供资料。这种部署是本项目的工程选择：保留单体应用结构，同时让资源访问实际经过MCP消息和传输处理，而非以Java方法直调代替协议链路。

在AI流程中，Writing Skill组织任务，Context Management确定资料范围并调用MCP访问已保存资源和查询工具。上下文续写与一致性检查拟以这一真实链路取得相关背景；当前未保存正文、选中文本和作者要求可直接进入上下文管理，无需先写库再读取。组织后的上下文交给LLM生成候选或检查结果，由作者确认后经普通业务接口保存。MCP承担资料访问职责，生成内容的适用性仍需作者判断与系统测试验证。

# 内部审核记录（不进入最终论文）

## 1. 读取依据与当前状态

- 项目依据为PROJECT_CONTEXT v1.7，重点核对第8、9、14节；RESEARCH_PLAN按最新范围声明理解。现有MCP设计来源于项目基线及任务书对齐报告，没有新增方案。
- 本会话已读取正式任务书、提交指导老师版开题报告、学校指导相关页，以及锁定2.1、2.2、2.3和选型稿。本轮重读2.4职责表述并回查基线协议设计；不宣称每轮重新全文精读所有历史资料。学校指导要求结合实际系统解释技术用途，本稿没有逐条翻译规范或新增三级标题。
- 冻结15篇及阅读笔记、证据矩阵沿用已核验记录。矩阵C02明确P13、P14、P15不支持MCP协议或效果，本节不引用其证明MCP，也不增删15篇名单。
- 本轮再次查看pom.xml与src结构，仍为基础工程，未声明MCP SDK依赖，未发现Client/Server、资源或工具业务代码。没有进行初始化、连接、读取或调用测试，不声称MCP已经落地。

## 2. 官方依据及A/B/C映射

访问日期：2026-10-08。以下均为官方2025-11-25版规范，正文保留对应链接；最终Word的技术资料引用方式按学校要求统一处理，不并入冻结15篇。

| 官方章节 | A：规范支持的事实 | 本稿使用与限制 |
| --- | --- | --- |
| Specification：Overview、Base Protocol | 开放协议、上下文与工具集成、JSON-RPC 2.0 | 不视为模型、RAG或Agent框架，不推导生成质量收益 |
| Architecture：Core Components、Capability Negotiation | Host管理Client；Client与特定Server连接；Server暴露能力；初始化声明功能 | 后端Host、一个自有Server及同应用部署属于C，不要求客户端多开或多Agent |
| Lifecycle：Initialization、Version Negotiation、Capability Negotiation | initialize请求、响应与notifications/initialized通知；版本与能力协商 | 正文为协议流程介绍，不是已经协商成功；实施需记录实际版本 |
| Resources：User Interaction Model、Capabilities、Reading Resources、Resource Templates | URI标识、应用决定上下文纳入方式、资源读取及参数化资源模板 | 项目创作资料属于C；有参数不是Tool的独占特征，本稿未将资源说成只能静态读取 |
| Tools：User Interaction Model、Capabilities、Listing/Calling Tools、Data Types | 命名工具、输入Schema、发现与调用 | 规范允许按应用需要安排交互；不要求本项目让模型自主选择工具。章节窗口为C类既定只读查询，不是内置标准工具 |
| Transports：Streamable HTTP、Sending Messages、Listening for Messages | POST发送单条JSON-RPC消息；请求响应可为JSON或SSE；GET可接收SSE或获405 | 不混同JSON-RPC与REST，也不等同前端模型文本流；服务端收到通知/响应可返回202无正文，正文的JSON/SSE选择限定于“请求” |

B类借鉴是把上下文资源提供与AI任务编排分别组织。C类具体决定包括同应用内嵌Server、回环HTTP、创作Resource、get_chapter_window工具及续写/一致性检查使用真实链路。这些决定来自现行基线，不冒充官方规范或学术论文结论。

## 3. 规范措辞与实施回核

官方Transports的Streamable HTTP开头将Server描述为“independent process”；该句是传输部署概述，未给出Host与Server必须运行在不同操作系统进程的MUST条款。本稿不将同进程回环部署说成规范示例或已获SDK兼容性证明，仍按已确认的同应用方案表述。实际SDK对内嵌Server、MVC适配及回环通信的支持须在实现时核验；本轮不擅自拆分进程或改变架构。

协议安全要求及用户授权仍需落实，回环地址本身不保证权限安全。Origin检查、认证、接口暴露范围、资源归属、工具参数校验等留第4章；不因本节简述省略基线中的相关约束。Tool的模型控制设计取向不意味着本系统必须引入自主Agent；应用仍需落实用户对资料访问和操作的知情与控制。

## 4. 一致性检查

- Host、Client、Server按协议角色说明，没有把Vue作为MCP Client或让它直连Server。MCP不替代Spring Service或普通业务REST接口。
- Resource用于资料读取，Tool用于可调用操作；既定查询示例没有扩展为自动写正文工具。未在正文固定URI、Schema或参数表。
- 保留真实Streamable HTTP协议链路要求，不用普通Java直调冒充调用；基线的故障降级不等于MCP验收成功，后续核心链路须按既定关闭fallback条件验证。
- 与2.4一致：Skill组织任务，Context Management决定和组合资料，MCP访问已保存资料，LLM生成与分析。当前输入可直接参与上下文，不建立“全部输入必须经MCP”的约束。
- 作者确认后才进入正式保存，未写自动覆盖；没有协议提升准确率、一致性或创作效率的结论。
- SDK版本、兼容性和具体组件尚待实现核验；没有新增Spring AI、第二套Web栈、模型供应商或其他技术决定。
- 第4章展开资源/工具、权限及架构流程，第5章说明真实通信代码，第6章提供实际初始化、发现、读取、调用及失败路径测试。正文未提前填写实现和测试成果。
- 本轮仅新建本文件，没有修改基线、规划、目录、任务书、开题报告、文献、锁定正文、pom.xml或代码，也未开始2.6。

自评：可进入审核；同应用SDK适配属于后续实施核验事项，不是本轮已验证事实。
