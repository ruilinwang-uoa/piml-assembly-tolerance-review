# 筛查分块 8（记录 351–400 / 共 449）

## 351. Physics-Guided Few-Shot Anomaly Image Generation for Industrial Inspection

- year: 2026 | venue:  | tier: B | relevance: 5 | citations: 0
- doi: 10.1109/aetcse69203.2026.11504047 | key: `doi:10.1109/aetcse69203.2026.11504047`
- source: Q4

**Abstract**: In industrial manufacturing, defect detection is an essential stage that cannot be compromised. However, there is an immediate barrier in training data-driven models for this task: real anomalous examples are extremely infrequent. In order to close this data gap, academics have suggested a number of synthetic generation techniques; nevertheless, the generated images usually exhibit irrational visual aberrations and flagrantly disregard physical rules. We utilize Physics-Guided Diffusion (PGD) to fill this essential gap. PGD, specifically designed for industrial inspection’s few-shot anomaly generation, compels the diffusion process to adhere to real physical limits. The main method by which it accomplishes this is Decoupled Spatial-Semantic Conditioning (DSSC), which combines learnable embeddings with physical priors, including surface topology gradients, to separate a defect’s spatial footprint from its visual appearance. We also present Denoising-Aware Attention Calibration (DAAC) to maintain the structural soundness of the created anomalies. When DAAC finds structural incompatibilities between the synthetic defect and the background, it dynamically shifts attention instead of ut

## 352. Physics-guided explainable machine learning for multi-response modeling of electrochemical micro-machining using polymer graphite electrodes

- year: 2026 | venue: Scientific Reports | tier: B | relevance: 5 | citations: 0
- doi: 10.1038/s41598-026-46315-1 | key: `doi:10.1038/s41598-026-46315-1`
- source: Q4

**Abstract**: Electrochemical micro-machining (ECMM) enables high-precision fabrication of micro-features in difficult-to-machine materials; however, its strongly nonlinear, multi-physics nature and the high cost of experimentation severely limit reliable data-driven modeling. This study presents a physics-guided machine learning framework for robust multi-response prediction of ECMM performance using polymer graphite electrodes. Controlled experiments were conducted with non-treated and cryogenically treated electrodes, and four critical responses were evaluated: material removal rate (MRR), overcut (Oc), surface roughness (Ra), and taper angle (Ta). Physics-guided descriptors incorporating interaction-driven and severity-based features were constructed to embed mechanistic structure associated with electrochemical excitation and tool-electrolyte-workpiece coupling. Ensemble learning models were trained and rigorously validated using repeated cross-validation. The optimal physics-guided XGBoost models achieved coefficients of determination of 0.817 (MRR), 0.914 (Oc), 0.866 (Ra), and 0.769 (Ta), with corresponding mean absolute errors of 0.013 g/min, 0.026 mm, 0.261 μm, and 0.049°, respectively,

## 353. A Physics-Informed Hybrid and Cascaded Modeling Framework for Device Electrical Prediction

- year: 2026 | venue: IEEE Transactions on Electron Devices | tier: B | relevance: 5 | citations: 0
- doi: 10.1109/ted.2026.3698400 | key: `doi:10.1109/ted.2026.3698400`
- source: Q4

**Abstract**: To address the modeling challenges encountered in a real 12-in CMOS high-volume manufacturing (HVM) environment, where data are scarce and affected by noise and equipment drift, this article proposes a physics-informed hybrid and cascaded learning framework for predicting key device electrical parameters and enabling virtual-manufacturing-based process-window optimization. First, physics-prior models are established for active-region resistance and gate capacitance, and systematic bias is reduced through physics-guided feature augmentation together with machine-learning-based compensation, thereby improving generalization under small-sample conditions. The interpretable intermediate physical quantities derived from the resistance and capacitance modeling paths are then used as bridging variables to construct a cascaded neural network, enabling a stable mapping from process recipes to threshold voltage and saturation drive current. Experimental validation on real fab data demonstrates that the proposed framework outperforms both purely physics-based and purely data-driven methods, achieving test-set MAPEs of 4.90%–6.50% and${R}^{{2}}$values of 0.74–0.90 in final device-level predict

## 354. Machine Learning for Scalable and Generalizable Quality Control in Two-Photon Lithography

- year: 2026 | venue:  | tier: B | relevance: 5 | citations: 0
- doi: 10.7302/dspace/29727 | key: `doi:10.7302/dspace/29727`
- source: Q4

**Abstract**: Two-photon lithography (TPL) is a high-precision additive manufacturing process for fabricating three-dimensional micro- and nano-scale structures. Its successful deployment in scientific and industrial applications critically depends on achieving consistent geometric accuracy and part quality under evolving production conditions. However, current quality control practice in TPL is largely manual and ad hoc, and there is a lack of systematic scalable and generalizable methods. To address this gap, this dissertation develops an integrated, physics-informed, data-driven framework for geometric accuracy modeling, machine health monitoring, and intelligent part quality classification in TPL. First, a hybrid physics-guided modeling approach is proposed to predict and improve geometric accuracy across process parameters and structure designs. Geometric dimensions are decomposed into a global trend, informed by voxel-scale physics and expressed as a function of laser power and scanning rate, and a spatial trend that captures within-sample variability across large structure arrays. A large-scale experimental data consisting of multiple hemisphere sizes and parameter combinations demonstrat

## 355. Physics-Informed Encoded Surrogates for Rapid High-Dof Antenna Synthesis and Inverse Design

- year: 2026 | venue:  | tier: B | relevance: 5 | citations: 0
- doi: 10.1109/dcas69364.2026.11544610 | key: `doi:10.1109/dcas69364.2026.11544610`
- source: Q5

**Abstract**: AI-based methods have been widely investigated for fast antenna performance evaluation and inverse design; nevertheless, challenges remain. Sharp high-$Q$resonant notches make direct regression of sampled$\left|S_{11}\right|$curves unreliable. We address this by a physics-informed encoded-domain$\left|S_{11}\right|$parameterization (baseline plus a few Lorentz-type resonant components) and a FiLM-conditioned multi-branch CNN with a resonance-count head and count-guided peak pruning to suppress spurious notches. Full-space 2-D radiation patterns are difficult to learn because dense angular grids lead to outputdimensionality explosion. We address this by encoding patterns with a low-frequency 2-D DCT coefficient block and regressing the coefficients in the encoded domain. Stable high-DoF multiobjective inverse design is challenging due to combinatorial pixel search and sparse feasibility. We address this by optimizing in a statistically-physically constrained continuous encoded design space and coupling millisecond-level surrogate evaluation with NSGA-II. Full-wave simulations (CST) confirm close agreement with surrogate predictions and demonstrate fast, stable multiobjective inverse

## 356. A closed-loop automated control architecture with physics-informed compensation for springback regulation in aerospace tube bending manufacturing

- year: 2026 | venue:  | tier: B | relevance: 5 | citations: 0
- doi: 10.1117/12.3122441 | key: `doi:10.1117/12.3122441`
- source: Q5

**Abstract**: Springback in aerospace tube bending is a closed-loop control problem; the elastic rebound of the workpiece after tool release represents a systematic output error caused by material nonlinearities and batch-to-batch parametric uncertainties through a conventional fragmented workflow that lacks any feedback path for sensing, compensating, or reporting such errors together. This paper introduces a four-layer closed-loop control structure composed of unified geometry parameterization, automatic Finite Element (FE) solver combination, physics-informed springback correction, and structured quality-reporting system to achieve standardized cross-connections between components through uniform interface specifications without involving any human intervention. The primary algorithms are a physics-informed uncertain compensation module that models the change in elasticity as a bounded disturbance and analytically obtains a first-order feedforward correction of Euler-Bernoulli beam theory to reduce systematic springback underprediction without re-running simulations. The structure of this system uses an independent upgradeable design method at all levels to expose a plain text interface speci

## 357. A mechanism-data fusion framework for process-microstructure prediction and optimization in laser directed energy deposition of Ti-6Al-4V using dual-level surrogate modeling

