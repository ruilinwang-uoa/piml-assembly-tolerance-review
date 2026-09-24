# 筛查分块 5（记录 201–250 / 共 449）

## 201. Data-Driven and Hybrid Modeling for Metal Fatigue: A Review of Classical Methods, Machine Learning, and Physics-Informed Neural Networks

- year: 2026 | venue: Metals | tier: B | relevance: 6 | citations: 1
- doi: 10.3390/met16050476 | key: `doi:10.3390/met16050476`
- source: Q1

**Abstract**: The prediction of metal fatigue life has evolved from classical empirical approaches to advanced, data-driven computational models. However, traditional methods struggle with large data scatter, complex variable-amplitude loading, and the cost of experimental testing. These limitations are particularly pronounced in additively manufactured (AM) components, which exhibit random porosity and are highly sensitive to process parameters. This review integrates classical fatigue mechanics with modern data-driven methodologies. It evaluates fatigue-life prediction for metallic alloys, welded assemblies, and AM materials. We review classical prediction tools, machine learning (ML) algorithms, deep learning architectures, and physics-informed neural networks (PINNs). ML models capture nonlinear degradation patterns but suffer from limited interpretability (“black-box” behavior) and are unable to extrapolate from small datasets. Embedding governing physical laws into PINNs helps mitigate these limitations. This approach enhances physical consistency, reduces training-data requirements, and strengthens extrapolation capability. In additively manufactured metals, defect location is often a mor

## 202. Physics-Informed Neural Networks for Process Optimization in Laser Powder Bed Fusion of Inconel 718 Superalloy: A Data-Efficient, Physics-Constrained Machine Learning Framework

- year: 2026 | venue: Metals | tier: B | relevance: 6 | citations: 1
- doi: 10.3390/met16050465 | key: `doi:10.3390/met16050465`
- source: Q1

**Abstract**: This study aimed to develop and validate a physics-informed neural network (PINN) framework for data-efficient and physically consistent process optimization in the laser powder bed fusion (LPBF) of Inconel 718 (IN718) superalloy. Laser powder bed fusion (LPBF) is widely adopted for fabricating Inconel 718 (IN718) components in aerospace and energy applications; however, navigating its high-dimensional, nonlinear process parameter space remains a central challenge. High-fidelity finite element simulations are computationally prohibitive for extensive parameter sweeps, whereas purely data-driven machine learning (ML) models are limited by data scarcity and unphysical extrapolation behavior. This study presents a physics-informed neural network (PINN) framework that embeds the transient heat conduction equation and Goldak double-ellipsoidal heat source model directly into the neural network training loss, enforcing thermophysical consistency simultaneously with data fidelity. The model was trained on a curated, multi-source dataset of LPBF IN718 parameter combinations drawn from peer-reviewed experimental studies and validated finite element simulation outputs, spanning the laser pow

## 203. A hybrid framework combining damage mechanics and Physics-Informed neural Networks for damage and failure analysis of additively manufactured lattice structures

- year: 2025 | venue: Materials & Design | tier: B | relevance: 6 | citations: 1
- doi: 10.1016/j.matdes.2025.115059 | key: `doi:10.1016/j.matdes.2025.115059`
- source: Q3

**Abstract**: Additive manufacturing (AM) lattice structures offer high load-bearing capacity with lightweight design, yet their mechanical behavior remains insufficiently understood. This study develops a Continuum Damage Mechanics (CDM)-based framework to describe constitutive response and damage evolution in AM materials, together with its numerical implementation. The model is applied to simulate compression of body-centered cubic with vertical strut (BCCZ) lattices. Results show that the framework effectively captures the behavior of multi-layer lattice structures and accurately estimates compressive modulus and initial ultimate strength. Parametric studies indicate that larger cell size or layer number reduces stiffness and strength, while increasing the number of cells per layer significantly enhances them. To improve predictive efficiency, three machine learning (ML) models are constructed: an artificial neural network (ANN), a weak boundary effects-based physics-informed neural network (PINN), and a physical law-driven PINN. Comparative analysis demonstrates that the two PINN models outperform ANN, as physical knowledge improves prediction accuracy, generalization, and physical consiste

## 204. Structural Health Monitoring of a Satellite Antenna: A Benchmark Between the Modal Method, iFEM Coupled with Modal Strain Expansion, and a Physics-Informed Neural Network

- year: 2025 | venue:  | tier: B | relevance: 6 | citations: 1
- doi: 10.12783/shm2025/37480 | key: `doi:10.12783/shm2025/37480`
- source: Q3

**Abstract**: Shape sensing techniques for real-time deformation reconstruction are an increasingly important topic for Structural Health Monitoring (SHM), particularly in the con- text of digitalisation and digital twins. Artificial intelligence and artificial neural net- works are showing promising results for such tasks. Physics-Informed Neural Networks (PINN) have recently gained interest due to less training data-dependent predictions by incorporating physics laws into the training. To benchmark such a PINN for solving inverse problems in shape sensing, referred to as “iPINN”, this paper presents a study on its performance against the Modal Method (MM) as an established technique on the example of a composite space antenna. Moreover, a combination of the two mainstream methods for shape sensing is tested on the same space structure. Starting from a few strain measurements, the strain field is first expanded using a variation of the MM. Then, displacements are reconstructed using the inverse Finite Element Method (iFEM). This study shows that both the iPINN and the combination of MM and iFEM can produce predictions of deformed shapes, although further investigations are needed to improve the

## 205. A Multimodal Spatiotemporal Fusion Network With Physical-Data-Driven Learning for Additive Manufacturing Fault Diagnosis

- year: 2025 | venue: IEEE Transactions on Instrumentation and Measurement | tier: B | relevance: 6 | citations: 1
- doi: 10.1109/tim.2025.3633352 | key: `doi:10.1109/tim.2025.3633352`
- source: Q3

**Abstract**: In additive manufacturing process, the fusion of multi-source sensing signals and cross-modal interaction are crucial to improve the accuracy of fault diagnosis. Most of the existing methods focus mainly on signal time-series features, but the spatial and time-frequency features were always ignored. In this study, a multi-modal spatio-temporal fusion network (MSTNet) with a three-branch synergetic architecture is proposed. The network integrates acoustic emission (AE) and thermal modalities to achieve fault diagnosis in additive manufacturing. Firstly, a channel-enhanced Mamba (CEMamba) architecture is designed to achieve feature extraction of multi-channel frequency-space joint signals generated by continuous wavelet transform (CWT), gramian angular difference fields (GADF), and recurrence plot. The CEMamba architecture can effectively capture the multi-channel features of AE signals including spatial, time-series, and time-frequency features. Secondly, the bi-directional gated recurrent unit is introduced to capture the dynamic evolution laws of AE signals. Specially, a novel physics-based loss function is designed to constrain the physics informed neural network (PINN) for gener

## 206. Parametric study of plasma swirling flow based on magnetohydrodynamics informed deep learning

- year: 2025 | venue: Physics of Fluids | tier: B | relevance: 6 | citations: 1
- doi: 10.1063/5.0264343 | key: `doi:10.1063/5.0264343`
- source: Q3

**Abstract**: A magnetohydrodynamics (MHD) informed deep learning framework is developed to address the challenges of achieving higher accuracy and faster optimization speeds in physics-informed neural networks (PINNs) for solving multi-parameter MHD problems without labeled data. By integrating hybrid boundary conditions, optimized activation functions, and residual-based adaptive sampling strategy, the proposed framework achieves a global relative error of approximately 2% across a wide parameter range. To address the challenge of training coupled equations in broad parameter regimes, we introduce coefficient normalization for coupled terms that balances loss contributions and prevents equation decoupling. Through this MHD-informed deep learning approach, comprehensive parametric studies and parameter optimizations are conducted to systematically investigate the effects of magnetic field strength, mass flow rate, and geometric configuration on plasma swirling flow dynamics. The proposed methodology leverages the automatic differentiability of PINNs for rapid parameter optimization, achieving up to an order-of-magnitude acceleration in parameter optimization compared to conventional methods lik

## 207. Causality-driven multi-stage physics-informed neural networks for high-fidelity simulation of key variable fields in industrial reactors

