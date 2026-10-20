# 期权晨报 2026-10-20（快照 10:20 ET）

📊 市场环境

SPY $769.58 ｜ QQQ $717.63
VIX 18.12 ↓1.7%（5D +18.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 10-23（3D）ATM IV 87.6% vs 10-26 66.8%（差 +20.8pp），覆盖 建筑许可 Prel、新屋开工
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔵 **期限 OI 集中**: 10-26 455C ΔOI +6,026 占该期限总 OI 17.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 368.06 → 今开 370.35（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 374.60 ｜ 低 363.64

Options: P/C成交量 0.58 | OI比 0.90 | ATM IV 87.6% | Skew 2.7pp | Term 0.53 | ExpMove ±6.7%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.53，近月 IV 高于远月）｜保护溢价中性（Skew 2.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（3D）±6.7% ｜ 10-26（6D）±7.0% ｜ 10-28（8D）±7.6% ｜ 10-30（10D）±8.0%
   ⇒ IV–VIX Spread: +69.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 51,426,884 | GEX Change vs 上次快照 11,008,531 | Flip: Primary Flip: 349.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1182 / LOW 64 / INVALID 786
结构观察区: Primary Flip 349.33（全链重定价，覆盖 100%）
Call Wall 400（现价低于该位 7.5%）
最近结构参考: Flip 349（现价高于该位 6.0%）
量化视角： 正 Gamma（5143万，无历史分位）｜正 Gamma 增强（+1101万）｜现价位于 Flip 上方 5.96%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 365（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 349（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 120.0P — Vol 21,600 | 最新价 $0.01 | OI 1041→11840 (ΔOI +10799张) | ΔOI/Volume 50.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10799张（+1037.4% vs前日OI），连续性待观察（方向未知）
10-23 290.0P — Vol 7,374 | 最新价 $0.14 | OI 999→7726 (ΔOI +6727张) | ΔOI/Volume 91.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6727张（+673.4% vs前日OI），连续性待观察（方向未知）
10-26 455.0C — Vol 6,257 | 最新价 $0.30 | OI 728→6754 (ΔOI +6026张) | ΔOI/Volume 96.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6026张（+827.8% vs前日OI），连续性待观察（方向未知）
10-23 405.0C — Vol 8,294 | 最新价 $1.69 | OI 3132→8073 (ΔOI +4941张) | ΔOI/Volume 59.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4941张（+157.8% vs前日OI），连续性待观察（方向未知）
10-23 410.0C — Vol 10,121 | 最新价 $1.28 | OI 3916→8452 (ΔOI +4536张) | ΔOI/Volume 44.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4536张（+115.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 33,029 张（Put 17,526 / Call 15,503），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +46.4k / P +41.5k ｜ Activity HIGH ｜ 3D
10-26  C +11.5k / P +2.3k ｜ Activity HIGH ｜ 6D
10-28  C +1.3k / P +1.5k ｜ Activity HIGH ｜ 8D
10-30  C +5.0k / P +8.3k ｜ Activity HIGH ｜ 10D

📆 10-23 Forward Structure
存量OI: C 210.1k / P 189.5k，今日变化ΔOI: C +46.4k / P +41.5k，平值价格ATM: C $13.45 / P $11.17 ｜ ATM IV 87.6%，净 delta 敞口 548k shares
Top ΔOI: P 290 +6,727 ｜ C 405 +4,941
仓位参考: Max Pain 365 ｜ Call Wall 400（+8.1%，弱）（OI 14.0k）
量化解读： 存量两侧均衡｜ATM IV 87.6%｜历史 Rank 93%（近端代理）｜IV/RV 2.76×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 548,229 股

📆 10-26 Forward Structure
存量OI: C 21.8k / P 12.5k，今日变化ΔOI: C +11.5k / P +2.3k，平值价格ATM: C $14.15 / P $11.80 ｜ ATM IV 66.8%，净 delta 敞口 128k shares
Top ΔOI: C 455 +6,026 ｜ C 400 +565
仓位参考: Max Pain 365 ｜ Call Wall 400（+8.1%，弱）（OI 1.6k） ｜ Put Wall 360（-2.7%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 66.8%｜历史 Rank 93%（近端代理）｜IV/RV 2.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 127,876 股

📆 10-28 Forward Structure
存量OI: C 6.2k / P 6.3k，今日变化ΔOI: C +1.3k / P +1.5k，平值价格ATM: C $15.20 / P $12.95 ｜ ATM IV 62.9%，净 delta 敞口 -777 shares
Top ΔOI: C 400 +252 ｜ P 367 +194
仓位参考: Max Pain 365 ｜ Call Wall 400（+8.1%，弱）（OI 0.8k） ｜ Put Wall 350（-5.4%）（OI 1.4k）
量化解读： 存量两侧均衡｜ATM IV 62.9%｜历史 Rank 93%（近端代理）｜IV/RV 1.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 777 股

📆 10-30 Forward Structure
存量OI: C 73.8k / P 64.9k，今日变化ΔOI: C +5.0k / P +8.3k，平值价格ATM: C $16.16 / P $13.51 ｜ ATM IV 59.4%，净 delta 敞口 29k shares
Top ΔOI: P 270 +2,129
仓位参考: Max Pain 370 ｜ Call Wall 400（+8.1%）（OI 9.5k） ｜ Put Wall 380（+2.7%，弱）（OI 3.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 59.4%｜历史 Rank 93%（近端代理）｜IV/RV 1.87×（近似）｜净 delta 敞口 正 28,694 股

📅 事件差分（观察，非因果）: 10-23（3D）ATM IV 87.6% vs 10-26 66.8%（差 +20.8pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/TSLA_morning.json