- year: 2026 | venue: Advanced Equipment | tier: B | relevance: 5 | citations: 0
- doi: 10.55092/ae20260006 | key: `doi:10.55092/ae20260006`
- source: Q5

**Abstract**: The laser-directed energy deposition (L-DED) process involves complex thermal and material interactions, posing challenges for controlling microstructural evolution in metal additive manufacturing. To enable rapid, efficient process optimization, this study develops a physics-informed mechanism-data fusion framework that couples macroscopic finite element method (FEM) and microscopic phase-field method (PFM) with a dual-level long short-term memory (LSTM) neural network. A multiscale physical model is employed to investigate grain growth behavior and the influence of process parameters on microstructural morphology. To map this non-linear temporal evolution, a dual-level data-driven surrogate model is developed. Compared to a conventional multilayer perceptron (MLP), the LSTM effectively captures time-dependent thermal accumulation. In recursive predictions, four initial input layers were identified as the optimal initialization length, enabling stable prediction and mitigating potential layer-wise error propagation, maintaining average R2 values of around 0.95. Using the average grain area as the primary microstructural control target, and incorporating the average grain width, a 

## 358. Röntgen-CT-ondersteunde datagedreven in-procesmonitoring voor metaal- Laser Powder Bed Fusion

- year: 2026 | venue: Lirias | tier: B | relevance: 5 | citations: 0
- doi: — | key: `t:rntgenctondersteundedatagedreveninprocesmonitoringvoormetaallaserpowderbedfusion`
- source: Q5

**Abstract**: Laser Powder Bed Fusion of metals (PBF-LB/M) promises design freedom for critical aerospace and biomedical parts, yet the cost and difficulty of post-build certification constrain its industrial adoption. This thesis advances qualify as-you-build manufacturing by developing high-fidelity, data-driven surrogate models that transform in-process monitoring data into real-time predictions of sub-surface pores and surface dimensional errors. A co-axial optical monitoring system comprising a photodiode and an NIR camera captured the laser-powder interaction, with X-ray computed tomography providing ground-truth labels. For binary pore detection, a hybrid CNN-LSTM model that incorporated inter-hatch and inter-layer remelting effects achieved an area under the Receiver Operating Characteristic curve (AUROC) of 0.91 for pores exceeding 8000 µm3. To predict keyhole pore, physics-informed melt pool features integrated into a Random Forest model (AUROC = 0.95) outperformed deep learning benchmarks, delivering superior accuracy at substantially lower computational cost. In lack-of-fusion porosity regression, the CNN-LSTM surrogate model achieved high accuracy in within-scenario predictions (RMS

## 359. Physics-Informed Machine Learning for Fatigue and Fracture Analysis and Prediction: A Scoping Review

- year: 2026 | venue:  | tier: B | relevance: 5 | citations: 0
- doi: 10.17605/osf.io/cjd2h | key: `doi:10.17605/osf.io/cjd2h`
- source: Q7

**Abstract**: Fatigue and fracture pose critical challenges to the safety and reliability of engineering structures, with traditional prediction methods often limited by data demands, computational cost, and inherent complexities. This is particularly pronounced in the context of Industry 4.0, where advanced manufacturing processes like metal additive manufacturing introduce unique complexities related to material properties, defect characteristics, and the need for real-time quality assurance. While reviews exist on machine learning in fatigue, a systematization focused specifically on the integration of physical constraints and how they mitigate data scarcity in various engineering contexts, including these advanced manufacturing environments, is lacking. This bibliographic review systematically surveys advancements in applying physics-informed machine learning to fatigue and fracture analysis across diverse materials and applications. We detail methodologies, neural network architectures, and foundational theoretical models—such as Basquin's formula, Paris's Law, continuous damage mechanics, von Mises criterion, and continuum mechanics principles—that are explicitly integrated. The review hig

## 360. A Review of Residual Stress and Deformation in Metal Additive Manufacturing: Formation Mechanisms, Influencing Factors, Prediction Methods, and Mitigation Strategies

- year: 2026 | venue: Coatings | tier: B | relevance: 5 | citations: 0
- doi: 10.3390/coatings16080975 | key: `doi:10.3390/coatings16080975`
- source: Q7

**Abstract**: Metal additive manufacturing (MAM) enables the fabrication of geometrically complex and high-performance components but is accompanied by steep thermal gradients, repeated thermal cycling, phase transformation, residual stress, and deformation. These effects can reduce dimensional accuracy, manufacturing stability, fatigue resistance, and service reliability. This review systematically examines residual-stress and deformation behavior in MAM from the perspectives of formation mechanisms, influencing factors, measurement and prediction methods, mitigation strategies, and service-related consequences. The temperature gradient, mechanical constraint, and phase transition mechanisms are discussed as quantitatively coupled rather than independent processes. Comparative attention is given to process-specific differences, alloy-dependent thermophysical and metallurgical behavior, multi-track and multi-material interactions, and complex geometries. Destructive and non-destructive measurement techniques are compared in terms of penetration depth, spatial resolution, uncertainty, and cross-validation. Thermo-mechanical finite element, inherent strain, analytical, reduced-order, machine-learn

## 361. Neither Precision Nor Architecture Alone: Controlled Tests of Failure Remedies for Physics-Informed Neural Networks

- year: 2026 | venue:  | tier: A | relevance: 5 | citations: 0
- doi: — | key: `t:neitherprecisionnorarchitecturealonecontrolledtestsoffailureremediesforphysicsin`
- source: S2-Q1

**Abstract**: Physics-Informed Neural Networks (PINNs) frequently fail on stiff or advection-dominated PDEs, and two recent accounts offer competing remedies: switching from FP32 to FP64 to repair an L-BFGS stopping artifact, or replacing the MLP with a state-space-model (SSM) backbone plus sub-sequence alignment to counter architectural simplicity bias. We test both under matched, seed-paired controls in a pre-registered 144-run study spanning convection, reaction, and wave, plus an independent 85-run convection/wave study; success is relative $\ell_2$ error below $0.05$. The two remedies act on disjoint regime-and-seed slices: neither substitutes for the other. On hard convection ($\beta{=}50$), alignment recovers 2/5 seeds in FP32 and 3/5 in FP64, where the unaligned SSM succeeds on 0/5 seeds at either precision and the vanilla MLP moves only from 0/5 to 1/5 across the precision switch---the recoveries trace to the alignment objective, not the backbone. On reaction the backbone alone already succeeds on 3/5--4/5 seeds, so each remedy covers a regime the other does not. Responses are also seed-specific: the same precision switch flips individual seeds in opposite directions and, on wave, lower

## 362. Annular Computational Imaging: Capture Clear Panoramic Images Through Simple Lens

- year: 2022 | venue: IEEE Transactions on Computational Imaging | tier: A | relevance: 4 | citations: 19
- doi: 10.1109/tci.2022.3233467 | key: `doi:10.1109/tci.2022.3233467`
- source: Q1

**Abstract**: Panoramic Annular Lens (PAL) composed of few lenses has great potential in panoramic surrounding sensing tasks for mobile and wearable devices because of its tiny size and large Field of View (FoV). However, the image quality of tiny-volume PAL confines to optical limit due to the lack of lenses for aberration correction. In this paper, we propose an Annular Computational Imaging (ACI) framework to break the optical limit of light-weight PAL design. To facilitate learning-based image restoration, we introduce a wave-based simulation pipeline for panoramic imaging and tackle the synthetic-to-real gap through multiple data distributions. The proposed pipeline can be easily adapted to any PAL with design parameters and is suitable for loose-tolerance designs. Furthermore, we design the Physics Informed Image Restoration Network (PI$^{2}$RNet) considering the physical priors of panoramic imaging and single-pass physics-informed engine. At the dataset level, we create the DIVPano dataset and the extensive experiments on it illustrate that our proposed network sets the new state of the art in the panoramic image restoration under spatially-variant degradation. In addition, the evaluation

## 363. Intelligent Feedrate Optimization Using an Uncertainty-Aware Digital Twin Within a Model Predictive Control Framework

- year: 2024 | venue: IEEE Access | tier: A | relevance: 4 | citations: 11
- doi: 10.1109/access.2024.3384471 | key: `doi:10.1109/access.2024.3384471`
- source: Q1

**Abstract**: The future of intelligent manufacturing machines involves autonomous selection of process parameters to maximize productivity while maintaining quality within specified constraints. To effectively optimize process parameters, these machines need to adapt to existing uncertainties in the physical system. This paper proposes a novel framework and methodology for feedrate optimization that is based on a physics-informed data-driven digital twin with quantified uncertainty. The servo dynamics are modeled using a digital twin, which incorporates the known uncertainty in the physics-based models and predicts the distribution of contour error using a data-driven model that learns the unknown uncertainty on-the-fly by sensor measurements. Using the quantified uncertainty, the proposed feedrate optimization maximizes productivity while maintaining quality under desired servo error constraints and stringency (i.e., the tolerance for constraint violation under uncertainty) using a model predictive control framework. Experimental results obtained using a 3-axis desktop CNC machine tool and a desktop 3D printer demonstrate significant cycle time reductions of up to 38% and 17% respectively, whi

## 364. Fault-Tolerant Sun-Pointing Attitude Control Based on Physics-Guided Neural Networks

- year: 2024 | venue: IEEE Transactions on Industrial Informatics | tier: A | relevance: 4 | citations: 4
- doi: 10.1109/tii.2024.3438256 | key: `doi:10.1109/tii.2024.3438256`
- source: Q4

**Abstract**: To ensure system reliability and maintain power supply in fault conditions, this article proposes a fault-tolerant sun-pointing controller based on physics-guided neural networks for handling sensor faults. The proposed controller gains the fault tolerance ability by learning from the behavior of the nominal controller, which integrates a physics-based model with a deep learning model to exploit implicit physical insights during the learning process. The proposed controller enhances the intrinsic interpolative nature of the pure deep learning model, thereby improving fault tolerance for unknown faults. Furthermore, a novel loss function that incorporates the physics-based model is proposed. The loss function assigns different loss terms to the fault-free and the fault datasets, facilitating accurate utilization of loss terms. Unlike traditional active fault-tolerant control schemes, the proposed method requires no explicit fault detection and diagnosis module. The effectiveness of the proposed controller is validated through hardware-in-the-loop simulations. The results indicate that the proposed controller outperforms the pure deep learning controller, as evidenced by a shorter su

## 365. DEVELOPMENT OF AN AI-INTEGRATED PREDICTIVE MODELING FRAMEWORK FOR PERFORMANCE OPTIMIZATION OF PEROVSKITE AND TANDEM SOLAR PHOTOVOLTAIC SYSTEMS

- year: 2023 | venue: International Journal of Business and Economics Insights | tier: A | relevance: 4 | citations: 4
- doi: 10.63125/8xm7wa53 | key: `doi:10.63125/8xm7wa53`
- source: S2-Q1

**Abstract**: This study explores the integration of artificial intelligence into predictive modeling frameworks aimed at optimizing the performance of perovskite and tandem solar photovoltaic systems, technologies that have emerged as transformative solutions for enhancing solar energy efficiency and accelerating global decarbonization efforts. Perovskite solar cells have gained significant attention due to their tunable bandgaps, high defect tolerance, and cost-effective fabrication methods, while tandem architectures—particularly perovskite–silicon combinations—offer the potential to surpass the Shockley–quizzer efficiency limit. Despite these advantages, persistent challenges related to instability, ion migration, current matching, and spectral sensitivity hinder widespread adoption. Artificial intelligence has been increasingly applied across these domains, enabling high-throughput materials discovery, surrogate modeling for device physics, reinforcement learning for maximum power point tracking, and computer vision approaches for defect detection. This study followed the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) guidelines to ensure methodological rigor an