- year: 2026 | venue: Complex & Intelligent Systems | tier: B | relevance: 6 | citations: 1
- doi: 10.1007/s40747-026-02262-y | key: `doi:10.1007/s40747-026-02262-y`
- source: Q3

**Abstract**: Industrial reactors, such as smelting kettles and polymerization reactors, form the critical cyber-physical systems (CPS) at the forefront of modern process manufacturing. The accurate simulation of their internal multi-physics fields is fundamental to achieving state observability, intelligent control, and ultimately, smart manufacturing. Constrained by scarce measurable data, a complex reaction mechanism, and strong multi-physics coupling, existing models struggle to accurately simulate the key variable fields. To address this, we propose, for the first time, a causality-driven multi-stage physics-informed neural network (CD-MSPINN). First, we derive theoretical constraints from the partial differential equations and boundary conditions within the reactor, ensuring that the simulation rigorously obeys the physics of industrial reactors and substantially mitigates the data-scarcity problem. Second, we design a causality-driven multi-stage training strategy to decouple the multi-physics fields and propose a causality-guided neural network weight-initialization method that balances industrial first-principles with training efficiency. Validation based on on-site polyester fiber poly

## 208. Towards Sustainable Laser-Based Manufacturing: A Physics-Informed Machine Learning Approach to Keyhole Welding

- year: 2026 | venue: Procedia CIRP | tier: B | relevance: 6 | citations: 1
- doi: 10.1016/j.procir.2026.05.173 | key: `doi:10.1016/j.procir.2026.05.173`
- source: Q3

**Abstract**: Laser-based keyhole welding is widely used in next-generation advanced manufacturing due to its high precision, speed, and efficiency. However, optimizing process parameters such as laser power, speed, and beam profile to achieve target weld geometries typically requires extensive experimental trials or computationally intensive simulations. In this work, we propose a novel Physics-Informed Neural Network (PINN) framework that enables rapid and data-efficient prediction of keyhole weld outcomes, significantly reducing the reliance on both. The approach embeds the governing heat equation and associated boundary and initial conditions directly into the neural network training, allowing the model to infer a physically consistent temperature field. By solving an inverse problem, the PINN is calibrated using limited experimental data, and once trained, it generalizes to different process conditions with negligible computational cost. Key geometric features of the melt pool—such as penetration depth and width—can then be extracted from the predicted temperature field, enabling efficient process optimization. We validate the framework on two industrially relevant scenarios with markedly d

## 209. Multiphysics modeling of hybrid thermo-electrochemical energy storage integration for industrial energy systems: A path to sustainable manufacturing under dynamic policy scenarios

- year: 2026 | venue: AIP Advances | tier: B | relevance: 6 | citations: 1
- doi: 10.1063/5.0322499 | key: `doi:10.1063/5.0322499`
- source: Q3

**Abstract**: Industrial energy systems integrating renewable generation, carbon capture, and hybrid storage are essential for sustainable manufacturing, yet many existing approaches rely on steady-state assumptions and neglect dynamic thermo-electrochemical behavior, safety constraints, and evolving policy incentives. This study proposes a transient multiphysics hybrid energy storage framework that combines a physics-based P2D battery model, thermal energy storage, and supercapacitors within a unified simulation environment. To accelerate prediction and optimization, a hybrid physics–deep learning surrogate strategy using physics-informed neural networks and Transformer-based models is introduced for Carbon Capture, Utilization, and Storage reactor kinetics, renewable forecasting, and multi-scenario operational planning. A dynamic policy scenario engine incorporating carbon pricing, hydrogen incentives, and renewable subsidies is integrated through stochastic optimization to evaluate policy-driven performance. Simulation-based digital-twin validation demonstrates improvements of 38%–52% in storage utilization, a 14.7% reduction in exergy losses, and 9.3%–16.8% lower lifecycle costs, while surro

## 210. Physics-Informed Machine Learning for Accelerated Testing of Roll-to-Roll Printed Sensors

- year: 2022 | venue:  | tier: A | relevance: 6 | citations: 0
- doi: 10.1115/msec2022-85392 | key: `doi:10.1115/msec2022-85392`
- source: Q1

**Abstract**: Abstract Roll-to-roll printing has significantly shortened the time from design to production of sensors and IoT devices, while being cost-effective for mass production. But due to less manufacturing tolerance controls available, properties such as sensor thickness, composition, roughness, etc., cannot be precisely controlled. Since these properties likely affect the sensor behavior, roll-to-roll printed sensors require validation testing before they can be deployed in the field. In this work, we improve the testing of Nitrate sensors that need to be calibrated in a solution of known Nitrate concentration for around 1–2 days. To accelerate this process, we observe the initial behavior of the sensors for a few hours, and use a physics-informed machine learning method to predict their measurements 24 hours in the future, thus saving valuable time and testing resources. Due to the variability in roll-to-roll printing, this prediction task requires models that are robust to changes in properties of the new test sensors. We show that existing methods fail at this task and describe a physics-informed machine learning method that improves the prediction robustness to different testing con

## 211. Constraint-Guided PINNs: A Constrained Optimization Approach

- year: 2025 | venue: Lirias (KU Leuven) | tier: B | relevance: 6 | citations: 0
- doi: — | key: `t:constraintguidedpinnsaconstrainedoptimizationapproach`
- source: Q1

**Abstract**: sponsorship: This research was supported by the DTF-PINN SBO project of Flanders Make, the strategic research centre for the manufacturing industry of Flanders, Belgium and received funding from the Flemish Government (AI Research Program). (DTF-PINN SBO project of Flanders Make, strategic research centre for the manufacturing industry of Flanders, Belgium, Flemish Government (AI Research Program))

## 212. Physics-informed and vision-guided deep learning for robust 3D shape reconstruction of multi-core FBG sensors

- year: 2026 | venue: Optics Express | tier: A | relevance: 6 | citations: 0
- doi: 10.1364/oe.600846 | key: `doi:10.1364/oe.600846`
- source: Q1

**Abstract**: This paper proposes PINN+RMF, a physics-informed and vision-guided framework for robust 3D shape reconstruction using multi-core fiber Bragg grating (MCFBG) sensors. It maps node-wise spectral responses to interpretable local states—including curvature, bending direction, and temperature variation—using calibration parameters as physical priors. A differentiable rotation-minimizing-frame (RMF) layer integrates these states into the global centerline while suppressing torsion-induced orientation drift. Synchronized stereo vision provides coordinate-level supervision, and coarse-to-fine optimization first enforces local physical consistency and then refines global geometry. Experiments on a 1000-mm flexible rod yield a mean point error of 0.93 mm and a mean tip error of 1.62 mm (P95 tip error 5.18 mm, i.e., 0.52% of the rod length). RMF integration substantially reduces frame drift under 3D twisting: in a spatial-twist case, the maximum point-wise error drops from 9.40 mm with Frenet integration to 1.44 mm with RMF. Under a 3-mm tip-error tolerance, PINN+RMF consistently achieves higher success rates than the Frenet-based and end-to-end baselines across the test set. Simulations unde

## 213. Physics-Informed Neural Network Approach for Surface Wave Propagation in Functionally Graded Magnetoelastic Layered Media

- year: 2026 | venue: arXiv (Cornell University) | tier: B | relevance: 6 | citations: 0
- doi: — | key: `t:physicsinformedneuralnetworkapproachforsurfacewavepropagationinfunctionallygrade`
- source: Q1

**Abstract**: This paper investigates propagation of SH-waves in a layered composite structure consisting of a pre-stressed functionally graded magnetoelastic orthotropic layer overlying a pre-stressed functionally graded orthotropic half-space under the influence of gravity. The study introduces a physics-informed neural network (PINN) framework for the dispersion analysis of SH-waves in the considered composite medium. As a benchmark, an analytical solution to the dispersion relation is derived and used to validate accuracy and reliability of the proposed PINN formulation. In the developed PINN model, the phase velocity corresponding to a prescribed wave number is treated as a trainable parameter, enabling the determination of the dispersion relation associated with the nonlinear eigenvalue problem. The Adam optimizer is employed to minimize the loss function during the training process. In addition, the effects of different activation functions and network architectures, including variations in number of hidden layers and neurons, are systematically investigated to study the performance of the proposed framework. Error analysis is carried out using several norms, namely $L_1$, $L_2$, RMSE, re

