# 期权晨报 2026-10-14（快照 10:20 ET）

📊 市场环境

SPY $771.45 ｜ QQQ $732.49
VIX 15.81 ↑3.5%（5D +4.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 36.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-14

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 2.6 ｜ 前值 2.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 3.7 ｜ 前值 3.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 0.6 ｜ 前值 0.4　✅ 今日已公布
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 172P ΔOI +553（距现价 -1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 181.79 → 今开 178.66（-1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 182.39 ｜ 低 174.12

Options: P/C成交量 0.55 | OI比 0.81 | ATM IV 68.3% | Skew -4.5pp | Term 0.99 | ExpMove ±4.2%（近端） | Rank 29%
量化视角： IV 中性（Rank 29%）｜期限结构正常（Term 0.99）｜Put 保护异常便宜（Skew -4.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（2D）±4.2% ｜ 10-23（9D）±7.6% ｜ 10-30（16D）±11.6% ｜ 11-06（23D）±13.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 12,976,009 | GEX Change vs 上次快照 -15,302,458 | Flip: Primary Flip: 171.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 452 / LOW 115 / INVALID 255
结构观察区: Primary Flip 171.80（全链重定价，覆盖 98%）
最近结构参考: Flip 172（现价高于该位 2.3%）
量化视角： 正 Gamma（1298万，无历史分位）｜正 Gamma 减弱（1530万）｜现价位于 Flip 上方 2.33%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 180（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 172（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 192.5C — Vol 1,793 | 最新价 $1.32 | OI 6696→7936 (ΔOI +1240张) | ΔOI/Volume 69.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1240张（+18.5% vs前日OI），连续性待观察（方向未知）
10-16 172.5P — Vol 750 | 最新价 $1.09 | OI 602→1155 (ΔOI +553张) | ΔOI/Volume 73.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增553张（+91.9% vs前日OI），连续性待观察（方向未知）
10-23 100.0P — Vol 514 | 最新价 $0.08 | OI 5906→6286 (ΔOI +380张) | ΔOI/Volume 73.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增380张（+6.4% vs前日OI），连续性待观察（方向未知）
10-23 270.0C — Vol 387 | 最新价 $0.05 | OI 96→468 (ΔOI +372张) | ΔOI/Volume 96.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增372张（+387.5% vs前日OI），连续性待观察（方向未知）
10-16 180.0P — Vol 1,497 | 最新价 $3.45 | OI 3353→3682 (ΔOI +329张) | ΔOI/Volume 22.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增329张（+9.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,874 张（Put 1,262 / Call 1,612），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +0.9k / P +1.3k ｜ Activity HIGH ｜ 2D
10-23  C +1.5k / P +1.0k ｜ Activity MEDIUM △ ｜ 9D
10-30  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 16D
11-06  C +0.5k / P +0.3k ｜ Activity MEDIUM △ ｜ 23D

📆 10-16 Forward Structure
存量OI: C 139.4k / P 113.0k，今日变化ΔOI: C +0.9k / P +1.3k，平值价格ATM: C $4.35 / P $3.11 ｜ ATM IV 68.3%，净 delta 敞口 -63k shares
Top ΔOI: C 192 +1,240 ｜ C 185 -702 ｜ P 172 +553
仓位参考: Max Pain 180 ｜ Call Wall 185（+5.2%，弱）（OI 10.6k） ｜ Put Wall 165（-6.1%，弱）（OI 9.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 68.3%｜历史 Rank 29%（近端代理）｜IV/RV 2.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 62,920 股

10-23（MEDIUM △）仓位参考: Max Pain 185 ｜ Call Wall 190（+8.1%，弱）（OI 1.6k）

10-30（MEDIUM △）仓位参考: Max Pain 185 ｜ Call Wall 185（+5.2%，弱）（OI 1.3k） ｜ Put Wall 180（+2.4%，弱）（OI 0.8k）

11-06（MEDIUM △）Top ΔOI: 225C +271 ｜ 180P +63
11-06（MEDIUM △）仓位参考: Max Pain 178 ｜ Call Wall 177.5（+1.0%，弱）（OI 0.2k） ｜ Put Wall 170（-3.3%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 68.3% vs 10-23 58.9%（差 +9.4pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/COIN_morning.json