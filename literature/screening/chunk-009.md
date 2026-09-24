# 筛查分块 9（记录 401–449 / 共 449）

## 401. Physics-Informed Graph Neural Network for Predicting Pressure Ulcer Development in Bedridden Patients Using Body Position Sensor Data and Skin Perfusion Measurements

- year: 2026 | venue: Journal of Artificial Intelligence for Healthcare Systems | tier: A | relevance: 3 | citations: 0
- doi: 10.68159/q185736155 | key: `doi:10.68159/q185736155`
- source: Q1

**Abstract**: Pressure ulcers are a persistent issue in bedridden patients, especially in intensive care, rehabilitation, and long-term care, leading to pain, infection, and extended hospital stays.Current risk assessments rely on intermittent scoring and clinical judgment, failing to account for continuous changes in body posture, tissue loading, and mechanical tolerance.This conceptual framework proposes a physics-informed graph neural network to predict pressure ulcer risk by integrating data from body position sensors, local tissue loading, and skin perfusion measurements into a dynamic, personalized model.The model represents the body as a graph, with nodes representing pressure-prone areas and edges indicating anatomical and mechanical connections.Tissue stress, perfusion data, and posture features are processed through network layers constrained by soft-tissue mechanics.By encoding the relationship between external forces, internal tissue deformation, ischemia, and damage, the framework allows risk propagation across adjacent anatomical regions.This approach offers a path for continuous, personalized pressure ulcer risk monitoring, laying the foundation for clinical validation and sensor 

## 402. Neuromorphic Parameter Estimation for Power Converter Health Monitoring Using Spiking Neural Networks

- year: 2026 | venue:  | tier: A | relevance: 3 | citations: 0
- doi: 10.1145/3822454.3822481 | key: `doi:10.1145/3822454.3822481`
- source: Q1

**Abstract**: Always-on converter health monitoring demands sub-mW edge inference, a regime inaccessible to GPU-based physics-informed neural networks. This work separates spiking temporal processing from physics enforcement: a three-layer leaky integrate-and-fire SNN estimates passive component parameters while a differentiable ODE solver provides physics-consistent training by decoupling the ODE physics loss from the unrolled spiking loop. On an EMI-corrupted synchronous buck converter benchmark, the SNN reduces lumped resistance error from \(25.8\%\) to \(10.2\%\) versus a feedforward baseline, within the \(\pm 10\%\) manufacturing tolerance of passive components, at a projected ∼ 270 × energy reduction on neuromorphic hardware. Persistent membrane states further enable degradation tracking and event-driven fault detection via a + 5.5 percentage-point spike-rate jump at abrupt faults. With \(93\%\) spike sparsity, the architecture is suited for always-on deployment on Intel Loihi 2 or BrainChip Akida.

## 403. Neuromorphic Parameter Estimation for Power Converter Health Monitoring Using Spiking Neural Networks

- year: 2026 | venue: arXiv (Cornell University) | tier: A | relevance: 3 | citations: 0
- doi: 10.48550/arxiv.2604.15714 | key: `doi:10.48550/arxiv.2604.15714`
- source: Q1

**Abstract**: Always-on converter health monitoring demands sub-mW edge inference, a regime inaccessible to GPU-based physics-informed neural networks. This work separates spiking temporal processing from physics enforcement: a three-layer leaky integrate-and-fire SNN estimates passive component parameters while a differentiable ODE solver provides physics-consistent training by decoupling the ODE physics loss from the unrolled spiking loop. On an EMI-corrupted synchronous buck converter benchmark, the SNN reduces lumped resistance error from $25.8\%$ to $10.2\%$ versus a feedforward baseline, within the $\pm 10\%$ manufacturing tolerance of passive components, at a projected ${\sim}270\times$ energy reduction on neuromorphic hardware. Persistent membrane states further enable degradation tracking and event-driven fault detection via a $+5.5$ percentage-point spike-rate jump at abrupt faults. With $93\%$ spike sparsity, the architecture is suited for always-on deployment on Intel Loihi 2 or BrainChip Akida.

## 404. AI-ENABLED DESIGN AND OPTIMIZATION OF AEROSPACE ELECTRIC MOTORS: A TASK-ORIENTED REVIEW

- year: 2026 | venue: Journal of Computer Science and Electrical Engineering | tier: A | relevance: 3 | citations: 0
- doi: 10.61784/jcsee3135 | key: `doi:10.61784/jcsee3135`
- source: Q1

**Abstract**: Artificial intelligence (AI) becomes an effective tool in electric motor design. It can speed up design updates, improve optimization in complex conditions, and support physical modeling. However, most existing review papers discuss AI in motor design in a general way. These studies usually do not focus on the special needs of aerospace systems. This paper presents a task-based review of AI methods for aerospace electric motor design under extreme constraints which mainly covers data-efficient learning, surrogate models, multi-objective optimization, constraint-aware optimization, and physics-informed methods. These methods help designers deal with difficult trade-offs among power density, thermal behavior, mechanical strength, and fault tolerance, even when training data are limited. This paper also discusses the main problems in current studies. For example, many methods still lack validation under real flight conditions. In addition, this paper points out several future directions, such as the use of digital twins and AI workflows that can support certification. This review can provide a clear reference for researchers and engineers who apply AI to next-generation aerospace elec

## 405. Multi-robot formation control with nonholonomic motion constraints based on virtual leader strategy in complex environments

- year: 2026 | venue:  | tier: A | relevance: 3 | citations: 0
- doi: 10.1117/12.3117220 | key: `doi:10.1117/12.3117220`
- source: Q1

**Abstract**: The advantage of multi-robot systems over single robots lies in their stronger fault tolerance and flexibility in complex environments. This paper proposes a distributed framework for multi-robot formation control in environments with and without obstacles. In obstacle-free environments, robots maintain a predefined formation and relative pose. When obstacles prevent the original formation from passing, the robot team adaptively changes its formation and relative pose to navigate through the environment. In this framework, each robot can obtain its own and its neighbors’ global coordinates, as well as surrounding obstacle information, requiring only limited neighbor communication. This information is used to compute pose differences and determine command velocities. The framework consists of two modules. First, a Physics-Informed Neural Network (PINN) is used to learn the robot’s kinematic model, and negative feedback control is applied to adjust the command velocity for reaching target points. Second, a distributed leader–follower formation control strategy is adopted. In obstacle-free environments, a virtual leader is created to generate target points for followers to maintain fo

## 406. Machine-Learning Assisted Prediction of Multimode Nonlinear Coupling and Inverse Structural Design of Ultrafast Lasers

- year: 2025 | venue:  | tier: A | relevance: 3 | citations: 0
- doi: 10.1109/iceace67491.2025.11439775 | key: `doi:10.1109/iceace67491.2025.11439775`
- source: Q4

**Abstract**: Ultrafast lasers operating in the multimode regime exhibit rich spatiotemporal dynamics driven by dispersion, gain saturation, and Kerr-mediated intermodal coupling. Predicting these dynamics and, conversely, synthesizing cavity structures that realize target pulse properties remain challenging due to high-dimensional, stiff, and nonconvex physics. We propose a physics-guided machinelearning framework that learns forward maps from cavity parameters to multimode pulse manifolds and performs inverse structural design via differentiable photonics and Bayesian global search. A hybrid digital twin integrates a splitstep, vector, multimode propagation solver with operatorlearning surrogates to accelerate exploration while preserving physical invariants. We validate on bulk and fiber platforms with programmable dispersion/loss and intracavity spatial filters, demonstrating accurate prediction of cross-phase-modulation-driven energy exchange, stable spatiotemporal mode locking, and rapid synthesis of cavity layouts achieving sub-100-fs pulses with specified M2and energy. Robustness is assessed under pump noise, thermal drift, and fabrication tolerances with calibrated uncertainty quantific

## 407. Physics-Guided Physical-Coordinate Center Detection for Measured Radar Point Targets Under Ground Clutter

- year: 2026 | venue: Remote Sensing | tier: A | relevance: 3 | citations: 0
- doi: 10.3390/rs18132204 | key: `doi:10.3390/rs18132204`
- source: Q4

