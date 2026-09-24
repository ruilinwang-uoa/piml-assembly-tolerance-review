# 文献编码表 v2（Table 1 雏形）

> 更新日期：2026-09-13。来源：文献池 N=1779（Q1–Q14 检索式），经自动分层 + 人工摘要筛查后分组编码。
> ⚠️ 维度编码基于标题/摘要推断，**全文核对前不作最终引用依据**；`—` 表示该维度不适用或待核对。


## G1 PIML × 装配/容差 核心

| 编号 | 文献 | 年份 | 出处 | 被引 | 方法类别 | 物理融入机制 | 应用场景 | 保真度 | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| A01 | A Dynamic Prediction Method for Assembly Quality Based on Physics-Informed Machi | 2026 | Journal of Computing and Information Science  | 0 | PIML+机理 | 损失嵌入(偏差机理) | 飞机长桁装配偏差动态预测 | 实测+机理 | 10.1115/1.4072491 |
| A02 | Facilitating digital assembly: A physics-informed graph learning framework for p | 2026 | Journal of Manufacturing Systems | 0 | PIGL | 混合(图+物理损失) | 螺栓法兰连接装配偏差预测 | 仿真+实测 | 10.1016/j.jmsy.2026.06.014 |
| A03 | Physics-Constrained Bayesian Optimization for Optimal Actuators Placement in Com | 2022 | IEEE Transactions on Automation Science and E | 18 | 物理约束BO | 约束嵌入 | 复合材料结构装配作动器布局 | 仿真 | 10.1109/tase.2022.3200376 |
| A04 | A hybrid rigid-compliant computational framework for large-scale assembly: Integ | 2026 | Engineering Structures | 0 | 传统+ML混合 | 架构嵌入(torsor) | 大尺寸装配变动传播 | 仿真 | 10.1016/j.engstruct.2026.122965 |
| A05 | SmartFixture: Physics-guided reinforcement learning for automatic fixture layout | 2024 | IISE Transactions | 3 | 物理引导RL | 约束嵌入 | 薄壁件夹具布局(装配变形) | FEA仿真 | 10.1080/24725854.2024.2401041 |
| A06 | Fast and accurate active alignment of camera lenses with physics-informed deep l | 2025 | Optics Express | 6 | 物理信息DL | 损失嵌入 | 光学镜头主动对准(精密装配) | 实测 | 10.1364/oe.560123 |
| A07 | Physics-Informed Multi-Fidelity Graph Learning for Sequence-Aware Residual Bolt  | 2026 | Sensors | 0 | PIGL | 混合 | 多保真图代理(场景待通读) | 多保真 | 10.3390/s26175534 |
| A08 | A manifold learning-assisted generative adversarial network for rapid assembly s | 2026 | Thin-Walled Structures | 0 | 流形学习+GAN | 数据嵌入(物理流形) | 装配应力场快速预测 | 仿真 | 10.1016/j.tws.2026.114962 |
| A09 | Assembly‐Deviation‐Induced Sealing Leakage in PEMFC Stacks: Failure Mechanisms,  | 2026 | Fuel Cells | 0 | 混合建模 | 机理+数据 | 装配偏差→密封泄漏(燃料电池) | 单保真 | 10.1002/fuce.70156 |
| A10 | Leveraging Physics-Informed Neural Networks for Efficient Tolerance Analysis | 2026 | Procedia CIRP | 0 | PINN | 损失嵌入 | 容差分析直接应用(CAT2026) | 仿真 | 10.1016/j.procir.2026.03.130 |
| A11 | Adaptive Planning Method for ERS Point Layout in Aircraft Assembly Driven by Physics-Based Data-Driven Surrogate Model | 2026 | Sensors | 0 | 物理代理 | 混合 | 飞机装配 ERS 点布局规划 | 仿真 | 10.3390/s26030955 |

| A12 | Machine learning based surrogate modeling of the deformation behavior of large compliant thin-w | 2026 | Procedia CIRP | 0 | PIML | 损失嵌入 | 装配偏差/变形预测(筛查并入) | 仿真 | 10.1016/j.procir.2026.03.117 |
| A13 | ThermoDynaSMT: A Physics-Informed Machine Learning Model for Component Displacement in Surface  | 2025 | Journal of Electronic Packaging | 1 | PIML | 损失嵌入 | 制造几何相关(筛查并入) | 仿真 | 10.1115/1.4070105 |
| A14 | PhyViT-GAN: Physics-Guided MobileViT-GAN for precise self-alignment image generation | 2026 | The International Journal of Advanced Ma | 1 | 物理信息混合 | 无(纯数据) | 制造几何相关(筛查并入) | 仿真 | 10.1007/s00170-025-17227-7 |
## G2 数字孪生与在线几何保证

