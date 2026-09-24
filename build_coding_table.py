# -*- coding: utf-8 -*-
"""生成文献编码表 v2（Table 1 雏形，60+ 条，分组编码）
数据: literature/pool.csv 元数据 + 人工编码维度（基于标题/摘要，待全文核对）
"""
import csv
from pathlib import Path

LIT = Path(__file__).parent / "literature"
pool = list(csv.DictReader(open(LIT / "pool.csv", encoding="utf-8-sig")))

def find(frag):
    frag = frag.lower()
    hits = [r for r in pool if frag in r["title"].lower()]
    return hits[0] if hits else None

# 种子文献与匹配失败条目的手动元数据（来自 prior-arts 本地 PDF 盘点）
FALLBACK = {
 "D01": ("Digital twin-based high-precision assembly method for large-diameter cabin section docking","2026","J. Manuf. Syst.","0","10.1016/j.jmsy.2026.02.019"),
 "T30": ("A coordination modelling approach for assembly of multi-constrained objects based on measured skin model","2019","Assembly Autom.","11","10.1108/aa-04-2018-058"),
 "C01": ("Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear PDEs","2019","J. Comput. Phys.","高被引","10.1016/j.jcp.2018.10.045"),
 "C03": ("Physics-Informed Machine Learning: A survey on Problems, Methods and Applications","2022","arXiv（种子PDF）","—","—"),
 "C04": ("Physics-Informed Neural Network (PINN) Evolution and Beyond: A Systematic Literature Review and Meta-Analysis","2022","Big Data Cogn. Comput.","255","10.3390/bdcc6040140"),
 "K01": ("Knowledge graph–enabled tolerancing experience acquisition and reuse for tolerance specification","2023","Int. J. Adv. Manuf. Technol.","—","10.1007/s00170-023-12644-y"),
 "K02": ("一种融合物理信息屈曲代理的曲线纤维机翼智能优化算法（发明专利申请）","2026","CN122174367A","—","—"),
 "A10": ("Leveraging Physics-Informed Neural Networks for Efficient Tolerance Analysis","2026","Procedia CIRP","0","10.1016/j.procir.2026.03.130"),
 "A11": ("Adaptive Planning Method for ERS Point Layout in Aircraft Assembly Driven by Physics-Based Data-Driven Surrogate Model","2026","Sensors","0","10.3390/s26030955"),
 "M15": ("Predicting aircraft assembly gaps considering structural deformation: A CGAN-based surrogate modeling approach","2026","J. Manuf. Syst.","0","10.1016/j.jmsy.2025.12.018"),
}