## 214. Direct and Indirect Physics-Informed Neural Networks for Dirichlet Boundary Control of Semilinear Parabolic Equations: A Conditional Error Analysis

- year: 2026 | venue: arXiv (Cornell University) | tier: B | relevance: 6 | citations: 0
- doi: — | key: `t:directandindirectphysicsinformedneuralnetworksfordirichletboundarycontrolofsemil`
- source: Q1

**Abstract**: We study physics-informed neural networks (PINNs) for the Dirichlet boundary control of a semilinear parabolic equation with Tikhonov regularization. Two approaches are considered. A direct PINN parameterizes the state and control by separate networks and minimizes a penalized form of the tracking objective. An indirect PINN instead represents the state, adjoint, and control by unconstrained networks trained jointly to satisfy the first-order optimality system, with the state-control coupling and the homogeneous adjoint boundary and terminal conditions imposed as soft penalty terms rather than enforced architecturally. For the indirect formulation we develop an error estimation framework that decomposes the total error into approximation, optimization, quadrature, and soft boundary/terminal-constraint contributions. Under standing assumptions on optimal-solution regularity and compatibility, network approximability, uniform Hölder control of the soft-constraint residuals, and a local neighborhood of the reference optimality-system solution, we derive a quantitative linearized stability estimate and a conditional local nonlinear residual-to-error estimate, and construct a computable

## 215. Domain-Validity-Gated Metamorphic Testing of Scientific ML Surrogates

- year: 2026 | venue: arXiv (Cornell University) | tier: B | relevance: 6 | citations: 0
- doi: — | key: `t:domainvaliditygatedmetamorphictestingofscientificmlsurrogates`
- source: Q1

**Abstract**: Scientific machine-learning (SciML) surrogates approximate expensive simulations, but exact expected outputs for arbitrary inputs are unavailable (the oracle problem). Metamorphic testing checks relations across executions, yet a candidate relation is not automatically valid: its preconditions, output mapping, and the numerical floor of the scoring operator determine whether a violation is meaningful. We study how candidate metamorphic relations (MRs) can be screened for domain validity and turned into executable, oracle-free test assets for SciML surrogates. We propose (i) a domain-validity rubric that admits a candidate only when its tolerance dominates the operator's numerical floor and its preconditions hold; (ii) an MR-card executable-asset format recording source cases, transformations, metrics, tolerances, and typed relation-level verdicts; and (iii) a case-study protocol on MeshGraphNets cylinder-flow surrogates, with a claim ledger binding every result to a tracked artifact. On a MeshGraphNets checkpoint, node permutation holds to machine precision, mirror-y is a bounded out-of-distribution stress finding rather than an exact symmetry, and absolute conservation stays defer

## 216. Forecasting Rectangular Pocket Deviations in Birch Plywood for Milling Process Optimization

- year: 2026 | venue: Informatica | tier: B | relevance: 6 | citations: 0
- doi: 10.31449/inf.v50i2.10897 | key: `doi:10.31449/inf.v50i2.10897`
- source: Q1

**Abstract**: We explored the field of predicting and minimizing dimensional deviations when milling rectangular pockets in birch plywood, with the aim of improving the accuracy of manufacturing processes. We examined various machining conditions altering feed rate, depth of cut, and spindle speed and acquired high-resolution 3D scans to quantify pocket-shape deviations against the prescribed tolerances. To enhance the model’s robustness, the empirical dataset was augmented via synthetic data-generation techniques. We then compared several approaches using cross-validation. MLP proved the most accurate. These findings demonstrate the utility of readily available machine-learning algorithms for precise deviation prediction and lay the groundwork for future integration of automated hyperparameter tuning and feature-based process optimization.

## 217. A FEM-Based Surrogate Modelling and Optimization Framework for Physics-Constrained Electromagnetic Coil Design

- year: 2026 | venue: arXiv (Cornell University) | tier: B | relevance: 6 | citations: 0
- doi: 10.48550/arxiv.2608.18903 | key: `doi:10.48550/arxiv.2608.18903`
- source: Q1

**Abstract**: This work evaluates surrogate-assisted optimization of a seven-parameter current-excited coil--core benchmark subject to geometric, manufacturing, and separate core and copper mass constraints. A Python--MPh--COMSOL workflow couples a two-dimensional axisymmetric finite-element method (FEM) model to a Matern 5/2 Gaussian-process (GP) probabilistic surrogate. Here, physics-constrained denotes a design problem evaluated by a governing-equation FEM model and restricted by explicit physical, geometric, manufacturing, and material-allocation constraints; it does not denote a physics-informed GP architecture. Sequential Bayesian optimization (BO) ranks candidates using expected improvement (EI), and every reported incumbent is verified by FEM. Five paired runs show that optimizer ranking depends on the available FEM-evaluation budget: EI--BO improves rapidly at small continuation budgets, COBYLA is stronger at the earliest checkpoint, and BOBYQA attains the highest mean terminal response. A retrospective finite-pool study further finds no robust endpoint advantage of EI over posterior-mean ranking on this smooth response surface. The broader result is that early progress, terminal respon

## 218. A Physics-Informed Neural Network Combined with Domain Generalization Method for Harmonic Reducers Rul Prediction

- year: 2025 | venue:  | tier: B | relevance: 6 | citations: 0
- doi: 10.1109/icrms65480.2025.00042 | key: `doi:10.1109/icrms65480.2025.00042`
- source: Q3

**Abstract**: Harmonic reducers are an important component in industrial robots. Remaining useful life (RUL) prediction of harmonic reducers plays a significant role for the safety and reliability of industrial robots. However, due to the manufacturing deviations, various operational conditions and random degradation processes, the degradation behaviors of different harmonic reducers present significant unit-to-unit variability. While current data-driven methods show low capability in RUL prediction under serious unit-to-unit variability. To deal with this issue, this paper proposes a physicsinformed neural network (PINN) combined with domain generalization method for harmonic reducers RUL prediction. Specifically, the self-attention mechanism is introduced for feature extraction and the maximum mean discrepancy is computed based on the extracted features to quantify the deviation of data distributions among different units. Subsequently, a PINN serves to regularize the mapping from features to RUL. The proposed method was validated based on an accelerated degradation test of industrial robot harmonic reducers. The results demonstrate that the proposed method can provide more accurate RUL predic

## 219. Inverse Parameter Identification of Subsurface Residual Stress in Tractional Sliding Processes Using a Physics-Informed Neural Network

- year: 2025 | venue: Journal of Tribology | tier: B | relevance: 6 | citations: 0
- doi: 10.1115/1.4070741 | key: `doi:10.1115/1.4070741`
- source: Q3

**Abstract**: Abstract Residual stresses (RS) arise in a wide range of manufacturing processes, including additive manufacturing, welding, forming, grinding, and machining. Accurate characterization and prediction of RS are crucial for optimizing functional performance and structural integrity, as tensile stresses reduce fatigue strength while compressive stresses enhance it. Traditional finite element methods provide detailed insights into RS distributions but are computationally expensive for real-time use. To overcome this limitation, we propose a physics-informed neural network (PINN) framework that embeds the Prandtl–Reuss constitutive equations for elastoplasticity directly into the loss function, enabling mesh-free forward simulation of RS distribution and inverse identification of parameters under Hertzian contact loading. The inverse formulation simultaneously reconstructs stress fields and identifies key parameters, namely the effective friction coefficient and normalized load factor, from sparse data, addressing the nonuniqueness and instability of traditional inverse methods. Validation against high-fidelity Runge–Kutta–Gill reference solutions shows that residual stress prediction e

## 220. Effect of Random Interface Properties on Mechanical Properties of Regular Staggered Composites Using Physics Informed Neural Networks

- year: 2025 | venue:  | tier: B | relevance: 6 | citations: 0
- doi: 10.1115/imece-india2025-159775 | key: `doi:10.1115/imece-india2025-159775`
- source: Q3