## 366. Annular Computational Imaging: Capture Clear Panoramic Images through Simple Lens

- year: 2022 | venue: arXiv (Cornell University) | tier: A | relevance: 4 | citations: 1
- doi: 10.48550/arxiv.2206.06070 | key: `doi:10.48550/arxiv.2206.06070`
- source: Q1

**Abstract**: Panoramic Annular Lens (PAL) composed of few lenses has great potential in panoramic surrounding sensing tasks for mobile and wearable devices because of its tiny size and large Field of View (FoV). However, the image quality of tiny-volume PAL confines to optical limit due to the lack of lenses for aberration correction. In this paper, we propose an Annular Computational Imaging (ACI) framework to break the optical limit of light-weight PAL design. To facilitate learning-based image restoration, we introduce a wave-based simulation pipeline for panoramic imaging and tackle the synthetic-to-real gap through multiple data distributions. The proposed pipeline can be easily adapted to any PAL with design parameters and is suitable for loose-tolerance designs. Furthermore, we design the Physics Informed Image Restoration Network (PI2RNet) considering the physical priors of panoramic imaging and single-pass physics-informed engine. At the dataset level, we create the DIVPano dataset and the extensive experiments on it illustrate that our proposed network sets the new state of the art in the panoramic image restoration under spatially-variant degradation. In addition, the evaluation of t

## 367. Intelligent Feedrate Optimization using an Uncertainty-aware Digital Twin within a Model Predictive Control Framework

- year: 2023 | venue: Preprints.org | tier: A | relevance: 4 | citations: 1
- doi: 10.20944/preprints202311.0041.v1 | key: `doi:10.20944/preprints202311.0041.v1`
- source: Q1

**Abstract**: The future of intelligent manufacturing machines involves autonomous selection of process parameters to maximize productivity while maintaining quality within specified constraints. To effectively optimize process parameters, these machines need to adapt to existing uncertainties in the physical system. This paper proposes a novel framework and methodology for feedrate optimization that is based on a physics-informed data-driven digital twin with quantified uncertainty. The servo dynamics are modeled using a digital twin, which incorporates the known uncertainty in the physics-based models and predicts the distribution of contour error using a data-driven model that learns the unknown uncertainty on-the-fly by sensor measurements. Using the quantified uncertainty, the proposed feedrate optimization maximizes productivity while maintaining quality under desired servo error constraints and stringency (i.e., the tolerance for constraint violation under uncertainty) using a model predictive control framework. Experimental results obtained using a 3-axis desktop CNC machine tool and a desktop 3D printer demonstrate significant cycle time reductions of up to 38% and 17 respectively, whil

## 368. CtF: A Multi-Contact, Multi-Axis Spring–Hall Foot Sensor With Physics-Guided Learning for Legged Robots

- year: 2025 | venue: IEEE Sensors Journal | tier: A | relevance: 4 | citations: 1
- doi: 10.1109/jsen.2025.3622594 | key: `doi:10.1109/jsen.2025.3622594`
- source: Q1

**Abstract**: We present a compact multi-axis foot-end sensor for legged robots that couples a compliant spring–magnet mechanism with four MLX90393 tri-axial Hall sensors arranged circumferentially on a circular PCB. A physics-informed neural network (PINN) combined with a multilayer perceptron (MLP) and a short temporal window directly maps raw magnetic signals to simultaneous estimates of contact position and 3-D forces in real time, resolving force–location ambiguities under eccentric loading. Experiments at five predefined contact points produced over 200 k samples covering varied normal and shear loads. Scatter-plot analyses show strong linear agreement between predicted and measured forces; histogram statistics confine errors within ±5 N for normal and ±2 N for shear. Contact-location accuracy is confirmed by threshold hit rates of 86.7% at 2 mm, 90.4% at 3 mm, and 92.0% at 5 mm. The full inference pipeline achieves an end-to-end latency of ~10 ms, supporting real-time feedback control. With its low cost, impact tolerance, and accurate multi-point force estimation, the proposed sensor offers a practical means to enhance foot-ground perception in legged robots and supports terrain-adaptive 

## 369. Robust Transducer-Reflector Distance Control in Acoustic Levitation

- year: 2026 | venue: IEEE Open Journal of Ultrasonics Ferroelectrics and Frequency Control | tier: A | relevance: 4 | citations: 1
- doi: 10.1109/ojuffc.2026.3679991 | key: `doi:10.1109/ojuffc.2026.3679991`
- source: Q1

