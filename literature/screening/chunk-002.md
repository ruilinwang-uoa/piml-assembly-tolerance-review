# 筛查分块 2（记录 51–100 / 共 449）

## 51. Prediction of power evolution in second-order Raman systems based on PINN

- year: 2025 | venue:  | tier: A | relevance: 11 | citations: 1
- doi: 10.1117/12.3055798 | key: `doi:10.1117/12.3055798`
- source: Q1

**Abstract**: The application of second-order Raman amplifiers is growing due to their superior performance, but modeling these systems is complex and computationally demanding. Traditional numerical methods for simulating Raman power evolution require extensive resources and are highly sensitive to initial conditions, leading to potential inaccuracies. Data-driven machine learning models have been explored as alternatives, but they often require large datasets and are prone to underfitting or overfitting. Physics-Informed Neural Networks (PINNs) offer a promising solution, integrating physics-based constraints directly into the model. While previously applied only to first-order Raman systems, this paper extends PINNs to second-order Raman systems. By combining neural network capabilities with boundary conditions from Raman coupling equations, PINNs can simulate signal evolution accurately. Experiments with a 200 km bidirectional Raman system show that PINN achieves less than 1 dB error, improved efficiency, and higher tolerance for boundary conditions compared to traditional methods. These findings highlight PINN's potential for accurate and practical applications in Raman system modeling.

## 52. Physics-Informed Neural Networks For Semiconductor Film Deposition: A Review

- year: 2025 | venue: arXiv (Cornell University) | tier: B | relevance: 11 | citations: 0
- doi: 10.48550/arxiv.2507.10983 | key: `doi:10.48550/arxiv.2507.10983`
- source: Q3

**Abstract**: Semiconductor manufacturing relies heavily on film deposition processes, such as Chemical Vapor Deposition and Physical Vapor Deposition. These complex processes require precise control to achieve film uniformity, proper adhesion, and desired functionality. Recent advancements in Physics-Informed Neural Networks (PINNs), an innovative machine learning (ML) approach, have shown significant promise in addressing challenges related to process control, quality assurance, and predictive modeling within semiconductor film deposition and other manufacturing domains. This paper provides a comprehensive review of ML applications targeted at semiconductor film deposition processes. Through a thematic analysis, we identify key trends, existing limitations, and research gaps, offering insights into both the advantages and constraints of current methodologies. Our structured analysis aims to highlight the potential integration of these ML techniques to enhance interpretability, accuracy, and robustness in film deposition processes. Additionally, we examine state-of-the-art PINN methods, discussing strategies for embedding physical knowledge, governing laws, and partial differential equations in

## 53. tongne/Physics-Informed-Neural-Networks-SD-PINN-SDFEET-PINN: SD-PINN AND SDFEET-PINN V1

- year: 2025 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: B | relevance: 11 | citations: 0
- doi: 10.5281/zenodo.17620005 | key: `doi:10.5281/zenodo.17620005`
- source: Q3

**Abstract**: This version presents our SD-PINN and SDFEET-PINN models, as well as the classical PINN, PINN1, and PINN2 formulations. The models are applied to a thermal convection problem and to a thermal diffusion problem in a complex hydraulic seal that has been the subject of several studies in L-PBF additive manufacturing.

## 54. tongne/Physics-Informed-Neural-Networks-SD-PINN-SDFEET-PINN: SD-PINN AND SDFEET-PINN V1

- year: 2025 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: B | relevance: 11 | citations: 0
- doi: 10.5281/zenodo.17620004 | key: `doi:10.5281/zenodo.17620004`
- source: Q3

**Abstract**: This version presents our SD-PINN and SDFEET-PINN models, as well as the classical PINN, PINN1, and PINN2 formulations. The models are applied to a thermal convection problem and to a thermal diffusion problem in a complex hydraulic seal that has been the subject of several studies in L-PBF additive manufacturing.

## 55. Surface Roughness Prediction of CNC Lathe Machined Hardened Steel Using Physics-Informed Neural Network Leveraging Transfer Learning

- year: 2025 | venue:  | tier: B | relevance: 11 | citations: 0
- doi: 10.1109/icset65917.2025.11284154 | key: `doi:10.1109/icset65917.2025.11284154`
- source: Q3

**Abstract**: Data-centric models are revolutionizing the manufacturing industry. However, many challenges arise, especially when the system begins operating under new conditions, due to limited data availability. Furthermore, neural network models usually need a lot of data to increase prediction accuracy. Collecting manufacturing data is both costly and complex. To overcome this challenge, this paper proposes a data-efficient Physics-Informed Neural Network (PINN) model that leverages transfer learning and ensemble modeling for CNC machining. An ensemble of the PINNs framework was trained on the dry machining condition and then transferred and fine-tuned on a small dataset (27 rows) in a different cutting environment, the flood cooling condition. Physics-based rules are integrated into PINN to manage cutting parameters (speed, feed, depth of cut). The results show a significant improvement in the accuracy of predicting surface roughness. To maintain the model's reliability, both tests-ensemble PINN (pure transfer) and ensemble fine-tune PINN were conducted on unseen data, the 20 % of the working dataset kept aside. The pure transfer model fails to evaluate the target value with an$\mathbf{R}^{

## 56. Deep vs. Shallow: Benchmarking Physics-Informed Neural Architectures on the Biharmonic Equation

- year: 2025 | venue: arXiv (Cornell University) | tier: B | relevance: 11 | citations: 0
- doi: 10.48550/arxiv.2510.04490 | key: `doi:10.48550/arxiv.2510.04490`
- source: Q3

**Abstract**: Partial differential equation (PDE) solvers are fundamental to engineering simulation. Classical mesh-based approaches (finite difference/volume/element) are fast and accurate on high-quality meshes but struggle with higher-order operators and complex, hard-to-mesh geometries. Recently developed physics-informed neural networks (PINNs) and their variants are mesh-free and flexible, yet compute-intensive and often less accurate. This paper systematically benchmarks RBF-PIELM, a rapid PINN variant-an extreme learning machine with radial-basis activations-for higher-order PDEs. RBF-PIELM replaces PINNs' time-consuming gradient descent with a single-shot least-squares solve. We test RBF-PIELM on the fourth-order biharmonic equation using two benchmarks: lid-driven cavity flow (streamfunction formulation) and a manufactured oscillatory solution. Our results show up to $(350\times)$ faster training than PINNs and over $(10\times)$ fewer parameters for comparable solution accuracy. Despite surpassing PINNs, RBF-PIELM still lags mature mesh-based solvers and its accuracy degrades on highly oscillatory solutions, highlighting remaining challenges for practical deployment.

## 57. Efficient Bayesian model updating of large-scale bridges based on physics-informed neural networks surrogate model

- year: 2026 | venue: Structures | tier: B | relevance: 11 | citations: 0
- doi: 10.1016/j.istruc.2026.112311 | key: `doi:10.1016/j.istruc.2026.112311`
- source: Q3

**Abstract**: An accurate baseline finite element model (FEM) is essential for the subsequent structural condition assessment and damage identification. Bayesian framework is widely adopted to update the initial FEM for a more accurate baseline, owing to its noise robustness and uncertainty quantification. However, the solution of the posterior distribution of structural updating factors usually relies on Markov chain Monte Carlo (MCMC) method. The redundant and time-consuming matrix assembly in repeated numerical modelling causes a serious computational burden, preventing the application to large-scale structures. To address this drawback, a novel physics-informed neural network (PINN) surrogate model is proposed based on natural frequency order correctness and mode shape mass orthogonality. The PINN surrogate model, combined with Hamiltonian Monte Carlo sampling, forms an efficient Bayesian FEM updating method applicable to large-scale continuous rigid-frame bridges. Comparative analyses with other surrogate models, including neural network, Gaussian process regression, and Polynomial chaos expansion, show that the proposed PINN surrogate model can ensure physical consistency on the limited an