**Abstract**: Measured radar point-target detection under ground clutter is difficult because weak target echoes often compete with clutter peaks, and image-space detections do not directly represent physical range-Doppler coordinates. This paper proposes a waveform- and physics-guided center detector (WPG-Center) for measured radar maps. The method reformulates detection as continuous physical-coordinate center localization, constructs a four-channel clutter-aware range-Doppler (RD) representation, uses an anisotropic backbone with range-clutter response modulation, and supervises the center heatmap with waveform-resolution-aware Gaussian targets. Conditional physical-prior decoding is used as a targeted candidate reranking step for low-bandwidth, near-zero-Doppler cases. Experiments are conducted on the measured LSS-Ku-1.0 dataset using a strict blocked 5-fold linear frequency-modulated (LFM) protocol with physical localization tolerances and decoded-center detection metrics. WPG-Center achieves a probability of detection (Pd) of 0.850±0.101 and a range root-mean-square error (RMSE) of 18.16±12.19 m, giving the best average decoded-center detection probability and range accuracy among the comp

## 408. Grain-Boundary-Activity Correlation for Electrocatalytic Oxygen Evolution in High-Entropy Alloys

- year: 2023 | venue: PRX Energy | tier: A | relevance: 2 | citations: 17
- doi: 10.1103/prxenergy.2.033011 | key: `doi:10.1103/prxenergy.2.033011`
- source: Q1

**Abstract**: High-entropy alloys (HEAs) have emerged as a promising platform for designing efficient electrocatalysts; however, the relationship between their structure and activity has not yet been clearly established.In particular, the influences of crystalline defects, such as grain boundaries (GBs), on activity and stability remain unclear.This study demonstrates the impacts of GBs on the oxygen evolution reaction (OER) activity in the FeCoCrNi HEA.We observe a logarithmic dependence of OER performance on mean grain size, spanning 3 orders of magnitude, as measured by evaluators like overpotential and Tafel slope.Spatially resolved microscopic imaging of activated samples indicates that the GBs undergo substantial reconstructions and they are enriched with the in situ formed metal oxides (M-O, M = Fe, Co, Ni) and the amorphous regions.By comparing with simple metals, we reveal a "high-entropy effect," i.e., HEAs exhibit greater tolerance towards the grain refinements, which explains their activity both in bulk samples and nanoparticles.These findings offer physics-informed strategies for developing HEA electrocatalysis.

## 409. Connecting Structural Characteristics and Material Properties in Phase-Separating Polymer Solutions: Phase-Field Modeling and Physics-Informed Neural Networks

- year: 2023 | venue: Polymers | tier: A | relevance: 2 | citations: 7
- doi: 10.3390/polym15244711 | key: `doi:10.3390/polym15244711`
- source: Q1

**Abstract**: The formed morphology during phase separation is crucial for determining the properties of the resulting product, e.g., a functional membrane. However, an accurate morphology prediction is challenging due to the inherent complexity of molecular interactions. In this study, the phase separation of a two-dimensional model polymer solution is investigated. The spinodal decomposition during the formation of polymer-rich domains is described by the Cahn-Hilliard equation incorporating the Flory-Huggins free energy description between the polymer and solvent. We circumvent the heavy burden of precise morphology prediction through two aspects. First, we systematically analyze the degree of impact of the parameters (initial polymer volume fraction, polymer mobility, degree of polymerization, surface tension parameter, and Flory-Huggins interaction parameter) in a phase-separating system on morphological evolution characterized by geometrical fingerprints to determine the most influential factor. The sensitivity analysis provides an estimate for the error tolerance of each parameter in determining the transition time, the spinodal decomposition length, and the domain growth rate. Secondly, 

## 410. Multiscale Modeling of the Mechanical Response of Silicon Carbide Composite Within the Accelerated Fuel Qualification Framework

- year: 2025 | venue: Nuclear Technology | tier: A | relevance: 2 | citations: 2
- doi: 10.1080/00295450.2025.2480978 | key: `doi:10.1080/00295450.2025.2480978`
- source: Q1

**Abstract**: The accelerated fuel qualification (AFQ) framework has been used for the initial development of multiscale modeling of silicon carbide (SiC) fiber reinforced composite (SiC-SiC). The AFQ framework provides a methodology to leverage physics-informed multiscale modeling along with a reduced set of empirical test data to reduce the time and cost of licensing and qualification of new nuclear fuel systems while maintaining the overall nuclear power plant safety case. SiC-SiC is being proposed for in-core applications, most notably fuel cladding, for current and next-generation nuclear reactors because of its high temperature stability, irradiation tolerance, and ability to withstand many accident conditions. As these composites exhibit multiscale architectures and complex microstructure-based fracture mechanics, it is an appealing use case for the AFQ methodology. While the end goal of this work is a single multiscale model that can be used for predictive in-core performance, current focus is on the individual various length scale models. Four individual models have been initially developed from microscale to engineering system level to capture key physics-based effects across different

## 411. PLS-Net: A Physics-Embedded LSTM-Siamese Network for Early RUL Prediction in Lithium-Ion Batteries with Explainable AI Analysis

- year: 2026 | venue: Journal of the Electrochemical Society | tier: A | relevance: 2 | citations: 2
- doi: 10.1149/1945-7111/ae489b | key: `doi:10.1149/1945-7111/ae489b`
- source: S2-Q1

**Abstract**: 
 The increasing adoption of electric vehicles intensifies the need for precise prognostics of lithium-ion battery capacity and end-of-life, but the task remains constrained due to aging mechanisms over time. To overcome these issues, this study presents PLS-Net, Physics-informed LSTM Siamese Network that integrates domain knowledge with deep learning. As part of the feature extraction process, battery deterioration signals are analyzed to derive multivariate higher-order attributes and uses physics-based elements like resistance and capacity fading which serves as an input to PLS-Net. A Siamese architecture with cross-pair learning allows the network to simulate both self and cross battery interactions, increasing tolerance to data deficits. Unlike conventional models PLS-Net leverages both physical cognition and relational learning to make more accurate predictions. Experimental analysis on the NASA battery dataset shows that PLS-Net with limited historical samples starting from the 50th cycle of Battery B5, achieving a MSE of 3.73 X 10^{-5}, MAE of 0.0036, MAPE of 0.0025, and an R2 score of 99.78%, validating PLS-Net as scalable and reliable framework for predictive battery mana

## 412. Pipeline Defect Detection and Fine-Scale Reconstruction From 3-D MFL Signal Analysis Using Object Detection and Physics-Constrained Machine Learning

- year: 2022 | venue:  | tier: A | relevance: 2 | citations: 1
- doi: 10.1115/ipc2022-87313 | key: `doi:10.1115/ipc2022-87313`
- source: Q1

**Abstract**: Abstract Sustainable operation of pipeline networks for oil and gas transportation requires diagnostics capable of both detection and characterization of pipeline defects in particular corrosion defects. Current defect analysis techniques can identify and characterize the geometric features of metal loss defects or defect clusters such as peak depth, length, and width with limited accuracy. Probabilistic data driven models have also shown an ability to predict error bounds for individual defect characteristics as opposed to overall defect tolerance. The prediction accuracy of the health of a pipeline with metal loss defects such as corrosion can be improved with additional detail in the corrosion surface profile as this affects the burst pressure. This will enable operators to apply more accurate corrosion growth models and simulations that can forecast the reduction in pipeline capacity and facilitate more targeted diagnostic and mitigation plans. To this end, a data-driven workflow is proposed to automate the detection, classification, and surface prediction of external corrosion defects. This combines experimental MFL data and validated MFL simulations and leverages both image-b

## 413. Vascular-Aware Multimodal MR–PET Reconstruction for Early Stroke Detection: A Physics-Informed, Topology-Preserving, Adversarial Super-Resolution Framework

- year: 2025 | venue: Applied Sciences | tier: A | relevance: 2 | citations: 1
- doi: 10.3390/app152212186 | key: `doi:10.3390/app152212186`
- source: Q1

