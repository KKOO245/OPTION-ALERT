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
🔴 **事件差分**: 11-20（2D）ATM IV 98.4% vs 11-27 76.5%（差 +21.9pp），覆盖 新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-20 110P ΔOI +2,476（距现价 -3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 115.02 → 今开 115.20（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 115.70 ｜ 低 110.86

Options: P/C成交量 0.18 | OI比 0.46 | ATM IV 98.4% | Skew 7.2pp | Term 0.76 | ExpMove ±5.9%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价显著（Skew 7.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.18×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（2D）±5.9% ｜ 11-27（9D）±10.3% ｜ 12-04（16D）±12.4% ｜ 12-11（23D）±15.4%
   ⇒ IV–VIX Spread: +73.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -8,049,146 | GEX Change vs 上次快照 298,562 | Flip: Primary Flip: 119.82（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 405 / LOW 222 / INVALID 281
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 119.82（全链重定价，覆盖 96%）
Put Wall 110（现价高于该位 3.2%）
最近结构参考: Put Wall 110（现价高于该位 3.2%）
量化视角： 负 Gamma（805万，无历史分位）｜负 Gamma 缓解（+30万）｜现价位于 Flip 下方 5.26%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 110（Put Wall）；上方 131（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 120（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 105.0P — Vol 4,491 | 最新价 $0.96 | OI 995→5079 (ΔOI +4084张) | ΔOI/Volume 90.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4084张（+410.4% vs前日OI），连续性待观察（方向未知）
12-18 185.0C — Vol 3,002 | 最新价 $0.24 | OI 1932→4599 (ΔOI +2667张) | ΔOI/Volume 88.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2667张（+138.0% vs前日OI），连续性待观察（方向未知）
11-20 110.0P — Vol 4,630 | 最新价 $2.05 | OI 3911→6387 (ΔOI +2476张) | ΔOI/Volume 53.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2476张（+63.3% vs前日OI），连续性待观察（方向未知）
12-04 60.0P — Vol 1,261 | 最新价 $0.14 | OI 753→1972 (ΔOI +1219张) | ΔOI/Volume 96.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1219张（+161.9% vs前日OI），连续性待观察（方向未知）
11-20 120.0C — Vol 1,908 | 最新价 $2.04 | OI 424→1189 (ΔOI +765张) | ΔOI/Volume 40.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增765张（+180.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,211 张（Put 7,779 / Call 3,432），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C -0.8k / P +4.9k ｜ Activity MEDIUM △ ｜ 2D
11-27  C +2.5k / P +0.4k ｜ Activity HIGH ｜ 9D
12-04  C +1.4k / P +1.7k ｜ Activity HIGH ｜ 16D
12-11  C +0.1k / P +65 ｜ Activity MEDIUM △ ｜ 23D

📆 11-20 Forward Structure
存量OI: C 138.7k / P 63.7k，今日变化ΔOI: C -0.8k / P +4.9k，平值价格ATM: C $3.20 / P $3.45 ｜ ATM IV 98.4%，净 delta 敞口 98k shares
Top ΔOI: P 105 +4,084 ｜ P 110 +2,476
仓位参考: Max Pain 131 ｜ Put Wall 120（+5.7%，弱）（OI 6.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 98.4%｜历史 Rank 86%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 97,985 股

📆 11-27 Forward Structure
存量OI: C 12.2k / P 9.9k，今日变化ΔOI: C +2.5k / P +0.4k，平值价格ATM: C $5.20 / P $6.45 ｜ ATM IV 76.5%，净 delta 敞口 61k shares
Top ΔOI: C 126 +445
仓位参考: Max Pain 126 ｜ Call Wall 122（+7.5%，弱）（OI 0.3k） ｜ Put Wall 120（+5.7%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 76.5%｜历史 Rank 86%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 61,205 股

📆 12-04 Forward Structure
存量OI: C 8.3k / P 11.5k，今日变化ΔOI: C +1.4k / P +1.7k，平值价格ATM: C $6.70 / P $7.36 ｜ ATM IV 75.7%，净 delta 敞口 10k shares
Top ΔOI: C 133 +226 ｜ P 120 +198
仓位参考: Max Pain 135 ｜ Put Wall 120（+5.7%，弱）（OI 0.7k）
量化解读： 存量 Put 重｜ATM IV 75.7%｜历史 Rank 86%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 9,657 股

12-11（MEDIUM △）Top ΔOI: 120P +35 ｜ 110P +21
12-11（MEDIUM △）仓位参考: Max Pain 135 ｜ Put Wall 120（+5.7%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 98.4% vs 11-27 76.5%（差 +21.9pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/COIN_morning.json