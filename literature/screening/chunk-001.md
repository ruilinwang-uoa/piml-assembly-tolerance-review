# 筛查分块 1（记录 1–50 / 共 449）

## 1. Review of Recent Additive Manufacturing and Welding Research with Application of Physics-Informed Neural Networks

- year: 2024 | venue: Journal of Welding and Joining | tier: B | relevance: 21 | citations: 10
- doi: 10.5781/jwj.2024.42.4.3 | key: `doi:10.5781/jwj.2024.42.4.3`
- source: Q3

**Abstract**: This review introduces recent research on applying physics-informed neural networks (PINNs) to additive manufacturing and welding. PINNs, which are artificial intelligence models, integrate governing equations containing physical information with artificial neural networks, enabling the modeling of complex physical phenomena at a lower computational cost than traditional numerical models. Although PINNs have been employed in a limited number of studies on welding processes, they have been extensively used in various studies within the field of additive manufacturing. This study reviews the theoretical background of PINNs to explore their effective application to welding processes, examining 12 research cases in additive manufacturing and two research cases in welding processes. The analysis included the structure of the PINN, governing equations, and prediction results of each study. Results indicate that PINNs provide faster computation speeds and higher prediction accuracies than numerical models. Moreover, they could perform analyses without additional training even when process parameters and materials changed. Additionally, PINNs have been effectively applied to predict the me

## 2. A unified scalable framework for causal sweeping strategies for Physics-Informed Neural Networks (PINNs) and their temporal decompositions

- year: 2023 | venue: arXiv (Cornell University) | tier: A | relevance: 21 | citations: 9
- doi: 10.48550/arxiv.2302.14227 | key: `doi:10.48550/arxiv.2302.14227`
- source: Q1

**Abstract**: Physics-informed neural networks (PINNs) as a means of solving partial differential equations (PDE) have garnered much attention in the Computational Science and Engineering (CS&E) world. However, a recent topic of interest is exploring various training (i.e., optimization) challenges - in particular, arriving at poor local minima in the optimization landscape results in a PINN approximation giving an inferior, and sometimes trivial, solution when solving forward time-dependent PDEs with no data. This problem is also found in, and in some sense more difficult, with domain decomposition strategies such as temporal decomposition using XPINNs. We furnish examples and explanations for different training challenges, their cause, and how they relate to information propagation and temporal decomposition. We then propose a new stacked-decomposition method that bridges the gap between time-marching PINNs and XPINNs. We also introduce significant computational speed-ups by using transfer learning concepts to initialize subnetworks in the domain and loss tolerance-based propagation for the subdomains. Finally, we formulate a new time-sweeping collocation point algorithm inspired by the previo

## 3. Physics-Informed Machine Learning and Uncertainty Quantification for Mechanics of Heterogeneous Materials

- year: 2022 | venue: arXiv (Cornell University) | tier: B | relevance: 19 | citations: 1
- doi: 10.48550/arxiv.2202.10423 | key: `doi:10.48550/arxiv.2202.10423`
- source: Q1

**Abstract**: In this work, a model based on the Physics - Informed Neural Networks (PINNs) for solving elastic deformation of heterogeneous solids and associated Uncertainty Quantification (UQ) is presented. For the present study, the PINNs framework - Modulus developed by Nvidia is utilized, wherein we implement a module for mechanics of heterogeneous solids. We use PINNs to approximate momentum balance by assuming isotropic linear elastic constitutive behavior against a loss function. Along with governing equations, the associated initial / boundary conditions also softly participate in the loss function. Solids where the heterogeneity manifests as voids (low elastic modulus regions) and fibers (high elastic modulus regions) in a matrix are analyzed, and the results are validated against solutions obtained from a commercial Finite Element (FE) analysis package. The present study also reveals that PINNs can capture the stress jumps precisely at the material interfaces. Additionally, the present study explores the advantages associated with the surrogate features in PINNs via the variation in geometry and material properties. The presented UQ studies suggest that the mean and standard deviation

## 4. Finite basis physics-informed neural networks as a Schwarz domain decomposition method

- year: 2022 | venue: arXiv (Cornell University) | tier: B | relevance: 17 | citations: 3
- doi: 10.48550/arxiv.2211.05560 | key: `doi:10.48550/arxiv.2211.05560`
- source: Q1

**Abstract**: Physics-informed neural networks (PINNs) [4, 10] are an approach for solving boundary value problems based on differential equations (PDEs). The key idea of PINNs is to use a neural network to approximate the solution to the PDE and to incorporate the residual of the PDE as well as boundary conditions into its loss function when training it. This provides a simple and mesh-free approach for solving problems relating to PDEs. However, a key limitation of PINNs is their lack of accuracy and efficiency when solving problems with larger domains and more complex, multi-scale solutions. In a more recent approach, finite basis physics-informed neural networks (FBPINNs) [8] use ideas from domain decomposition to accelerate the learning process of PINNs and improve their accuracy. In this work, we show how Schwarz-like additive, multiplicative, and hybrid iteration methods for training FBPINNs can be developed. We present numerical experiments on the influence of these different training strategies on convergence and accuracy. Furthermore, we propose and evaluate a preliminary implementation of coarse space correction for FBPINNs.

## 5. Physics-informed neural networks to accelerate heat transfer predictions in additive manufacturing

- year: 2025 | venue:  | tier: B | relevance: 17 | citations: 2
- doi: 10.33599/nasampe/s.25.0137 | key: `doi:10.33599/nasampe/s.25.0137`
- source: Q3

**Abstract**: Accurate and scalable prediction of thermal history is pivotal for optimizing print quality in extrusion deposition additive manufacturing (EDAM). This paper investigates the applicability of physics-informed neural networks (PINNs) for 3D heat transfer analysis during the additive manufacturing process. As finite element method (FEM) requires increasingly fine meshes and smaller time increments to achieve higher accuracy, its computational cost rises substantially. PINNs offer a more scalable solution by eliminating the need for meshes and time increment schemes. We achieve this by recasting the solution to the differential equation as a stochastic minimization problem. While the current focus is a single forward problem, the paper sets the groundwork for future research into parametric problems, where PINNs demonstrate their full potential by efficiently solving a range of scenarios under varying initial, boundary conditions, and material properties. Our results show that PINNs can be used to solve the 3D heat transfer equation on evolving geometries without the need for spatial discretization and time-stepping schemes. This study showcases the growing relevance of PINNs in manuf

## 6. Retained imaging quality with reduced manufacturing precision: leveraging computational optics

- year: 2025 | venue: Advanced Photonics Nexus | tier: A | relevance: 16 | citations: 2
- doi: 10.1117/1.APN.4.4.046014 | key: `doi:10.1117/1.apn.4.4.046014`
- source: S2-Q1

**Abstract**: Abstract. Manufacturing-robust imaging systems leveraging computational optics hold immense potential for easing manufacturing constraints and enabling the development of cost-effective, high-quality imaging solutions. However, conventional approaches, which typically rely on data-driven neural networks to correct optical aberrations caused by manufacturing errors, are constrained by the lack of effective tolerance analysis methods for quantitatively evaluating manufacturing error boundaries. This limitation is crucial for further relaxing manufacturing constraints and providing practical guidance for fabrication. We propose a physics-informed design paradigm for manufacturing-robust imaging systems with computational optics, integrating a physics-informed tolerance analysis methodology for evaluating manufacturing error boundaries and a physics-informed neural network for image reconstruction. With this approach, we achieve a manufacturing-robust imaging system based on an off-axis three-mirror freeform all-aluminum design, delivering a modulation transfer function exceeding 0.34 at the Nyquist frequency (72  lp/mm) in simulation. Notably, this system requires a manufacturing prec

## 7. On the Role of Consistency Between Physics and Data in Physics-Informed Neural Networks

- year: 2026 | venue: arXiv (Cornell University) | tier: B | relevance: 15 | citations: 0
- doi: — | key: `t:ontheroleofconsistencybetweenphysicsanddatainphysicsinformedneuralnetworks`
- source: Q3