## 58. Tackling Failure Modes of PINNs and PIKANs Using Conflict-Free Gradients

- year: 2026 | venue: arXiv (Cornell University) | tier: B | relevance: 11 | citations: 0
- doi: — | key: `t:tacklingfailuremodesofpinnsandpikansusingconflictfreegradients`
- source: Q3

**Abstract**: Scientific machine learning methods such as physics-informed neural networks (PINNs) increasingly rely on domain decomposition for better scalability while solving partial differential equations (PDEs) over complex geometries, yet the resulting composite loss comprising residual, boundary, and interface terms is highly susceptible to conflicting gradients that degrade training. This work bridges domain decomposition with projection-based gradient surgery to systematically mitigate such conflicts in 2D and 3D settings. We evaluate two existing projection-based algorithms, PCGrad and ConFIG, and identify their performance degradation in specific scenarios such as 3D domains with multiple overlapping interfaces. To address this limitation, we propose Norm-PCGrad, a normalized variant that achieves state-of-the-art accuracy across a range of 2D and 3D domain decomposition problems. Across the benchmarks considered, Norm-PCGrad consistently achieves the lowest relative $L_2$ error compared to training without gradient surgery as well as to existing algorithms such as PCGrad and ConFIG, while incurring negligible additional computational overhead. To improve computational efficiency of d

## 59. NeuralPDE: Automating Physics-Informed Neural Networks (PINNs) with Error Approximations

- year: 2021 | venue: arXiv.org | tier: A | relevance: 10 | citations: 102
- doi: — | key: `t:neuralpdeautomatingphysicsinformedneuralnetworkspinnswitherrorapproximations`
- source: S2-Q1

**Abstract**: Physics-informed neural networks (PINNs) are an increasingly powerful way to solve partial differential equations, generate digital twins, and create neural surrogates of physical models. In this manuscript we detail the inner workings of NeuralPDE.jl and show how a formulation structured around numerical quadrature gives rise to new loss functions which allow for adaptivity towards bounded error tolerances. We describe the various ways one can use the tool, detailing mathematical techniques like using extended loss functions for parameter estimation and operator discovery, to help potential users adopt these PINN-based techniques into their workflow. We showcase how NeuralPDE uses a purely symbolic formulation so that all of the underlying training code is generated from an abstract formulation, and show how to make use of GPUs and solve systems of PDEs. Afterwards we give a detailed performance analysis which showcases the trade-off between training techniques on a large set of PDEs. We end by focusing on a complex multiphysics example, the Doyle-Fuller-Newman (DFN) Model, and showcase how this PDE can be formulated and solved with NeuralPDE. Together this manuscript is meant to 

## 60. Efficient Error Certification for Physics-Informed Neural Networks

- year: 2023 | venue: International Conference on Machine Learning | tier: A | relevance: 10 | citations: 11
- doi: — | key: `t:efficienterrorcertificationforphysicsinformedneuralnetworks`
- source: S2-Q1

**Abstract**: Recent work provides promising evidence that Physics-Informed Neural Networks (PINN) can efficiently solve partial differential equations (PDE). However, previous works have failed to provide guarantees on the worst-case residual error of a PINN across the spatio-temporal domain - a measure akin to the tolerance of numerical solvers - focusing instead on point-wise comparisons between their solution and the ones obtained by a solver on a set of inputs. In real-world applications, one cannot consider tests on a finite set of points to be sufficient grounds for deployment, as the performance could be substantially worse on a different set. To alleviate this issue, we establish guaranteed error-based conditions for PINNs over their continuous applicability domain. To verify the extent to which they hold, we introduce $\partial$-CROWN: a general, efficient and scalable post-training framework to bound PINN residual errors. We demonstrate its effectiveness in obtaining tight certificates by applying it to two classically studied PINNs - Burgers' and Schr\"odinger's equations -, and two more challenging ones with real-world applications - the Allan-Cahn and Diffusion-Sorption equations.

## 61. AI-Powered Next-Generation Technology for Semiconductor Optical Metrology: A Review

- year: 2025 | venue: Micromachines | tier: B | relevance: 10 | citations: 9
- doi: 10.3390/mi16080838 | key: `doi:10.3390/mi16080838`
- source: Q3

**Abstract**: As semiconductor manufacturing advances into the angstrom-scale era characterized by three-dimensional integration, conventional metrology technologies face fundamental limitations regarding accuracy, speed, and non-destructiveness. Although optical spectroscopy has emerged as a prominent research focus, its application in complex manufacturing scenarios continues to confront significant technical barriers. This review establishes three concrete objectives: To categorize AI-optical spectroscopy integration paradigms spanning forward surrogate modeling, inverse prediction, physics-informed neural networks (PINNs), and multi-level architectures; to benchmark their efficacy against critical industrial metrology challenges including tool-to-tool (T2T) matching and high-aspect-ratio (HAR) structure characterization; and to identify unresolved bottlenecks for guiding next-generation intelligent semiconductor metrology. By categorically elaborating on the innovative applications of AI algorithms-such as forward surrogate models, inverse modeling techniques, physics-informed neural networks (PINNs), and multi-level network architectures-in optical spectroscopy, this work methodically asses

## 62. Comparative study of artificial neural network and physics-informed neural network application in sheet metal forming

- year: 2024 | venue: Materials research proceedings | tier: B | relevance: 10 | citations: 7
- doi: 10.21741/9781644903131-251 | key: `doi:10.21741/9781644903131-251`
- source: Q3

**Abstract**: Abstract. Accurate prediction of the resultant geometry in sheet metal forming simulation is necessary to achieve zero-defect production. To quantify the effect of process parameters on the final geometry, numerical methods are used to simulate the process outputs for a given set of process variables. Finite element methods are employed in process optimization and design exploration. However, these computationally expensive models are unhelpful for process control applications. Surrogate models allowing fast prediction of resultant geometry or stress distribution can be plausible solutions. In the current study, we propose a sequential surrogate model to fit the stress field as a function of the process variable and the initial spatial coordinates. The framework is composed of two surrogate models. First, an artificial neural network (ANN) evaluates the displacement and the strain. Then, a second surrogate is employed to fit the stress using input strain and displacement. Here, ANN and physics-informed neural networks (PINN) are compared concerning prediction accuracy for the second surrogate model. The PINN is enhanced with the equilibrium equations. The developed method is demons

## 63. Physics-informed machine learning surrogate for scalable simulation of thermal histories during wire-arc directed energy deposition

- year: 2025 | venue: Additive Manufacturing Letters | tier: B | relevance: 10 | citations: 7
- doi: 10.1016/j.addlet.2025.100327 | key: `doi:10.1016/j.addlet.2025.100327`
- source: Q3

**Abstract**: Wire-arc directed energy deposition (DED) has emerged as a promising additive manufacturing (AM) technology for large-scale applications. However, the complex thermal dynamics inherent to the process present challenges in ensuring structural integrity and mechanical properties of fabricated components. Finite element method (FEM) simulations have been conventionally employed to predict thermal history during deposition. However, their high computational demand increase significantly with scale. Given the necessity of multiple repetitive simulations for heat management and the determination of optimal printing strategy, FEM simulation quickly becomes unfit. Instead, advancements have been made in using trained neural networks as surrogate models for rapid prediction. However, traditional data-driven approaches necessitate large amounts of relevant and verifiable external data, either from simulation, experimental, or analytical solutions, during the training and validation of the neural network. Regarding large-scale wire-arc DED, none of these data sources are readily available in quantities sufficient for an accurate surrogate. The introduction of physics-informed neural networks 

