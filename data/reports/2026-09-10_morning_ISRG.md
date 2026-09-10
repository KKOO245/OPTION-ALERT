# 期权晨报 2026-09-10（快照 10:56 ET）

📊 市场环境

SPY $758.27 ｜ QQQ $708.69
VIX 17.34 ↑5.3%（5D +21.1%） ｜ Vol Regime: NORMAL
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
🟡 **单日价格波动**: +2.2%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-11 365C ΔOI +49（距现价 +1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 353.24 → 今开 348.20（-1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 361.49 ｜ 低 345.25

Options: P/C成交量 0.65 | OI比 0.58 | ATM IV 43.8% | Skew 2.2pp | Term 0.76 | ExpMove ±3.2%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价中性（Skew 2.2pp）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（1D）±3.2% ｜ 09-18（8D）±4.6% ｜ 09-25（15D）±6.3% ｜ 10-02（22D）±7.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,712,430 | GEX Change vs 上次快照 2,331,859 | Flip: Primary Flip: 374.28（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 286 / LOW 225 / INVALID 453
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 374.28（全链重定价，覆盖 91%）
Put Wall 350（弱结构｜现价高于该位 3.1%）
最近结构参考: Put Wall 350（现价高于该位 3.1%）
量化视角： 负 Gamma（171万，无历史分位）｜负 Gamma 缓解（+233万）｜现价位于 Flip 下方 3.58%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 350（Put Wall，弱结构） / 350（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 374（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 402.5C — Vol 82 | 最新价 $0.25 | OI 17→98 (ΔOI +81张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增81张（+476.5% vs前日OI），连续性待观察（方向未知）
09-18 400.0C — Vol 193 | 最新价 $0.24 | OI 1048→1124 (ΔOI +76张) | ΔOI/Volume 39.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增76张（+7.2% vs前日OI），连续性待观察（方向未知）
09-18 405.0C — Vol 83 | 最新价 $0.18 | OI 134→190 (ΔOI +56张) | ΔOI/Volume 67.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增56张（+41.8% vs前日OI），连续性待观察（方向未知）
09-11 365.0C — Vol 64 | 最新价 $1.00 | OI 99→148 (ΔOI +49张) | ΔOI/Volume 76.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增49张（+49.5% vs前日OI），连续性待观察（方向未知）
09-18 380.0C — Vol 74 | 最新价 $1.25 | OI 304→349 (ΔOI +45张) | ΔOI/Volume 60.8% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增45张（+14.8% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 307 张（Put 0 / Call 307），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +61 / P +2 ｜ Activity MEDIUM △ ｜ 1D
09-18  C +0.3k / P -32 ｜ Activity MEDIUM △ ｜ 8D
09-25  C +7 / P +29 ｜ Activity MEDIUM △ ｜ 15D
10-02  C -5 / P +0 ｜ Activity LOW ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 3.9k / P 2.3k
今日变化ΔOI: C +61 / P +2
平值价格ATM:  C 1.67 / P 9.80
隐含波动率 ATM IV:  43.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 365 ｜ +49 ｜ $1.00 ｜ 名义 $4.9k* ｜ +1.1%
C 350 ｜ -31 ｜ $6.40 ｜ 名义 $-19.8k* ｜ -3.0%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：365（+1.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 350（结算参考） ｜ Call Wall 360（-0.2%，弱）（OI 1.2k） ｜ Put Wall 342.5（-5.1%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 43.9%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,238 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）仓位参考: Max Pain 375（结算参考）

09-25（MEDIUM △）Top ΔOI: 360P +18 ｜ 365C +10
09-25（MEDIUM △）仓位参考: Max Pain 370（结算参考） ｜ Put Wall 360（-0.2%，弱）（OI 0.2k）

10-02（Activity LOW）仓位参考: Max Pain 365（结算参考） ｜ Put Wall 335（-7.2%）（OI 2.4k）

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 43.9% vs 09-18 34.1%（差 +9.7pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/ISRG_morning.json