# 期权晨报 2026-10-21（快照 10:20 ET）

📊 市场环境

SPY $772.65 ｜ QQQ $726.16
VIX 17.20 ↓0.6%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 54C ΔOI +1,465（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 52.12 → 今开 52.05（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 52.10 ｜ 低 51.74

Options: P/C成交量 0.79 | OI比 0.52 | ATM IV 36.3% | Skew -1.2pp | Term 0.91 | ExpMove ±2.1%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构正常（Term 0.91）｜Put 保护异常便宜（Skew -1.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.52）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.79×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.52×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（2D）±2.1% ｜ 10-26（5D）±2.6% ｜ 10-28（7D）±3.6% ｜ 10-30（9D）±4.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 51,574,419 | GEX Change vs 上次快照 2,988,428 | Flip: Primary Flip: 50.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 703 / LOW 147 / INVALID 460
结构观察区: Primary Flip 50.61（全链重定价，覆盖 96%）
Put Wall 50（弱结构｜现价高于该位 3.8%）
最近结构参考: Flip 51（现价高于该位 2.5%）
量化视角： 正 Gamma（5157万，无历史分位）｜正 Gamma 增强（+299万）｜现价位于 Flip 上方 2.54%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构） / 52（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 51（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 49.5P — Vol 10,127 | 最新价 $0.89 | OI 101→10111 (ΔOI +10010张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10010张（+9910.9% vs前日OI），连续性待观察（方向未知）
11-20 53.5C — Vol 10,018 | 最新价 $1.53 | OI 30→10003 (ΔOI +9973张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9973张（+33243.3% vs前日OI），连续性待观察（方向未知）
11-20 59.0C — Vol 14,731 | 最新价 $0.36 | OI 64970→74068 (ΔOI +9098张) | ΔOI/Volume 61.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9098张（+14.0% vs前日OI），连续性待观察（方向未知）
11-20 57.0C — Vol 4,729 | 最新价 $0.59 | OI 6560→10934 (ΔOI +4374张) | ΔOI/Volume 92.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4374张（+66.7% vs前日OI），连续性待观察（方向未知）
10-21 53.0C — Vol 7,864 | 最新价 $0.10 | OI 2672→5451 (ΔOI +2779张) | ΔOI/Volume 35.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2779张（+104.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 36,234 张（Put 10,010 / Call 26,224），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 34.7k / P 18.2k，今日成交量: C 6.0k / P 4.8k，平值价格ATM: C $0.16 / P $0.26 ｜ ATM IV 36.3%，预期波动 ±0.8%，Max Pain 52
Top ΔOI: C 53 +2,779 ｜ P 51 +1,124 ｜ C 53 +754

📆 Forward Expiration Structure

10-23  C +4.0k / P +0.7k ｜ Activity HIGH ｜ 2D
10-26  C +1.1k / P +0.6k ｜ Activity HIGH ｜ 5D
10-28  C +1.2k / P +0.9k ｜ Activity HIGH ｜ 7D
10-30  C +1.4k / P +0.1k ｜ Activity MEDIUM △ ｜ 9D

📆 10-23 Forward Structure
存量OI: C 71.8k / P 47.2k，今日变化ΔOI: C +4.0k / P +0.7k，平值价格ATM: C $0.50 / P $0.58 ｜ ATM IV 33.9%，净 delta 敞口 187k shares
Top ΔOI: C 54 +1,465 ｜ P 51 -653
仓位参考: Max Pain 53 ｜ Call Wall 57（+9.8%，弱）（OI 7.0k） ｜ Put Wall 50（-3.7%，弱）（OI 4.4k）
量化解读： 存量 Call 重｜ATM IV 33.9%｜历史 Rank 58%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 187,312 股

📆 10-26 Forward Structure
存量OI: C 5.3k / P 4.0k，今日变化ΔOI: C +1.1k / P +0.6k，平值价格ATM: C $0.65 / P $0.69 ｜ ATM IV 27.1%，净 delta 敞口 10k shares
Top ΔOI: C 53 +299 ｜ C 55 +171 ｜ C 54 +136
仓位参考: Max Pain 50 ｜ Call Wall 50.5（-2.7%）（OI 1.5k） ｜ Put Wall 48（-7.5%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 27.1%｜历史 Rank 58%（近端代理）｜IV/RV 0.85×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 10,170 股

📆 10-28 Forward Structure
存量OI: C 3.3k / P 3.0k，今日变化ΔOI: C +1.2k / P +0.9k，平值价格ATM: C $0.88 / P $0.97 ｜ ATM IV 31.5%，净 delta 敞口 -10k shares
Top ΔOI: C 53 +296 ｜ C 54 +254 ｜ C 55 +171
仓位参考: Max Pain 52 ｜ Call Wall 55（+6.0%，弱）（OI 0.5k） ｜ Put Wall 48（-7.5%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜ATM IV 31.5%｜历史 Rank 58%（近端代理）｜IV/RV 0.99×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 9,890 股

10-30（MEDIUM △）Top ΔOI: 53C +668
10-30（MEDIUM △）仓位参考: Max Pain 54 ｜ Call Wall 56（+7.9%，弱）（OI 2.9k） ｜ Put Wall 50（-3.7%，弱）（OI 4.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/SLV_morning.json