**Abstract**: Acoustic levitation enables contactless manipulation for applications in containerless processing in chemistry and materials science. Single-transducer levitators, consisting of an ultrasonic transducer and a reflector, offer a minimal hardware configuration but require precise control of the transducer–reflector distanceH. We propose a distance stabilization system based on a motorized linear stage and a precision balance that measures the acoustic radiation force (ARF) as a time-averaged, surface-integrated force magnitude on the reflector. Because ARF versusHexhibits extremely narrow resonance peaks, micrometer-scale deviations markedly reduce force and destabilize levitation. In practice, high-power transducers are actively kept at resonance using resonance frequency tracking (RFT). As the tracked frequency changes, the wavelength changes as well and the optimal distanceHshifts. We introduce a two-stage control strategy in order to robustly stabilizeH. First, a physics-informed, one-sided adaptive hill climb algorithm locates the cavity resonance. Second, a physics-informed extremum-seeking controller maintains the experimentally determined resonance distance despite drift and 

## 370. SU‐E‐T‐179: Clinical Impact of IMRT Failure Modes at Or Near TG‐142 Tolerance Criteria Levels

- year: 2015 | venue: Medical Physics | tier: A | relevance: 4 | citations: 1
- doi: 10.1118/1.4924540 | key: `doi:10.1118/1.4924540`
- source: Q13-CR

**Abstract**:   Purpose:  Quantitatively assess the clinical impact of 11 critical IMRT dose delivery failure modes.    Methods:  Eleven step‐and‐shoot IMRT failure modes (FMs) were introduced into twelve Pinnacle v9.8 treatment plans. One standard and one highly modulated plan on the IROC IMRT phantom and ten previous H&amp;N patient treatment plans were used. FMs included physics components covered by basic QA near tolerance criteria levels (TG‐142) such as beam energy, MLC positioning, and MLC modeling. Resultant DVHs were compared to those of failure‐free plans and the severity of plan degradation was assessed considering PTV coverage and OAR and normal tissue tolerances and used for FMEA severity scoring. Six of these FMs were physically simulated and phantom irradiations performed. TLD and radiochromic film results are used for comparison to treatment planning studies.    Results:  Based on treatment planning studies, the largest clinical impact from the phantom cases was induced by 2 mm systematic MLC shift in one bank with the combination of a D95% target under dose near 16% and OAR overdose near 8%. Cord overdoses of 5%–11% occurred with gantry angle, collimator angle, couch angle, MLC 

## 371. Intelligent Feedrate Optimization using an Uncertainty-aware Digital Twin within a Model Predictive Control Framework

- year: 2023 | venue: Preprints.org | tier: A | relevance: 4 | citations: 0
- doi: 10.20944/preprints202311.0041.v2 | key: `doi:10.20944/preprints202311.0041.v2`
- source: Q1

**Abstract**: The future of intelligent manufacturing machines involves autonomous selection of process parameters to maximize productivity while maintaining quality within specified constraints. To effectively optimize process parameters, these machines need to adapt to existing uncertainties in the physical system. This paper proposes a novel framework and methodology for feedrate optimization that is based on a physics-informed data-driven digital twin with quantified uncertainty. The servo dynamics are modeled using a digital twin, which incorporates the known uncertainty in the physics-based models and predicts the distribution of contour error using a data-driven model that learns the unknown uncertainty on-the-fly by sensor measurements. Using the quantified uncertainty, the proposed feedrate optimization maximizes productivity while maintaining quality under desired servo error constraints and stringency (i.e., the tolerance for constraint violation under uncertainty) using a model predictive control framework. Experimental results obtained using a 3-axis desktop CNC machine tool and a desktop 3D printer demonstrate significant cycle time reductions of up to 38% and 17% respectively, whi

## 372. Intelligent Feedrate Optimization using an Uncertainty-aware Digital Twin within a Model Predictive Control Framework

- year: 2023 | venue: Preprints.org | tier: A | relevance: 4 | citations: 0
- doi: 10.20944/preprints202311.0041.v3 | key: `doi:10.20944/preprints202311.0041.v3`
- source: Q1

**Abstract**: The future of intelligent manufacturing machines involves autonomous selection of process parameters to maximize productivity while maintaining quality within specified constraints. To effectively optimize process parameters, these machines need to adapt to existing uncertainties in the physical system. This paper proposes a novel framework and methodology for feedrate optimization that is based on a physics-informed data-driven digital twin with quantified uncertainty. The servo dynamics are modeled using a digital twin, which incorporates the known uncertainty in the physics-based models and predicts the distribution of contour error using a data-driven model that learns the unknown uncertainty on-the-fly by sensor measurements. Using the quantified uncertainty, the proposed feedrate optimization maximizes productivity while maintaining quality under desired servo error constraints and stringency (i.e., the tolerance for constraint violation under uncertainty) using a model predictive control framework. Experimental results obtained using a 3-axis desktop CNC machine tool and a desktop 3D printer demonstrate significant cycle time reductions of up to 38% and 17% respectively, whi

## 373. Physics-informed spectral parameterization for tractable tolerance sampling in broadband imaging

- year: 2026 | venue: Optics Letters | tier: A | relevance: 4 | citations: 0
- doi: 10.1364/ol.600996 | key: `doi:10.1364/ol.600996`
- source: Q1

**Abstract**: Modeling wavelength-dependent aberrations in broadband imaging systems requires high-dimensional parameter spaces that render Monte Carlo (MC) tolerance analysis intractable. We propose a low-dimensional spectral parameterization of Zernike coefficients that compresses broadband aberration modeling from 288 to 36 parameters and enables tractable MC tolerance analysis for manufactured systems. For a dispersion-dominated DD-CASSI system, we further introduce a Cauchy-derived Hybrid basis whose 1/ λ 2 dependence captures defocus-driven dispersion. Compared with nominal-PSF training, MC-augmented training with the proposed parameterization improves reconstruction PSNR by 1.06 dB, of which 0.48 dB is attributable to the Hybrid basis over a polynomial baseline.

## 374. Explainable Remaining Useful Life Prediction of Air Circuit Breakers via Physics-Informed Electro-Mechanical Feature Fusion

- year: 2026 | venue: Sensors | tier: A | relevance: 4 | citations: 0
- doi: 10.3390/s26185802 | key: `doi:10.3390/s26185802`
- source: Q1

**Abstract**: Accurate remaining useful life (RUL) prediction of air circuit breakers (ACBs) is crucial for condition-based maintenance. However, existing data-driven prognostic methods suffer from electromechanical feature fragmentation, cross-device domain shifts, and the inability to penalize safety-critical late predictions. This study proposes an explainable RUL prediction framework via physics-informed feature fusion. Through full-lifecycle monitoring, novel indicators, including the electromechanical coupled degradation index (EMCDI) and the contact spring over-travel consumption rate (CSOCR), are introduced to decode interactive degradation cycles. To eliminate the interferences of initial manufacturing tolerances, a phase-decoupled normalization strategy empowers a random forest (RF) model to achieve cross-device transferability in a two-device proof-of-concept experiment, requiring only 50 initial operations for target calibration. Additionally, a safety-oriented asymmetric penalty score (APS) is integrated into the evaluation framework to explicitly penalize hazardous life overestimations. Experimental results demonstrate a full-lifecycle R2 of 0.9936 and a mean absolute error (MAE) o

## 375. WINO: A weak-form physics informed neural operator for hyperelasticity on variable domains

- year: 2026 | venue: Computer Methods in Applied Mechanics and Engineering | tier: A | relevance: 4 | citations: 0
- doi: 10.1016/j.cma.2026.119356 | key: `doi:10.1016/j.cma.2026.119356`
- source: Q1

**Abstract**: We propose a Weak-form Physics-Informed Neural Operator (WINO), a data-free framework that combines the efficiency of neural operators with the geometric flexibility of the φ -finite element method ( φ -FEM). φ -FEM is an unfitted method that accommodates geometric variations without body-fitted meshes, where the domain geometry is represented by the level-set function φ . To impose the boundary conditions, Dirichlet problems adopt the φ -FEM lifting so only the homogeneous displacement contribution is learned, whereas traction-driven Neumann problems additionally predict the auxiliary fields necessary for the unfitted weak formulation. Parameters are trained by minimizing squared weak-form residuals aligned with φ -FEM together with squared penalties on the cut-cell auxiliary equations, which removes the need for large paired datasets of converged reference solutions. When labeled reference data are available, an optional data-augmented variant (WINO+data) can further combine this physics-informed loss with a supervised term. After training, WINO outputs can seed the nonlinear φ -FEM solvers as neural operator warm starts (NOWS), which reduce iteration counts relative to tradition