**Abstract**: Rapid and reliable identification of large vessel occlusions and critical stenoses is essential for guiding treatment in acute ischemic stroke. Conventional MR angiography (MRA) and PET protocols are constrained by trade-offs among acquisition time, spatial resolution, and motion tolerance. A multimodal MR–PET angiography reconstruction framework is introduced that integrates joint Hankel-structured sparsity with topology-preserving multitask learning to overcome these limitations. High-resolution time-of-flight MRA and perfusion-sensitive PET volumes are reconstructed from undersampled data using a cross-modal low-rank Hankel prior coupled to a super-resolution generator optimized with adversarial, perceptual, and pixel-wise losses. Vesselness filtering and centerline continuity terms enforce preservation of fine arterial topology, while learned k-space and sinogram sampling concentrate measurements within vascular territories. Motion correction, blind deblurring, and modality-specific denoising are embedded to improve robustness under clinical conditions. A multitask output head estimates occlusion probability, stenosis localization, and collateral flow, with hypoperfusion mappin

## 414. A Physics-Driven Digital Workflow for Damage Tolerance Assessment of Turbine Discs

- year: 2026 | venue: Digital engineering. | tier: A | relevance: 2 | citations: 1
- doi: 10.1016/j.dte.2026.100127 | key: `doi:10.1016/j.dte.2026.100127`
- source: Q1

**Abstract**: This study proposes a physics-informed digital workflow for defect-tolerant life assessment of turbine discs, enabling efficient and scalable evaluation of crack growth behaviour across multiple defect scenarios. Turbine discs are fracture-critical aero-engine components whose structural integrity is strongly influenced by defect-driven fatigue crack growth. The proposed workflow integrates global finite element analysis, hotspot identification, local submodel extraction, and fracture-based life prediction within a unified computational chain linking structural response, defect morphology, and crack-driving mechanisms. Initial defects are idealized as equivalent cracks, and residual life is predicted by coupling FEM-derived local stress fields with a unified small-to-long crack growth model, enabling physically consistent evaluation across different defect sizes and locations. A representative turbine disc case is employed to demonstrate the workflow. The results show clear dependence of stress intensity factor and residual life on defect location, with surface defects generally more critical than subsurface or internal defects. Among the investigated regions, the dovetail root exh

## 415. Strain hardening in metallic materials: Mechanisms, applications, and multiscale pathways for next-generation alloys

- year: 2026 | venue: Materials Today Communications | tier: A | relevance: 2 | citations: 1
- doi: 10.1016/j.mtcomm.2026.115063 | key: `doi:10.1016/j.mtcomm.2026.115063`
- source: Q1