**Abstract**: Physics-informed neural networks (PINNs) have gained significant attention as a surrogate modeling strategy for partial differential equations (PDEs), particularly in regimes where labeled data are scarce and physical constraints can be leveraged to regularize the learning process. In practice, however, PINNs are frequently trained using experimental or numerical data that are not fully consistent with the governing equations due to measurement noise, discretization errors, or modeling assumptions. The implications of such data-to-PDE inconsistencies on the accuracy and convergence of PINNs remain insufficiently understood. In this work, we systematically analyze how data inconsistency fundamentally limits the attainable accuracy of PINNs. We introduce the concept of a consistency barrier, defined as an intrinsic lower bound on the error that arises from mismatches between the fidelity of the data and the exact enforcement of the PDE residual. To isolate and quantify this effect, we consider the 1D viscous Burgers equation with a manufactured analytical solution, which enables full control over data fidelity and residual errors. PINNs are trained using datasets of progressively inc

## 8. On the Role of Consistency Between Physics and Data in Physics-Informed Neural Networks

- year: 2026 | venue: DIGITAL.CSIC (Spanish National Research Council (CSIC)) | tier: B | relevance: 15 | citations: 0
- doi: 10.48550/arxiv.2602.10611 | key: `doi:10.48550/arxiv.2602.10611`
- source: Q3

**Abstract**: Physics-informed neural networks (PINNs) have gained significant attention as a surrogate modeling strategy for partial differential equations (PDEs), particularly in regimes where labeled data are scarce and physical constraints can be leveraged to regularize the learning process. In practice, however, PINNs are frequently trained using experimental or numerical data that are not fully consistent with the governing equations due to measurement noise, discretization errors, or modeling assumptions. The implications of such data-to-PDE inconsistencies on the accuracy and convergence of PINNs remain insufficiently understood. In this work, we systematically analyze how data inconsistency fundamentally limits the attainable accuracy of PINNs. We introduce the concept of a consistency barrier, defined as an intrinsic lower bound on the error that arises from mismatches between the fidelity of the data and the exact enforcement of the PDE residual. To isolate and quantify this effect, we consider the 1D viscous Burgers equation with a manufactured analytical solution, which enables full control over data fidelity and residual errors. PINNs are trained using datasets of progressively inc

## 9. Physics-Informed Neural Networks for Solving Second-Order Boundary Value Problems: A Comparative Study with Fem and Finit Difference Methods

- year: 2026 | venue: Preprints.org | tier: B | relevance: 14 | citations: 1
- doi: 10.20944/preprints202604.0401.v1 | key: `doi:10.20944/preprints202604.0401.v1`
- source: Q3

**Abstract**: Physics-Informed Neural Networks (PINNs) have emerged as a powerful paradigm for solving partial differential equations (PDEs) by embedding physical laws directly into the neural network training process. This paper presents a comprehensive comparative study of PINNs against traditional numerical methods—Finite Element Method (FEM) and Finite Difference (FD)—for solving second-order boundary value problems. We focus on the canonical problem u″(x)=e-x on the domain [0,1] with Dirichlet boundary conditions u(0)=1 and u(1)=e-1, which admits the exact analytical solution u(x)=e-x. The PINN architecture employs a trial solution formulation that automatically satisfies boundary conditions, utilizes automatic differentiation for computing derivatives, and leverages the L-BFGS optimizer with Sobol quasi-random collocation points. We provide rigorous mathematical derivations of the PINN loss function, trial solution construction, automatic differentiation chain rules, FEM weak formulation with stiffness matrix assembly, and FD central difference schemes. Numerical experiments demonstrate that PINNs achieve comparable accuracy to FEM and FD methods while offering mesh-free flexibility and th

## 10. Benchmarking Physics-Informed Neural Networks and Boundary Elements Methods for Wave Scattering

- year: 2025 | venue: arXiv (Cornell University) | tier: B | relevance: 14 | citations: 0
- doi: 10.48550/arxiv.2509.12483 | key: `doi:10.48550/arxiv.2509.12483`
- source: Q1

**Abstract**: This study compares the Boundary Element Method (BEM) and Physics-Informed Neural Networks (PINNs) for solving the two-dimensional Helmholtz equation in wave scattering problems. The objective is to evaluate the performance of both methods under the same conditions. We solve the Helmholtz equation using BEM and PINNs for the same scattering problem. PINNs are trained by minimizing the residual of the governing equations and boundary conditions with their configuration determined through hyperparameter optimization, while BEM is applied using boundary discretization. Both methods are evaluated in terms of solution accuracy and computation time. We conducted numerical experiments by varying the number of boundary integration points for the BEM and the number of hidden layers and neurons per layer for the PINNs. We performed a hyperparameter tuning to identify an adequate PINN configuration for this problem as a network with 3 hidden layers and 25 neurons per layer, using a learning rate of $10^{-2}$ and a sine activation function. At comparable levels of accuracy, the assembly and solution of the BEM system required a computational time on the order of $10^{-2}$~s, whereas the traini

## 11. Physics-Informed Neural Networks in Aerospace Engineering: A Systematic Review of Architectures, Training Strategies, and Open Challenges

- year: 2026 | venue: Applied Sciences | tier: B | relevance: 14 | citations: 0
- doi: 10.3390/app16136282 | key: `doi:10.3390/app16136282`
- source: Q1

**Abstract**: This paper provides a systematic synthesis of recent developments in physics-informed neural networks (PINNs) applied to aerospace engineering, with an emphasis on their role in physically consistent surrogate modeling, forward simulation, and inverse parameter estimation. Using a PRISMA-based methodology, the study surveys peer-reviewed works published between 2017 and 2025 across aviation- and space-related domains, including aerodynamics, structural mechanics, aeroelasticity, propulsion, control, structural health monitoring, satellite-orbit prediction, space-debris collision avoidance, and spacecraft radiation-impact modeling. The analysis shows that embedding governing equations, boundary conditions, and observational data into composite loss functions enables PINNs to improve predictive consistency, reduce dependence on dense simulation or experimental datasets, and support parameter identification under sparse or noisy measurements. Attention is given to architectural variants such as XPINNs, cPINNs, gPINNs, operator-learning approaches, and hybrid PINN-CFD/FEM formulations, as well as to training strategies based on adaptive sampling, domain decomposition, transfer learning

## 12. A Sequential Meta-Transfer (SMT) Learning to Combat Complexities of Physics-Informed Neural Networks: Application to Composites Autoclave Processing

- year: 2023 | venue: arXiv (Cornell University) | tier: B | relevance: 14 | citations: 0
- doi: 10.48550/arxiv.2308.06447 | key: `doi:10.48550/arxiv.2308.06447`
- source: Q3

**Abstract**: Physics-Informed Neural Networks (PINNs) have gained popularity in solving nonlinear partial differential equations (PDEs) via integrating physical laws into the training of neural networks, making them superior in many scientific and engineering applications. However, conventional PINNs still fall short in accurately approximating the solution of complex systems with strong nonlinearity, especially in long temporal domains. Besides, since PINNs are designed to approximate a specific realization of a given PDE system, they lack the necessary generalizability to efficiently adapt to new system configurations. This entails computationally expensive re-training from scratch for any new change in the system. To address these shortfalls, in this work a novel sequential meta-transfer (SMT) learning framework is proposed, offering a unified solution for both fast training and efficient adaptation of PINNs in highly nonlinear systems with long temporal domains. Specifically, the framework decomposes PDE's time domain into smaller time segments to create "easier" PDE problems for PINNs training. Then for each time interval, a meta-learner is assigned and trained to achieve an optimal initia

## 13. Physics-Informed Deep Learning Approaches for Industrial Heat Exchangers

- year: 2025 | venue:  | tier: B | relevance: 14 | citations: 0
- doi: 10.1201/9781032688121-6 | key: `doi:10.1201/9781032688121-6`
- source: Q3

