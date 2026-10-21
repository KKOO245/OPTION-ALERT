# 期权晨报 2026-10-21（快照 10:20 ET）

📊 市场环境

SPY $769.11 ｜ QQQ $721.54
VIX 17.20 ↓0.6%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 373.71 → 今开 381.51（+2.1%） | 较昨收变动（含盘初走势） ｜ 今日高 388.84 ｜ 低 380.51

Options: P/C成交量 0.44 | OI比 0.95 | ATM IV 96.6% | Skew 2.8pp | Term 0.47 | ExpMove ±6.1%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.47，近月 IV 高于远月）｜保护溢价中性（Skew 2.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.95×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（2D）±6.1% ｜ 10-26（5D）±6.5% ｜ 10-28（7D）±7.0% ｜ 10-30（9D）±7.5%
   ⇒ IV–VIX Spread: +79.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 93,281,334 | GEX Change vs 上次快照 30,384,631 | Flip: Primary Flip: 353.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1416 / LOW 100 / INVALID 574
结构观察区: Primary Flip 353.50（全链重定价，覆盖 100%）
Call Wall 400（现价低于该位 3.5%）
最近结构参考: Call Wall 400（现价低于该位 3.5%）
量化视角： 正 Gamma（9328万，无历史分位）｜正 Gamma 增强（+3038万）｜现价位于 Flip 上方 9.21%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 365（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 354（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 190.0P — Vol 7,442 | 最新价 $0.02 | OI 855→8028 (ΔOI +7173张) | ΔOI/Volume 96.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7173张（+839.0% vs前日OI），连续性待观察（方向未知）
10-23 410.0C — Vol 19,744 | 最新价 $2.04 | OI 8452→13480 (ΔOI +5028张) | ΔOI/Volume 25.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5028张（+59.5% vs前日OI），连续性待观察（方向未知）
10-26 455.0C — Vol 5,767 | 最新价 $0.27 | OI 6754→10865 (ΔOI +4111张) | ΔOI/Volume 71.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4111张（+60.9% vs前日OI），连续性待观察（方向未知）
10-23 180.0P — Vol 3,954 | 最新价 $0.01 | OI 12050→15962 (ΔOI +3912张) | ΔOI/Volume 98.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3912张（+32.5% vs前日OI），连续性待观察（方向未知）
10-23 200.0P — Vol 3,635 | 最新价 $0.01 | OI 401→3828 (ΔOI +3427张) | ΔOI/Volume 94.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3427张（+854.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 23,651 张（Put 14,512 / Call 9,139），跨 2 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +26.9k / P +36.2k ｜ Activity HIGH ｜ 2D
10-26  C +12.7k / P +6.1k ｜ Activity HIGH ｜ 5D
10-28  C +1.4k / P +1.7k ｜ Activity HIGH ｜ 7D
10-30  C +4.7k / P +10.1k ｜ Activity HIGH ｜ 9D

📆 10-23 Forward Structure
存量OI: C 237.0k / P 225.7k，今日变化ΔOI: C +26.9k / P +36.2k，平值价格ATM: C $12.25 / P $11.20 ｜ ATM IV 96.6%，净 delta 敞口 427k shares
Top ΔOI: C 410 +5,028
仓位参考: Max Pain 365 ｜ Call Wall 400（+3.6%，弱）（OI 16.1k） ｜ Put Wall 350（-9.3%，弱）（OI 6.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 96.6%｜历史 Rank 95%（近端代理）｜IV/RV 3.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 427,100 股

📆 10-26 Forward Structure
存量OI: C 34.4k / P 18.6k，今日变化ΔOI: C +12.7k / P +6.1k，平值价格ATM: C $13.15 / P $11.95 ｜ ATM IV 67.5%，净 delta 敞口 150k shares
Top ΔOI: C 455 +4,111 ｜ P 350 +1,340 ｜ P 330 +1,214
仓位参考: Max Pain 368 ｜ Put Wall 350（-9.3%）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 67.5%｜历史 Rank 95%（近端代理）｜IV/RV 2.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 150,152 股

📆 10-28 Forward Structure
存量OI: C 7.6k / P 8.0k，今日变化ΔOI: C +1.4k / P +1.7k，平值价格ATM: C $14.30 / P $12.71 ｜ ATM IV 62.5%，净 delta 敞口 36k shares
Top ΔOI: P 350 +157
仓位参考: Max Pain 368 ｜ Call Wall 420（+8.8%，弱）（OI 1.1k） ｜ Put Wall 350（-9.3%）（OI 1.6k）
量化解读： 存量两侧均衡｜ATM IV 62.5%｜历史 Rank 95%（近端代理）｜IV/RV 2.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 36,216 股

📆 10-30 Forward Structure
存量OI: C 78.6k / P 75.1k，今日变化ΔOI: C +4.7k / P +10.1k，平值价格ATM: C $15.27 / P $13.80 ｜ ATM IV 58.6%，净 delta 敞口 119k shares
Top ΔOI: C 420 +1,564
仓位参考: Max Pain 370 ｜ Call Wall 400（+3.6%）（OI 9.7k） ｜ Put Wall 350（-9.3%，弱）（OI 3.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 58.6%｜历史 Rank 95%（近端代理）｜IV/RV 2.06×（近似）｜净 delta 敞口 正 118,661 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/TSLA_morning.json