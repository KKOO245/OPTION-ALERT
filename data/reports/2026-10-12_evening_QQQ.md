# 期权晚报 2026-10-12（快照 16:40 ET）

📊 市场环境

SPY $778.10 ｜ QQQ $746.04
VIX 15.21 ↑2.5%（5D -2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.96 ｜ 实际 待公布 ｜ 前值 3.98
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.7 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-13 770C ΔOI +2,986（距现价 +3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 749.64 → 收盘 746.04（-0.5%） ｜ 今日高 749.79 ｜ 低 744.84 ｜ 昨收 751.27 → 收盘 746.04（-0.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.84 | OI比 2.63 | ATM IV 10.8% | Skew 4.0pp | Term 1.71 | ExpMove ±0.6%（近端） | Rank 12%
量化视角： IV 历史低位（Rank 12%，期权偏便宜）｜期限结构正常偏陡（Term 1.71）｜保护溢价中性（Skew 4.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.63×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 24% ｜ P/C OI(近端) 94%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 24%）｜近端 Put 显著偏重（P/C OI 分位 94%，历史高位区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-13（1D）±0.6% ｜ 10-14（2D）±1.0% ｜ 10-15（3D）±1.2% ｜ 10-16（4D）±1.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -404,224,007 | GEX Change vs 上次快照 -75,414,870 | Flip: Primary Flip: 751.08（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 3184 / LOW 417 / INVALID 1465
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 751.08（全链重定价，覆盖 95%）
Call Wall 760（弱结构｜现价低于该位 1.8%）
最近结构参考: Flip 751（现价低于该位 0.7%）
量化视角： 负 Gamma（4.04亿，历史分位偏负区，比 76% 的交易日更负）｜负 Gamma 加深（7541万）｜现价位于 Flip 下方 0.67%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 751（MaxPain，仅结算参考） / 760（Call Wall，弱结构）。
• Gamma 区域：切换参考 751（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 710.0P — Vol 4,425 | 最新价 $4.39 | OI 798→10898 (ΔOI +10100张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10100张（+1265.7% vs前日OI），连续性待观察（方向未知）
11-13 690.0P — Vol 302 | 最新价 $3.31 | OI 8938→15200 (ΔOI +6262张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6262张（+70.1% vs前日OI），连续性待观察（方向未知）
11-13 725.0P — Vol 560 | 最新价 $8.61 | OI 9501→15726 (ΔOI +6225张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6225张（+65.5% vs前日OI），连续性待观察（方向未知）
10-16 700.0P — Vol 3,814 | 最新价 $0.09 | OI 59812→65862 (ΔOI +6050张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增6050张（+10.1% vs前日OI），值得跟踪（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 28,637 张（Put 28,637 / Call 0），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $12M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-13  C +16.1k / P +31.3k ｜ Activity HIGH ｜ 1D
10-14  C +5.8k / P +18.1k ｜ Activity HIGH ｜ 2D
10-15  C +13.4k / P +4.6k ｜ Activity HIGH ｜ 3D
10-16  C +9.1k / P +44.2k ｜ Activity MEDIUM △ ｜ 4D

📆 10-13 Forward Structure
存量OI: C 42.5k / P 123.6k，今日变化ΔOI: C +16.1k / P +31.3k，平值价格ATM: C $2.00 / P $2.31 ｜ ATM IV 13.7%，净 delta 敞口 -613k shares
Top ΔOI: C 770 +2,986 ｜ P 735 +2,224 ｜ P 708 +1,974
仓位参考: Max Pain 751 ｜ Call Wall 760（+1.9%，弱）（OI 2.8k） ｜ Put Wall 750（+0.5%，弱）（OI 12.7k）
量化解读： 存量 Put 重｜ATM IV 13.7%｜历史 Rank 12%（近端代理）｜IV/RV 1.01×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 612,880 股

📆 10-14 Forward Structure
存量OI: C 26.0k / P 65.3k，今日变化ΔOI: C +5.8k / P +18.1k，平值价格ATM: C $3.56 / P $3.78 ｜ ATM IV 16.6%，净 delta 敞口 -261k shares
Top ΔOI: P 725 +1,773 ｜ C 765 +1,274 ｜ P 746 +1,195
仓位参考: Max Pain 751 ｜ Call Wall 755（+1.2%，弱）（OI 2.3k） ｜ Put Wall 730（-2.2%，弱）（OI 2.8k）
量化解读： 存量 Put 重｜ATM IV 16.6%｜历史 Rank 12%（近端代理）｜IV/RV 1.22×（近似）｜净 delta 敞口 负 260,905 股

📆 10-15 Forward Structure
存量OI: C 30.0k / P 49.7k，今日变化ΔOI: C +13.4k / P +4.6k，平值价格ATM: C $4.47 / P $4.64 ｜ ATM IV 16.9%，净 delta 敞口 -35k shares
Top ΔOI: C 770 +5,037 ｜ C 767 +1,725 ｜ C 760 +1,698
仓位参考: Max Pain 750 ｜ Call Wall 767（+2.8%，弱）（OI 2.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 16.9%｜历史 Rank 12%（近端代理）｜IV/RV 1.24×（近似）｜净 delta 敞口 负 35,268 股

10-16（MEDIUM △）Top ΔOI: 700P +6,050 ｜ 725P -4,089
10-16（MEDIUM △）仓位参考: Max Pain 734 ｜ Call Wall 760（+1.9%，弱）（OI 66.6k） ｜ Put Wall 740（-0.8%，弱）（OI 29.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/QQQ_evening.json