# 期权晚报 2026-11-02（快照 16:40 ET）

📊 市场环境

SPY $752.10 ｜ QQQ $681.09
VIX 21.15 ↑8.9%（5D +15.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 22.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 11-02 10:00　【高】ISM 制造业 PMI　预测 54.6 ｜ 实际 55.5 ｜ 前值 54.5　✅ 今日已公布
- 周一 11-02 19:00　【高】Midterm Elections　实际 待公布　⏰ 今日
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.13 ｜ 实际 待公布 ｜ 前值 7.079
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48.2 ｜ 实际 待公布 ｜ 前值 48

🔍 重点速览
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **事件差分**: 11-04 ATM IV 90.5% vs 11-06 80.4%（差 +10.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-04 134P ΔOI +1,335（距现价 -1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 137.04 → 收盘 136.37（-0.5%） ｜ 今日高 142.05 ｜ 低 135.72 ｜ 昨收 134.72 → 收盘 136.37（+1.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.74 | OI比 1.01 | ATM IV 56.1% | Skew -1.5pp | Term 1.03 | ExpMove ±5.4%（近端） | Rank 55%
量化视角： IV 中性（Rank 55%）｜期限结构正常（Term 1.03）｜Put 保护异常便宜（Skew -1.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.74×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.01×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-04（2D）±5.4% ｜ 11-06（4D）±6.8% ｜ 11-09（7D）±7.4% ｜ 11-11（9D）±8.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -45,253,204 | GEX Change vs 上次快照 -18,876,515 | Flip: Primary Flip: 144.22（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 684 / LOW 207 / INVALID 537
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 144.22（全链重定价，覆盖 96%）
Put Wall 135（弱结构｜现价高于该位 1.0%）
最近结构参考: Put Wall 135（现价高于该位 1.0%）
量化视角： 负 Gamma（4525万，无历史分位）｜负 Gamma 加深（1888万）｜现价位于 Flip 下方 5.44%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（Put Wall，弱结构）；上方 140（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 144（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 80.0P — Vol 75 | 最新价 $0.01 | OI 156→7687 (ΔOI +7531张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7531张（+4827.6% vs前日OI），连续性待观察（方向未知）
11-06 140.0C — Vol 7,971 | 最新价 $2.97 | OI 884→7425 (ΔOI +6541张) | ΔOI/Volume 82.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6541张（+739.9% vs前日OI），连续性待观察（方向未知）
11-06 135.0P — Vol 7,721 | 最新价 $4.00 | OI 10615→16589 (ΔOI +5974张) | ΔOI/Volume 77.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5974张（+56.3% vs前日OI），连续性待观察（方向未知）
11-06 115.0P — Vol 2,434 | 最新价 $0.32 | OI 3789→9365 (ΔOI +5576张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5576张（+147.2% vs前日OI），连续性待观察（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 25,622 张（Put 19,081 / Call 6,541），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-04  C +5.4k / P +11.8k ｜ Activity HIGH ｜ 2D
11-06  C +31.3k / P +46.4k ｜ Activity HIGH ｜ 4D
11-09  C +1.4k / P +1.1k ｜ Activity HIGH ｜ 7D
11-11  C +0.9k / P +0.7k ｜ Activity HIGH ｜ 9D

📆 11-04 Forward Structure
存量OI: C 18.9k / P 23.5k，今日变化ΔOI: C +5.4k / P +11.8k，平值价格ATM: C $3.81 / P $3.55 ｜ ATM IV 90.5%，净 delta 敞口 -95k shares
Top ΔOI: P 125 +3,504 ｜ P 120 +1,881 ｜ P 134 +1,335
仓位参考: Max Pain 143 ｜ Call Wall 145（+6.3%，弱）（OI 2.0k） ｜ Put Wall 125（-8.3%）（OI 3.6k）
量化解读： 存量 Put 重｜ATM IV 90.5%｜历史 Rank 55%（近端代理）｜IV/RV 1.63×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 94,838 股

📆 11-06 Forward Structure
存量OI: C 169.3k / P 147.1k，今日变化ΔOI: C +31.3k / P +46.4k，平值价格ATM: C $4.79 / P $4.55 ｜ ATM IV 80.4%，净 delta 敞口 67k shares
Top ΔOI: C 140 +6,541 ｜ P 135 +5,974
仓位参考: Max Pain 145 ｜ Call Wall 150（+10.0%，弱）（OI 12.6k） ｜ Put Wall 140（+2.7%，弱）（OI 17.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 80.4%｜历史 Rank 55%（近端代理）｜IV/RV 1.45×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 66,819 股

📆 11-09 Forward Structure
存量OI: C 5.5k / P 3.6k，今日变化ΔOI: C +1.4k / P +1.1k，平值价格ATM: C $5.55 / P $4.60 ｜ ATM IV 65.5%，净 delta 敞口 -124 shares
Top ΔOI: C 150 +322 ｜ P 135 +211 ｜ C 140 +199
仓位参考: Max Pain 144 ｜ Call Wall 150（+10.0%，弱）（OI 0.6k） ｜ Put Wall 134（-1.7%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 65.5%｜历史 Rank 55%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 负 124 股

📆 11-11 Forward Structure
存量OI: C 2.1k / P 1.5k，今日变化ΔOI: C +0.9k / P +0.7k，平值价格ATM: C $6.45 / P $5.00 ｜ ATM IV 65.5%，净 delta 敞口 -5k shares
Top ΔOI: C 150 +274 ｜ C 145 +118 ｜ P 150 +98
仓位参考: Max Pain 142 ｜ Call Wall 150（+10.0%，弱）（OI 0.4k） ｜ Put Wall 135（-1.0%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 65.5%｜历史 Rank 55%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 负 4,678 股

📅 事件差分（观察，非因果）: 11-04（2D）ATM IV 90.5% vs 11-06 80.4%（差 +10.2pp）——覆盖 ISM 制造业 PMI、Midterm Elections 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/SPCX_evening.json