**Abstract**: Mathematical modeling has been used for design, optimization and control of manufacturing processes. While rigorous physics-based models have been employed for process and equipment design and for offline process optimization, their utility for real-time manufacturing operations is rather limited due to their complexity and high computational demands. Data-driven models, on the other hand, have been used for improving the efficiency of manufacturing operations through monitoring, diagnosis, online optimization and control, leveraging the availability of vast amounts of data generated in a manufacturing plant. However, their performance is strongly influenced by the availability and quality of data. They may also predict results that may or may not obey the fundamental physical laws. Physics-informed deep learning (PIDL) is emerging as a new modeling framework to combine physics-based and data-driven models for overcoming the limitations and for taking advantage of both these modeling approaches. Recent work on various PIDL approaches like physics-informed neural networks (PINNs), domain decomposition and transfer learning of PINNs, hypernetwork-based PINNs for adapting the models e

## 14. Self-Evolving Multi-Modal Digital Twin System Using Reinforcement-Driven Physics-Informed Neural Networks (RPINN) for Sustainable Advanced Manufacturing

- year: 2026 | venue:  | tier: B | relevance: 14 | citations: 0
- doi: 10.55306/cjamc.2026.010101 | key: `doi:10.55306/cjamc.2026.010101`
- source: Q3

**Abstract**: The need to optimize manufacturing and ensure its sustainability has increased the pace of implementing digital twins in real-time monitoring, optimization, and control of manufacturing processes. Nevertheless, the majority of the current digital twins are built on a fixed data-driven model, which lacks flexibility, has difficulties with multimodal data integration, and does not provide physical consistency with changing operating conditions. Physicsinformed neural networks (PINNs) are partially satisfying to physical fidelity but are constrained by their fixed training schemes and inability to adapt to changing process dynamics. To fill this gap, this paper suggests a self-evolving multi-mode digital twin solution, which is based on reinforcement-based physics-informed neural networks (R-PINN) in sustainable high-end manufacturing. The suggested system is based on multimodal sensor data, physical laws, and reinforcement learning that will allow the digital twin to self-adapt continuously when production conditions alter. Reinforcement learning is a set of dynamically optimizing the parameters of PINN and control policies to reduce the consumption of energy, the error in prediction

## 15. PHYSICS-INFORMED NEURAL NETWORKS FOR SOLVING SECOND-ORDER BOUNDARY VALUE PROBLEMS: A COMPARATIVE STUDY WITH FEM AND FINITE DIFFERENCE METHODS

- year: 2026 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: B | relevance: 14 | citations: 0
- doi: 10.5281/zenodo.19424818 | key: `doi:10.5281/zenodo.19424818`
- source: Q3

**Abstract**: Physics-Informed Neural Networks (PINNs) have emerged as a powerful paradigm for solving partial differential equations (PDEs) by embedding physical laws directly into the neural network training process. This paper presents a comprehensive comparative study of PINNs against traditional numerical methods—Finite Element Method (FEM) and Finite Difference (FD)—for solving second-order boundary value problems. We focus on the canonical problem on the domain with Dirichlet boundary conditions and , which admits the exact analytical solution . The PINN architecture employs a trial solution formulation that automatically satisfies boundary conditions, utilizes automatic differentiation for computing derivatives, and leverages the L-BFGS optimizer with Sobol quasi-random collocation points. We provide rigorous mathematical derivations of the PINN loss function, trial solution construction, automatic differentiation chain rules, FEM weak formulation with stiffness matrix assembly, and FD central difference schemes. Numerical experiments demonstrate that PINNs achieve comparable accuracy to FEM and FD methods while offering mesh-free flexibility and the ability to incorporate physical const

## 16. PHYSICS-INFORMED NEURAL NETWORKS FOR SOLVING SECOND-ORDER BOUNDARY VALUE PROBLEMS: A COMPARATIVE STUDY WITH FEM AND FINITE DIFFERENCE METHODS

- year: 2026 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: B | relevance: 14 | citations: 0
- doi: 10.5281/zenodo.19414830 | key: `doi:10.5281/zenodo.19414830`
- source: Q3

**Abstract**: Physics-Informed Neural Networks (PINNs) have emerged as a powerful paradigm for solving partial differential equations (PDEs) by embedding physical laws directly into the neural network training process. This paper presents a comprehensive comparative study of PINNs against traditional numerical methods—Finite Element Method (FEM) and Finite Difference (FD)—for solving second-order boundary value problems. We focus on the canonical problem on the domain with Dirichlet boundary conditions and , which admits the exact analytical solution . The PINN architecture employs a trial solution formulation that automatically satisfies boundary conditions, utilizes automatic differentiation for computing derivatives, and leverages the L-BFGS optimizer with Sobol quasi-random collocation points. We provide rigorous mathematical derivations of the PINN loss function, trial solution construction, automatic differentiation chain rules, FEM weak formulation with stiffness matrix assembly, and FD central difference schemes. Numerical experiments demonstrate that PINNs achieve comparable accuracy to FEM and FD methods while offering mesh-free flexibility and the ability to incorporate physical const

## 17. PHYSICS-INFORMED NEURAL NETWORKS FOR SOLVING SECOND-ORDER BOUNDARY VALUE PROBLEMS: A COMPARATIVE STUDY WITH FEM AND FINITE DIFFERENCE METHODS

- year: 2026 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: B | relevance: 14 | citations: 0
- doi: 10.5281/zenodo.19414831 | key: `doi:10.5281/zenodo.19414831`
- source: Q3

**Abstract**: Physics-Informed Neural Networks (PINNs) have emerged as a powerful paradigm for solving partial differential equations (PDEs) by embedding physical laws directly into the neural network training process. This paper presents a comprehensive comparative study of PINNs against traditional numerical methods—Finite Element Method (FEM) and Finite Difference (FD)—for solving second-order boundary value problems. We focus on the canonical problem on the domain with Dirichlet boundary conditions and , which admits the exact analytical solution . The PINN architecture employs a trial solution formulation that automatically satisfies boundary conditions, utilizes automatic differentiation for computing derivatives, and leverages the L-BFGS optimizer with Sobol quasi-random collocation points. We provide rigorous mathematical derivations of the PINN loss function, trial solution construction, automatic differentiation chain rules, FEM weak formulation with stiffness matrix assembly, and FD central difference schemes. Numerical experiments demonstrate that PINNs achieve comparable accuracy to FEM and FD methods while offering mesh-free flexibility and the ability to incorporate physical const

## 18. Development of a surrogate model for uncertainty quantification of compressor performance due to manufacturing tolerance

- year: 2023 | venue: Journal of the Global Power and Propulsion Society | tier: B | relevance: 13 | citations: 5
- doi: 10.33737/jgpps/168293 | key: `doi:10.33737/jgpps/168293`
- source: Q1

**Abstract**: In gas turbines and jet engines, stagger angle and tip gap variations between adjacent blades lead to the deterioration of performance. To evaluate the effect of manufacturing tolerance on performance, a CFD-based uncertainty quantification analysis is performed in this work. However, evaluating dozens of thousands of rotor assembly through CFD simulations would be computationally prohibitive. A surrogate model is thus developed to predict compressor performance given an ordered set of manufactured blades. The model is used to predict the influence of tip gap and stagger angle variations on maximum isentropic efficiency. The results confirm that the best arrangement is obtained by minimizing the stagger angle variation between adjacent blades, and by maximizing the tip gap variation. Another finding is that the best arrangement yields the lowest variability, the range of maximum efficiency being 4 times sharper (resp. 2 times) than worst arrangement for stagger angle variations (resp. tip gap variations). Not measuring manufacturing tolerance, or not specifying any strategy for the blade arrangement, lead to variability as large as the worst arrangement.

## 19. Stochastic analysis of heterogeneous porous material with modified neural architecture search (NAS) based physics-informed neural networks using transfer learning

