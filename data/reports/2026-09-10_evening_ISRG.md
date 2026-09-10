# 期权晚报 2026-09-10（快照 17:04 ET）

📊 市场环境

SPY $757.83 ｜ QQQ $708.69
VIX 17.84 ↑8.4%（5D +24.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-10 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.4 ｜ 前值 0.1　✅ 今日已公布
- 周四 09-10 10:00　【高】成屋销售　预测 3.98 ｜ 实际 3.98 ｜ 前值 4.06　✅ 今日已公布
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.2
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 待公布 ｜ 前值 3.4
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 待公布 ｜ 前值 2.5
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 待公布 ｜ 前值 51.7

🔍 重点速览
🔴 **事件差分**: 09-11（1D）ATM IV 52.3% vs 09-18 34.6%（差 +17.8pp），覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **单日价格波动**: +2.0%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-25 365C ΔOI +10（距现价 +1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 348.20 → 收盘 360.46（+3.5%） ｜ 今日高 362.48 ｜ 低 345.25 ｜ 昨收 353.24 → 收盘 360.46（+2.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.16 | OI比 0.58 | ATM IV 52.4% | Skew 10.8pp | Term 0.65 | ExpMove ±2.4%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.65，近月 IV 高于远月）｜保护溢价显著（Skew 10.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.16×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（1D）±2.4% ｜ 09-18（8D）±4.0% ｜ 09-25（15D）±7.0% ｜ 10-02（22D）±7.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,360,152 | GEX Change vs 上次快照 -647,722 | Flip: Primary Flip: 374.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 289 / LOW 203 / INVALID 472
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 374.35（全链重定价，覆盖 93%）
Put Wall 350（弱结构｜现价高于该位 3.0%）
最近结构参考: Put Wall 350（现价高于该位 3.0%）
量化视角： 负 Gamma（236万，无历史分位）｜负 Gamma 加深（65万）｜现价位于 Flip 下方 3.71%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 350（Put Wall，弱结构） / 350（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 374（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 402.5C — Vol 82（Yahoo补） | 最新价 $0.25 | OI 17→98 (ΔOI +81张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增81张（+476.5% vs前日OI），连续性待观察（方向未知）
09-18 400.0C — Vol 15 | 最新价 $0.25 | OI 1048→1124 (ΔOI +76张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增76张（+7.2% vs前日OI），值得跟踪（方向未知）
09-18 405.0C — Vol 1（Yahoo补） | 最新价 $0.18 | OI 134→190 (ΔOI +56张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增56张（+41.8% vs前日OI），值得跟踪（方向未知）
09-11 365.0C — Vol 22 | 最新价 $1.50 | OI 99→148 (ΔOI +49张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增49张（+49.5% vs前日OI），值得跟踪（方向未知）
09-18 380.0C — Vol 29 | 最新价 $1.87 | OI 304→349 (ΔOI +45张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增45张（量数据缺失），以日内换手为主
量化视角： 5 个事件合计 ΔOI ≈ 307 张（Put 0 / Call 307），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +61 / P +2 ｜ Activity LOW ｜ 1D
09-18  C +0.3k / P -32 ｜ Activity LOW ｜ 8D
09-25  C +7 / P +29 ｜ Activity MEDIUM △ ｜ 15D
10-02  C -5 / P +0 ｜ Activity MEDIUM △ ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 3.9k / P 2.3k
今日变化ΔOI: C +61 / P +2
平值价格ATM:  C 4.55 / P 4.20
隐含波动率 ATM IV:  52.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 365 ｜ +49 ｜ $1.50 ｜ 名义 $7.3k* ｜ +1.3%
C 350 ｜ -31 ｜ $12.00 ｜ 名义 $-37.2k* ｜ -2.9%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：365（+1.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 350（结算参考） ｜ Call Wall 360（-0.1%，弱）（OI 1.2k） ｜ Put Wall 342.5（-5.0%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 52.3%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,171 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 375（结算参考）

09-25（MEDIUM △）Top ΔOI: 360P +18 ｜ 365C +10
09-25（MEDIUM △）仓位参考: Max Pain 370（结算参考） ｜ Put Wall 360（-0.1%，弱）（OI 0.2k）

10-02（MEDIUM △）Top ΔOI: 350P -7 ｜ 325P +6
10-02（MEDIUM △）仓位参考: Max Pain 365（结算参考） ｜ Put Wall 335（-7.1%）（OI 2.4k）

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 52.3% vs 09-18 34.6%（差 +17.8pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/ISRG_evening.json