# 期权晚报 2026-10-19（快照 16:40 ET）

📊 市场环境

SPY $766.48 ｜ QQQ $718.36
VIX 18.44 ↓7.8%（5D +21.2%） ｜ Vol Regime: NORMAL
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
🟡 **近现价集中开仓**: 10-30 1350C ΔOI +127（距现价 -1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,358.50 → 收盘 1,371.12（+0.9%） ｜ 今日高 1407.00 ｜ 低 1357.64 ｜ 昨收 1,299.30 → 收盘 1,371.12（+5.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.58 | OI比 0.93 | ATM IV 77.4% | Skew 2.1pp | Term 0.95 | ExpMove ±6.5%（近端） | Rank 36%
量化视角： IV 中性（Rank 36%）｜期限结构正常（Term 0.95）｜保护溢价中性（Skew 2.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.93×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（4D）±6.5% ｜ 10-30（11D）±12.6% ｜ 11-06（18D）±14.2% ｜ 11-13（25D）±15.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,475,839 | GEX Change vs 上次快照 -43,687 | Flip: Primary Flip: 1418.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1979 / LOW 317 / INVALID 1100
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1418.05（全链重定价，覆盖 100%）
Call Wall 1,500（现价低于该位 8.6%）
最近结构参考: Flip 1418（现价低于该位 3.3%）
量化视角： 负 Gamma（248万，无历史分位）｜负 Gamma 加深（4万）｜现价位于 Flip 下方 3.31%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,465（MaxPain，仅结算参考） / 1,500（Call Wall）。
• Gamma 区域：切换参考 1418（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 700.0P — Vol 53 | 最新价 $0.10 | OI 0→1551 (ΔOI +1551张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增1551张（前日OI缺失），值得跟踪（方向未知）
10-23 640.0P — Vol 13 | 最新价 $0.05 | OI 0→874 (ΔOI +874张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增874张（前日OI缺失），值得跟踪（方向未知）
10-23 830.0P — Vol 5 | 最新价 $0.10 | OI 18→812 (ΔOI +794张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增794张（+4411.1% vs前日OI），连续性待观察（方向未知）
10-23 1550.0C — Vol 3,009 | 最新价 $3.85 | OI 764→1387 (ΔOI +623张) | ΔOI/Volume 20.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增623张（+81.5% vs前日OI），连续性待观察（方向未知）
10-23 850.0P — Vol 244 | 最新价 $0.08 | OI 125→730 (ΔOI +605张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增605张（+484.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,447 张（Put 3,824 / Call 623），跨 1 个期限｜远端彩票/名义（4 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +7.6k / P +10.2k ｜ Activity HIGH ｜ 4D
10-30  C +2.4k / P +0.8k ｜ Activity HIGH ｜ 11D
11-06  C +1.8k / P +0.7k ｜ Activity HIGH ｜ 18D
11-13  C +0.5k / P +0.2k ｜ Activity HIGH ｜ 25D

📆 10-23 Forward Structure
存量OI: C 36.0k / P 33.4k，今日变化ΔOI: C +7.6k / P +10.2k，平值价格ATM: C $45.20 / P $43.70 ｜ ATM IV 77.4%，净 delta 敞口 169k shares
仓位参考: Max Pain 1,465 ｜ Call Wall 1500（+9.4%）（OI 2.2k） ｜ Put Wall 1250（-8.8%，弱）（OI 1.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 77.4%｜历史 Rank 36%（近端代理）｜IV/RV 1.57×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 169,244 股

📆 10-30 Forward Structure
存量OI: C 22.4k / P 15.1k，今日变化ΔOI: C +2.4k / P +0.8k，平值价格ATM: C $90.86 / P $81.30 ｜ ATM IV 88.1%，净 delta 敞口 26k shares
Top ΔOI: C 1780 +162 ｜ C 1350 +127 ｜ P 1200 +123
仓位参考: Max Pain 1,520 ｜ Call Wall 1500（+9.4%，弱）（OI 1.5k） ｜ Put Wall 1400（+2.1%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 88.1%｜历史 Rank 36%（近端代理）｜IV/RV 1.79×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 25,769 股

📆 11-06 Forward Structure
存量OI: C 8.0k / P 6.9k，今日变化ΔOI: C +1.8k / P +0.7k，平值价格ATM: C $99.29 / P $94.87 ｜ ATM IV 79.9%，净 delta 敞口 36k shares
Top ΔOI: C 1400 +587 ｜ P 1200 +574
仓位参考: Max Pain 1,520 ｜ Call Wall 1400（+2.1%，弱）（OI 0.6k） ｜ Put Wall 1400（+2.1%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜ATM IV 79.9%｜历史 Rank 36%（近端代理）｜IV/RV 1.62×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 36,112 股

📆 11-13 Forward Structure
存量OI: C 3.5k / P 3.7k，今日变化ΔOI: C +0.5k / P +0.2k，平值价格ATM: C $111.95 / P $106.40 ｜ ATM IV 76.0%，净 delta 敞口 7k shares
Top ΔOI: C 1420 +80 ｜ P 1300 +78 ｜ C 1680 +62
仓位参考: Max Pain 1,520 ｜ Call Wall 1480（+7.9%，弱）（OI 0.2k） ｜ Put Wall 1300（-5.2%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 76.0%｜历史 Rank 36%（近端代理）｜IV/RV 1.54×（近似）｜净 delta 敞口 正 7,499 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/SNDK_evening.json