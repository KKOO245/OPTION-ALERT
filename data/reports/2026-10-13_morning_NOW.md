# 期权晨报 2026-10-13（快照 10:20 ET）

📊 市场环境

SPY $777.22 ｜ QQQ $743.45
VIX 15.31 ↑0.7%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 46.0（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.95 ｜ 实际 3.99 ｜ 前值 3.93　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 150C ΔOI -949（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NOW  昨收 140.32 → 今开 140.19（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 145.17 ｜ 低 140.19

Options: P/C成交量 0.24 | OI比 0.77 | ATM IV 55.6% | Skew 0.8pp | Term 1.07 | ExpMove ±4.2%（近端） | Rank 46%
量化视角： IV 中性（Rank 46%）｜期限结构正常（Term 1.07）｜保护溢价薄（Skew 0.8pp）｜存量 Call 偏重（OI比 0.77）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.24×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（3D）±4.2% ｜ 10-23（10D）±6.8% ｜ 10-30（17D）±12.8% ｜ 11-06（24D）±12.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 28,381,541 | GEX Change vs 上次快照 7,415,708 | Flip: Primary Flip: 134.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 486 / LOW 28 / INVALID 122
结构观察区: Primary Flip 134.63（全链重定价，覆盖 96%）
Call Wall 150（现价低于该位 3.9%）
最近结构参考: Call Wall 150（现价低于该位 3.9%）
量化视角： 正 Gamma（2838万，无历史分位）｜正 Gamma 增强（+742万）｜现价位于 Flip 上方 7.05%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 130（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 135（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 170.0C — Vol 914 | 最新价 $0.12 | OI 388→1208 (ΔOI +820张) | ΔOI/Volume 89.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增820张（+211.3% vs前日OI），连续性待观察（方向未知）
10-16 140.0P — Vol 1,533 | 最新价 $2.72 | OI 2178→2943 (ΔOI +765张) | ΔOI/Volume 49.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增765张（+35.1% vs前日OI），连续性待观察（方向未知）
10-23 145.0C — Vol 1,564 | 最新价 $2.78 | OI 806→1348 (ΔOI +542张) | ΔOI/Volume 34.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增542张（+67.2% vs前日OI），连续性待观察（方向未知）
11-06 140.0P — Vol 514 | 最新价 $8.40 | OI 53→539 (ΔOI +486张) | ΔOI/Volume 94.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增486张（+917.0% vs前日OI），连续性待观察（方向未知）
10-23 150.0C — Vol 1,424 | 最新价 $1.60 | OI 1073→1531 (ΔOI +458张) | ΔOI/Volume 32.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增458张（+42.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,071 张（Put 1,251 / Call 1,820），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +0.6k / P +1.8k ｜ Activity HIGH ｜ 3D
10-23  C +2.8k / P +0.4k ｜ Activity HIGH ｜ 10D
10-30  C +0.6k / P +0.6k ｜ Activity HIGH ｜ 17D
11-06  C +0.2k / P +0.5k ｜ Activity MEDIUM △ ｜ 24D

📆 10-16 Forward Structure
存量OI: C 88.4k / P 68.1k，今日变化ΔOI: C +0.6k / P +1.8k，平值价格ATM: C $3.00 / P $3.00 ｜ ATM IV 55.6%，净 delta 敞口 -59k shares
Top ΔOI: C 150 -949 ｜ P 140 +765 ｜ P 130 +425
仓位参考: Max Pain 130 ｜ Call Wall 150（+4.1%）（OI 15.3k） ｜ Put Wall 130（-9.8%，弱）（OI 5.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 55.6%｜历史 Rank 46%（近端代理）｜IV/RV 2.02×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 59,042 股

📆 10-23 Forward Structure
存量OI: C 18.7k / P 19.1k，今日变化ΔOI: C +2.8k / P +0.4k，平值价格ATM: C $4.95 / P $4.85 ｜ ATM IV 50.4%，净 delta 敞口 55k shares
Top ΔOI: C 145 +542 ｜ C 150 +458
仓位参考: Max Pain 136 ｜ Call Wall 150（+4.1%，弱）（OI 1.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 50.4%｜历史 Rank 46%（近端代理）｜IV/RV 1.83×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 54,692 股

📆 10-30 Forward Structure
存量OI: C 9.0k / P 11.4k，今日变化ΔOI: C +0.6k / P +0.6k，平值价格ATM: C $8.45 / P $10.00 ｜ ATM IV 67.8%，净 delta 敞口 8k shares
Top ΔOI: P 135 +286 ｜ P 144 +78 ｜ C 130 +72
仓位参考: Max Pain 135 ｜ Call Wall 150（+4.1%，弱）（OI 1.0k） ｜ Put Wall 130（-9.8%，弱）（OI 0.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 67.8%｜历史 Rank 46%（近端代理）｜IV/RV 2.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 8,369 股

11-06（MEDIUM △）Top ΔOI: 140P +486
11-06（MEDIUM △）仓位参考: Max Pain 140 ｜ Call Wall 155（+7.5%）（OI 0.9k） ｜ Put Wall 140（-2.9%）（OI 0.5k）

📅 事件差分（观察，非因果）: 10-16（3D）ATM IV 55.6% vs 10-23 50.4%（差 +5.1pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/NOW_morning.json