- year: 2020 | venue: arXiv (Cornell University) | tier: B | relevance: 13 | citations: 5
- doi: 10.48550/arxiv.2010.12344 | key: `doi:10.48550/arxiv.2010.12344`
- source: Q3

**Abstract**: In this work, a modified neural architecture search method (NAS) based physics-informed deep learning model is presented for stochastic analysis in heterogeneous porous material. Monte Carlo method based on a randomized spectral representation is first employed to construct a stochastic model for simulation of flow through porous media. To solve the governing equations for stochastic groundwater flow problem, we build a modified NAS model based on physics-informed neural networks (PINNs) with transfer learning in this paper that will be able to fit different partial differential equations (PDEs) with less calculation. The performance estimation strategies adopted is constructed from an error estimation model using the method of manufactured solutions. A sensitivity analysis is performed to obtain the prior knowledge of the PINNs model and narrow down the range of parameters for search space and use hyper-parameter optimization algorithms to further determine the values of the parameters. Further the NAS based PINNs model also saves the weights and biases of the most favorable architectures, then used in the fine-tuning process. It is found that the log-conductivity field using Gaus

## 20. Physics-informed neural networks for transformed geometries and manifolds

- year: 2023 | venue: arXiv (Cornell University) | tier: A | relevance: 13 | citations: 3
- doi: 10.48550/arxiv.2311.15940 | key: `doi:10.48550/arxiv.2311.15940`
- source: Q3

**Abstract**: Physics-informed neural networks (PINNs) effectively embed physical principles into machine learning, but often struggle with complex or alternating geometries. We propose a novel method for integrating geometric transformations within PINNs to robustly accommodate geometric variations. Our method incorporates a diffeomorphism as a mapping of a reference domain and adapts the derivative computation of the physics-informed loss function. This generalizes the applicability of PINNs not only to smoothly deformed domains, but also to lower-dimensional manifolds and allows for direct shape optimization while training the network. We demonstrate the effectivity of our approach on several problems: (i) Eikonal equation on Archimedean spiral, (ii) Poisson problem on surface manifold, (iii) Incompressible Stokes flow in deformed tube, and (iv) Shape optimization with Laplace operator. Through these examples, we demonstrate the enhanced flexibility over traditional PINNs, especially under geometric variations. The proposed framework presents an outlook for training deep neural operators over parametrized geometries, paving the way for advanced modeling with PDEs on complex geometries in scie

## 21. Tolerance-Aware Deep Optics

- year: 2025 | venue: arXiv (Cornell University) | tier: A | relevance: 13 | citations: 2
- doi: 10.48550/arxiv.2502.04719 | key: `doi:10.48550/arxiv.2502.04719`
- source: Q1

**Abstract**: Deep optics has emerged as a promising approach by co-designing optical elements with deep learning algorithms. However, current research typically overlooks the analysis and optimization of manufacturing and assembly tolerances. This oversight creates a significant performance gap between designed and fabricated optical systems. To address this challenge, we present the first end-to-end tolerance-aware optimization framework that incorporates multiple tolerance types into the deep optics design pipeline. Our method combines physics-informed modelling with data-driven training to enhance optical design by accounting for and compensating for structural deviations in manufacturing and assembly. We validate our approach through computational imaging applications, demonstrating results in both simulations and real-world experiments. We further examine how our proposed solution improves the robustness of optical systems and vision algorithms against tolerances through qualitative and quantitative analyses. Code and additional visual results are available at openimaginglab.github.io/LensTolerance.

## 22. Physics-Informed Tolerance Allocation: A Surrogate-Based Framework for the Control of Geometric Variation on System Performance

- year: 2019 | venue:  | tier: A | relevance: 13 | citations: 2
- doi: — | key: `t:physicsinformedtoleranceallocationasurrogatebasedframeworkforthecontrolofgeometr`
- source: S2-Q1

**Abstract**: In this paper, we present a novel tolerance allocation algorithm for the assessment and control of geometric variation on system performance that is applicable to any system of partial differential equations. In particular, we parameterize the geometric domain of the system in terms of design parameters and subsequently measure the effect of design parameter variation on system performance. A surrogate model via a tensor representation is constructed to map the design parameter variation to the system performance. A set of optimization problems over this surrogate model restricted to nested hyperrectangles represents the effect of prescribing design tolerances, where the maximizer of this restricted function depicts the worst-case member, i.e. the worst-case design. Moreover, the loci of these tolerance hyperrectangles with maximizers attaining, but not surpassing, the performance constraint represents the boundary to the feasible region of allocatable tolerances. Every tolerance in this domain is measured through a user-specified, weighted norm which is informed by design considerations such as cost and manufacturability. The boundary of the feasible set is elucidated as an immers

## 23. Alikhanov-XfPINNs: Adaptive Physics-Informed Learning for Nonlinear Fractional PDEs on Nonuniform Meshes

- year: 2026 | venue: arXiv (Cornell University) | tier: A | relevance: 13 | citations: 0
- doi: — | key: `t:alikhanovxfpinnsadaptivephysicsinformedlearningfornonlinearfractionalpdesonnonun`
- source: Q1

**Abstract**: To address the initial singularity inherent in solutions to fractional partial differential equations (fPDEs), we propose an accelerated Alikhanov discretization formulation implemented on nonuniform time grids. Based on the physics-informed neural networks (PINNs) framework, we introduce an Alikhanov-extended fractional PINNs (XfPINNs) architecture that combines high-order temporal discretization and deep learning. The nonlocal memory term in fPDEs leads to high computational cost, while the weak singularity near $t\to 0^+$ can deteriorate accuracy on uniform meshes. To separate temporal discretization effects from optimization and sampling errors, we further develop an auxiliary time-marching configuration that enables auditable temporal-convergence studies under controlled training tolerances. This architecture can solve general nonlinear fPDEs. The XfPINNs approach is designed for forward and inverse problems, allowing for data-driven solution reconstruction and parameter estimation. First, the neural network approximates the solution of nonlinear fPDEs; then, an adaptive activation function accelerates convergence and enhances training efficiency. The optimization framework em

## 24. Alikhanov-XfPINNs: Adaptive Physics-Informed Learning for Nonlinear Fractional PDEs on Nonuniform Meshes

- year: 2026 | venue: arXiv (Cornell University) | tier: A | relevance: 13 | citations: 0
- doi: 10.48550/arxiv.2605.01305 | key: `doi:10.48550/arxiv.2605.01305`
- source: Q1

**Abstract**: To address the initial singularity inherent in solutions to fractional partial differential equations (fPDEs), we propose an accelerated Alikhanov discretization formulation implemented on nonuniform time grids. Based on the physics-informed neural networks (PINNs) framework, we introduce an Alikhanov-extended fractional PINNs (XfPINNs) architecture that combines high-order temporal discretization and deep learning. The nonlocal memory term in fPDEs leads to high computational cost, while the weak singularity near $t\to 0^+$ can deteriorate accuracy on uniform meshes. To separate temporal discretization effects from optimization and sampling errors, we further develop an auxiliary time-marching configuration that enables auditable temporal-convergence studies under controlled training tolerances. This architecture can solve general nonlinear fPDEs. The XfPINNs approach is designed for forward and inverse problems, allowing for data-driven solution reconstruction and parameter estimation. First, the neural network approximates the solution of nonlinear fPDEs; then, an adaptive activation function accelerates convergence and enhances training efficiency. The optimization framework em

## 25. Temperature Field Prediction and Convection Coefficient Estimation from Temperature Data Using PINNs

- year: 2026 | venue: Lecture notes in production engineering | tier: B | relevance: 13 | citations: 0
- doi: 10.1007/978-3-032-01194-7_36 | key: `doi:10.1007/978-3-032-01194-7_36`
- source: Q1