## 376. Physics-Informed Auto-Differentiation for Limited-Angle Tomography of Thick Amorphous Specimens Using BF-STEM

- year: 2026 | venue: Microscopy and Microanalysis | tier: A | relevance: 4 | citations: 0
- doi: 10.1093/mam/ozag053.322 | key: `doi:10.1093/mam/ozag053.322`
- source: Q1

**Abstract**: Electron Tomography is a widely used 3D imaging tool for biological specimens because it offers higher resolution than optical imaging and greater accessibility than X-ray sources. While transmission electron microscopy (TEM) tomography can offer advantages for thin specimens under well-controlled imaging conditions, imaging thick, amorphous specimens becomes increasingly challenging due to reduced transmission and loss of usable contrast at large thicknesses. Alternatively, bright-field scanning transmission electron microscopy (BF-STEM) tomography, due to improved dose control and tolerance to multiple scattering, is preferred for thick samples, as it can image samples thicker than 400 nm while maintaining sufficient resolution and signal [1][2]. However, BF-STEM tomography of sheet-like laminar specimens remains strongly limited by incomplete tilt ranges, and the mismatch between conventional linear reconstruction algorithms and the underlying nonlinear image-formation physics limits reconstruction quality. In this work, we employ a physics-informed automatic differentiation (PIAD) based limited-angle tomography framework that uses a multislice TEM forward model to approximate t

## 377. A machine learning study on the fatigue crack path of short crack on an α titanium alloy

- year: 2023 | venue: Philosophical Transactions of the Royal Society A Mathematical Physical and Engineering Sciences | tier: A | relevance: 3 | citations: 3
- doi: 10.1098/rsta.2022.0391 | key: `doi:10.1098/rsta.2022.0391`
- source: Q1

**Abstract**: In the present study, a physics-informed neural network model based on Bayesian hyperparameter optimization is proposed for the prediction of short crack growth paths. A large number of cyclic loadings at a lower amplitude were applied to an α titanium sample by an ultrasonic fatigue machine to ensure a sufficient amount of data for machine learning. The grain size, grain orientation and grain boundary direction on the path, as well as crack growth direction, were selected as feature data for training the prediction model. The optimizations of the size ratio and the angle operation were conducted to compare different data processing methods, respectively. After evaluation, eventually, a model for predicting crack growth path is obtained with a reliable performance of 10% tolerance on the path angle at each grain boundary. And the prediction effect of the proposed model is better than that of some classic machine learning models and slip trace analysis. This article is part of the theme issue 'Physics-informed machine learning and its structural integrity applications (Part 1)'.

## 378. Artificial intelligence for mechanistic understanding of hepatitis B virus

- year: 2025 | venue: Frontiers in Virology | tier: A | relevance: 3 | citations: 2
- doi: 10.3389/fviro.2025.1729171 | key: `doi:10.3389/fviro.2025.1729171`
- source: Q1

**Abstract**: Chronic hepatitis B virus (HBV) persists through a compact proteome, deep reliance on host pathways, and a nuclear covalently closed circular DNA (cccDNA) reservoir that current antivirals rarely extinguish. This Mini Review synthesizes advances from 2020–2025 in which artificial intelligence (AI) augments mechanistic understanding of HBV rather than serving only predictive ends. We summarize (i) AI-enabled structural modeling that clarifies polymerase priming and HBx architecture; (ii) physics-informed and multiscale inference that links sparse measurements to replication and cccDNA kinetics; (iii) sequence-based learners that expose non-random host-genome integration contexts and mutational constellations associated with immune tolerance or escape; (iv) network-aware analyses that prioritize host dependencies and connect CRISPR perturbations to virus–host modules governing cccDNA transcriptional control; and (v) AI-assisted antiviral discovery that couples virtual screening with mechanism-anchored interpretation (e.g., capsid assembly modulators). Across these domains, AI sharpens hypotheses by mapping viral mutations and host factors to discrete steps of the life cycle, quantita

## 379. Physics-informed State-space Neural Networks for Transport Phenomena

- year: 2023 | venue: arXiv (Cornell University) | tier: A | relevance: 3 | citations: 1
- doi: 10.48550/arxiv.2309.12211 | key: `doi:10.48550/arxiv.2309.12211`
- source: Q1

**Abstract**: This work introduces Physics-informed State-space neural network Models (PSMs), a novel solution to achieving real-time optimization, flexibility, and fault tolerance in autonomous systems, particularly in transport-dominated systems such as chemical, biomedical, and power plants. Traditional data-driven methods fall short due to a lack of physical constraints like mass conservation; PSMs address this issue by training deep neural networks with sensor data and physics-informing using components' Partial Differential Equations (PDEs), resulting in a physics-constrained, end-to-end differentiable forward dynamics model. Through two in silico experiments -- a heated channel and a cooling system loop -- we demonstrate that PSMs offer a more accurate approach than a purely data-driven model. In the former experiment, PSMs demonstrated significantly lower average root-mean-square errors across test datasets compared to a purely data-driven neural network, with reductions of 44 %, 48 %, and 94 % in predicting pressure, velocity, and temperature, respectively. Beyond accuracy, PSMs demonstrate a compelling multitask capability, making them highly versatile. In this work, we showcase two: s

## 380. Data-driven modeling of AlSi10Mg mechanical properties: predictive approach to process parameters selection in laser powder bed fusion

- year: 2025 | venue: Materials & Design | tier: A | relevance: 3 | citations: 1
- doi: 10.1016/j.matdes.2025.114918 | key: `doi:10.1016/j.matdes.2025.114918`
- source: Q1

**Abstract**: • Data-driven and physics-informed modeling optimizes LPBF AlSi10Mg with high accuracy. • Bidirectional LSTM outperforms RNN/LSTM with < 10 % error and physics-aligned interpretations. • Symbolic regression balances parameter influence for transparent process optimization. • Robust generalization reduces costs and improves part performance in industrial applications. • Machine learning framework accelerates AlSi10Mg development for tailored LPBF properties. Data-driven methods for accelerated design and optimization of additively manufactured AlSi 10 Mg components based on the prediction of their mechanical properties are presented. The bidirectional long short-term memory demonstrates superior performance compared to symbolic regression, achieving maximum relative errors below 7.83 % using 5-fold cross-validation for all predicted mechanical properties. Despite the possibility of achieving accurate predictions, symbolic regression and random forest methods yield feature importances that conflict with established LPBF knowledge, suggesting sequence learning methods may be better suited for capturing the process’s complex relationships. The models, validated against experimental dat

## 381. Enhanced Lightweight Blockchain‐Based Integrated Finite Element Neural Network for Secure Routing in Wireless Sensor Networks

- year: 2025 | venue: International Journal of Communication Systems | tier: A | relevance: 3 | citations: 1
- doi: 10.1002/dac.70184 | key: `doi:10.1002/dac.70184`
- source: Q1

**Abstract**: ABSTRACT Ensuring secure and energy‐efficient routing in wireless sensor networks (WSNs) remains a critical challenge due to limited resources and susceptibility to attacks. This paper introduces a novel model, PBFT‐IFENN—a lightweight blockchain‐based Practical Byzantine Fault Tolerance system integrated with a Finite Element Neural Network designed to address these issues comprehensively. The model leverages the Duck Swarm Algorithm (DSA) for dynamic cluster head selection, whereas data aggregation is optimized through an Integrated Finite Element Neural Network (I‐FENN), incorporating Physics‐Informed Neural Networks (PINNs) for reducing redundancy. Security is ensured using a lightweight PBFT consensus, and efficient routing is maintained via the Musical Chairs Routing Protocol (MCRP). Performance was evaluated using the NS‐3 simulator and compared against recent benchmark protocols including UDTP‐RPR, GTGAN, DRPL_SDN, DA‐TD3, and ILEACH. Results demonstrate that PBFT‐IFENN achieves superior outcomes, with a packet delivery ratio (PDR) of 95%, energy consumption of 1.12 J for 100 nodes, and throughput of 750 Kbps. These results significantly outperform all referenced methods, s

