# 期权晨报 2026-11-03（快照 10:20 ET）

📊 市场环境

SPY $755.34 ｜ QQQ $685.28
VIX 21.03 ↓0.6%（5D +20.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-03

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.1 ｜ 实际 7.523 ｜ 前值 7.19　✅ 今日已公布
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-04 47C ΔOI +2,566（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 45.57 → 今开 45.08（-1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 45.25 ｜ 低 44.92

Options: P/C成交量 0.43 | OI比 0.39 | ATM IV 58.5% | Skew 5.0pp | Term 0.73 | ExpMove ±2.8%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜保护溢价中性（Skew 5.0pp）｜存量 Call 偏重（OI比 0.39）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.39×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-04（1D）±2.8% ｜ 11-06（3D）±4.2% ｜ 11-09（6D）±4.6% ｜ 11-11（8D）±5.7%
   ⇒ IV–VIX Spread: +37.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,063,572 | GEX Change vs 上次快照 3,157,997 | Flip: Primary Flip: 44.99（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 678 / LOW 112 / INVALID 358
结构观察区: Primary Flip 44.99（全链重定价，覆盖 99%）
Put Wall 45（弱结构｜现价高于该位 0.2%）
最近结构参考: Put Wall 45（现价高于该位 0.2%）
量化视角： 正 Gamma（206万，无历史分位）｜由负转正（+316万）｜现价位于 Flip 上方 0.23%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 45（Put Wall，弱结构） / 45（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 45（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 48.0C — Vol 5,861 | 最新价 $1.04 | OI 1935→6154 (ΔOI +4219张) | ΔOI/Volume 72.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4219张（+218.0% vs前日OI），连续性待观察（方向未知）
11-04 47.0C — Vol 3,691 | 最新价 $0.18 | OI 625→3191 (ΔOI +2566张) | ΔOI/Volume 69.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2566张（+410.6% vs前日OI），连续性待观察（方向未知）
11-06 35.0P — Vol 2,518 | 最新价 $0.01 | OI 232→2689 (ΔOI +2457张) | ΔOI/Volume 97.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2457张（+1059.0% vs前日OI），连续性待观察（方向未知）
11-20 40.0P — Vol 6,146 | 最新价 $0.27 | OI 10408→12830 (ΔOI +2422张) | ΔOI/Volume 39.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2422张（+23.3% vs前日OI），连续性待观察（方向未知）
11-20 43.0P — Vol 2,525 | 最新价 $0.75 | OI 3343→5027 (ΔOI +1684张) | ΔOI/Volume 66.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1684张（+50.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 13,348 张（Put 6,563 / Call 6,785），跨 4 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-04  C +8.5k / P +3.7k ｜ Activity HIGH ｜ 1D
11-06  C +4.6k / P +3.7k ｜ Activity HIGH ｜ 3D
11-09  C +1.8k / P +1.4k ｜ Activity HIGH ｜ 6D
11-11  C +1.0k / P +0.4k ｜ Activity HIGH ｜ 8D

📆 11-04 Forward Structure
存量OI: C 32.7k / P 12.9k，今日变化ΔOI: C +8.5k / P +3.7k，平值价格ATM: C $0.66 / P $0.58 ｜ ATM IV 58.5%，净 delta 敞口 26k shares
Top ΔOI: C 47 +2,566 ｜ C 46 +1,156 ｜ C 49 +1,033
仓位参考: Max Pain 45 ｜ Call Wall 47（+4.2%，弱）（OI 3.2k） ｜ Put Wall 44（-2.4%，弱）（OI 2.9k）
量化解读： 存量 Call 重｜ATM IV 58.5%｜历史 Rank 90%（近端代理）｜IV/RV 1.42×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 26,211 股

📆 11-06 Forward Structure
存量OI: C 142.1k / P 40.3k，今日变化ΔOI: C +4.6k / P +3.7k，平值价格ATM: C $1.01 / P $0.88 ｜ ATM IV 55.4%，净 delta 敞口 89k shares
Top ΔOI: C 49 +1,202 ｜ C 47 +1,132
仓位参考: Max Pain 48 ｜ Put Wall 45（-0.2%，弱）（OI 4.6k）
量化解读： 存量 Call 重｜ATM IV 55.4%｜历史 Rank 90%（近端代理）｜IV/RV 1.35×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 88,942 股

📆 11-09 Forward Structure
存量OI: C 4.6k / P 3.5k，今日变化ΔOI: C +1.8k / P +1.4k，平值价格ATM: C $1.12 / P $0.97 ｜ ATM IV 45.1%，净 delta 敞口 -1k shares
Top ΔOI: C 47 +564 ｜ P 45 +303
仓位参考: Max Pain 46 ｜ Call Wall 47（+4.2%，弱）（OI 1.0k） ｜ Put Wall 43（-4.6%）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 45.1%｜历史 Rank 90%（近端代理）｜IV/RV 1.10×（近似）｜净 delta 敞口 负 1,219 股

📆 11-11 Forward Structure
存量OI: C 5.9k / P 1.9k，今日变化ΔOI: C +1.0k / P +0.4k，平值价格ATM: C $1.35 / P $1.20 ｜ ATM IV 47.3%，净 delta 敞口 4k shares
Top ΔOI: C 49 +182 ｜ P 44 +173
仓位参考: Max Pain 45 ｜ Call Wall 47（+4.2%，弱）（OI 0.6k） ｜ Put Wall 45（-0.2%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 47.3%｜历史 Rank 90%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 正 3,623 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/SLV_morning.json