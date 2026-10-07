# 期权晨报 2026-10-07（快照 10:20 ET）

📊 市场环境

SPY $777.04 ｜ QQQ $757.73
VIX 15.79 ↑5.2%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　✅ 今日已公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 200C ΔOI +2,841（距现价 +4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 192.07 → 今开 192.70（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 194.70 ｜ 低 190.11

Options: P/C成交量 0.33 | OI比 0.65 | ATM IV 46.2% | Skew 0.2pp | Term 1.21 | ExpMove ±3.0%（近端） | Rank 29%
量化视角： IV 中性（Rank 29%）｜期限结构正常偏陡（Term 1.21）｜保护溢价薄（Skew 0.2pp）｜存量 Call 偏重（OI比 0.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.33×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.65×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±3.0% ｜ 10-16（9D）±5.2% ｜ 10-23（16D）±7.1% ｜ 10-30（23D）±8.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 69,416,080 | GEX Change vs 上次快照 -2,136,786 | Flip: Primary Flip: 182.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 542 / LOW 74 / INVALID 196
结构观察区: Primary Flip 182.89（全链重定价，覆盖 100%）
Call Wall 200（弱结构｜现价低于该位 4.2%）
最近结构参考: Call Wall 200（现价低于该位 4.2%）
量化视角： 正 Gamma（6942万，无历史分位）｜正 Gamma 减弱（214万）｜现价位于 Flip 上方 4.76%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 188（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 183（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 200.0C — Vol 22,365 | 最新价 $0.70 | OI 11060→13901 (ΔOI +2841张) | ΔOI/Volume 12.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2841张（+25.7% vs前日OI），连续性待观察（方向未知）
10-09 182.5P — Vol 5,555 | 最新价 $0.49 | OI 2653→4491 (ΔOI +1838张) | ΔOI/Volume 33.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1838张（+69.3% vs前日OI），连续性待观察（方向未知）
10-16 205.0C — Vol 3,221 | 最新价 $1.32 | OI 4267→5603 (ΔOI +1336张) | ΔOI/Volume 41.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1336张（+31.3% vs前日OI），连续性待观察（方向未知）
10-09 195.0C — Vol 40,546 | 最新价 $1.93 | OI 17941→19107 (ΔOI +1166张) | ΔOI/Volume 2.9% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增1166张（+6.5% vs前日OI），值得跟踪（方向未知）
10-09 185.0P — Vol 6,904 | 最新价 $0.83 | OI 7002→8082 (ΔOI +1080张) | ΔOI/Volume 15.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1080张（+15.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,261 张（Put 2,918 / Call 5,343），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +5.2k / P +6.4k ｜ Activity HIGH ｜ 2D
10-16  C +3.2k / P -0.1k ｜ Activity HIGH ｜ 9D
10-23  C +1.4k / P +1.2k ｜ Activity HIGH ｜ 16D
10-30  C +1.5k / P +0.7k ｜ Activity HIGH ｜ 23D

📆 10-09 Forward Structure
存量OI: C 122.3k / P 79.1k，今日变化ΔOI: C +5.2k / P +6.4k，平值价格ATM: C $2.23 / P $3.42 ｜ ATM IV 46.2%，净 delta 敞口 -127k shares
Top ΔOI: C 200 +2,841 ｜ P 182 +1,838 ｜ C 195 +1,166
仓位参考: Max Pain 188 ｜ Call Wall 205（+7.0%，弱）（OI 20.5k） ｜ Put Wall 185（-3.4%，弱）（OI 8.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 46.2%｜历史 Rank 29%（近端代理）｜IV/RV 2.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 127,136 股

📆 10-16 Forward Structure
存量OI: C 158.5k / P 191.9k，今日变化ΔOI: C +3.2k / P -0.1k，平值价格ATM: C $4.45 / P $5.60 ｜ ATM IV 40.8%，净 delta 敞口 -27k shares
Top ΔOI: C 205 +1,336 ｜ P 180 -972 ｜ P 175 -807
仓位参考: Max Pain 170 ｜ Call Wall 200（+4.4%）（OI 16.9k） ｜ Put Wall 175（-8.7%，弱）（OI 8.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 40.8%｜历史 Rank 29%（近端代理）｜IV/RV 2.05×（近似）｜净 delta 敞口 负 27,326 股

📆 10-23 Forward Structure
存量OI: C 25.1k / P 19.3k，今日变化ΔOI: C +1.4k / P +1.2k，平值价格ATM: C $6.35 / P $7.30 ｜ ATM IV 40.8%，净 delta 敞口 10k shares
Top ΔOI: C 192 -316 ｜ C 210 +315
仓位参考: Max Pain 180 ｜ Call Wall 180（-6.1%）（OI 4.7k） ｜ Put Wall 175（-8.7%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 40.8%｜历史 Rank 29%（近端代理）｜IV/RV 2.05×（近似）｜净 delta 敞口 正 10,033 股

📆 10-30 Forward Structure
存量OI: C 27.7k / P 18.5k，今日变化ΔOI: C +1.5k / P +0.7k，平值价格ATM: C $7.85 / P $8.32 ｜ ATM IV 41.9%，净 delta 敞口 16k shares
Top ΔOI: C 200 +870 ｜ C 190 -233 ｜ P 180 +177
仓位参考: Max Pain 185 ｜ Call Wall 200（+4.4%，弱）（OI 3.3k） ｜ Put Wall 180（-6.1%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 41.9%｜历史 Rank 29%（近端代理）｜IV/RV 2.10×（近似）｜净 delta 敞口 正 16,473 股

📅 事件差分（观察，非因果）: 10-09（2D）ATM IV 46.2% vs 10-16 40.8%（差 +5.3pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/PLTR_morning.json