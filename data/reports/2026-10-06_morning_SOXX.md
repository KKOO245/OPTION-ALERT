# 期权晨报 2026-10-06（快照 10:20 ET）

📊 市场环境

SPY $779.55 ｜ QQQ $759.66
VIX 15.48 ↓0.3%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.3（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🔵 **期限 OI 集中**: 10-09 555P ΔOI +2,008 占该期限总 OI 14.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 589.51 → 今开 593.54（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 596.39 ｜ 低 590.90

Options: P/C成交量 0.59 | OI比 1.56 | ATM IV 32.0% | Skew 6.6pp | Term 1.15 | ExpMove ±3.4%（近端） | Rank 44%
量化视角： IV 中性（Rank 44%）｜期限结构正常偏陡（Term 1.15）｜保护溢价显著（Skew 6.6pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.59×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.56×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-09（3D）±3.4% ｜ 10-16（10D）±4.8% ｜ 10-23（17D）±5.7% ｜ 10-30（24D）±7.8%
   ⇒ IV–VIX Spread: +16.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,458,330 | GEX Change vs 上次快照 -298,961 | Flip: Primary Flip: 577.37（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 536 / LOW 245 / INVALID 719
结构观察区: Primary Flip 577.37（全链重定价，覆盖 92%）
Call Wall 600（现价低于该位 1.0%）
最近结构参考: Call Wall 600（现价低于该位 1.0%）
量化视角： 正 Gamma（846万，无历史分位）｜正 Gamma 减弱（30万）｜现价位于 Flip 上方 2.90%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 555（MaxPain，仅结算参考）；上方 600（Call Wall）。
• Gamma 区域：切换参考 577（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 520.0P — Vol 2,572 | 最新价 $0.69 | OI 3803→6290 (ΔOI +2487张) | ΔOI/Volume 96.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2487张（+65.4% vs前日OI），连续性待观察（方向未知）
10-16 450.0P — Vol 2,504 | 最新价 $0.07 | OI 5190→7615 (ΔOI +2425张) | ΔOI/Volume 96.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2425张（+46.7% vs前日OI），连续性待观察（方向未知）
10-09 555.0P — Vol 2,017 | 最新价 $0.60 | OI 223→2231 (ΔOI +2008张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2008张（+900.5% vs前日OI），连续性待观察（方向未知）
10-16 587.5P — Vol 198 | 最新价 $15.53 | OI 1→199 (ΔOI +198张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增198张（+19800.0% vs前日OI），连续性待观察（方向未知）
10-30 535.0P — Vol 155 | 最新价 $6.18 | OI 6→161 (ΔOI +155张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增155张（+2583.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,273 张（Put 7,273 / Call 0），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +0.2k / P +2.1k ｜ Activity HIGH ｜ 3D
10-16  C -47 / P +5.1k ｜ Activity MEDIUM △ ｜ 10D
10-23  C +8 / P +67 ｜ Activity MEDIUM △ ｜ 17D
10-30  C +77 / P +0.3k ｜ Activity MEDIUM △ ｜ 24D

📆 10-09 Forward Structure
存量OI: C 5.6k / P 8.7k，今日变化ΔOI: C +0.2k / P +2.1k，平值价格ATM: C $6.50 / P $13.70 ｜ ATM IV 32.0%，净 delta 敞口 271 shares
Top ΔOI: P 555 +2,008 ｜ P 550 -287 ｜ P 570 +131
仓位参考: Max Pain 555 ｜ Put Wall 570（-4.1%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜ATM IV 32.0%｜历史 Rank 44%（近端代理）｜IV/RV 0.93×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 271 股

10-16（MEDIUM △）Top ΔOI: 520P +2,487 ｜ 600C -251
10-16（MEDIUM △）仓位参考: Max Pain 530 ｜ Call Wall 600（+1.0%）（OI 8.9k）

10-23（MEDIUM △）Top ΔOI: 552P +8 ｜ 555C +6
10-23（MEDIUM △）仓位参考: Max Pain 540 ｜ Call Wall 570（-4.1%，弱）（OI 88）

10-30（MEDIUM △）Top ΔOI: 535P +155 ｜ 560P +30
10-30（MEDIUM △）仓位参考: Max Pain 555 ｜ Call Wall 630（+6.0%）（OI 1.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/SOXX_morning.json