**Abstract**: Abstract Biological composites such as nacre, bone, and bamboo showcase exceptional mechanical properties despite comprising comparatively weaker constituents. Analyzing the design and structure of these composites through bio-inspiration facilitates the creation of synthetic composites with superior properties. The brick-and-mortar arrangement within nacre represents an optimal design that can serve as inspiration for bio-inspired composites. In brick-and-mortar (BaM) composites randomness could exist in their microstructural building elements and interface properties due to flaws in manufacturing. TSC network model describes the stress transfer in nacre and nacre-like BaM composites, in which hard elastic platelets are assumed to be connected by cohesive tension (CT) and cohesive shear (CS) spring elements. In the present study, regular staggered composites with random interface properties are modeled using the TSC network model and Physics Informed Neural Networks (PINN) is used to study the effect of random interface strengths on the total strain energy of the composites. In this work, physical constraints such as displacement and elongation are taken into consideration while o

## 221. Reconstruction of two-dimensional magnetohydrodynamic and Hall magnetohydrodynamic equilibria in space using physics-informed neural networks

- year: 2025 | venue:  | tier: B | relevance: 6 | citations: 0
- doi: 10.22541/essoar.176366734.43101104/v1 | key: `doi:10.22541/essoar.176366734.43101104/v1`
- source: Q3

**Abstract**: We present a novel data analysis technique based on physics-informed neural networks (PINNs) to reconstruct two-dimensional (2D), magnetohydrodynamic (MHD) and Hall MHD equilibria in a space plasma from in situ spacecraft measurements. Our method incorporates the steady-state MHD or Hall MHD equations—a set of partial differential equations (PDEs) as physical constraints—into a deep learning framework. In contrast to traditional reconstruction techniques relying on explicit spatial integration of the PDEs from spacecraft trajectories, the PINN approach allows us to derive a physically consistent equilibrium by minimizing a composite loss function that includes both prediction errors and PDE residuals. We validate the method through benchmark tests using exact solutions of axially symmetric MHD and Hall MHD equilibria, and further demonstrate its utility through application to an extensively investigated magnetotail reconnection event observed by the Magnetospheric Multiscale mission. The resulting reconstruction reproduces key structural features, including the X-type current sheet geometry and quadrupolar Hall magnetic field, consistent with prior results and numerical simulations

## 222. Optimized Predictive Modeling for Accurate Hardness Profiles in Hot-Rolled Alloy Steel Manufacturing Processes

- year: 2025 | venue: Journal of Advanced Manufacturing Systems | tier: B | relevance: 6 | citations: 0
- doi: 10.1142/s0219686726500344 | key: `doi:10.1142/s0219686726500344`
- source: Q3

