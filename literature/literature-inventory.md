# 综述论文 · 种子文献盘点（prior-arts 目录）

> 盘点日期：2026-09-13。来源：`prior-arts/` 目录 9 篇 PDF 首页信息提取。
> 用途：综述 §2–§5 的种子文献；系统性检索（PRISMA）执行前的起点。
> ⚠️ 以下摘要性描述基于首页文本，正式引用前须通读全文核对。

## 核心方法文献（§2.2 PIML 基础）

| # | 文件 | 文献 | 综述落位 |
|---|------|------|----------|
| 1 | `PINN_RPK_2019_1.pdf` | Raissi, Perdikaris, Karniadakis. *Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear PDEs*. JCP 378 (2019) 686–707. 22 页 | §2.2 奠基文献；时间线起点 |
| 2 | `piml_survey_report.pdf` | Hao, Liu, Zhang, Ying, Feng, Su, Zhu. *Physics-Informed Machine Learning: A survey on Problems, Methods and Applications*. 2022. 44 页 | §2.2 已有综述对标（须划界：其为通用 PIML 综述，本文聚焦制造/容差场景） |
| 3 | `2202.10679v2.pdf` | Peng, Saikrishna, Xia. *Physics-Informed Graph Learning*. arXiv 2202.10679. 8 页 | §2.2 物理信息图学习分支 |

## 装配偏差与容差应用文献（§4 应用版图）

| # | 文件 | 文献 | 综述落位 |
|---|------|------|----------|
| 4 | `1-s2.0-S0278612526001743-main.pdf` | Shen, Jing, Liu, Zhao, Du. *Facilitating digital assembly: A physics-informed graph learning framework for prediction of assembly deviations in bolted flange connections*. JMS (2026). 13 页 | §4.1 装配偏差预测 —— **直接竞品文献**，航空发动机螺栓法兰连接 |
| 5 | `1-s2.0-S0278612526000488-main.pdf` | Liu, He, Gao, Zhang, Xu, Bai, Hou. *Digital twin-based high-precision assembly method for large-diameter cabin section docking*. JMS (2026). 21 页 | §4.4 数字孪生装配（大直径舱段对接） |
| 6 | `1-s2.0-S2212827126007432-main.pdf` | Procedia CIRP 145 (2026) 135–140，19th CIRP Conference on Computer-Aided Tolerancing (CAT 2026) 论文 | §4 待通读后精确落位（CAT 2026 会议论文，6 页短文） |
| 7 | `sensors-26-05534.pdf` | *Physics-Informed Multi-Fidelity Graph Learning for ...*. Sensors 26:5534 (2026). 22 页 | §5.1 多保真学习 + 物理信息图学习交叉 |

## 容差设计与知识表示文献（§4.3 / §5.4）

| # | 文件 | 文献 | 综述落位 |
|---|------|------|----------|
| 8 | `s00170-023-12644-y.pdf` | Jia, Zhang, Saad. *Knowledge graph–enabled tolerancing experience acquisition and reuse for tolerance specification*. Int. J. Adv. Manuf. Technol. 129:5515–5539 (2023). 25 页 | §5.4 知识图谱×容差设计（与用户博士研究方向呼应） |
| 9 | `CN122174367A_...pdf` | 王晓喆等（北航）. *一种融合物理信息屈曲代理的曲线纤维机翼智能优化算法*. 中国发明专利申请 CN122174367A (2026). 33 页 | §4.3 容差/变形优化路线；物理信息屈曲代理 + 机翼 —— 与姊妹研究论文场景相邻 |

## 初步观察（待通读全文验证）

1. **直接竞品仅 1 篇**（#4，JMS 2026 物理信息图学习装配偏差预测）——综述的问题空间真实存在，"PIML × 容差分析"尚无专门综述。
2. **文献 #2 是通用 PIML 综述**，本文须明确划界：制造系统层 + 容差/装配场景聚焦。
3. **文献缺口**：多智能体、OOD 鲁棒性、迁移学习在容差代理模型中的应用——现有种子文献未覆盖，恰是 §7 开放挑战的论据，也是姊妹研究论文的切入点。
4. **检索扩展方向**：Kopatsch et al. (2026) PINN 公差分析（pinn.md 提及，prior-arts 未收录）、CGAN-based surrogate for aircraft assembly gaps (2026)、CIRP CAT 会议历年论文集。

## 下一步

- [ ] 执行系统性检索（Scopus/WoS/arXiv），按 outline.md 检索式扩展至 60–100 篇
- [ ] 建立文献编码表（Table 1 雏形）：方法/物理约束机制/应用场景/数据保真度/指标
- [ ] 通读 #4 与 #7 全文，提炼分类法维度
