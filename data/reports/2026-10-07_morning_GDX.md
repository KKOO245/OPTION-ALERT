# 期权晨报 2026-10-07（快照 10:20 ET）

📊 市场环境

SPY $777.04 ｜ QQQ $757.73
VIX 15.79 ↑5.2%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　✅ 今日已公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-16 84P ΔOI +1,537（距现价 -1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-19 80P ΔOI +23 占该期限总 OI 10.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 88.22 → 今开 85.32（-3.3%） | 较昨收变动（含盘初走势） ｜ 今日高 85.70 ｜ 低 84.36

Options: P/C成交量 0.60 | OI比 0.33 | ATM IV 43.7% | Skew -2.3pp | Term 0.91 | ExpMove ±3.0%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构正常（Term 0.91）｜Put 保护异常便宜（Skew -2.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.33）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.33×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±3.0% ｜ 10-16（9D）±4.9% ｜ 10-19（12D）±6.1% ｜ 10-21（14D）±5.8%
   ⇒ IV–VIX Spread: +27.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,980,115 | GEX Change vs 上次快照 -60,124,717 | Flip: Primary Flip: 85.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 436 / LOW 140 / INVALID 392
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 85.36（全链重定价，覆盖 92%）
Put Wall 85（弱结构｜现价高于该位 0.3%） | Call Wall 90（弱结构｜现价低于该位 5.3%）
最近结构参考: Flip 85（现价低于该位 0.1%）
量化视角： 负 Gamma（198万，无历史分位）｜由正转负（6012万）｜现价位于 Flip 下方 0.11%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 85（Put Wall，弱结构）；上方 87（MaxPain，仅结算参考） / 90（Call Wall，弱结构）。
• Gamma 区域：切换参考 85（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 91.0C — Vol 5,108 | 最新价 $2.50 | OI 102→5180 (ΔOI +5078张) | ΔOI/Volume 99.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5078张（+4978.4% vs前日OI），连续性待观察（方向未知）
10-09 91.5C — Vol 4,039 | 最新价 $0.35 | OI 93→4070 (ΔOI +3977张) | ΔOI/Volume 98.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3977张（+4276.3% vs前日OI），连续性待观察（方向未知）
10-16 75.0P — Vol 2,791 | 最新价 $0.03 | OI 10093→12736 (ΔOI +2643张) | ΔOI/Volume 94.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2643张（+26.2% vs前日OI），连续性待观察（方向未知）
10-16 84.0P — Vol 1,884 | 最新价 $0.71 | OI 6000→7537 (ΔOI +1537张) | ΔOI/Volume 81.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1537张（+25.6% vs前日OI），连续性待观察（方向未知）
10-16 94.0C — Vol 1,594 | 最新价 $0.60 | OI 590→1888 (ΔOI +1298张) | ΔOI/Volume 81.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1298张（+220.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,533 张（Put 4,180 / Call 10,353），跨 3 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +5.7k / P +0.9k ｜ Activity HIGH ｜ 2D
10-16  C +3.8k / P +4.6k ｜ Activity MEDIUM △ ｜ 9D
10-19  C +37 / P +83 ｜ Activity MEDIUM △ ｜ 12D
10-21  C +28 / P +13 ｜ Activity MEDIUM △ ｜ 14D

📆 10-09 Forward Structure
存量OI: C 96.8k / P 32.0k，今日变化ΔOI: C +5.7k / P +0.9k，平值价格ATM: C $1.52 / P $1.00 ｜ ATM IV 43.7%，净 delta 敞口 -26k shares
Top ΔOI: C 91 +3,977 ｜ P 85 +351
仓位参考: Max Pain 87 ｜ Call Wall 88（+3.2%，弱）（OI 16.4k） ｜ Put Wall 82（-3.8%，弱）（OI 6.8k）
量化解读： 存量 Call 重｜ATM IV 43.7%｜历史 Rank 68%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 26,382 股

10-16（MEDIUM △）Top ΔOI: 84P +1,537
10-16（MEDIUM △）仓位参考: Max Pain 90 ｜ Call Wall 90（+5.5%，弱）（OI 9.0k） ｜ Put Wall 90（+5.5%，弱）（OI 10.5k）

10-19（MEDIUM △）Top ΔOI: 80P +23 ｜ 90P +22
10-19（MEDIUM △）仓位参考: Max Pain 90 ｜ Call Wall 90（+5.5%，弱）（OI 13） ｜ Put Wall 80（-6.2%，弱）（OI 24）

10-21（MEDIUM △）Top ΔOI: 85P +10 ｜ 90C +10
10-21（MEDIUM △）仓位参考: Max Pain 85 ｜ Call Wall 90（+5.5%，弱）（OI 10） ｜ Put Wall 85（-0.3%）（OI 10）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/GDX_morning.json