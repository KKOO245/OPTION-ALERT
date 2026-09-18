# 期权晚报 2026-09-18（快照 16:40 ET）

📊 市场环境

SPY $761.69 ｜ QQQ $721.45
VIX 14.81 ↓4.1%（5D -6.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 29.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 150P ΔOI -1,912（距现价 -4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 150P ΔOI +254 占该期限总 OI 15.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 161.0）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 158.21 → 收盘 156.72（-0.9%） ｜ 今日高 159.19 ｜ 低 155.89 ｜ 昨收 158.25 → 收盘 156.72（-1.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-23，窗口结束前不做对错判定）

Options: P/C成交量 0.05 | OI比 1.42 | ATM IV 40.6% | Skew -5.4pp | Term 0.74 | ExpMove ±3.6%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.05×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.42×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（7D）±3.6% ｜ 10-02（14D）±4.2% ｜ 10-09（21D）±6.3% ｜ 10-16（28D）±6.7%
   ⇒ IV–VIX Spread: +25.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -42,917,868 | GEX Change vs 上次快照 35,044,023 | Flip: Candidates 161.01 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 72%（带内） ｜ IV 有效性: VALID 332 / LOW 128 / INVALID 394
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈161（全链重定价，覆盖 72%，CONDITIONAL）
Put Wall 150（现价高于该位 4.5%）
最近结构参考: Flip 161（现价低于该位 2.7%）
量化视角： 负 Gamma（4292万，无历史分位）｜负 Gamma 缓解（+3504万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall） / 156（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 161（全链重定价，覆盖 72%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +0.3k / P -1.0k ｜ Activity MEDIUM △ ｜ 7D
10-02  C +73 / P +0.2k ｜ Activity MEDIUM △ ｜ 14D
10-09  C +8 / P +0.5k ｜ Activity HIGH ｜ 21D
10-16  C +3.4k / P +6.8k ｜ Activity HIGH ｜ 28D

📆 09-25 Forward Structure
存量OI: C 7.2k / P 32.3k，今日变化ΔOI: C +0.3k / P -1.0k，平值价格ATM: C $2.74 / P $2.85 ｜ ATM IV 29.3%，净 delta 敞口 -19k shares
Top ΔOI: P 150 -1,912 ｜ P 157 +597 ｜ P 158 +339
仓位参考: Max Pain 158 ｜ Call Wall 160（+2.1%，弱）（OI 2.4k） ｜ Put Wall 150（-4.3%，弱）（OI 9.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 29.3%｜历史 Rank 86%（近端代理）｜IV/RV 1.27×（近似）｜净 delta 敞口 负 18,537 股

10-02（MEDIUM △）Top ΔOI: 158P +77 ｜ 164P +60
10-02（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 165（+5.3%）（OI 0.7k） ｜ Put Wall 157（+0.2%，弱）（OI 0.2k）

📆 10-09 Forward Structure
存量OI: C 0.3k / P 1.3k，今日变化ΔOI: C +8 / P +0.5k，平值价格ATM: C $3.37 / P $6.46 ｜ ATM IV 30.1%，净 delta 敞口 -8k shares
Top ΔOI: P 150 +254 ｜ C 158 +5
仓位参考: Max Pain 160 ｜ Call Wall 160（+2.1%，弱）（OI 18） ｜ Put Wall 150（-4.3%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 30.1%｜历史 Rank 86%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 8,422 股

📆 10-16 Forward Structure
存量OI: C 33.3k / P 53.6k，今日变化ΔOI: C +3.4k / P +6.8k，平值价格ATM: C $5.14 / P $5.31 ｜ ATM IV 29.9%，净 delta 敞口 -107k shares
Top ΔOI: P 153 +3,826 ｜ C 170 +2,054 ｜ P 150 +1,425
仓位参考: Max Pain 165 ｜ Call Wall 165（+5.3%，弱）（OI 2.3k） ｜ Put Wall 150（-4.3%）（OI 17.7k）
量化解读： 存量 Put 重｜ATM IV 29.9%｜历史 Rank 86%（近端代理）｜IV/RV 1.30×（近似）｜净 delta 敞口 负 107,409 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=24 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=24）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/XBI_evening.json