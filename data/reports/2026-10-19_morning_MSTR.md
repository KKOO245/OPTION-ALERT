# 期权晨报 2026-10-19（快照 10:20 ET）

📊 市场环境

SPY $766.48 ｜ QQQ $718.36
VIX 18.46 ↓7.7%（5D +21.4%） ｜ Vol Regime: NORMAL
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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 136.83 → 今开 139.07（+1.6%） | 较昨收变动（含盘初走势） ｜ 今日高 140.77 ｜ 低 138.37

Options: P/C成交量 0.30 | OI比 0.82 | ATM IV 78.8% | Skew 3.4pp | Term 0.91 | ExpMove ±6.8%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构正常（Term 0.91）｜保护溢价中性（Skew 3.4pp）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.30×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（4D）±6.8% ｜ 10-30（11D）±10.8% ｜ 11-06（18D）±0.0% ｜ 11-13（25D）±14.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 27,167,374 | GEX Change vs 上次快照 40,341,128 | Flip: Primary Flip: 131.54（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 552 / LOW 90 / INVALID 244
结构观察区: Primary Flip 131.54（全链重定价，覆盖 100%）
Call Wall 135（弱结构｜现价高于该位 2.6%）
最近结构参考: Call Wall 135（现价高于该位 2.6%）
量化视角： 正 Gamma（2717万，无历史分位）｜由负转正（+4034万）｜现价位于 Flip 上方 5.31%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（Call Wall，弱结构）；上方 141（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 132（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 148.0C — Vol 32,004 | 最新价 $1.57 | OI 174→23820 (ΔOI +23646张) | ΔOI/Volume 73.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23646张（+13589.7% vs前日OI），连续性待观察（方向未知）
10-23 155.0C — Vol 37,444 | 最新价 $0.69 | OI 11131→25868 (ΔOI +14737张) | ΔOI/Volume 39.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14737张（+132.4% vs前日OI），连续性待观察（方向未知）
10-23 70.0P — Vol 12,034 | 最新价 $0.06 | OI 1511→12552 (ΔOI +11041张) | ΔOI/Volume 91.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11041张（+730.7% vs前日OI），连续性待观察（方向未知）
10-23 147.0C — Vol 11,892 | 最新价 $1.77 | OI 480→10991 (ΔOI +10511张) | ΔOI/Volume 88.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10511张（+2189.8% vs前日OI），连续性待观察（方向未知）
11-20 140.0C — Vol 12,374 | 最新价 $10.85 | OI 2303→12516 (ΔOI +10213张) | ΔOI/Volume 82.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10213张（+443.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 70,148 张（Put 11,041 / Call 59,107），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +113.7k / P +47.2k ｜ Activity HIGH ｜ 4D
10-30  C +4.8k / P +7.4k ｜ Activity MEDIUM △ ｜ 11D
11-06  C +0.9k / P +1.8k ｜ Activity MEDIUM △ ｜ 18D
11-13  C +0.8k / P +2.2k ｜ Activity HIGH ｜ 25D

📆 10-23 Forward Structure
存量OI: C 208.7k / P 170.7k，今日变化ΔOI: C +113.7k / P +47.2k，平值价格ATM: C $4.61 / P $4.82 ｜ ATM IV 78.8%，净 delta 敞口 3.7M shares
Top ΔOI: C 148 +23,646 ｜ C 155 +14,737
仓位参考: Max Pain 141 ｜ Call Wall 148（+6.8%，弱）（OI 23.8k） ｜ Put Wall 140（+1.1%，弱）（OI 6.4k）
量化解读： 存量 Call 重｜ATM IV 78.8%｜历史 Rank 48%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,661,719 股

10-30（MEDIUM △）Top ΔOI: 117P +873
10-30（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 150（+8.3%，弱）（OI 1.1k） ｜ Put Wall 125（-9.8%）（OI 12.2k）

11-06（MEDIUM △）仓位参考: Max Pain 160 ｜ Put Wall 150（+8.3%，弱）（OI 2.2k）

📆 11-13 Forward Structure
存量OI: C 10.5k / P 19.4k，今日变化ΔOI: C +0.8k / P +2.2k，平值价格ATM: C $10.15 / P $10.35 ｜ ATM IV 72.6%，净 delta 敞口 -45k shares
Top ΔOI: C 144 +353 ｜ P 125 +308
仓位参考: Max Pain 162 ｜ Call Wall 144（+4.0%，弱）（OI 0.4k） ｜ Put Wall 150（+8.3%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 72.6%｜历史 Rank 48%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 负 45,052 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/MSTR_morning.json