## 64. Real‑Time Model Predictive Control of Monoclonal Antibody Capture in Continuous Manufacturing Using Physics‑Informed Neural Networks Accelerated Mechanistic Modeling

- year: 2025 | venue: Biotechnology and Bioengineering | tier: B | relevance: 10 | citations: 2
- doi: 10.1002/bit.70141 | key: `doi:10.1002/bit.70141`
- source: Q3

**Abstract**: Continuous bioprocessing with Protein A affinity chromatography has demonstrated great potential to increase productivity and reduce the cost of goods in monoclonal antibody (mAb) production. However, maintaining process stability and responding to dynamic changes remains significant challenges, particularly in the real-time optimization and control of multi-column periodic counter-current chromatography (PCC) for Protein A affinity chromatography, due to the computational complexity of rapidly solving mechanistic models. To address this challenge, this study developed distilled physics-informed neural networks (PINNs) based on the general rate model (GRM) to accelerate and enhance the breakthrough curve fitting and four-column PCC (4C-PCC) process optimization. The distilled PINNs achieved a balance between prediction accuracy and computational speed. The 157k-parameter distilled PINN enabled the breakthrough curve fitting and 4C-PCC process optimization approximately 10 times faster than numerical methods while improving accuracy by about 40%. A smaller 2k-parameter model achieved a 22-fold acceleration with an acceptable trade-off in accuracy, and the optimization time was reduc

## 65. Power-Based Normalization of Loss Terms to Improve the Performance of Physics-Informed Neural Networks (PINNs)

- year: 2024 | venue: Preprints.org | tier: B | relevance: 10 | citations: 1
- doi: 10.20944/preprints202408.0528.v1 | key: `doi:10.20944/preprints202408.0528.v1`
- source: Q3

**Abstract**: A novel approach is developed to improve the convergence of Physics-Informed Neural Networks (PINNs), aiming to employ them as real-time computational models within the framework of the digital twin for manufacturing processes. This method entails the weighting of physical equations, boundary conditions, and initial conditions to ensure their comparable magnitudes, with power being the chosen quantity in this study. The approach is applied to thermal problems, which are crucial for predicting manufacturing part defects. Different configurations, including complex boundary conditions and complex physics, were tested to assess the model’s robustness. The W-PINN demonstrates good predictions and strong stability compared to the classical PINN.

## 66. Novel Method to Improve the Convergence of Physics-Informed Neural Networks for Complex Thermal Simulations

- year: 2025 | venue: Applied Sciences | tier: B | relevance: 10 | citations: 1
- doi: 10.3390/app152212234 | key: `doi:10.3390/app152212234`
- source: Q3

**Abstract**: In the context of developing PINN methods for real-time digital twins in manufacturing processes, we propose a new approach that combines two complementary weighting strategies to significantly improve their convergence. The first method, called SD-PINN, balances the loss terms associated with the governing equations, boundary conditions, and initial conditions, ensuring that their contributions are dimensionally consistent and therefore comparable in magnitude. The second method, called SDFEET-PINN, rescales the terms of the governing equations during the early stages of training. This facilitates learning by temporarily modifying the equations to make terms comparable in amplitude, and then progressively restoring the original formulation, thereby preserving the influence of lower-magnitude terms that are often neglected in standard PINN approaches. We apply these methods to transient thermal problems, which are critical for predicting defects in Powder Bed Fusion (PBF). A range of 2D configurations with complex boundary conditions is used to test robustness, and a practical case study is carried out on heat transfer in a complex 3D geometry previously investigated both numerical

## 67. A Self-Aware Robotic Machining Architecture Based on Physics-Informed Neural Networks

- year: 2025 | venue:  | tier: B | relevance: 10 | citations: 1
- doi: 10.1109/icmcr64890.2025.10962807 | key: `doi:10.1109/icmcr64890.2025.10962807`
- source: Q3

**Abstract**: Industrial robots have been widely used in various industrial scenarios due to their flexibility and expandability. However, robots are susceptible to instability at high speeds and load conditions due to their low stiffness and dynamic characteristics variation with posture. Enhancing the processing stability of industrial robots through data-driven modeling and physical modeling approaches suffers from different drawbacks, such as solution complexity and weak interpretability. With the emergence of physics-informed neural networks (PINNs), new methodologies can be developed to enhance the self-aware processing of robots. In this paper, typical industry application scenarios and dynamics of robotics as well as PINNs are introduced and analyzed, and a framework and method based on PINNs are proposed to enhance the self-aware operation of industrial robots. This framework and methodology contribute to the researcher's efforts to apply PINNs more intensively to robot operation in the future to improve the stability and intelligence of robot operation.

## 68. Efficient Error Certification for Physics-Informed Neural Networks

- year: 2023 | venue: arXiv (Cornell University) | tier: A | relevance: 10 | citations: 0
- doi: 10.48550/arxiv.2305.10157 | key: `doi:10.48550/arxiv.2305.10157`
- source: Q1

**Abstract**: Recent work provides promising evidence that Physics-Informed Neural Networks (PINN) can efficiently solve partial differential equations (PDE). However, previous works have failed to provide guarantees on the worst-case residual error of a PINN across the spatio-temporal domain - a measure akin to the tolerance of numerical solvers - focusing instead on point-wise comparisons between their solution and the ones obtained by a solver on a set of inputs. In real-world applications, one cannot consider tests on a finite set of points to be sufficient grounds for deployment, as the performance could be substantially worse on a different set. To alleviate this issue, we establish guaranteed error-based conditions for PINNs over their continuous applicability domain. To verify the extent to which they hold, we introduce $\partial$-CROWN: a general, efficient and scalable post-training framework to bound PINN residual errors. We demonstrate its effectiveness in obtaining tight certificates by applying it to two classically studied PINNs - Burgers' and Schrödinger's equations -, and two more challenging ones with real-world applications - the Allan-Cahn and Diffusion-Sorption equations.

## 69. Hybrid Physics-Informed Neural Networks Integrating Multi-Relaxation-Time Lattice Boltzmann Method for Forward and Inverse Flow Problems

- year: 2025 | venue: Preprints.org | tier: B | relevance: 10 | citations: 0
- doi: 10.20944/preprints202510.1309.v1 | key: `doi:10.20944/preprints202510.1309.v1`
- source: Q1

**Abstract**: The development of stable, accurate, and generalizable numerical simulation methods remains a critical challenge in computational fluid dynamics (CFD). Recently, physics-informed neural networks (PINNs) have emerged as a promising approach by embedding physical laws directly into the loss function of neural networks, enabling mesh-free solutions of governing equations. PINNs offer a new perspective on CFD and open a significant pathway for AI for science. However, existing PINN models often face trade-offs between generality, stability, and accuracy. To address these trade-offs, this paper proposes a novel hybrid architecture, PINN-MRT, which integrates the multi-relaxation-time lattice Boltzmann method (MRT-LBM) with PINNs. For the first time, the MRT-LBM evolution equation is embedded as the physics-informed residual within the loss function. Due to the mesoscopic kinetic nature of the MRT-LBM equations, the proposed PINN-MRT inherently possesses the potential for fluid solution generality. The PINN-MRT adopts a dual-network architecture, which separately predicts macroscopic conserved variables and non-equilibrium distribution functions. A composite loss function is then constru

## 70. Variational Boosting for Physics-Informed Neural Networks

- year: 2026 | venue: arXiv (Cornell University) | tier: B | relevance: 10 | citations: 0
- doi: — | key: `t:variationalboostingforphysicsinformedneuralnetworks`
- source: Q1

