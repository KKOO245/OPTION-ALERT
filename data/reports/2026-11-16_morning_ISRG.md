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
🟡 **事件差分**: 11-20 ATM IV 41.9% vs 11-27 31.2%（差 +10.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 443.59 → 今开 444.38（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 446.20 ｜ 低 437.73

Options: P/C成交量 0.83 | OI比 1.00 | ATM IV 41.9% | Skew 0.4pp | Term 0.80 | ExpMove ±3.0%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价薄（Skew 0.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.83×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.00×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（4D）±3.0% ｜ 11-27（11D）±4.6% ｜ 12-04（18D）±5.5% ｜ 12-11（25D）±7.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,467,168 | GEX Change vs 上次快照 -293,015 | Flip: Primary Flip: 418.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 289 / LOW 159 / INVALID 518
结构观察区: Primary Flip 418.91（全链重定价，覆盖 93%）
Call Wall 480（弱结构｜现价低于该位 8.5%）
最近结构参考: Flip 419（现价高于该位 4.8%）
量化视角： 正 Gamma（247万，无历史分位）｜正 Gamma 减弱（29万）｜现价位于 Flip 上方 4.84%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 410（MaxPain，仅结算参考）；上方 480（Call Wall，弱结构）。
• Gamma 区域：切换参考 419（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 465.0C — Vol 61 | 最新价 $2.00 | OI 198→250 (ΔOI +52张) | ΔOI/Volume 85.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增52张（+26.3% vs前日OI），连续性待观察（方向未知）
11-20 472.5C — Vol 56 | 最新价 $1.10 | OI 2→54 (ΔOI +52张) | ΔOI/Volume 92.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增52张（+2600.0% vs前日OI），连续性待观察（方向未知）
11-20 420.0P — Vol 48 | 最新价 $1.05 | OI 266→313 (ΔOI +47张) | ΔOI/Volume 97.9% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增47张（+17.7% vs前日OI），值得跟踪（方向未知）
12-18 510.0C — Vol 50 | 最新价 $1.80 | OI 120→165 (ΔOI +45张) | ΔOI/Volume 90.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增45张（+37.5% vs前日OI），连续性待观察（方向未知）
12-18 490.0C — Vol 49 | 最新价 $3.60 | OI 212→255 (ΔOI +43张) | ΔOI/Volume 87.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增43张（+20.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 239 张（Put 47 / Call 192），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 4D
11-27  C +73 / P +38 ｜ Activity MEDIUM △ ｜ 11D
12-04  C +28 / P +13 ｜ Activity LOW ｜ 18D
12-11  C +1 / P +3 ｜ Activity MEDIUM △ ｜ 25D

📆 11-20 Forward Structure
存量OI: C 10.6k / P 10.6k，今日变化ΔOI: C +0.2k / P +0.1k，平值价格ATM: C $7.78 / P $5.30 ｜ ATM IV 41.9%，净 delta 敞口 -511 shares
Top ΔOI: C 465 +52 ｜ C 472 +52 ｜ P 420 +47
仓位参考: Max Pain 410 ｜ Call Wall 420（-4.4%，弱）（OI 0.8k） ｜ Put Wall 410（-6.6%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 41.9%｜历史 Rank 64%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 511 股

11-27（MEDIUM △）Top ΔOI: 475C +17 ｜ 472C +15
11-27（MEDIUM △）仓位参考: Max Pain 430 ｜ Call Wall 430（-2.1%，弱）（OI 64） ｜ Put Wall 410（-6.6%，弱）（OI 42）

12-04（Activity LOW）仓位参考: Max Pain 450 ｜ Call Wall 475（+8.2%，弱）（OI 81） ｜ Put Wall 405（-7.8%，弱）（OI 25）

12-11（MEDIUM △）Top ΔOI: 465C -4 ｜ 400P +1
12-11（MEDIUM △）仓位参考: Max Pain 440 ｜ Call Wall 450（+2.5%）（OI 0.1k） ｜ Put Wall 435（-1.0%）（OI 22）

📅 事件差分（观察，非因果）: 11-20（4D）ATM IV 41.9% vs 11-27 31.2%（差 +10.6pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/ISRG_morning.json