| 编号 | 文献 | 年份 | 出处 | 被引 | 方法类别 | 物理融入机制 | 应用场景 | 保真度 | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| D01 | Digital twin-based high-precision assembly method for large-diameter cabin section docking | 2026 | J. Manuf. Syst. | 0 | 数字孪生 | 数据嵌入 | 大直径舱段对接装配 | 多保真(DT) | 10.1016/j.jmsy.2026.02.019 |
| D02 | Digital Twin-driven Inversion of Assembly Precision for Industrial Equipment: Ch | 2025 | Chinese Journal of Mechanical Engineering | 6 | 数字孪生+ML | 数据嵌入 | 工业装备装配精度反演 | 多保真(DT) | 10.1186/s10033-025-01224-8 |
| D03 | Online geometry assurance in individualized production by feedback control and m | 2022 | Journal of Manufacturing Systems | 19 | 数字孪生 | 模型校准 | 钣金件装配在线几何保证 | 实测+仿真 | 10.1016/j.jmsy.2022.11.011 |
| D04 | Digital Twin-Based Clamping Sequence Analysis and Optimization for Improved Geom | 2024 | Applied Sciences | 12 | 数字孪生 | 数据嵌入 | 钣金装配夹紧序列优化 | 仿真 | 10.3390/app14020510 |
| D05 | Quality Prediction and Control of Assembly and Welding Process for Ship Group Pr | 2020 | Scanning | 42 | 数字孪生 | 数据嵌入 | 船舶装配焊接质量预测 | 实测 | 10.1155/2020/3758730 |

| D06 | Digital twin–driven multiscale modelling for real-time defect prediction in metal additive manu | 2026 | Scientific Reports | 2 | PIML | 损失嵌入 | 制造几何相关(筛查并入) | 仿真 | 10.1038/s41598-026-58348-7 |
| D07 | Structural Health Monitoring of a Satellite Antenna: A Benchmark Between the Modal Method, iFEM | 2025 |  | 1 | PIML | 损失嵌入 | 制造几何相关(筛查并入) | 仿真+实测 | 10.12783/shm2025/37480 |
| D08 | Real-time distortion prediction in metallic additive manufacturing via a physics-informed neura | 2025 | arXiv (Cornell University) | 0 | PIML | 损失嵌入 | 制造几何相关(筛查并入) | 仿真 | 10.48550/arxiv.2511.13178 |
| D09 | Deep Neural Operator Enabled Digital Twin Modeling for Additive Manufacturing | 2024 | arXiv (Cornell University) | 3 | PIML | 损失嵌入 | 制造几何相关(筛查并入) | 仿真+实测 | 10.48550/arxiv.2405.09572 |
| D10 | Intelligent Feedrate Optimization Using an Uncertainty-Aware Digital Twin Within a Model Predic | 2024 | IEEE Access | 11 | PIML | 损失嵌入 | 容差分析(筛查并入) | 实测 | 10.1109/access.2024.3384471 |
## G3 数据驱动/ML 偏差预测（非物理信息）

