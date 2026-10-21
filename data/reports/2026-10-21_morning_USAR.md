# 期权晨报 2026-10-21（快照 10:20 ET）

📊 市场环境

SPY $769.11 ｜ QQQ $721.59
VIX 17.20 ↓0.6%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-23 10C ΔOI +1,063（距现价 +2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 10.06 → 今开 10.33（+2.7%） | 较昨收变动（含盘初走势） ｜ 今日高 10.35 ｜ 低 10.09

Options: P/C成交量 0.10 | OI比 0.24 | ATM IV 88.9% | Skew -1.7pp | Term 0.99 | ExpMove ±5.4%（近端） | Rank 20%
量化视角： IV 历史低位（Rank 20%，期权偏便宜）｜期限结构正常（Term 0.99）｜Put 保护异常便宜（Skew -1.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.24）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.10×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.24×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（2D）±5.4% ｜ 10-30（9D）±8.4% ｜ 11-06（16D）±15.3% ｜ 11-13（23D）±18.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,792,739 | GEX Change vs 上次快照 1,804,505 | Flip: Primary Flip: 9.86（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 238 / LOW 87 / INVALID 111
结构观察区: Primary Flip 9.86（全链重定价，覆盖 99%）
Put Wall 10（弱结构｜现价高于该位 2.1%）
最近结构参考: Put Wall 10（现价高于该位 2.1%）
量化视角： 正 Gamma（179万，无历史分位）｜由负转正（+180万）｜现价位于 Flip 上方 3.53%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 10（Put Wall，弱结构）；上方 10（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 10（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 10.5P — Vol 1,273 | 最新价 $1.28 | OI 55→1287 (ΔOI +1232张) | ΔOI/Volume 96.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1232张（+2240.0% vs前日OI），连续性待观察（方向未知）
10-23 10.5C — Vol 1,910 | 最新价 $0.16 | OI 1522→2585 (ΔOI +1063张) | ΔOI/Volume 55.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1063张（+69.8% vs前日OI），连续性待观察（方向未知）
10-23 12.0C — Vol 1,140 | 最新价 $0.02 | OI 1710→2679 (ΔOI +969张) | ΔOI/Volume 85.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增969张（+56.7% vs前日OI），连续性待观察（方向未知）
10-30 10.0C — Vol 1,356 | 最新价 $0.57 | OI 129→775 (ΔOI +646张) | ΔOI/Volume 47.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增646张（+500.8% vs前日OI），连续性待观察（方向未知）
11-20 9.0P — Vol 642 | 最新价 $0.51 | OI 372→725 (ΔOI +353张) | ΔOI/Volume 55.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增353张（+94.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,263 张（Put 1,585 / Call 2,678），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +2.6k / P -0.7k ｜ Activity MEDIUM △ ｜ 2D
10-30  C +1.1k / P -39 ｜ Activity MEDIUM △ ｜ 9D
11-06  C +0.2k / P -0.1k ｜ Activity LOW ｜ 16D
11-13  C +0.1k / P -33 ｜ Activity LOW ｜ 23D

📆 10-23 Forward Structure
存量OI: C 23.7k / P 5.6k，今日变化ΔOI: C +2.6k / P -0.7k，平值价格ATM: C $0.39 / P $0.16 ｜ ATM IV 88.9%，净 delta 敞口 139k shares
Top ΔOI: C 10 +1,063 ｜ P 12 -361
仓位参考: Max Pain 10 ｜ Call Wall 10.5（+2.8%，弱）（OI 2.6k） ｜ Put Wall 9.5（-7.0%）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 88.9%｜历史 Rank 20%（近端代理）｜IV/RV 1.65×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 138,929 股

10-30（MEDIUM △）Top ΔOI: 10C +646 ｜ 11C +160
10-30（MEDIUM △）仓位参考: Max Pain 12 ｜ Call Wall 11（+7.7%，弱）（OI 2.7k） ｜ Put Wall 10（-2.1%，弱）（OI 0.6k）

11-06（Activity LOW）仓位参考: Max Pain 13 ｜ Call Wall 11（+7.7%，弱）（OI 0.4k） ｜ Put Wall 10（-2.1%，弱）（OI 0.8k）

11-13（Activity LOW）仓位参考: Max Pain 15 ｜ Call Wall 10.5（+2.8%，弱）（OI 0.2k） ｜ Put Wall 11（+7.7%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/USAR_morning.json