# 期权晨报 2026-11-10（快照 10:20 ET）

📊 市场环境

SPY $751.28 ｜ QQQ $676.84
VIX 19.85 ↓0.3%（5D -4.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-11 180C ΔOI +11,231（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 178.67 → 今开 173.98（-2.6%） | 较昨收变动（含盘初走势） ｜ 今日高 174.65 ｜ 低 170.12

Options: P/C成交量 1.02 | OI比 0.68 | ATM IV 74.6% | Skew 6.2pp | Term 0.77 | ExpMove ±3.5%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价显著（Skew 6.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.02×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-11（1D）±3.5% ｜ 11-13（3D）±5.2% ｜ 11-16（6D）±5.8% ｜ 11-18（8D）±9.7%
   ⇒ IV–VIX Spread: +54.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -86,421,302 | GEX Change vs 上次快照 16,001,567 | Flip: Primary Flip: 178.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1099 / LOW 242 / INVALID 725
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 178.69（全链重定价，覆盖 100%）
最近结构参考: Flip 179（现价低于该位 2.9%）
量化视角： 负 Gamma（8642万，无历史分位）｜负 Gamma 缓解（+1600万）｜现价位于 Flip 下方 2.93%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 180（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 179（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 190.0C — Vol 47,261 | 最新价 $1.15 | OI 22514→36906 (ΔOI +14392张) | ΔOI/Volume 30.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14392张（+63.9% vs前日OI），连续性待观察（方向未知）
11-11 180.0C — Vol 55,100 | 最新价 $3.16 | OI 406→11637 (ΔOI +11231张) | ΔOI/Volume 20.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11231张（+2766.3% vs前日OI），连续性待观察（方向未知）
11-13 180.0C — Vol 37,679 | 最新价 $4.35 | OI 793→10833 (ΔOI +10040张) | ΔOI/Volume 26.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10040张（+1266.1% vs前日OI），连续性待观察（方向未知）
11-27 145.0P — Vol 9,971 | 最新价 $1.35 | OI 490→9335 (ΔOI +8845张) | ΔOI/Volume 88.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8845张（+1805.1% vs前日OI），连续性待观察（方向未知）
11-27 182.5C — Vol 9,046 | 最新价 $8.55 | OI 0→8721 (ΔOI +8721张) | ΔOI/Volume 96.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8721张（前日OI缺失），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 53,229 张（Put 8,845 / Call 44,384），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-11  C +86.7k / P +45.2k ｜ Activity HIGH ｜ 1D
11-13  C +75.4k / P +38.4k ｜ Activity HIGH ｜ 3D
11-16  C +27.7k / P +13.5k ｜ Activity HIGH ｜ 6D
11-18  C +22.9k / P +9.9k ｜ Activity HIGH ｜ 8D

📆 11-11 Forward Structure
存量OI: C 137.8k / P 93.4k，今日变化ΔOI: C +86.7k / P +45.2k，平值价格ATM: C $3.35 / P $2.69 ｜ ATM IV 74.6%，净 delta 敞口 222k shares
Top ΔOI: C 180 +11,231 ｜ C 190 +8,028 ｜ C 185 +7,879
仓位参考: Max Pain 180 ｜ Call Wall 180（+3.8%，弱）（OI 11.6k） ｜ Put Wall 170（-2.0%，弱）（OI 9.5k）
量化解读： 存量 Call 重｜ATM IV 74.6%｜历史 Rank 92%（近端代理）｜IV/RV 1.55×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 222,129 股

📆 11-13 Forward Structure
存量OI: C 466.7k / P 355.9k，今日变化ΔOI: C +75.4k / P +38.4k，平值价格ATM: C $4.85 / P $4.15 ｜ ATM IV 68.4%，净 delta 敞口 1.8M shares
Top ΔOI: C 190 +14,392 ｜ C 180 +10,040 ｜ C 185 +8,325
仓位参考: Max Pain 190 ｜ Call Wall 190（+9.5%，弱）（OI 36.9k） ｜ Put Wall 170（-2.0%，弱）（OI 18.0k）
量化解读： 存量 Call 重｜ATM IV 68.4%｜历史 Rank 92%（近端代理）｜IV/RV 1.42×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,828,812 股

📆 11-16 Forward Structure
存量OI: C 54.2k / P 26.3k，今日变化ΔOI: C +27.7k / P +13.5k，平值价格ATM: C $5.47 / P $4.65 ｜ ATM IV 56.6%，净 delta 敞口 272k shares
Top ΔOI: C 200 +5,348 ｜ C 180 +4,595 ｜ P 170 +2,834
仓位参考: Max Pain 180 ｜ Call Wall 180（+3.8%，弱）（OI 4.8k） ｜ Put Wall 170（-2.0%）（OI 3.6k）
量化解读： 存量 Call 重｜ATM IV 56.6%｜历史 Rank 92%（近端代理）｜IV/RV 1.18×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 271,724 股

📆 11-18 Forward Structure
存量OI: C 50.1k / P 24.1k，今日变化ΔOI: C +22.9k / P +9.9k，平值价格ATM: C $8.80 / P $7.94 ｜ ATM IV 81.0%，净 delta 敞口 336k shares
Top ΔOI: C 155 +2,199 ｜ C 185 +2,137 ｜ C 190 +2,054
仓位参考: Max Pain 180 ｜ Call Wall 190（+9.5%，弱）（OI 4.1k） ｜ Put Wall 160（-7.8%，弱）（OI 2.5k）
量化解读： 存量 Call 重｜ATM IV 81.0%｜历史 Rank 92%（近端代理）｜IV/RV 1.68×（近似）｜净 delta 敞口 正 336,198 股

📅 事件差分（观察，非因果）: 11-11（1D）ATM IV 74.6% vs 11-13 68.4%（差 +6.1pp）——覆盖 Core Inflation Rate MoM、Inflation Rate MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=93 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=93）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/NVDA_morning.json