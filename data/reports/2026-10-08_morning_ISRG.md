# 期权晨报 2026-10-08（快照 10:20 ET）

📊 市场环境

SPY $774.21 ｜ QQQ $747.58
VIX 15.43 ↑2.3%（5D -5.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 425C ΔOI +177（距现价 +3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 414.52 → 今开 411.60（-0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 413.78 ｜ 低 407.70

Options: P/C成交量 0.36 | OI比 0.50 | ATM IV 39.8% | Skew 2.5pp | Term 1.16 | ExpMove ±2.1%（近端） | Rank 53%
量化视角： IV 中性（Rank 53%）｜期限结构正常偏陡（Term 1.16）｜保护溢价中性（Skew 2.5pp）｜存量 Call 偏重（OI比 0.50）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.50×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±2.1% ｜ 10-16（8D）±3.9% ｜ 10-23（15D）±9.2% ｜ 10-30（22D）±8.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,582,199 | GEX Change vs 上次快照 -1,480,048 | Flip: Primary Flip: 397.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 317 / LOW 139 / INVALID 408
结构观察区: Primary Flip 397.15（全链重定价，覆盖 94%）
Call Wall 420（弱结构｜现价低于该位 2.4%）
最近结构参考: Call Wall 420（现价低于该位 2.4%）
量化视角： 正 Gamma（358万，无历史分位）｜正 Gamma 减弱（148万）｜现价位于 Flip 上方 3.18%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 392（MaxPain，仅结算参考）；上方 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 397（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 425.0C — Vol 189 | 最新价 $1.20 | OI 163→340 (ΔOI +177张) | ΔOI/Volume 93.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增177张（+108.6% vs前日OI），连续性待观察（方向未知）
10-09 430.0C — Vol 171 | 最新价 $0.55 | OI 163→303 (ΔOI +140张) | ΔOI/Volume 81.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增140张（+85.9% vs前日OI），连续性待观察（方向未知）
10-09 397.5P — Vol 130 | 最新价 $0.96 | OI 15→145 (ΔOI +130张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增130张（+866.7% vs前日OI），连续性待观察（方向未知）
10-09 392.5P — Vol 138 | 最新价 $0.20 | OI 41→160 (ΔOI +119张) | ΔOI/Volume 86.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增119张（+290.2% vs前日OI），连续性待观察（方向未知）
10-16 430.0C — Vol 54 | 最新价 $3.13 | OI 322→361 (ΔOI +39张) | ΔOI/Volume 72.2% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增39张（+12.1% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 605 张（Put 249 / Call 356），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +0.3k / P +0.3k ｜ Activity HIGH ｜ 1D
10-16  C +0.1k / P +22 ｜ Activity MEDIUM △ ｜ 8D
10-23  C -5 / P +42 ｜ Activity LOW ｜ 15D
10-30  C +23 / P +6 ｜ Activity MEDIUM △ ｜ 22D

📆 10-09 Forward Structure
存量OI: C 3.3k / P 1.6k，今日变化ΔOI: C +0.3k / P +0.3k，平值价格ATM: C $5.18 / P $3.50 ｜ ATM IV 39.8%，净 delta 敞口 -4k shares
Top ΔOI: C 425 +177 ｜ C 430 +140 ｜ P 397 +130
仓位参考: Max Pain 392 ｜ Call Wall 420（+2.5%，弱）（OI 0.7k） ｜ Put Wall 370（-9.7%）（OI 0.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 39.8%｜历史 Rank 53%（近端代理）｜IV/RV 1.62×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 4,462 股

10-16（MEDIUM △）Top ΔOI: 430C +39 ｜ 442C +27
10-16（MEDIUM △）仓位参考: Max Pain 390 ｜ Call Wall 400（-2.4%，弱）（OI 0.9k） ｜ Put Wall 380（-7.3%，弱）（OI 0.6k）

10-23（Activity LOW）仓位参考: Max Pain 415 ｜ Call Wall 425（+3.7%）（OI 0.5k） ｜ Put Wall 415（+1.3%）（OI 0.5k）

10-30（MEDIUM △）Top ΔOI: 380P +8 ｜ 395P -8
10-30（MEDIUM △）仓位参考: Max Pain 390 ｜ Call Wall 450（+9.8%，弱）（OI 75） ｜ Put Wall 375（-8.5%，弱）（OI 52）

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 39.8% vs 10-16 32.4%（差 +7.4pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/ISRG_morning.json