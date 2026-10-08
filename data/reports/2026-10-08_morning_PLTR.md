# 期权晨报 2026-10-08（快照 10:20 ET）

📊 市场环境

SPY $774.21 ｜ QQQ $747.58
VIX 15.43 ↑2.3%（5D -5.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **事件差分**: 10-09 ATM IV 58.1% vs 10-16 45.4%（差 +12.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-09 195C ΔOI -1,248（距现价 -3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 194.12 → 今开 199.00（+2.5%） | 较昨收变动（含盘初走势） ｜ 今日高 204.44 ｜ 低 197.00

Options: P/C成交量 0.27 | OI比 0.64 | ATM IV 58.1% | Skew -3.6pp | Term 1.02 | ExpMove ±2.8%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构正常（Term 1.02）｜Put 保护异常便宜（Skew -3.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.27×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±2.8% ｜ 10-16（8D）±5.5% ｜ 10-23（15D）±7.2% ｜ 10-30（22D）±9.0%
   ⇒ IV–VIX Spread: +42.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 132,327,559 | GEX Change vs 上次快照 34,052,015 | Flip: Primary Flip: 184.55（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 584 / LOW 79 / INVALID 155
结构观察区: Primary Flip 184.55（全链重定价，覆盖 100%）
Call Wall 200（弱结构｜现价高于该位 0.7%）
最近结构参考: Call Wall 200（现价高于该位 0.7%）
量化视角： 正 Gamma（1.32亿，无历史分位）｜正 Gamma 增强（+3405万）｜现价位于 Flip 上方 9.17%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 188（MaxPain，仅结算参考） / 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 185（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 190.0P — Vol 2,793 | 最新价 $10.71 | OI 238→2956 (ΔOI +2718张) | ΔOI/Volume 97.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2718张（+1142.0% vs前日OI），连续性待观察（方向未知）
10-09 205.0C — Vol 10,321 | 最新价 $0.19 | OI 20524→22390 (ΔOI +1866张) | ΔOI/Volume 18.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1866张（+9.1% vs前日OI），连续性待观察（方向未知）
10-16 192.5P — Vol 2,767 | 最新价 $4.25 | OI 537→2247 (ΔOI +1710张) | ΔOI/Volume 61.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1710张（+318.4% vs前日OI），连续性待观察（方向未知）
10-16 205.0C — Vol 6,479 | 最新价 $1.48 | OI 5603→6876 (ΔOI +1273张) | ΔOI/Volume 19.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1273张（+22.7% vs前日OI），连续性待观察（方向未知）
10-09 192.5P — Vol 10,054 | 最新价 $1.85 | OI 1655→2886 (ΔOI +1231张) | ΔOI/Volume 12.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1231张（+74.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,798 张（Put 5,659 / Call 3,139），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +2.7k / P +0.5k ｜ Activity MEDIUM △ ｜ 1D
10-16  C +3.4k / P +5.2k ｜ Activity HIGH ｜ 8D
10-23  C +1.1k / P +1.0k ｜ Activity HIGH ｜ 15D
10-30  C +0.5k / P +1.6k ｜ Activity HIGH ｜ 22D

📆 10-09 Forward Structure
存量OI: C 125.1k / P 79.6k，今日变化ΔOI: C +2.7k / P +0.5k，平值价格ATM: C $2.24 / P $3.35 ｜ ATM IV 58.1%，净 delta 敞口 39k shares
Top ΔOI: C 205 +1,866 ｜ C 195 -1,248 ｜ P 190 -1,245
仓位参考: Max Pain 188 ｜ Call Wall 205（+1.8%，弱）（OI 22.4k） ｜ Put Wall 185（-8.2%，弱）（OI 8.9k）
量化解读： 存量 Call 重｜ATM IV 58.1%｜历史 Rank 91%（近端代理）｜IV/RV 2.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 39,071 股

📆 10-16 Forward Structure
存量OI: C 161.9k / P 197.1k，今日变化ΔOI: C +3.4k / P +5.2k，平值价格ATM: C $5.09 / P $6.00 ｜ ATM IV 45.4%，净 delta 敞口 80k shares
Top ΔOI: P 192 +1,710 ｜ C 205 +1,273 ｜ P 195 +1,132
仓位参考: Max Pain 170 ｜ Call Wall 200（-0.7%）（OI 17.6k） ｜ Put Wall 190（-5.7%，弱）（OI 4.9k）
量化解读： 存量 Put 重｜ATM IV 45.4%｜历史 Rank 91%（近端代理）｜IV/RV 2.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 79,877 股

📆 10-23 Forward Structure
存量OI: C 26.2k / P 20.3k，今日变化ΔOI: C +1.1k / P +1.0k，平值价格ATM: C $6.80 / P $7.70 ｜ ATM IV 44.0%，净 delta 敞口 42k shares
Top ΔOI: C 200 +569 ｜ C 205 +255
仓位参考: Max Pain 180 ｜ Call Wall 200（-0.7%，弱）（OI 3.0k） ｜ Put Wall 190（-5.7%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 44.0%｜历史 Rank 91%（近端代理）｜IV/RV 2.23×（近似）｜净 delta 敞口 正 41,541 股

📆 10-30 Forward Structure
存量OI: C 28.2k / P 20.1k，今日变化ΔOI: C +0.5k / P +1.6k，平值价格ATM: C $8.35 / P $9.70 ｜ ATM IV 44.3%，净 delta 敞口 -18k shares
Top ΔOI: P 190 +1,007 ｜ P 180 +301 ｜ C 200 -242
仓位参考: Max Pain 185 ｜ Call Wall 200（-0.7%，弱）（OI 3.1k） ｜ Put Wall 190（-5.7%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 44.3%｜历史 Rank 91%（近端代理）｜IV/RV 2.25×（近似）｜净 delta 敞口 负 17,957 股

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 58.1% vs 10-16 45.4%（差 +12.7pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/PLTR_morning.json