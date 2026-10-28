# 期权晨报 2026-10-28（快照 10:20 ET）

📊 市场环境

SPY $770.28 ｜ QQQ $725.61
VIX 17.36 ↓0.9%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 4　✅ 今日已公布
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 222C ΔOI +2,305（距现价 +2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 217.94 → 今开 219.88（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 219.99 ｜ 低 217.27

Options: P/C成交量 0.63 | OI比 0.93 | ATM IV 46.6% | Skew 1.4pp | Term 0.86 | ExpMove ±2.6%（近端） | Rank 63%
量化视角： IV 中性（Rank 63%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价薄（Skew 1.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.93×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（2D）±2.6% ｜ 11-02（5D）±3.1% ｜ 11-04（7D）±4.1% ｜ 11-06（9D）±4.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 310,887,236 | GEX Change vs 上次快照 10,806,643 | Flip: Primary Flip: 210.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 746 / LOW 216 / INVALID 498
结构观察区: Primary Flip 210.89（全链重定价，覆盖 97%）
Put Wall 200（弱结构｜现价高于该位 8.9%） | Call Wall 230（现价低于该位 5.3%）
最近结构参考: Flip 211（现价高于该位 3.3%）
量化视角： 正 Gamma（3.11亿，无历史分位）｜正 Gamma 增强（+1081万）｜现价位于 Flip 上方 3.29%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构） / 215（MaxPain，仅结算参考）；上方 230（Call Wall）。
• Gamma 区域：切换参考 211（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-28 197.5P — Vol 10,697 | 最新价 $0.01 | OI 1052→10580 (ΔOI +9528张) | ΔOI/Volume 89.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9528张（+905.7% vs前日OI），连续性待观察（方向未知）
10-28 225.0C — Vol 43,728 | 最新价 $0.05 | OI 10969→19584 (ΔOI +8615张) | ΔOI/Volume 19.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8615张（+78.5% vs前日OI），连续性待观察（方向未知）
10-28 220.0C — Vol 156,720 | 最新价 $0.73 | OI 10010→16820 (ΔOI +6810张) | ΔOI/Volume 4.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6810张（+68.0% vs前日OI），连续性待观察（方向未知）
10-28 222.5C — Vol 77,080 | 最新价 $0.20 | OI 10960→16343 (ΔOI +5383张) | ΔOI/Volume 7.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5383张（+49.1% vs前日OI），连续性待观察（方向未知）
10-28 195.0P — Vol 7,128 | 最新价 $0.02 | OI 2559→5929 (ΔOI +3370张) | ΔOI/Volume 47.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3370张（+131.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 33,706 张（Put 12,898 / Call 20,808），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 132.5k / P 123.2k，今日成交量: C 132.6k / P 83.0k，平值价格ATM: C $1.52 / P $0.76 ｜ ATM IV 46.6%，预期波动 ±1.0%，Max Pain 215
Top ΔOI: P 197 +9,528 ｜ C 225 +8,615 ｜ C 220 +6,810

📆 Forward Expiration Structure

10-30  C +11.0k / P +5.9k ｜ Activity HIGH ｜ 2D
11-02  C +6.0k / P +7.8k ｜ Activity HIGH ｜ 5D
11-04  C +3.5k / P +2.0k ｜ Activity HIGH ｜ 7D
11-06  C +5.3k / P +5.5k ｜ Activity HIGH ｜ 9D

📆 10-30 Forward Structure
存量OI: C 482.8k / P 304.3k，今日变化ΔOI: C +11.0k / P +5.9k，平值价格ATM: C $3.30 / P $2.41 ｜ ATM IV 41.3%，净 delta 敞口 173k shares
Top ΔOI: C 230 +2,807 ｜ C 232 +2,586 ｜ C 222 +2,305
仓位参考: Max Pain 215 ｜ Call Wall 225（+3.3%，弱）（OI 59.2k） ｜ Put Wall 210（-3.6%，弱）（OI 23.5k）
量化解读： 存量 Call 重｜ATM IV 41.3%｜历史 Rank 63%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 173,228 股

📆 11-02 Forward Structure
存量OI: C 20.2k / P 20.2k，今日变化ΔOI: C +6.0k / P +7.8k，平值价格ATM: C $3.90 / P $2.91 ｜ ATM IV 32.4%，净 delta 敞口 -32k shares
Top ΔOI: P 215 +2,409 ｜ C 225 +1,633
仓位参考: Max Pain 215 ｜ Call Wall 230（+5.6%，弱）（OI 3.3k） ｜ Put Wall 215（-1.3%，弱）（OI 2.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 32.4%｜历史 Rank 63%（近端代理）｜IV/RV 1.18×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 32,005 股

📆 11-04 Forward Structure
存量OI: C 12.0k / P 8.0k，今日变化ΔOI: C +3.5k / P +2.0k，平值价格ATM: C $4.83 / P $4.05 ｜ ATM IV 34.9%，净 delta 敞口 69k shares
Top ΔOI: C 225 +745 ｜ C 217 +490 ｜ P 205 +468
仓位参考: Max Pain 215 ｜ Call Wall 225（+3.3%）（OI 3.7k） ｜ Put Wall 205（-5.9%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 34.9%｜历史 Rank 63%（近端代理）｜IV/RV 1.27×（近似）｜净 delta 敞口 正 69,309 股

📆 11-06 Forward Structure
存量OI: C 109.4k / P 152.1k，今日变化ΔOI: C +5.3k / P +5.5k，平值价格ATM: C $5.55 / P $4.44 ｜ ATM IV 35.8%，净 delta 敞口 58k shares
Top ΔOI: C 217 +1,688 ｜ C 230 +1,639
仓位参考: Max Pain 225 ｜ Call Wall 230（+5.6%，弱）（OI 12.3k） ｜ Put Wall 200（-8.2%，弱）（OI 11.7k）
量化解读： 存量 Put 重｜ATM IV 35.8%｜历史 Rank 63%（近端代理）｜IV/RV 1.31×（近似）｜净 delta 敞口 正 58,222 股

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 41.3% vs 11-02 32.4%（差 +9.0pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/NVDA_morning.json