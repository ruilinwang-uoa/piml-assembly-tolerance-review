# 系统性文献检索日志（PRISMA 留痕）

- 检索日期: 2026-09-13
- 时间窗: 2019-01-01 ~ 2026-12-31
- 数据库: OpenAlex（主，works search，per_page=100）+ Semantic Scholar（辅，bulk search）

| 检索式编号 | 数据库 | 检索式 | 总命中 | 抓取 | 状态 |
|---|---|---|---|---|---|
| Q1 | OpenAlex | `"physics-informed" AND (tolerance OR tolerancing)` | 7646 | 100 | OK |
| Q2 | OpenAlex | `"physics-informed" AND ("assembly deviation" OR "assembly gap" OR "gap prediction")` | 117 | 100 | OK |
| Q3 | OpenAlex | `"physics-informed neural network" AND (manufacturing OR assembly)` | 6802 | 100 | OK |
| Q4 | OpenAlex | `"physics-guided" AND (tolerance OR assembly OR manufacturing)` | 3333 | 100 | OK |
| Q5 | OpenAlex | `"physics-informed" AND surrogate AND (manufacturing OR assembly)` | 5098 | 100 | OK |
| Q6 | OpenAlex | `"physics-informed graph learning"` | 82 | 82 | OK |
| Q7 | OpenAlex | `"physics-informed" AND ("digital twin") AND (manufacturing OR assembly)` | 4200 | 100 | OK |
| S2-Q1 | SemanticScholar | `"physics-informed" AND (tolerance OR tolerancing)` | - | 0 | FAIL: 429 Client Error:  for url: https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=physics-informed%20AND%20%28tolerance%20OR%20tolerancing%29&fields=title,authors,year,venue,externalIds,citationCount,abstract&year=2019-2026&limit=100 |
| S2-Q2 | SemanticScholar | `"physics-informed" AND ("assembly deviation" OR "assembly gap" OR "gap prediction")` | - | 0 | FAIL: 429 Client Error:  for url: https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=physics-informed%20AND%20%28assembly%20deviation%20OR%20assembly%20gap%20OR%20gap%20prediction%29&fields=title,authors,year,venue,externalIds,citationCount,abstract&year=2019-2026&limit=100 |
| S2-Q6 | SemanticScholar | `"physics-informed graph learning"` | 725 | 725 | OK |

## 汇总

- 抓取总量（去重前）: 1407
- 去重后文献池: 1264
- 去重规则: DOI 优先，缺失时用规范化标题
- 排序: 关键词相关性粗打分（仅排序用，不作纳入决定）

## 下一步（PRISMA 筛选项）

- [ ] 标题/摘要筛查：剔除明显越界（流体/医学/气候等）与无物理约束机制的论文
- [ ] 全文评估：对高分文献执行纳入/排除标准
- [ ] 追溯滚雪球：对核心文献做引用追踪（S2 citations API）

## 三级分层结果（2026-09-13）

自动分层规则（标题+摘要关键词）：Tier A = 物理信息方法 × 容差/装配/偏差；Tier B = 物理信息方法 × 制造/结构相邻领域；Tier C = 其余 PIML 通用方法。

| 层级 | 数量 | 说明 |
|---|---|---|
| Tier A 核心 | 37 | 含约 40% 误报（band gap/光学装配/地震反演等词碰撞），人工初筛后有效约 15–20 篇 |
| Tier B 邻近 | 305 | 制造/结构/复合材料方向 PIML，综述 §5 使能技术主要来源 |
| Tier C 背景 | 922 | PIML 通用方法，仅取高被引奠基文献进 §2.2 |
| **合计** | **1264** | |

年度分布见 `figures/fig1-publication-trend.png`（Tier A+B 从 2019 年 5 篇增至 2025 年 74 篇，2026 年前 9 个月已 127 篇——领域处于爆发期，支撑综述立论）。

人工初筛产出 `literature/coding-table.md`（26 条编码，全文核对前不作最终引用依据）。

## 第二轮：全文筛查 + 定向补检（2026-09-13 晚）

### Tier A（首轮 37 篇）摘要级全文筛查结论
- **纳入 6 篇**：A01 飞机长桁装配 PIML 动态预测、A04 光学镜头主动对准（边缘）、A13 SmartFixture 夹具布局、A22 JMS 物理信息图学习法兰装配、A32 聚合物挤出质量（边缘）、A34 torsor 刚柔混合大尺度装配
- **排除 31 篇**：band gap 材料信息学（5）、地震反演（3）、电力系统（5）、声学/光学（2）、Galerkin "assembly" 词碰撞（2）、生物/化学（6）、其他越界（8）

### 补充检索式 Q8–Q14（时间窗放宽至 2015 起，捕捉传统容差文献）
| 检索式 | 主题 | 总命中 | 抓取 |
|---|---|---|---|
| Q8 | 容差分析 × ML/NN/DL | 1500 | 100 |
| Q9 | 变动传播 × 装配 × 学习/代理 | 161 | 100 |
| Q10 | Skin Model × 容差/装配 | 5687 | 100 |
| Q11 | 容差分配 × 学习/代理 | 312 | 100 |
| Q12 | 几何/形状/尺寸偏差 × 装配 × 预测 | 2211 | 100 |
| Q13 | Kopatsch 定向 | 15 | 15（**未命中目标论文**，结果为 DNA 纳米技术等同名噪声） |
| Q14 | GAN/CGAN × 装配间隙 | 49 | 49 |