| 编号 | 文献 | 年份 | 出处 | 被引 | 方法类别 | 物理融入机制 | 应用场景 | 保真度 | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| M01 | DeviationGAN: A generative end-to-end approach for the deviation prediction of s | 2023 | Mechanical Systems and Signal Processing | 24 | GAN | 无(纯数据) | 钣金装配偏差端到端预测 | 仿真+实测 | 10.1016/j.ymssp.2023.110822 |
| M02 | Neural Network Gaussian Process Considering Input Uncertainty for Composite Stru | 2020 | IEEE/ASME Transactions on Mechatronics | 27 | NN-GP | 输入不确定性建模 | 复合材料结构装配偏差与残余应力 | 仿真 | 10.1109/tmech.2020.3040755 |
| M03 | Gaussian Processes with Input Location Error and Applications to the Composite P | 2022 | SIAM/ASA Journal on Uncertainty Quantificatio | 15 | GP | 输入误差建模 | 复合材料装配过程 | 仿真 | 10.1137/20m1312447 |
| M04 | Surrogate model–based optimal feed-forward control for dimensional-variation red | 2018 | Journal of Quality Technology | 35 | 代理模型 | 无 | 复合材料件尺寸变动前馈控制 | 仿真 | 10.1080/00224065.2018.1474688 |
| M05 | Anomaly detection in Skin Model Shapes using machine learning classifiers | 2019 | The International Journal of Advanced Manufac | 30 | ML分类 | 无 | Skin Model Shapes 异常检测 | 仿真 | 10.1007/s00170-019-03794-z |
| M06 | A multilayer shallow learning approach to variation prediction and variation sou | 2020 | Journal of Intelligent Manufacturing | 11 | 浅层学习 | 无 | 多工序加工变动预测与溯源 | 实测 | 10.1007/s10845-020-01649-z |
| M07 | Inspection by exception: A new machine learning-based approach for multistage ma | 2020 | Applied Soft Computing | 31 | ML | 无 | 多工序制造质量预测 | 实测 | 10.1016/j.asoc.2020.106787 |
| M08 | A Bayesian framework to estimate part quality and associated uncertainties in mu | 2019 | Computers in Industry | 46 | 贝叶斯 | 不确定性建模 | 多工序制造件质量估计 | 实测 | 10.1016/j.compind.2018.10.008 |
| M09 | A FDQN-based tolerance closed-loop optimization model for thin-wall components i | 2025 | Advanced Engineering Informatics | 6 | 深度RL | 无 | 飞机薄壁件容差闭环优化 | 仿真 | 10.1016/j.aei.2025.103453 |
| M10 | Predicting geometric parameters of assemblies with neural network models | 2018 | Journal of Physics Conference Series | 8 | NN | 无 | 装配几何参数预测 | 仿真 | 10.1088/1742-6596/1096/1/012198 |
| M11 | A new surrogate model–based method for individualized spot welding sequence opti | 2019 | The International Journal of Advanced Manufac | 22 | 代理模型 | 无 | 点焊序列优化(几何偏差) | 仿真 | 10.1007/s00170-019-04706-x |
| M12 | Critical joint identification for efficient sequencing | 2020 | Journal of Intelligent Manufacturing | 11 | ML | 无 | 焊点序列优化 | 仿真 | 10.1007/s10845-020-01660-4 |
| M13 | Reduced-order modelling for real-time physics-based variation simulation enhance | 2024 | The International Journal of Advanced Manufac | 17 | 降阶模型 | 物理模型降阶 | 柔顺装配变动实时仿真 | 仿真 | 10.1007/s00170-024-13493-z |
| M14 | Multi-task learning with state propagation for quality forecasts in polymer extr | 2025 | Journal of Intelligent Manufacturing | 6 | 多任务ML | 状态传播约束 | 聚合物挤出质量预测 | 实测 | 10.1007/s10845-025-02616-2 |
| M15 | Predicting aircraft assembly gaps considering structural deformation: A CGAN-bas | 2025 | Journal of Manufacturing Systems | 3 | CGAN代理 | 无(纯数据) | 飞机装配间隙预测(结构变形) | 仿真 | 10.1016/j.jmsy.2025.12.018 |

## G4 传统容差分析与变动建模

