# 期权晨报 2026-11-11（快照 10:20 ET）

📊 市场环境

SPY $756.41 ｜ QQQ $687.15
VIX 18.31 ↓5.9%（5D +10.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 36.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 11C ΔOI +37（距现价 -3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 11.58 → 今开 12.20（+5.4%） | 较昨收变动（含盘初走势） ｜ 今日高 12.23 ｜ 低 11.80

Options: P/C成交量 0.02 | OI比 0.40 | ATM IV 94.1% | Skew 7.4pp | Term 0.88 | ExpMove ±8.4%（近端） | Rank 35%
量化视角： IV 中性（Rank 35%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价显著（Skew 7.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.40）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.02×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.40×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±8.4% ｜ 11-20（9D）±15.7% ｜ 11-27（16D）±12.9% ｜ 12-04（23D）±12.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,973,793 | GEX Change vs 上次快照 414,492 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 187 / LOW 73 / INVALID 126
结构观察区: NO_CROSS
Put Wall 11（现价高于该位 8.6%） | Call Wall 12（现价低于该位 4.4%）
最近结构参考: Call Wall 12（现价低于该位 4.4%）
量化视角： 正 Gamma（197万，无历史分位）｜正 Gamma 增强（+41万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 11（Put Wall）；上方 12（MaxPain，仅结算参考） / 12（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 12.5C — Vol 213 | 最新价 $0.10 | OI 349→466 (ΔOI +117张) | ΔOI/Volume 54.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增117张（+33.5% vs前日OI），连续性待观察（方向未知）
11-13 11.5C — Vol 44 | 最新价 $0.46 | OI 137→174 (ΔOI +37张) | ΔOI/Volume 84.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增37张（+27.0% vs前日OI），连续性待观察（方向未知）
12-11 10.0C — Vol 33 | 最新价 $1.95 | OI 0→33 (ΔOI +33张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增33张（前日OI缺失），值得跟踪（方向未知）
11-20 12.5C — Vol 33 | 最新价 $0.29 | OI 69→100 (ΔOI +31张) | ΔOI/Volume 93.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31张（+44.9% vs前日OI），连续性待观察（方向未知）
11-13 14.0P — Vol 36 | 最新价 $2.42 | OI 25→53 (ΔOI +28张) | ΔOI/Volume 77.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增28张（+112.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 246 张（Put 28 / Call 218），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +0.2k / P +70 ｜ Activity MEDIUM △ ｜ 2D
11-20  C +37 / P -6 ｜ Activity MEDIUM △ ｜ 9D
11-27  C -1 / P +16 ｜ Activity LOW ｜ 16D
12-04  C +7 / P +1 ｜ Activity LOW ｜ 23D

📆 11-13 Forward Structure
存量OI: C 3.0k / P 1.2k，今日变化ΔOI: C +0.2k / P +70，平值价格ATM: C $0.45 / P $0.55 ｜ ATM IV 94.1%，净 delta 敞口 4k shares
Top ΔOI: C 12 +117 ｜ C 11 +37
仓位参考: Max Pain 12 ｜ Call Wall 13（+8.8%，弱）（OI 0.5k） ｜ Put Wall 11（-7.9%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 94.1%｜历史 Rank 35%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,481 股

11-20（MEDIUM △）Top ΔOI: 12C +31 ｜ 13C +13
11-20（MEDIUM △）仓位参考: Max Pain 12 ｜ Call Wall 12（+0.5%，弱）（OI 0.7k） ｜ Put Wall 11（-7.9%，弱）（OI 0.5k）

11-27（Activity LOW）仓位参考: Max Pain 12 ｜ Call Wall 12.5（+4.6%）（OI 4.0k） ｜ Put Wall 12.5（+4.6%）（OI 0.3k）

12-04（Activity LOW）仓位参考: Max Pain 13 ｜ Call Wall 12.5（+4.6%，弱）（OI 48）

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 94.1% vs 11-20 87.8%（差 +6.4pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/NNE_morning.json