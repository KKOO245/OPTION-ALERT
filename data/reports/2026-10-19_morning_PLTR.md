# 期权晨报 2026-10-19（快照 10:20 ET）

📊 市场环境

SPY $766.65 ｜ QQQ $721.21
VIX 18.46 ↓7.7%（5D +21.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 22.8（extreme fear）
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
🟡 **近现价集中开仓**: 10-23 195C ΔOI +12,191（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 186.03 → 今开 187.00（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 193.18 ｜ 低 186.15

Options: P/C成交量 0.41 | OI比 0.94 | ATM IV 53.7% | Skew 4.8pp | Term 1.16 | ExpMove ±4.7%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构正常偏陡（Term 1.16）｜保护溢价中性（Skew 4.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.41×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.94×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（4D）±4.7% ｜ 10-30（11D）±7.2% ｜ 11-06（18D）±12.8% ｜ 11-13（25D）±13.7%
   ⇒ IV–VIX Spread: +35.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 30,405,491 | GEX Change vs 上次快照 31,824,310 | Flip: Primary Flip: 180.59（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 659 / LOW 49 / INVALID 204
结构观察区: Primary Flip 180.59（全链重定价，覆盖 100%）
Call Wall 200（弱结构｜现价低于该位 4.4%）
最近结构参考: Call Wall 200（现价低于该位 4.4%）
量化视角： 正 Gamma（3041万，无历史分位）｜由负转正（+3182万）｜现价位于 Flip 上方 5.93%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 181（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 195.0C — Vol 20,058 | 最新价 $1.71 | OI 1432→13623 (ΔOI +12191张) | ΔOI/Volume 60.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12191张（+851.3% vs前日OI），连续性待观察（方向未知）
10-23 190.0C — Vol 16,273 | 最新价 $3.31 | OI 1106→11370 (ΔOI +10264张) | ΔOI/Volume 63.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10264张（+928.0% vs前日OI），连续性待观察（方向未知）
10-23 120.0P — Vol 7,543 | 最新价 $0.06 | OI 497→7913 (ΔOI +7416张) | ΔOI/Volume 98.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7416张（+1492.2% vs前日OI），连续性待观察（方向未知）
10-23 200.0C — Vol 18,937 | 最新价 $0.81 | OI 4063→10685 (ΔOI +6622张) | ΔOI/Volume 35.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6622张（+163.0% vs前日OI），连续性待观察（方向未知）
10-23 197.5C — Vol 11,511 | 最新价 $1.20 | OI 549→6846 (ΔOI +6297张) | ΔOI/Volume 54.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6297张（+1147.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 42,790 张（Put 7,416 / Call 35,374），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +56.9k / P +30.3k ｜ Activity HIGH ｜ 4D
10-30  C +2.9k / P +7.7k ｜ Activity HIGH ｜ 11D
11-06  C +3.4k / P +2.7k ｜ Activity MEDIUM △ ｜ 18D
11-13  C +0.9k / P +0.5k ｜ Activity MEDIUM △ ｜ 25D

📆 10-23 Forward Structure
存量OI: C 107.3k / P 101.0k，今日变化ΔOI: C +56.9k / P +30.3k，平值价格ATM: C $3.95 / P $5.00 ｜ ATM IV 53.7%，净 delta 敞口 1.7M shares
Top ΔOI: C 195 +12,191 ｜ C 190 +10,264
仓位参考: Max Pain 190 ｜ Call Wall 195（+1.9%，弱）（OI 13.6k） ｜ Put Wall 185（-3.3%，弱）（OI 4.1k）
量化解读： 存量两侧均衡｜ATM IV 53.7%｜历史 Rank 78%（近端代理）｜IV/RV 1.40×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,708,712 股

📆 10-30 Forward Structure
存量OI: C 45.3k / P 48.6k，今日变化ΔOI: C +2.9k / P +7.7k，平值价格ATM: C $6.34 / P $7.40 ｜ ATM IV 50.4%，净 delta 敞口 25k shares
Top ΔOI: P 190 +1,897 ｜ P 165 +1,028
仓位参考: Max Pain 190 ｜ Call Wall 205（+7.2%，弱）（OI 3.6k） ｜ Put Wall 190（-0.7%）（OI 6.1k）
量化解读： 存量两侧均衡｜ATM IV 50.4%｜历史 Rank 78%（近端代理）｜IV/RV 1.31×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 24,742 股

11-06（MEDIUM △）Top ΔOI: 165P +934 ｜ 150P +357
11-06（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 205（+7.2%，弱）（OI 1.6k） ｜ Put Wall 190（-0.7%）（OI 3.1k）

11-13（MEDIUM △）Top ΔOI: 155P -396 ｜ 180P -359
11-13（MEDIUM △）仓位参考: Max Pain 192 ｜ Call Wall 210（+9.8%，弱）（OI 1.0k） ｜ Put Wall 180（-5.9%，弱）（OI 1.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/PLTR_morning.json