**Abstract**: The alloy steel’s Mechanical Properties (MPs) are most influenced by its composition of chemicals and the hot rolling process factors. However, modeling the interactions between these components is extremely difficult due to the rolling process’s complexity and dynamic nature as a nonlinear system. To overcome these challenges, this work introduces an advanced approach for optimizing predictive modeling in Hot-rolled Alloy Steel (HRAS) manufacturing, focusing on enhancing accuracy in hardness profiles and refining process parameters. The proposed approach utilizes the Temporal Dynamic Graph Neural Network (TDGNN), with the main objective of improving the mechanical characteristics of HRAS and enhancing accuracy and reliability. The TDGNN is employed to forecast the mechanical characteristics. The proposed method is implemented and compared with existing techniques on the MATLAB platform, including Physics-informed Neural Networks (PINNs), Deep Neural Networks (DNNs), and Convolutional Neural Networks (CNNs), demonstrating superior performance. The proposed TDGNN approach achieved a prediction accuracy of 97%, significantly outperforming existing methods such as CNN (71%), PINN (79%

## 223. Deep Learning for Process Monitoring and Defect Detection of Laser-Based Powder Bed Fusion of Polymers

- year: 2025 | venue: Preprints.org | tier: B | relevance: 6 | citations: 0
- doi: 10.20944/preprints202510.1423.v1 | key: `doi:10.20944/preprints202510.1423.v1`
- source: Q3

**Abstract**: Additive Manufacturing (AM) is increasingly leveraging Deep Learning (DL) to enhance process monitoring, defect detection, and predictive simulation. This paper synthesizes our results in applying DL to laser-based powder bed fusion of polymers (PBF-LB/P), fo-cusing on four key architectures: convolutional neural networks (CNNs) for real-time spa-tial anomaly detection, recurrent neural networks (RNNs/LSTMs) for capturing temporal dynamics, generative models (GANs and autoencoders) for unsupervised anomaly detec-tion and data augmentation, and physics-informed neural networks (PINNs) for embed-ding governing equations into predictive models. Each approach demonstrates distinct advantages: CNNs deliver high accuracy, LSTMs capture evolving defects, GANs mitigate data scarcity, and PINNs improve generalizability, yet critical limitations persist, includ-ing heavy reliance on labelled datasets, instability of generative models, limited interpret-ability, and lack of scalability for real-time industrial deployment. This paper delineates a roadmap for advancing DL-driven monitoring of the PBF-LB/P process from academic feasibility to robust industrial practice, with particular emphasis 

## 224. Physics-Informed Neural Networks for Accurate Photoresist Thickness Prediction

- year: 2026 | venue:  | tier: B | relevance: 6 | citations: 0
- doi: 10.1109/cstic68613.2026.11537714 | key: `doi:10.1109/cstic68613.2026.11537714`
- source: Q3

**Abstract**: Accurate prediction of photoresist thickness is essential for process control in integrated circuit manufacturing. In this study, we apply physics-informed neural networks (PINNs) to solve the spin-coating thickness equation, combining the strengths of physics-based models and data-driven learning. The proposed PINN model, calibrated with experimental data, effectively captures the relationship between film thickness and rotational speed and demonstrates significantly higher prediction accuracy than the traditional Emslie-Bonner-Peck (EBP) method across multiple photoresist types.

## 225. Physics-Informed Neural Networks for NIR Spectroscopy Analysis of Pharmaceutical Tablet Properties

- year: 2026 | venue: Systems and Control Transactions | tier: B | relevance: 6 | citations: 0
- doi: 10.69997/sct.137896 | key: `doi:10.69997/sct.137896`
- source: Q3

**Abstract**: In pharmaceutical process engineering, accurate prediction of tablet properties is crucial for ensuring product quality, optimizing manufacturing efficiency, and advancing sustainable production practices. This study presents a physics-informed neural network (PINN) framework for predicting the physical properties of pharmaceutical tablets from near-infrared (NIR) spectra. The PINN framework integrates revised Kubelka-Munk theory and physical constraints to ensure physically consistent predictions while requiring less training data than conventional artificial neural networks. Tablets were manufactured using acetaminophen and microcrystalline cellulose formulations with varying compositions and compression settings. The PINN framework successfully predicts critical quality attributes, including tensile strength, porosity, and density. It offers a data-efficient, interpretable solution for pharmaceutical tablet quality control.

## 226. 3D Magnetic Field Reconstruction and Mapping with Physics-Informed Neural Networks

- year: 2026 | venue: arXiv (Cornell University) | tier: B | relevance: 6 | citations: 0
- doi: 10.48550/arxiv.2605.25640 | key: `doi:10.48550/arxiv.2605.25640`
- source: Q3

**Abstract**: Accurate reconstruction of magnetic fields in inaccessible regions is vital for many high-precision experiments in physics. Traditional methods, such as spherical harmonic expansion, often suffer from truncation errors that limit their precision. This study proposes an advanced Physics-Informed Neural Network (PINN) framework for high-precision 3D magnetic field mapping. Unlike conventional data-driven models, the proposed PINN integrates Maxwell's equations directly into the loss function, enforcing divergence-free and curl-free conditions across the entire domain. A key innovation is the inclusion of explicit physics-residual losses at measurement locations, ensuring rigorous physical consistency beyond random collocation sampling. Validation using simulated data achieves a reconstruction accuracy of $10^{-4}$, a tenfold improvement over existing PINN benchmarks. Furthermore, experimental validation using a custom coil assembly demonstrates robust reconstruction with sub-percent relative accuracy, reaching the $10^{-3}$ level under ambient conditions. This AI-driven methodology provides a robust, high-precision solution for field monitoring and measurement in complex experimental

## 227. 3D Magnetic Field Reconstruction and Mapping with Physics-Informed Neural Networks

- year: 2026 | venue: arXiv (Cornell University) | tier: B | relevance: 6 | citations: 0
- doi: — | key: `t:3dmagneticfieldreconstructionandmappingwithphysicsinformedneuralnetworks`
- source: Q3

**Abstract**: Accurate reconstruction of magnetic fields in inaccessible regions is vital for many high-precision experiments in physics. Traditional methods, such as spherical harmonic expansion, often suffer from truncation errors that limit their precision. This study proposes an advanced Physics-Informed Neural Network (PINN) framework for high-precision 3D magnetic field mapping. Unlike conventional data-driven models, the proposed PINN integrates Maxwell's equations directly into the loss function, enforcing divergence-free and curl-free conditions across the entire domain. A key innovation is the inclusion of explicit physics-residual losses at measurement locations, ensuring rigorous physical consistency beyond random collocation sampling. Validation using simulated data achieves a reconstruction accuracy of $10^{-4}$, a tenfold improvement over existing PINN benchmarks. Furthermore, experimental validation using a custom coil assembly demonstrates robust reconstruction with sub-percent relative accuracy, reaching the $10^{-3}$ level under ambient conditions. This AI-driven methodology provides a robust, high-precision solution for field monitoring and measurement in complex experimental

## 228. Learnable Viscosity Modulation in Physics-Informed Neural Networks for Incompressible Flow Reconstruction

- year: 2026 | venue: arXiv (Cornell University) | tier: B | relevance: 6 | citations: 0
- doi: — | key: `t:learnableviscositymodulationinphysicsinformedneuralnetworksforincompressibleflow`
- source: Q3

**Abstract**: Accurately and stably solving the incompressible Navier--Stokes equations with physics-informed neural networks (PINNs) remains challenging, particularly for sparse or noisy observations and for flow regimes in which the local balance among convection, diffusion, and pressure is difficult to capture. To address this issue, we propose a framework, denoted as LVM-PINN, which incorporates a learnable viscosity modulation (LVM) mechanism into the PINN residual. Specifically, the model predicts a spatiotemporal scalar field that is embedded directly into the viscous diffusion term of the momentum equations, thereby enabling adaptive modulation of the local dissipation strength during training. This modification improves optimization stability while enhancing the representation of complex flow structures. The effect of the proposed mechanism is further examined through a controlled ablation setting with an otherwise unchanged network architecture, as well as through comparisons with GRU- and residual-attention-based backbone baselines. Numerical experiments on two-dimensional benchmark problems, including the Kovasznay flow and two manufactured forcing flows, show that the proposed frame

## 229. Learnable Viscosity Modulation in Physics-Informed Neural Networks for Incompressible Flow Reconstruction

- year: 2026 | venue: arXiv (Cornell University) | tier: B | relevance: 6 | citations: 0
- doi: 10.48550/arxiv.2603.27496 | key: `doi:10.48550/arxiv.2603.27496`
- source: Q3

**Abstract**: Accurately and stably solving the incompressible Navier--Stokes equations with physics-informed neural networks (PINNs) remains challenging, particularly for sparse or noisy observations and for flow regimes in which the local balance among convection, diffusion, and pressure is difficult to capture. To address this issue, we propose a framework, denoted as LVM-PINN, which incorporates a learnable viscosity modulation (LVM) mechanism into the PINN residual. Specifically, the model predicts a spatiotemporal scalar field that is embedded directly into the viscous diffusion term of the momentum equations, thereby enabling adaptive modulation of the local dissipation strength during training. This modification improves optimization stability while enhancing the representation of complex flow structures. The effect of the proposed mechanism is further examined through a controlled ablation setting with an otherwise unchanged network architecture, as well as through comparisons with GRU- and residual-attention-based backbone baselines. Numerical experiments on two-dimensional benchmark problems, including the Kovasznay flow and two manufactured forcing flows, show that the proposed frame

## 230. pinn-rk: Runge-Kutta Physics-Informed Neural Networks with time-discrete losses

- year: 2026 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: B | relevance: 6 | citations: 0
- doi: 10.5281/zenodo.21865023 | key: `doi:10.5281/zenodo.21865023`
- source: Q3

**Abstract**: A PyTorch library for solving time-dependent partial differential equations with Runge-Kutta Physics-Informed Neural Networks (RK-PINNs). Instead of collocating the PDE residual at scattered space-time points, pinn-rk partitions the time interval into slabs and builds a time-discrete loss from Runge-Kutta collocation: the network is evaluated at the stage times of a Butcher tableau, the residual is reconstructed in time by barycentric Lagrange interpolation, and the squared residual is integrated over each slab with the Runge-Kutta quadrature weights. Features General Runge-Kutta backend via ButcherTableau, with Gauss-Legendre (order 4, A-stable), Radau IIA (order 3, L-stable) and Lobatto IIIA (trapezoidal, A-stable) two-stage tableaux included and further schemes addable without touching the loss. Time-discrete residual assembled over a TimeMesh of slabs, with degree q-1 projections realised at the collocation nodes. Exact enforcement of homogeneous Dirichlet boundary conditions through a multiplicative ansatz u(x,t) = Φ(x) gθ(x,t), so boundary error never enters the optimisation. Modular elliptic operators behind an EllipticOperator protocol (1D Laplacian provided), with derivati

## 231. pinn-rk: Runge-Kutta Physics-Informed Neural Networks with time-discrete losses

- year: 2026 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: B | relevance: 6 | citations: 0
- doi: 10.5281/zenodo.21860298 | key: `doi:10.5281/zenodo.21860298`
- source: Q3

**Abstract**: A PyTorch library for solving time-dependent partial differential equations with Runge-Kutta Physics-Informed Neural Networks (RK-PINNs). Instead of collocating the PDE residual at scattered space-time points, pinn-rk partitions the time interval into slabs and builds a time-discrete loss from Runge-Kutta collocation: the network is evaluated at the stage times of a Butcher tableau, the residual is reconstructed in time by barycentric Lagrange interpolation, and the squared residual is integrated over each slab with the Runge-Kutta quadrature weights. Features General Runge-Kutta backend via ButcherTableau, with Gauss-Legendre (order 4, A-stable), Radau IIA (order 3, L-stable) and Lobatto IIIA (trapezoidal, A-stable) two-stage tableaux included and further schemes addable without touching the loss. Time-discrete residual assembled over a TimeMesh of slabs, with degree q-1 projections realised at the collocation nodes. Exact enforcement of homogeneous Dirichlet boundary conditions through a multiplicative ansatz u(x,t) = Φ(x) gθ(x,t), so boundary error never enters the optimisation. Modular elliptic operators behind an EllipticOperator protocol (1D Laplacian provided), with derivati

## 232. pinn-rk: Runge-Kutta Physics-Informed Neural Networks with time-discrete losses

- year: 2026 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: B | relevance: 6 | citations: 0
- doi: 10.5281/zenodo.21839392 | key: `doi:10.5281/zenodo.21839392`
- source: Q3

**Abstract**: A PyTorch library for solving time-dependent partial differential equations with Runge-Kutta Physics-Informed Neural Networks (RK-PINNs). Instead of collocating the PDE residual at scattered space-time points, pinn-rk partitions the time interval into slabs and builds a time-discrete loss from Runge-Kutta collocation: the network is evaluated at the stage times of a Butcher tableau, the residual is reconstructed in time by barycentric Lagrange interpolation, and the squared residual is integrated over each slab with the Runge-Kutta quadrature weights. Features General Runge-Kutta backend via ButcherTableau, with Gauss-Legendre (order 4, A-stable), Radau IIA (order 3, L-stable) and Lobatto IIIA (trapezoidal, A-stable) two-stage tableaux included and further schemes addable without touching the loss. Time-discrete residual assembled over a TimeMesh of slabs, with degree q-1 projections realised at the collocation nodes. Exact enforcement of homogeneous Dirichlet boundary conditions through a multiplicative ansatz u(x,t) = Φ(x) gθ(x,t), so boundary error never enters the optimisation. Modular elliptic operators behind an EllipticOperator protocol (1D Laplacian provided), with derivati

## 233. pinn-rk: Runge-Kutta Physics-Informed Neural Networks with time-discrete losses

- year: 2026 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: B | relevance: 6 | citations: 0
- doi: 10.5281/zenodo.21871378 | key: `doi:10.5281/zenodo.21871378`
- source: Q3

**Abstract**: A PyTorch library for solving time-dependent partial differential equations with Runge-Kutta Physics-Informed Neural Networks (RK-PINNs). Instead of collocating the PDE residual at scattered space-time points, pinn-rk partitions the time interval into slabs and builds a time-discrete loss from Runge-Kutta collocation: the network is evaluated at the stage times of a Butcher tableau, the residual is reconstructed in time by barycentric Lagrange interpolation, and the squared residual is integrated over each slab with the Runge-Kutta quadrature weights. Features General Runge-Kutta backend via ButcherTableau, with Gauss-Legendre (order 4, A-stable), Radau IIA (order 3, L-stable) and Lobatto IIIA (trapezoidal, A-stable) two-stage tableaux included and further schemes addable without touching the loss. Time-discrete residual assembled over a TimeMesh of slabs, with degree q-1 projections realised at the collocation nodes. Exact enforcement of homogeneous Dirichlet boundary conditions through a multiplicative ansatz u(x,t) = Φ(x) gθ(x,t), so boundary error never enters the optimisation. Modular elliptic operators behind an EllipticOperator protocol (1D Laplacian provided), with derivati

## 234. pinn-rk: Runge-Kutta Physics-Informed Neural Networks with time-discrete losses

- year: 2026 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: B | relevance: 6 | citations: 0
- doi: 10.5281/zenodo.21850047 | key: `doi:10.5281/zenodo.21850047`
- source: Q3

**Abstract**: A PyTorch library for solving time-dependent partial differential equations with Runge-Kutta Physics-Informed Neural Networks (RK-PINNs). Instead of collocating the PDE residual at scattered space-time points, pinn-rk partitions the time interval into slabs and builds a time-discrete loss from Runge-Kutta collocation: the network is evaluated at the stage times of a Butcher tableau, the residual is reconstructed in time by barycentric Lagrange interpolation, and the squared residual is integrated over each slab with the Runge-Kutta quadrature weights. Features General Runge-Kutta backend via ButcherTableau, with Gauss-Legendre (order 4, A-stable), Radau IIA (order 3, L-stable) and Lobatto IIIA (trapezoidal, A-stable) two-stage tableaux included and further schemes addable without touching the loss. Time-discrete residual assembled over a TimeMesh of slabs, with degree q-1 projections realised at the collocation nodes. Exact enforcement of homogeneous Dirichlet boundary conditions through a multiplicative ansatz u(x,t) = Φ(x) gθ(x,t), so boundary error never enters the optimisation. Modular elliptic operators behind an EllipticOperator protocol (1D Laplacian provided), with derivati

## 235. pinn-rk: Runge-Kutta Physics-Informed Neural Networks with time-discrete losses

- year: 2026 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: B | relevance: 6 | citations: 0
- doi: 10.5281/zenodo.21843920 | key: `doi:10.5281/zenodo.21843920`
- source: Q3

**Abstract**: A PyTorch library for solving time-dependent partial differential equations with Runge-Kutta Physics-Informed Neural Networks (RK-PINNs). Instead of collocating the PDE residual at scattered space-time points, pinn-rk partitions the time interval into slabs and builds a time-discrete loss from Runge-Kutta collocation: the network is evaluated at the stage times of a Butcher tableau, the residual is reconstructed in time by barycentric Lagrange interpolation, and the squared residual is integrated over each slab with the Runge-Kutta quadrature weights. Features General Runge-Kutta backend via ButcherTableau, with Gauss-Legendre (order 4, A-stable), Radau IIA (order 3, L-stable) and Lobatto IIIA (trapezoidal, A-stable) two-stage tableaux included and further schemes addable without touching the loss. Time-discrete residual assembled over a TimeMesh of slabs, with degree q-1 projections realised at the collocation nodes. Exact enforcement of homogeneous Dirichlet boundary conditions through a multiplicative ansatz u(x,t) = Φ(x) gθ(x,t), so boundary error never enters the optimisation. Modular elliptic operators behind an EllipticOperator protocol (1D Laplacian provided), with derivati

## 236. pinn-rk: Runge-Kutta Physics-Informed Neural Networks with time-discrete losses

- year: 2026 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: B | relevance: 6 | citations: 0
- doi: 10.5281/zenodo.21875876 | key: `doi:10.5281/zenodo.21875876`
- source: Q3

**Abstract**: A PyTorch library for solving time-dependent partial differential equations with Runge-Kutta Physics-Informed Neural Networks (RK-PINNs). Instead of collocating the PDE residual at scattered space-time points, pinn-rk partitions the time interval into slabs and builds a time-discrete loss from Runge-Kutta collocation: the network is evaluated at the stage times of a Butcher tableau, the residual is reconstructed in time by barycentric Lagrange interpolation, and the squared residual is integrated over each slab with the Runge-Kutta quadrature weights. Features General Runge-Kutta backend via ButcherTableau, with Gauss-Legendre (order 4, A-stable), Radau IIA (order 3, L-stable) and Lobatto IIIA (trapezoidal, A-stable) two-stage tableaux included and further schemes addable without touching the loss. Time-discrete residual assembled over a TimeMesh of slabs, with degree q-1 projections realised at the collocation nodes. Exact enforcement of homogeneous Dirichlet boundary conditions through a multiplicative ansatz u(x,t) = Φ(x) gθ(x,t), so boundary error never enters the optimisation. Modular elliptic operators behind an EllipticOperator protocol (1D Laplacian provided), with derivati

## 237. pinn-rk: Runge-Kutta Physics-Informed Neural Networks with time-discrete losses

- year: 2026 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: B | relevance: 6 | citations: 0
- doi: 10.5281/zenodo.21839391 | key: `doi:10.5281/zenodo.21839391`
- source: Q3

**Abstract**: A PyTorch library for solving time-dependent partial differential equations with Runge-Kutta Physics-Informed Neural Networks (RK-PINNs). Instead of collocating the PDE residual at scattered space-time points, pinn-rk partitions the time interval into slabs and builds a time-discrete loss from Runge-Kutta collocation: the network is evaluated at the stage times of a Butcher tableau, the residual is reconstructed in time by barycentric Lagrange interpolation, and the squared residual is integrated over each slab with the Runge-Kutta quadrature weights. Features General Runge-Kutta backend via ButcherTableau, with Gauss-Legendre (order 4, A-stable), Radau IIA (order 3, L-stable) and Lobatto IIIA (trapezoidal, A-stable) two-stage tableaux included and further schemes addable without touching the loss. Time-discrete residual assembled over a TimeMesh of slabs, with degree q-1 projections realised at the collocation nodes. Exact enforcement of homogeneous Dirichlet boundary conditions through a multiplicative ansatz u(x,t) = Φ(x) gθ(x,t), so boundary error never enters the optimisation. Modular elliptic operators behind an EllipticOperator protocol (1D Laplacian provided), with derivati

## 238. Multi-Modal Physics-Informed Neural Network for Single-Track Geometry Prediction in Powder-Bed Arc Additive Manufacturing of 316L Stainless Steel

- year: 2026 | venue: Materials | tier: B | relevance: 6 | citations: 0
- doi: 10.3390/ma19163454 | key: `doi:10.3390/ma19163454`
- source: Q3

**Abstract**: This study presents a methodology for predicting the geometric features of single tracks of 316L stainless steel produced by Powder-Bed Arc Additive Manufacturing (PBAAM) from four independent process parameters using a multi-modal Physics-Informed Neural Network (PINN). PBAAM shares the same powder-deposition and layering scheme as Laser Powder Bed Fusion (LPBF) but uses a low-current micro-TIG arc rather than a laser as the heat source. A multi-task PINN architecture was developed that simultaneously predicts five geometric features measured from two imaging modalities (top-view and side-view arc), namely the arc core diameter (Dq), the arc cone angle (αc), the heat-affected zone width (wHAZ), the track core width (dcore) and the areal equivalent track width (wiz), from four input parameters (arc current, traverse speed, work angle and working distance). The model was assessed on a full-factorial training matrix of 36 experiments and on four pure speed extrapolation experiments above the training range. A composite quality score filter classified 23 of the training experiments as stable and 13 as unstable. On the pure validation set, the mean absolute percentage error (MAPE) was 

## 239. DBPnet: Damper Characteristics-Based Bayesian Physics-Informed Neural Network for Wheel Load Estimation

- year: 2026 | venue: arXiv (Cornell University) | tier: B | relevance: 6 | citations: 0
- doi: — | key: `t:dbpnetdampercharacteristicsbasedbayesianphysicsinformedneuralnetworkforwheelload`
- source: Q3

**Abstract**: Advanced driver assistance systems (ADAS) play an important role in modern automotive intelligence, significantly enhancing vehicle safety and stability. The performance of ADAS critically relies on accurate and reliable vehicle state estimation, particularly from vehicle dynamic sensors. Among these signals, wheel load is a key variable for chassis control and safety-critical functions, yet it remains difficult to estimate robustly due to complex suspension geometry, nonlinear dynamics, and measurement noise. To address this issue, we propose DBPnet, a Bayesian physics-informed neural network (PINN) with a physics-aware embedding module inspired by damper characteristics. First, this paper presents a suspension linkage-level modeling (SLLM) approach that constructs a nonlinear instantaneous dynamic model by explicitly considering the complex geometric structure of the suspension. Building upon SLLM, Bayesian inference is integrated into the PINN to effectively cope with noise and uncertainty in the vehicle chassis system, thereby improving the model's robustness. Then, a physics-informed loss function is employed to ensure consistency with fundamental physical principles, while th

## 240. Direct and Indirect Physics-Informed Neural Networks for Dirichlet Boundary Control of Semilinear Parabolic Equations: A Conditional Error Analysis

- year: 2026 | venue: arXiv (Cornell University) | tier: B | relevance: 6 | citations: 0
- doi: 10.48550/arxiv.2609.14269 | key: `doi:10.48550/arxiv.2609.14269`
- source: Q3

**Abstract**: We study physics-informed neural networks (PINNs) for the Dirichlet boundary control of a semilinear parabolic equation with Tikhonov regularization. Two approaches are considered. A direct PINN parameterizes the state and control by separate networks and minimizes a penalized form of the tracking objective. An indirect PINN instead represents the state, adjoint, and control by unconstrained networks trained jointly to satisfy the first-order optimality system, with the state-control coupling and the homogeneous adjoint boundary and terminal conditions imposed as soft penalty terms rather than enforced architecturally. For the indirect formulation we develop an error estimation framework that decomposes the total error into approximation, optimization, quadrature, and soft boundary/terminal-constraint contributions. Under standing assumptions on optimal-solution regularity and compatibility, network approximability, uniform Hölder control of the soft-constraint residuals, and a local neighborhood of the reference optimality-system solution, we derive a quantitative linearized stability estimate and a conditional local nonlinear residual-to-error estimate, and construct a computable

## 241. Strategic Integration of Mechanistic, Hybrid, and AI Models in Biopharmaceutical Manufacturing

- year: 2026 | venue:  | tier: B | relevance: 6 | citations: 0
- doi: 10.1021/bk-2026-1529.ch007 | key: `doi:10.1021/bk-2026-1529.ch007`
- source: Q3

**Abstract**: Abstract The integration of mechanistic, hybrid, and AI-driven modeling methods has great potential to change biopharmaceutical manufacturing. This combination aids in gaining a better understanding of processes, predictive control, and successful lifecycle management. In this chapter a case driven framework is presented for selection and use of modeling methods in both upstream and downstream operations. This involves optimization and modeling of bioreactors and chromatography steps. In upstream operations, mechanistic models provide foundational insights into cell growth and metabolic dynamics, while hybrid approaches and Physics-Informed Neural Networks (PINNs) are increasingly leveraged to predict critical quality attributes and optimize process performance, especially in data-limited environments. In downstream processing, mechanistic and hybrid models are useful for the characterization of the resin, mass transfer analysis, impurity clearance and process design in chromatography steps such as Protein A, ion-exchange, and hydrophobic interaction chromatography. The models can be used for effective process development, to aid tech transfer, and to manage deviations by integrati

## 242. PiGRAND: Physics-informed Graph Neural Diffusion for Intelligent Additive Manufacturing

- year: 2026 | venue: arXiv (Cornell University) | tier: B | relevance: 6 | citations: 0
- doi: — | key: `t:pigrandphysicsinformedgraphneuraldiffusionforintelligentadditivemanufacturing`
- source: Q3

**Abstract**: A comprehensive understanding of heat transport is essential for optimizing various mechanical and engineering applications, including 3D printing. Recent advances in machine learning, combined with physics-based models, have enabled a powerful fusion of numerical methods and data-driven algorithms. This progress is driven by the availability of limited sensor data in various engineering and scientific domains, where the cost of data collection and the inaccessibility of certain measurements are high. To this end, we present PiGRAND, a Physics-informed graph neural diffusion framework. In order to reduce the computational complexity of graph learning, an efficient graph construction procedure was developed. Our approach is inspired by the explicit Euler and implicit Crank-Nicolson methods for modeling continuous heat transport, leveraging sub-learning models to secure the accurate diffusion across graph nodes. To enhance computational performance, our approach is combined with efficient transfer learning. We evaluate PiGRAND on thermal images from 3D printing, demonstrating significant improvements in prediction accuracy and computational performance compared to traditional graph n

## 243. Generative Design and AI Driven Topology Optimization for Sustainable Aerospace Structures

- year: 2026 | venue:  | tier: B | relevance: 6 | citations: 0
- doi: 10.5281/zenodo.18814259 | key: `doi:10.5281/zenodo.18814259`
- source: Q3

**Abstract**: The aerospace industry is undergoing a structural revolution driven by the integration of Artificial Intelligence (AI) and Additive Manufacturing (AM). Traditional subtractive manufacturing often results in "over-engineered" components that carry unnecessary weight. This paper explores the application of Generative Design algorithms and Topology Optimization (TO) to radically reduce the mass of load-bearing aircraft brackets and engine mounts. By utilizing Physics-Informed Neural Networks (PINNs), we demonstrate a 45% reduction in component weight while maintaining the structural integrity and fatigue life required by 2026 FAA safety standards. The study further analyzes the transition from "Design-for-Manufacturing" to "Design-for-Performance," highlighting how AI can synthesize complex bio-mimetic geometries that were previously impossible to produce. Our results provide a framework for the next generation of "Ultra-Light" aircraft, providing a technical path to carbon-neutral aviation.

## 244. Generative Design and AI Driven Topology Optimization for Sustainable Aerospace Structures

- year: 2026 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: B | relevance: 6 | citations: 0
- doi: 10.5281/zenodo.18814260 | key: `doi:10.5281/zenodo.18814260`
- source: Q3

**Abstract**: The aerospace industry is undergoing a structural revolution driven by the integration of Artificial Intelligence (AI) and Additive Manufacturing (AM). Traditional subtractive manufacturing often results in "over-engineered" components that carry unnecessary weight. This paper explores the application of Generative Design algorithms and Topology Optimization (TO) to radically reduce the mass of load-bearing aircraft brackets and engine mounts. By utilizing Physics-Informed Neural Networks (PINNs), we demonstrate a 45% reduction in component weight while maintaining the structural integrity and fatigue life required by 2026 FAA safety standards. The study further analyzes the transition from "Design-for-Manufacturing" to "Design-for-Performance," highlighting how AI can synthesize complex bio-mimetic geometries that were previously impossible to produce. Our results provide a framework for the next generation of "Ultra-Light" aircraft, providing a technical path to carbon-neutral aviation.

## 245. Deep Learning Driven 2D/3D Image Analysis Techniques for Surface Characterisation and Defect Detection in Additive Manufacturing: An Overview

- year: 2026 | venue: Recent Advances in Computer Science and Communications | tier: B | relevance: 6 | citations: 0
- doi: 10.2174/0126662558442163260226071649 | key: `doi:10.2174/0126662558442163260226071649`
- source: Q3

**Abstract**: Introduction: Deep learning has rapidly transformed Additive Manufacturing (AM) quality control by enabling advanced 2D and 3D image analysis for defect detection and surface characterisation. Current approaches utilising YOLO, U-Net, and 3D CNNs have demonstrated significant improvements. However, critical research gaps remain, particularly in data scarcity, cross-domain generalisation, and integration with legacy manufacturing systems. This review bridges these gaps by comprehensively synthesising recent advances (2020-2025) and highlighting emerging solutions through multi-modal sensor fusion and physics-informed neural networks. Methods: This systematic review analysed over 200 peer-reviewed publications from major scientific databases (Scopus, IEEE Xplore, Elsevier, SpringerLink). Selection criteria focused on empirical AM studies with quantitative performance metrics. Data extraction encompassed imaging modalities, neural architectures, datasets (VISION, EOSTATE PowderBed with over 1.2 million images, NEU-CLS, Defect Spectrum), evaluation protocols (IoU, mAP, F1 score), and real-time deployment strategies. Results: State-of-the-art 2D detection models (GDCP-YOLO, YOLOv8-enhan

## 246. Physics-informed machine learning of melt pool dynamics in metal additive manufacturing

- year: 2026 | venue: Rutgers University Community Repository (Rutgers University) | tier: B | relevance: 6 | citations: 0
- doi: 10.7282/t3-rgpt-5136 | key: `doi:10.7282/t3-rgpt-5136`
- source: Q3

**Abstract**: Metal additive manufacturing, such as Laser-Based Powder Bed Fusion (L-PBF) and Directed Energy Deposition (DED), presents an enabling opportunity for creating complex metal parts with design freedom. The unique thermal cycle of rapid heating, fast solidification, and melt-back during metal AM may cause very complex melt pool dynamics. The complex kinetic process and thermal history may lead to various quality issues of the printed parts. Therefore, the understanding and prognosis of metal pool dynamics remains the central intractable problem for printing high-quality metal parts or new alloys. Compared with physics-based simulation models, machine learning has the potential to handle high-dimensional and massive process data for efficient surrogate modeling and decision-making. However, pure data-driven machine learning models are black-box, inherently computation-intensive, and storage-intensive. A deep knowledge gap exists between machine learning and physics-based modeling in predicting melt pool dynamics.To address these limitations, this dissertation has developed a Physics-Informed Machine Learning (PIML) framework that integrates governing physical laws and small datasets f

## 247. Optimization of interfacial bonding of date palm seed reinforced polymer using machine learning and weibull reliability analysis: a review

- year: 2026 | venue: SVU-International Journal of Engineering Sciences and Applications | tier: B | relevance: 6 | citations: 0
- doi: 10.21608/svusrc.2026.484911.1331 | key: `doi:10.21608/svusrc.2026.484911.1331`
- source: Q3

**Abstract**: The need to maximize benefits from date palm seeds (DPS) as a sustainable natural fibre led to a search for advanced solutions to optimize the interfacial bonding between DPS and the polymer matrix, leading to enhanced overall properties. Weibull analysis is an effective tool to evaluate the reliability of materials and describe the dispersion of fibres within the matrix, while machine learning (ML) leverages these complex patterns to predict the performance of the final composite. Despite the advantages of current research, there is a lack of integration between ML and the Weibull distribution to improve composite reliability. This review aims to present how the mechanical performance of DPS-reinforced polymer composites could be optimized by integrating ML and Weibull statistical analysis to overcome weak interfacial bonding. Despite the efficiency of ML in forecasting material behavior, a significant translational disparity persists between data-driven models and empirical physical reality. To mitigate this limitation, physics-informed neural networks (PINNs) emerge as a robust paradigm, systematically integrating fundamental governing physical laws into the computational framew

## 248. A Physics-Informed Surrogate Architecture for Real-Time Thermostructural Limit Protection in Regeneratively Cooled Scramjet Structures: Formulation, a Verified Reduced-Order Demonstration, and a Digital-Twin Roadmap

- year: 2026 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: B | relevance: 6 | citations: 0
- doi: 10.5281/zenodo.21788996 | key: `doi:10.5281/zenodo.21788996`
- source: Q3

**Abstract**: Scramjet combustors survive by regenerative cooling, and sizing that cooling requires conjugate heat transfer (CHT) analysis far too slow to run inside a flight control loop. We formulate a physics-informed surrogate architecture for real-time thermostructural limit protection and evaluate it on a reduced conjugate heat transfer problem verified end to end -- against an exact nonlinear steady solution and by the method of manufactured solutions (observed orders 2.00 in space, 0.95 in time). A parametric physics-informed neural network with a hard initial condition and non-dimensionalised residuals reproduces the transient field to 10.5 K RMSE and peak von Mises stress to 2.7% over 40 held-out operating points, answering a constraint query in 2.29 ms. A six-way ablation at fixed architecture and budget shows the residual substitutes for data: with four reference solutions it improves stress error 3.7x, and with none it reaches 2.86%, beating a supervised model given four. With 24 solutions, however, supervised training is twice as accurate in-envelope -- we report this rather than omit it. Because collocation is free, widening its sampling cuts out-of-envelope stress error from 7.05

## 249. A Physics-Informed Conditional GAN Framework with Multi-Objective Optimization for Automated Design of Acoustic Metamaterials

- year: 2026 | venue: Journal of Physics Conference Series | tier: B | relevance: 6 | citations: 0
- doi: 10.1088/1742-6596/3196/1/012032 | key: `doi:10.1088/1742-6596/3196/1/012032`
- source: Q3

**Abstract**: Abstract Owing to their extraordinary ability to manipulate acoustic and electromagnetic waves, the field of metamaterials attracts considerable attention in terms of their potential applications for cloaking devices, sound isolation, photonic crystals, and more. Nonetheless, designing optimum metamaterial unit cell structures is still a non-trivial process that typically requires time-intensive simulations, manual adjustments and knowledge in the domain. A new framework that combines Generative Adversarial Networks (GANs) with Physics-Informed Neural Networks (PINNs) and multi-objective optimization capabilities to enable the automated design of acoustic metamaterial unit cells is presented. In particular, developing a Conditional GAN (cGAN) architecture in which the generator is conditioned on target acoustic properties (e.g., bandgap frequency and width) and learns to generate corresponding 2D unit cell geometries. To ensure the physical feasibility of generated designs, a physics-informed loss is included based on governing wave equations. In addition, a multi-objective loss function is used to trade-off between different design objectives, i.e., balance between property accura

## 250. AI-Driven Metal Additive Manufacturing: A Critical Review of Techniques, Challenges, and Emerging Opportunities

- year: 2026 | venue: Journal of Manufacturing Engineering | tier: B | relevance: 6 | citations: 0
- doi: 10.37255/jme.v21i2pp064-076 | key: `doi:10.37255/jme.v21i2pp064-076`
- source: Q3

**Abstract**: Metal additive manufacturing (MAM) technology offers significant opportunities for the production of complex metal components, including greater design freedom and improved material utilization. However, issues such as process instability, defect formation, complex microstructure, and poor repeatability pose significant challenges to the realization of industrial applications of the MAM technology. In recent years, the implementation of AI and ML methods has been considered as one of the possible ways to address these problems. The goal of this paper is to provide a comprehensive overview of recent developments in metal additive manufacturing technology enabled by artificial intelligence methods, including process parameter optimization, defect detection, microstructure prediction, and material qualification. Developments in deep learning, Bayesian optimization, physics-guided machine learning, and related areas will be considered in detail, along with their potential contributions to advancing process-structure-property relationships. Also, the emergence of new trends in autonomous manufacturing systems, generative design, digital twins, and others will be discussed to demonstrate
