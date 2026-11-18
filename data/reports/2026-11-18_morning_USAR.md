# 期权晨报 2026-11-18（快照 10:20 ET）

📊 市场环境

SPY $731.00 ｜ QQQ $659.51
VIX 24.58 ↓3.5%（5D +40.5%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 11-20（2D）ATM IV 145.4% vs 11-27 113.6%（差 +31.8pp），覆盖 新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 6.64 → 今开 6.66（+0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 7.52 ｜ 低 6.51

Options: P/C成交量 0.08 | OI比 0.48 | ATM IV 145.4% | Skew 14.9pp | Term 0.75 | ExpMove ±8.9%（近端） | Rank 79%
量化视角： IV 历史高位（Rank 79%，期权偏贵）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜保护溢价显著（Skew 14.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.48）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.08×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.48×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（2D）±8.9% ｜ 11-27（9D）±14.1% ｜ 12-04（16D）±23.9% ｜ 12-11（23D）±22.9%
   ⇒ IV–VIX Spread: +120.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 146,819 | GEX Change vs 上次快照 1,726,913 | Flip: Primary Flip: 7.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 226 / LOW 97 / INVALID 109
结构观察区: Primary Flip 7.36（全链重定价，覆盖 100%）
最近结构参考: Flip 7（现价高于该位 0.5%）
量化视角： 正 Gamma（15万，无历史分位）｜由负转正（+173万）｜现价位于 Flip 上方 0.50%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 7（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 7.0P — Vol 1,939 | 最新价 $1.02 | OI 2344→4058 (ΔOI +1714张) | ΔOI/Volume 88.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1714张（+73.1% vs前日OI），连续性待观察（方向未知）
12-18 12.0C — Vol 1,368 | 最新价 $0.05 | OI 1447→2757 (ΔOI +1310张) | ΔOI/Volume 95.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1310张（+90.5% vs前日OI），连续性待观察（方向未知）
11-20 5.0P — Vol 753 | 最新价 $0.01 | OI 226→604 (ΔOI +378张) | ΔOI/Volume 50.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增378张（+167.3% vs前日OI），连续性待观察（方向未知）
12-18 10.0C — Vol 542 | 最新价 $0.11 | OI 3258→3574 (ΔOI +316张) | ΔOI/Volume 58.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增316张（+9.7% vs前日OI），连续性待观察（方向未知）
11-20 7.0C — Vol 672 | 最新价 $0.15 | OI 306→616 (ΔOI +310张) | ΔOI/Volume 46.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增310张（+101.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,028 张（Put 2,092 / Call 1,936），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +1.0k / P -2.7k ｜ Activity HIGH ｜ 2D
11-27  C +0.7k / P -22 ｜ Activity MEDIUM △ ｜ 9D
12-04  C +0.2k / P +73 ｜ Activity MEDIUM △ ｜ 16D
12-11  C +0.1k / P -30 ｜ Activity MEDIUM △ ｜ 23D

📆 11-20 Forward Structure
存量OI: C 56.7k / P 27.3k，今日变化ΔOI: C +1.0k / P -2.7k，平值价格ATM: C $0.32 / P $0.34 ｜ ATM IV 145.4%，净 delta 敞口 348k shares
Top ΔOI: P 8 -1,121 ｜ P 10 -614 ｜ P 8 -531
仓位参考: Max Pain 10 ｜ Call Wall 8（+8.2%，弱）（OI 2.0k） ｜ Put Wall 8（+8.2%，弱）（OI 4.0k）
量化解读： 存量 Call 重｜ATM IV 145.4%｜历史 Rank 79%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 347,799 股

11-27（MEDIUM △）Top ΔOI: 8C +178 ｜ 7C +149
11-27（MEDIUM △）仓位参考: Max Pain 8 ｜ Call Wall 8（+8.2%，弱）（OI 3.6k） ｜ Put Wall 8（+8.2%，弱）（OI 0.5k）

12-04（MEDIUM △）Top ΔOI: 7C +120
12-04（MEDIUM △）仓位参考: Max Pain 9 ｜ Call Wall 7.5（+1.4%，弱）（OI 0.2k） ｜ Put Wall 7（-5.3%，弱）（OI 0.1k）

12-11（MEDIUM △）Top ΔOI: 7C +63 ｜ 8C +23
12-11（MEDIUM △）仓位参考: Max Pain 9 ｜ Call Wall 7.5（+1.4%，弱）（OI 97） ｜ Put Wall 8（+8.2%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 145.4% vs 11-27 113.6%（差 +31.8pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/USAR_morning.json