**Abstract**: Physics-Informed Neural Networks (PINNs) solve differential equations by minimizing the residual of a nonlinear operator over a neural parameterization of the solution. However, monolithic PINNs often suffer from ill-conditioning, spectral bias, and optimization instability. We introduce a variational boosting framework in which solutions are constructed additively in function space. Each stage trains a weak learner whose converged correction satisfies a local orthogonality condition, equivalent to a projected functional gradient descent step onto the tangent space of the network's function manifold. Because each correction network is deliberately small, the restricted minimization admits full Newton or conjugate gradient updates, which are typically infeasible in large PINNs. The resulting method separates global nonlinear refinement into a sequence of well-conditioned subproblems while preserving the full variational structure of the operator. This framework provides a geometric interpretation of multi-stage PINNs as projected functional gradient descent and enables stable second-order optimization for nonlinear differential equations.

## 71. Physics‐informed neural network (PINN)‐embedded digital twinning for manufacturing sustainability: A framework for intelligent and adaptive process systems

- year: 2026 | venue: AIChE Journal | tier: B | relevance: 10 | citations: 0
- doi: 10.1002/aic.70611 | key: `doi:10.1002/aic.70611`
- source: Q1

**Abstract**: Abstract Advanced manufacturing comes into the digital age. Among strategic digital technologies, digital twin (DT) technology has been increasingly applied in industry. A more recent advancement in DT technology is the integration of physics‐informed neural networks (PINNs) in digital twinning, which enables the construction of a robust virtual plant. By leveraging real‐time data from a connected physical plant, the PINN‐based DT supports sustainability assessment, optimizes design and operation, predicts sustainability challenges, and identifies best possible technical solutions. In this paper, a PINN‐embedded modular DT framework is introduced for sustainable manufacturing. The PINNs are used to dynamically adjust key parameters in DT modules. This allows the resulting digital plant to be self‐evolving and capable of accurately mirroring, predicting, and improving the plant's sustainability performance. It also facilitates reconfiguring processes, where sustainability metrics are incorporated into process design. The methodological efficacy is demonstrated by developing and operating sustainable cleaning‐rinsing systems in electroplating plants.

## 72. Integrated Machine Learning and Smart Infrastructure Frameworks for Advanced Additive and Hybrid Manufacturing Systems

- year: 2026 | venue: Journal of Computer Science and Information Technology | tier: B | relevance: 10 | citations: 0
- doi: 10.61424/jcsit.v3i2.1015 | key: `doi:10.61424/jcsit.v3i2.1015`
- source: Q1

**Abstract**: Machine learning, digital twins, cyber-physical systems, and smart infrastructure are changing the way additive and hybrid manufacturing goes from static, process-defined to adaptive, data-driven manufacturing. The reviewed integrated architectural approach is able to link manufacturing at the physical level with the sensing, data infrastructure, physics-based modelling, surrogate modelling, artificial intelligence, and closed-loop control levels. Digital threads enable ongoing data connectivity and traceability from design to production, inspection, and maintenance phases, and digital twins maintain a dynamic representation of changing conditions in the processes. In the manufacturing sector, Edge and cloud infrastructure make it possible to capture and process data in real time and manage and analyze it at scale in a variety of factory conditions. Surrogate and physics-informed models complement high-fidelity physics-based simulations for reducing computational demands and enabling rapid prediction and optimization. Layer-to-layer and within-layer control strategies further allow the adjustment of manufacturing parameters in an adaptive way using real-time process information. Th

## 73. Application of Scientific Machine Learning Techniques to Metal Additive Manufacturing Simulation: A Comparison Between Physics-Informed Neural Networks and Extended Physics-Informed Neural Networks

- year: 2025 | venue:  | tier: B | relevance: 10 | citations: 0
- doi: 10.26153/tsw/63515 | key: `doi:10.26153/tsw/63515`
- source: Q3

**Abstract**: This paper presents a comparison between physics-informed neural network (PINN) and extended physics-informed neural network (XPINN), both scientific machine learning techniques, when applied to the same multi-layer simulation framework for multi-layer Direct Energy Deposition (DED) thermal history prediction. Whilst both techniques offer the benefits of being meshless and having derivative information readily available, they each have their own caveats. XPINN’s ‘divide-and-conquer’ strategy overcomes the classic deficiency of PINN when working with discontinuities at an increased computational cost. This comparison study aims to identify the threshold in complexity beyond which the increased computational cost is justified by the enhanced expressibility of XPINN.

## 74. Responsmatrisbaserat artificiellt neuralt nätverk av kärnklyvsystem

- year: 2026 | venue: Diva portal (Dalarna University Library) | tier: B | relevance: 10 | citations: 0
- doi: — | key: `t:responsmatrisbaseratartificielltneuraltntverkavkrnklyvsystem`
- source: Q3

**Abstract**: Advanced nuclear reactor analysis requires computational solvers that are both fast and physically reliable. While High-Fidelity Monte Carlo simulations are accurate, their computational cost is prohibitive for many applications. This thesis develops a Physics-Informed Neural Network (PINN) as an ultrafast surrogate model for the Response Matrix Method (RMM), bypassing the Monte Carlo bottleneck. A dataset of local subresponse matrices was generated using OpenMC for a 17x17 Pressurized Water Reactor (PWR) fuel assembly across various operational states. The PINN architecture, based on a Multi-Head ResNet, enforces neutronic and thermodynamic constraints such as neutron conservation and negative Doppler feedback. The model was benchmarked against an Unconstrained Deep Feed Forward Neural Network (FFNN) and a Random Forest (RF) regressor within a 3D coupled mini-core solver. Results show that the PINN accelerates global spatial evaluations by a factor exceeding $10^5$, reducing inference time from minutes to approximately one millisecond. Error decomposition analysis revealed that the Random Forest achieved artificial accuracy through unphysical error cancellation. In contrast, the P

## 75. An Advanced Mission Profile-based Lifetime Assessment in Power Electronics Assembly Using Physics-informed Surrogate Modeling

- year: 2026 | venue:  | tier: B | relevance: 10 | citations: 0
- doi: 10.1109/eurosime69483.2026.11511966 | key: `doi:10.1109/eurosime69483.2026.11511966`
- source: Q5

**Abstract**: Power modules under mission-profile operation develop thermo-mechanical fatigue in bond wires and solder joints due to temperature cycling. Empirical lifetime rules miss transient and sequential effects, while finite-element (FE) analysis, though physical, is computationally too expensive for application-close mission profile or system-level studies. We propose a physics-informed surrogate of an FE-modeled SiC power module that calculates in multi-physics domain to obtain damage indicators for bond-wire foot and solder interconnections, like plastic strain. Trained on FE simulations from ARTEMIS-derived profiles and evaluated on independent frames, Transformer and Temporal Convolution Network (TCN) were determined as the best deep models for bond wires and solder interconnection respectively. Moreover, random forest + AdaBoost (RF+ADA) was the most stable shallow alternative. All surrogate models can reach R2> 0.995 against FE results. Estimation of lifetime based on surrogate results stayed within a deviation of 10% in comparison to the strain calculated using FE model. It shows that the surrogate approaches may enable a mission profile-based reliability assessment for power elect

## 76. Analysing the role of physics-informed neural networks in modelling industrial systems through case studies in automotive manufacturing

- year: 2025 | venue: International Journal on Interactive Design and Manufacturing (IJIDeM) | tier: B | relevance: 9 | citations: 6
- doi: 10.1007/s12008-025-02364-w | key: `doi:10.1007/s12008-025-02364-w`
- source: Q3

