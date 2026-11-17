# 期权晨报 2026-11-16（快照 10:20 ET）

📊 市场环境

SPY $739.95 ｜ QQQ $661.75
VIX 21.57 ↑11.8%（5D +8.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.8
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **事件差分**: 11-20 ATM IV 79.8% vs 11-27 68.0%（差 +11.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 38.76 → 今开 37.50（-3.3%） | 较昨收变动（含盘初走势） ｜ 今日高 38.24 ｜ 低 36.90

Options: P/C成交量 0.38 | OI比 0.49 | ATM IV 79.8% | Skew 5.3pp | Term 0.84 | ExpMove ±7.5%（近端） | Rank 71%
量化视角： IV 中性（Rank 71%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价中性（Skew 5.3pp）｜存量 Call 偏重（OI比 0.49）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（4D）±7.5% ｜ 11-27（11D）±8.9% ｜ 12-04（18D）±13.0% ｜ 12-11（25D）±13.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,292,043 | GEX Change vs 上次快照 3,904,425 | Flip: Primary Flip: 34.55（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 251 / LOW 72 / INVALID 115
结构观察区: Primary Flip 34.55（全链重定价，覆盖 100%）
Put Wall 35（现价高于该位 8.3%）
最近结构参考: Put Wall 35（现价高于该位 8.3%）
量化视角： 正 Gamma（629万，无历史分位）｜正 Gamma 增强（+390万）｜现价位于 Flip 上方 9.71%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall）；上方 40（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 35（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 40.0C — Vol 15,328 | 最新价 $2.60 | OI 2166→16729 (ΔOI +14563张) | ΔOI/Volume 95.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14563张（+672.4% vs前日OI），连续性待观察（方向未知）
12-18 45.0C — Vol 14,923 | 最新价 $1.10 | OI 5735→16598 (ΔOI +10863张) | ΔOI/Volume 72.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10863张（+189.4% vs前日OI），连续性待观察（方向未知）
11-20 40.0C — Vol 1,238 | 最新价 $0.96 | OI 1277→1989 (ΔOI +712张) | ΔOI/Volume 57.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增712张（+55.8% vs前日OI），连续性待观察（方向未知）
11-27 50.0C — Vol 593 | 最新价 $0.11 | OI 1964→2553 (ΔOI +589张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增589张（+30.0% vs前日OI），连续性待观察（方向未知）
11-20 42.5C — Vol 408 | 最新价 $0.42 | OI 139→486 (ΔOI +347张) | ΔOI/Volume 85.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增347张（+249.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 27,074 张（Put 0 / Call 27,074），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +2.0k / P +0.3k ｜ Activity MEDIUM △ ｜ 4D
11-27  C +1.0k / P +0.3k ｜ Activity MEDIUM △ ｜ 11D
12-04  C +0.1k / P +74 ｜ Activity MEDIUM △ ｜ 18D
12-11  C +61 / P +32 ｜ Activity MEDIUM △ ｜ 25D

📆 11-20 Forward Structure
存量OI: C 28.2k / P 13.8k，今日变化ΔOI: C +2.0k / P +0.3k，平值价格ATM: C $1.40 / P $1.45 ｜ ATM IV 79.8%，净 delta 敞口 32k shares
Top ΔOI: C 40 +712
仓位参考: Max Pain 40 ｜ Call Wall 40（+5.5%，弱）（OI 2.0k） ｜ Put Wall 35（-7.7%）（OI 3.9k）
量化解读： 存量 Call 重｜ATM IV 79.8%｜历史 Rank 71%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 32,393 股

11-27（MEDIUM △）Top ΔOI: 35P +209
11-27（MEDIUM △）仓位参考: Max Pain 42

12-04（MEDIUM △）仓位参考: Max Pain 35 ｜ Call Wall 35（-7.7%）（OI 0.5k） ｜ Put Wall 35（-7.7%，弱）（OI 0.1k）

12-11（MEDIUM △）Top ΔOI: 39C -21 ｜ 40P +18
12-11（MEDIUM △）仓位参考: Max Pain 42 ｜ Call Wall 37（-2.4%，弱）（OI 68） ｜ Put Wall 40（+5.5%，弱）（OI 89）

📅 事件差分（观察，非因果）: 11-20（4D）ATM IV 79.8% vs 11-27 68.0%（差 +11.8pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/MP_morning.json