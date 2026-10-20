# 期权晨报 2026-10-20（快照 10:20 ET）

📊 市场环境

SPY $768.68 ｜ QQQ $720.35
VIX 18.12 ↓1.7%（5D +18.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 25.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 485P ΔOI +2,370（距现价 -2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-30 360P ΔOI +69,458 占该期限总 OI 42.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 501.93 → 今开 494.99（-1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 503.62 ｜ 低 489.70

Options: P/C成交量 2.73 | OI比 1.76 | ATM IV 53.2% | Skew 11.7pp | Term 0.78 | ExpMove ±4.1%（近端） | Rank 89%
量化视角： IV 历史高位（Rank 89%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价显著（Skew 11.7pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 2.73）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.73×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.76×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-23（3D）±4.1% ｜ 10-30（10D）±7.2% ｜ 11-06（17D）±8.2% ｜ 11-13（24D）±3.8%
   ⇒ IV–VIX Spread: +35.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -34,991,127 | GEX Change vs 上次快照 -3,262,413 | Flip: Primary Flip: 562.81（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 623 / LOW 270 / INVALID 653
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 562.81（全链重定价，覆盖 100%）
Call Wall 520（弱结构｜现价低于该位 4.2%）
最近结构参考: Call Wall 520（现价低于该位 4.2%）
量化视角： 负 Gamma（3499万，无历史分位）｜负 Gamma 加深（326万）｜现价位于 Flip 下方 11.50%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 515（MaxPain，仅结算参考） / 520（Call Wall，弱结构）。
• Gamma 区域：切换参考 563（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 360.0P — Vol 69,638 | 最新价 $0.25 | OI 13010→82468 (ΔOI +69458张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增69458张（+533.9% vs前日OI），连续性待观察（方向未知）
10-30 450.0P — Vol 2,525 | 最新价 $2.36 | OI 7493→9983 (ΔOI +2490张) | ΔOI/Volume 98.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2490张（+33.2% vs前日OI），连续性待观察（方向未知）
10-30 485.0P — Vol 2,422 | 最新价 $7.90 | OI 3595→5965 (ΔOI +2370张) | ΔOI/Volume 97.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2370张（+65.9% vs前日OI），连续性待观察（方向未知）
11-20 450.0P — Vol 2,118 | 最新价 $7.02 | OI 6105→7994 (ΔOI +1889张) | ΔOI/Volume 89.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1889张（+30.9% vs前日OI），连续性待观察（方向未知）
11-06 610.0C — Vol 582 | 最新价 $0.40 | OI 9→1408 (ΔOI +1399张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1399张（+15544.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 77,606 张（Put 76,207 / Call 1,399），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +1.5k / P +1.1k ｜ Activity MEDIUM △ ｜ 3D
10-30  C +0.5k / P +75.7k ｜ Activity HIGH ｜ 10D
11-06  C +2.3k / P +1.6k ｜ Activity HIGH ｜ 17D
11-13  C +0.2k / P +96 ｜ Activity MEDIUM △ ｜ 24D

📆 10-23 Forward Structure
存量OI: C 11.2k / P 19.8k，今日变化ΔOI: C +1.5k / P +1.1k，平值价格ATM: C $9.11 / P $11.28 ｜ ATM IV 53.2%，净 delta 敞口 25k shares
Top ΔOI: C 510 +484 ｜ C 527 +224
仓位参考: Max Pain 515 ｜ Call Wall 500（+0.4%，弱）（OI 1.4k） ｜ Put Wall 510（+2.4%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 53.2%｜历史 Rank 89%（近端代理）｜IV/RV 1.79×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 24,966 股

📆 10-30 Forward Structure
存量OI: C 19.7k / P 143.2k，今日变化ΔOI: C +0.5k / P +75.7k，平值价格ATM: C $23.85 / P $12.20 ｜ ATM IV 46.0%，净 delta 敞口 -152k shares
Top ΔOI: P 360 +69,458 ｜ P 450 +2,490 ｜ P 485 +2,370
仓位参考: Max Pain 540 ｜ Call Wall 520（+4.4%）（OI 3.9k）
量化解读： 存量 Put 重｜ATM IV 46.0%｜历史 Rank 89%（近端代理）｜IV/RV 1.54×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 152,463 股

📆 11-06 Forward Structure
存量OI: C 6.2k / P 5.7k，今日变化ΔOI: C +2.3k / P +1.6k，平值价格ATM: C $23.90 / P $17.20 ｜ ATM IV 44.5%，净 delta 敞口 -38k shares
Top ΔOI: C 610 +1,399 ｜ P 455 +945 ｜ C 580 +704
仓位参考: Max Pain 538 ｜ Put Wall 470（-5.6%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 44.5%｜历史 Rank 89%（近端代理）｜IV/RV 1.49×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 37,835 股

11-13（MEDIUM △）Top ΔOI: 485C +36
11-13（MEDIUM △）仓位参考: Max Pain 548 ｜ Put Wall 520（+4.4%，弱）（OI 0.1k）

📅 事件差分（观察，非因果）: 10-23（3D）ATM IV 53.2% vs 10-30 46.0%（差 +7.3pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=59 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=59）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/SOXX_morning.json