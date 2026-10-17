## 2.1.7 前端技术选型

本系统面向PC网页端的小说持续创作，页面既要组织作品和设定资料，也要协调章节目录、正文编辑区与AI辅助面板。技术选型主要考虑组件划分、交互状态管理以及与现有开发准备的衔接。Vue 3、React和Angular均可用于构建此类交互界面，比较重点在于各自的页面组织方式和本项目采用时需要配合的技术。

Vue 3通过声明式模板和响应式数据组织界面，单文件组件可集中描述组件的结构、逻辑和样式。[Vue官方指南](https://vuejs.org/guide/introduction.html)React以组件组织界面，常用JSX表达页面结构，并通过状态更新和组件间数据传递协调交互。[React快速入门](https://react.dev/learn)Angular以组件类和模板组织页面，可使用Signals管理状态，并提供路由、表单等配套能力。[Angular组件说明](https://angular.dev/essentials/components)、[状态管理说明](https://angular.dev/essentials/signals)及[框架概览](https://angular.dev/overview)三种方案都能够支持页面拆分与数据驱动的交互，选择时还需结合项目已有准备和实际组织需求。

本项目已围绕Vue开展前期技术学习和页面方案梳理，并确定Element Plus、Vue Router和Pinia的组合。采用Vue 3可沿用这些准备：按业务划分工作台与资料页面，在编辑页面中协调章节选择、正文和候选结果，通过路由组织页面入口，通过共享状态保持当前作品与章节信息一致。React和Angular也可实现这些需求，但改用其他方案需要重新安排配套组件和应用组织方式。结合本项目规模与开发准备，继续采用Vue 3更符合当前实施安排。

通用表单和列表拟使用Element Plus，正文编辑区域另按创作需要选择组件。Axios用于前后端HTTP通信，ECharts用于个人创作字数和作品情况等折线图、柱状图展示。这些工具分别配合界面、通信与可视化需求，共同组成当前前端方案，而非作为框架性能优劣的判断依据。

## 2.2.6 后端技术选型

本系统后端基于Java 17，采用单体Web应用组织常规创作业务与智能辅助服务。用户认证、资料维护和章节保存需要稳定的请求处理与数据访问分工，因此选用Spring Boot与Spring MVC配合构建后端。Spring Boot通过自动配置组织常用组件，Spring MVC承担Web请求处理，两者共同服务于面向前端的RESTful接口。[Spring Boot自动配置说明](https://docs.spring.io/spring-boot/3.5/reference/using/auto-configuration.html)及[Spring MVC文档](https://docs.spring.io/spring-framework/reference/web/webmvc.html)当前工程采用Spring Boot 3.5.16，沿用该基础可将业务服务与AI辅助入口放在同一应用中维护，符合本项目现有部署和模块组织要求。

持久层主要考虑基础数据操作与自定义查询之间的配合。MyBatis围绕SQL映射组织数据访问，允许通过XML或注解配置查询及结果映射；MyBatis-Plus建立在MyBatis基础上，补充通用CRUD、条件构造与分页等能力，同时保留自定义查询方式。[MyBatis介绍](https://mybatis.org/mybatis-3/)及[MyBatis-Plus介绍](https://baomidou.com/en/introduce/)JPA是Java持久化规范，Hibernate是其常见实现之一，以实体及其关系映射组织持久化，也支持查询语言、条件查询和原生SQL。[Jakarta Persistence规范](https://jakarta.ee/specifications/persistence/3.2/jakarta-persistence-spec-3.2)及[Hibernate ORM说明](https://hibernate.org/orm/)二者体现了不同的数据访问组织方式，不能仅凭采用哪一种就判断查询性能。

本系统的作品、卷章节和创作资料具有较多常规增删改查，个人创作统计与上下文取材又需要按业务组合查询条件。相比主要逐项编写SQL映射，MyBatis-Plus提供的基础操作更贴合这些重复的数据维护需求；相较以实体关系管理为中心的方案，本项目更倾向保留按业务编写查询的方式。因此选择当前工程中的MyBatis-Plus 3.5.17，在使用基础操作的同时，为统计和上下文查询保留专门处理。已有Web工程采用Spring Boot与MyBatis完成业务系统开发[P11]，可作为技术组合的应用参考，本项目选用增强工具则依据自身的数据访问需求。

身份认证方面，Session通常由服务端维护会话信息，客户端通过会话标识关联后续请求；签名JWT则在令牌中携带声明，由后端校验后识别请求身份。[HttpSession文档](https://jakarta.ee/specifications/servlet/6.0/apidocs/jakarta.servlet/jakarta/servlet/http/httpsession)及[RFC 7519](https://www.rfc-editor.org/rfc/rfc7519.html)两种方式都可用于Web认证，前后端分离本身并不排除Session。本系统沿用已确定的JWT方案，将邮箱密码认证后的身份凭证用于接口请求，并结合角色、数据归属和业务规则校验权限。这一选择与当前认证设计一致，不预设其安全性或性能优于Session。

接口协作方面，后续拟结合OpenAPI/Swagger相关描述能力与Knife4j整理请求参数、返回结构和认证要求，供前后端核对与开发调试使用。[Knife4j官方文档](https://doc.xiaominfo.com/docs/quick-start)该部分目前属于技术方案，尚未加入工程依赖。

# 内部审核记录（不进入最终论文）

## 材料与写作范围

- 核对PROJECT_CONTEXT当前v1.7的系统定位、前后端技术及个人创作统计范围；读取RESEARCH_PLAN最新状态。旧版本记录不覆盖现行基线。
- 读取已锁定2.1 V0.3、2.2 V0.2作为技术及语言依据，本轮不改两文件。当前输出的2.1.7、2.2.6仅为待合并小节，总目录未调整。
- 检查pom.xml及src结构：Java 17、Spring Boot 3.5.16、MyBatis-Plus 3.5.17保持；有Web、Security、OAuth2 Resource Server和MySQL驱动依赖。未发现Swagger/Knife4j、Redis依赖。源码仍为基础骨架，本轮没有构建或实现业务。
- 核对FINAL_15_REFERENCES_PLAN和阅读笔记§21.4、§22.4，以及证据矩阵WEB06—08、COMP06—07。15篇全文状态以最新阅读记录为准，不沿用早期“未获取全文”的历史文字。
- 学校指导PDF第6—7页要求联系本系统需求说明选型，并建议同类技术比较。参考往届在线学习平台论文的“需求—比较—结论”组织形式；未沿用其中对React、Angular、JPA等的贬低性判断，也未复制原句。
- 沿用ARS-Codex学术写作流程的证据与项目决定区分方法。正文采用自然段，未增加比较表、性能实验或技术排名。

## 比较对象与取舍

1. Vue 3、React、Angular作为前端界面组织候选，比较组件、状态及配套组织方式。React本身是UI库，Vue和Angular的框架定位与集成范围有差异，本稿按“完成同类前端任务的方案”比较，不声称三者产品层级完全相同。
2. MyBatis、MyBatis-Plus与JPA/Hibernate作为持久层路线比较。明确增强工具与基础框架的关系，以及规范与实现的关系，不将Hibernate和JPA当成两个无关替代框架。
3. Session/JWT仅比较认证方案中身份信息的保存与传递方式；前者是会话机制，后者是令牌格式，并非两套完整安全框架。没有“JWT天然适合分离、Session不适合”的推断。
4. Spring Boot/MVC按现有单体需求说明选择，不强行与Spring Cloud比较，也不贬低其他Spring应用配置方式。无需引入新的后端候选框架来扩大本轮研究。
5. 未加入Element Plus与Ant Design Vue的额外比较：当前论证重点是前端应用组织，没有组件库实测证据。Axios、ECharts、Swagger/Knife4j仅说明配套用途；HTML/CSS等基础技术、MySQL以及不同职责的工具不作强行比较。

## A/B/C证据映射

下列官方资料于2026-10-08核查。链接为研究稿证据锚点，最终Word引用/注释按学校要求处理；不加入冻结的15篇文献。

| 分类 | 正文判断 | 依据与限制 |
| --- | --- | --- |
| A | Vue模板、响应式及单文件组件 | Vue Introduction的Declarative Rendering、Reactivity及Single-File Components；不证明开发者个人熟练度或框架更快 |
| A | React组件、JSX、状态及数据共享 | React Quick Start的Components、JSX、Updating the screen与Sharing data；不评价学习成本高低 |
| A | Angular组件、Signals与配套能力 | Angular Components、Signals、Overview；不将Signals表述为唯一状态方式 |
| A | Boot自动配置与MVC Web请求职责 | Spring Boot 3.5 Auto-configuration、Spring Web MVC；不证明业务已经实现 |
| A | MyBatis映射及MyBatis-Plus增强 | 两者官方Introduction；分页仍需实际配置，自定义查询仍需设计，不声称无需SQL |
| A | JPA实体持久化及多种查询方式 | Jakarta Persistence规范中Entity Operations、Query Language、Criteria API与SQL Queries；Hibernate ORM官方页用于规范实现关系，不否定其SQL能力 |
| A | Session与JWT的身份传递差异 | HttpSession文档关于跨请求会话识别；RFC 7519 §3、§4、§7；不是两者安全或性能比较实验 |
| A | Knife4j接口文档用途 | 官方快速开始；当前未集成状态依据本地pom，不根据网页推断工程状态 |
| A/B | P11工程应用及借鉴 | PDF第4页／刊页21，§2.3、§3.1；证据矩阵WEB06—07。A为原文采用Boot/MyBatis，B为技术组合应用参考；不能推为MP、JWT或本系统效果证据 |
| C | 选择Vue及已有配套组合 | v1.7、已确认前端方案和前期技术准备。正文“已有准备”仅指学习与方案梳理，不表示前端已开发、具备多年经验或已量化学习成本 |
| C | Boot/MVC单体、MP与JWT选择 | 当前基线及工程配置。项目倾向保留业务查询控制，不意味着JPA不能满足相同需求 |

Element Plus、Router、Pinia、Axios及ECharts的配套用途沿用2.1 V0.3已核对的官方来源与边界，本轮没有新增这些工具的比较性结论。P12已回查，但与本稿P11应用案例用途相近，未强行加入正文；其他正式文献不用于证明框架优劣。

## 一致性与未决事项

- 未发现无来源的性能、安全性或效率优劣评价，没有贬低候选技术。选型结论属于本项目适配判断，未声称通过候选系统实现或基准测试得出。
- 与v1.7及锁定2.1、2.2技术内容一致。未恢复行业创作趋势；ECharts仅展示个人业务数据，不定义统计口径或AI质量。
- Swagger/Knife4j仍为拟采用、未集成。业务开发、JWT签发与授权、模型及MCP链路未被描述为已完成。
- Token存储、续期、退出与失效策略仍待详细设计；Redis未写成当前认证实现。新增比较对象不代表项目引入React、Angular、JPA等依赖。
- 未改变技术方案、系统功能、15篇文献或目录文件。两节标题按本轮指定编号给出，后续统一合并目录。

自评：可进入下一轮审核。