| 编号 | 文献 | 年份 | 出处 | 被引 | 方法类别 | 物理融入机制 | 应用场景 | 保真度 | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| T01 | Skin Model Shapes: Offering New Potentials for Modelling Product Shape Variabili | 2015 | ? | 17 | Skin Model Shapes | — | 形状变动建模范式 | — | 10.1115/detc2015-46701 |
| T02 | Status and Prospects of Skin Model Shapes for Geometric Variations Management | 2016 | Procedia CIRP | 44 | Skin Model Shapes | — | 几何变动管理综述 | — | 10.1016/j.procir.2016.02.005 |
| T03 | Integrating form errors and local surface deformations into tolerance analysis b | 2018 | Computer-Aided Design | 88 | SMS+FEA | — | 形状误差+局部变形容差分析 | 仿真 | 10.1016/j.cad.2018.05.005 |
| T04 | Manufacturing signature in jacobian and torsor models for tolerance analysis of  | 2016 | Robotics and Computer-Integrated Manufacturin | 48 | Jacobian-Torsor | — | 刚性件容差分析(制造签名) | 仿真 | 10.1016/j.rcim.2016.11.004 |
| T05 | Manufacturing signature in variational and vector-loop models for tolerance anal | 2016 | The International Journal of Advanced Manufac | 34 | Variational/Vector-loop | — | 刚性件容差分析 | 仿真 | 10.1007/s00170-016-8947-z |
| T06 | Assembly tolerance analysis based on the Jacobian model and skin model shapes | 2019 | Assembly Automation | 27 | Jacobian+SMS | — | 装配容差分析 | 仿真 | 10.1108/aa-10-2017-128 |
| T07 | Polytope-based tolerance analysis with consideration of form defects and surface | 2020 | International Journal of Computer Integrated  | 13 | Polytope | — | CAT多胞体模型 | 仿真 | 10.1080/0951192x.2020.1858501 |
| T08 | A generic integrated approach of assembly tolerance analysis based on skin model | 2020 | Proceedings of the Institution of Mechanical  | 31 | SMS | — | 装配容差分析通用框架 | 仿真 | 10.1177/0954405420958862 |
| T09 | Statistical Tolerance Analysis Based on Good Point Set and Homogeneous Transform | 2016 | Procedia CIRP | 22 | 统计法 | — | 统计容差分析 | 仿真 | 10.1016/j.procir.2016.02.042 |
| T10 | Integration of Thermal Effects into Tolerancing Using Skin Model Shapes | 2016 | Procedia CIRP | 23 | SMS+热 | — | 热变形融入容差 | 仿真 | 10.1016/j.procir.2016.02.079 |
| T11 | 3D Tolerance Analysis with Manufacturing Signature and Operating Conditions | 2016 | Procedia CIRP | 20 | 制造签名 | — | 工况融入3D容差分析 | 仿真 | 10.1016/j.procir.2016.02.097 |
| T12 | Assembly accuracy analysis of cylindrical parts based on skin model shapes consi | 2023 | Precision Engineering | 26 | SMS | — | 回转件装配精度 | 仿真 | 10.1016/j.precisioneng.2023.01.004 |
| T13 | An assembly accuracy analysis approach of mechanical assembly involving parallel | 2024 | Precision Engineering | 11 | NSMS | — | 并/串联装配偏差传播 | 仿真 | 10.1016/j.precisioneng.2024.01.016 |
| T14 | Assembly accuracy analysis and phase optimization of aero-engine multistage roto | 2024 | Precision Engineering | 25 | 变动建模 | — | 航空发动机多级转子装配相位优化 | 实测 | 10.1016/j.precisioneng.2024.04.003 |
| T15 | Virtual Geometry Assurance Process and Toolbox | 2016 | Procedia CIRP | 73 | 几何保证 | — | 虚拟几何保证流程 | 实测+仿真 | 10.1016/j.procir.2016.02.043 |
| T16 | Challenges of Geometrical Variations Modelling in Virtual Product Realization | 2017 | Procedia CIRP | 12 | 综述 | — | 变动建模挑战 | — | 10.1016/j.procir.2017.01.019 |
| T17 | A Review on Variation Modeling of Aircraft Assembly | 2023 | International Journal of Robotics and Automat | 7 | 综述 | — | 飞机装配变动建模综述 | — | 10.31875/2409-9694.2023.10.05 |
| T18 | Systems Thinking in Tolerance and Quality-related Design Decision-making | 2015 | Procedia CIRP | 13 | 系统思维 | — | 容差-质量设计决策 | — | 10.1016/j.procir.2015.04.044 |
| T19 | A comprehensive study of tolerance analysis methods for rigid parts with manufac | 2017 | Journal of Advanced Mechanical Design Systems | 12 | 综述 | — | 刚性件容差分析方法比较 | 仿真 | 10.1299/jamdsm.2017jamdsm0017 |
| T20 | Investigating the potential of ontologies to enable knowledge-based tolerancing  | 2026 | Procedia CIRP | 0 | 本体 | — | CNC铣削件知识化容差 | 知识 | 10.1016/j.procir.2026.03.129 |
| T21 | Towards Seamless Integration: Embedding Advanced Geometric Tolerance Models in S | 2026 | Procedia CIRP | 0 | 系统级仿真 | — | 系统级仿真中的几何容差模型 | 仿真 | 10.1016/j.procir.2026.03.140 |
| T22 | Variation Simulation During Assembly of Non-rigid Components. Realistic Assembly | 2016 | Procedia CIRP | 39 | 柔顺装配仿真 | — | 非刚性件装配仿真(ANATOLEFLEX) | 仿真 | 10.1016/j.procir.2016.02.336 |
| T23 | Efficient Spot Welding Sequence Simulation in Compliant Variation Simulation | 2021 | Journal of Manufacturing Science and Engineer | 16 | 柔顺装配仿真 | — | 点焊序列变动仿真 | 仿真 | 10.1115/1.4049654 |
| T24 | Optimal design of fixture layouts for compliant sheet metal assemblies | 2020 | The International Journal of Advanced Manufac | 32 | 夹具优化 | — | 柔顺钣金装配夹具布局 | 仿真 | 10.1007/s00170-020-05954-y |
| T25 | Development of Fixture Layout Optimization for Thin-Walled Parts: A Review | 2024 | Chinese Journal of Mechanical Engineering | 21 | 综述 | — | 薄壁件夹具布局优化综述 | — | 10.1186/s10033-024-01004-w |
| T26 | Numerical Process Based on Measuring Data for Gap Prediction of an Assembly | 2015 | Procedia CIRP | 17 | 实测驱动 | — | 航空装配间隙预测 | 实测 | 10.1016/j.procir.2015.04.050 |
| T27 | Bridging the gap between design and manufacturing specifications for non-rigid p | 2023 | The International Journal of Advanced Manufac | 13 | 影响系数法 | — | 非刚性件设计-制造规范衔接 | 仿真 | 10.1007/s00170-023-11480-4 |
| T28 | Decomposing deviations of scanned surfaces of sheet metal assemblies | 2021 | Journal of Manufacturing Systems | 7 | FEA+实测 | — | 钣金装配扫描表面偏差分解 | 实测 | 10.1016/j.jmsy.2021.08.011 |
| T29 | Variation Analysis Considering the Partial Parallel Connection in Aero-Engine Ro | 2022 | Energies | 14 | 变动分析 | — | 航空发动机转子装配变动 | 仿真 | 10.3390/en15124451 |
| T30 | A coordination modelling approach for assembly of multi-constrained objects based on measured skin model | 2019 | Assembly Autom. | 11 | 实测驱动 | — | 飞机多约束对象装配协调 | 实测 | 10.1108/aa-04-2018-058 |
| T31 | Octree-Based Generation and Variation Analysis of Skin Model Shapes | 2018 | Journal of Manufacturing and Materials Proces | 8 | SMS生成 | — | Skin Model Shapes 八叉树生成与变动分析 | 仿真 | 10.3390/jmmp2030052 |
| T32 | Stream of Variation Modeling and Analysis for Multistage Manufacturing Processes | 2006 | CRC Press | 152 | SOVA状态空间 | — | 多工位制造变动传播(专著) | 仿真 | 10.1201/9781420003901 |
| T33 | State Space Modeling of Sheet Metal Assembly for Dimensional Control | 1999 | J. Manuf. Sci. Eng. | 342 | SOVA状态空间 | — | 钣金装配尺寸控制状态空间建模 | 仿真 | 10.1115/1.2833137 |