**Abstract**: Abstract Thermal deformation is a critical factor affecting the precision of machine tools, requiring accurate thermal modeling to predict temperature fields and thermal parameters. Traditional approaches, such as the Finite Element Method (FEM), require well-defined boundary conditions, which are often unknown or difficult to measure in real machining environments. This paper explores the use of Physics-informed neural networks (PINNs) as an alternative method for solving steady-state heat conduction problems in two dimensions. PINNs integrate sparse sensor data with physical laws, enabling temperature field prediction and convection coefficient estimation without the need for fully specified boundary conditions. We evaluate five different PINN models, varying the balance between data-driven and physics-informed constraints. Results show that enforcing the heat equation alone yields high accuracy in temperature prediction, but accurate convection coefficient estimation requires explicit enforcement of convection conditions. While PINNs successfully infer missing parameters, their sensitivity to temperature gradients can impact accuracy. Additionally, the need for retraining PINNs 

## 26. A Hyper Physics-Informed Neural Network for Predicting Heat Transfer Patterns During the Curing Process in Aerospace Composite Manufacturing

- year: 2024 | venue:  | tier: B | relevance: 13 | citations: 0
- doi: 10.1115/imece2024-144949 | key: `doi:10.1115/imece2024-144949`
- source: Q3

**Abstract**: Abstract The importance of fast and accurate process simulation is crucial in various manufacturing settings to enable both design experimentation and real-time monitoring and control. Traditional numerical simulations, however, are often too slow and computationally demanding for real-time applications. Physics-Informed Neural Networks (PINN) offer a promising alternative but struggle with dynamic prediction and generalization due to the need for retraining with any change in system configurations. To overcome this, Hypernetwork-based PINN (HyperPINN) has been developed. HyperPINN utilizes a secondary neural network to generate necessary weights for the primary PINN network based on input system configurations, thus avoiding retraining for different conditions. This paper showcases the use of HyperPINN in simulating the heat transfer patterns of a curing process for aerospace-grade composites. The process involves modeling transient heat transfer in a one-dimensional composite part. The Hypernetwork and the primary PINN are jointly trained across various system configurations, allowing the Hypernetwork to dynamically adjust PINN parameters as per the current conditions while maint

## 27. Accelerating Electrodeposition Simulation Using Physics Informed Neural Networks

- year: 2025 | venue: Language arts journal of Michigan | tier: B | relevance: 13 | citations: 0
- doi: — | key: `t:acceleratingelectrodepositionsimulationusingphysicsinformedneuralnetworks`
- source: Q3

**Abstract**: Electrodeposition plays a vital role in processes such as electrochemical additive manufacturing (ECAM) and electroplating, where precise control over operating conditions, such as current density, deposit thickness and electrolyte concentration is crucial to achieving desirable mechanical and structural properties. Given the vast number of independent variables available for the process of electrodeposition, traditional methods of experimentation and simulation are often time-consuming, costly, and prone to inaccuracies, limiting their usefulness in optimizing electrodeposition parameters. This study investigates the application of machine learning (ML) models, specifically data-driven artificial neural networks (ANNs), simulation-based physics-informed neural networks (PINNs), and hybrid PINNs (combining experimental data with simulation parameters and physics laws), to accelerate and enhance the accuracy of electrodeposition parameter predictions. Baseline data was generated from a potentiostatic electrodeposition experiment and simulation models incorporating Fick’s Second Law and Faraday’s Law. Data-driven ANNs utilized experimental data, simulation-based PINNs integrated simu

## 28. Finite element and physics-informed neural network fusion for elasticity mechanics solving techniques

- year: 2025 | venue:  | tier: B | relevance: 13 | citations: 0
- doi: 10.1117/12.3085008 | key: `doi:10.1117/12.3085008`
- source: Q3

**Abstract**: Simulation of linear elasticity problems is widely applied in mechanical and architectural engineering, and surrogate models driven by sample data have become an effective approach to perform fast simulations. However, due to the scarcity and high cost of data in engineering, traditional data-driven surrogate models suffer from low accuracy. This paper proposes a novel approach combining the finite element method (FEM) with physics-informed neural networks (PINN) based on the principle of minimum potential energy (PINN-MPEP) for solving elasticity mechanics problems. Traditional FEM relies on mesh discretization, matrix assembly, and numerical solution of algebraic systems, but it is computationally expensive, especially for large-scale and complex structures. PINN, a deep learning-based technique, has gained attention for solving partial differential equations (PDEs) without explicit mesh construction. However, PINN faces challenges such as slow convergence and accuracy limitations when applied to complex problems. To overcome these challenges, we introduce the PINN-MPEP method, which integrates the minimum potential energy principle as a physical constraint into the PINN framewor

## 29. Zone-based Physics-Informed Neural Network (Z-PINN) for Addressing Data Scarcity in Ceramic Sintering Processes

- year: 2025 | venue:  | tier: B | relevance: 13 | citations: 0
- doi: 10.1109/ictc66702.2025.11387909 | key: `doi:10.1109/ictc66702.2025.11387909`
- source: Q3

**Abstract**: Recent advances in artificial intelligence have enabled predictive modeling and control in manufacturing processes. However, industrial datasets often suffer from missing entries and limited availability due to sensor limitations, failures, and high installation costs. Physics-Informed Neural Networks (PINNs) incorporate physical laws into the learning process, offering physically consistent predictions, but their performance deteriorates in complex processes when relying on a single global partial differential equation (PDE) or ordinary differential equation (ODE). To address this limitation, we propose a Zone-based PINN (Z-PINN) framework that divides the process timeline into multiple zones based on a predefined ceramic sintering schedule and trains a separate PINN for each zone. Without modifying the original PINN structure, this approach allows localized learning and improves prediction accuracy while ensuring physical consistency. We evaluate Z-PINN on real ceramic sintering data under three scenarios: short-term missing values, long-term missing values, and full sequence generation from minimal initial inputs. Experimental results show that Z-PINN significantly outperforms t

## 30. Two step training a single physics-informed neural network for solving Navier Stokes equations with various boundary conditions

- year: 2025 | venue: Manufacturing Letters | tier: B | relevance: 13 | citations: 0
- doi: 10.1016/j.mfglet.2025.06.009 | key: `doi:10.1016/j.mfglet.2025.06.009`
- source: Q3

**Abstract**: Physics-Informed Neural Networks (PINNs) are a popular scientific machine learning framework used to solve partial differential equations (PDEs). One of the common applications of PINNs is in solving fluid flow problems using the Navier–Stokes (NS) equations. The NS equations are a set of PDEs that describe the flow of a viscous fluid and have been extensively applied in manufacturing problems, such as modeling flow in injection molding or the flow of molten metal in additive manufacturing. Solving a single PINN with various boundary conditions requires training a unified model to predict the flow field for each specific boundary condition setup. This poses a challenge in training PINNs due to the limited number of samples that can be taken from the parametric space corresponding to various boundary conditions, often leading to poor-quality solutions. To address this, we propose a two-step solution to solve PINNs for the Navier–Stokes equations with various boundary conditions. The proposed method enables PINNs to learn effectively both from the domain and from parametric spaces. This two-step approach provides the model with a finer initial understanding of the domain space and th

## 31. Physics Informed Neural Networks (PINN) for Low Snr Magnetic Resonance Electrical Properties Tomography (MREPT)

- year: 2022 | venue: Diagnostics | tier: B | relevance: 12 | citations: 16
- doi: 10.3390/diagnostics12112627 | key: `doi:10.3390/diagnostics12112627`
- source: Q1

**Abstract**: Electrical properties (EPs) of tissues facilitate early detection of cancerous tissues. Magnetic resonance electrical properties tomography (MREPT) is a technique to non-invasively probe the EPs of tissues from MRI measurements. Most MREPT methods rely on numerical differentiation (ND) to solve partial differential Equations (PDEs) to reconstruct the EPs. However, they are not practical for clinical data because ND is noise sensitive and the MRI measurements for MREPT are noisy in nature. Recently, Physics informed neural networks (PINNs) have been introduced to solve PDEs by substituting ND with automatic differentiation (AD). To the best of our knowledge, it has not been applied to MREPT due to the challenges in using PINN on MREPT as (i) a PINN requires part of ground-truth EPs as collocation points to optimize the network's AD, (ii) the noisy input data disrupts the optimization of PINNs despite the noise-filtering nature of NNs and additional denoising processes. In this work, we propose a PINN-MREPT model based on a canonical analytic MREPT model. A reference padding layer with known EPs was added to surround the region of interest for providing additive collocation points. M

