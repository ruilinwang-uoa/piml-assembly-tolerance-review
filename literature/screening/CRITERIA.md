# 筛查纳入标准（eligibility criteria，与稿件 §2.2 一致，逐字）

**纳入（include）** 要求同时满足：
1. 方法为 learning-based 或 physics-informed（含 loss-based / architecture-based / data-based / hybrid 任一物理融入机制）；
2. 应用对象为 tolerance analysis、assembly deviation/gap prediction、variation propagation、geometry assurance 之一，
   或其直接邻近（fixture layout、tolerance allocation、digital-twin geometry assurance）。

**排除（exclude）** 任一即排除：
1. 术语碰撞的域外工作（optical band gaps、seismic inversion、power systems、fluid/turbulence、biomedical 等）；
2. 无任何物理约束/物理融入机制的纯数据方法（此类若属容差/装配预测则归 M 组基线，标记 baseline 而非 include-physics）；
3. 与制造/装配/容差完全无关的一般 ML/PDE 方法工作。

**判决写法**：decisions.json 中每条 {doi_or_title_key: {"verdict": "include"|"exclude"|"baseline", "group": "G1..G8 或 null", "reason": "一句话"}}。
- include + group → 合并入编码表对应组；
- baseline → 记录但不入物理信息核心统计（M 组基线语义）；
- exclude → 仅留痕。