| M16 | Development of a surrogate model for uncertainty quantification of compressor performance due t | 2023 | Journal of the Global Power and Propulsi | 5 | 学习代理 | 数据嵌入 | 容差分析(筛查并入) | 仿真 | 10.33737/jgpps/168293 |
| M17 | Forecasting Rectangular Pocket Deviations in Birch Plywood for Milling Process Optimization | 2026 | Informatica | 0 | 学习代理 | 无(纯数据) | 容差分析(筛查并入) | 仿真 | 10.31449/inf.v50i2.10897 |
| M18 | Surrogate Models for the Efficient Estimation of Residual Fields Associated With Additively Man | 2019 |  | 0 | PIML | 损失嵌入 | 制造几何相关(筛查并入) | 仿真 | 10.1115/detc2019-98332 |
| M19 | Data-driven inverse parameter design for stable dimensional control in extrusion-based additive | 2026 | Computers in Industry | 0 | ML | 约束嵌入 | 容差分析(筛查并入) | 实测 | 10.1016/j.compind.2026.104520 |
| M20 | Röntgen-CT-ondersteunde datagedreven in-procesmonitoring voor metaal- Laser Powder Bed Fusion | 2026 | Lirias | 0 | PIML | 损失嵌入 | 制造几何相关(筛查并入) | 仿真 | — |
## G5 容差分配与优化

| 编号 | 文献 | 年份 | 出处 | 被引 | 方法类别 | 物理融入机制 | 应用场景 | 保真度 | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| O01 | Optimal Tolerance Allocation in a Complex Assembly Using Evolutionary Algorithms | 2016 | International Journal of Simulation Modelling | 14 | 进化算法 | — | 复杂装配容差分配 | 仿真 | 10.2507/ijsimm15(1)10.331 |
| O02 | Ontological model-based optimal determination of geometric tolerances in an asse | 2019 | Journal of Engineering Design | 17 | 本体+优化 | — | 非刚性装配几何容差确定 | 知识+仿真 | 10.1080/09544828.2019.1605585 |
| O03 | Generating Manufacturing Distributions for Sampling-based Tolerance Analysis usi | 2024 | Procedia CIRP | 4 | 采样优化 | — | 容差-成本优化 | 仿真 | 10.1016/j.procir.2024.10.019 |
| O04 | Dimensional tolerance optimization of SAR antennas with uncertainty quantificati | 2024 | Aerospace Science and Technology | 13 | UQ+可靠性 | — | SAR天线尺寸容差优化 | 仿真 | 10.1016/j.ast.2024.109412 |
| O05 | Tolerance Optimization of Patch Parameters for Locally Reinforced Composite Stru | 2022 | Applied Composite Materials | 10 | 优化 | — | 复合材料局部加强容差 | 仿真 | 10.1007/s10443-022-10072-x |
| O06 | Toward cost-efficient tolerancing of 3D-printed parts: a novel methodology for t | 2021 | The International Journal of Advanced Manufac | 13 | 成本建模 | — | 增材制造容差-成本 | 实测 | 10.1007/s00170-021-08488-z |
| O07 | Tolerance management during the design of composite structures considering varia | 2021 | The International Journal of Advanced Manufac | 20 | 变动管理 | — | 复材结构设计容差管理 | 仿真 | 10.1007/s00170-020-06555-5 |
| O08 | Optimal tolerance allocation based on Difficulty matrix using FMECA tool | 2018 | Procedia CIRP | 11 | FMECA | — | 容差分配难度矩阵 | — | 10.1016/j.procir.2018.03.005 |
| O09 | Visual quality and sustainability considerations in tolerance optimization: A ma | 2015 | International Journal of Production Economics | 25 | 优化 | — | 视觉质量-可持续容差优化 | — | 10.1016/j.ijpe.2015.06.023 |
| O10 | Coaxiality error analysis and optimization of cylindrical parts of CNC turning p | 2022 | The International Journal of Advanced Manufac | 17 | 误差优化 | — | CNC车削同轴度 | 实测 | 10.1007/s00170-022-09184-2 |

