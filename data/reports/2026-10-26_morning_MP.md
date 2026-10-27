# 期权晨报 2026-10-26（快照 09:08 ET）

📊 市场环境

SPY $765.37 ｜ QQQ $712.20
VIX 19.22 ↓1.2%（5D +4.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-26

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 待公布 ｜ 前值 0
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 38P ΔOI +562（距现价 -0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 38.30 → 今开 38.14（-0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 38.87 ｜ 低 37.11

Options: P/C成交量 1.29 | OI比 0.80 | ATM IV 57.6% | Skew -2.3pp | Term 1.07 | ExpMove ±6.3%（近端） | Rank 32%
量化视角： IV 中性（Rank 32%）｜期限结构正常（Term 1.07）｜Put 保护异常便宜（Skew -2.3pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.80）+ 当日成交偏 Put（P/C量 1.29）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.29×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（4D）±6.3% ｜ 11-06（11D）±10.5% ｜ 11-13（18D）±12.0% ｜ 11-20（25D）±14.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,602,433 | GEX Change vs 上次快照 -619,813 | Flip: Primary Flip: 40.30（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 303 / LOW 51 / INVALID 132
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 40.30（全链重定价，覆盖 91%）
Put Wall 35（弱结构｜现价高于该位 9.4%）
最近结构参考: Flip 40（现价低于该位 5.0%）
量化视角： 负 Gamma（160万，无历史分位）｜负 Gamma 加深（62万）｜现价位于 Flip 下方 5.02%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall，弱结构）；上方 44（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 40（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 38.0P — Vol 964 | 最新价 $1.03 | OI 622→1184 (ΔOI +562张) | ΔOI/Volume 58.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增562张（+90.3% vs前日OI），连续性待观察（方向未知）
11-20 50.0C — Vol 359 | 最新价 $0.34 | OI 3320→3557 (ΔOI +237张) | ΔOI/Volume 66.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增237张（+7.1% vs前日OI），连续性待观察（方向未知）
10-30 38.5C — Vol 381 | 最新价 $1.16 | OI 57→207 (ΔOI +150张) | ΔOI/Volume 39.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增150张（+263.2% vs前日OI），连续性待观察（方向未知）
10-30 41.0C — Vol 166 | 最新价 $0.39 | OI 119→233 (ΔOI +114张) | ΔOI/Volume 68.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增114张（+95.8% vs前日OI），连续性待观察（方向未知）
10-30 40.0C — Vol 131 | 最新价 $0.61 | OI 80→182 (ΔOI +102张) | ΔOI/Volume 77.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增102张（+127.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,165 张（Put 562 / Call 603），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +0.8k / P +0.8k ｜ Activity HIGH ｜ 4D
11-06  C +0.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 11D
11-13  C +16 / P +8 ｜ Activity MEDIUM △ ｜ 18D
11-20  C +84 / P +30 ｜ Activity MEDIUM △ ｜ 25D

📆 10-30 Forward Structure
存量OI: C 9.6k / P 7.7k，今日变化ΔOI: C +0.8k / P +0.8k，平值价格ATM: C $1.16 / P $1.27 ｜ ATM IV 57.6%，净 delta 敞口 -10k shares
Top ΔOI: P 38 +562 ｜ C 38 +150 ｜ C 41 +114
仓位参考: Max Pain 44 ｜ Call Wall 42（+9.7%，弱）（OI 0.6k） ｜ Put Wall 38（-0.7%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 57.6%｜历史 Rank 32%（近端代理）｜IV/RV 1.30×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 10,155 股

11-06（MEDIUM △）Top ΔOI: 42P +63
11-06（MEDIUM △）仓位参考: Max Pain 43 ｜ Call Wall 40（+4.5%，弱）（OI 0.3k） ｜ Put Wall 38（-0.7%）（OI 0.9k）

11-13（MEDIUM △）仓位参考: Max Pain 42 ｜ Call Wall 35（-8.6%，弱）（OI 0.5k） ｜ Put Wall 39（+1.9%）（OI 0.7k）

11-20（MEDIUM △）Top ΔOI: 40C -213
11-20（MEDIUM △）仓位参考: Max Pain 45 ｜ Call Wall 40（+4.5%，弱）（OI 0.8k） ｜ Put Wall 40（+4.5%，弱）（OI 1.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/MP_morning.json