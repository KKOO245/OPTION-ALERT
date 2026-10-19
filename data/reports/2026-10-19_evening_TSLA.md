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
🔴 **事件差分**: 10-23（4D）ATM IV 76.6% vs 10-26 61.4%（差 +15.2pp），覆盖 建筑许可 Prel、新屋开工
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-26 360P ΔOI +681（距现价 -2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-28 350P ΔOI +1,196 占该期限总 OI 12.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 357.48 → 收盘 368.06（+3.0%） ｜ 今日高 369.58 ｜ 低 354.47 ｜ 昨收 354.72 → 收盘 368.06（+3.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.81 | OI比 0.46 | ATM IV 21.4% | Skew -6.0pp | Term 2.09 | ExpMove ±6.4%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构正常偏陡（Term 2.09）｜Put 保护异常便宜（Skew -6.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.81×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（4D）±6.4% ｜ 10-26（7D）±6.7% ｜ 10-28（9D）±7.0% ｜ 10-30（11D）±7.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 84,121,904 | GEX Change vs 上次快照 24,579,637 | Flip: Primary Flip: 345.40（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 1088 / LOW 151 / INVALID 781
结构观察区: Primary Flip 345.40（全链重定价，覆盖 88%）
Call Wall 400（现价低于该位 8.0%）
最近结构参考: Flip 345（现价高于该位 6.6%）
量化视角： 正 Gamma（8412万，无历史分位）｜正 Gamma 增强（+2458万）｜现价位于 Flip 上方 6.56%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 360（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 345（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 130.0P — Vol 213 | 最新价 $0.01 | OI 1545→24561 (ΔOI +23016张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23016张（+1489.7% vs前日OI），连续性待观察（方向未知）
10-23 220.0P — Vol 271 | 最新价 $0.02 | OI 3760→21096 (ΔOI +17336张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17336张（+461.1% vs前日OI），连续性待观察（方向未知）
10-23 180.0P — Vol 1,111 | 最新价 $0.01 | OI 85→12034 (ΔOI +11949张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11949张（+14057.6% vs前日OI），连续性待观察（方向未知）
10-23 210.0P — Vol 3,024 | 最新价 $0.04 | OI 157→8788 (ΔOI +8631张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8631张（+5497.4% vs前日OI），连续性待观察（方向未知）
10-23 370.0C — Vol 13,413 | 最新价 $10.90 | OI 1652→8267 (ΔOI +6615张) | ΔOI/Volume 49.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6615张（+400.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 67,547 张（Put 60,932 / Call 6,615），跨 1 个期限｜远端彩票/名义（4 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +65.4k / P +80.7k ｜ Activity HIGH ｜ 4D
10-26  C +5.3k / P +3.6k ｜ Activity HIGH ｜ 7D
10-28  C +1.5k / P +2.5k ｜ Activity HIGH ｜ 9D
10-30  C +3.6k / P +4.3k ｜ Activity HIGH ｜ 11D

📆 10-23 Forward Structure
存量OI: C 163.6k / P 148.1k，今日变化ΔOI: C +65.4k / P +80.7k，平值价格ATM: C $12.18 / P $11.41 ｜ ATM IV 76.6%，净 delta 敞口 1.8M shares
仓位参考: Max Pain 365 ｜ Call Wall 400（+8.7%，弱）（OI 10.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 76.6%｜历史 Rank 40%（近端代理）｜IV/RV 2.65×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,842,629 股

📆 10-26 Forward Structure
存量OI: C 10.3k / P 10.1k，今日变化ΔOI: C +5.3k / P +3.6k，平值价格ATM: C $12.55 / P $11.95 ｜ ATM IV 61.4%，净 delta 敞口 52k shares
Top ΔOI: P 360 +681 ｜ P 350 +519
仓位参考: Max Pain 365 ｜ Call Wall 400（+8.7%，弱）（OI 1.0k） ｜ Put Wall 360（-2.2%，弱）（OI 1.0k）
量化解读： 存量两侧均衡｜ATM IV 61.4%｜历史 Rank 40%（近端代理）｜IV/RV 2.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 51,764 股

📆 10-28 Forward Structure
存量OI: C 4.9k / P 4.8k，今日变化ΔOI: C +1.5k / P +2.5k，平值价格ATM: C $12.60 / P $13.10 ｜ ATM IV 60.1%，净 delta 敞口 2k shares
Top ΔOI: P 350 +1,196 ｜ P 330 +370 ｜ C 377 +185
仓位参考: Max Pain 360 ｜ Call Wall 400（+8.7%，弱）（OI 0.5k） ｜ Put Wall 350（-4.9%）（OI 1.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 60.1%｜历史 Rank 40%（近端代理）｜IV/RV 2.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,150 股

📆 10-30 Forward Structure
存量OI: C 68.8k / P 56.7k，今日变化ΔOI: C +3.6k / P +4.3k，平值价格ATM: C $14.76 / P $13.70 ｜ ATM IV 55.7%，净 delta 敞口 168k shares
Top ΔOI: C 380 +1,191 ｜ P 305 +1,024
仓位参考: Max Pain 370 ｜ Call Wall 400（+8.7%）（OI 9.7k） ｜ Put Wall 380（+3.2%，弱）（OI 3.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 55.7%｜历史 Rank 40%（近端代理）｜IV/RV 1.93×（近似）｜净 delta 敞口 正 167,806 股

📅 事件差分（观察，非因果）: 10-23（4D）ATM IV 76.6% vs 10-26 61.4%（差 +15.2pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/TSLA_evening.json