| O11 | Retained imaging quality with reduced manufacturing precision: leveraging computational optics | 2025 | Advanced Photonics Nexus | 2 | PIML | 损失嵌入 | 容差分析(筛查并入) | 仿真 | 10.1117/1.APN.4.4.046014 |
| O12 | Tolerance-Aware Deep Optics | 2025 | arXiv (Cornell University) | 2 | PIML | 损失嵌入 | 容差分析(筛查并入) | 仿真 | 10.48550/arxiv.2502.04719 |
| O13 | Physics-Informed Tolerance Allocation: A Surrogate-Based Framework for the Control of Geometric | 2019 |  | 2 | PIML | 损失嵌入 | 容差分配 | 仿真+实测 | 10.48550/arxiv.1904.06559 |
## G6 PIML 使能技术

| 编号 | 文献 | 年份 | 出处 | 被引 | 方法类别 | 物理融入机制 | 应用场景 | 保真度 | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| E01 | Physics-informed neural networks for data-free surrogate modelling and engineeri | 2023 | Materials & Design | 45 | PINN | 损失嵌入 | 工程优化代理(无数据) | 无数据 | 10.1016/j.matdes.2023.112034 |
| E02 | Accelerating Thermal Simulations in Additive Manufacturing by Training Physics-I | 2023 | Journal of Computing and Information Science  | 31 | PINN | 损失嵌入 | 增材热仿真加速 | 仿真 | 10.1115/1.4062852 |
| E03 | Physics-Informed Online Learning for Temperature Prediction in Metal AM | 2024 | Materials | 23 | PINN+在线学习 | 损失嵌入 | 金属AM温度场在线预测 | 在线数据 | 10.3390/ma17133306 |
| E04 | Solving forward and inverse problems of contact mechanics using physics-informed | 2024 | Advanced Modeling and Simulation in Engineeri | 77 | PINN | 损失嵌入 | 接触力学正逆问题 | 仿真 | 10.1186/s40323-024-00265-3 |
| E05 | Physics-Informed Neural Networks for Solving Forward and Inverse Problems in Com | 2023 | IEEE Transactions on Neural Networks and Lear | 135 | PINN | 损失嵌入 | 复杂梁系统(机翼相邻) | 仿真 | 10.1109/tnnls.2023.3310585 |
| E06 | Physics-informed neural network with transfer learning (TL-PINN) based on domain | 2023 | Scientific Reports | 88 | PINN+迁移 | 损失嵌入 | 域相似度迁移学习 | 仿真 | 10.1038/s41598-023-43325-1 |
| E07 | Advancing deformation calculation: a physics-informed deep graph learning framew | 2025 | Advanced Modeling and Simulation in Engineeri | 3 | PIGL | 架构嵌入 | 超弹性变形计算 | 仿真 | 10.1186/s40323-025-00304-7 |
| E08 | A physics-informed and data-driven framework for robotic welding in manufacturin | 2025 | Nature Communications | 43 | PIML | 混合 | 机器人焊接 | 实测+仿真 | 10.1038/s41467-025-60164-y |
| E09 | Physics-Informed Neural Networks With Weighted Losses by Uncertainty Evaluation  | 2023 | IEEE Transactions on Neural Networks and Lear | 99 | PINN+UQ | 加权损失 | 不确定性加权训练 | 仿真 | 10.1109/tnnls.2023.3247163 |
| E10 | Multi-layer thermal simulation using physics-informed neural network | 2024 | Additive manufacturing | 16 | PINN | 损失嵌入 | 多层热仿真 | 仿真 | 10.1016/j.addma.2024.104498 |
| E11 | A physics-guided reinforcement learning framework for an autonomous manufacturin | 2021 | ? | 4 | 物理引导RL | 约束嵌入 | 自主制造系统 | 仿真 | 10.23919/acc50511.2021.9482944 |
| E12 | A physics-informed Bayesian optimization method for rapid development of electri | 2024 | Scientific Reports | 17 | 物理信息BO | 约束嵌入 | 电机快速设计 | 仿真 | 10.1038/s41598-024-54965-2 |
| E13 | Fourier Neural Operator for Parametric Partial Differential Equations | 2021 | ICLR (arXiv:2010.08895) |  1105  | 算子学习 | 架构嵌入(算子) | PDE参数化代理(待迁移容差) | 仿真 | — |
| E14 | Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators | 2021 | Nature Machine Intelligence | 3204 | 算子学习 | 架构嵌入(算子) | PDE非线性算子学习(待迁移容差) | 仿真 | 10.1038/s42256-021-00302-5 |

