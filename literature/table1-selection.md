# Table 1 精选对比矩阵（§6.1 用，52 条）

> 生成：2026-09-13，由 build 脚本从 coding-table.md v2 精选（G1/G2 全收 + 各组按被引 top）；2026-09-14 随 B-3/B-4 新增文献更新至 52 条（A10/A11 依"G1 全收"规则纳入；M15 被引 3，未达 G3 选录线，不纳入）。
> 验证类型由保真度字段推导（摘要级编码，全文核对前不作最终依据）。

| 编号 | 文献 | 年份 | 出处 | 方法 | 融入机制 | 应用场景 | 保真度 | 验证类型 | 被引 |
|---|---|---|---|---|---|---|---|---|---|
| A01 | A Dynamic Prediction Method for Assembly Quality Based on Ph | 2026 | Journal of Computing and Informa | PIML+机理 | 损失嵌入(偏差机理) | 飞机长桁装配偏差动态预测 | 实测+机理 | 含实测 | 0 |
| A02 | Facilitating digital assembly: A physics-informed graph lear | 2026 | Journal of Manufacturing Systems | PIGL | 混合(图+物理损失) | 螺栓法兰连接装配偏差预测 | 仿真+实测 | 实测+仿真 | 0 |
| A03 | Physics-Constrained Bayesian Optimization for Optimal Actuat | 2022 | IEEE Transactions on Automation  | 物理约束BO | 约束嵌入 | 复合材料结构装配作动器布局 | 仿真 | 纯仿真 | 18 |
| A04 | A hybrid rigid-compliant computational framework for large-s | 2026 | Engineering Structures | 传统+ML混合 | 架构嵌入(torsor) | 大尺寸装配变动传播 | 仿真 | 纯仿真 | 0 |
| A05 | SmartFixture: Physics-guided reinforcement learning for auto | 2024 | IISE Transactions | 物理引导RL | 约束嵌入 | 薄壁件夹具布局(装配变形) | FEA仿真 | 纯仿真 | 3 |
| A06 | Fast and accurate active alignment of camera lenses with phy | 2025 | Optics Express | 物理信息DL | 损失嵌入 | 光学镜头主动对准(精密装配) | 实测 | 含实测 | 6 |
| A07 | Physics-Informed Multi-Fidelity Graph Learning for Sequence- | 2026 | Sensors | PIGL | 混合 | 多保真图代理(场景待通读) | 多保真 | N/A（综述/知识/方法） | 0 |
| A08 | A manifold learning-assisted generative adversarial network  | 2026 | Thin-Walled Structures | 流形学习+GAN | 数据嵌入(物理流形) | 装配应力场快速预测 | 仿真 | 纯仿真 | 0 |
| A10 | Leveraging Physics-Informed Neural Networks for Efficient To | 2026 | Procedia CIRP | PINN | 损失嵌入 | 容差分析直接应用(CAT2026) | 仿真 | 纯仿真 | 0 |
| A11 | Adaptive Planning Method for ERS Point Layout in Aircraft As | 2026 | Sensors | 物理代理 | 混合 | 飞机装配 ERS 点布局规划 | 仿真 | 纯仿真 | 0 |
| D01 | Digital twin-based high-precision assembly method for large- | 2026 | J. Manuf. Syst. | 数字孪生 | 数据嵌入 | 大直径舱段对接装配 | 多保真(DT) | N/A（综述/知识/方法） | 0 |
| D02 | Digital Twin-driven Inversion of Assembly Precision for Indu | 2025 | Chinese Journal of Mechanical En | 数字孪生+ML | 数据嵌入 | 工业装备装配精度反演 | 多保真(DT) | N/A（综述/知识/方法） | 6 |
| D03 | Online geometry assurance in individualized production by fe | 2022 | Journal of Manufacturing Systems | 数字孪生 | 模型校准 | 钣金件装配在线几何保证 | 实测+仿真 | 实测+仿真 | 19 |
| D04 | Digital Twin-Based Clamping Sequence Analysis and Optimizati | 2024 | Applied Sciences | 数字孪生 | 数据嵌入 | 钣金装配夹紧序列优化 | 仿真 | 纯仿真 | 12 |
| D05 | Quality Prediction and Control of Assembly and Welding Proce | 2020 | Scanning | 数字孪生 | 数据嵌入 | 船舶装配焊接质量预测 | 实测 | 含实测 | 42 |
| M08 | A Bayesian framework to estimate part quality and associated | 2019 | Computers in Industry | 贝叶斯 | 不确定性建模 | 多工序制造件质量估计 | 实测 | 含实测 | 46 |
| M04 | Surrogate model–based optimal feed-forward control for dimen | 2018 | Journal of Quality Technology | 代理模型 | 无 | 复合材料件尺寸变动前馈控制 | 仿真 | 纯仿真 | 35 |
| M07 | Inspection by exception: A new machine learning-based approa | 2020 | Applied Soft Computing | ML | 无 | 多工序制造质量预测 | 实测 | 含实测 | 31 |
| M05 | Anomaly detection in Skin Model Shapes using machine learnin | 2019 | The International Journal of Adv | ML分类 | 无 | Skin Model Shapes 异常检测 | 仿真 | 纯仿真 | 30 |
| M02 | Neural Network Gaussian Process Considering Input Uncertaint | 2020 | IEEE/ASME Transactions on Mechat | NN-GP | 输入不确定性建模 | 复合材料结构装配偏差与残余应力 | 仿真 | 纯仿真 | 27 |
| M01 | DeviationGAN: A generative end-to-end approach for the devia | 2023 | Mechanical Systems and Signal Pr | GAN | 无(纯数据) | 钣金装配偏差端到端预测 | 仿真+实测 | 实测+仿真 | 24 |
| M11 | A new surrogate model–based method for individualized spot w | 2019 | The International Journal of Adv | 代理模型 | 无 | 点焊序列优化(几何偏差) | 仿真 | 纯仿真 | 22 |
| M13 | Reduced-order modelling for real-time physics-based variatio | 2024 | The International Journal of Adv | 降阶模型 | 物理模型降阶 | 柔顺装配变动实时仿真 | 仿真 | 纯仿真 | 17 |
| T03 | Integrating form errors and local surface deformations into  | 2018 | Computer-Aided Design | SMS+FEA | — | 形状误差+局部变形容差分析 | 仿真 | 纯仿真 | 88 |
| T15 | Virtual Geometry Assurance Process and Toolbox | 2016 | Procedia CIRP | 几何保证 | — | 虚拟几何保证流程 | 实测+仿真 | 实测+仿真 | 73 |
| T04 | Manufacturing signature in jacobian and torsor models for to | 2016 | Robotics and Computer-Integrated | Jacobian-Torso | — | 刚性件容差分析(制造签名) | 仿真 | 纯仿真 | 48 |
| T02 | Status and Prospects of Skin Model Shapes for Geometric Vari | 2016 | Procedia CIRP | Skin Model Sha | — | 几何变动管理综述 | — | N/A（综述/知识/方法） | 44 |
| T22 | Variation Simulation During Assembly of Non-rigid Components | 2016 | Procedia CIRP | 柔顺装配仿真 | — | 非刚性件装配仿真(ANATOLEFLEX) | 仿真 | 纯仿真 | 39 |
| T05 | Manufacturing signature in variational and vector-loop model | 2016 | The International Journal of Adv | Variational/Ve | — | 刚性件容差分析 | 仿真 | 纯仿真 | 34 |
| T24 | Optimal design of fixture layouts for compliant sheet metal  | 2020 | The International Journal of Adv | 夹具优化 | — | 柔顺钣金装配夹具布局 | 仿真 | 纯仿真 | 32 |
| T08 | A generic integrated approach of assembly tolerance analysis | 2020 | Proceedings of the Institution o | SMS | — | 装配容差分析通用框架 | 仿真 | 纯仿真 | 31 |
| T06 | Assembly tolerance analysis based on the Jacobian model and  | 2019 | Assembly Automation | Jacobian+SMS | — | 装配容差分析 | 仿真 | 纯仿真 | 27 |
| T12 | Assembly accuracy analysis of cylindrical parts based on ski | 2023 | Precision Engineering | SMS | — | 回转件装配精度 | 仿真 | 纯仿真 | 26 |
| O09 | Visual quality and sustainability considerations in toleranc | 2015 | International Journal of Product | 优化 | — | 视觉质量-可持续容差优化 | — | N/A（综述/知识/方法） | 25 |
| O07 | Tolerance management during the design of composite structur | 2021 | The International Journal of Adv | 变动管理 | — | 复材结构设计容差管理 | 仿真 | 纯仿真 | 20 |
| O02 | Ontological model-based optimal determination of geometric t | 2019 | Journal of Engineering Design | 本体+优化 | — | 非刚性装配几何容差确定 | 知识+仿真 | 纯仿真 | 17 |
| O10 | Coaxiality error analysis and optimization of cylindrical pa | 2022 | The International Journal of Adv | 误差优化 | — | CNC车削同轴度 | 实测 | 含实测 | 17 |
| O01 | Optimal Tolerance Allocation in a Complex Assembly Using Evo | 2016 | International Journal of Simulat | 进化算法 | — | 复杂装配容差分配 | 仿真 | 纯仿真 | 14 |
| E05 | Physics-Informed Neural Networks for Solving Forward and Inv | 2023 | IEEE Transactions on Neural Netw | PINN | 损失嵌入 | 复杂梁系统(机翼相邻) | 仿真 | 纯仿真 | 135 |
| E09 | Physics-Informed Neural Networks With Weighted Losses by Unc | 2023 | IEEE Transactions on Neural Netw | PINN+UQ | 加权损失 | 不确定性加权训练 | 仿真 | 纯仿真 | 99 |
| E06 | Physics-informed neural network with transfer learning (TL-P | 2023 | Scientific Reports | PINN+迁移 | 损失嵌入 | 域相似度迁移学习 | 仿真 | 纯仿真 | 88 |
| E04 | Solving forward and inverse problems of contact mechanics us | 2024 | Advanced Modeling and Simulation | PINN | 损失嵌入 | 接触力学正逆问题 | 仿真 | 纯仿真 | 77 |
| E01 | Physics-informed neural networks for data-free surrogate mod | 2023 | Materials & Design | PINN | 损失嵌入 | 工程优化代理(无数据) | 无数据 | 纯仿真 | 45 |
| E08 | A physics-informed and data-driven framework for robotic wel | 2025 | Nature Communications | PIML | 混合 | 机器人焊接 | 实测+仿真 | 实测+仿真 | 43 |
| E02 | Accelerating Thermal Simulations in Additive Manufacturing b | 2023 | Journal of Computing and Informa | PINN | 损失嵌入 | 增材热仿真加速 | 仿真 | 纯仿真 | 31 |
| C02 | Scientific Machine Learning Through Physics–Informed Neural  | 2022 | Journal of Scientific Computing | 综述 | — | PINN方法与趋势 | — | N/A（综述/知识/方法） | 2658 |
| C04 | Physics-Informed Neural Network (PINN) Evolution and Beyond: | 2022 | Big Data Cogn. Comput. | 综述 | — | PINN演进 | — | N/A（综述/知识/方法） | 255 |
| C06 | Advancements in Physics-Informed Neural Networks for Laminat | 2024 | Mathematics | 综述 | — | 层合复合材料PINN | — | N/A（综述/知识/方法） | 70 |
| C08 | NeuralPDE: Automating Physics-Informed Neural Networks (PINN | 2021 | arXiv (Cornell University) | 工具 | — | PINN自动化工具 | — | N/A（综述/知识/方法） | 50 |
| C07 | Physics-Informed Neural Networks in Polymers: A Review | 2025 | Polymers | 综述 | — | 聚合物PINN | — | N/A（综述/知识/方法） | 44 |
| K01 | Knowledge graph–enabled tolerancing experience acquisition a | 2023 | Int. J. Adv. Manuf. Technol. | 知识图谱 | — | 容差规范经验获取与重用 | 经验知识 | N/A（综述/知识/方法） | — |
| K02 | 一种融合物理信息屈曲代理的曲线纤维机翼智能优化算法（发明专利申请） | 2026 | CN122174367A | 物理信息代理 | 损失嵌入(屈曲) | 曲线纤维机翼优化 | 仿真 | 纯仿真 | — |