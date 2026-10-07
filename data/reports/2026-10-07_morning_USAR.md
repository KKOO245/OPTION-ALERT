# 期权晨报 2026-10-07（快照 10:20 ET）

📊 市场环境

SPY $774.46 ｜ QQQ $754.66
VIX 15.79 ↑5.2%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　⏰ 今日
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 13P ΔOI +202（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 13.74 → 今开 13.35（-2.8%） | 较昨收变动（含盘初走势） ｜ 今日高 13.39 ｜ 低 13.06

Options: P/C成交量 0.19 | OI比 0.40 | ATM IV 67.2% | Skew -7.9pp | Term 1.07 | ExpMove ±7.0%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常（Term 1.07）｜Put 保护异常便宜（Skew -7.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.40）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.19×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.40×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±7.0% ｜ 10-16（9D）±11.6% ｜ 10-23（16D）±12.3% ｜ 10-30（23D）±14.1%
   ⇒ IV–VIX Spread: +51.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,741,404 | GEX Change vs 上次快照 -2,303,449 | Flip: Primary Flip: 13.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 183 / LOW 68 / INVALID 139
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 13.77（全链重定价，覆盖 100%）
最近结构参考: Flip 14（现价低于该位 4.4%）
量化视角： 负 Gamma（274万，无历史分位）｜负 Gamma 加深（230万）｜现价位于 Flip 下方 4.43%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 14（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 15.0C — Vol 984 | 最新价 $0.05 | OI 2022→2589 (ΔOI +567张) | ΔOI/Volume 57.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增567张（+28.0% vs前日OI），连续性待观察（方向未知）
10-09 14.5C — Vol 1,029 | 最新价 $0.13 | OI 2836→3326 (ΔOI +490张) | ΔOI/Volume 47.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增490张（+17.3% vs前日OI），连续性待观察（方向未知）
10-16 14.0C — Vol 714 | 最新价 $0.48 | OI 515→998 (ΔOI +483张) | ΔOI/Volume 67.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增483张（+93.8% vs前日OI），连续性待观察（方向未知）
10-30 13.0P — Vol 420 | 最新价 $0.51 | OI 626→1023 (ΔOI +397张) | ΔOI/Volume 94.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增397张（+63.4% vs前日OI），连续性待观察（方向未知）
10-30 16.5C — Vol 450 | 最新价 $0.21 | OI 886→1239 (ΔOI +353张) | ΔOI/Volume 78.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增353张（+39.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,290 张（Put 397 / Call 1,893），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +1.1k / P -2 ｜ Activity HIGH ｜ 2D
10-16  C +1.0k / P +0.2k ｜ Activity HIGH ｜ 9D
10-23  C +0.3k / P +0.4k ｜ Activity HIGH ｜ 16D
10-30  C +0.8k / P +0.9k ｜ Activity HIGH ｜ 23D

📆 10-09 Forward Structure
存量OI: C 19.0k / P 7.5k，今日变化ΔOI: C +1.1k / P -2，平值价格ATM: C $0.85 / P $0.07 ｜ ATM IV 67.2%，净 delta 敞口 27k shares
Top ΔOI: P 13 +202
仓位参考: Max Pain 14 ｜ Call Wall 14（+6.4%，弱）（OI 1.9k） ｜ Put Wall 13（-1.2%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 67.2%｜历史 Rank 3%（近端代理）｜IV/RV 1.33×（近似）｜净 delta 敞口 正 27,244 股

📆 10-16 Forward Structure
存量OI: C 49.6k / P 16.4k，今日变化ΔOI: C +1.0k / P +0.2k，平值价格ATM: C $1.27 / P $0.25 ｜ ATM IV 65.1%，净 delta 敞口 28k shares
Top ΔOI: C 14 +483
仓位参考: Max Pain 16 ｜ Put Wall 14（+6.4%，弱）（OI 2.0k）
量化解读： 存量 Call 重｜ATM IV 65.1%｜历史 Rank 3%（近端代理）｜IV/RV 1.29×（近似）｜净 delta 敞口 正 28,349 股

📆 10-23 Forward Structure
存量OI: C 10.9k / P 5.8k，今日变化ΔOI: C +0.3k / P +0.4k，平值价格ATM: C $1.27 / P $0.35 ｜ ATM IV 72.1%，净 delta 敞口 -4k shares
Top ΔOI: P 12 +141 ｜ P 12 +110
仓位参考: Max Pain 16 ｜ Put Wall 14（+6.4%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 72.1%｜历史 Rank 3%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 4,084 股

📆 10-30 Forward Structure
存量OI: C 6.4k / P 8.1k，今日变化ΔOI: C +0.8k / P +0.9k，平值价格ATM: C $1.35 / P $0.51 ｜ ATM IV 68.0%，净 delta 敞口 -17k shares
Top ΔOI: P 13 +397 ｜ P 12 +323
仓位参考: Max Pain 16 ｜ Call Wall 14（+6.4%，弱）（OI 0.3k） ｜ Put Wall 14（+6.4%）（OI 2.5k）
量化解读： 存量 Put 重｜ATM IV 68.0%｜历史 Rank 3%（近端代理）｜IV/RV 1.35×（近似）｜净 delta 敞口 负 17,468 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/USAR_morning.json