# (编号, 标题匹配片段, 方法类别, 物理融入机制, 应用场景, 数据保真度, 备注)
CURATED = [
# ===== G1 PIML×装配/容差 核心 =====
("A01","A Dynamic Prediction Method for Assembly Quality Based on Physics-Informed","PIML+机理","损失嵌入(偏差机理)","飞机长桁装配偏差动态预测","实测+机理","核心"),
("A02","Facilitating digital assembly","PIGL","混合(图+物理损失)","螺栓法兰连接装配偏差预测","仿真+实测","核心/直接竞品"),
("A03","Physics-Constrained Bayesian Optimization for Optimal Actuators Placement","物理约束BO","约束嵌入","复合材料结构装配作动器布局","仿真","核心"),
("A04","hybrid rigid-compliant computational framework for large-scale assembly","传统+ML混合","架构嵌入(torsor)","大尺寸装配变动传播","仿真","核心(非PIML基线)"),
("A05","SmartFixture","物理引导RL","约束嵌入","薄壁件夹具布局(装配变形)","FEA仿真","核心邻近"),
("A06","Fast and accurate active alignment of camera lenses","物理信息DL","损失嵌入","光学镜头主动对准(精密装配)","实测","边缘核心"),
("A07","Physics-Informed Multi-Fidelity Graph Learning","PIGL","混合","多保真图代理(场景待通读)","多保真","种子"),
("A08","A manifold learning-assisted generative adversarial network for rapid assembly stress","流形学习+GAN","数据嵌入(物理流形)","装配应力场快速预测","仿真","生成式路线"),
("A09","Assembly‐Deviation‐Induced Sealing Leakage in PEMFC Stacks","混合建模","机理+数据","装配偏差→密封泄漏(燃料电池)","单保真","偏差功能后果"),
("A10","Leveraging Physics-Informed Neural Networks for Efficient Tolerance Analysis","PINN","损失嵌入","容差分析直接应用(CAT2026)","仿真","核心/Kopatsch，pinn.md 引用"),
("A11","Adaptive Planning Method for ERS Point Layout in Aircraft Assembly","物理代理","混合","飞机装配 ERS 点布局规划","仿真","核心邻近"),
# ===== G2 数字孪生与在线几何保证 =====
("D01","Digital twin-based high-precision assembly method for large-diameter cabin","数字孪生","数据嵌入","大直径舱段对接装配","多保真(DT)","种子"),
("D02","Digital Twin-driven Inversion of Assembly Precision","数字孪生+ML","数据嵌入","工业装备装配精度反演","多保真(DT)","核心"),
("D03","Online geometry assurance in individualized production","数字孪生","模型校准","钣金件装配在线几何保证","实测+仿真","核心"),
("D04","Digital Twin-Based Clamping Sequence Analysis","数字孪生","数据嵌入","钣金装配夹紧序列优化","仿真","邻近"),
("D05","Quality Prediction and Control of Assembly and Welding Process for Ship","数字孪生","数据嵌入","船舶装配焊接质量预测","实测","邻近"),
# ===== G3 数据驱动/ML 偏差预测（非物理信息） =====
("M01","DeviationGAN","GAN","无(纯数据)","钣金装配偏差端到端预测","仿真+实测","生成式/对比基线"),
("M02","Neural Network Gaussian Process Considering Input Uncertainty","NN-GP","输入不确定性建模","复合材料结构装配偏差与残余应力","仿真","对比基线"),
("M03","Gaussian Processes with Input Location Error","GP","输入误差建模","复合材料装配过程","仿真","对比基线"),
("M04","Surrogate model–based optimal feed-forward control","代理模型","无","复合材料件尺寸变动前馈控制","仿真","对比基线"),
("M05","Anomaly detection in Skin Model Shapes using machine learning","ML分类","无","Skin Model Shapes 异常检测","仿真","SMS+ML交叉"),
("M06","multilayer shallow learning approach to variation prediction","浅层学习","无","多工序加工变动预测与溯源","实测","对比基线"),
("M07","Inspection by exception","ML","无","多工序制造质量预测","实测","对比基线"),
("M08","Bayesian framework to estimate part quality","贝叶斯","不确定性建模","多工序制造件质量估计","实测","对比基线"),
("M09","FDQN-based tolerance closed-loop optimization","深度RL","无","飞机薄壁件容差闭环优化","仿真","容差分配+RL"),
("M10","Predicting geometric parameters of assemblies with neural network","NN","无","装配几何参数预测","仿真","早期NN路线"),
("M11","surrogate model–based method for individualized spot welding sequence","代理模型","无","点焊序列优化(几何偏差)","仿真","对比基线"),
("M12","Critical joint identification for efficient sequencing","ML","无","焊点序列优化","仿真","对比基线"),
("M13","Reduced-order modelling for real-time physics-based variation simulation","降阶模型","物理模型降阶","柔顺装配变动实时仿真","仿真","多保真/实时化"),
("M14","Multi-task learning with state propagation","多任务ML","状态传播约束","聚合物挤出质量预测","实测","边缘核心"),
("M15","Predicting aircraft assembly gaps considering structural deformation","CGAN代理","无(纯数据)","飞机装配间隙预测(结构变形)","仿真","直接竞品/JMS，pinn.md 引用"),
# ===== G4 传统容差分析与变动建模（§2.1 基线） =====
("T01","Skin Model Shapes: Offering New Potentials","Skin Model Shapes","—","形状变动建模范式","—","SMS奠基"),
("T02","Status and Prospects of Skin Model Shapes","Skin Model Shapes","—","几何变动管理综述","—","SMS综述"),
("T03","Integrating form errors and local surface deformations into tolerance analysis","SMS+FEA","—","形状误差+局部变形容差分析","仿真","CAD期刊"),
("T04","Manufacturing signature in jacobian and torsor models","Jacobian-Torsor","—","刚性件容差分析(制造签名)","仿真","经典模型"),
("T05","Manufacturing signature in variational and vector-loop models","Variational/Vector-loop","—","刚性件容差分析","仿真","经典模型"),
("T06","Assembly tolerance analysis based on the Jacobian model and skin model","Jacobian+SMS","—","装配容差分析","仿真","模型融合"),
("T07","Polytope-based tolerance analysis with consideration of form defects","Polytope","—","CAT多胞体模型","仿真","经典模型"),
("T08","generic integrated approach of assembly tolerance analysis based on skin model","SMS","—","装配容差分析通用框架","仿真","SMS集成"),
("T09","Statistical Tolerance Analysis Based on Good Point Set","统计法","—","统计容差分析","仿真","统计路线"),
("T10","Integration of Thermal Effects into Tolerancing","SMS+热","—","热变形融入容差","仿真","多物理扩展"),
("T11","3D Tolerance Analysis with Manufacturing Signature and Operating Conditions","制造签名","—","工况融入3D容差分析","仿真","工况扩展"),
("T12","Assembly accuracy analysis of cylindrical parts based on skin model shapes","SMS","—","回转件装配精度","仿真","SMS应用"),
("T13","assembly accuracy analysis approach of mechanical assembly involving parallel and serial","NSMS","—","并/串联装配偏差传播","仿真","非高斯SMS"),
("T14","Assembly accuracy analysis and phase optimization of aero-engine multistage rotors","变动建模","—","航空发动机多级转子装配相位优化","实测","航空场景"),
("T15","Virtual Geometry Assurance Process and Toolbox","几何保证","—","虚拟几何保证流程","实测+仿真","工业流程"),
("T16","Challenges of Geometrical Variations Modelling in Virtual Product Realization","综述","—","变动建模挑战","—","问题定义"),
("T17","A Review on Variation Modeling of Aircraft Assembly","综述","—","飞机装配变动建模综述","—","直接相邻综述/划界对象"),
("T18","Systems Thinking in Tolerance and Quality-related Design","系统思维","—","容差-质量设计决策","—","系统层视角"),
("T19","comprehensive study of tolerance analysis methods for rigid parts","综述","—","刚性件容差分析方法比较","仿真","方法比较"),
("T20","Investigating the potential of ontologies to enable knowledge-based tolerancing","本体","—","CNC铣削件知识化容差","知识","CAT2026/K类交叉"),
("T21","Towards Seamless Integration: Embedding Advanced Geometric Tolerance Models","系统级仿真","—","系统级仿真中的几何容差模型","仿真","CAT2026"),
("T22","Variation Simulation During Assembly of Non-rigid Components","柔顺装配仿真","—","非刚性件装配仿真(ANATOLEFLEX)","仿真","商业工具链"),
("T23","Efficient Spot Welding Sequence Simulation in Compliant Variation Simulation","柔顺装配仿真","—","点焊序列变动仿真","仿真","经典路线"),
("T24","fixture layouts for compliant sheet metal assemblies","夹具优化","—","柔顺钣金装配夹具布局","仿真","经典路线"),
("T25","Development of Fixture Layout Optimization for Thin-Walled Parts","综述","—","薄壁件夹具布局优化综述","—","综述"),
("T26","Numerical Process Based on Measuring Data for Gap Prediction","实测驱动","—","航空装配间隙预测","实测","间隙预测早期"),
("T27","Bridging the gap between design and manufacturing specifications for non-rigid","影响系数法","—","非刚性件设计-制造规范衔接","仿真","ICM路线"),
("T28","Decomposing deviations of scanned surfaces of sheet metal assemblies","FEA+实测","—","钣金装配扫描表面偏差分解","实测","汽车行业"),
("T29","Variation Analysis Considering the Partial Parallel Connection in Aero-Engine Rotor","变动分析","—","航空发动机转子装配变动","仿真","航空场景"),
("T30","assembly coordination modelling approach","实测驱动","—","飞机多约束对象装配协调","实测","数字镜像"),
("T31","Octree-Based Generation and Variation Analysis of Skin Model Shapes","SMS生成","—","Skin Model Shapes 八叉树生成与变动分析","仿真","SMS工具链"),
# ===== G5 容差分配与优化（§4.3） =====
("O01","Optimal Tolerance Allocation in a Complex Assembly Using Evolutionary","进化算法","—","复杂装配容差分配","仿真","优化路线"),
("O02","Ontological model-based optimal determination of geometric tolerances","本体+优化","—","非刚性装配几何容差确定","知识+仿真","K类交叉"),
("O03","Sampling-based tolerance analysis","采样优化","—","容差-成本优化","仿真","成本路线"),
("O04","Dimensional tolerance optimization of SAR antennas","UQ+可靠性","—","SAR天线尺寸容差优化","仿真","UQ交叉"),
("O05","Tolerance Optimization of Patch Parameters for Locally Reinforced Composite","优化","—","复合材料局部加强容差","仿真","复材场景"),
("O06","Toward cost-efficient tolerancing of 3D-printed parts","成本建模","—","增材制造容差-成本","实测","AM场景"),
("O07","Tolerance management during the design of composite structures","变动管理","—","复材结构设计容差管理","仿真","复材场景"),
("O08","Optimal tolerance allocation based on Difficulty matrix using FMECA","FMECA","—","容差分配难度矩阵","—","方法交叉"),
("O09","Visual quality and sustainability considerations in tolerance optimization","优化","—","视觉质量-可持续容差优化","—","市场视角"),
("O10","Coaxiality error analysis and optimization of cylindrical parts of CNC turning","误差优化","—","CNC车削同轴度","实测","加工端"),
# ===== G6 PIML 使能技术（§5） =====
("E01","Physics-informed neural networks for data-free surrogate modelling","PINN","损失嵌入","工程优化代理(无数据)","无数据","代理奠基"),
("E02","Accelerating Thermal Simulations in Additive Manufacturing","PINN","损失嵌入","增材热仿真加速","仿真","AM使能"),
("E03","Physics-Informed Online Learning for Temperature Prediction in Metal AM","PINN+在线学习","损失嵌入","金属AM温度场在线预测","在线数据","在线学习"),
("E04","Solving forward and inverse problems of contact mechanics","PINN","损失嵌入","接触力学正逆问题","仿真","装配相邻"),
("E05","Physics-Informed Neural Networks for Solving Forward and Inverse Problems in Complex Beam","PINN","损失嵌入","复杂梁系统(机翼相邻)","仿真","结构相邻"),
("E06","physics-informed neural network with transfer learning","PINN+迁移","损失嵌入","域相似度迁移学习","仿真","§5.2迁移"),
("E07","Advancing deformation calculation: a physics-informed deep graph learning","PIGL","架构嵌入","超弹性变形计算","仿真","柔顺装配相邻"),
("E08","physics-informed and data-driven framework for robotic welding","PIML","混合","机器人焊接","实测+仿真","制造使能"),
("E09","Physics-Informed Neural Networks With Weighted Losses by Uncertainty Evaluation","PINN+UQ","加权损失","不确定性加权训练","仿真","§5.3UQ"),
("E10","Multi-layer thermal simulation using physics-informed neural network","PINN","损失嵌入","多层热仿真","仿真","AM使能"),
("E11","physics-guided reinforcement learning framework for an autonomous manufacturing","物理引导RL","约束嵌入","自主制造系统","仿真","多智能体相邻"),
("E12","physics-informed Bayesian optimization method for rapid development of electrical","物理信息BO","约束嵌入","电机快速设计","仿真","BO使能"),
# ===== G7 方法与综述背景（§2.2） =====
("C01","Physics-informed neural networks: A deep learning framework","PINN","损失嵌入(PDE残差)","正/逆问题通用求解","单保真","种子/奠基"),
("C02","Scientific Machine Learning Through Physics–Informed Neural Networks","综述","—","PINN方法与趋势","—","高被引综述"),
("C03","Physics-Informed Machine Learning: A survey on Problems, Methods and Applications","综述","—","PIML通用综述","—","种子/划界对象"),
("C04","PINN Evolution and Beyond: A Systematic Literature Review","综述","—","PINN演进","—","综述"),
("C05","Physics-Informed Graph Learning","PIGL","架构嵌入(图)","图学习通用","单保真","种子"),
("C06","Advancements in Physics-Informed Neural Networks for Laminated Composites","综述","—","层合复合材料PINN","—","材料相邻综述"),
("C07","Physics-Informed Neural Networks in Polymers: A Review","综述","—","聚合物PINN","—","材料相邻综述"),
("C08","NeuralPDE: Automating Physics-Informed Neural Networks","工具","—","PINN自动化工具","—","工具链"),
# ===== G8 知识表示×容差（§5.4） =====
("K01","Knowledge graph–enabled tolerancing experience acquisition","知识图谱","—","容差规范经验获取与重用","经验知识","种子"),
("K02","一种融合物理信息屈曲代理的曲线纤维机翼智能优化算法","物理信息代理","损失嵌入(屈曲)","曲线纤维机翼优化","仿真","种子/专利"),
]

