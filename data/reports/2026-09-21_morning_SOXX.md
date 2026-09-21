# 期权晨报 2026-09-21（快照 10:20 ET）

📊 市场环境

SPY $767.46 ｜ QQQ $734.21
VIX 14.85 ↑0.3%（5D -13.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 32.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-16 525P ΔOI +726（距现价 -4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 533.07 → 今开 545.20（+2.3%） | 较昨收变动（含盘初走势） ｜ 今日高 550.08 ｜ 低 541.47

Options: P/C成交量 0.46 | OI比 1.45 | ATM IV 31.6% | Skew -0.3pp | Term 1.14 | ExpMove ±5.7%（近端） | Rank 43%
量化视角： IV 中性（Rank 43%）｜期限结构正常（Term 1.14）｜Put 保护异常便宜（Skew -0.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.45×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（4D）±5.7% ｜ 10-02（11D）±8.3% ｜ 10-09（18D）±7.7% ｜ 10-16（25D）±8.4%
   ⇒ IV–VIX Spread: +16.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,897,762 | GEX Change vs 上次快照 4,134,705 | Flip: Primary Flip: 541.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 544 / LOW 271 / INVALID 691
结构观察区: Primary Flip 541.77（全链重定价，覆盖 95%）
最近结构参考: Flip 542（现价高于该位 1.3%）
量化视角： 正 Gamma（390万，无历史分位）｜由负转正（+413万）｜现价位于 Flip 上方 1.30%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 520（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 542（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 525.0P — Vol 1,055 | 最新价 $16.50 | OI 568→1294 (ΔOI +726张) | ΔOI/Volume 68.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增726张（+127.8% vs前日OI），连续性待观察（方向未知）
10-16 500.0P — Vol 1,964 | 最新价 $8.40 | OI 4577→5293 (ΔOI +716张) | ΔOI/Volume 36.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增716张（+15.6% vs前日OI），连续性待观察（方向未知）
10-16 435.0P — Vol 885 | 最新价 $1.88 | OI 189→894 (ΔOI +705张) | ΔOI/Volume 79.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增705张（+373.0% vs前日OI），连续性待观察（方向未知）
09-25 520.0P — Vol 426 | 最新价 $3.79 | OI 191→481 (ΔOI +290张) | ΔOI/Volume 68.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增290张（+151.8% vs前日OI），连续性待观察（方向未知）
09-25 490.0P — Vol 531 | 最新价 $0.91 | OI 1430→1683 (ΔOI +253张) | ΔOI/Volume 47.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增253张（+17.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,690 张（Put 2,690 / Call 0），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +0.7k / P +0.9k ｜ Activity MEDIUM △ ｜ 4D
10-02  C +0.3k / P +0.6k ｜ Activity MEDIUM △ ｜ 11D
10-09  C +0.2k / P +83 ｜ Activity MEDIUM △ ｜ 18D
10-16  C -0.6k / P +0.2k ｜ Activity MEDIUM △ ｜ 25D

📆 09-25 Forward Structure
存量OI: C 11.1k / P 16.0k，今日变化ΔOI: C +0.7k / P +0.9k，平值价格ATM: C $5.45 / P $25.64 ｜ ATM IV 31.6%，净 delta 敞口 47k shares
Top ΔOI: P 520 +290
仓位参考: Max Pain 520 ｜ Call Wall 580（+5.7%，弱）（OI 2.0k） ｜ Put Wall 520（-5.2%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜ATM IV 31.6%｜历史 Rank 43%（近端代理）｜IV/RV 0.90×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 47,161 股

10-02（MEDIUM △）Top ΔOI: 500P +153 ｜ 550C +134
10-02（MEDIUM △）仓位参考: Max Pain 515 ｜ Call Wall 542.5（-1.1%，弱）（OI 2.8k）

10-09（MEDIUM △）Top ΔOI: 530C +99 ｜ 525P +38
10-09（MEDIUM △）仓位参考: Max Pain 515 ｜ Call Wall 525（-4.3%）（OI 1.6k）

10-16（MEDIUM △）Top ΔOI: 480P -1,227 ｜ 525P +726
10-16（MEDIUM △）仓位参考: Max Pain 520 ｜ Call Wall 550（+0.2%，弱）（OI 3.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/SOXX_morning.json