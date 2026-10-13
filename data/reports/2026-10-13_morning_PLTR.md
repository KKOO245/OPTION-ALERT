# 期权晨报 2026-10-13（快照 10:20 ET）

📊 市场环境

SPY $777.22 ｜ QQQ $743.40
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
🟡 **近现价集中开仓**: 10-16 220C ΔOI +4,183（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 209.00 → 今开 207.90（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 210.88 ｜ 低 206.21

Options: P/C成交量 0.52 | OI比 1.09 | ATM IV 47.8% | Skew 2.4pp | Term 1.20 | ExpMove ±3.6%（近端） | Rank 42%
量化视角： IV 中性（Rank 42%）｜期限结构正常偏陡（Term 1.20）｜保护溢价中性（Skew 2.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.09×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（3D）±3.6% ｜ 10-23（10D）±5.7% ｜ 10-30（17D）±7.4% ｜ 11-06（24D）±12.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 92,172,399 | GEX Change vs 上次快照 -3,362,805 | Flip: Primary Flip: 189.51（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 599 / LOW 48 / INVALID 151
结构观察区: Primary Flip 189.51（全链重定价，覆盖 98%）
Call Wall 220（弱结构｜现价低于该位 4.3%）
最近结构参考: Call Wall 220（现价低于该位 4.3%）
量化视角： 正 Gamma（9217万，无历史分位）｜正 Gamma 减弱（336万）｜现价位于 Flip 上方 11.11%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（MaxPain，仅结算参考）；上方 220（Call Wall，弱结构）。
• Gamma 区域：切换参考 190（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 222.5C — Vol 10,783 | 最新价 $0.47 | OI 0→8252 (ΔOI +8252张) | ΔOI/Volume 76.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8252张（前日OI缺失），连续性待观察（方向未知）
10-16 220.0C — Vol 29,860 | 最新价 $0.75 | OI 14174→18357 (ΔOI +4183张) | ΔOI/Volume 14.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4183张（+29.5% vs前日OI），连续性待观察（方向未知）
10-16 207.5P — Vol 12,503 | 最新价 $3.10 | OI 1463→4175 (ΔOI +2712张) | ΔOI/Volume 21.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2712张（+185.4% vs前日OI），连续性待观察（方向未知）
10-16 225.0C — Vol 5,408 | 最新价 $0.33 | OI 7742→9457 (ΔOI +1715张) | ΔOI/Volume 31.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1715张（+22.1% vs前日OI），连续性待观察（方向未知）
10-23 220.0C — Vol 5,602 | 最新价 $2.26 | OI 2643→4251 (ΔOI +1608张) | ΔOI/Volume 28.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1608张（+60.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 18,470 张（Put 2,712 / Call 15,758），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +11.1k / P +12.1k ｜ Activity HIGH ｜ 3D
10-23  C +4.8k / P +4.0k ｜ Activity HIGH ｜ 10D
10-30  C +0.4k / P +2.5k ｜ Activity MEDIUM △ ｜ 17D
11-06  C +1.7k / P +1.7k ｜ Activity MEDIUM △ ｜ 24D

📆 10-16 Forward Structure
存量OI: C 237.9k / P 259.1k，今日变化ΔOI: C +11.1k / P +12.1k，平值价格ATM: C $4.04 / P $3.55 ｜ ATM IV 47.8%，净 delta 敞口 -510k shares
Top ΔOI: C 222 +8,252 ｜ C 220 +4,183 ｜ C 215 -3,857
仓位参考: Max Pain 180 ｜ Call Wall 220（+4.5%，弱）（OI 18.4k） ｜ Put Wall 190（-9.8%，弱）（OI 9.0k）
量化解读： 存量两侧均衡｜ATM IV 47.8%｜历史 Rank 42%（近端代理）｜IV/RV 1.83×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 509,787 股

📆 10-23 Forward Structure
存量OI: C 39.3k / P 53.7k，今日变化ΔOI: C +4.8k / P +4.0k，平值价格ATM: C $6.27 / P $5.76 ｜ ATM IV 43.0%，净 delta 敞口 82k shares
Top ΔOI: C 220 +1,608 ｜ C 207 +757 ｜ P 200 +581
仓位参考: Max Pain 190 ｜ Call Wall 220（+4.5%，弱）（OI 4.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 43.0%｜历史 Rank 42%（近端代理）｜IV/RV 1.65×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 82,479 股

10-30（MEDIUM △）Top ΔOI: 210P +306 ｜ 205P +264
10-30（MEDIUM △）仓位参考: Max Pain 192 ｜ Call Wall 205（-2.6%，弱）（OI 2.9k） ｜ Put Wall 190（-9.8%，弱）（OI 3.2k）

11-06（MEDIUM △）Top ΔOI: 230C +335 ｜ 195P +334
11-06（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 220（+4.5%，弱）（OI 1.4k） ｜ Put Wall 190（-9.8%）（OI 2.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/PLTR_morning.json