# 期权晨报 2026-11-13（快照 10:20 ET）

📊 市场环境

SPY $750.54 ｜ QQQ $673.61
VIX 19.65 ↑5.1%（5D -23.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 11-20 ATM IV 104.8% vs 11-27 93.8%（差 +11.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 937.46 → 今开 915.86（-2.3%） | 较昨收变动（含盘初走势） ｜ 今日高 939.53 ｜ 低 853.75

Options: P/C成交量 1.03 | OI比 0.64 | ATM IV 147.4% | Skew 12.3pp | Term 0.62 | ExpMove ±11.7%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.62，近月 IV 高于远月）｜保护溢价显著（Skew 12.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.03×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±11.7% ｜ 11-27（14D）±19.1% ｜ 12-04（21D）±17.5% ｜ 12-11（28D）±16.0%
   ⇒ IV–VIX Spread: +127.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,273,192 | GEX Change vs 上次快照 -3,933,176 | Flip: Primary Flip: 893.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1788 / LOW 880 / INVALID 1364
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 893.87（全链重定价，覆盖 99%）
最近结构参考: Flip 894（现价低于该位 2.9%）
量化视角： 负 Gamma（327万，无历史分位）｜由正转负（393万）｜现价位于 Flip 下方 2.93%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 920（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 894（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 1000.0C — Vol 10,890 | 最新价 $3.70 | OI 2308→3510 (ΔOI +1202张) | ΔOI/Volume 11.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1202张（+52.1% vs前日OI），连续性待观察（方向未知）
11-20 600.0P — Vol 1,781 | 最新价 $0.85 | OI 1097→2212 (ΔOI +1115张) | ΔOI/Volume 62.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1115张（+101.6% vs前日OI），连续性待观察（方向未知）
11-20 500.0P — Vol 1,240 | 最新价 $0.30 | OI 530→1615 (ΔOI +1085张) | ΔOI/Volume 87.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1085张（+204.7% vs前日OI），连续性待观察（方向未知）
11-13 1050.0C — Vol 4,048 | 最新价 $0.95 | OI 1763→2821 (ΔOI +1058张) | ΔOI/Volume 26.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1058张（+60.0% vs前日OI），连续性待观察（方向未知）
11-13 930.0P — Vol 3,333 | 最新价 $18.50 | OI 271→931 (ΔOI +660张) | ΔOI/Volume 19.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增660张（+243.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,120 张（Put 2,860 / Call 2,260），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 59.5k / P 38.2k，今日成交量: C 20.3k / P 21.0k，平值价格ATM: C $14.80 / P $13.00 ｜ ATM IV 147.4%，预期波动 ±3.2%，Max Pain 920
Top ΔOI: C 1000 +1,202 ｜ C 1050 +1,058 ｜ P 930 +660

📆 Forward Expiration Structure

11-20  C +1.9k / P +4.0k ｜ Activity HIGH ｜ 7D
11-27  C +1.6k / P +0.2k ｜ Activity MEDIUM △ ｜ 14D
12-04  C +1.1k / P +0.3k ｜ Activity MEDIUM △ ｜ 21D
12-11  C +0.3k / P +0.2k ｜ Activity HIGH ｜ 28D

📆 11-20 Forward Structure
存量OI: C 79.0k / P 58.7k，今日变化ΔOI: C +1.9k / P +4.0k，平值价格ATM: C $51.34 / P $50.52 ｜ ATM IV 104.8%，净 delta 敞口 28k shares
Top ΔOI: P 600 +1,115
仓位参考: Max Pain 1,080 ｜ Call Wall 900（+3.7%，弱）（OI 1.5k） ｜ Put Wall 870（+0.3%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 104.8%｜历史 Rank 91%（近端代理）｜IV/RV 0.79×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 27,731 股

11-27（MEDIUM △）Top ΔOI: 940C +106 ｜ 810C +100
11-27（MEDIUM △）仓位参考: Max Pain 1,090 ｜ Put Wall 800（-7.8%，弱）（OI 0.3k）

12-04（MEDIUM △）Top ΔOI: 1200C +417 ｜ 1100C +101
12-04（MEDIUM △）仓位参考: Max Pain 980 ｜ Call Wall 950（+9.5%，弱）（OI 0.3k） ｜ Put Wall 820（-5.5%，弱）（OI 0.4k）

📆 12-11 Forward Structure
存量OI: C 5.2k / P 3.2k，今日变化ΔOI: C +0.3k / P +0.2k，平值价格ATM: C $95.00 / P $44.00 ｜ ATM IV 91.1%，净 delta 敞口 5k shares
Top ΔOI: C 1345 +64 ｜ P 850 +46
仓位参考: Max Pain 930 ｜ Call Wall 840（-3.2%，弱）（OI 53） ｜ Put Wall 830（-4.3%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 91.1%｜历史 Rank 91%（近端代理）｜IV/RV 0.68×（近似）｜净 delta 敞口 正 4,508 股

📅 事件差分（观察，非因果）: 11-20（7D）ATM IV 104.8% vs 11-27 93.8%（差 +11.0pp）——覆盖 PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/SNDK_morning.json