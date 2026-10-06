# 期权晨报 2026-10-06（快照 10:20 ET）

📊 市场环境

SPY $779.74 ｜ QQQ $760.96
VIX 15.48 ↓0.3%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 49.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 145C ΔOI +368（距现价 +4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NOW  昨收 136.08 → 今开 138.46（+1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 140.60 ｜ 低 137.33

Options: P/C成交量 0.34 | OI比 0.75 | ATM IV 56.0% | Skew 0.8pp | Term 1.05 | ExpMove ±4.4%（近端） | Rank 35%
量化视角： IV 中性（Rank 35%）｜期限结构正常（Term 1.05）｜保护溢价薄（Skew 0.8pp）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（3D）±4.4% ｜ 10-16（10D）±6.7% ｜ 10-23（17D）±9.8% ｜ 10-30（24D）±14.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,840,228 | GEX Change vs 上次快照 7,825,442 | Flip: Primary Flip: 132.95（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 505 / LOW 33 / INVALID 152
结构观察区: Primary Flip 132.95（全链重定价，覆盖 100%）
Call Wall 150（现价低于该位 7.3%）
最近结构参考: Flip 133（现价高于该位 4.6%）
量化视角： 正 Gamma（1484万，无历史分位）｜正 Gamma 增强（+783万）｜现价位于 Flip 上方 4.60%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 133（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 155.0C — Vol 793 | 最新价 $3.40 | OI 138→877 (ΔOI +739张) | ΔOI/Volume 93.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增739张（+535.5% vs前日OI），连续性待观察（方向未知）
10-16 145.0C — Vol 1,257 | 最新价 $1.67 | OI 4351→4958 (ΔOI +607张) | ΔOI/Volume 48.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增607张（+13.9% vs前日OI），连续性待观察（方向未知）
10-16 150.0C — Vol 1,016 | 最新价 $0.85 | OI 13513→14033 (ΔOI +520张) | ΔOI/Volume 51.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增520张（+3.9% vs前日OI），连续性待观察（方向未知）
10-09 144.0C — Vol 809 | 最新价 $0.68 | OI 477→907 (ΔOI +430张) | ΔOI/Volume 53.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增430张（+90.2% vs前日OI），连续性待观察（方向未知）
10-30 132.0P — Vol 391 | 最新价 $6.60 | OI 26→414 (ΔOI +388张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增388张（+1492.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,684 张（Put 388 / Call 2,296），跨 4 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +3.7k / P +1.9k ｜ Activity MEDIUM △ ｜ 3D
10-16  C +1.8k / P +55 ｜ Activity HIGH ｜ 10D
10-23  C +0.4k / P +0.4k ｜ Activity MEDIUM △ ｜ 17D
10-30  C +0.7k / P +0.8k ｜ Activity MEDIUM △ ｜ 24D

📆 10-09 Forward Structure
存量OI: C 23.6k / P 17.7k，今日变化ΔOI: C +3.7k / P +1.9k，平值价格ATM: C $3.40 / P $2.73 ｜ ATM IV 56.0%，净 delta 敞口 93k shares
Top ΔOI: C 144 +430 ｜ C 150 +377 ｜ C 145 +368
仓位参考: Max Pain 135 ｜ Call Wall 150（+7.9%）（OI 5.2k） ｜ Put Wall 130（-6.5%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 56.0%｜历史 Rank 35%（近端代理）｜IV/RV 1.45×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 92,686 股

📆 10-16 Forward Structure
存量OI: C 79.6k / P 63.3k，今日变化ΔOI: C +1.8k / P +55，平值价格ATM: C $4.79 / P $4.50 ｜ ATM IV 50.4%，净 delta 敞口 55k shares
Top ΔOI: C 145 +607 ｜ C 150 +520 ｜ C 140 +222
仓位参考: Max Pain 130 ｜ Call Wall 150（+7.9%）（OI 14.0k） ｜ Put Wall 130（-6.5%，弱）（OI 4.7k）
量化解读： 存量 Call 重｜ATM IV 50.4%｜历史 Rank 35%（近端代理）｜IV/RV 1.31×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 55,152 股

10-23（MEDIUM △）Top ΔOI: 131P +86
10-23（MEDIUM △）仓位参考: Max Pain 134 ｜ Call Wall 140（+0.7%，弱）（OI 1.0k）

10-30（MEDIUM △）Top ΔOI: 132P +388 ｜ 155C +148
10-30（MEDIUM △）仓位参考: Max Pain 134 ｜ Call Wall 140（+0.7%，弱）（OI 0.6k） ｜ Put Wall 130（-6.5%，弱）（OI 0.5k）

📅 事件差分（观察，非因果）: 10-09（3D）ATM IV 56.0% vs 10-16 50.4%（差 +5.6pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/NOW_morning.json