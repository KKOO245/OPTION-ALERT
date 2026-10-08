# 期权晨报 2026-10-08（快照 10:20 ET）

📊 市场环境

SPY $775.90 ｜ QQQ $755.97
VIX 15.43 ↑2.3%（5D -5.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 150P ΔOI -4,932（距现价 -0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 153.37 → 今开 150.18（-2.1%） | 较昨收变动（含盘初走势） ｜ 今日高 151.77 ｜ 低 147.78

Options: P/C成交量 0.35 | OI比 0.77 | ATM IV 68.6% | Skew -4.5pp | Term 0.92 | ExpMove ±3.2%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -4.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.77）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.35×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±3.2% ｜ 10-16（8D）±7.0% ｜ 10-23（15D）±9.7% ｜ 10-30（22D）±12.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -8,198,212 | GEX Change vs 上次快照 -7,886,559 | Flip: Primary Flip: 151.55（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 558 / LOW 119 / INVALID 265
结构观察区: Primary Flip 151.55（全链重定价，覆盖 99%）
最近结构参考: Flip 152（现价低于该位 0.9%）
量化视角： 负 Gamma（820万，无历史分位）｜负 Gamma 加深（789万）｜现价位于 Flip 下方 0.89%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 152（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 142.0P — Vol 6,697 | 最新价 $1.76 | OI 532→6926 (ΔOI +6394张) | ΔOI/Volume 95.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6394张（+1201.9% vs前日OI），连续性待观察（方向未知）
10-16 170.0C — Vol 10,332 | 最新价 $1.49 | OI 5072→11172 (ΔOI +6100张) | ΔOI/Volume 59.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6100张（+120.3% vs前日OI），连续性待观察（方向未知）
10-16 160.0C — Vol 6,692 | 最新价 $3.50 | OI 8316→12241 (ΔOI +3925张) | ΔOI/Volume 58.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3925张（+47.2% vs前日OI），连续性待观察（方向未知）
10-09 115.0P — Vol 4,002 | 最新价 $0.03 | OI 5070→8963 (ΔOI +3893张) | ΔOI/Volume 97.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3893张（+76.8% vs前日OI），连续性待观察（方向未知）
10-30 210.0C — Vol 3,984 | 最新价 $0.72 | OI 1873→5191 (ΔOI +3318张) | ΔOI/Volume 83.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3318张（+177.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 23,630 张（Put 10,287 / Call 13,343），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +2.0k / P +10.2k ｜ Activity HIGH ｜ 1D
10-16  C +18.2k / P +4.1k ｜ Activity HIGH ｜ 8D
10-23  C +5.2k / P +7.3k ｜ Activity MEDIUM △ ｜ 15D
10-30  C +4.5k / P +3.4k ｜ Activity HIGH ｜ 22D

📆 10-09 Forward Structure
存量OI: C 216.8k / P 167.1k，今日变化ΔOI: C +2.0k / P +10.2k，平值价格ATM: C $2.67 / P $2.10 ｜ ATM IV 68.6%，净 delta 敞口 77k shares
仓位参考: Max Pain 155 ｜ Call Wall 165（+9.9%，弱）（OI 26.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 68.6%｜历史 Rank 26%（近端代理）｜IV/RV 0.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 76,736 股

📆 10-16 Forward Structure
存量OI: C 202.1k / P 188.1k，今日变化ΔOI: C +18.2k / P +4.1k，平值价格ATM: C $5.50 / P $4.95 ｜ ATM IV 59.1%，净 delta 敞口 390k shares
Top ΔOI: P 142 +6,394 ｜ C 170 +6,100 ｜ P 150 -4,932
仓位参考: Max Pain 130 ｜ Call Wall 160（+6.5%，弱）（OI 12.2k） ｜ Put Wall 142（-5.5%，弱）（OI 6.9k）
量化解读： 存量两侧均衡｜ATM IV 59.1%｜历史 Rank 26%（近端代理）｜IV/RV 0.79×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 389,684 股

10-23（MEDIUM △）Top ΔOI: 138P +2,461 ｜ 160P +2,407
10-23（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 165（+9.9%，弱）（OI 2.1k） ｜ Put Wall 160（+6.5%）（OI 6.2k）

📆 10-30 Forward Structure
存量OI: C 26.7k / P 35.1k，今日变化ΔOI: C +4.5k / P +3.4k，平值价格ATM: C $9.75 / P $9.00 ｜ ATM IV 62.2%，净 delta 敞口 -24k shares
Top ΔOI: C 210 +3,318 ｜ P 130 +1,063 ｜ P 140 +862
仓位参考: Max Pain 160 ｜ Call Wall 162.5（+8.2%，弱）（OI 2.6k） ｜ Put Wall 160（+6.5%，弱）（OI 3.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 62.2%｜历史 Rank 26%（近端代理）｜IV/RV 0.83×（近似）｜净 delta 敞口 负 24,358 股

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 68.6% vs 10-16 59.1%（差 +9.5pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/MSTR_morning.json