## 32. Physics-Informed Neural Networks in Aerospace: A Structured Taxonomy with Literature Review

- year: 2025 | venue: Challenges and Issues of Modern Science | tier: B | relevance: 12 | citations: 5
- doi: 10.15421/cims.4.313 | key: `doi:10.15421/cims.4.313`
- source: Q1

**Abstract**: Purpose. This study aims to develop a structured four-tier taxonomy that systematically organizes aerospace engineering tasks suitable for the application of Physics-Informed Neural Networks (PINNs), while validating this classification through a literature review and identifying opportunities for future research. Design / Method / Approach. The methodology involves grouping tasks into four distinct tiers—Physical Modeling, Dynamic Analysis, Functional Assessment, and System-Level Assessment—based on their physical, operational, and systemic characteristics. This framework is subsequently populated with real-world examples derived from the analysis of 145 peer-reviewed studies. Findings. The reviewed literature confirms a balanced distribution of PINNs applications across all tiers. Contrary to initial assumptions, studies were identified even in areas previously presumed underrepresented, such as acoustic modeling, optical simulations, and environmental impact assessment. This outcome reveals the broader applicability of PINNs and calls for a reassessment of current assumptions regarding underexplored domains. Theoretical Implications. The proposed taxonomy offers a coherent frame

## 33. A modular coupled physics-informed neural network framework for urban flood prediction

- year: 2026 | venue: Journal of Water and Climate Change | tier: B | relevance: 12 | citations: 3
- doi: 10.2166/wcc.2026.311 | key: `doi:10.2166/wcc.2026.311`
- source: Q3

**Abstract**: ABSTRACT Urban pluvial flooding driven by localized extreme rainfall increasingly exceeds the capacity of metropolitan drainage systems. Manhole surcharge overflow interacting with surface runoff produces complex inundation dynamics that are difficult to capture in real time. High-fidelity 1D–2D coupled numerical models are too computationally expensive for operational deployment, whereas purely data-driven deep-learning surrogates, although fast, do not enforce conservation laws or provide physically interpretable behaviour. We propose a modular coupled physics-informed neural network (MC-PINN) that bridges this gap. MC-PINN consists of a 1D PINN for sewer network flow governed by the Saint-Venant equations and a 2D PINN for surface flow governed by shallow-water equations, coupled through manhole overflow acting as a boundary condition. Mass continuity is enforced at the interface and momentum is strongly constrained via physics-based residual losses, enabling a hybrid surrogate with near real-time inference potential. To demonstrate feasibility, we present a manufactured-solution proof-of-concept in which a 1D advection PINN and a 2D diffusion PINN are coupled via a shared inter

## 34. Physics-informed neural networks for solving thermo-mechanics problems\n of functionally graded material

- year: 2021 | venue: arXiv (Cornell University) | tier: B | relevance: 12 | citations: 2
- doi: 10.48550/arxiv.2111.10751 | key: `doi:10.48550/arxiv.2111.10751`
- source: Q3

**Abstract**: Differential equations are indispensable to engineering and hence to\ninnovation. In recent years, physics-informed neural networks (PINN) have\nemerged as a novel method for solving differential equations. PINN method has\nthe advantage of being meshless, scalable, and can potentially be intelligent\nin terms of transferring the knowledge learned from solving one differential\nequation to the other. The exploration in this field has majorly been limited\nto solving linear-elasticity problems, crack propagation problems. This study\nuses PINNs to solve coupled thermo-mechanics problems of materials with\nfunctionally graded properties. An in-depth analysis of the PINN framework has\nbeen carried out by understanding the training datasets, model architecture,\nand loss functions. The efficacy of the PINN models in solving thermo-mechanics\ndifferential equations has been measured by comparing the obtained solutions\neither with analytical solutions or finite element method-based solutions.\nWhile R2 score of more than 99% has been achieved in predicting primary\nvariables such as displacement and temperature fields, achieving the same for\nsecondary variables such as stress turns ou

## 35. On Covariance Estimation in Physics Informed Neural Networks for Orbit Determination

- year: 2025 | venue:  | tier: B | relevance: 12 | citations: 2
- doi: 10.5194/egusphere-egu25-11680 | key: `doi:10.5194/egusphere-egu25-11680`
- source: Q3

**Abstract**: Artificial intelligence (AI), particularly machine learning (ML), is widely applied in fields such as medicine, autonomous driving, and manufacturing. Over time, ML has also seen increasing use in space and geosciences, where its algorithms hold the potential to enhance orbit prediction and orbit determination (OD) by utilizing measurement data. However, ML models like Artificial Neural Networks (ANNs) are limited to problems with abundant data and are often considered "black boxes", as their predictions lack interpretability in a scientifically meaningful way. To address these challenges, Raissi et al. 2018 introduced Physics Informed Neural Networks (PINNs), a specialized type of ANN. PINNs integrate the governing differential equations of a system into the learning process, imposing a physical constraint on the network's training and predictions. This approach allows effective training with small datasets, removing the reliance on large amounts of measurements. Additionally, PINNs can estimate unknown or poorly defined parameters within the differential equations, making them conceptually similar to classical OD algorithms like the Weighted Least Squares method. Building on this

## 36. Acoustic Field Reconstruction in Tubes via Physics-Informed Neural Networks

- year: 2025 | venue:  | tier: A | relevance: 12 | citations: 1
- doi: 10.61782/fa.2025.0074 | key: `doi:10.61782/fa.2025.0074`
- source: Q1

**Abstract**: This study investigates the application of Physics-Informed Neural Networks (PINNs) to inverse problems in acoustic tube analysis, focusing on reconstructing acoustic fields from noisy and limited observation data.Specifically, we address scenarios where the radiation model is unknown, and pressure data is only available at the tube's radiation end.A PINNs framework is proposed to reconstruct the acoustic field, along with the PINN Fine-Tuning Method (PINN-FTM) and a traditional optimization method (TOM) for predicting radiation model coefficients.The results demonstrate that PINNs can effectively reconstruct the tube's acoustic field under noisy conditions, even with unknown radiation parameters.PINN-FTM outperforms TOM by delivering balanced and reliable predictions and exhibiting robust noise-tolerance capabilities.

## 37. Physics-informed machine learning for material characterization: A perspective on data-efficient discovery through physics-informed neural networks

- year: 2025 | venue: International Journal of AI for Materials and Design | tier: B | relevance: 12 | citations: 1
- doi: 10.36922/ijamd025440043 | key: `doi:10.36922/ijamd025440043`
- source: Q3

**Abstract**: Accurate characterization of material properties is critical for modeling and optimizing advanced systems, yet conventional experimental and simulation-based approaches remain costly and data-intensive. As artificial intelligence evolves from data-driven modeling to physics-informed and knowledge-guided paradigms, this perspective article highlights the role of physics-informed machine learning (PIML), specifically physics-informed neural networks (PINNs), as a key enabler of data-efficient, physically consistent inference. PINNs embed governing equations into the learning process and have demonstrated strong capability in recovering constitutive and transport parameters from sparse or noisy data while preserving physical fidelity. This paper examines the fundamental structure, workflow integration, and recent advances of PINNs in the context of inverse material characterization. It also discusses open challenges in computational cost, training stability, and uncertainty quantification. Looking forward, integration with digital twins, generative modeling, and autonomous experimentation presents a pathway toward interpretable, adaptive, and automated characterization for next-genera

## 38. Genetic algorithm–optimized loss balancing in physics-informed neural networks for manufacturing digital twin applications

