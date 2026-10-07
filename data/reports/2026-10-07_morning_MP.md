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
🟡 **近现价集中开仓**: 10-30 44P ΔOI +1,505（距现价 -4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-30 44P ΔOI +1,505 占该期限总 OI 18.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 48.53 → 今开 47.00（-3.2%） | 较昨收变动（含盘初走势） ｜ 今日高 47.01 ｜ 低 46.07

Options: P/C成交量 1.92 | OI比 0.77 | ATM IV 60.3% | Skew -1.0pp | Term 0.97 | ExpMove ±3.6%（近端） | Rank 37%
量化视角： IV 中性（Rank 37%）｜期限结构正常（Term 0.97）｜Put 保护异常便宜（Skew -1.0pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.77）+ 当日成交偏 Put（P/C量 1.92）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.92×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±3.6% ｜ 10-16（9D）±6.6% ｜ 10-23（16D）±7.5% ｜ 10-30（23D）±9.2%
   ⇒ IV–VIX Spread: +44.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,654,421 | GEX Change vs 上次快照 -4,279,021 | Flip: Primary Flip: 47.60（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 284 / LOW 54 / INVALID 98
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 47.60（全链重定价，覆盖 98%）
Put Wall 45（现价高于该位 2.8%） | Call Wall 50（弱结构｜现价低于该位 7.5%）
最近结构参考: Put Wall 45（现价高于该位 2.8%）
量化视角： 负 Gamma（365万，无历史分位）｜由正转负（428万）｜现价位于 Flip 下方 2.86%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 45（Put Wall）；上方 48（MaxPain，仅结算参考） / 50（Call Wall，弱结构）。
• Gamma 区域：切换参考 48（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 44.0P — Vol 1,609 | 最新价 $0.87 | OI 91→1596 (ΔOI +1505张) | ΔOI/Volume 93.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1505张（+1653.8% vs前日OI），连续性待观察（方向未知）
10-09 50.0C — Vol 677 | 最新价 $0.53 | OI 1771→2200 (ΔOI +429张) | ΔOI/Volume 63.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增429张（+24.2% vs前日OI），连续性待观察（方向未知）
10-23 52.0C — Vol 334 | 最新价 $1.02 | OI 113→302 (ΔOI +189张) | ΔOI/Volume 56.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增189张（+167.3% vs前日OI），连续性待观察（方向未知）
10-09 51.0C — Vol 796 | 最新价 $0.32 | OI 743→914 (ΔOI +171张) | ΔOI/Volume 21.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增171张（+23.0% vs前日OI），连续性待观察（方向未知）
10-09 52.0C — Vol 815 | 最新价 $0.17 | OI 721→865 (ΔOI +144张) | ΔOI/Volume 17.7% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增144张（+20.0% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,438 张（Put 1,505 / Call 933），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +0.8k / P -0.1k ｜ Activity MEDIUM △ ｜ 2D
10-16  C +0.7k / P +91 ｜ Activity MEDIUM △ ｜ 9D
10-23  C +0.5k / P +22 ｜ Activity MEDIUM △ ｜ 16D
10-30  C +0.3k / P +1.5k ｜ Activity HIGH ｜ 23D

📆 10-09 Forward Structure
存量OI: C 11.7k / P 9.1k，今日变化ΔOI: C +0.8k / P -0.1k，平值价格ATM: C $0.98 / P $0.69 ｜ ATM IV 60.3%，净 delta 敞口 6k shares
Top ΔOI: C 50 +429
仓位参考: Max Pain 48 ｜ Call Wall 50（+8.1%，弱）（OI 2.2k） ｜ Put Wall 47（+1.6%）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 60.3%｜历史 Rank 37%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,582 股

10-16（MEDIUM △）Top ΔOI: 50C +133 ｜ 48P +113
10-16（MEDIUM △）仓位参考: Max Pain 50 ｜ Call Wall 50（+8.1%，弱）（OI 4.2k） ｜ Put Wall 45（-2.7%，弱）（OI 4.4k）

10-23（MEDIUM △）Top ΔOI: 47C +72
10-23（MEDIUM △）仓位参考: Max Pain 50 ｜ Call Wall 50（+8.1%，弱）（OI 0.2k） ｜ Put Wall 45（-2.7%，弱）（OI 0.2k）

📆 10-30 Forward Structure
存量OI: C 4.7k / P 3.6k，今日变化ΔOI: C +0.3k / P +1.5k，平值价格ATM: C $2.73 / P $1.51 ｜ ATM IV 53.6%，净 delta 敞口 -40k shares
Top ΔOI: P 44 +1,505
仓位参考: Max Pain 48 ｜ Call Wall 50（+8.1%，弱）（OI 0.3k） ｜ Put Wall 44（-4.8%）（OI 1.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 53.6%｜历史 Rank 37%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 负 40,274 股

📅 事件差分（观察，非因果）: 10-09（2D）ATM IV 60.3% vs 10-16 51.1%（差 +9.2pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/MP_morning.json