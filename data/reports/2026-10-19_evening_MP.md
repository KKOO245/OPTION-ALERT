# 期权晚报 2026-10-19（快照 16:40 ET）

📊 市场环境

SPY $766.48 ｜ QQQ $718.36
VIX 18.44 ↓7.8%（5D +21.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 23.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 40P ΔOI +873（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-23 36P ΔOI +2,666 占该期限总 OI 18.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 40.75 → 收盘 38.95（-4.4%） ｜ 今日高 40.75 ｜ 低 38.92 ｜ 昨收 40.17 → 收盘 38.95（-3.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-22，窗口结束前不做对错判定）

Options: P/C成交量 0.62 | OI比 1.34 | ATM IV 65.5% | Skew -3.9pp | Term 1.02 | ExpMove ±5.3%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构正常（Term 1.02）｜Put 保护异常便宜（Skew -3.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.34×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-23（4D）±5.3% ｜ 10-30（11D）±8.4% ｜ 11-06（18D）±14.9% ｜ 11-13（25D）±6.4%
   ⇒ IV–VIX Spread: +47.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,299,492 | GEX Change vs 上次快照 -664,063 | Flip: Primary Flip: 43.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 221 / LOW 62 / INVALID 221
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 43.33（全链重定价，覆盖 99%）
Put Wall 40（弱结构｜现价低于该位 2.6%）
最近结构参考: Put Wall 40（现价低于该位 2.6%）
量化视角： 负 Gamma（330万，无历史分位）｜负 Gamma 加深（66万）｜现价位于 Flip 下方 10.12%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 40（Put Wall，弱结构） / 44（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 43（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 36.5P — Vol 14 | 最新价 $0.21 | OI 27→2693 (ΔOI +2666张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2666张（+9874.1% vs前日OI），连续性待观察（方向未知）
10-23 40.0P — Vol 292 | 最新价 $1.36 | OI 308→1181 (ΔOI +873张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增873张（+283.4% vs前日OI），连续性待观察（方向未知）
10-23 45.0C — Vol 366 | 最新价 $0.05 | OI 269→773 (ΔOI +504张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增504张（+187.4% vs前日OI），连续性待观察（方向未知）
11-20 70.0C — Vol 2 | 最新价 $0.04 | OI 1025→1525 (ΔOI +500张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增500张（+48.8% vs前日OI），连续性待观察（方向未知）
10-23 36.0P — Vol 77 | 最新价 $0.15 | OI 54→546 (ΔOI +492张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增492张（+911.1% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,035 张（Put 4,031 / Call 1,004），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +1.1k / P +4.6k ｜ Activity HIGH ｜ 4D
10-30  C +0.2k / P +1.0k ｜ Activity HIGH ｜ 11D
11-06  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 18D
11-13  C +36 / P +46 ｜ Activity MEDIUM △ ｜ 25D

📆 10-23 Forward Structure
存量OI: C 6.3k / P 8.5k，今日变化ΔOI: C +1.1k / P +4.6k，平值价格ATM: C $1.08 / P $1.00 ｜ ATM IV 65.5%，净 delta 敞口 -133k shares
Top ΔOI: P 36 +2,666 ｜ P 40 +873
仓位参考: Max Pain 44 ｜ Call Wall 42（+7.8%，弱）（OI 0.2k） ｜ Put Wall 36.5（-6.3%）（OI 2.7k）
量化解读： 存量 Put 重｜ATM IV 65.5%｜历史 Rank 48%（近端代理）｜IV/RV 1.32×（近似）｜净 delta 敞口 负 132,566 股

📆 10-30 Forward Structure
存量OI: C 6.6k / P 6.1k，今日变化ΔOI: C +0.2k / P +1.0k，平值价格ATM: C $1.70 / P $1.57 ｜ ATM IV 61.7%，净 delta 敞口 -39k shares
Top ΔOI: P 38 +441 ｜ P 37 +337 ｜ P 36 +100
仓位参考: Max Pain 45 ｜ Put Wall 38（-2.4%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 61.7%｜历史 Rank 48%（近端代理）｜IV/RV 1.25×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 39,237 股

11-06（MEDIUM △）仓位参考: Max Pain 43 ｜ Call Wall 40（+2.7%，弱）（OI 0.3k） ｜ Put Wall 38（-2.4%）（OI 0.8k）

11-13（MEDIUM △）仓位参考: Max Pain 50 ｜ Put Wall 39（+0.1%）（OI 0.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=57 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=57）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/MP_evening.json