- year: 2026 | venue: Journal of Intelligent Manufacturing and Special Equipment | tier: B | relevance: 12 | citations: 1
- doi: 10.1108/jimse-04-2026-0016 | key: `doi:10.1108/jimse-04-2026-0016`
- source: Q3

**Abstract**: Purpose This study addresses a key limitation in physics-informed neural networks (PINNs), namely the reliance on manually selected or heuristically tuned loss weights governing the balance between data fidelity, physics residuals and boundary constraints. Improper weighting often leads to instability, poor reproducibility and sensitivity to user expertise, particularly in manufacturing-oriented thermal modelling and digital twin applications. Design/methodology/approach A genetic algorithm (GA)-based meta-optimization framework is proposed to automate the selection of normalized loss weights in PINNs. The GA operates as an offline optimization layer, while the inner PINN enforces the governing partial differential equations. A composite fitness function evaluates candidate weight configurations using physics consistency, data agreement and boundary-condition satisfaction. The framework is validated using a two-dimensional transient heat-conduction problem with a moving Gaussian heat source representative of laser-based manufacturing processes under noisy data conditions. Comparative analysis is performed against fixed-weight and adaptive-weight PINN strategies. Findings The propos

## 39. Acoustic Field Reconstruction in Tubes via Physics-Informed Neural Networks

- year: 2025 | venue: arXiv (Cornell University) | tier: A | relevance: 12 | citations: 0
- doi: 10.48550/arxiv.2505.12557 | key: `doi:10.48550/arxiv.2505.12557`
- source: Q1

**Abstract**: This study investigates the application of Physics-Informed Neural Networks (PINNs) to inverse problems in acoustic tube analysis, focusing on reconstructing acoustic fields from noisy and limited observation data. Specifically, we address scenarios where the radiation model is unknown, and pressure data is only available at the tube's radiation end. A PINNs framework is proposed to reconstruct the acoustic field, along with the PINN Fine-Tuning Method (PINN-FTM) and a traditional optimization method (TOM) for predicting radiation model coefficients. The results demonstrate that PINNs can effectively reconstruct the tube's acoustic field under noisy conditions, even with unknown radiation parameters. PINN-FTM outperforms TOM by delivering balanced and reliable predictions and exhibiting robust noise-tolerance capabilities.

## 40. Leveraging Physics-Informed Neural Networks for Efficient Tolerance Analysis

- year: 2026 | venue: Procedia CIRP | tier: A | relevance: 12 | citations: 0
- doi: 10.1016/j.procir.2026.03.130 | key: `doi:10.1016/j.procir.2026.03.130`
- source: Q1

**Abstract**: The effect of manufacturing-induced deviations on non-geometric Key Characteristics (KC) within the scope of tolerance analysis is determined by the iterative solving of partial or ordinary differential equations. The statistical assurance of the KCs coupled with the computationally expensive evaluation of differential equations results in unacceptably long computation times. Data-driven surrogate models provide a solution to this problem, as they only require the numerical solution of the differential equations for their training and are capable to approximate the solutions after training with low computational effort. However, the accuracy of the predictions of the surrogate model depends on the quantity and quality of information about the system that is considered during its training. Physics-informed neural networks pursue this approach by incorporating physical principles during network training. This additional system knowledge aims to increase prediction accuracy in comparison to purely data-driven approaches. In tolerance analyses, prediction accuracy in the evaluation of non-geometric KCs is crucial. Thus, this paper proposes an approach that incorporates physics-based kn

## 41. Failure-informed PINNs for a multi-strain SVEIR epidemic model

- year: 2026 | venue: Discover Applied Sciences | tier: A | relevance: 12 | citations: 0
- doi: 10.1007/s42452-026-09216-6 | key: `doi:10.1007/s42452-026-09216-6`
- source: Q1

**Abstract**: Abstract Tightly coupled multi-compartment epidemic models tend to expose a weakness of standard Physics-Informed Neural Networks (PINNs). When collocation points are placed uniformly, the network spends much of its capacity on smooth regions while leaving the sharp transients poorly resolved. We work around this by pairing Failure-Informed PINNs (FI-PINNs) with a Self-Adaptive Importance Sampling (SAIS) refinement strategy, and we apply the combination to a nine-equation Susceptible/Vaccinated/Exposed/Infected/Recovered (SVEIR) model that follows three viral strains together with a vaccination compartment. The idea behind the construction is simple. We build a residual-based limit-state function, estimate the failure probability associated with it, and let the network steer its own sampling toward the time intervals where the governing equations are not yet satisfied to within a prescribed tolerance. On the same temporal domain, with identical initial conditions and the same network architecture, SAIS-enhanced FI-PINNs reach a relative $$L_2$$ error of $$1.04\times 10^{-6}$$, against $$7.36\times 10^{-3}$$ for uniform sampling and $$3.42\times 10^{-4}$$ for Residual-Based Adaptive

## 42. Physics-Informed AI for Material Characterization: A Perspective on Data-Efficient Discovery through Physics-Informed Neural Networks

- year: 2025 | venue:  | tier: B | relevance: 12 | citations: 0
- doi: 10.31224/5763 | key: `doi:10.31224/5763`
- source: Q3

**Abstract**: Accurate characterization of material properties is critical for modeling and optimizing advanced systems, yet conventional experimental and simulation-based approaches remain costly and data-intensive. As artificial intelligence (AI) evolves from data-driven modeling to physics-informed and knowledge-guided paradigms, this Perspective highlights the role of physics-informed machine learning (PIML), specifically physics-informed neural networks (PINNs), as a key enabler of data-efficient, physically consistent inference. PINNs embed governing equations into the learning process and have demonstrated strong capability in recovering constitutive and transport parameters from sparse or noisy data while preserving physical fidelity. This Perspective examines the fundamental structure, workflow integration, and recent advances of PINNs in the context of inverse material characterization. It also discusses open challenges in computational cost, training stability, and uncertainty quantification. Looking forward, integration with digital twins, generative modeling, and autonomous experimentation presents a pathway toward interpretable, adaptive, and automated characterization for next-gen

## 43. HyPINO: Multi-Physics Neural Operators via HyperPINNs and the Method of Manufactured Solutions

- year: 2025 | venue:  | tier: B | relevance: 12 | citations: 0
- doi: 10.52202/085713-4845 | key: `doi:10.52202/085713-4845`
- source: Q3

**Abstract**: We present HyPINO, a multi-physics neural operator designed for zero-shot generalization across a broad class of PDEs without requiring task-specific fine-tuning. Our approach combines a Swin Transformer-based hypernetwork with mixed supervision: (i) labeled data from analytical solutions generated via the Method of Manufactured Solutions (MMS), and (ii) unlabeled samples optimized using physics-informed objectives. The model maps PDE parameterizations to target Physics-Informed Neural Networks (PINNs) and can handle linear elliptic, hyperbolic, and parabolic equations in two dimensions with varying source terms, geometries, and mixed Dirichlet/Neumann boundary conditions, including interior boundaries. HyPINO achieves strong zero-shot accuracy on seven benchmark problems from PINN literature, outperforming U-Nets, Poseidon, and Physics-Informed Neural Operators (PINO). Further, we introduce an iterative refinement procedure that treats the residual of the generated PINN as "delta PDE" and performs another forward pass to generate a corrective PINN. Summing their contributions and repeating this process forms an ensemble whose combined solution progressively reduces the error on si

## 44. Towards Sustainable Scientific Machine Learning: Fast and interpretable PDE Solvers via RBF-PIELM

- year: 2025 | venue:  | tier: B | relevance: 12 | citations: 0
- doi: 10.1145/3799830.3799865 | key: `doi:10.1145/3799830.3799865`
- source: Q3