**Abstract**: Abstract When modelling industrial systems, two major challenges need to be addressed: complexity and uncertainty. Traditional modelling approaches can be categorized into data-driven and physics-based methods. Data-driven models excel at identifying patterns but struggle with interpreting the complexities of physical systems and often require large amounts of data. In contrast, physics-based models rely on detailed information that is often incomplete or uncertain. To overcome these limitations, Physics-Informed Neural Networks (PINNs) have emerged as a hybrid approach, combining the flexibility of neural networks with the rigour of physical constraints. This approach leverages both data and physics to provide more accurate predictions. The paper reviews the applications of PINNs in industry, demonstrating their advantages over traditional methods, particularly in terms of efficiency and versatility. To validate the model, two case studies from the automotive industry are presented. The first case study involves predicting the thermal power of an industrial air handling unit (AHU) used in a topcoat painting process, while the second focuses on forecasting temperature profiles in a

## 77. Physics-informed and black-box Identification of robotic actuator with a flexible joint

- year: 2024 | venue: IFAC-PapersOnLine | tier: B | relevance: 9 | citations: 4
- doi: 10.1016/j.ifacol.2024.08.538 | key: `doi:10.1016/j.ifacol.2024.08.538`
- source: Q3

**Abstract**: In robotics, precise models are critical for ensuring safety and functionality. However, acquiring a precise model characterizing a system’s dynamics can be challenging. One of the alternatives to address this issue is system Identification, which aims to obtain models through physical and experimental observations. In this manner, the developments in machine learning algorithms, such as neural networks, have significantly improved the modeling of complex and nonlinear phenomena. In this work, a mass-spring-damper (MSD) system and a low-cost original elastomer-based Series Elastic Actuators (eSEA) assembly are used to evaluate the performance of system Identification models. The black-box models selected are variations of the AutoRegressive Moving Average with eXogenous input (ARMAX) algorithm. The gray-box model aims to estimate the parameters of 4 friction models; the optimization is done utilizing physics-informed neural networks (PINNs). For both case studies, the PINNs outperformed the black-box models. In the didactic example, the parameters obtained are close to the ground truth, and the highest determinant coefficient obtained is 0.99. The friction model that best represent

## 78. Inverted model selection in physics-informed neural networks: when a lower residual selects a worse solution

- year: 2026 | venue: arXiv (Cornell University) | tier: A | relevance: 9 | citations: 0
- doi: 10.48550/arxiv.2608.21683 | key: `doi:10.48550/arxiv.2608.21683`
- source: Q1

**Abstract**: Physics-informed neural networks (PINNs) are commonly evaluated via a single aggregate residual, assuming a smaller residual indicates a better solution. Testing this directly across three constrained PDE systems, I find this assumption can systematically fail. In matched pairs of solvers differing only in whether a defining structural identity is hard-wired or penalized, the penalized variant frequently attains a lower equation residual while violating that identity by several orders of magnitude, causing the exact variant to be falsely ranked worse. Over 64 matched pairs spanning two systems, four network variants, and eight seeds, this inversion occurs in 83\% of cases (95\% Wilson CI: 72--90\%), with rates from 72\% to 94\% across systems. Testing across six architectures--MLP, cPINN, XPINN, hp-VPINN, and physics-informed DeepONet and FNO--inverts the ranking in 46 of 48 pairs, indicating that this variability is problem-dependent rather than specific to the approximator. A third, larger vorticity--streamfunction problem shows the same ordering: the residual-optimal solver violates its structural identity by over six orders above tolerance, despite a residual margin of only 9.3

## 79. A Physics-informed Neural Network Approach for Robust Buckling Load Prediction and Reliability-Based Design of Thin Truncated Conical Shells

- year: 2026 | venue: arXiv (Cornell University) | tier: A | relevance: 9 | citations: 0
- doi: 10.48550/arxiv.2608.21818 | key: `doi:10.48550/arxiv.2608.21818`
- source: Q1

**Abstract**: Thin-walled truncated conical shells are widely used in aerospace, marine, offshore, and lightweight infrastructure systems due to their high strength-to-weight ratio and geometric efficiency. Their buckling resistance under axial compression, however, is highly sensitive to geometric imperfections, manufacturing tolerances, material variability, and nonlinear instability effects. Conventional design procedures rely on conservative knockdown factors (KDFs), such as those recommended in NASA SP-8019, which do not explicitly account for shell geometry, fabrication quality, data uncertainty, or target reliability. This study develops a physics-informed neural network (PiNN) framework for predicting critical buckling loads of thin truncated conical shells and integrates the trained surrogate within a reliability-based design (RBD) formulation. The model combines geometric and material descriptors with mechanics-informed features derived from shell stability theory and the localized reduced stiffness method (LRSM). A physics-informed loss function penalizes mechanically inadmissible predictions exceeding the theoretical elastic buckling load. The framework is trained and evaluated using

## 80. Adaptive Hard-Soft Physics-Informed Neural Networks for Robust Boundary-Constrained PDE Solving

- year: 2026 | venue: arXiv (Cornell University) | tier: B | relevance: 9 | citations: 0
- doi: — | key: `t:adaptivehardsoftphysicsinformedneuralnetworksforrobustboundaryconstrainedpdesolv`
- source: Q1

**Abstract**: Physics-informed neural networks (PINNs) provide an effective way to solve partial differential equations (PDEs) by embedding physical principles into the learning process. However, the conventional PINN formulation, in which all constraints are imposed as soft penalty terms within a composite loss, often exhibits slow convergence, sensitivity to loss weight scaling, and inaccurate boundary enforcement due to poor conditioning of the optimization landscape. To address these limitations, this study proposes a unified hard--soft physics--informed neural network (HSPINN) with adaptive loss weighting. In this framework, Dirichlet and periodic boundary conditions are enforced exactly by construction through analytical or polynomial lifting, masking functions, and periodic feature mappings, while the governing PDE residuals, Neumann fluxes, and initial conditions are treated as soft constraints. An inverse-share softmax strategy dynamically balances the relative importance of individual loss components during training, eliminating manual penalty tuning and improving gradient stability. This formulation ensures boundary admissibility throughout optimization and enhances convergence effici

## 81. PINNs for Stochastic Dynamics: Modeling Brownian Motion via Verlet Integration

- year: 2026 | venue: International Journal of Information Technology and Computer Science | tier: A | relevance: 9 | citations: 0
- doi: 10.5815/ijitcs.2026.02.08 | key: `doi:10.5815/ijitcs.2026.02.08`
- source: Q1

**Abstract**: This study presents a Physics-Informed Neural Network (PINN) framework for modeling stochastic systems like Brownian motion, designed to overcome critical challenges in physical consistency and numerical stability that affect classical solvers and standard data-driven models. Traditional numerical methods often struggle with high-dimensional spaces or sparse data, while many machine learning approaches fail to enforce fundamental physical laws. To address this, our proposed PINN architecture integrates a multi-component loss function that explicitly enforces the Fokker-Planck equation, which describes the system’s governing physics, alongside boundary conditions and a global probability conservation law. This physics-informed approach is anchored by high-fidelity training data generated from Verlet-integrated trajectories of the underlying Langevin dynamics. We validate our model against the analytical solution for one-dimensional Brownian motion, demonstrating its ability to accurately recover the true probability density function (PDF). Rigorous comparisons using statistical metrics show superior accuracy over a canonical data-driven operator learning model, DeepONet. Specificall

## 82. Physics-Informed Neural Network for Concrete Manufacturing Process Optimization

- year: 2024 | venue: arXiv (Cornell University) | tier: B | relevance: 9 | citations: 0
- doi: 10.48550/arxiv.2408.14502 | key: `doi:10.48550/arxiv.2408.14502`
- source: Q3

