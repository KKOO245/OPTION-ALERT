# 期权晨报 2026-11-12（快照 10:20 ET）

📊 市场环境

SPY $757.88 ｜ QQQ $688.17
VIX 18.45 ↑5.5%（5D -34.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-16 165P ΔOI +3,100（距现价 +2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 173.73 → 今开 150.99（-13.1%） | 较昨收变动（含盘初走势） ｜ 今日高 164.08 ｜ 低 148.80

Options: P/C成交量 0.80 | OI比 0.71 | ATM IV 78.6% | Skew 6.9pp | Term 0.69 | ExpMove ±0.3%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价显著（Skew 6.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.71）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.71×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±0.3% ｜ 11-16（4D）±6.5% ｜ 11-18（6D）±10.6% ｜ 11-20（8D）±0.6%
   ⇒ IV–VIX Spread: +60.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -123,892,309 | GEX Change vs 上次快照 -134,855,276 | Flip: Primary Flip: 170.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1290 / LOW 246 / INVALID 618
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 170.18（全链重定价，覆盖 100%）
最近结构参考: Flip 170（现价低于该位 5.4%）
量化视角： 负 Gamma（1.24亿，无历史分位）｜由正转负（1.35亿）｜现价位于 Flip 下方 5.43%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 178（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 170（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 185.0C — Vol 77,702 | 最新价 $0.32 | OI 17844→39898 (ΔOI +22054张) | ΔOI/Volume 28.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22054张（+123.6% vs前日OI），连续性待观察（方向未知）
11-13 180.0C — Vol 110,620 | 最新价 $0.99 | OI 21886→32939 (ΔOI +11053张) | ΔOI/Volume 10.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11053张（+50.5% vs前日OI），连续性待观察（方向未知）
11-13 130.0P — Vol 12,252 | 最新价 $0.01 | OI 5948→16943 (ΔOI +10995张) | ΔOI/Volume 89.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10995张（+184.8% vs前日OI），连续性待观察（方向未知）
11-13 187.5C — Vol 30,452 | 最新价 $0.19 | OI 8218→19024 (ΔOI +10806张) | ΔOI/Volume 35.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10806张（+131.5% vs前日OI），连续性待观察（方向未知）
11-20 182.5C — Vol 23,145 | 最新价 $4.95 | OI 4281→15054 (ΔOI +10773张) | ΔOI/Volume 46.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10773张（+251.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 65,681 张（Put 10,995 / Call 54,686），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +77.6k / P +18.8k ｜ Activity HIGH ｜ 1D
11-16  C +21.1k / P +13.6k ｜ Activity HIGH ｜ 4D
11-18  C +14.5k / P +11.4k ｜ Activity HIGH ｜ 6D
11-20  C +6.1k / P +17.6k ｜ Activity MEDIUM △ ｜ 8D

📆 11-13 Forward Structure
存量OI: C 593.3k / P 423.0k，今日变化ΔOI: C +77.6k / P +18.8k，平值价格ATM: C $0.57 / P $0.00 ｜ ATM IV 48.8%，净 delta 敞口 1.7M shares
Top ΔOI: C 185 +22,054 ｜ C 180 +11,053 ｜ P 130 +10,995
仓位参考: Max Pain 178 ｜ Call Wall 175（+8.7%，弱）（OI 17.7k） ｜ Put Wall 160（-0.6%，弱）（OI 25.3k）
量化解读： 存量 Call 重｜ATM IV 48.8%｜历史 Rank 92%（近端代理）｜IV/RV 0.94×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,743,917 股

📆 11-16 Forward Structure
存量OI: C 122.3k / P 56.9k，今日变化ΔOI: C +21.1k / P +13.6k，平值价格ATM: C $5.70 / P $4.74 ｜ ATM IV 75.0%，净 delta 敞口 -692k shares
Top ΔOI: P 165 +3,100
仓位参考: Max Pain 175 ｜ Call Wall 175（+8.7%，弱）（OI 5.4k） ｜ Put Wall 155（-3.7%，弱）（OI 6.9k）
量化解读： 存量 Call 重｜ATM IV 75.0%｜历史 Rank 92%（近端代理）｜IV/RV 1.44×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 691,686 股

📆 11-18 Forward Structure
存量OI: C 87.2k / P 50.4k，今日变化ΔOI: C +14.5k / P +11.4k，平值价格ATM: C $9.00 / P $8.10 ｜ ATM IV 101.6%，净 delta 敞口 -197k shares
Top ΔOI: C 175 +3,253 ｜ C 195 +1,868 ｜ C 180 +1,744
仓位参考: Max Pain 175 ｜ Call Wall 175（+8.7%，弱）（OI 6.2k） ｜ Put Wall 160（-0.6%）（OI 5.4k）
量化解读： 存量 Call 重｜ATM IV 101.6%｜历史 Rank 92%（近端代理）｜IV/RV 1.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 197,161 股

11-20（MEDIUM △）Top ΔOI: 220C -15,391 ｜ 182C +10,773
11-20（MEDIUM △）仓位参考: Max Pain 200 ｜ Call Wall 175（+8.7%，弱）（OI 19.6k） ｜ Put Wall 170（+5.6%，弱）（OI 40.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/NVDA_morning.json