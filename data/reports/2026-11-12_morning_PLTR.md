# 期权晨报 2026-11-12（快照 10:20 ET）

📊 市场环境

SPY $756.94 ｜ QQQ $685.60
VIX 18.45 ↑5.5%（5D -34.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 162P ΔOI +1,560（距现价 -4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 172.40 → 今开 169.94（-1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 171.56 ｜ 低 168.25

Options: P/C成交量 1.03 | OI比 0.63 | ATM IV 58.9% | Skew 3.8pp | Term 0.82 | ExpMove ±2.8%（近端） | Rank 73%
量化视角： IV 中性（Rank 73%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价中性（Skew 3.8pp）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.03×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±2.8% ｜ 11-20（8D）±6.3% ｜ 11-27（15D）±8.0% ｜ 12-04（22D）±9.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 53,231,760 | GEX Change vs 上次快照 -7,431,062 | Flip: Primary Flip: 161.29（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 491 / LOW 202 / INVALID 247
结构观察区: Primary Flip 161.29（全链重定价，覆盖 99%）
Call Wall 185（弱结构｜现价低于该位 7.9%）
最近结构参考: Flip 161（现价高于该位 5.7%）
量化视角： 正 Gamma（5323万，无历史分位）｜正 Gamma 减弱（743万）｜现价位于 Flip 上方 5.67%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 162（MaxPain，仅结算参考）；上方 185（Call Wall，弱结构）。
• Gamma 区域：切换参考 161（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 177.5C — Vol 3,464 | 最新价 $3.35 | OI 1021→3956 (ΔOI +2935张) | ΔOI/Volume 84.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2935张（+287.5% vs前日OI），连续性待观察（方向未知）
11-20 182.5C — Vol 4,225 | 最新价 $1.87 | OI 1272→3891 (ΔOI +2619张) | ΔOI/Volume 62.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2619张（+205.9% vs前日OI），连续性待观察（方向未知）
12-04 155.0P — Vol 2,579 | 最新价 $2.20 | OI 819→2863 (ΔOI +2044张) | ΔOI/Volume 79.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2044张（+249.6% vs前日OI），连续性待观察（方向未知）
11-13 162.5P — Vol 5,339 | 最新价 $0.33 | OI 1255→2815 (ΔOI +1560张) | ΔOI/Volume 29.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1560张（+124.3% vs前日OI），连续性待观察（方向未知）
11-13 175.0C — Vol 16,235 | 最新价 $1.66 | OI 6526→7957 (ΔOI +1431张) | ΔOI/Volume 8.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1431张（+21.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 10,589 张（Put 3,604 / Call 6,985），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +1.4k / P +2.4k ｜ Activity HIGH ｜ 1D
11-20  C +6.8k / P +1.5k ｜ Activity HIGH ｜ 8D
11-27  C +0.9k / P -72 ｜ Activity MEDIUM △ ｜ 15D
12-04  C +0.2k / P +3.2k ｜ Activity HIGH ｜ 22D

📆 11-13 Forward Structure
存量OI: C 139.8k / P 88.2k，今日变化ΔOI: C +1.4k / P +2.4k，平值价格ATM: C $2.72 / P $2.00 ｜ ATM IV 58.9%，净 delta 敞口 -136k shares
Top ΔOI: C 170 -1,765 ｜ P 162 +1,560 ｜ C 175 +1,431
仓位参考: Max Pain 162 ｜ Call Wall 165（-3.2%，弱）（OI 12.8k） ｜ Put Wall 165（-3.2%，弱）（OI 4.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 58.9%｜历史 Rank 73%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 135,998 股

📆 11-20 Forward Structure
存量OI: C 186.2k / P 189.9k，今日变化ΔOI: C +6.8k / P +1.5k，平值价格ATM: C $5.79 / P $4.91 ｜ ATM IV 51.3%，净 delta 敞口 185k shares
Top ΔOI: C 177 +2,935 ｜ C 182 +2,619 ｜ P 162 +1,384
仓位参考: Max Pain 175 ｜ Call Wall 180（+5.6%，弱）（OI 11.2k） ｜ Put Wall 185（+8.5%，弱）（OI 9.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 51.3%｜历史 Rank 73%（近端代理）｜IV/RV 0.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 185,050 股

11-27（MEDIUM △）Top ΔOI: 172C +250
11-27（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 180（+5.6%，弱）（OI 1.4k） ｜ Put Wall 170（-0.3%，弱）（OI 1.3k）

📆 12-04 Forward Structure
存量OI: C 15.9k / P 12.9k，今日变化ΔOI: C +0.2k / P +3.2k，平值价格ATM: C $8.80 / P $7.60 ｜ ATM IV 47.8%，净 delta 敞口 -43k shares
Top ΔOI: P 155 +2,044
仓位参考: Max Pain 175 ｜ Call Wall 185（+8.5%，弱）（OI 1.2k） ｜ Put Wall 155（-9.1%）（OI 2.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 47.8%｜历史 Rank 73%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 负 42,871 股

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 58.9% vs 11-20 51.3%（差 +7.7pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/PLTR_morning.json