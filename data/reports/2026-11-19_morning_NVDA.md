# 期权晨报 2026-11-19（快照 10:20 ET）

📊 市场环境

SPY $735.18 ｜ QQQ $663.53
VIX 22.66 ↓7.7%（5D +21.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-23 160C ΔOI +5,803（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 150.96 → 今开 152.92（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 158.13 ｜ 低 152.55

Options: P/C成交量 0.49 | OI比 0.55 | ATM IV 68.8% | Skew 1.8pp | Term 0.71 | ExpMove ±0.7%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜保护溢价薄（Skew 1.8pp）｜存量 Call 偏重（OI比 0.55）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.55×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±0.7% ｜ 11-23（4D）±4.6% ｜ 11-25（6D）±5.8% ｜ 11-27（8D）±0.0%
   ⇒ IV–VIX Spread: +46.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 36,923,078 | GEX Change vs 上次快照 165,436,335 | Flip: Primary Flip: 154.62（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 962 / LOW 305 / INVALID 689
结构观察区: Primary Flip 154.62（全链重定价，覆盖 100%）
Put Wall 160（弱结构｜现价低于该位 2.5%）
最近结构参考: Flip 155（现价高于该位 0.9%）
量化视角： 正 Gamma（3692万，无历史分位）｜由负转正（+1.65亿）｜现价位于 Flip 上方 0.88%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 160（Put Wall，弱结构） / 170（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 155（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 205.0C — Vol 46,670 | 最新价 $0.31 | OI 16959→53682 (ΔOI +36723张) | ΔOI/Volume 78.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增36723张（+216.5% vs前日OI），连续性待观察（方向未知）
12-18 170.0C — Vol 70,065 | 最新价 $2.58 | OI 66019→100929 (ΔOI +34910张) | ΔOI/Volume 49.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增34910张（+52.9% vs前日OI），连续性待观察（方向未知）
11-20 160.0C — Vol 124,539 | 最新价 $0.62 | OI 27594→48831 (ΔOI +21237张) | ΔOI/Volume 17.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21237张（+77.0% vs前日OI），连续性待观察（方向未知）
11-27 165.0C — Vol 32,129 | 最新价 $1.00 | OI 5343→24223 (ΔOI +18880张) | ΔOI/Volume 58.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18880张（+353.4% vs前日OI），连续性待观察（方向未知）
11-27 157.5C — Vol 19,938 | 最新价 $2.47 | OI 1524→17684 (ΔOI +16160张) | ΔOI/Volume 81.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16160张（+1060.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 127,910 张（Put 0 / Call 127,910），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +26.9k / P -126.7k ｜ Activity HIGH ｜ 1D
11-23  C +18.6k / P +7.7k ｜ Activity HIGH ｜ 4D
11-25  C +12.0k / P +7.5k ｜ Activity HIGH ｜ 6D
11-27  C +71.5k / P +9.9k ｜ Activity HIGH ｜ 8D

📆 11-20 Forward Structure
存量OI: C 1599.0k / P 885.4k，今日变化ΔOI: C +26.9k / P -126.7k，平值价格ATM: C $0.63 / P $0.40 ｜ ATM IV 66.1%，净 delta 敞口 19.1M shares
Top ΔOI: P 200 -31,483 ｜ P 190 -30,800
仓位参考: Max Pain 170 ｜ Call Wall 170（+9.0%，弱）（OI 61.5k） ｜ Put Wall 150（-3.8%，弱）（OI 47.6k）
量化解读： 存量 Call 重｜ATM IV 66.1%｜历史 Rank 88%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 19,063,770 股

📆 11-23 Forward Structure
存量OI: C 73.8k / P 42.3k，今日变化ΔOI: C +18.6k / P +7.7k，平值价格ATM: C $4.30 / P $2.88 ｜ ATM IV 52.9%，净 delta 敞口 521k shares
Top ΔOI: C 160 +5,803 ｜ C 170 +2,583 ｜ C 155 +2,390
仓位参考: Max Pain 155 ｜ Call Wall 160（+2.6%）（OI 10.1k） ｜ Put Wall 150（-3.8%，弱）（OI 6.1k）
量化解读： 存量 Call 重｜ATM IV 52.9%｜历史 Rank 88%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 521,076 股

📆 11-25 Forward Structure
存量OI: C 43.7k / P 19.8k，今日变化ΔOI: C +12.0k / P +7.5k，平值价格ATM: C $5.17 / P $3.90 ｜ ATM IV 55.4%，净 delta 敞口 221k shares
Top ΔOI: C 165 +2,451 ｜ C 160 +1,513
仓位参考: Max Pain 155 ｜ Call Wall 165（+5.8%）（OI 5.1k） ｜ Put Wall 150（-3.8%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 55.4%｜历史 Rank 88%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 221,138 股

📆 11-27 Forward Structure
存量OI: C 296.8k / P 173.7k，今日变化ΔOI: C +71.5k / P +9.9k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 38.8%，净 delta 敞口 3.2M shares
Top ΔOI: C 165 +18,880 ｜ C 157 +16,160
仓位参考: Max Pain 165 ｜ Call Wall 165（+5.8%，弱）（OI 24.3k） ｜ Put Wall 165（+5.8%，弱）（OI 15.7k）
量化解读： 存量 Call 重｜ATM IV 38.8%｜历史 Rank 88%（近端代理）｜IV/RV 0.78×（近似）｜净 delta 敞口 正 3,160,988 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/NVDA_morning.json