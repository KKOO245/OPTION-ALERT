# 期权晨报 2026-10-16（快照 10:20 ET）

📊 市场环境

SPY $771.01 ｜ QQQ $716.46
VIX 15.93 ↓3.2%（5D +7.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔵 **期限 OI 集中**: 10-28 420C ΔOI +664 占该期限总 OI 11.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 362.44 → 今开 369.04（+1.8%） | 较昨收变动（含盘初走势） ｜ 今日高 370.58 ｜ 低 363.37

Options: P/C成交量 0.40 | OI比 0.91 | ATM IV 72.4% | Skew -2.3pp | Term 0.64 | ExpMove ±2.6%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.64，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.40×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.91×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-19（3D）±2.6% ｜ 10-23（7D）±7.4% ｜ 10-26（10D）±7.6% ｜ 10-28（12D）±8.4%
   ⇒ IV–VIX Spread: +56.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 52,845,842 | GEX Change vs 上次快照 45,859,882 | Flip: Primary Flip: 360.26（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 1055 / LOW 140 / INVALID 663
结构观察区: Primary Flip 360.26（全链重定价，覆盖 96%）
Call Wall 400（现价低于该位 8.2%）
最近结构参考: Flip 360（现价高于该位 2.0%）
量化视角： 正 Gamma（5285万，无历史分位）｜正 Gamma 增强（+4586万）｜现价位于 Flip 上方 1.96%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 370（MaxPain，仅结算参考） / 400（Call Wall）。
• Gamma 区域：切换参考 360（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-19 430.0C — Vol 6,705 | 最新价 $0.20 | OI 553→6462 (ΔOI +5909张) | ΔOI/Volume 88.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5909张（+1068.5% vs前日OI），连续性待观察（方向未知）
10-19 410.0C — Vol 7,140 | 最新价 $0.25 | OI 853→6563 (ΔOI +5710张) | ΔOI/Volume 80.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5710张（+669.4% vs前日OI），连续性待观察（方向未知）
10-16 440.0C — Vol 7,699 | 最新价 $0.08 | OI 7228→12256 (ΔOI +5028张) | ΔOI/Volume 65.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5028张（+69.6% vs前日OI），连续性待观察（方向未知）
10-16 375.0C — Vol 34,013 | 最新价 $1.43 | OI 8242→12838 (ΔOI +4596张) | ΔOI/Volume 13.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4596张（+55.8% vs前日OI），连续性待观察（方向未知）
10-16 377.5C — Vol 20,367 | 最新价 $1.09 | OI 6089→10270 (ΔOI +4181张) | ΔOI/Volume 20.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4181张（+68.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 25,424 张（Put 0 / Call 25,424），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 466.2k / P 423.9k，今日成交量: C 403.2k / P 161.6k，平值价格ATM: C $3.38 / P $2.42 ｜ ATM IV 72.4%，预期波动 ±1.6%，Max Pain 370
Top ΔOI: C 440 +5,028 ｜ C 375 +4,596 ｜ C 377 +4,181

📆 Forward Expiration Structure

10-19  C +34.4k / P +10.4k ｜ Activity HIGH ｜ 3D
10-23  C +13.8k / P +11.9k ｜ Activity HIGH ｜ 7D
10-26  C +2.2k / P +2.7k ｜ Activity HIGH ｜ 10D
10-28  C +1.9k / P +0.4k ｜ Activity HIGH ｜ 12D

📆 10-19 Forward Structure
存量OI: C 73.3k / P 35.8k，今日变化ΔOI: C +34.4k / P +10.4k，平值价格ATM: C $5.20 / P $4.28 ｜ ATM IV 34.1%，净 delta 敞口 539k shares
Top ΔOI: C 410 +5,710 ｜ C 390 +2,331
仓位参考: Max Pain 365 ｜ Call Wall 400（+8.9%，弱）（OI 6.3k） ｜ Put Wall 360（-2.0%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 34.1%｜历史 Rank 87%（近端代理）｜IV/RV 1.21×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 539,129 股

📆 10-23 Forward Structure
存量OI: C 98.2k / P 67.4k，今日变化ΔOI: C +13.8k / P +11.9k，平值价格ATM: C $14.00 / P $13.30 ｜ ATM IV 64.6%，净 delta 敞口 77k shares
Top ΔOI: C 452 +1,151 ｜ C 400 +1,142
仓位参考: Max Pain 370 ｜ Call Wall 400（+8.9%，弱）（OI 7.3k） ｜ Put Wall 350（-4.7%，弱）（OI 3.6k）
量化解读： 存量 Call 重｜ATM IV 64.6%｜历史 Rank 87%（近端代理）｜IV/RV 2.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 76,940 股

📆 10-26 Forward Structure
存量OI: C 5.0k / P 6.6k，今日变化ΔOI: C +2.2k / P +2.7k，平值价格ATM: C $14.32 / P $13.75 ｜ ATM IV 56.5%，净 delta 敞口 13k shares
Top ΔOI: P 347 +819 ｜ P 335 +467 ｜ C 400 +411
仓位参考: Max Pain 368 ｜ Call Wall 400（+8.9%，弱）（OI 0.5k） ｜ Put Wall 347.5（-5.4%，弱）（OI 0.8k）
量化解读： 存量 Put 重｜ATM IV 56.5%｜历史 Rank 87%（近端代理）｜IV/RV 2.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 13,071 股

📆 10-28 Forward Structure
存量OI: C 3.4k / P 2.3k，今日变化ΔOI: C +1.9k / P +0.4k，平值价格ATM: C $15.25 / P $15.45 ｜ ATM IV 54.8%，净 delta 敞口 36k shares
Top ΔOI: C 420 +664 ｜ C 400 +334
仓位参考: Max Pain 365 ｜ Call Wall 400（+8.9%，弱）（OI 0.4k） ｜ Put Wall 375（+2.1%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 54.8%｜历史 Rank 87%（近端代理）｜IV/RV 1.95×（近似）｜净 delta 敞口 正 36,024 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/TSLA_morning.json