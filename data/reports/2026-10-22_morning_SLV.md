# 期权晨报 2026-10-22（快照 10:20 ET）

📊 市场环境

SPY $764.28 ｜ QQQ $704.47
VIX 17.91 ↑7.4%（5D +8.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 19.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-23 52C ΔOI +1,195（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 52.26 → 今开 50.26（-3.8%） | 较昨收变动（含盘初走势） ｜ 今日高 50.33 ｜ 低 49.66

Options: P/C成交量 0.49 | OI比 0.60 | ATM IV 45.8% | Skew 1.6pp | Term 0.81 | ExpMove ±2.1%（近端） | Rank 77%
量化视角： IV 历史高位（Rank 77%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价薄（Skew 1.6pp）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（1D）±2.1% ｜ 10-26（4D）±2.8% ｜ 10-28（6D）±3.9% ｜ 10-30（8D）±4.8%
   ⇒ IV–VIX Spread: +27.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,587,436 | GEX Change vs 上次快照 -46,848,235 | Flip: Primary Flip: 50.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 763 / LOW 122 / INVALID 315
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 50.05（全链重定价，覆盖 97%）
Put Wall 50（弱结构｜现价低于该位 0.2%）
最近结构参考: Put Wall 50（现价低于该位 0.2%）
量化视角： 负 Gamma（359万，无历史分位）｜由正转负（4685万）｜现价位于 Flip 下方 0.31%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 50（Put Wall，弱结构） / 52（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 50（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 105.0C — Vol 2,382 | 最新价 $0.01 | OI 5597→7833 (ΔOI +2236张) | ΔOI/Volume 93.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2236张（+40.0% vs前日OI），连续性待观察（方向未知）
10-23 52.5C — Vol 2,726 | 最新价 $0.43 | OI 1985→3379 (ΔOI +1394张) | ΔOI/Volume 51.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1394张（+70.2% vs前日OI），连续性待观察（方向未知）
10-23 53.0C — Vol 3,956 | 最新价 $0.24 | OI 3418→4729 (ΔOI +1311张) | ΔOI/Volume 33.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1311张（+38.4% vs前日OI），连续性待观察（方向未知）
10-26 48.5P — Vol 1,322 | 最新价 $0.05 | OI 134→1395 (ΔOI +1261张) | ΔOI/Volume 95.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1261张（+941.0% vs前日OI），连续性待观察（方向未知）
10-30 55.5C — Vol 151 | 最新价 $0.18 | OI 1029→2263 (ΔOI +1234张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1234张（+119.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,436 张（Put 1,261 / Call 6,175），跨 4 个期限｜彩票/名义 1 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +5.2k / P -1.4k ｜ Activity HIGH ｜ 1D
10-26  C +2.1k / P +3.0k ｜ Activity HIGH ｜ 4D
10-28  C +2.1k / P +2.4k ｜ Activity HIGH ｜ 6D
10-30  C +3.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 8D

📆 10-23 Forward Structure
存量OI: C 77.0k / P 45.8k，今日变化ΔOI: C +5.2k / P -1.4k，平值价格ATM: C $0.46 / P $0.59 ｜ ATM IV 45.8%，净 delta 敞口 297k shares
Top ΔOI: C 52 +1,394 ｜ C 53 +1,311 ｜ C 52 +1,195
仓位参考: Max Pain 52 ｜ Call Wall 52（+4.2%，弱）（OI 5.7k） ｜ Put Wall 51（+2.2%，弱）（OI 4.4k）
量化解读： 存量 Call 重｜ATM IV 45.8%｜历史 Rank 77%（近端代理）｜IV/RV 1.44×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 297,461 股

📆 10-26 Forward Structure
存量OI: C 7.3k / P 6.9k，今日变化ΔOI: C +2.1k / P +3.0k，平值价格ATM: C $0.64 / P $0.74 ｜ ATM IV 32.6%，净 delta 敞口 -87k shares
Top ΔOI: P 48 +1,261 ｜ P 49 +1,185
仓位参考: Max Pain 50 ｜ Call Wall 50.5（+1.2%）（OI 1.5k） ｜ Put Wall 49（-1.8%，弱）（OI 1.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 32.6%｜历史 Rank 77%（近端代理）｜IV/RV 1.03×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 86,837 股

📆 10-28 Forward Structure
存量OI: C 5.4k / P 5.4k，今日变化ΔOI: C +2.1k / P +2.4k，平值价格ATM: C $0.89 / P $1.03 ｜ ATM IV 37.8%，净 delta 敞口 -57k shares
Top ΔOI: P 48 +645
仓位参考: Max Pain 52 ｜ Call Wall 53（+6.2%，弱）（OI 0.6k） ｜ Put Wall 48（-3.8%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 37.8%｜历史 Rank 77%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 负 57,024 股

10-30（MEDIUM △）Top ΔOI: 50P -545
10-30（MEDIUM △）仓位参考: Max Pain 54 ｜ Call Wall 54（+8.2%，弱）（OI 2.5k） ｜ Put Wall 50（+0.2%，弱）（OI 3.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/SLV_morning.json