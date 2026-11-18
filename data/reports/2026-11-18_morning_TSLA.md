# 期权晨报 2026-11-18（快照 10:20 ET）

📊 市场环境

SPY $731.20 ｜ QQQ $659.91
VIX 24.58 ↓3.5%（5D +40.5%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 26.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 390C ΔOI +1,046（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 380.11 → 今开 385.19（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 389.27 ｜ 低 379.35

Options: P/C成交量 0.48 | OI比 0.90 | ATM IV 72.5% | Skew 8.7pp | Term 0.44 | ExpMove ±0.0%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.44，近月 IV 高于远月）｜保护溢价显著（Skew 8.7pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（2D）±0.0% ｜ 11-23（5D）±4.9% ｜ 11-25（7D）±6.1% ｜ 11-27（9D）±0.0%
   ⇒ IV–VIX Spread: +47.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 72,281,164 | GEX Change vs 上次快照 43,138,007 | Flip: Primary Flip: 373.12（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1400 / LOW 322 / INVALID 898
结构观察区: Primary Flip 373.12（全链重定价，覆盖 99%）
Call Wall 400（弱结构｜现价低于该位 3.7%）
最近结构参考: Flip 373（现价高于该位 3.3%）
量化视角： 正 Gamma（7228万，无历史分位）｜正 Gamma 增强（+4314万）｜现价位于 Flip 上方 3.27%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 380（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 373（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-18 360.0P — Vol 21,348 | 最新价 $0.73 | OI 1623→4483 (ΔOI +2860张) | ΔOI/Volume 13.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2860张（+176.2% vs前日OI），连续性待观察（方向未知）
11-18 400.0C — Vol 24,878 | 最新价 $0.32 | OI 4080→6714 (ΔOI +2634张) | ΔOI/Volume 10.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2634张（+64.6% vs前日OI），连续性待观察（方向未知）
11-18 385.0C — Vol 26,123 | 最新价 $3.10 | OI 1744→4260 (ΔOI +2516张) | ΔOI/Volume 9.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2516张（+144.3% vs前日OI），连续性待观察（方向未知）
11-20 410.0C — Vol 6,273 | 最新价 $0.78 | OI 20047→22443 (ΔOI +2396张) | ΔOI/Volume 38.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2396张（+11.9% vs前日OI），连续性待观察（方向未知）
11-18 375.0P — Vol 21,949 | 最新价 $3.40 | OI 897→3209 (ΔOI +2312张) | ΔOI/Volume 10.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2312张（+257.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,718 张（Put 5,172 / Call 7,546），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 63.2k / P 57.0k，今日成交量: C 166.6k / P 80.5k，平值价格ATM: C $2.88 / P $3.17 ｜ ATM IV 72.5%，预期波动 ±1.6%，Max Pain 380
Top ΔOI: P 360 +2,860 ｜ C 400 +2,634 ｜ C 385 +2,516

📆 Forward Expiration Structure

11-20  C +9.8k / P +1.7k ｜ Activity HIGH ｜ 2D
11-23  C +2.4k / P +5.1k ｜ Activity HIGH ｜ 5D
11-25  C +1.2k / P +0.8k ｜ Activity HIGH ｜ 7D
11-27  C +3.5k / P +3.2k ｜ Activity HIGH ｜ 9D

📆 11-20 Forward Structure
存量OI: C 363.2k / P 508.2k，今日变化ΔOI: C +9.8k / P +1.7k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 0.0%，净 delta 敞口 201k shares
Top ΔOI: C 410 +2,396 ｜ C 405 +1,607 ｜ C 390 +1,046
仓位参考: Max Pain 375 ｜ Call Wall 400（+3.8%，弱）（OI 26.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜净 delta 敞口 正 200,536 股

📆 11-23 Forward Structure
存量OI: C 24.0k / P 12.0k，今日变化ΔOI: C +2.4k / P +5.1k，平值价格ATM: C $9.40 / P $9.65 ｜ ATM IV 51.6%，净 delta 敞口 -16k shares
Top ΔOI: P 357 +1,190 ｜ P 355 +1,108 ｜ P 377 +619
仓位参考: Max Pain 382 ｜ Put Wall 357.5（-7.2%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 51.6%｜历史 Rank 86%（近端代理）｜IV/RV 0.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 16,204 股

📆 11-25 Forward Structure
存量OI: C 3.8k / P 4.7k，今日变化ΔOI: C +1.2k / P +0.8k，平值价格ATM: C $12.00 / P $11.40 ｜ ATM IV 54.0%，净 delta 敞口 11k shares
Top ΔOI: C 420 +271 ｜ C 400 +208 ｜ P 380 +116
仓位参考: Max Pain 380 ｜ Call Wall 400（+3.8%，弱）（OI 0.4k） ｜ Put Wall 370（-4.0%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 54.0%｜历史 Rank 86%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 10,919 股

📆 11-27 Forward Structure
存量OI: C 62.1k / P 56.8k，今日变化ΔOI: C +3.5k / P +3.2k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 3.9%，净 delta 敞口 73k shares
Top ΔOI: C 382 +393 ｜ C 420 +381
仓位参考: Max Pain 375 ｜ Call Wall 410（+6.4%）（OI 9.1k） ｜ Put Wall 350（-9.2%，弱）（OI 2.7k）
量化解读： 存量两侧均衡｜ATM IV 3.9%｜历史 Rank 86%（近端代理）｜IV/RV 0.07×（近似）｜净 delta 敞口 正 72,697 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/TSLA_morning.json