## 382. Physics-Informed Deep Learning for 2-D Phased Array Beamforming With Imperfection Tolerance

- year: 2026 | venue: IEEE Access | tier: A | relevance: 3 | citations: 1
- doi: 10.1109/access.2026.3651811 | key: `doi:10.1109/access.2026.3651811`
- source: Q1

**Abstract**: Designing efficient and reliable two-dimensional (2D) beamforming for phased array antennas (PAAs) remains a significant challenge because of the heavy computational demands involved. In this study, we introduce a beamforming framework that adopts a physics-informed deep neural network (PIDNN). The proposed model incorporates physical principles directly into the training process through a customized loss function, which minimizes the mean squared error between the array response and a target reference signal. The beamforming weights produced by the PIDNN are systematically evaluated against the theoretically optimal Wiener solution. To assess robustness, the method is implemented on an 8×8 PAA and evaluated against both a shallow architecture—the radial basis function neural network (RBFNN)—and a deeper model, the convolutional neural network (CNN). Moreover, the PIDNN is applied to a large PAA to assess its performance when the number of antenna elements increases. Experimental results demonstrate that the PIDNN closely approximates Wiener-optimal weights while maintaining robustness to array imperfections and achieving this with markedly reduced computational cost.

## 383. An improved random projection-based integration method for differential-algebraic equations (DAEs) of constrained mechanical systems

- year: 2026 | venue: Proceedings of the Institution of Mechanical Engineers Part K Journal of Multi-body Dynamics | tier: A | relevance: 3 | citations: 1
- doi: 10.1177/14644193261438931 | key: `doi:10.1177/14644193261438931`
- source: Q1

**Abstract**: Accurately integrating stiff ordinary differential equations (ODEs) and index-1 differential-algebraic equations that govern constrained multibody systems remains computationally demanding, especially for real-time applications. This article proposes an improved parsimonious physics-informed random-projection neural-network (PIRPNN) integrator that embeds explicit velocity- and position-correction into a single-hidden-layer random-feature framework and employs a vectorized assembly of system matrices for computation efficiency. Two illustrative examples are utilized to demonstrate the proposed algorithm and advantages. For the multibody dynamics benchmark problems examined, the improved PIRPNN demonstrates improved accuracy in terms of L 2 -trajectory error and energy drift, together with a notable reduction in computational cost compared with the original PIRPNN. At peculiar tolerances from 10 −6 to 10 −10 , it also outperforms the implicit MATLAB solvers ode15s and ode23t, further lowering both trajectory error and total-energy drift. The results underscore the potential of random-projection neural integrators as lightweight, constraint-preserving integration method alternative t

## 384. A Thermally Reliable Variable-Topology Magnetic Coupler with Closed-Loop Multiphysics Co-Design for Guided-Platform AUV Wireless Charging

- year: 2026 | venue: IEEE Transactions on Transportation Electrification | tier: A | relevance: 3 | citations: 1
- doi: 10.1109/tte.2026.3692658 | key: `doi:10.1109/tte.2026.3692658`
- source: Q4

**Abstract**: Guided-platform wireless charging enables persistent autonomous underwater vehicle (AUV) operation but imposes severe electromagnetic and thermal constraints due to large docking gaps, full-angle misalignment, and compact subsea integration. This paper proposes a thermally reliable variable-topology magnetic coupler (VTMC) with a radially reconfigurable transmitter and a staggered dual-layer receiver to ensure strong coupling and rotation tolerance. A temperature-aware hybrid loss model, combining analytical formulations with finite-element field extraction, is developed to accurately capture high-frequency and temperature-dependent losses. These spatially nonuniform losses are embedded into a loss-validated closed-loop multiphysics framework, which identifies the receiver nanocrystalline core as the dominant hotspot source and reveals the underlying thermal mechanism. Based on this insight, a physics-guided stacked-core optimization is proposed to reduce peak temperature and improve thermal uniformity without degrading electromagnetic performance. A 4.2 kW prototype validates the proposed approach, achieving 92.8% DC–DC efficiency, stable power transfer over 0–360° rotation, and r

## 385. Data-driven identification of robot DH parameter errors using a physics-informed transformer network

- year: 2026 | venue: International Computing Imaging Conference | tier: A | relevance: 3 | citations: 1
- doi: 10.1117/12.3091946 | key: `doi:10.1117/12.3091946`
- source: S2-Q1

**Abstract**: The pose accuracy of a six-axis robotic arm is crucial for high-end applications such as aerospace and precision manufacturing. For robotic arms using DH (Denavit-Hartenberg) for kinematic modeling, model parameter errors originating from machining tolerances are the key factors limiting their positioning accuracy. Traditional parameter calibration methods using iterative optimization are often sensitive to initial values and prone to converging to local optimal solutions. This study proposes a neural network-based parameter identification method. Using pose error (represented by axis-angle notation) and joint angles as inputs, the parameter alpha is identified as output and undergoes standardization. The transformer encoder serves as the network structure, with a physical loss term derived from forward kinematics calculations added to the loss function. The final trained model achieved a Mean Absolute Error (MAE) of 2.5×10-4 (rad) in predicting alpha on 50 test samples, a 37.78 % reduction compared to uncompensated values. Using the compensated parameters, the pose error was reduced by 94.57 % compared to the uncompensated kinematic model, demonstrating the effectiveness of the pr

## 386. Train and test data from EBSD observation from A machine learning study on the fatigue crack path of short crack on an α titanium alloy

- year: 2023 | venue: Figshare | tier: A | relevance: 3 | citations: 0
- doi: 10.6084/m9.figshare.23977800 | key: `doi:10.6084/m9.figshare.23977800`
- source: Q1

**Abstract**: In the present study, a physics-informed neural network model based on Bayesian hyperparameter optimization is proposed for the prediction of short crack growth paths. A large number of cyclic loadings at a lower amplitude were applied to an α titanium sample by ultrasonic fatigue machine to ensure a sufficient amount of data for machine learning. The grain size, grain orientation, grain boundary direction on the path, as well as crack growth direction, were selected as feature data for training the prediction model. The optimizations of the size ratio and the angle operation were conducted to compare different data processing methods, respectively. After evaluation, eventually, a model for predicting crack growth path is obtained with a reliable performance of 10% tolerance on the path angle at each grain boundary. And the prediction effect of the proposed model is better than that of some classic machine learning models and slip trace analysis.This article is part of the theme issue 'Physics-informed machine learning and its structural integrity applications (Part 1)'.

## 387. Process Analysis and Predictions in Basic Oxygen Furnace using AI and Machine Learning

- year: 2024 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: A | relevance: 3 | citations: 0
- doi: 10.5281/zenodo.19041647 | key: `doi:10.5281/zenodo.19041647`
- source: Q1

**Abstract**: This thesis investigates the optimization of Basic Oxygen Furnace (BOF) steelmaking through statistical and machine learning approaches to improve process stability and steel quality. Two complementary studies are presented: the prediction of Total Oxygen (O2) consumption and the evaluation of dephosphorization efficiency using the phosphorus partition ratio (Lp). Using data from Durgapur Steel Plant (SAIL), Multiple regression and machine learning models were developed and compared, with Multivariate Linear Regression demonstrating the best predictive performance and interpretability. For Total O2 prediction, a tolerance interval framework was introduced to provide robust operational ranges suitable for industrial decision-making. For dephosphorization, the study demonstrates that although models using endpoint slag chemistry and tap temperature achieve excellent predictive accuracy (R² of 0.99), their applicability is limited to offline process diagnostics because these variables are unavailable during active converter operation. The findings highlight the importance of distinguishing between diagnostic and real-time predictive models and suggest that future BOF automation should

## 388. Process Analysis and Predictions in Basic Oxygen Furnace using AI and Machine Learning