lines = ["# 文献编码表 v2（Table 1 雏形）\n",
 "> 更新日期：2026-09-13。来源：文献池 N=1779（Q1–Q14 检索式），经自动分层 + 人工摘要筛查后分组编码。",
 "> ⚠️ 维度编码基于标题/摘要推断，**全文核对前不作最终引用依据**；`—` 表示该维度不适用或待核对。\n"]

groups = [("G1 PIML × 装配/容差 核心","A"),("G2 数字孪生与在线几何保证","D"),
          ("G3 数据驱动/ML 偏差预测（非物理信息）","M"),("G4 传统容差分析与变动建模","T"),
          ("G5 容差分配与优化","O"),("G6 PIML 使能技术","E"),
          ("G7 方法与综述背景","C"),("G8 知识表示 × 容差","K")]

hdr = "| 编号 | 文献 | 年份 | 出处 | 被引 | 方法类别 | 物理融入机制 | 应用场景 | 保真度 | DOI |"
sep = "|---|---|---|---|---|---|---|---|---|---|---|"
total, missing = 0, []
for gname, prefix in groups:
    lines.append(f"\n## {gname}\n")
    lines += [hdr, sep]
    for e in CURATED:
        if not e[0].startswith(prefix): continue
        cid, frag, mcat, mech, app, fid, note = e
        r = find(frag)
        if r:
            title = r["title"].replace("|","/").replace("\n"," ")[:80]
            year = r["year"] or "?"
            venue = (r["venue"] or "?").replace("|","/")[:45]
            cit = r["citations"] or "0"
            doi = r["doi"] or "—"
        elif cid in FALLBACK:
            title, year, venue, cit, doi = FALLBACK[cid]
            missing.append((cid, "fallback-manual"))
        else:
            missing.append((cid, frag))
            title, year, venue, cit, doi = frag[:80], "?", "?", "?", "—"
        lines.append(f"| {cid} | {title} | {year} | {venue} | {cit} | {mcat} | {mech} | {app} | {fid} | {doi} |")
        total += 1

lines.append(f"\n## 统计\n\n- 编码条目: {total}（8 组）")
lines.append(f"- 未在池中匹配到（须手动补元数据）: {len(missing)} 条")
for cid, frag in missing:
    lines.append(f"  - {cid}: {frag}")
lines.append("\n## 待办\n")
lines.append("- [ ] 逐条全文核对维度编码")
lines.append("- [ ] Kopatsch et al. (2026) PINN 公差分析仍未检获——Q13 未命中，须通过 Crossref 或出版商页面定向查找")
lines.append("- [ ] 'CGAN-based surrogate for aircraft assembly gaps (2026)' 未直接检获；Q14 命中的流形学习 GAN 装配应力场 (2026) 疑为相关工作，待核对")
Path(LIT / "coding-table.md").write_text("\n".join(lines), encoding="utf-8")
print(f"total={total} missing={len(missing)}")
for m in missing: print("MISS:", m)
