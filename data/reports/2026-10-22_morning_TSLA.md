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
🟡 **近现价集中开仓**: 10-23 400C ΔOI +3,507（距现价 +3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-26 455C ΔOI +9,699 占该期限总 OI 12.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 386.47 → 今开 374.03（-3.2%） | 较昨收变动（含盘初走势） ｜ 今日高 388.86 ｜ 低 373.71

Options: P/C成交量 0.52 | OI比 0.99 | ATM IV 63.1% | Skew -0.2pp | Term 0.63 | ExpMove ±3.0%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.63，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.99×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（1D）±3.0% ｜ 10-26（4D）±3.6% ｜ 10-28（6D）±4.5% ｜ 10-30（8D）±5.3%
   ⇒ IV–VIX Spread: +45.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 126,521,010 | GEX Change vs 上次快照 17,836,350 | Flip: Primary Flip: 365.48（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1394 / LOW 182 / INVALID 524
结构观察区: Primary Flip 365.48（全链重定价，覆盖 100%）
Call Wall 400（弱结构｜现价低于该位 3.1%）
最近结构参考: Call Wall 400（现价低于该位 3.1%）
量化视角： 正 Gamma（1.27亿，无历史分位）｜正 Gamma 增强（+1784万）｜现价位于 Flip 上方 6.05%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 370（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 365（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-26 455.0C — Vol 10,278 | 最新价 $0.24 | OI 10865→20564 (ΔOI +9699张) | ΔOI/Volume 94.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9699张（+89.3% vs前日OI），连续性待观察（方向未知）
10-30 205.0P — Vol 7,974 | 最新价 $0.04 | OI 30→6656 (ΔOI +6626张) | ΔOI/Volume 83.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6626张（+22086.7% vs前日OI），连续性待观察（方向未知）
10-23 330.0P — Vol 20,061 | 最新价 $0.20 | OI 5418→11122 (ΔOI +5704张) | ΔOI/Volume 28.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5704张（+105.3% vs前日OI），连续性待观察（方向未知）
10-23 420.0C — Vol 22,839 | 最新价 $1.58 | OI 11330→16073 (ΔOI +4743张) | ΔOI/Volume 20.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4743张（+41.9% vs前日OI），连续性待观察（方向未知）
10-30 190.0P — Vol 6,377 | 最新价 $0.03 | OI 1772→6102 (ΔOI +4330张) | ΔOI/Volume 67.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4330张（+244.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 31,102 张（Put 16,660 / Call 14,442），跨 3 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +36.3k / P +44.3k ｜ Activity HIGH ｜ 1D
10-26  C +15.6k / P +11.0k ｜ Activity HIGH ｜ 4D
10-28  C +1.7k / P +2.6k ｜ Activity HIGH ｜ 6D
10-30  C +4.1k / P +20.6k ｜ Activity HIGH ｜ 8D

📆 10-23 Forward Structure
存量OI: C 273.3k / P 270.0k，今日变化ΔOI: C +36.3k / P +44.3k，平值价格ATM: C $5.50 / P $6.05 ｜ ATM IV 63.1%，净 delta 敞口 -179k shares
Top ΔOI: C 420 +4,743 ｜ C 400 +3,507
仓位参考: Max Pain 370 ｜ Call Wall 400（+3.2%，弱）（OI 19.6k） ｜ Put Wall 350（-9.7%，弱）（OI 8.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 63.1%｜历史 Rank 76%（近端代理）｜IV/RV 2.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 178,940 股

📆 10-26 Forward Structure
存量OI: C 50.0k / P 29.6k，今日变化ΔOI: C +15.6k / P +11.0k，平值价格ATM: C $6.80 / P $7.34 ｜ ATM IV 42.6%，净 delta 敞口 -71k shares
Top ΔOI: C 455 +9,699 ｜ P 365 +1,548
仓位参考: Max Pain 375 ｜ Put Wall 350（-9.7%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 42.6%｜历史 Rank 76%（近端代理）｜IV/RV 1.40×（近似）｜净 delta 敞口 负 70,602 股

📆 10-28 Forward Structure
存量OI: C 9.4k / P 10.7k，今日变化ΔOI: C +1.7k / P +2.6k，平值价格ATM: C $8.35 / P $9.03 ｜ ATM IV 43.8%，净 delta 敞口 -8k shares
Top ΔOI: P 355 +482 ｜ C 410 +331 ｜ P 380 +231
仓位参考: Max Pain 370 ｜ Call Wall 420（+8.4%，弱）（OI 1.1k） ｜ Put Wall 350（-9.7%）（OI 1.6k）
量化解读： 存量两侧均衡｜ATM IV 43.8%｜历史 Rank 76%（近端代理）｜IV/RV 1.44×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 7,685 股

📆 10-30 Forward Structure
存量OI: C 82.7k / P 95.7k，今日变化ΔOI: C +4.1k / P +20.6k，平值价格ATM: C $10.02 / P $10.41 ｜ ATM IV 43.6%，净 delta 敞口 -81k shares
仓位参考: Max Pain 370 ｜ Call Wall 400（+3.2%）（OI 9.2k） ｜ Put Wall 380（-2.0%，弱）（OI 4.0k）
量化解读： 存量两侧均衡｜ATM IV 43.6%｜历史 Rank 76%（近端代理）｜IV/RV 1.43×（近似）｜净 delta 敞口 负 81,297 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/TSLA_morning.json