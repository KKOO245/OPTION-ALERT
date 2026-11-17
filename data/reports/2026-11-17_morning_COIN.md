# 期权晨报 2026-11-17（快照 10:20 ET）

📊 市场环境

SPY $734.92 ｜ QQQ $656.95
VIX 22.73 ↓0.8%（5D +16.8%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.8　✅ 今日已公布
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **事件差分**: 11-20（3D）ATM IV 89.6% vs 11-27 72.3%（差 +17.3pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 119.84 → 今开 117.73（-1.8%） | 较昨收变动（含盘初走势） ｜ 今日高 121.61 ｜ 低 117.72

Options: P/C成交量 0.34 | OI比 0.42 | ATM IV 89.6% | Skew 6.7pp | Term 0.81 | ExpMove ±7.0%（近端） | Rank 79%
量化视角： IV 历史高位（Rank 79%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价显著（Skew 6.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.42）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.42×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（3D）±7.0% ｜ 11-27（10D）±9.9% ｜ 12-04（17D）±12.5% ｜ 12-11（24D）±15.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,903,938 | GEX Change vs 上次快照 4,392,013 | Flip: Primary Flip: 121.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 424 / LOW 198 / INVALID 286
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 121.33（全链重定价，覆盖 100%）
Put Wall 110（现价高于该位 9.2%）
最近结构参考: Flip 121（现价低于该位 1.0%）
量化视角： 负 Gamma（190万，无历史分位）｜负 Gamma 缓解（+439万）｜现价位于 Flip 下方 0.98%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 110（Put Wall）；上方 133（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 121（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 150.0C — Vol 3,061 | 最新价 $0.08 | OI 5313→6056 (ΔOI +743张) | ΔOI/Volume 24.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增743张（+14.0% vs前日OI），连续性待观察（方向未知）
11-20 130.0C — Vol 1,442 | 最新价 $1.13 | OI 465→935 (ΔOI +470张) | ΔOI/Volume 32.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增470张（+101.1% vs前日OI），连续性待观察（方向未知）
12-18 125.0C — Vol 612 | 最新价 $8.30 | OI 124→522 (ΔOI +398张) | ΔOI/Volume 65.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增398张（+321.0% vs前日OI），连续性待观察（方向未知）
11-20 95.0P — Vol 702 | 最新价 $0.16 | OI 908→1288 (ΔOI +380张) | ΔOI/Volume 54.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增380张（+41.9% vs前日OI），连续性待观察（方向未知）
11-20 125.0C — Vol 1,489 | 最新价 $2.29 | OI 95→473 (ΔOI +378张) | ΔOI/Volume 25.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增378张（+397.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,369 张（Put 380 / Call 1,989），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +5.8k / P -2.7k ｜ Activity MEDIUM △ ｜ 3D
11-27  C +1.9k / P +0.2k ｜ Activity HIGH ｜ 10D
12-04  C +0.7k / P +0.3k ｜ Activity MEDIUM △ ｜ 17D
12-11  C +0.5k / P +0.1k ｜ Activity MEDIUM △ ｜ 24D

📆 11-20 Forward Structure
存量OI: C 139.5k / P 58.7k，今日变化ΔOI: C +5.8k / P -2.7k，平值价格ATM: C $4.37 / P $4.02 ｜ ATM IV 89.6%，净 delta 敞口 515k shares
Top ΔOI: P 160 -1,031 ｜ P 165 -763
仓位参考: Max Pain 133 ｜ Call Wall 131（+9.0%，弱）（OI 7.4k） ｜ Put Wall 120（-0.1%，弱）（OI 6.4k）
量化解读： 存量 Call 重｜ATM IV 89.6%｜历史 Rank 79%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 515,092 股

📆 11-27 Forward Structure
存量OI: C 9.7k / P 9.6k，今日变化ΔOI: C +1.9k / P +0.2k，平值价格ATM: C $6.35 / P $5.55 ｜ ATM IV 72.3%，净 delta 敞口 75k shares
Top ΔOI: C 130 +228
仓位参考: Max Pain 131 ｜ Call Wall 130（+8.2%，弱）（OI 0.5k） ｜ Put Wall 120（-0.1%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜ATM IV 72.3%｜历史 Rank 79%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 正 74,515 股

12-04（MEDIUM △）Top ΔOI: 130C +149 ｜ 120P +105
12-04（MEDIUM △）仓位参考: Max Pain 140 ｜ Call Wall 130（+8.2%，弱）（OI 0.3k）

12-11（MEDIUM △）Top ΔOI: 140C +225 ｜ 125C +77
12-11（MEDIUM △）仓位参考: Max Pain 135 ｜ Call Wall 130（+8.2%，弱）（OI 0.1k）

📅 事件差分（观察，非因果）: 11-20（3D）ATM IV 89.6% vs 11-27 72.3%（差 +17.3pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/COIN_morning.json