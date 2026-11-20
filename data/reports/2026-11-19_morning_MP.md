# 期权晨报 2026-11-19（快照 10:20 ET）

📊 市场环境

SPY $nan ｜ QQQ $nan
VIX 22.66 ↓7.7%（5D +21.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 18.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 37C ΔOI +1,045（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-11 38C ΔOI +370 占该期限总 OI 10.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 35.95 → 今开 36.02（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 37.39 ｜ 低 35.96

Options: P/C成交量 0.34 | OI比 0.37 | ATM IV 100.3% | Skew 14.3pp | Term 0.68 | ExpMove ±4.6%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.68，近月 IV 高于远月）｜保护溢价显著（Skew 14.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.37）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.37×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±4.6% ｜ 11-27（8D）±8.5% ｜ 12-04（15D）±12.8% ｜ 12-11（22D）±14.2%
   ⇒ IV–VIX Spread: +77.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,008,897 | GEX Change vs 上次快照 5,645,561 | Flip: Primary Flip: 34.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 260 / LOW 81 / INVALID 97
结构观察区: Primary Flip 34.92（全链重定价，覆盖 98%）
Put Wall 35（现价高于该位 5.9%）
最近结构参考: Put Wall 35（现价高于该位 5.9%）
量化视角： 正 Gamma（801万，无历史分位）｜正 Gamma 增强（+565万）｜现价位于 Flip 上方 6.17%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall）；上方 38（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 35（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 37.0C — Vol 1,393 | 最新价 $0.53 | OI 721→1766 (ΔOI +1045张) | ΔOI/Volume 75.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1045张（+144.9% vs前日OI），连续性待观察（方向未知）
11-27 50.0C — Vol 1,008 | 最新价 $0.04 | OI 2553→3552 (ΔOI +999张) | ΔOI/Volume 99.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增999张（+39.1% vs前日OI），连续性待观察（方向未知）
12-18 50.0C — Vol 1,217 | 最新价 $0.26 | OI 17224→18187 (ΔOI +963张) | ΔOI/Volume 79.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增963张（+5.6% vs前日OI），连续性待观察（方向未知）
11-27 40.5C — Vol 894 | 最新价 $0.41 | OI 43→790 (ΔOI +747张) | ΔOI/Volume 83.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增747张（+1737.2% vs前日OI），连续性待观察（方向未知）
11-20 40.0C — Vol 578 | 最新价 $0.09 | OI 2250→2667 (ΔOI +417张) | ΔOI/Volume 72.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增417张（+18.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,171 张（Put 0 / Call 4,171），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +2.5k / P -55 ｜ Activity MEDIUM △ ｜ 1D
11-27  C +2.6k / P +0.1k ｜ Activity HIGH ｜ 8D
12-04  C +0.2k / P +61 ｜ Activity MEDIUM △ ｜ 15D
12-11  C +0.5k / P +0.1k ｜ Activity HIGH ｜ 22D

📆 11-20 Forward Structure
存量OI: C 32.9k / P 12.3k，今日变化ΔOI: C +2.5k / P -55，平值价格ATM: C $0.90 / P $0.82 ｜ ATM IV 100.3%，净 delta 敞口 116k shares
Top ΔOI: C 37 +1,045 ｜ C 40 +417 ｜ C 38 +239
仓位参考: Max Pain 38 ｜ Call Wall 40（+7.9%，弱）（OI 2.7k） ｜ Put Wall 35（-5.6%）（OI 3.9k）
量化解读： 存量 Call 重｜ATM IV 100.3%｜历史 Rank 92%（近端代理）｜IV/RV 1.48×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 115,629 股

📆 11-27 Forward Structure
存量OI: C 11.7k / P 4.9k，今日变化ΔOI: C +2.6k / P +0.1k，平值价格ATM: C $1.61 / P $1.54 ｜ ATM IV 69.1%，净 delta 敞口 39k shares
Top ΔOI: C 40 +747
仓位参考: Max Pain 38 ｜ Call Wall 40.5（+9.2%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 69.1%｜历史 Rank 92%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 38,845 股

12-04（MEDIUM △）Top ΔOI: 40C +92
12-04（MEDIUM △）仓位参考: Max Pain 38 ｜ Call Wall 35（-5.6%）（OI 0.5k） ｜ Put Wall 34（-8.3%，弱）（OI 0.2k）

📆 12-11 Forward Structure
存量OI: C 2.6k / P 1.0k，今日变化ΔOI: C +0.5k / P +0.1k，平值价格ATM: C $2.36 / P $2.89 ｜ ATM IV 68.6%，净 delta 敞口 19k shares
Top ΔOI: C 38 +370 ｜ C 36 +116 ｜ P 43 +82
仓位参考: Max Pain 38 ｜ Call Wall 38（+2.5%，弱）（OI 1.0k） ｜ Put Wall 40（+7.9%，弱）（OI 89）
量化解读： 存量 Call 重｜ATM IV 68.6%｜历史 Rank 92%（近端代理）｜IV/RV 1.01×（近似）｜净 delta 敞口 正 18,513 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/MP_morning.json