## G7 方法与综述背景

| 编号 | 文献 | 年份 | 出处 | 被引 | 方法类别 | 物理融入机制 | 应用场景 | 保真度 | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| C01 | Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear PDEs | 2019 | J. Comput. Phys. | 高被引 | PINN | 损失嵌入(PDE残差) | 正/逆问题通用求解 | 单保真 | 10.1016/j.jcp.2018.10.045 |
| C02 | Scientific Machine Learning Through Physics–Informed Neural Networks: Where we a | 2022 | Journal of Scientific Computing | 2658 | 综述 | — | PINN方法与趋势 | — | 10.1007/s10915-022-01939-z |
| C03 | Physics-Informed Machine Learning: A survey on Problems, Methods and Applications | 2022 | arXiv（种子PDF） | — | 综述 | — | PIML通用综述 | — | — |
| C04 | Physics-Informed Neural Network (PINN) Evolution and Beyond: A Systematic Literature Review and Meta-Analysis | 2022 | Big Data Cogn. Comput. | 255 | 综述 | — | PINN演进 | — | 10.3390/bdcc6040140 |
| C06 | Advancements in Physics-Informed Neural Networks for Laminated Composites: A Com | 2024 | Mathematics | 70 | 综述 | — | 层合复合材料PINN | — | 10.3390/math13010017 |
| C07 | Physics-Informed Neural Networks in Polymers: A Review | 2025 | Polymers | 44 | 综述 | — | 聚合物PINN | — | 10.3390/polym17081108 |
| C08 | NeuralPDE: Automating Physics-Informed Neural Networks (PINNs) with\n Error Appr | 2021 | arXiv (Cornell University) | 50 | 工具 | — | PINN自动化工具 | — | 10.48550/arxiv.2107.09443 |

## G8 知识表示 × 容差

| 编号 | 文献 | 年份 | 出处 | 被引 | 方法类别 | 物理融入机制 | 应用场景 | 保真度 | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| K01 | Knowledge graph–enabled tolerancing experience acquisition and reuse for tolerance specification | 2023 | Int. J. Adv. Manuf. Technol. | — | 知识图谱 | — | 容差规范经验获取与重用 | 经验知识 | 10.1007/s00170-023-12644-y |
| K02 | 一种融合物理信息屈曲代理的曲线纤维机翼智能优化算法（发明专利申请） | 2026 | CN122174367A | — | 物理信息代理 | 损失嵌入(屈曲) | 曲线纤维机翼优化 | 仿真 | — |

