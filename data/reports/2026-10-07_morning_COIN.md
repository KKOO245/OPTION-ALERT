# 期权晨报 2026-10-07（快照 10:20 ET）

📊 市场环境

SPY $774.46 ｜ QQQ $754.66
VIX 15.79 ↑5.2%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　⏰ 今日
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 182P ΔOI +620（距现价 +2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 185.74 → 今开 180.23（-3.0%） | 较昨收变动（含盘初走势） ｜ 今日高 181.20 ｜ 低 177.74

Options: P/C成交量 0.52 | OI比 0.54 | ATM IV 63.5% | Skew -4.2pp | Term 1.03 | ExpMove ±4.0%（近端） | Rank 17%
量化视角： IV 历史低位（Rank 17%，期权偏便宜）｜期限结构正常（Term 1.03）｜Put 保护异常便宜（Skew -4.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±4.0% ｜ 10-16（9D）±7.1% ｜ 10-23（16D）±9.5% ｜ 10-30（23D）±13.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,633,378 | GEX Change vs 上次快照 -17,549,103 | Flip: Primary Flip: 176.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 473 / LOW 129 / INVALID 242
结构观察区: Primary Flip 176.38（全链重定价，覆盖 99%）
最近结构参考: Flip 176（现价高于该位 1.4%）
量化视角： 正 Gamma（563万，无历史分位）｜正 Gamma 减弱（1755万）｜现价位于 Flip 上方 1.43%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 188（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 176（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 195.0C — Vol 7,059 | 最新价 $1.47 | OI 12812→13730 (ΔOI +918张) | ΔOI/Volume 13.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增918张（+7.2% vs前日OI），连续性待观察（方向未知）
10-09 200.0C — Vol 5,193 | 最新价 $0.80 | OI 8474→9104 (ΔOI +630张) | ΔOI/Volume 12.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增630张（+7.4% vs前日OI），连续性待观察（方向未知）
10-09 182.5P — Vol 1,380 | 最新价 $2.80 | OI 1307→1927 (ΔOI +620张) | ΔOI/Volume 44.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增620张（+47.4% vs前日OI），连续性待观察（方向未知）
10-09 205.0C — Vol 2,206 | 最新价 $0.44 | OI 2532→3054 (ΔOI +522张) | ΔOI/Volume 23.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增522张（+20.6% vs前日OI），连续性待观察（方向未知）
10-09 180.0P — Vol 3,172 | 最新价 $1.97 | OI 1497→1975 (ΔOI +478张) | ΔOI/Volume 15.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增478张（+31.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,168 张（Put 1,098 / Call 2,070），跨 1 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +3.3k / P +1.0k ｜ Activity HIGH ｜ 2D
10-16  C +0.6k / P +0.8k ｜ Activity HIGH ｜ 9D
10-23  C +0.6k / P +0.5k ｜ Activity HIGH ｜ 16D
10-30  C +0.5k / P +0.2k ｜ Activity HIGH ｜ 23D

📆 10-09 Forward Structure
存量OI: C 68.5k / P 37.2k，今日变化ΔOI: C +3.3k / P +1.0k，平值价格ATM: C $3.10 / P $4.02 ｜ ATM IV 63.5%，净 delta 敞口 -24k shares
Top ΔOI: C 195 +918 ｜ P 182 +620
仓位参考: Max Pain 188 ｜ Call Wall 195（+9.0%）（OI 13.7k） ｜ Put Wall 170（-5.0%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 63.5%｜历史 Rank 17%（近端代理）｜IV/RV 0.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 23,832 股

📆 10-16 Forward Structure
存量OI: C 86.0k / P 80.2k，今日变化ΔOI: C +0.6k / P +0.8k，平值价格ATM: C $6.00 / P $6.65 ｜ ATM IV 55.2%，净 delta 敞口 11k shares
Top ΔOI: C 182 +222
仓位参考: Max Pain 180 ｜ Call Wall 190（+6.2%，弱）（OI 2.6k） ｜ Put Wall 165（-7.8%，弱）（OI 3.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 55.2%｜历史 Rank 17%（近端代理）｜IV/RV 0.83×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 10,658 股

📆 10-23 Forward Structure
存量OI: C 8.3k / P 7.3k，今日变化ΔOI: C +0.6k / P +0.5k，平值价格ATM: C $8.25 / P $8.78 ｜ ATM IV 55.8%，净 delta 敞口 -2k shares
Top ΔOI: P 182 +191 ｜ C 190 +117
仓位参考: Max Pain 190 ｜ Call Wall 190（+6.2%）（OI 0.9k） ｜ Put Wall 170（-5.0%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 55.8%｜历史 Rank 17%（近端代理）｜IV/RV 0.84×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 2,279 股

📆 10-30 Forward Structure
存量OI: C 8.8k / P 7.7k，今日变化ΔOI: C +0.5k / P +0.2k，平值价格ATM: C $11.51 / P $11.72 ｜ ATM IV 62.3%，净 delta 敞口 3k shares
Top ΔOI: C 200 +186 ｜ P 180 +106
仓位参考: Max Pain 185 ｜ Call Wall 185（+3.4%，弱）（OI 1.2k） ｜ Put Wall 170（-5.0%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜ATM IV 62.3%｜历史 Rank 17%（近端代理）｜IV/RV 0.93×（近似）｜净 delta 敞口 正 2,669 股

📅 事件差分（观察，非因果）: 10-09（2D）ATM IV 63.5% vs 10-16 55.2%（差 +8.4pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/COIN_morning.json