- year: 2024 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: A | relevance: 3 | citations: 0
- doi: 10.5281/zenodo.21396633 | key: `doi:10.5281/zenodo.21396633`
- source: Q1

**Abstract**: This thesis investigates the optimization of Basic Oxygen Furnace (BOF) steelmaking through statistical and machine learning approaches to improve process stability and steel quality. Two complementary studies are presented: the prediction of Total Oxygen (O2) consumption and the evaluation of dephosphorization efficiency using the phosphorus partition ratio (Lp). Using data from Durgapur Steel Plant (SAIL), Multiple regression and machine learning models were developed and compared, with Multivariate Linear Regression demonstrating the best predictive performance and interpretability. For Total O2 prediction, a tolerance interval framework was introduced to provide robust operational ranges suitable for industrial decision-making. For dephosphorization, the study demonstrates that although models using endpoint slag chemistry and tap temperature achieve excellent predictive accuracy (R² of 0.99), their applicability is limited to offline process diagnostics because these variables are unavailable during active converter operation. The findings highlight the importance of distinguishing between diagnostic and real-time predictive models and suggest that future BOF automation should

## 389. Physics-informed Gaussian Processes for Safe Envelope Expansion

- year: 2025 | venue: arXiv (Cornell University) | tier: A | relevance: 3 | citations: 0
- doi: 10.48550/arxiv.2501.01000 | key: `doi:10.48550/arxiv.2501.01000`
- source: Q1

**Abstract**: Flight test analysis often requires predefined test points with arbitrarily tight tolerances, leading to extensive and resource-intensive experimental campaigns. To address this challenge, we propose a novel approach to flight test analysis using Gaussian processes (GPs) with physics-informed mean functions to estimate aerodynamic quantities from arbitrary flight test data, validated using real T-38 aircraft data collected in collaboration with the United States Air Force Test Pilot School. We demonstrate our method by estimating the pitching moment coefficient without requiring predefined or repeated flight test points, significantly reducing the need for extensive experimental campaigns. Our approach incorporates aerodynamic models as priors within the GP framework, enhancing predictive accuracy across diverse flight conditions and providing robust uncertainty quantification. Key contributions include the integration of physics-based priors in a probabilistic model, which allows for precise computation from arbitrary flight test maneuvers, and the demonstration of our method capturing relevant dynamic characteristics such as short-period mode behavior. The proposed framework offe

## 390. Physics-Informed Machine Learning for Structural Health Monitoring of Aerospace Composite Structures

- year: 2025 | venue:  | tier: A | relevance: 3 | citations: 0
- doi: 10.12783/shm2025/37485 | key: `doi:10.12783/shm2025/37485`
- source: Q1

**Abstract**: This paper presents advanced structural health monitoring (SHM) methods for aerospace composite structures, which pose unique challenges due to sensor placement, cost, and environmental exposure. We introduce novel, physics-disciplined, data-driven approaches developed through two European Union projects. The first technique embeds glass-coated copper microwires in carbon-fibre composites, exploiting their Giant Magnetoimpedance (GMI) response to detect, classify, and quantify damage under stress. The second approach supports damage monitoring in composite liquid hydrogen tanks using Fibre Bragg Grating (FBG) sensors, addressing the challenges of conformal geometry and strict leakage tolerance where conventional diagnostics are inadequate. Physics-informed machine learning algorithms are developed for both systems. Finite element simulations inform neural network architecture and feature selection, while simulated signals guide strain and damage modelling. Experimental and simulation-based validation confirms high accuracy in damage detection and characterisation. This work was funded by the European Union under the Horizon Europe grant 101056884 and by the EU Clean Hydrogen Partne

## 391. Voltage Sag Economic Loss Assessment Method via Physics-Informed Non-equilibrium Dynamics with Minimal Data Requirements

- year: 2025 | venue:  | tier: A | relevance: 3 | citations: 0
- doi: 10.1109/ei268505.2025.11425220 | key: `doi:10.1109/ei268505.2025.11425220`
- source: Q1

**Abstract**: Voltage sag has emerged as a critical power quality issue causing substantial economic losses to sensitive industrial processes. Existing assessment methods suffer from either limited accuracy due to single-factor considerations or impractical data requirements for comprehensive approaches. This paper presents a minimal data requirement modeling framework based on non-equilibrium thermodynamics theory to overcome these limitations. The proposed method establishes a dynamic model that captures the intrinsic evolutionary mechanisms of voltage-sensitive processes. Through rapid model calibration with minimal measurement data, the approach reduces data requirements from extensive long-term monitoring to sparse sampling at critical points, eliminating engineering barriers of large-scale field experiments. Transforming uncertain voltage tolerance curve (VTC) regions into deterministic events via process parameter deviation quantification, dramatically enhancing practical applicability. Validation demonstrates over 90% accuracy across diverse sag events, providing quantitative basis for optimal mitigation equipment deployment and investment decisions.

## 392. Physics Informed Neural Networks for design optimisation of diamond particle detectors for charged particle fast-tracking at high luminosity hadron colliders

- year: 2025 | venue: arXiv (Cornell University) | tier: A | relevance: 3 | citations: 0
- doi: 10.48550/arxiv.2509.21123 | key: `doi:10.48550/arxiv.2509.21123`
- source: Q1

**Abstract**: Future high-luminosity hadron colliders demand tracking detectors with extreme radiation tolerance, high spatial precision, and sub-nanosecond timing. 3D diamond pixel sensors offer these capabilities due to diamond's radiation hardness and high carrier mobility. Conductive electrodes, produced via femtosecond IR laser pulses, exhibit high resistivity that delays signal propagation. This effect necessitates extending the classical Ramo-Shockley weighting potential formalism. We model the phenomenon through a 3rd-order, 3+1D PDE derived as a quasi-stationary approximation of Maxwell's equations. The PDE is solved numerically and coupled with charge transport simulations for realistic 3D sensor geometries. A Mixture-of-Experts Physics-Informed Neural Network, trained on Spectral Method data, provides a meshless solver to assess timing degradation from electrode resistance.

## 393. Physics-Informed Gaussian Processes for Efficient Envelope Expansion

- year: 2026 | venue: Journal of Aerospace Information Systems | tier: A | relevance: 3 | citations: 0
- doi: 10.2514/1.i011606 | key: `doi:10.2514/1.i011606`
- source: Q1

**Abstract**: Flight test analysis often requires predefined test points with arbitrarily tight tolerances, leading to extensive and resource-intensive experimental campaigns. To address this challenge, we propose a novel approach to flight test analysis using Gaussian processes (GPs) with physics-informed mean functions to estimate aerodynamic quantities from arbitrary flight test data, validated using real T-38 aircraft data collected in collaboration with the United States Air Force Test Pilot School. We demonstrate our method by estimating the pitching moment coefficient [Formula: see text] without requiring predefined or repeated flight test points, significantly reducing the need for extensive experimental campaigns. Our approach incorporates aerodynamic models as priors within the GP framework, enhancing predictive accuracy across diverse flight conditions and providing robust uncertainty quantification. Key contributions include the integration of physics-based priors in a probabilistic model, which allows for precise computation from arbitrary flight test maneuvers, and the demonstration of our method capturing relevant dynamic characteristics such as short-period mode behavior. The pro

## 394. A systematic review of physics-informed machine learning for resilient microgrid control and dynamics

- year: 2026 | venue: Electric Power Systems Research | tier: A | relevance: 3 | citations: 0
- doi: 10.1016/j.epsr.2026.113906 | key: `doi:10.1016/j.epsr.2026.113906`
- source: Q1

**Abstract**: Distribution systems increasingly deploy inverter-dominated microgrids to maintain prioritized service during extreme weather, cyber-physical disturbances, renewable-generation uncertainty, and upstream-grid degradation. Resilient operation depends on feasible transitions among grid-connected operation, islanding, restoration, and reconnection. These transitions must satisfy operating limits, converter constraints, synchronization tolerances, and protection requirements while accounting for resynchronization logic, breaker permissives, topology changes, and post-closing dynamics. Reduced-order models may not capture these constraints when converter limiting, switching events, and protection actions determine system trajectories. Physics-informed machine learning (PI-ML) addresses this limitation by embedding network equations, topology, device constraints, stability conditions, and feasibility mechanisms into learned models and controllers. Existing reviews treat microgrid resilience and PI-ML separately, without auditing transition-feasibility claims. This work presents a systematic, claim-level review of PI-ML for resilient microgrid dynamics and control. Claims are classified by