| E15 | Surface Roughness Prediction of CNC Lathe Machined Hardened Steel Using Physics-Informed Neural | 2025 |  | 0 | PIML | 损失嵌入 | 制造几何相关(筛查并入) | 仿真 | 10.1109/icset65917.2025.11284154 |
| E16 | Comparative study of artificial neural network and physics-informed neural network application  | 2024 | Materials research proceedings | 7 | PIML | 损失嵌入 | 几何质量预测(筛查并入) | 仿真 | 10.21741/9781644903131-251 |
| E17 | Bead geometry prediction in wire arc directed energy deposition using physics-informed machine  | 2025 | Additive manufacturing | 15 | PIML | 损失嵌入 | 几何质量预测(筛查并入) | 实测 | 10.1016/j.addma.2025.104881 |
| E18 | Close the Design-to-Manufacturing Gap in Computational Optics with a 'Real2Sim' Learned Two-Pho | 2023 |  | 12 | PIML | 损失嵌入 | 制造几何相关(筛查并入) | 仿真 | 10.1145/3610548.3618251 |
| E19 | Physics-Informed Machine Learning for Predicting Thermal Distortion in Metal Additive Manufactu | 2025 | American Journal of Scholarly Research a | 0 | PIML | 损失嵌入 | 制造几何相关(筛查并入) | 仿真 | 10.63125/ny974y17 |
| E20 | Real-time and data-efficient springback prediction in tube bending using force measurement and  | 2025 | Journal of Manufacturing Processes | 12 | PIML | 损失嵌入 | 制造几何相关(筛查并入) | 仿真+实测 | 10.1016/j.jmapro.2025.10.104 |
| E21 | Towards Sustainable Laser-Based Manufacturing: A Physics-Informed Machine Learning Approach to  | 2026 | Procedia CIRP | 1 | PIML | 损失嵌入 | 几何质量预测(筛查并入) | 仿真+实测 | 10.1016/j.procir.2026.05.173 |
| E22 | Physics-Informed Neural Networks for Accurate Photoresist Thickness Prediction | 2026 |  | 0 | PIML | 损失嵌入 | 制造几何相关(筛查并入) | 实测 | 10.1109/cstic68613.2026.11537714 |
| E23 | Multi-Modal Physics-Informed Neural Network for Single-Track Geometry Prediction in Powder-Bed  | 2026 | Materials | 0 | PIML | 损失嵌入 | 几何质量预测(筛查并入) | 仿真+实测 | 10.3390/ma19163454 |
| E24 | Advancing Thermal Physics-Informed PointNet Distortion Prediction Capabilities in Wire Arc-Dire | 2025 | Journal of Computing and Information Sci | 3 | PIML | 损失嵌入 | 几何质量预测(筛查并入) | 实测 | 10.1115/1.4069381 |
| E25 | Physics-guided neural network framework for surface roughness prediction in additively manufact | 2026 | Journal of Laser Applications | 2 | 物理信息混合 | 损失嵌入 | 制造几何相关(筛查并入) | 仿真+实测 | 10.2351/7.0002049 |
| E26 | Physics-informed polynomial chaos expansions for geometric uncertainties | 2025 |  | 0 | PIML | 损失嵌入 | 几何质量预测(筛查并入) | 仿真+实测 | 10.23967/icossar.2025.030 |
| E27 | Artificial Intelligence Enabled Precise 3D Printing of Polyvinylidene Fluoride (PVDF) Microfibe | 2026 | ACS Applied Materials & Interfaces | 0 | PIML | 损失嵌入 | 制造几何相关(筛查并入) | 仿真 | 10.1021/acsami.6c01560 |
| E28 | Spatially-Aware Milling Surface Flatness Prediction Through Physics-Based Graph Neural Network | 2024 |  | 0 | 物理信息混合 | 损失嵌入 | 容差分析(筛查并入) | 仿真 | 10.1115/detc2024-143787 |
| E29 | Physics-guided explainable machine learning for multi-response modeling of electrochemical micr | 2026 | Scientific Reports | 0 | 物理信息混合 | 损失嵌入 | 制造几何相关(筛查并入) | 仿真+实测 | 10.1038/s41598-026-46315-1 |
| E30 | Machine Learning for Scalable and Generalizable Quality Control in Two-Photon Lithography | 2026 |  | 0 | PIML | 损失嵌入 | 几何质量预测(筛查并入) | 实测 | 10.7302/dspace/29727 |
| E31 | A closed-loop automated control architecture with physics-informed compensation for springback  | 2026 |  | 0 | PIML | 损失嵌入 | 几何质量预测(筛查并入) | 仿真 | 10.1117/12.3122441 |
| E32 | Data-driven identification of robot DH parameter errors using a physics-informed transformer ne | 2026 | International Computing Imaging Conferen | 1 | PIML | 损失嵌入 | 容差分析(筛查并入) | 仿真 | 10.1117/12.3091946 |
## 统计

- 编码条目: 131（8 组）
- 桥接文献新增（2026-09-16，评审 MAJOR #15）：T32/T33（SOVA 多工位变动传播，§3 桥接）、E13/E14（FNO/DeepONet 算子学习，§5 定位）；T32/T33/E14 Crossref 核验、E13 OpenAlex 被引（arXiv/ICLR 无 Crossref 记录）
- 未在新池中匹配：重检后按 DOI 复核（2026-09-19）

## 待办

- [ ] 逐条全文核对维度编码
- 筛查合并（2026-09-19）：第三轮重检增量筛查并入 34 条（剔除与既有条目重复 1 条：Kopatsch=A10）（include 30/baseline 5；LLM 辅助初筛+单人裁决，编码为关键词规则的摘要级保守编码；详见 screening/decisions.json）