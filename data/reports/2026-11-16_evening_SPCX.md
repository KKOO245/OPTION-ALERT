# 期权晚报 2026-11-16（快照 16:40 ET）

📊 市场环境

SPY $739.95 ｜ QQQ $661.75
VIX 22.91 ↑18.7%（5D +15.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.8
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🟡 **近现价集中开仓**: 11-18 133P ΔOI +694（距现价 -3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-23 126P ΔOI +1,576 占该期限总 OI 19.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 138.45 → 收盘 137.36（-0.8%） ｜ 今日高 139.98 ｜ 低 135.73 ｜ 昨收 139.11 → 收盘 137.36（-1.3%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-19，窗口结束前不做对错判定）

Options: P/C成交量 0.48 | OI比 0.56 | ATM IV 79.5% | Skew 6.6pp | Term 0.74 | ExpMove ±4.7%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价显著（Skew 6.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.56）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-18（2D）±4.7% ｜ 11-20（4D）±6.6% ｜ 11-23（7D）±7.4% ｜ 11-25（9D）±7.7%
   ⇒ IV–VIX Spread: +56.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -20,555,008 | GEX Change vs 上次快照 -4,577,018 | Flip: Primary Flip: 139.09（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 718 / LOW 238 / INVALID 592
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 139.09（全链重定价，覆盖 93%）
Put Wall 130（弱结构｜现价高于该位 5.7%）
最近结构参考: Flip 139（现价低于该位 1.2%）
量化视角： 负 Gamma（2056万，无历史分位）｜负 Gamma 加深（458万）｜现价位于 Flip 下方 1.25%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 130（Put Wall，弱结构）；上方 140（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 139（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 140.0P — Vol 4,662 | 最新价 $5.85 | OI 29672→36362 (ΔOI +6690张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6690张（+22.6% vs前日OI），连续性待观察（方向未知）
11-20 120.0P — Vol 4,644 | 最新价 $0.40 | OI 18817→25254 (ΔOI +6437张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6437张（+34.2% vs前日OI），连续性待观察（方向未知）
量化视角： 2 个事件合计 ΔOI ≈ 13,127 张（Put 13,127 / Call 0），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-18  C +8.6k / P +4.5k ｜ Activity HIGH ｜ 2D
11-20  C +32.9k / P +48.1k ｜ Activity HIGH ｜ 4D
11-23  C +0.9k / P +2.0k ｜ Activity HIGH ｜ 7D
11-25  C +0.4k / P +1.4k ｜ Activity HIGH ｜ 9D

📆 11-18 Forward Structure
存量OI: C 22.6k / P 28.4k，今日变化ΔOI: C +8.6k / P +4.5k，平值价格ATM: C $3.45 / P $3.05 ｜ ATM IV 78.8%，净 delta 敞口 3k shares
Top ΔOI: C 150 +2,112 ｜ P 133 +694
仓位参考: Max Pain 140 ｜ Call Wall 150（+9.2%）（OI 3.8k） ｜ Put Wall 135（-1.7%，弱）（OI 10.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 78.8%｜历史 Rank 90%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,007 股

📆 11-20 Forward Structure
存量OI: C 506.5k / P 427.3k，今日变化ΔOI: C +32.9k / P +48.1k，平值价格ATM: C $4.75 / P $4.35 ｜ ATM IV 79.1%，净 delta 敞口 -210k shares
Top ΔOI: P 140 +6,690 ｜ P 120 +6,437 ｜ C 140 +5,261
仓位参考: Max Pain 145 ｜ Call Wall 145（+5.6%，弱）（OI 42.9k） ｜ Put Wall 140（+1.9%，弱）（OI 36.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 79.1%｜历史 Rank 90%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 209,553 股

📆 11-23 Forward Structure
存量OI: C 4.5k / P 3.7k，今日变化ΔOI: C +0.9k / P +2.0k，平值价格ATM: C $5.45 / P $4.76 ｜ ATM IV 66.5%，净 delta 敞口 -18k shares
Top ΔOI: P 126 +1,576 ｜ C 146 +339 ｜ P 142 +101
仓位参考: Max Pain 141 ｜ Call Wall 150（+9.2%，弱）（OI 1.0k） ｜ Put Wall 126（-8.3%）（OI 1.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 66.5%｜历史 Rank 90%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 18,077 股

📆 11-25 Forward Structure
存量OI: C 1.8k / P 2.1k，今日变化ΔOI: C +0.4k / P +1.4k，平值价格ATM: C $5.95 / P $4.60 ｜ ATM IV 65.0%，净 delta 敞口 -33k shares
Top ΔOI: P 130 +1,301 ｜ C 140 +77
仓位参考: Max Pain 140 ｜ Call Wall 145（+5.6%，弱）（OI 0.4k） ｜ Put Wall 130（-5.4%）（OI 1.4k）
量化解读： 存量两侧均衡｜ATM IV 65.0%｜历史 Rank 90%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 负 32,799 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/SPCX_evening.json