**Abstract**: Concrete manufacturing projects are one of the most common ones for consulting agencies. Because of the highly non-linear dependency of input materials like ash, water, cement, superplastic, etc; with the resultant strength of concrete, it gets difficult for machine learning models to successfully capture this relation and perform cost optimizations. This paper highlights how PINNs (Physics Informed Neural Networks) can be useful in the given situation. This state-of-the-art model shall also get compared with traditional models like Linear Regression, Random Forest, Gradient Boosting, and Deep Neural Network. Results of the research highlights how well PINNs performed even with reduced dataset, thus resolving one of the biggest issues of limited data availability for ML models. On an average, PINN got the loss value reduced by 26.3% even with 40% lesser data compared to the Deep Neural Network. In addition to predicting strength of the concrete given the quantity of raw materials, the paper also highlights the use of heuristic optimization method like Particle Swarm Optimization (PSO) in predicting quantity of raw materials required to manufacture concrete of given strength with le

## 83. Physics-Informed Neural Networks for Fast Thermal Simulation in Laser Wire Additive Manufacturing

- year: 2025 | venue:  | tier: B | relevance: 9 | citations: 0
- doi: 10.1109/mecatronics-rem67547.2025.11349643 | key: `doi:10.1109/mecatronics-rem67547.2025.11349643`
- source: Q3

**Abstract**: Robotized manufacturing processes such as Wire Arc Additive Manufacturing (WAAM) and Laser Wire Additive Manufacturing (LWAM) are inherently multi-physics and governed by partial differential equations (PDEs). Classical numerical solvers (FEM, FDM, FVM) provide accuracy but are often too slow for mechatronic use cases like real-time monitoring, model-predictive control, or high-fidelity digital twins. This paper demonstrates how Physics-Informed Neural Networks (PINNs) can approximate transient thermal fields in LWAM by minimizing PDE and boundary residuals directly, eliminating the need for meshing or time stepping at inference. We provide a reproducible PINN implementation, an ONNX-exportable inference wrapper for deployment, and a companion ONNX validator that confirms faithful model export by comparing ONNX predictions against the trained PyTorch model outputs (MAE $\lt0.001^{\circ} \mathrm{C}$).

## 84. Process-Variation-Aware Physics-Informed Neural Network for Statistical Electromagnetic Analysis of Advanced VLSI Interconnects

- year: 2026 | venue: International Journal of Computational and Biological Sciences | tier: B | relevance: 9 | citations: 0
- doi: 10.66238/ijcbs95 | key: `doi:10.66238/ijcbs95`
- source: Q3

**Abstract**: Advanced VLSI interconnects are increasingly dominated by electromagnetic parasitics whose statistical spread depends on line width, spacing, dielectric height, material permittivity, and conductor resistivity. Conventional variation-aware extraction requires repeated field solves and therefore becomes expensive when design exploration or yield screening needs thousands of samples. This paper proposes a process-variation-aware physics-informed neural network (PV-PINN) that maps spatial coordinates and process variables directly to the electrostatic potential field of a coupled interconnect cross-section. The model combines finite-difference calibration snapshots with a Laplace-equation residual, then propagates manufacturing variations through the trained surrogate to estimate capacitance, peak electric field, and an RC delay proxy. The study intentionally uses a transparent synthetic benchmark generated by an included deterministic finite-difference solver rather than unverified measurement data. On 16 held-out geometries, the PV-PINN achieved a mean potential-field RMSE of 0.0231, a mean capacitance error of 9.54%, and a mean delay-proxy error of 9.54%. In a 60-sample Monte Carlo

## 85. Non-contact discharge estimation using physics-informed neural networks and CNN-enhanced image velocimetry

- year: 2026 | venue: Journal of Hydrology | tier: B | relevance: 9 | citations: 0
- doi: 10.1016/j.jhydrol.2026.136015 | key: `doi:10.1016/j.jhydrol.2026.136015`
- source: Q3

**Abstract**: Accurate river discharge estimation using non-contact techniques remains a fundamental challenge in hydrology, particularly under complex field conditions. This study proposes a physics-informed framework for non-contact river discharge estimation by integrating CNN-enhanced Large-Scale Particle Image Velocimetry (CNN-LSPIV) with physics-informed neural networks (PINNs). The shallow water continuity equation is incorporated into the loss function to enforce mass conservation during velocity refinement and water depth inversion. Two inversion strategies are developed: a velocity-refinement mode (PINN-VR), which refines CNN-LSPIV velocity fields prior to leapfrog-based depth integration, and a direct depth inversion mode (PINN-DDI), which simultaneously reconstructs velocity and depth fields through global physics-constrained optimization. The framework is validated using laboratory flume experiments under three bed configurations (smooth, lateral composite, and longitudinal composite beds) and further evaluated through unmanned aerial vehicle (UAV)-based field observations with acoustic Doppler current profiler (ADCP) validation. CNN-LSPIV substantially improves surface velocity mea

## 86. Research-Ability-Orientated Course Design and Cultivation Examples of Numerical Simulation Technology on Manufacturing Processes for Graduate Students

- year: 2026 | venue: Higher Education Research | tier: B | relevance: 9 | citations: 0
- doi: 10.11648/j.her.20261102.12 | key: `doi:10.11648/j.her.20261102.12`
- source: Q3

