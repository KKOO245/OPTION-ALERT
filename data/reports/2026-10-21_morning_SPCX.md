# 期权晨报 2026-10-21（快照 10:20 ET）

📊 市场环境

SPY $772.65 ｜ QQQ $726.24
VIX 17.20 ↓0.6%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 170C ΔOI +5,345（距现价 +2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-28 144P ΔOI +2,981 占该期限总 OI 18.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 147.79 → 今开 160.56（+8.6%） | 较昨收变动（含盘初走势） ｜ 今日高 166.12 ｜ 低 158.20

Options: P/C成交量 0.47 | OI比 1.08 | ATM IV 129.1% | Skew -5.1pp | Term 0.41 | ExpMove ±5.0%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.41，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.08×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（2D）±5.0% ｜ 10-26（5D）±5.6% ｜ 10-28（7D）±6.5% ｜ 10-30（9D）±7.4%
   ⇒ IV–VIX Spread: +111.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 132,413,133 | GEX Change vs 上次快照 132,213,655 | Flip: Primary Flip: 149.97（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 787 / LOW 161 / INVALID 638
结构观察区: Primary Flip 149.97（全链重定价，覆盖 99%）
Call Wall 170（弱结构｜现价低于该位 2.3%）
最近结构参考: Call Wall 170（现价低于该位 2.3%）
量化视角： 正 Gamma（1.32亿，无历史分位）｜正 Gamma 增强（+1.32亿）｜现价位于 Flip 上方 10.71%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 147（MaxPain，仅结算参考）；上方 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 150（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 125.0P — Vol 32,942 | 最新价 $2.09 | OI 13104→39503 (ΔOI +26399张) | ΔOI/Volume 80.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26399张（+201.5% vs前日OI），连续性待观察（方向未知）
10-21 120.0P — Vol 21,259 | 最新价 $0.06 | OI 2620→15154 (ΔOI +12534张) | ΔOI/Volume 59.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12534张（+478.4% vs前日OI），连续性待观察（方向未知）
10-21 160.0C — Vol 23,207 | 最新价 $1.44 | OI 4390→13641 (ΔOI +9251张) | ΔOI/Volume 39.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9251张（+210.7% vs前日OI），连续性待观察（方向未知）
10-21 135.0P — Vol 26,209 | 最新价 $0.95 | OI 4347→12613 (ΔOI +8266张) | ΔOI/Volume 31.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8266张（+190.2% vs前日OI），连续性待观察（方向未知）
10-21 140.0P — Vol 18,538 | 最新价 $2.10 | OI 2198→9788 (ΔOI +7590张) | ΔOI/Volume 40.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7590张（+345.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 64,040 张（Put 54,789 / Call 9,251），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 95.6k / P 103.2k，今日成交量: C 265.1k / P 125.9k，平值价格ATM: C $2.52 / P $2.09 ｜ ATM IV 129.1%，预期波动 ±2.8%，Max Pain 147
Top ΔOI: P 120 +12,534 ｜ C 160 +9,251 ｜ P 135 +8,266

📆 Forward Expiration Structure

10-23  C +35.2k / P +31.2k ｜ Activity HIGH ｜ 2D
10-26  C +6.8k / P +5.0k ｜ Activity HIGH ｜ 5D
10-28  C +1.7k / P +3.1k ｜ Activity HIGH ｜ 7D
10-30  C +10.2k / P +10.3k ｜ Activity HIGH ｜ 9D

📆 10-23 Forward Structure
存量OI: C 188.6k / P 183.7k，今日变化ΔOI: C +35.2k / P +31.2k，平值价格ATM: C $4.40 / P $3.90 ｜ ATM IV 79.5%，净 delta 敞口 1.8M shares
Top ΔOI: C 170 +5,345
仓位参考: Max Pain 149 ｜ Call Wall 170（+2.4%）（OI 26.7k） ｜ Put Wall 150（-9.7%，弱）（OI 5.3k）
量化解读： 存量两侧均衡｜ATM IV 79.5%｜历史 Rank 100%（近端代理）｜IV/RV 1.63×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,766,410 股

📆 10-26 Forward Structure
存量OI: C 16.0k / P 10.6k，今日变化ΔOI: C +6.8k / P +5.0k，平值价格ATM: C $5.00 / P $4.25 ｜ ATM IV 59.4%，净 delta 敞口 408k shares
Top ΔOI: C 155 +1,312 ｜ C 170 +981 ｜ C 175 +714
仓位参考: Max Pain 147 ｜ Call Wall 155（-6.6%，弱）（OI 2.2k） ｜ Put Wall 150（-9.7%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 59.4%｜历史 Rank 100%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 407,940 股

📆 10-28 Forward Structure
存量OI: C 4.4k / P 11.5k，今日变化ΔOI: C +1.7k / P +3.1k，平值价格ATM: C $5.70 / P $5.15 ｜ ATM IV 59.8%，净 delta 敞口 113k shares
Top ΔOI: P 144 +2,981 ｜ C 148 +152
仓位参考: Max Pain 148 ｜ Call Wall 165（-0.6%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜ATM IV 59.8%｜历史 Rank 100%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 113,074 股

📆 10-30 Forward Structure
存量OI: C 141.8k / P 102.7k，今日变化ΔOI: C +10.2k / P +10.3k，平值价格ATM: C $6.45 / P $5.81 ｜ ATM IV 58.9%，净 delta 敞口 795k shares
Top ΔOI: C 190 -5,126 ｜ C 162 +3,956
仓位参考: Max Pain 155 ｜ Call Wall 172.5（+3.9%，弱）（OI 13.6k） ｜ Put Wall 150（-9.7%，弱）（OI 7.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 58.9%｜历史 Rank 100%（近端代理）｜IV/RV 1.21×（近似）｜净 delta 敞口 正 794,765 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/SPCX_morning.json