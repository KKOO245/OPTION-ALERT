# 期权晚报 2026-10-02（快照 16:40 ET）

📊 市场环境

SPY $769.64 ｜ QQQ $749.58
VIX 15.31 ↓6.6%（5D +3.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 45P ΔOI +792（距现价 -4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 47.00 → 收盘 46.97（-0.1%） ｜ 今日高 47.38 ｜ 低 46.15 ｜ 昨收 46.09 → 收盘 46.97（+1.9%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-09，窗口结束前不做对错判定）

Options: P/C成交量 0.99 | OI比 0.58 | ATM IV 86.1% | Skew 0.8pp | Term 0.63 | ExpMove ±5.8%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.63，近月 IV 高于远月）｜保护溢价薄（Skew 0.8pp）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.99×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±5.8% ｜ 10-16（14D）±8.3% ｜ 10-23（21D）±11.0% ｜ 10-30（28D）±12.1%
   ⇒ IV–VIX Spread: +70.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,945,673 | GEX Change vs 上次快照 -1,179,498 | Flip: Primary Flip: 48.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 80%（带内） ｜ IV 有效性: VALID 262 / LOW 63 / INVALID 131
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 48.89（全链重定价，覆盖 80%）
Put Wall 45（现价高于该位 4.4%） | Call Wall 50（弱结构｜现价低于该位 6.1%）
最近结构参考: Flip 49（现价低于该位 3.9%）
量化视角： 负 Gamma（195万，无历史分位）｜负 Gamma 加深（118万）｜现价位于 Flip 下方 3.93%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 45（Put Wall） / 46（MaxPain，仅结算参考）；上方 50（Call Wall，弱结构）。
• Gamma 区域：切换参考 49（全链重定价，覆盖 80%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0.7k / P +0.7k ｜ Activity HIGH ｜ 7D
10-16  C -0.1k / P +1.8k ｜ Activity MEDIUM △ ｜ 14D
10-23  C +46 / P +69 ｜ Activity MEDIUM △ ｜ 21D
10-30  C +0.2k / P +0.1k ｜ Activity HIGH ｜ 28D

📆 10-09 Forward Structure
存量OI: C 6.7k / P 6.2k，今日变化ΔOI: C +0.7k / P +0.7k，平值价格ATM: C $1.35 / P $1.38 ｜ ATM IV 51.1%，净 delta 敞口 21k shares
仓位参考: Max Pain 49 ｜ Call Wall 50（+6.5%，弱）（OI 0.5k） ｜ Put Wall 47（+0.1%）（OI 2.2k）
量化解读： 存量两侧均衡｜ATM IV 51.1%｜历史 Rank 82%（近端代理）｜IV/RV 1.11×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 21,030 股

10-16（MEDIUM △）Top ΔOI: 45P +792 ｜ 44P +428
10-16（MEDIUM △）仓位参考: Max Pain 50 ｜ Call Wall 50（+6.5%，弱）（OI 3.8k） ｜ Put Wall 45（-4.2%，弱）（OI 4.4k）

10-23（MEDIUM △）Top ΔOI: 50C +74 ｜ 45C +43
10-23（MEDIUM △）仓位参考: Max Pain 50 ｜ Call Wall 50（+6.5%，弱）（OI 0.2k） ｜ Put Wall 45（-4.2%，弱）（OI 0.2k）

📆 10-30 Forward Structure
存量OI: C 2.8k / P 1.5k，今日变化ΔOI: C +0.2k / P +0.1k，平值价格ATM: C $2.83 / P $2.83 ｜ ATM IV 54.2%，净 delta 敞口 7k shares
Top ΔOI: C 46 +86 ｜ C 51 +62 ｜ C 50 +35
仓位参考: Max Pain 49 ｜ Call Wall 51（+8.6%，弱）（OI 0.3k） ｜ Put Wall 45（-4.2%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 54.2%｜历史 Rank 82%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 正 6,536 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/MP_evening.json