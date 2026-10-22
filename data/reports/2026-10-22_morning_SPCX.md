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
🟡 **近现价集中开仓**: 10-23 155P ΔOI +17,588（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-28 160P ΔOI +6,310 占该期限总 OI 20.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 159.31 → 今开 154.19（-3.2%） | 较昨收变动（含盘初走势） ｜ 今日高 154.22 ｜ 低 150.86

Options: P/C成交量 0.80 | OI比 1.08 | ATM IV 67.8% | Skew 0.1pp | Term 0.75 | ExpMove ±3.2%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜保护溢价薄（Skew 0.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.08×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（1D）±3.2% ｜ 10-26（4D）±4.3% ｜ 10-28（6D）±5.3% ｜ 10-30（8D）±6.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -31,404,584 | GEX Change vs 上次快照 -116,195,192 | Flip: Primary Flip: 155.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 922 / LOW 136 / INVALID 394
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 155.38（全链重定价，覆盖 99%）
Put Wall 140（弱结构｜现价高于该位 8.9%）
最近结构参考: Flip 155（现价低于该位 1.9%）
量化视角： 负 Gamma（3140万，无历史分位）｜由正转负（1.16亿）｜现价位于 Flip 下方 1.87%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（Put Wall，弱结构）；上方 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 155（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 155.0P — Vol 79,886 | 最新价 $1.61 | OI 4913→22501 (ΔOI +17588张) | ΔOI/Volume 22.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17588张（+358.0% vs前日OI），连续性待观察（方向未知）
10-23 160.0P — Vol 65,104 | 最新价 $3.70 | OI 3201→11261 (ΔOI +8060张) | ΔOI/Volume 12.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8060张（+251.8% vs前日OI），连续性待观察（方向未知）
10-23 150.0P — Vol 46,305 | 最新价 $0.59 | OI 5266→12843 (ΔOI +7577张) | ΔOI/Volume 16.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7577张（+143.9% vs前日OI），连续性待观察（方向未知）
10-30 170.0C — Vol 23,967 | 最新价 $1.89 | OI 5679→12325 (ΔOI +6646张) | ΔOI/Volume 27.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6646张（+117.0% vs前日OI），连续性待观察（方向未知）
10-23 165.0C — Vol 79,118 | 最新价 $1.30 | OI 14020→20665 (ΔOI +6645张) | ΔOI/Volume 8.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6645张（+47.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 46,516 张（Put 33,225 / Call 13,291），跨 2 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $6M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +23.2k / P +45.0k ｜ Activity HIGH ｜ 1D
10-26  C +8.8k / P +15.8k ｜ Activity HIGH ｜ 4D
10-28  C +5.2k / P +9.6k ｜ Activity HIGH ｜ 6D
10-30  C +9.6k / P +26.1k ｜ Activity HIGH ｜ 8D

📆 10-23 Forward Structure
存量OI: C 211.8k / P 228.7k，今日变化ΔOI: C +23.2k / P +45.0k，平值价格ATM: C $2.55 / P $2.32 ｜ ATM IV 67.8%，净 delta 敞口 -3.2M shares
Top ΔOI: P 155 +17,588 ｜ P 160 +8,060 ｜ P 150 +7,577
仓位参考: Max Pain 155 ｜ Call Wall 165（+8.2%，弱）（OI 20.7k） ｜ Put Wall 155（+1.7%，弱）（OI 22.5k）
量化解读： 存量两侧均衡｜ATM IV 67.8%｜历史 Rank 85%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,189,085 股

📆 10-26 Forward Structure
存量OI: C 24.8k / P 26.4k，今日变化ΔOI: C +8.8k / P +15.8k，平值价格ATM: C $3.40 / P $3.10 ｜ ATM IV 48.2%，净 delta 敞口 -1.0M shares
Top ΔOI: P 160 +5,025 ｜ P 155 +2,374 ｜ P 165 +2,209
仓位参考: Max Pain 160 ｜ Call Wall 155（+1.7%，弱）（OI 2.1k） ｜ Put Wall 160（+4.9%）（OI 5.2k）
量化解读： 存量两侧均衡｜ATM IV 48.2%｜历史 Rank 85%（近端代理）｜IV/RV 0.87×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,030,858 股

📆 10-28 Forward Structure
存量OI: C 9.6k / P 21.1k，今日变化ΔOI: C +5.2k / P +9.6k，平值价格ATM: C $4.15 / P $3.95 ｜ ATM IV 50.7%，净 delta 敞口 -607k shares
Top ΔOI: P 160 +6,310 ｜ P 155 +1,317
仓位参考: Max Pain 160 ｜ Call Wall 160（+4.9%，弱）（OI 0.9k） ｜ Put Wall 160（+4.9%，弱）（OI 6.4k）
量化解读： 存量 Put 重｜ATM IV 50.7%｜历史 Rank 85%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 负 607,377 股

📆 10-30 Forward Structure
存量OI: C 151.5k / P 128.8k，今日变化ΔOI: C +9.6k / P +26.1k，平值价格ATM: C $5.05 / P $4.75 ｜ ATM IV 52.7%，净 delta 敞口 -1.0M shares
Top ΔOI: C 170 +6,646 ｜ P 155 +6,131 ｜ P 150 +6,011
仓位参考: Max Pain 158 ｜ Call Wall 165（+8.2%，弱）（OI 9.8k） ｜ Put Wall 150（-1.6%，弱）（OI 13.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 52.7%｜历史 Rank 85%（近端代理）｜IV/RV 0.95×（近似）｜净 delta 敞口 负 1,012,644 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/SPCX_morning.json