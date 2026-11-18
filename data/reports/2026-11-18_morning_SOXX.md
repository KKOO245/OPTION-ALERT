# 期权晨报 2026-11-18（快照 10:20 ET）

📊 市场环境

SPY $731.20 ｜ QQQ $659.40
VIX 24.58 ↓3.5%（5D +40.5%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 26.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 11-20（2D）ATM IV 89.6% vs 11-27 66.7%（差 +22.9pp），覆盖 新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-20 138P ΔOI +1,045（距现价 -2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 141.46 → 今开 143.73（+1.6%） | 较昨收变动（含盘初走势） ｜ 今日高 144.23 ｜ 低 139.07

Options: P/C成交量 2.61 | OI比 1.77 | ATM IV 89.6% | Skew 13.0pp | Term 0.68 | ExpMove ±5.4%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.68，近月 IV 高于远月）｜保护溢价显著（Skew 13.0pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 2.61）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.61×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.77×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-20（2D）±5.4% ｜ 11-27（9D）±8.4% ｜ 12-04（16D）±10.1% ｜ 12-11（23D）±12.4%
   ⇒ IV–VIX Spread: +65.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -60,305,682 | GEX Change vs 上次快照 3,440,075 | Flip: Primary Flip: 152.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 634 / LOW 375 / INVALID 617
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 152.96（全链重定价，覆盖 97%）
最近结构参考: Flip 153（现价低于该位 7.2%）
量化视角： 负 Gamma（6031万，无历史分位）｜负 Gamma 缓解（+344万）｜现价位于 Flip 下方 7.24%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 153（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 145.0C — Vol 225 | 最新价 $6.00 | OI 63→1169 (ΔOI +1106张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1106张（+1755.6% vs前日OI），连续性待观察（方向未知）
11-20 138.0P — Vol 1,182 | 最新价 $3.50 | OI 116→1161 (ΔOI +1045张) | ΔOI/Volume 88.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1045张（+900.9% vs前日OI），连续性待观察（方向未知）
12-04 125.0P — Vol 1,026 | 最新价 $2.95 | OI 105→1092 (ΔOI +987张) | ΔOI/Volume 96.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增987张（+940.0% vs前日OI），连续性待观察（方向未知）
12-04 160.0C — Vol 102 | 最新价 $1.55 | OI 1077→2014 (ΔOI +937张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增937张（+87.0% vs前日OI），连续性待观察（方向未知）
11-27 145.0C — Vol 1,859 | 最新价 $3.93 | OI 293→1051 (ΔOI +758张) | ΔOI/Volume 40.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增758张（+258.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,833 张（Put 2,032 / Call 2,801），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +2.2k / P -5.7k ｜ Activity HIGH ｜ 2D
11-27  C +1.4k / P +1.5k ｜ Activity MEDIUM △ ｜ 9D
12-04  C +2.5k / P +1.4k ｜ Activity HIGH ｜ 16D
12-11  C +0.3k / P +0.1k ｜ Activity MEDIUM △ ｜ 23D

📆 11-20 Forward Structure
存量OI: C 201.9k / P 356.6k，今日变化ΔOI: C +2.2k / P -5.7k，平值价格ATM: C $4.00 / P $3.66 ｜ ATM IV 89.6%，净 delta 敞口 575k shares
Top ΔOI: P 140 -4,285 ｜ P 170 -3,004 ｜ P 138 +1,045
仓位参考: Max Pain 155 ｜ Call Wall 145（+2.2%，弱）（OI 6.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 89.6%｜历史 Rank 99%（近端代理）｜IV/RV 0.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 575,168 股

11-27（MEDIUM △）Top ΔOI: 145C +758 ｜ 130P +563
11-27（MEDIUM △）仓位参考: Max Pain 160 ｜ Put Wall 150（+5.7%，弱）（OI 3.6k）

📆 12-04 Forward Structure
存量OI: C 13.8k / P 23.3k，今日变化ΔOI: C +2.5k / P +1.4k，平值价格ATM: C $6.90 / P $7.40 ｜ ATM IV 64.8%，净 delta 敞口 44k shares
Top ΔOI: C 145 +1,106 ｜ P 125 +987 ｜ C 160 +937
仓位参考: Max Pain 153 ｜ Call Wall 145（+2.2%，弱）（OI 1.2k） ｜ Put Wall 140（-1.3%，弱）（OI 5.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 64.8%｜历史 Rank 99%（近端代理）｜IV/RV 0.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 43,961 股

12-11（MEDIUM △）Top ΔOI: 143C +81 ｜ 130P +65
12-11（MEDIUM △）仓位参考: Max Pain 147 ｜ Call Wall 147（+3.6%，弱）（OI 0.2k） ｜ Put Wall 140（-1.3%）（OI 0.8k）

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 89.6% vs 11-27 66.7%（差 +22.9pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/SOXX_morning.json