### 本轮结论
- 文献池 1264 → **1779**（新增 515）
- 编码表 v2：**89 条 / 8 组**（G1 PIML×装配核心 8、G2 数字孪生 5、G3 数据驱动偏差预测 14、G4 传统容差与变动建模 30、G5 容差分配优化 10、G6 PIML 使能技术 12、G7 方法综述背景 8、G8 知识表示×容差 2）
- 重要收获：DeviationGAN (MSSP 2023)、NN-GP 复材装配 (TMech 2020)、物理约束 BO 复材装配 (TASE 2022)、A Review on Variation Modeling of Aircraft Assembly (2023，**直接相邻综述，须划界**)、Skin Model Shapes 系列（Schleich/Anwer 学派）
- 未决：Kopatsch et al. (2026) 与 "CGAN-based surrogate for aircraft assembly gaps (2026)" 均未检获；后者疑与"流形学习 GAN 装配应力场 (Thin-Walled Structures 2026)"相关，待核对


---

# 第三轮：全量无上限重检索（2026-09-17 至 09-19）

- 动机：评审发现第一/二轮 OpenAlex 每式仅抓取相关性 top-100（未披露截断）；用户裁决全量无上限重检。
- 执行历史：Q1–Q7 以原式在 OpenAlex 逐查询×逐单年光标分页全量抓取（2026-09-17/18 跨三窗口完成，本 IP 共享日配额 1000 请求多次被并发流量耗尽，断点缓存见 literature/archive/oa-Q*.json）；Q8–Q14 因配额持续被抢占，经用户裁决改道 **Semantic Scholar bulk search + Crossref bibliographic search 双源执行**（2026-09-19，v2 重拟串，Q8/Q11 于 09-19 短语收紧）。S2 三式含此前 429 失败项的退避重试；滚雪球（G1+G2 核心引用追踪，首轮未执行待办）已执行。
- 检索式来源披露：Q1–Q7 原式逐字（search_literature.py）；Q8–Q14 原串未存档，v2 重拟。

| 检索式编号 | 数据库 | 检索式 | 总命中 | 抓取 | 状态 |
|---|---|---|---|---|---|
| Q1 | OpenAlex（原式全量，断点缓存） | - | - | 7848 | OK |
| Q2 | OpenAlex（原式全量，断点缓存） | - | - | 120 | OK |
| Q3 | OpenAlex（原式全量，断点缓存） | - | - | 6949 | OK |
| Q4 | OpenAlex（原式全量，断点缓存） | - | - | 3421 | OK |
| Q5 | OpenAlex（原式全量，断点缓存） | - | - | 5247 | OK |
| Q6 | OpenAlex（原式全量，断点缓存） | - | - | 85 | OK |
| Q7 | OpenAlex（原式全量，断点缓存） | - | - | 4318 | OK |
| Q8 | SemanticScholar | `"tolerance analysis" AND ("machine learning" OR "neural network" OR "deep learning")` | - | 0 | FAIL: GET failed: https://api.semanticscholar.org/graph/v1/paper/search/bulk :: <Response [429]> |
| Q9 | SemanticScholar | `("variation propagation" OR "dimensional variation") AND assembly AND (learning OR surrogate)` | - | 0 | OK |
| Q10 | SemanticScholar | `"skin model" AND (tolerance OR assembly)` | - | 70 | OK |
| Q11 | SemanticScholar | `"tolerance allocation" AND ("machine learning" OR surrogate OR optimization)` | - | 0 | OK |
| Q12 | SemanticScholar | `("geometric deviation" OR "form deviation" OR "dimensional deviation") AND assembly AND prediction` | - | 4 | OK |
| Q13 | SemanticScholar | `Kopatsch AND (physics-informed OR tolerance)` | - | 0 | OK |
| Q14 | SemanticScholar | `("generative adversarial" OR GAN) AND assembly AND (gap OR deviation)` | - | 0 | OK |
| Q8 | Crossref | `"tolerance analysis" AND ("machine learning" OR "neural network" OR "deep learning")` | - | 5000 | OK |
| Q9 | Crossref | `("variation propagation" OR "dimensional variation") AND assembly AND (learning OR surrogate)` | - | 5000 | OK |
| Q10 | Crossref | `"skin model" AND (tolerance OR assembly)` | - | 5000 | OK |
| Q11 | Crossref | `"tolerance allocation" AND ("machine learning" OR surrogate OR optimization)` | - | 5000 | OK |
| Q12 | Crossref | `("geometric deviation" OR "form deviation" OR "dimensional deviation") AND assembly AND prediction` | - | 5000 | OK |
| Q13 | Crossref | `Kopatsch AND (physics-informed OR tolerance)` | - | 5000 | OK |
| Q14 | Crossref | `("generative adversarial" OR GAN) AND assembly AND (gap OR deviation)` | - | 5000 | OK |

## 汇总（第三轮）

- 抓取总量（去重前）: 64393
- 去重后文献池: **46239**（分层: {'C': 44895, 'B': 1190, 'A': 154}；分层规则为 v2 内容规则，title+abstract，缺摘要记录按 title 判层）
- 旧池（1,779）已备份: literature/archive/pool-v1.csv
- 完整机器日志: literature/harvest-v2-log.json
