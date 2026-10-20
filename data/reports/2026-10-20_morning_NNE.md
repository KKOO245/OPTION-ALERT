# 期权晨报 2026-10-20（快照 10:20 ET）

📊 市场环境

SPY $769.58 ｜ QQQ $717.63
VIX 18.12 ↓1.7%（5D +18.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 10-23 ATM IV 91.9% vs 10-30 77.8%（差 +14.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-23 13C ΔOI +286（距现价 +4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 13.01 → 今开 12.66（-2.7%） | 较昨收变动（含盘初走势） ｜ 今日高 13.07 ｜ 低 12.56

Options: P/C成交量 0.12 | OI比 0.27 | ATM IV 91.9% | Skew -6.5pp | Term 0.80 | ExpMove ±8.0%（近端） | Rank 28%
量化视角： IV 中性（Rank 28%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.27）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.12×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.27×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（3D）±8.0% ｜ 10-30（10D）±11.4% ｜ 11-06（17D）±14.3% ｜ 11-13（24D）±17.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 592,571 | GEX Change vs 上次快照 318,351 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 164 / LOW 83 / INVALID 155
结构观察区: NO_CROSS
Put Wall 14（现价低于该位 7.6%）
最近结构参考: Put Wall 14（现价低于该位 7.6%）
量化视角： 正 Gamma（59万，无历史分位）｜正 Gamma 增强（+32万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（Put Wall） / 14（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 14.0C — Vol 344 | 最新价 $0.17 | OI 121→426 (ΔOI +305张) | ΔOI/Volume 88.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增305张（+252.1% vs前日OI），连续性待观察（方向未知）
10-23 13.5C — Vol 429 | 最新价 $0.29 | OI 212→498 (ΔOI +286张) | ΔOI/Volume 66.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增286张（+134.9% vs前日OI），连续性待观察（方向未知）
10-30 14.5C — Vol 194 | 最新价 $0.25 | OI 97→286 (ΔOI +189张) | ΔOI/Volume 97.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增189张（+194.8% vs前日OI），连续性待观察（方向未知）
10-30 15.0C — Vol 132 | 最新价 $0.15 | OI 40→141 (ΔOI +101张) | ΔOI/Volume 76.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增101张（+252.5% vs前日OI），连续性待观察（方向未知）
11-20 12.0P — Vol 101 | 最新价 $0.60 | OI 224→298 (ΔOI +74张) | ΔOI/Volume 73.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增74张（+33.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 955 张（Put 74 / Call 881），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +0.7k / P +43 ｜ Activity HIGH ｜ 3D
10-30  C +0.4k / P +18 ｜ Activity HIGH ｜ 10D
11-06  C +6 / P +11 ｜ Activity MEDIUM △ ｜ 17D
11-13  C +17 / P -74 ｜ Activity HIGH ｜ 24D

📆 10-23 Forward Structure
存量OI: C 6.5k / P 1.7k，今日变化ΔOI: C +0.7k / P +43，平值价格ATM: C $0.51 / P $0.53 ｜ ATM IV 91.9%，净 delta 敞口 17k shares
Top ΔOI: C 14 +305 ｜ C 13 +286 ｜ C 13 +51
仓位参考: Max Pain 14 ｜ Put Wall 14（+8.3%）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 91.9%｜历史 Rank 28%（近端代理）｜IV/RV 1.56×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 17,308 股

📆 10-30 Forward Structure
存量OI: C 6.8k / P 1.0k，今日变化ΔOI: C +0.4k / P +18，平值价格ATM: C $0.70 / P $0.78 ｜ ATM IV 77.8%，净 delta 敞口 8k shares
Top ΔOI: C 14 +42
仓位参考: Max Pain 14 ｜ Put Wall 14（+8.3%）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 77.8%｜历史 Rank 28%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 7,612 股

11-06（MEDIUM △）Top ΔOI: 13P +5
11-06（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 13（+0.5%，弱）（OI 77）

📆 11-13 Forward Structure
存量OI: C 0.6k / P 0.4k，今日变化ΔOI: C +17 / P -74，平值价格ATM: C $1.28 / P $1.00 ｜ ATM IV 75.7%，净 delta 敞口 3k shares
Top ΔOI: P 12 -125 ｜ P 13 +50
仓位参考: Max Pain 14 ｜ Call Wall 13.5（+4.4%，弱）（OI 50） ｜ Put Wall 12.5（-3.3%）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 75.7%｜历史 Rank 28%（近端代理）｜IV/RV 1.29×（近似）｜净 delta 敞口 正 2,764 股

📅 事件差分（观察，非因果）: 10-23（3D）ATM IV 91.9% vs 10-30 77.8%（差 +14.1pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/NNE_morning.json