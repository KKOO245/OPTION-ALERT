# 期权晨报 2026-11-12（快照 10:20 ET）

📊 市场环境

SPY $756.94 ｜ QQQ $685.69
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
🔴 **事件差分**: 11-13（1D）ATM IV 127.8% vs 11-20 105.2%（差 +22.6pp），覆盖 成屋销售、PPI 生产者物价 MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 977.69 → 今开 888.10（-9.2%） | 较昨收变动（含盘初走势） ｜ 今日高 937.88 ｜ 低 869.49

Options: P/C成交量 0.53 | OI比 0.67 | ATM IV 127.8% | Skew 2.7pp | Term 0.70 | ExpMove ±6.0%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价中性（Skew 2.7pp）｜存量 Call 偏重（OI比 0.67）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.67×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±6.0% ｜ 11-20（8D）±12.6% ｜ 11-27（15D）±15.1% ｜ 12-04（22D）±17.8%
   ⇒ IV–VIX Spread: +109.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,117,865 | GEX Change vs 上次快照 -4,785,486 | Flip: Primary Flip: 910.84（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1847 / LOW 834 / INVALID 1351
结构观察区: Primary Flip 910.84（全链重定价，覆盖 100%）
最近结构参考: Flip 911（现价高于该位 1.2%）
量化视角： 正 Gamma（112万，无历史分位）｜正 Gamma 减弱（479万）｜现价位于 Flip 上方 1.21%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 930（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 911（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 1150.0C — Vol 6,566 | 最新价 $1.30 | OI 655→3059 (ΔOI +2404张) | ΔOI/Volume 36.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2404张（+367.0% vs前日OI），连续性待观察（方向未知）
11-13 1050.0C — Vol 4,698 | 最新价 $8.20 | OI 836→1763 (ΔOI +927张) | ΔOI/Volume 19.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增927张（+110.9% vs前日OI），连续性待观察（方向未知）
11-13 1200.0C — Vol 3,239 | 最新价 $0.68 | OI 1076→1936 (ΔOI +860张) | ΔOI/Volume 26.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增860张（+79.9% vs前日OI），连续性待观察（方向未知）
11-13 1100.0C — Vol 10,408 | 最新价 $3.07 | OI 2528→3195 (ΔOI +667张) | ΔOI/Volume 6.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增667张（+26.4% vs前日OI），连续性待观察（方向未知）
11-13 1225.0C — Vol 800 | 最新价 $0.55 | OI 154→757 (ΔOI +603张) | ΔOI/Volume 75.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增603张（+391.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,461 张（Put 0 / Call 5,461），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +6.4k / P +6.1k ｜ Activity HIGH ｜ 1D
11-20  C +2.0k / P +1.7k ｜ Activity HIGH ｜ 8D
11-27  C -0.7k / P +0.3k ｜ Activity HIGH ｜ 15D
12-04  C +0.7k / P +0.2k ｜ Activity MEDIUM △ ｜ 22D

📆 11-13 Forward Structure
存量OI: C 54.7k / P 36.7k，今日变化ΔOI: C +6.4k / P +6.1k，平值价格ATM: C $27.60 / P $28.00 ｜ ATM IV 127.8%，净 delta 敞口 -377k shares
Top ΔOI: C 1150 +2,404 ｜ C 1050 +927
仓位参考: Max Pain 930 ｜ Call Wall 1000（+8.5%，弱）（OI 2.3k） ｜ Put Wall 850（-7.8%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 127.8%｜历史 Rank 84%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 377,021 股

📆 11-20 Forward Structure
存量OI: C 77.1k / P 54.8k，今日变化ΔOI: C +2.0k / P +1.7k，平值价格ATM: C $59.24 / P $57.10 ｜ ATM IV 105.2%，净 delta 敞口 -42k shares
Top ΔOI: C 1080 -580 ｜ C 1030 +468 ｜ C 1260 -458
仓位参考: Max Pain 1,100 ｜ Call Wall 1000（+8.5%，弱）（OI 2.1k） ｜ Put Wall 870（-5.6%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 105.2%｜历史 Rank 84%（近端代理）｜IV/RV 0.79×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 41,948 股

📆 11-27 Forward Structure
存量OI: C 16.5k / P 9.6k，今日变化ΔOI: C -0.7k / P +0.3k，平值价格ATM: C $70.97 / P $68.00 ｜ ATM IV 93.2%，净 delta 敞口 12k shares
Top ΔOI: C 1300 -1,259 ｜ C 1270 -447 ｜ C 1130 +304
仓位参考: Max Pain 1,130 ｜ Put Wall 930（+0.9%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 93.2%｜历史 Rank 84%（近端代理）｜IV/RV 0.70×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 11,541 股

12-04（MEDIUM △）Top ΔOI: 1000C +76 ｜ 970C +55
12-04（MEDIUM △）仓位参考: Max Pain 990 ｜ Call Wall 950（+3.1%，弱）（OI 0.2k） ｜ Put Wall 830（-10.0%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 127.8% vs 11-20 105.2%（差 +22.6pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/SNDK_morning.json