**Abstract**: “Numerical Simulation Technology on Manufacturing Processes” is a graduate-level course designed for students majoring in mechanical engineering, especially in manufacturing technology. With the advancement of manufacturing and information technologies, the course has become significantly more applicable and practical for students across various manufacturing fields. To enable students not only to master numerical simulation techniques but also to extract and analyze engineering problems from a scientific perspective, this paper presents the course design, core contents, and representative outcomes as a reference. The main contents include: (1) the course background, target audience, and key instructional procedures, with an emphasis on the rationale behind student presentation sessions; (2) two typical manufacturing process case studies that illustrate how the course systematically enhances students’ research capabilities through the pre-simulation stages of problem extraction and model simplification; (3) a discussion on the application prospects of cutting-edge artificial intelligence (AI) technologies such as physics-informed neural networks (PINN) and graph neural networks (GN

## 87. Machine learning based surrogate modeling of the deformation behavior of large compliant thin-walled structures

- year: 2026 | venue: Procedia CIRP | tier: B | relevance: 9 | citations: 0
- doi: 10.1016/j.procir.2026.03.117 | key: `doi:10.1016/j.procir.2026.03.117`
- source: Q3

**Abstract**: The wide-spread adoption of large thin-walled structures made of carbon fiber reinforced polymers (CFRP) in the aeronautical sector contributes to better fuel efficiency and lower CO 2 emissions. However, despite their advantages, the automation of assembly processes involving these structures remains challenging due to their compliance which translates into a tendency to deform under process induced loads. Model-based control strategies can mitigate deformations during assembly, but high-fidelity simulations such as finite element models (FEM), though accurate, are too slow for real-time integration. While accurate, these simulations can be computationally expensive and time-consuming, particularly for large-scale problems or when multiple design iterations are required. This paper presents surrogate modeling approaches to approximate the mechanical response of large compliant thin-walled CFRP structures. The proposed work presents a benchmark study of different surrogate modeling techniques, ranging from classical machine learning methods to physics-informed neural networks utilizing the DeepFEM framework. The performance of these surrogate models is evaluated based on their accu

## 88. Physics-Guided Surrogate-Assisted Reinforcement Learning for Multi-Objective Coordinated Speed Control of a Shearer Under Complex Coal–Rock Conditions

- year: 2026 | venue: Machines | tier: B | relevance: 9 | citations: 0
- doi: 10.3390/machines14091016 | key: `doi:10.3390/machines14091016`
- source: Q3

**Abstract**: Advanced manufacturing and cutting machinery often operate under variable material properties and uncertain load conditions, making real-time process optimization difficult when high-fidelity simulations and physical experiments are costly. To address this problem, this study proposes a physics-guided surrogate-assisted reinforcement learning framework for multi-objective speed regulation of coal–rock cutting machinery. The haulage speed and drum rotational speed are jointly optimized to balance production rate, cutting specific energy consumption, current load, vibration impact, and speed-regulation stability. First, an EDEM–RecurDyn–Simulink co-simulation model was established to obtain cutting current and vibration response data under different coal–rock structures and speed combinations. Similar-material cutting experiments were conducted to validate the vibration response, with root mean square (RMS) relative errors of 3.38%, 4.21%, 5.75%, and 5.03% under full-coal, single-gangue-layer, double-gangue-layer, and full-rock conditions, respectively. Based on these data, an improved physics-informed neural network (PINN) surrogate model was developed by embedding an equivalent coa

## 89. Benchmarking Sim2Real Gap: High-fidelity Digital Twinning of Agile Manufacturing

- year: 2024 | venue: arXiv (Cornell University) | tier: B | relevance: 9 | citations: 0
- doi: 10.48550/arxiv.2409.10784 | key: `doi:10.48550/arxiv.2409.10784`
- source: Q5

**Abstract**: As the manufacturing industry shifts from mass production to mass customization, there is a growing emphasis on adopting agile, resilient, and human-centric methodologies in line with the directives of Industry 5.0. Central to this transformation is the deployment of digital twins, a technology that digitally replicates manufacturing assets to enable enhanced process optimization, predictive maintenance, synthetic data generation, and accelerated customization and prototyping. This chapter delves into the technologies underpinning the creation of digital twins specifically tailored to agile manufacturing scenarios within the realm of robotic automation. It explores the transfer of trained policies and process optimizations from simulated settings to real-world applications through advanced techniques such as domain randomization, domain adaptation, curriculum learning, and model-based system identification. The chapter also examines various industrial manufacturing automation scenarios, including bin-picking, part inspection, and product assembly, under Sim2Real conditions. The performance of digital twin technologies in these scenarios is evaluated using practical metrics includin

## 90. Inverted model selection in physics-informed neural networks: when a lower residual selects a worse solution

- year: 2026 | venue:  | tier: A | relevance: 9 | citations: 0
- doi: — | key: `t:invertedmodelselectioninphysicsinformedneuralnetworkswhenalowerresidualselectsaw`
- source: S2-Q1

**Abstract**: Physics-informed neural networks (PINNs) are commonly evaluated via a single aggregate residual, assuming a smaller residual indicates a better solution. Testing this directly across three constrained PDE systems, I find this assumption can systematically fail. In matched pairs of solvers differing only in whether a defining structural identity is hard-wired or penalized, the penalized variant frequently attains a lower equation residual while violating that identity by several orders of magnitude, causing the exact variant to be falsely ranked worse. Over 64 matched pairs spanning two systems, four network variants, and eight seeds, this inversion occurs in 83\% of cases (95\% Wilson CI: 72--90\%), with rates from 72\% to 94\% across systems. Testing across six architectures--MLP, cPINN, XPINN, hp-VPINN, and physics-informed DeepONet and FNO--inverts the ranking in 46 of 48 pairs, indicating that this variability is problem-dependent rather than specific to the approximator. A third, larger vorticity--streamfunction problem shows the same ordering: the residual-optimal solver violates its structural identity by over six orders above tolerance, despite a residual margin of only 9.3

## 91. A Physics-informed Neural Network Approach for Robust Buckling Load Prediction and Reliability-Based Design of Thin Truncated Conical Shells

- year: 2026 | venue:  | tier: A | relevance: 9 | citations: 0
- doi: — | key: `t:aphysicsinformedneuralnetworkapproachforrobustbucklingloadpredictionandreliabili`
- source: S2-Q1

**Abstract**: Thin-walled truncated conical shells are widely used in aerospace, marine, offshore, and lightweight infrastructure systems due to their high strength-to-weight ratio and geometric efficiency. Their buckling resistance under axial compression, however, is highly sensitive to geometric imperfections, manufacturing tolerances, material variability, and nonlinear instability effects. Conventional design procedures rely on conservative knockdown factors (KDFs), such as those recommended in NASA SP-8019, which do not explicitly account for shell geometry, fabrication quality, data uncertainty, or target reliability. This study develops a physics-informed neural network (PiNN) framework for predicting critical buckling loads of thin truncated conical shells and integrates the trained surrogate within a reliability-based design (RBD) formulation. The model combines geometric and material descriptors with mechanics-informed features derived from shell stability theory and the localized reduced stiffness method (LRSM). A physics-informed loss function penalizes mechanically inadmissible predictions exceeding the theoretical elastic buckling load. The framework is trained and evaluated using

## 92. Bonobos Show Limited Social Tolerance in a Group Setting: A Comparison with Chimpanzees and a Test of the Relational Model

- year: 2015 | venue: Folia Primatologica | tier: B | relevance: 8 | citations: 36
- doi: 10.1159/000373886 | key: `doi:10.1159/000373886`
- source: Q13-CR

**Abstract**:  Social tolerance is a core aspect of primate social relationships with implications for the evolution of cooperation, prosociality and social learning. We measured the social tolerance of bonobos in an experiment recently validated with chimpanzees to allow for a comparative assessment of group-level tolerance, and found that the bonobo group studied here exhibited lower social tolerance on average than chimpanzees in this paradigm. Furthermore, following the Relational Model of de Waal, we investigated whether bonobos responded to an increased potential for social conflict with tolerance, conflict avoidance or conflict escalation, and found that only behaviours indicative of conflict escalation differed across conditions. Taken together, these findings contribute to the current debate over the level of social tolerance of bonobos and lend support to the position that the social tolerance of bonobos may not be notably high compared with other primates. 

## 93. Machine learning for metal additive manufacturing: Predicting temperature and melt pool fluid dynamics using physics-informed neural networks

- year: 2020 | venue: arXiv (Cornell University) | tier: B | relevance: 8 | citations: 17
- doi: 10.48550/arxiv.2008.13547 | key: `doi:10.48550/arxiv.2008.13547`
- source: Q3

**Abstract**: The recent explosion of machine learning (ML) and artificial intelligence (AI) shows great potential in the breakthrough of metal additive manufacturing (AM) process modeling. However, the success of conventional machine learning tools in data science is primarily attributed to the unprecedented large amount of labeled data-sets (big data), which can be either obtained by experiments or first-principle simulations. Unfortunately, these labeled data-sets are expensive to obtain in AM due to the high expense of the AM experiments and prohibitive computational cost of high-fidelity simulations. We propose a physics-informed neural network (PINN) framework that fuses both data and first physical principles, including conservation laws of momentum, mass, and energy, into the neural network to inform the learning processes. To the best knowledge of the authors, this is the first application of PINN to three dimensional AM processes modeling. Besides, we propose a hard-type approach for Dirichlet boundary conditions (BCs) based on a Heaviside function, which can not only enforce the BCs but also accelerate the learning process. The PINN framework is applied to two representative metal man

## 94. Bead geometry prediction in wire arc directed energy deposition using physics-informed machine learning and low-fidelity data

- year: 2025 | venue: Additive manufacturing | tier: A | relevance: 8 | citations: 15
- doi: 10.1016/j.addma.2025.104881 | key: `doi:10.1016/j.addma.2025.104881`
- source: Q3

**Abstract**: Wire Arc Directed Energy Deposition (Wire Arc DED) is a promising metal additive manufacturing technique, yet accurate bead geometry prediction remains a challenge due to the complex thermal and geometric interactions in the process. In this study, we present a coupled Physics-Informed Neural Network (PINN) framework to predict the bead geometry by integrating the governing process physics and experimental data, thereby addressing the limitations of both computationally expensive numerical models and purely data-driven approaches. The model employs a sequential two-step workflow, where a thermal model first predicts temperature evolution, which subsequently informs a geometry model for predicting the bead geometry. Results indicate that a high-fidelity PINN model with high spatiotemporal resolution captures the intricately coupled thermal and geometric variations inherent to bead deposition with good predictive accuracy albeit at a higher computational cost, while a low-fidelity PINN model with lower spatiotemporal resolution offers a computationally efficient alternative with marginally higher errors. The incorporation of measured bead geometry data significantly enhances predicti

## 95. A Data-driven Multi-fidelity Physics-informed Learning Framework for Smart Manufacturing: A Composites Processing Case Study

- year: 2022 | venue:  | tier: B | relevance: 8 | citations: 12
- doi: 10.1109/icps51978.2022.9816983 | key: `doi:10.1109/icps51978.2022.9816983`
- source: Q3

**Abstract**: Despite the successful implementations of physics-informed neural networks in different scientific domains, it has been shown that for complex nonlinear systems, achieving an accurate model requires extensive hyperparameter tuning, network architecture design, and costly and exhaustive training processes. To avoid such obstacles and make the training of physics-informed models less precarious, in this paper, a data-driven multi-fidelity physics-informed framework is proposed based on transfer learning principles. The framework incorporates the knowledge from low-fidelity (auxiliary) systems and limited labeled data from target (actual) system to significantly improve the performance of conventional physics-informed models. While minimizing the efforts of designing a complex task-specific network for the problem at hand, the proposed settings guide the physics-informed model towards a fast and efficient convergence to a global optimum. An adaptive weighting method is utilized to further enhance the optimization of the model's composite loss function during the training process. A data-driven strategy is also introduced for maintaining high performance in subdomains with significant 

## 96. Close the Design-to-Manufacturing Gap in Computational Optics with a 'Real2Sim' Learned Two-Photon Neural Lithography Simulator

- year: 2023 | venue:  | tier: B | relevance: 8 | citations: 12
- doi: 10.1145/3610548.3618251 | key: `doi:10.1145/3610548.3618251`
- source: Q7

**Abstract**: We introduce neural lithography to address the ‘design-to-manufacturing’ gap in computational optics. Computational optics with large design degrees of freedom enable advanced functionalities and performance beyond traditional optics. However, the existing design approaches often overlook the numerical modeling of the manufacturing process, which can result in significant performance deviation between the design and the fabricated optics. To bridge this gap, we, for the first time, propose a fully differentiable design framework that integrates a pre-trained photolithography simulator into the model-based optical design loop. Leveraging a blend of physics-informed modeling and data-driven training using experimentally collected datasets, our photolithography simulator serves as a regularizer on fabrication feasibility during design, compensating for structure discrepancies introduced in the lithography process. We demonstrate the effectiveness of our approach through two typical tasks in computational optics, where we design and fabricate a holographic optical element (HOE) and a multi-level diffractive lens (MDL) using a two-photon lithography system, showcasing improved optical p

## 97. Physics-informed data-driven modeling of AC optimal power flow via quadratic approximation

- year: 2026 | venue: International Journal of Electrical Power & Energy Systems | tier: A | relevance: 8 | citations: 3
- doi: 10.1016/j.ijepes.2026.111714 | key: `doi:10.1016/j.ijepes.2026.111714`
- source: Q1

**Abstract**: Parameters in alternating-current optimal power flow (AC-OPF) models evolve with operating conditions and equipment aging, which can create a gap between analytical models and field behavior. To mitigate this effect, this paper leverages field measurements within a physics-informed, data-driven framework that preserves the OPF structure while learning high-fidelity quadratic surrogates of network physics. Two complementary models are proposed. The Convex Quadratic Approximation Model (CQAM) replaces non-convex constraints with data-driven convex under-estimators and concave over-estimators constructed via sparsity-promoting semidefinite programming (SDP), yielding a tractable convex program that admits globally optimal solutions for the convexified problem. The Non-convex Quadratic Approximation Model (NQAM) learns explicit quadratic equalities through regularized quadratic programming (QP), closely matching the AC-feasible set and producing solutions that satisfy power flow constraints within numerical tolerances. A cooperative workflow exploits their strengths: CQAM provides fast screening and dispatch when tractability is critical, whereas NQAM refines solutions and supports fea

## 98. Physics-informed neural networks for the prediction of robot dynamics considering motor and external force couplings

- year: 2025 | venue: Frontiers of Information Technology & Electronic Engineering | tier: B | relevance: 8 | citations: 3
- doi: 10.1631/fitee.2500254 | key: `doi:10.1631/fitee.2500254`
- source: Q3

**Abstract**: In recent years, physics-informed neural networks (PINNs) have shown remarkable potential in modeling conservative systems of rigid-body dynamics. However, when applied to practical interaction tasks of manipulators (e.g., part assembly and medical operations), existing PINN frameworks lack effective external force modeling mechanisms, resulting in significantly degraded prediction accuracy in dynamic interaction scenarios. Additionally, because industrial robots (including UR5 and UR10e robots) are generally not equipped with joint torque sensors, obtaining precise dynamics training data remains challenging. To address these issues, this study proposes two enhanced PINNs that integrate motor dynamics and external force modeling. First, two data-driven Jacobian matrix estimation methods are introduced to incorporate external forces: one learns the mapping between end-effector velocity and joint velocity to approximate the Jacobian matrix, while the other first learns the system’s kinematic behavior and then derives the Jacobian matrix through analytical differentiation of the forward kinematics model. Second, current-to-torque mapping is embedded as physical prior knowledge to esta

## 99. Knowledge-graph-enhanced disturbance control in manufacturing systems: a state-of-the-art review

- year: 2025 | venue: International Journal of Computer Integrated Manufacturing | tier: B | relevance: 8 | citations: 3
- doi: 10.1080/0951192x.2025.2509324 | key: `doi:10.1080/0951192x.2025.2509324`
- source: Q3

**Abstract**: In the context of Industry 5.0, intensified competition and dynamic uncertainty have made efficient control essential for ensuring quality, quantity, and timely delivery in discrete manufacturing systems. However, production processes are vulnerable to unpredictable disturbances with complex, interrelated root causes. This paper reviews the use of knowledge graphs in disturbance control within manufacturing systems to support knowledge sharing and reuse. It first classifies manufacturing disturbances based on factory physics, production bottlenecks, and production factors, considering precedence, impact, and root causes. Next, it examines the integration of knowledge graphs with manufacturing systems, including application scenarios, available datasets, modeling approaches, and Smart Question & Answer systems. The current progress in knowledge-graph-driven disturbance control is then explored, and a disturbance control model based on Physics-Informed Neural Networks (PINNs) is proposed. Finally, the paper summarizes existing research and outlines future directions.

## 100. Physics-Informed Surrogates for Temperature Prediction of Multi-Tracks in Laser Powder Bed Fusion

- year: 2025 | venue: arXiv (Cornell University) | tier: B | relevance: 8 | citations: 2
- doi: 10.48550/arxiv.2502.01820 | key: `doi:10.48550/arxiv.2502.01820`
- source: Q3

**Abstract**: Modeling plays a critical role in additive manufacturing (AM), enabling a deeper understanding of underlying processes. Parametric solutions for such models are of great importance, enabling the optimization of production processes and considerable cost reductions. However, the complexity of the problem and diversity of spatio-temporal scales involved in the process pose significant challenges for traditional numerical methods. Surrogate models offer a powerful alternative by accelerating simulations and facilitating real-time monitoring and control. The present study presents an operator learning approach that relies on the deep operator network (DeepONet) and physics-informed neural networks (PINN) to predict the three-dimensional temperature distribution during melting and consolidation in laser powder bed fusion (LPBF). Parametric solutions for both single-track and multi-track scenarios with respect to tool path are obtained. To address the challenges in obtaining parametric solutions for multi-track scenarios using DeepONet architecture, a sequential PINN approach is proposed to efficiently manage the increased training complexity inherent in those scenarios. The accuracy and