**Abstract**: Strain hardening (work hardening), the rise in flow stress with plastic strain, governs the strength–ductility balance of metallic alloys and strongly influences uniform elongation and crash/fatigue tolerance. This review synthesizes 209 studies (2017–2025) identified through Scopus, Web of Science, and ScienceDirect searches (Jan–Oct 2025) plus reference-chaining, and selected using explicit inclusion criteria (metallic systems; quantitative stress–strain or hardening indices; mechanistic interpretation) following PRISMA-style screening. Strain-hardening pathways across FCC, BCC, and HCP systems are examined, emphasizing dislocation storage vs dynamic recovery, grain-boundary/heterogeneous-structure hardening, precipitation–dislocation interactions, and twinning/phase-transformation–assisted hardening (TWIP/TRIP). Classical constitutive laws (Hollomon, Swift, Voce, Kocks–Mecking) are contrasted with emerging physics-informed and machine-learning approaches for predicting θ(ε) and n evolution. Where comparability allowed, descriptive group summaries are reported (median, IQR; bootstrap CIs when n ≥ 8 ; otherwise, findings are integrated via structured narrative synthesis. Finally, 

## 416. Recent advances in terahertz-based bound states in the continuum metasurfaces for 6G communications and MedTech

- year: 2026 | venue: Journal of Optics | tier: A | relevance: 2 | citations: 1
- doi: 10.1088/2040-8986/ae8605 | key: `doi:10.1088/2040-8986/ae8605`
- source: Q1

**Abstract**: Abstract Bound states in the continuums (BICs) have emerged as a revolutionary paradigm in terahertz (THz) photonics, enabling metasurfaces with theoretically infinite quality factors (Q-factors) and unprecedented light-matter control. This review synthesizes a decade of progress in THz-BIC research, tracing the evolution from foundational symmetry-protected designs to application-optimized quasi-BICs. We dissect multipolar origins, topological robustness, and symmetry-breaking strategies underpinning high-Q resonances, alongside computational frameworks for predictive design. The timeline highlights key milestones: early dielectric metasurfaces with high Q-factor, flexible biosensors achieving microgram detection limits, and Kerker-conditioned gas spectrometers reducing path lengths by few orders of magnitude. Emerging frontiers in reconfigurable BICs and chiral quantum photonics are critically evaluated. Despite breakthroughs, scalability barriers persist for 6G integration, including nano-fabrication tolerances, material loss trade-offs, and dynamic control gaps. This review establishes BIC metasurfaces as pivotal enablers of compact, high-efficiency THz technologies poised to b

## 417. Efficient Uncertainty Quantification in Electromagnetic Modeling Using Physics-Informed Deep Operator Neural Networks

- year: 2024 | venue:  | tier: A | relevance: 2 | citations: 0
- doi: 10.23919/inc-usnc-ursi61303.2024.10632459 | key: `doi:10.23919/inc-usnc-ursi61303.2024.10632459`
- source: Q1

**Abstract**: Quantifying the impact of material and fabrication tolerances is important in computer-aided design of electromagnetic structures (A. C. M. Austin and C. D. Sarris. “Efficient Analysis of Geometrical Uncertainty in the FDTD Method Using Polynomial Chaos with Application to Microwave Circuits,” IEEE Trans. Microw. Theory and Techn., vol. 61, issue 12, Dec. 2013). However, accurate modeling of these uncertainties requires a large number of electromagnetic simulations.

## 418. Neural Networks Ensembles to Accelerate Power Grid Contingency Analysis

- year: 2024 | venue: OSTI OAI (U.S. Department of Energy Office of Scientific and Technical Information) | tier: A | relevance: 2 | citations: 0
- doi: — | key: `t:neuralnetworksensemblestoacceleratepowergridcontingencyanalysis`
- source: Q1

**Abstract**: Novel uncertainty quantification approach for machine learning based physics informed graph neural networks capable of quickly computing bulk energy system contingencies from a large search space with tolerance to changing grid topologies.

## 419. Adaptive Basis-inspired Deep Neural Network for Solving Partial Differential Equations with Localized Features

- year: 2024 | venue: arXiv (Cornell University) | tier: A | relevance: 2 | citations: 0
- doi: 10.48550/arxiv.2412.00636 | key: `doi:10.48550/arxiv.2412.00636`
- source: Q1

**Abstract**: This paper proposes an Adaptive Basis-inspired Deep Neural Network (ABI-DNN) for solving partial differential equations with localized phenomena such as sharp gradients and singularities. Like the adaptive finite element method, ABI-DNN incorporates an iteration of "solve, estimate, mark, enhancement", which automatically identifies challenging regions and adds new neurons to enhance its capability. A key challenge is to force new neurons to focus on identified regions with limited understanding of their roles in approximation. To address this, we draw inspiration from the finite element basis function and construct the novel Basis-inspired Block (BI-block), to help understand the contribution of each block. With the help of the BI-block and the famous Kolmogorov Superposition Theorem, we first develop a novel fixed network architecture named the Basis-inspired Deep Neural Network (BI-DNN), and then integrate it into the aforementioned adaptive framework to propose the ABI-DNN. Extensive numerical experiments demonstrate that both BI-DNN and ABI-DNN can effectively capture the challenging singularities in target functions. Compared to PINN, BI-DNN attains significantly lower relati

## 420. Enhancing Fault Tolerance in Self-Healing Hardware Using Triple Modular Redundancy

- year: 2025 | venue: International Scientific Journal of Engineering and Management | tier: A | relevance: 2 | citations: 0
- doi: 10.55041/isjem02849 | key: `doi:10.55041/isjem02849`
- source: Q1

**Abstract**: This paper presents a novel self-healing architecture that synergistically combines hardened Triple Modular Redundancy (TMR) with adaptive fault recovery to address reliability challenges in mission-critical electronic systems. The proposed solution integrates radiation-hardened DICE-based TMR cells, intelligent fault monitoring, and machine learning-driven prognostics within a hierarchical framework that optimizes temporal, spatial, and information redundancy domains. Key innovations include adaptive clock domain partitioning, genetic algorithm-based resource reallocation, and physics-informed neural networks for aging prediction. Experimental validation through heavy ion radiation testing and accelerated aging demonstrates a 92% improvement in mean work-between-failure metrics compared to conventional approaches, with 89.2% fault prediction accuracy and <5% performance overhead. The architecture maintains compliance with stringent aerospace standards (DO-254 Level A) while establishing quantifiable reliability-power-performance tradeoffs for next-generation radiation-hardened systems. Keywords: Triple Modular Redundancy (TMR), Self-healing hardware, Radiation-hardened electronics

## 421. The Wiener path integral interpretation of the 3:1 combat rule

- year: 2025 | venue: Communications in Theoretical Physics | tier: A | relevance: 2 | citations: 0
- doi: 10.1088/1572-9494/ae2b60 | key: `doi:10.1088/1572-9494/ae2b60`
- source: Q1

**Abstract**: Abstract The Wiener path integral framework is proposed to model military combat dynamics by incorporating the neglected stochastic effects to the Lanchester’s square law. This framework is applied to evaluate the empirical 3:1 combat rule, which posits that an attacker requires a threefold force superiority to achieve victory. Specifically, the attacker’s winning probability is computed utilizing a semi-analytical Rayleigh–Ritz method. Numerical results demonstrate that the validity of the rule critically depends on specific parameter regimes, primarily contingent upon the relative combat effectiveness ratio between the opposing forces and the tolerance for attrition. This work establishes a physics-informed theoretical bridge between statistical mechanics and military operations research for analyzing uncertain combat systems.

## 422. The Wiener Path Integral Interpretation of the 3:1 Combat Rule

- year: 2025 | venue: arXiv (Cornell University) | tier: A | relevance: 2 | citations: 0
- doi: 10.48550/arxiv.2512.21957 | key: `doi:10.48550/arxiv.2512.21957`
- source: Q1

**Abstract**: The Wiener path integral framework is proposed to model military combat dynamics by incorporating the neglected stochastic effects to the Lanchester's square law. This framework is applied to evaluate the empirical 3:1 combat rule, which posits that an attacker requires a threefold force superiority to achieve victory. Specifically, the attacker's winning probability is computed utilizing a semi-analytical Rayleigh-Ritz method. Numerical results demonstrate that the validity of the rule critically depends on specific parameter regimes, primarily contingent upon the relative combat effectiveness ratio between the opposing forces and the tolerance for attrition. This work establishes a physics-informed theoretical bridge between statistical mechanics and military operations research for analyzing uncertain combat systems.

## 423. A Data-Driven Method with Known Physical Information Based on Dual-Layer Iterative Extended Kalman Filter

- year: 2025 | venue:  | tier: A | relevance: 2 | citations: 0
- doi: 10.1109/icoecai67333.2025.11335865 | key: `doi:10.1109/icoecai67333.2025.11335865`
- source: Q1

**Abstract**: Nonlinear dynamical system characterization presents formidable obstacles when employing established Sparse Identification of Nonlinear Dynamics (SINDy) frameworks under noisy operational conditions. SINDy’s inability to effectively handle noise accumulation arising from derivative computations fundamentally undermines system identification accuracy, particularly when measurement uncertainties propagate through the sparse regression process. This investigation presents a novel Iterative Extended Kalman Filter integrated with Physics-Informed SINDy (IEKF-PSINDy) framework. Our methodology strengthens SINDy’s noise tolerance and predictive accuracy through physical constraint integration and state estimation refinement. Computational experiments validate that IEKF-PSINDy significantly exceeds traditional techniques under severe noise scenarios, delivering superior identification precision and enhanced system robustness.

## 424. Voorspelling van de transversale trekeigenschappen van vezelversterkte composieten: Een data en fysica gedreven aanpak

- year: 2025 | venue: Lirias | tier: A | relevance: 2 | citations: 0
- doi: — | key: `t:voorspellingvandetransversaletrekeigenschappenvanvezelversterktecomposieteneenda`
- source: Q1

**Abstract**: Unidirectional fibre-reinforced composites are widely used in high-performance engineering structures due to their superior strength-to-weight ratio and damage tolerance. A critical mode of early failure in these materials is transverse cracking, which can severely compromise their structural integrity and long-term durability. The microscale is the relevant scale to understand and predict transverse cracking in fibre-reinforced composites, as it captures the detailed interaction between fibres and the surrounding matrix. Predicting such damage initiation and evolution at the microscale is particularly challenging, given the intrinsic heterogeneity and complex architecture of the composite microstructure. Traditional experimental characterisation techniques are often limited by cost and scalability. Meanwhile, conventional microstructure generators fail to capture key microstructure features, such as resin-rich pockets, that influence damage mechanisms. To overcome these limitations, this thesis presents an integrated, data-driven, and physics-informed framework for extracting fibre geometries and microstructural features, generating realistic microstructures, and conducting high-f

## 425. Hybrid Adaptive Digital Twin-Based Fault Tolerance for Cyber-Resilient EV Charging Systems

- year: 2026 | venue:  | tier: A | relevance: 2 | citations: 0
- doi: 10.1109/iatmsi68868.2026.11465248 | key: `doi:10.1109/iatmsi68868.2026.11465248`
- source: Q1

**Abstract**: The rapid proliferation of electric vehicles (EVs) introduces unprecedented challenges in reliability, cybersecurity, and operational continuity of charging infrastructures. To ensure uninterrupted and resilient operation, this paper proposes a novel Hybrid Adaptive Resilient Twin (HART-DT) algorithm that integrates digital twin (DT) technology with advanced faulttolerant control. The proposed framework establishes a realtime cyber-physical synchronization between a virtual EV twin and its physical counterpart to detect, isolate, and mitigate both sensor/actuator faults and malicious cyberattacks. A hybrid anomaly detection pipeline is designed by combining residualbased statistical tests, physics-informed invariants, and spectral anomaly features for early fault detection. Once an anomaly is detected, a sparse optimization-based isolation module identifies compromised components, which are further validated using model-consistency pruning within the digital twin. Subsequently, an adaptive safe-mode Model Predictive Control (MPC) strategy ensures stable and efficient charging operation under uncertainty. The proposed algorithm also introduces a replica-consensus mechanism between e

## 426. Integrated physics-informed and unsupervised learning assessment of hemp-reinforced masonry barrel vaults under shaking table testing

- year: 2026 | venue: Mechanical Systems and Signal Processing | tier: A | relevance: 2 | citations: 0
- doi: 10.1016/j.ymssp.2026.114886 | key: `doi:10.1016/j.ymssp.2026.114886`
- source: Q1

**Abstract**: The seismic assessment of strengthened masonry vaults through full-scale shaking-table testing remains limited, particularly for sustainable, heritage-compatible systems. This study investigates the dynamic response and damage evolution of full-scale masonry barrel vaults strengthened with a hemp-mesh biocomposite embedded in a cocciopesto matrix. A two-phase experimental campaign was carried out on two geometrically identical vaults subjected to progressively scaled three-component earthquake records, enabling the analysis of three representative structural configurations: unreinforced, newly reinforced, and damaged-then-reinforced. Reinforcement effectiveness and damage progression were assessed through a multi-indicator framework combining modal parameters with two proposed indicators: an energy-based indicator derived from Arias intensity and an autoencoder-based indicator. Each is formulated in a baseline-relative (excitation-dependent) form and in an input-normalized form where the energy-based indicator is normalized by the Arias intensity of the input and the autoencoder-based indicator by the squared RMS of the input. It follows that the input-normalized indicators isolate

## 427. Coupling Conductive Networks and Binder Chemistry to Balance Rate Capability and Mechanical Durability in Flexible NMC811 Cathodes

- year: 2026 | venue: ACS Applied Energy Materials | tier: A | relevance: 2 | citations: 0
- doi: 10.1021/acsaem.6c01815 | key: `doi:10.1021/acsaem.6c01815`
- source: Q1

**Abstract**: Abstract The rapid growth of flexible and wearable electronics has created an increasing demand for lithium-ion batteries that can maintain high electrochemical performance while withstanding repeated mechanical deformation. In this research, we investigate the incorporation of single-walled carbon nanotubes (SWCNTs) as a conductive carbon dopant together with a polymer binder (VT475) in LiNi0.8Mn0.1Co0.1O2 (NMC811) cathodes. SWCNTs play a dual role in cathode performance. Mechanically, their one-dimensional nanostructure mitigates particle pulverization and improves tolerance to mechanical deformation (e.g., bending), which is essential for flexible and wearable applications. Electrochemically, SWCNTs form a percolated conductive network within the cathode, significantly improving electronic conductivity and facilitating efficient electron transport. This synergistic effect enhances capacity retention and cycling stability, even at high C-rates (132 mAh/g@5C). Pouch cells incorporating the SWCNT-doped cathodes were extensively characterized using galvanostatic testing at various C-rates, long-term cycling (1000 cycles), electrochemical impedance spectroscopy, and adhesion testing 

## 428. Poloidal-Field Coil Set and Equilibrium-Current Optimization for a Compact Spherical-Tokamak Breeder: Shaping the Negative-Triangularity, Solenoid-Free Equilibrium with Vertical-Stability Authority

- year: 2026 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: A | relevance: 2 | citations: 0
- doi: 10.5281/zenodo.22645944 | key: `doi:10.5281/zenodo.22645944`
- source: Q1

**Abstract**: The poloidal-field (PF) coils are what hold a strongly shaped, strongly elongated plasma in place: they must pull the outboard boundary inward to negative triangularity, sustain a doubling elongation against its own ideal vertical instability, and set the divertor null, while the toroidal-field magnet does its own, entirely separate job. We pose the coil-current problem for a compact negative-triangularity spherical-tokamak breeder (design point I_p=9.66 MA, Q=3.076, P_ fus=85.04 MW, δ=-0.30, κ=2.0, B_0=8 T, =1.20 m, aspect ratio A=2.5) as a regularized inverse free-boundary problem: sixteen isoflux constraints on a Miller negative-triangularity boundary, a two-parameter current-profile family pinned to the poloidal beta and the plasma current, and the coil currents recovered by a Tikhonov least-squares over the vacuum Green's functions at each Picard step of a free-boundary Grad–Shafranov solve. We derive the governing equations, the inverse-problem formulation, and the numerical scheme — a five-point discretization of the elliptic operator on a 129×129 grid, a von Hagenow free-boundary treatment, and Picard iteration to a relative flux tolerance of 10^-6 — and we report the conve

## 429. Poloidal-Field Coil Set and Equilibrium-Current Optimization for a Compact Spherical-Tokamak Breeder: Shaping the Negative-Triangularity, Solenoid-Free Equilibrium with Vertical-Stability Authority

- year: 2026 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: A | relevance: 2 | citations: 0
- doi: 10.5281/zenodo.22645945 | key: `doi:10.5281/zenodo.22645945`
- source: Q1

**Abstract**: The poloidal-field (PF) coils are what hold a strongly shaped, strongly elongated plasma in place: they must pull the outboard boundary inward to negative triangularity, sustain a doubling elongation against its own ideal vertical instability, and set the divertor null, while the toroidal-field magnet does its own, entirely separate job. We pose the coil-current problem for a compact negative-triangularity spherical-tokamak breeder (design point I_p=9.66 MA, Q=3.076, P_ fus=85.04 MW, δ=-0.30, κ=2.0, B_0=8 T, =1.20 m, aspect ratio A=2.5) as a regularized inverse free-boundary problem: sixteen isoflux constraints on a Miller negative-triangularity boundary, a two-parameter current-profile family pinned to the poloidal beta and the plasma current, and the coil currents recovered by a Tikhonov least-squares over the vacuum Green's functions at each Picard step of a free-boundary Grad–Shafranov solve. We derive the governing equations, the inverse-problem formulation, and the numerical scheme — a five-point discretization of the elliptic operator on a 129×129 grid, a von Hagenow free-boundary treatment, and Picard iteration to a relative flux tolerance of 10^-6 — and we report the conve

## 430. Implicit and Explicit Treatments of Model Error in Numerical Simulation

- year: 2026 | venue: Archives of Computational Methods in Engineering | tier: A | relevance: 2 | citations: 0
- doi: 10.1007/s11831-026-10522-w | key: `doi:10.1007/s11831-026-10522-w`
- source: Q1

**Abstract**: Abstract Numerical simulations of physical systems exhibit discrepancies arising from unmodeled physics and idealizations, as well as numerical approximation errors stemming from discretization and solver tolerances. This article reviews techniques developed in the past several decades to approximate and account for model errors, both implicitly and explicitly. Beginning from fundamentals, we frame model error in inverse problems, data assimilation, and predictive modeling contexts. We then survey major approaches: the Bayesian approximation error framework, embedded internal error models for structural uncertainty, probabilistic numerical methods for discretization uncertainty, model discrepancy modeling in Bayesian calibration and its recent extensions, machine-learning-based discrepancy correction, multi-fidelity and hybrid modeling strategies, as well as residual-based, variational, and adjoint-driven error estimators. Throughout, we emphasize the conceptual underpinnings of implicit versus explicit error treatment and highlight how these methods improve predictive performance and uncertainty quantification in practical applications ranging from engineering design to Earth-syst

## 431. Poloidal-Field Coil Set and Equilibrium-Current Optimization for a Compact Spherical-Tokamak Breeder: Shaping the Negative-Triangularity, Solenoid-Free Equilibrium with Vertical-Stability Authority

- year: 2026 | venue: Harvard Dataverse | tier: A | relevance: 2 | citations: 0
- doi: 10.7910/dvn/jxwtju | key: `doi:10.7910/dvn/jxwtju`
- source: Q1

**Abstract**: The poloidal-field (PF) coils are what hold a strongly shaped, strongly elongated plasma in place: they must pull the outboard boundary inward to negative triangularity, sustain a doubling elongation against its own ideal vertical instability, and set the divertor null, while the toroidal-field magnet does its own, entirely separate job. We pose the coil-current problem for a compact negative-triangularity spherical-tokamak breeder (design point I_p=9.66 MA, Q=3.076, P_ fus=85.04 MW, δ=-0.30, κ=2.0, B_0=8 T, =1.20 m, aspect ratio A=2.5) as a regularized inverse free-boundary problem: sixteen isoflux constraints on a Miller negative-triangularity boundary, a two-parameter current-profile family pinned to the poloidal beta and the plasma current, and the coil currents recovered by a Tikhonov least-squares over the vacuum Green's functions at each Picard step of a free-boundary Grad–Shafranov solve. We derive the governing equations, the inverse-problem formulation, and the numerical scheme — a five-point discretization of the elliptic operator on a 129×129 grid, a von Hagenow free-boundary treatment, and Picard iteration to a relative flux tolerance of 10^-6 — and we report the conve

## 432. Making the Invisible Visible: Toward High-Quality Terahertz Tomographic Imaging via Physics-Guided Restoration

- year: 2023 | venue: arXiv (Cornell University) | tier: A | relevance: 2 | citations: 0
- doi: 10.48550/arxiv.2304.14894 | key: `doi:10.48550/arxiv.2304.14894`
- source: Q4

**Abstract**: Terahertz (THz) tomographic imaging has recently attracted significant attention thanks to its non-invasive, non-destructive, non-ionizing, material-classification, and ultra-fast nature for object exploration and inspection. However, its strong water absorption nature and low noise tolerance lead to undesired blurs and distortions of reconstructed THz images. The diffraction-limited THz signals highly constrain the performances of existing restoration methods. To address the problem, we propose a novel multi-view Subspace-Attention-guided Restoration Network (SARNet) that fuses multi-view and multi-spectral features of THz images for effective image restoration and 3D tomographic reconstruction. To this end, SARNet uses multi-scale branches to extract intra-view spatio-spectral amplitude and phase features and fuse them via shared subspace projection and self-attention guidance. We then perform inter-view fusion to further improve the restoration of individual views by leveraging the redundancies between neighboring views. Here, we experimentally construct a THz time-domain spectroscopy (THz-TDS) system covering a broad frequency range from 0.1 THz to 4 THz for building up a tempo

## 433. Keynote Speaker 1

- year: 2023 | venue:  | tier: A | relevance: 2 | citations: 0
- doi: 10.1109/cosite60233.2023.10249263 | key: `doi:10.1109/cosite60233.2023.10249263`
- source: Q4

**Abstract**: Terahertz (THz) computational imaging has recently attracted significant attention thanks to its non-invasive, non-destructive, non-ionizing, materialclassification, and ultra-fast nature for 3D object exploration and inspection.However, its strong water absorption nature and low noise tolerance lead to undesired blurs and degradations of reconstructed THz images.The performances of existing methods are highly constrained by the diffraction-limited THz signals.In this talk, we will introduce the characteristics of THz imaging and its applications.We will also show how to break the limitations of THz imaging with the aid of rich spectral amplitude and phase information carried in prominent THz frequencies (i.e., the water absorption profile of THz signal) for THz image restoration.To this end, we propose a novel physics-guided deep neural network model, namely Subspace-Attention-guided Restoration Network (SARNet), that fuses such multi-spectral features of THz images for effective restoration.Furthermore, we experimentally construct a THz time-domain spectroscopy system covering a broad frequency range from 0.1 THz to 4 THz for building up THz CT database of hidden 3D objects.

## 434. Device-physics co-design of hybrid RRAM-MRAM crossbars: overcoming stochastic non-idealities for energy efficient edge speech recognition

- year: 2025 | venue: AIP Publishing | tier: A | relevance: 2 | citations: 0
- doi: 10.60893/figshare.jap.c.8121287.v1 | key: `doi:10.60893/figshare.jap.c.8121287.v1`
- source: Q4

**Abstract**: Memristive in-memory computing leverages intrinsic device physics to overcome von Neumann bottlenecks in edge AI, yet non-idealities in resistive switching materials limit deployment robustness. Here, we demonstrate a physics-guided hybrid memristor architecture integrating resistive random-access memory (RRAM) and magnetoresistive random-access memory (MRAM) for energy-efficient keyword spotting (KWS). By co-designing a binarized depthwise separable convolutional neural network (790-bit model) with device-aware algorithms, we exploit the complementary physical properties of RRAM (high density, filamentary switching) and MRAM (high endurance, spintronic switching). Convolutional layers are mapped to RRAM crossbars for parallel analog vector-matrix multiplication via Ohm's law, while fully connected layers utilize MRAM's endurance for in-situ training. A statistic-aware training strategy incorporates device stochasticity (Gaussian resistance variation, shorts/opens) during backpropagation, enhancing fault tolerance. Implemented on a 1-kb TiN/HfOx/TaOx RRAM and CoFeB/MgO-based MRAM array, the system achieves 3.72 ms latency and 14.95 μW power at >85% accuracy under 20% defect rates. 

## 435. Device-physics co-design of hybrid RRAM-MRAM crossbars: overcoming stochastic non-idealities for energy efficient edge speech recognition

- year: 2025 | venue: AIP Publishing | tier: A | relevance: 2 | citations: 0
- doi: 10.60893/figshare.jap.c.8121287 | key: `doi:10.60893/figshare.jap.c.8121287`
- source: Q4

**Abstract**: Memristive in-memory computing leverages intrinsic device physics to overcome von Neumann bottlenecks in edge AI, yet non-idealities in resistive switching materials limit deployment robustness. Here, we demonstrate a physics-guided hybrid memristor architecture integrating resistive random-access memory (RRAM) and magnetoresistive random-access memory (MRAM) for energy-efficient keyword spotting (KWS). By co-designing a binarized depthwise separable convolutional neural network (790-bit model) with device-aware algorithms, we exploit the complementary physical properties of RRAM (high density, filamentary switching) and MRAM (high endurance, spintronic switching). Convolutional layers are mapped to RRAM crossbars for parallel analog vector-matrix multiplication via Ohm's law, while fully connected layers utilize MRAM's endurance for in-situ training. A statistic-aware training strategy incorporates device stochasticity (Gaussian resistance variation, shorts/opens) during backpropagation, enhancing fault tolerance. Implemented on a 1-kb TiN/HfOx/TaOx RRAM and CoFeB/MgO-based MRAM array, the system achieves 3.72 ms latency and 14.95 μW power at >85% accuracy under 20% defect rates. 

## 436. Device-physics co-design of hybrid RRAM-MRAM crossbars: Overcoming stochastic non-idealities for energy efficient edge speech recognition

- year: 2025 | venue: Journal of Applied Physics | tier: A | relevance: 2 | citations: 0
- doi: 10.1063/5.0293805 | key: `doi:10.1063/5.0293805`
- source: Q4

**Abstract**: Memristive in-memory computing leverages intrinsic device physics to overcome von Neumann bottlenecks in edge artificial intelligence (AI), yet non-idealities in resistive switching materials limit deployment robustness. Here, we demonstrate a physics-guided hybrid memristor architecture integrating resistive random-access memory (RRAM) and magnetoresistive random-access memory (MRAM) for energy-efficient keyword spotting. By co-designing a binarized depthwise separable convolutional neural network (790-bit model) with device-aware algorithms, we exploit the complementary physical properties of RRAM (high density, filamentary switching) and MRAM (high endurance, spintronic switching). Convolutional layers are mapped to RRAM crossbars for parallel analog vector-matrix multiplication via Ohm's law, while fully connected layers utilize MRAM's endurance for in situ training. A statistic-aware training strategy incorporates device stochasticity (Gaussian resistance variation, shorts/opens) during backpropagation, enhancing fault tolerance. Implemented on a 1 kb TiN/HfOx/TaOx RRAM and CoFeB/MgO-based MRAM array, the system achieves 3.72 ms latency and 14.95 μW power at >85% accuracy unde

## 437. Digital Twin Construction and Safety Early Warning for UHVDC Steel Transmission Towers Under Icing and Galloping Conditions

- year: 2026 | venue: 2026 2nd International Conference on Advanced Energy Systems and Power Electronics (AESPE) | tier: A | relevance: 2 | citations: 0
- doi: 10.1109/AESPE70224.2026.11601951 | key: `doi:10.1109/aespe70224.2026.11601951`
- source: S2-Q1

**Abstract**: Conductor galloping severely threatens the structural integrity of Ultra-High Voltage Direct Current (UHVDC)steel towers under atmospheric icing, yet real-time tower security evaluation is inadequately addressed by existing digital twin applications under dynamic galloping loads. A specialized six-dimensional digital twin structure mapping galloping-induced unbalanced tensions from tower-line coupled analysis onto a high-fidelity finite element model of the tower is proposed. Formalized via coordinate transformation, a virtual-real deflection mapping system realizes real-time synchronization between sensors and the virtual entity. According to simulation experiments on a 500 kV UHVDC system, galloping increases tower top displacement by 2.5–4.5 times by comparing with static ice conditions, with peak response at 15 m/s. A Critical Success Index of 0.917 is achieved by the deflection-based warning mechanism with sub-2% mapping error. The put-forward framework connects aerodynamic galloping analysis and component-level structure health watching, gives a physics-informed method to promote the working tolerance of UHVDC transmission infrastructure in regions easy to have icing, which m

## 438. Recent advances and future prospects of laser-arc hybrid welding: process parameters, microstructural evolution, mechanical performance, and numerical simulation

- year: 2026 | venue: Journal of Materials Research and Technology | tier: A | relevance: 1 | citations: 0
- doi: 10.1016/j.jmrt.2026.08.269 | key: `doi:10.1016/j.jmrt.2026.08.269`
- source: Q1

**Abstract**: : Laser-arc hybrid welding (LAHW) has emerged as a promising joining technology by integrating the high energy density and deep penetration capability of laser welding with the excellent gap tolerance and metallurgical adaptability of arc welding. Although extensive investigations have been conducted on LAHW, challenges associated with process instability, defect formation, microstructural heterogeneity, and insufficient predictive capability of numerical models still restrict its widespread application. In this work, the laser-arc interaction mechanisms, process parameter optimization, molten pool dynamics, microstructural evolution, mechanical performance, and numerical simulation approaches in LAHW are summarized. In particular, an integrated framework linking processing parameters, heat-source coupling behavior, keyhole stability, defect evolution, microstructure formation, and joint performance is established. Furthermore, heat-source model selection, comparisons between finite-element and thermo-fluid models, keyhole evolution, and defect prediction are analyzed. Future perspectives are discussed regarding artificial intelligence-assisted parameter optimization, real-time mon

## 439. Evaluating DV/CV-QKD Architectures for SAFE Long-Term Secure Storage: A Risk Model and ILP-Based Cost Optimization Approach

- year: 2026 | venue: arXiv (Cornell University) | tier: A | relevance: 0 | citations: 0
- doi: — | key: `t:evaluatingdvcvqkdarchitecturesforsafelongtermsecurestorageariskmodelandilpbasedc`
- source: Q1

**Abstract**: This paper presents a unified cost-modeling and optimization framework designed to evaluate hybrid discrete-variable/continuous-variable quantum key distribution (DV/CV-QKD) infrastructures operating within the SAFE (Secure and Efficient) long-term storage (LTSS) protocol. Our methodology jointly addresses the information-theoretic and computational dimensions of cryptographic durability over multi-decade horizons by coupling a quantitative risk model with a stochastic integer linear programming (ILP) formulation. Going beyond idealized physics-informed limits, the framework incorporates realistic next-generation industrial implementations and multiplexed coexistence specifications, together with a sample-average approximation (SAA) pipeline, to determine cost-optimal and structurally feasible SAFE topologies under transmission-budget and security constraints. The proposed framework is evaluated on both randomized synthetic deployments and realistic metropolitan-scale QKD infrastructures, including the Paris Metro-Scale and Greater Paris networks, to characterize the interplay between network topology, QKD modality, and deployment cost while enforcing a target global compromise tol

## 440. Evaluating DV/CV-QKD Architectures for SAFE Long-Term Secure Storage: A Risk Model and ILP-Based Cost Optimization Approach

- year: 2026 | venue: arXiv (Cornell University) | tier: A | relevance: 0 | citations: 0
- doi: 10.48550/arxiv.2607.19010 | key: `doi:10.48550/arxiv.2607.19010`
- source: Q1

**Abstract**: This paper presents a unified cost-modeling and optimization framework designed to evaluate hybrid discrete-variable/continuous-variable quantum key distribution (DV/CV-QKD) infrastructures operating within the SAFE (Secure and Efficient) long-term storage (LTSS) protocol. Our methodology jointly addresses the information-theoretic and computational dimensions of cryptographic durability over multi-decade horizons by coupling a quantitative risk model with a stochastic integer linear programming (ILP) formulation. Going beyond idealized physics-informed limits, the framework incorporates realistic next-generation industrial implementations and multiplexed coexistence specifications, together with a sample-average approximation (SAA) pipeline, to determine cost-optimal and structurally feasible SAFE topologies under transmission-budget and security constraints. The proposed framework is evaluated on both randomized synthetic deployments and realistic metropolitan-scale QKD infrastructures, including the Paris Metro-Scale and Greater Paris networks, to characterize the interplay between network topology, QKD modality, and deployment cost while enforcing a target global compromise tol

## 441. A Drop-in, Focus-Extending Phase Mask Simplifies Microscopic and Microfluidic Imaging Systems for Cost-Effective Point-of-Care Diagnostics

- year: 2022 | venue: Analytical Chemistry | tier: A | relevance: -1 | citations: 7
- doi: 10.1021/acs.analchem.2c01421 | key: `doi:10.1021/acs.analchem.2c01421`
- source: Q1

**Abstract**: Microscopic imaging and imaging flow cytometry have wide potential in point-of-care assays; however, their narrow depth of focus necessitates precise mechanical or fluidic focus control of a sample in order to acquire high-quality images that can be used for downstream analysis, increasing the cost and complexity of the imaging system. This complexity represents a barrier to miniaturization and translation of point-of-care assays based on microscopic imaging or imaging flow cytometry. To address this challenge, we present a simple drop-in phase mask with a physics-informed, circularly symmetric asphere phase profile that extends the depth of focus by >5-fold while largely preserving the image quality compared to other depth extending methods. We show that such a focus-extended system overcomes manufacturing tolerances in low-cost sample chambers, enlarges the useable field-of-view of low-cost objectives, and permits increased throughput and precision in flow imaging systems without the need for complex flow-focusing. As the image quality is preserved without the need for postacquisition image restoration, our solution is also highly appropriate for on-line applications such as cell

## 442. Inverse-designed release-free optomechanical crystal with high photon-phonon coupling

- year: 2026 | venue: arXiv (Cornell University) | tier: A | relevance: -1 | citations: 1
- doi: 10.48550/arxiv.2605.03910 | key: `doi:10.48550/arxiv.2605.03910`
- source: Q4

**Abstract**: Interactions between light and mechanics provide a powerful interface between optical and microwave-frequency signals, with applications spanning classical signal processing and quantum technologies. High-performance optomechanical devices require both strong photon-phonon coupling and tolerance to parasitic laser heating. Release-free optomechanical crystals provide improved thermal anchoring compared to suspended nanobeams, but have so far exhibited weaker vacuum optomechanical coupling rates, leaving a trade-off between coupling strength and thermal robustness. Here, we largely close this gap: we design and experimentally demonstrate a release-free silicon optomechanical crystal with a record vacuum optomechanical coupling rate of about $g_\text{OM} / (2 π) = 800$ kHz, comparable to suspended state-of-the-art devices. The resulting optomechanical scattering rate $Γ_\text{OM}/(2 π)= 1.1$ kHz is nearly twice that of previous release-free implementations. This performance is achieved by combining physics-guided human intuition with a multiphysics inverse-design algorithm introduced here for resonant optomechanical structures. Beyond the specific device demonstrated, the inverse-des

## 443. Inverse-designed release-free optomechanical crystal with high photon-phonon coupling

- year: 2026 | venue: arXiv (Cornell University) | tier: A | relevance: -1 | citations: 0
- doi: — | key: `t:inversedesignedreleasefreeoptomechanicalcrystalwithhighphotonphononcoupling`
- source: Q4

**Abstract**: Interactions between light and mechanics provide a powerful interface between optical and microwave-frequency signals, with applications spanning classical signal processing and quantum technologies. High-performance optomechanical devices require both strong photon-phonon coupling and tolerance to parasitic laser heating. Release-free optomechanical crystals provide improved thermal anchoring compared to suspended nanobeams, but have so far exhibited weaker vacuum optomechanical coupling rates, leaving a trade-off between coupling strength and thermal robustness. Here, we largely close this gap: we design and experimentally demonstrate a release-free silicon optomechanical crystal with a record vacuum optomechanical coupling rate of about $g_\text{OM} / (2 π) = 800$ kHz, comparable to suspended state-of-the-art devices. The resulting optomechanical scattering rate $Γ_\text{OM}/(2 π)= 1.1$ kHz is nearly twice that of previous release-free implementations. This performance is achieved by combining physics-guided human intuition with a multiphysics inverse-design algorithm introduced here for resonant optomechanical structures. Beyond the specific device demonstrated, the inverse-des

## 444. Single-shot characterization of photon indistinguishability with dielectric metasurfaces

- year: 2024 | venue: arXiv (Cornell University) | tier: A | relevance: -2 | citations: 0
- doi: 10.48550/arxiv.2401.01485 | key: `doi:10.48550/arxiv.2401.01485`
- source: Q1

**Abstract**: Characterizing the indistinguishability of photons is a key task in quantum photonics, underpinning the tuning and stabilization of the photon sources and thereby increasing the accuracy of quantum operations. The protocols for measuring the degree of indistinguishability conventionally require photon-coincidence measurements at several different time or phase delays, which is a fundamental bottleneck towards the fast measurements and real-time monitoring of indistinguishability. Here, we develop a static dielectric metasurface grating without any reconfigurable elements that realizes a tailored multiport transformation in the free-space configuration without the need for phase locking and enables single-shot characterization of the indistinguishability between two photons in multiple degrees of freedom including time, spectrum, spatial modes, and polarization. Topology optimization is employed to design a silicon metasurface with polarization independence, high transmission, and high tolerance to measurement noise. We fabricate the metasurface and experimentally quantify the indistinguishability of photons in the time domain with fidelity over 98.4\%. We anticipate that the develo

## 445. Benchmarking Quantum and Classical Algorithms for the 1D Burgers Equation: QTN, HSE, and PINN

- year: 2026 | venue: arXiv (Cornell University) | tier: A | relevance: -2 | citations: 0
- doi: — | key: `t:benchmarkingquantumandclassicalalgorithmsforthe1dburgersequationqtnhseandpinn`
- source: Q1

**Abstract**: We present a comparative benchmark of Quantum Tensor Networks (QTN), the Hydrodynamic Schrödinger Equation (HSE), and Physics-Informed Neural Networks (PINN) for simulating the 1D Burgers' equation. Evaluating these emerging paradigms against classical GMRES and Spectral baselines, we analyse solution accuracy, runtime scaling, and resource overhead across grid resolutions ranging from $N=4$ to $N=128$. Our results reveal a distinct performance hierarchy. The QTN solver achieves superior precision ($L_2 \sim 10^{-7}$) with remarkable near-constant runtime scaling, effectively leveraging entanglement compression to capture shock fronts. In contrast, while the Finite-Difference HSE implementation remains robust, the Spectral HSE method suffers catastrophic numerical instability at high resolutions, diverging significantly at $N=128$. PINNs demonstrate flexibility as mesh-free solvers but stall at lower accuracy tiers ($L_2 \sim 10^{-1}$), limited by spectral bias compared to grid-based methods. Ultimately, while quantum methods offer novel representational advantages for low-resolution fluid dynamics, this study confirms they currently yield no computational advantage over classical 

## 446. Benchmarking Quantum and Classical Algorithms for the 1D Burgers Equation: QTN, HSE, and PINN

- year: 2026 | venue: arXiv (Cornell University) | tier: A | relevance: -2 | citations: 0
- doi: 10.48550/arxiv.2602.04239 | key: `doi:10.48550/arxiv.2602.04239`
- source: Q1

**Abstract**: We present a comparative benchmark of Quantum Tensor Networks (QTN), the Hydrodynamic Schrödinger Equation (HSE), and Physics-Informed Neural Networks (PINN) for simulating the 1D Burgers' equation. Evaluating these emerging paradigms against classical GMRES and Spectral baselines, we analyse solution accuracy, runtime scaling, and resource overhead across grid resolutions ranging from $N=4$ to $N=128$. Our results reveal a distinct performance hierarchy. The QTN solver achieves superior precision ($L_2 \sim 10^{-7}$) with remarkable near-constant runtime scaling, effectively leveraging entanglement compression to capture shock fronts. In contrast, while the Finite-Difference HSE implementation remains robust, the Spectral HSE method suffers catastrophic numerical instability at high resolutions, diverging significantly at $N=128$. PINNs demonstrate flexibility as mesh-free solvers but stall at lower accuracy tiers ($L_2 \sim 10^{-1}$), limited by spectral bias compared to grid-based methods. Ultimately, while quantum methods offer novel representational advantages for low-resolution fluid dynamics, this study confirms they currently yield no computational advantage over classical 

## 447. Using optimal control to guide neural-network interpolation of continuously-parameterized gates

- year: 2024 | venue: arXiv (Cornell University) | tier: A | relevance: -7 | citations: 0
- doi: 10.48550/arxiv.2412.06623 | key: `doi:10.48550/arxiv.2412.06623`
- source: Q1

**Abstract**: Control synthesis for continuously-parameterized families of quantum gates can enable critical advantages for mid-sized quantum computing applications in advance of fault-tolerance. We combine quantum optimal control with physics-informed machine learning to efficiently synthesize control surfaces that interpolate among continuously-parameterized gate families. Using optimal control as an active learning strategy to guide pretraining, we bootstrap a physics-informed neural network to achieve rapid convergence to nonlinear control surfaces sufficient for our desired gates. We find our approach is critical for enabling an expressiveness beyond linear interpolation, which is important in cases of hard quantum control. We show in simulation that by adapting our pretraining to use a few reference pulse calibrations, we can apply transfer learning to quickly calibrate our learned control surfaces when devices fluctuate over time. We demonstrate synthesis for one and two qubit gates with one or two parameters, focusing on gate families for variational quantum algorithm (VQA) ansatz. By avoiding the inefficient decomposition of VQA ansatz into basis gate sets, continuous gate families are 

## 448. Using Optimal Control to Guide Neural-Network Interpolation of Continuously-Parameterized Gates

- year: 2024 | venue:  | tier: A | relevance: -7 | citations: 0
- doi: 10.1109/qce60285.2024.00159 | key: `doi:10.1109/qce60285.2024.00159`
- source: Q1

**Abstract**: Control synthesis for continuously-parameterized families of quantum gates can enable critical advantages for mid-sized quantum computing applications in advance of fault-tolerance. We combine quantum optimal control with physics-informed machine learning to efficiently synthesize control surfaces that interpolate among continuously-parameterized gate families. Using optimal control as an active learning strategy to guide pretraining, we bootstrap a physics-informed neural network to achieve rapid convergence to nonlinear control surfaces sufficient for our desired gates. We find our approach is critical for enabling an expressiveness beyond linear interpolation, which is important in cases of hard quantum control. We show in simulation that by adapting our pretraining to use a few reference pulse calibrations, we can apply transfer learning to quickly calibrate our learned control surfaces when devices fluctuate over time. We demonstrate synthesis for one and two qubit gates with one or two parameters, focusing on gate families for variational quantum algorithm (VQA) ansatz. By avoiding the inefficient decomposition of VQA ansatz into basis gate sets, continuous gate families are 

## 449. Quantum Optimization Algorithms for Strongly Correlated Many-Body Systems

- year: 2026 | venue: arXiv (Cornell University) | tier: A | relevance: -18 | citations: 0
- doi: — | key: `t:quantumoptimizationalgorithmsforstronglycorrelatedmanybodysystems`
- source: Q1

**Abstract**: This perspective article analyzes the potential and critical challenges of employing quantum optimization algorithms to investigate phase transitions in quantum many-body systems during the Noisy Intermediate-Scale Quantum era. The simulation of strongly correlated systems is frequently intractable on classical computers due to the exponential growth of the Hilbert space and the fermionic sign problem. In this context, we review and compare the performance of traditional Variational Quantum Algorithms, such as the Variational Quantum Eigensolver and the Quantum Approximate Optimization Algorithm, against emerging heuristic approaches, specifically Feedback-based Quantum Algorithms, such as FALQON. We explore the applicability of these methods in the study of open phenomena in condensed matter physics, including Deconfined Quantum Criticality, strange metals, Many-Body Localization, topological phase transitions, and quantum spin liquids. We discuss how fundamental operational bottlenecks, notably expressibility- and noise-induced barren plateaus, severely compromise gradient-based optimization. We conclude that deterministic feedback-guided methods provide geometrically more robust