## 395. Accelerated Discovery and Stability Prediction of Lead-Free Halide Perovskites via Physics-Informed Machine Learning

- year: 2026 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: A | relevance: 3 | citations: 0
- doi: 10.5281/zenodo.18776435 | key: `doi:10.5281/zenodo.18776435`
- source: Q1

**Abstract**: Metal halide perovskites have emerged as promising candidates for advanced photovoltaic and optoelectronic devices; however, their commercial deployment is significantly limited by the toxicity and chemical instability of lead-based compositions . All-inorganic lead-free alternatives, particularly cesium tin mixed-halide perovskites, (CsSn(ClxBryI1−x−y)3) provide a viable pathway to environmentally benign and thermally stable materials . However, identifying experimentally realizable compositions remains challenging due to the vast combinatorial compositional space and the persistent discrepancy between theoretical stability and practicalsynthesis.This study develops a physics-informed and explainable machine learning framework to predict the synthesizability and thermodynamic stability of mixed-halide tin perovskites . A Positive-Unlabeled learning strategy, utilizing transductive bagging and decision tree classifiers, estimates synthesis probability based on literature-derived data [5]. A 76-dimensional descriptorset, incorporating compositional, elemental, structural, and density functional theory (DFT)-derived thermodynamic parameters, is constructed . Gradient boosting regress

## 396. Pretrain Finite Element Method: A Pretraining and Warm-start Framework for PDEs via Physics-Informed Neural Operators

- year: 2026 | venue: arXiv (Cornell University) | tier: A | relevance: 3 | citations: 0
- doi: — | key: `t:pretrainfiniteelementmethodapretrainingandwarmstartframeworkforpdesviaphysicsinf`
- source: Q1

**Abstract**: We propose a Pretrained Finite Element Method (PFEM),a physics driven framework that bridges the efficiency of neural operator learning with the accuracy and robustness of classical finite element methods (FEM). PFEM consists of a physics informed pretraining stage and an optional finetuning stage. In the pretraining stage, a neural operator based on the Transolver architecture is trained solely from governing partial differential equations, without relying on labeled solution data. The model operates directly on unstructured point clouds, jointly encoding geometric information, material properties, and boundary conditions, and produces physically consistent initial solutions with extremely high computational efficiency. PDE constraints are enforced through explicit finite element, based differentiation, avoiding the overhead associated with automatic differentiation. In the fine-tuning stage, the pretrained prediction is used as an initial guess for conventional FEM solvers, preserving their accuracy, convergence guarantees, and extrapolation capability while substantially reducing the number of iterations required to reach a prescribed tolerance. PFEM is validated on a broad rang

## 397. Pretrain Finite Element Method: A Pretraining and Warm-start Framework for PDEs via Physics-Informed Neural Operators

- year: 2026 | venue: arXiv (Cornell University) | tier: A | relevance: 3 | citations: 0
- doi: 10.48550/arxiv.2601.03086 | key: `doi:10.48550/arxiv.2601.03086`
- source: Q1

**Abstract**: We propose a Pretrained Finite Element Method (PFEM),a physics driven framework that bridges the efficiency of neural operator learning with the accuracy and robustness of classical finite element methods (FEM). PFEM consists of a physics informed pretraining stage and an optional finetuning stage. In the pretraining stage, a neural operator based on the Transolver architecture is trained solely from governing partial differential equations, without relying on labeled solution data. The model operates directly on unstructured point clouds, jointly encoding geometric information, material properties, and boundary conditions, and produces physically consistent initial solutions with extremely high computational efficiency. PDE constraints are enforced through explicit finite element, based differentiation, avoiding the overhead associated with automatic differentiation. In the fine-tuning stage, the pretrained prediction is used as an initial guess for conventional FEM solvers, preserving their accuracy, convergence guarantees, and extrapolation capability while substantially reducing the number of iterations required to reach a prescribed tolerance. PFEM is validated on a broad rang

## 398. Accelerated Discovery and Stability Prediction of Lead-Free Halide Perovskites via Physics-Informed Machine Learning

- year: 2026 | venue: Zenodo (CERN European Organization for Nuclear Research) | tier: A | relevance: 3 | citations: 0
- doi: 10.5281/zenodo.18776434 | key: `doi:10.5281/zenodo.18776434`
- source: Q1

**Abstract**: Metal halide perovskites have emerged as promising candidates for advanced photovoltaic and optoelectronic devices; however, their commercial deployment is significantly limited by the toxicity and chemical instability of lead-based compositions . All-inorganic lead-free alternatives, particularly cesium tin mixed-halide perovskites, (CsSn(ClxBryI1−x−y)3) provide a viable pathway to environmentally benign and thermally stable materials . However, identifying experimentally realizable compositions remains challenging due to the vast combinatorial compositional space and the persistent discrepancy between theoretical stability and practicalsynthesis.This study develops a physics-informed and explainable machine learning framework to predict the synthesizability and thermodynamic stability of mixed-halide tin perovskites . A Positive-Unlabeled learning strategy, utilizing transductive bagging and decision tree classifiers, estimates synthesis probability based on literature-derived data [5]. A 76-dimensional descriptorset, incorporating compositional, elemental, structural, and density functional theory (DFT)-derived thermodynamic parameters, is constructed . Gradient boosting regress

## 399. Physics-Informed and Geometry-Consistent Dual-View UAV Infrared Object Detection With Thermal Statistical Priors and Voxel-BEV Fusion

- year: 2026 | venue: IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing | tier: A | relevance: 3 | citations: 0
- doi: 10.1109/jstars.2026.3706420 | key: `doi:10.1109/jstars.2026.3706420`
- source: Q1

**Abstract**: Infrared imagery is valuable for UAV-based earth observation because it remains effective at night and under weak illumination, but collaborative dual-view detection still faces two coupled bottlenecks: weak thermal texture in the image plane and large-parallax misalignment across views. This article addresses these issues with a physics-informed and geometry-consistent framework for dual-view UAV infrared object detection. First, a Thermal-Spatial joint patch embedding module augments visual tokens with local thermal statistics, namely mean, variance, skewness, and kurtosis, so that target-background differences are encoded before high-level semantic fusion. Second, a Voxel-BEV fusion module lifts features from both cameras into a shared world coordinate system, aggregates them inside a tolerance slab, and projects the fused representation back to a reference view for detection. The resulting pipeline avoids direct planar stitching while preserving complementary evidence from the auxiliary view. Experiments on the public DualView-Occlusion benchmark show that the proposed method reaches 90.9% mAP $_{50}$ and 84.1% recall, while maintaining strong robustness to viewpoint variation 

## 400. Data-free neural PDE solvers based on Graph Neural Networks and weak forms

- year: 2026 | venue: arXiv (Cornell University) | tier: A | relevance: 3 | citations: 0
- doi: — | key: `t:datafreeneuralpdesolversbasedongraphneuralnetworksandweakforms`
- source: Q1

**Abstract**: We present a physics-informed, data-free neural solver for partial differential equations, built on a graph neural network architecture that utilises message passing. By relying on the weak form of the problem, we use gradients of finite-element shape functions (which are therefore polynomials) rather than automatic differentiation operators to compute the residuals of the equation from the displacements predicted by the network itself. Our approach generalises to previously unseen load cases and geometries, achieving easily convergence errors in the residuals of less than 1% and being capable of scaling up to models of considerable size and arbitrary geometries. To ensure compliance with the laws of physics and provide guarantees regarding the inference, it is possible to use the residual itself as an error indicator for the inference, and thus perform a refinement at the testing stage if the residual tolerance set in advance by the user is not met. Examples are provided to demonstrate the performance of the proposed method. This results in a method that avoids the costly process of obtaining, curating and storing high-fidelity synthetic data for training the neural network. Whils