**Abstract**: Partial differential equation (PDE) solvers are fundamental to engineering simulation. Classical mesh-based approaches (finite difference/volume/element) are fast and accurate on high-quality meshes but struggle with higher-order operators and complex, hard-to-mesh geometries. Recently developed physics-informed neural networks (PINNs) and their variants are mesh-free and flexible, yet compute-intensive and often less accurate. This paper systematically benchmarks RBF-PIELM, a rapid PINN variant—an extreme learning machine with radial-basis activations—for higher-order PDEs. RBF-PIELM replaces PINNs’ time-consuming gradient descent with a single-shot least-squares solve. We test RBF-PIELM on the fourth-order biharmonic equation using two benchmarks domains: lid-driven cavity flow (streamfunction formulation) and one manufactured solutions with oscillatory forcing. Additionally, we test RBF-PIELM on the Poisson equation on a 3D gyroidal domain to demonstrate performance in complex geometries. Our results show up to 350 × faster training than PINNs and over 10 × fewer parameters for comparable solution accuracy. Using the Greens Algorithm Methodology, we also calculate a reduction of

## 45. An Efficient Architecture Selection Approach for PINNs Applied to Electromagnetic Problems

- year: 2026 | venue: IEEE transactions on magnetics | tier: A | relevance: 12 | citations: 0
- doi: 10.1109/TMAG.2025.3615791 | key: `doi:10.1109/tmag.2025.3615791`
- source: S2-Q1

**Abstract**: Physics-informed neural networks (PINNs) offer a promising alternative to mitigate difficulties inherent in mesh-based approaches, such as finite-difference (FD) methods, particularly concerning mesh generation times and computational costs for achieving higher accuracies. Since PINNs are mesh-free and provide continuous function representations, they naturally solve these challenges faced by traditional mesh-based methods. However, a major bottleneck in deploying PINNs lies in the cumbersome process of choosing optimal hyperparameters for specific problems and target error tolerances. In this work, we propose and benchmark a hybrid random and grid search approach to tune suitable PINN hyperparameters. Our results in an application example indicate that this approach is more efficient and reliable than conventional grid-based, random-based, or surrogate-guided optimization strategies.

## 46. Self-scalable Tanh (Stan): Faster Convergence and Better Generalization in Physics-informed Neural Networks

- year: 2022 | venue: arXiv (Cornell University) | tier: B | relevance: 11 | citations: 14
- doi: 10.48550/arxiv.2204.12589 | key: `doi:10.48550/arxiv.2204.12589`
- source: Q3

**Abstract**: Physics-informed Neural Networks (PINNs) are gaining attention in the engineering and scientific literature for solving a range of differential equations with applications in weather modeling, healthcare, manufacturing, etc. Poor scalability is one of the barriers to utilizing PINNs for many real-world problems. To address this, a Self-scalable tanh (Stan) activation function is proposed for the PINNs. The proposed Stan function is smooth, non-saturating, and has a trainable parameter. During training, it can allow easy flow of gradients to compute the required derivatives and also enable systematic scaling of the input-output mapping. It is shown theoretically that the PINNs with the proposed Stan function have no spurious stationary points when using gradient descent algorithms. The proposed Stan is tested on a number of numerical studies involving general regression problems. It is subsequently used for solving multiple forward problems, which involve second-order derivatives and multiple dimensions, and an inverse problem where the thermal diffusivity of a rod is predicted with heat conduction data. These case studies establish empirically that the Stan activation function can 

## 47. A Parametric Physics-Informed Deep Learning Method for Probabilistic Design of Thermal Protection Systems

- year: 2023 | venue: Energies | tier: B | relevance: 11 | citations: 11
- doi: 10.3390/en16093820 | key: `doi:10.3390/en16093820`
- source: Q3

**Abstract**: Precise and efficient calculations are necessary to accurately assess the effects of thermal protection system (TPS) uncertainties on aerospacecrafts. This paper presents a probabilistic design methodology for TPSs based on physics-informed neural networks (PINNs) with parametric uncertainty. A typical thermal coating system is used to investigate the impact of uncertainty on the thermal properties of insulation materials and to evaluate the resulting temperature distribution. A sensitivity analysis is conducted to identify the influence of the parameters on the thermal response. The results show that PINNs can produce quick and accurate predictions of the temperature of insulation materials. The accuracy of the PINN model is comparable to that of a response surface surrogate model. Still, the computational time required by the PINN model is only a fraction of the latter. Considering both computational efficiency and accuracy, the PINN model can be used as a high-precision surrogate model to guide the TPS design effectively.

## 48. Predicting the fatigue life of additively manufactured AlSi10Mg alloy using a physics-informed neural network incorporating continuous damage mechanics

- year: 2024 | venue: Proceedings of the Institution of Mechanical Engineers Part B Journal of Engineering Manufacture | tier: B | relevance: 11 | citations: 6
- doi: 10.1177/09544054241290283 | key: `doi:10.1177/09544054241290283`
- source: Q3

**Abstract**: The material characteristics of additively manufactured AlSi10Mg alloy, including the random distribution of process-induced micro defects, microstructual anisotropy, and grain morphologies with complex diversity, poses a significant challenge in accurately predicting its fatigue life, limiting its application in the aircraft field. This work herein introduces a novel approach incorporating a physics-informed neural network (PINN), in which an artificial neural network (ANN) is embedded with a damage mechanics model (CDM) and the critical process parameters of laser powder bed fusion (L-PBF) additive manufacturing. The partial differential equations of the updated CDM model are introduced into the training procedures of the PINN to building a loss function, effectively “teaching” the PINN to learn the physical knowledge. A comparison of the fatigue life prediction results of ANN and the proposed PINN models shows that the PINN model outperforms its counterparts with a 38.71% higher prediction accuracy. The effects of L-PBF process parameters on the fatigue life of as-built AlSi10Mg is examined using both ANN and PINN, proving the better predictive performance and data-physics consi

## 49. Physics-Informed Online Learning for Temperature Prediction in Metal AM

- year: 2024 | venue: Preprints.org | tier: B | relevance: 11 | citations: 6
- doi: 10.20944/preprints202406.0404.v1 | key: `doi:10.20944/preprints202406.0404.v1`
- source: Q3

**Abstract**: In metal additive manufacturing (AM), precise temperature field prediction is crucial for process monitoring, automation, control, and optimization. Traditional methods, primarily offline and data-driven, struggle with adapting to real-time changes and new process scenarios, which limits their applicability for effective AM process control. To address these challenges, this paper introduces the first physics-informed (PI) online learning framework specifically designed for temperature prediction in metal AM. Utilizing a physics-informed neural network (PINN), this framework integrates a neural network architecture with physics-informed inputs and loss functions. Pretrained on a known process to establish a baseline, the PINN transitions to an online learning phase, dynamically updating its weights in response to new, unseen data. This adaptation allows the model to continuously refine its predictions in real-time. By integrating physics-informed components, the PINN leverages prior knowledge about the manufacturing processes, enabling rapid adjustments to process parameters, geometries, deposition patterns, and materials. Empirical results confirm the robust performance of this PI 

## 50. Comprehensive Surrogate-Based Optimization of Lightweight Composite Manufacturing

- year: 2022 | venue: AIAA Journal | tier: B | relevance: 11 | citations: 5
- doi: 10.2514/1.j061075 | key: `doi:10.2514/1.j061075`
- source: Q3

**Abstract**: The problem of holistic manufacturing optimization in lightweight composite applications is considered. The composite manufacturing optimization problem is explored from a holistic perspective that integrates the material constitutive parameters at different scales with the corresponding physics at every processing phase. To efficiently solve the manufacturing optimization problem in high dimensions, a physics-informed neural network surrogate is developed based on the governing first-principles physics. Focus is placed on training a neural network model that spans across all the different scales and physics at each manufacturing phase of the lightweight composite problem such that subsequent optimization results reflect the integrated, multiscale, and multiphysical aspects of the system. A holistic manufacturing optimization paradigm is formulated to discover optimal design vectors embedded in a parameter space of around 70 dimensions. Various objective functions that reflect different design preferences in the manufacturing problem are explored. In one optimization formulation, the final weight (i.e., density) of the composite design is reduced by 8.9% with respect to the nominal
