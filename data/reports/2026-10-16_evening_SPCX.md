# 期权晚报 2026-10-16（快照 16:40 ET）

📊 市场环境

SPY $763.25 ｜ QQQ $709.80
VIX 19.99 ↑21.4%（5D +34.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 17.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-21 150C ΔOI +1,796（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-26 150C ΔOI +699 占该期限总 OI 10.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 146.1）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 147.82 → 收盘 146.03（-1.2%） ｜ 今日高 147.92 ｜ 低 142.96 ｜ 昨收 148.62 → 收盘 146.03（-1.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-21，窗口结束前不做对错判定）

Options: P/C成交量 0.84 | OI比 0.86 | ATM IV 58.4% | Skew 10.8pp | Term 1.01 | ExpMove ±2.9%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构正常（Term 1.01）｜保护溢价显著（Skew 10.8pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-19（3D）±2.9% ｜ 10-21（5D）±7.8% ｜ 10-23（7D）±8.7% ｜ 10-26（10D）±9.8%
   ⇒ IV–VIX Spread: +38.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -139,973 | GEX Change vs 上次快照 7,306,848 | Flip: Candidates 146.06 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 78%（带内） ｜ IV 有效性: VALID 745 / LOW 93 / INVALID 578
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈146（全链重定价，覆盖 78%，CONDITIONAL）
最近结构参考: Flip 146（现价低于该位 0.0%）
量化视角： 负 Gamma（14万，无历史分位）｜负 Gamma 缓解（+731万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 147（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 146（全链重定价，覆盖 78%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-19  C +8.6k / P +12.1k ｜ Activity HIGH ｜ 3D
10-21  C +7.4k / P +3.9k ｜ Activity HIGH ｜ 5D
10-23  C +13.3k / P +19.8k ｜ Activity HIGH ｜ 7D
10-26  C +1.9k / P +0.4k ｜ Activity HIGH ｜ 10D

📆 10-19 Forward Structure
存量OI: C 45.2k / P 34.8k，今日变化ΔOI: C +8.6k / P +12.1k，平值价格ATM: C $2.17 / P $2.09 ｜ ATM IV 39.9%，净 delta 敞口 161k shares
Top ΔOI: C 155 +2,232 ｜ P 135 +2,029
仓位参考: Max Pain 155 ｜ Call Wall 157.5（+7.9%，弱）（OI 4.6k） ｜ Put Wall 148（+1.3%）（OI 8.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 39.9%｜历史 Rank 70%（近端代理）｜IV/RV 0.78×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 160,683 股

📆 10-21 Forward Structure
存量OI: C 20.7k / P 11.0k，今日变化ΔOI: C +7.4k / P +3.9k，平值价格ATM: C $5.74 / P $5.65 ｜ ATM IV 83.6%，净 delta 敞口 134k shares
Top ΔOI: C 150 +1,796 ｜ C 146 +1,080 ｜ C 155 +618
仓位参考: Max Pain 150 ｜ Call Wall 150（+2.7%，弱）（OI 2.0k） ｜ Put Wall 147（+0.7%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 83.6%｜历史 Rank 70%（近端代理）｜IV/RV 1.64×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 134,384 股

📆 10-23 Forward Structure
存量OI: C 80.2k / P 91.0k，今日变化ΔOI: C +13.3k / P +19.8k，平值价格ATM: C $6.43 / P $6.33 ｜ ATM IV 78.7%，净 delta 敞口 -107k shares
Top ΔOI: P 136 +3,944 ｜ C 165 +3,424 ｜ P 145 +3,095
仓位参考: Max Pain 155 ｜ Call Wall 155（+6.1%，弱）（OI 7.8k） ｜ Put Wall 140（-4.1%，弱）（OI 7.8k）
量化解读： 存量两侧均衡｜ATM IV 78.7%｜历史 Rank 70%（近端代理）｜IV/RV 1.54×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 106,502 股

📆 10-26 Forward Structure
存量OI: C 4.1k / P 2.7k，今日变化ΔOI: C +1.9k / P +0.4k，平值价格ATM: C $6.80 / P $7.45 ｜ ATM IV 69.6%，净 delta 敞口 52k shares
Top ΔOI: C 150 +699 ｜ C 155 +417 ｜ P 144 -167
仓位参考: Max Pain 150 ｜ Call Wall 155（+6.1%，弱）（OI 0.8k） ｜ Put Wall 144（-1.4%）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 69.6%｜历史 Rank 70%（近端代理）｜IV/RV 1.36×（近似）｜净 delta 敞口 正 52,269 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/SPCX_evening.json