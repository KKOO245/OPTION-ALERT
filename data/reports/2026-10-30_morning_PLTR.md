# 期权晨报 2026-10-30（快照 10:20 ET）

📊 市场环境

SPY $756.15 ｜ QQQ $690.49
VIX 18.77 ↑9.1%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 196.42 → 今开 193.76（-1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 193.92 ｜ 低 186.33

Options: P/C成交量 0.62 | OI比 1.06 | ATM IV 82.0% | Skew 4.5pp | Term 0.83 | ExpMove ±12.4%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价中性（Skew 4.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.06×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（7D）±12.4% ｜ 11-13（14D）±13.5% ｜ 11-20（21D）±14.6% ｜ 11-27（28D）±14.9%
   ⇒ IV–VIX Spread: +63.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 2,743,686 | GEX Change vs 上次快照 -31,766,922 | Flip: Primary Flip: 188.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 671 / LOW 65 / INVALID 208
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 188.50（全链重定价，覆盖 96%）
Put Wall 180（弱结构｜现价高于该位 5.1%） | Call Wall 200（弱结构｜现价低于该位 5.4%）
最近结构参考: Flip 189（现价高于该位 0.3%）
量化视角： 正 Gamma（274万，无历史分位）｜正 Gamma 减弱（3177万）｜现价位于 Flip 上方 0.34%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（Put Wall，弱结构）；上方 195（MaxPain，仅结算参考） / 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 189（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 410.0C — Vol 4,653 | 最新价 $0.01 | OI 123→4776 (ΔOI +4653张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4653张（+3782.9% vs前日OI），连续性待观察（方向未知）
11-06 202.5C — Vol 4,748 | 最新价 $9.10 | OI 1599→5903 (ΔOI +4304张) | ΔOI/Volume 90.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4304张（+269.2% vs前日OI），连续性待观察（方向未知）
11-06 212.5C — Vol 3,682 | 最新价 $5.80 | OI 1264→4391 (ΔOI +3127张) | ΔOI/Volume 84.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3127张（+247.4% vs前日OI），连续性待观察（方向未知）
11-20 230.0C — Vol 2,757 | 最新价 $3.50 | OI 11494→13210 (ΔOI +1716张) | ΔOI/Volume 62.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1716张（+14.9% vs前日OI），连续性待观察（方向未知）
11-06 200.0C — Vol 4,727 | 最新价 $10.35 | OI 3016→4152 (ΔOI +1136张) | ΔOI/Volume 24.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1136张（+37.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,936 张（Put 0 / Call 14,936），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 120.4k / P 127.8k，今日成交量: C 50.2k / P 31.3k，平值价格ATM: C $1.61 / P $1.76 ｜ ATM IV 82.0%，预期波动 ±1.8%，Max Pain 195
Top ΔOI: C 210 -3,298 ｜ C 202 -2,819 ｜ C 205 -1,512

📆 Forward Expiration Structure

11-06  C +19.1k / P +7.0k ｜ Activity HIGH ｜ 7D
11-13  C +2.1k / P +1.4k ｜ Activity MEDIUM △ ｜ 14D
11-20  C +2.2k / P -1.4k ｜ Activity HIGH ｜ 21D
11-27  C +1.0k / P +0.9k ｜ Activity MEDIUM △ ｜ 28D

📆 11-06 Forward Structure
存量OI: C 76.0k / P 63.8k，今日变化ΔOI: C +19.1k / P +7.0k，平值价格ATM: C $11.74 / P $11.68 ｜ ATM IV 109.3%，净 delta 敞口 217k shares
Top ΔOI: C 202 +4,304 ｜ C 212 +3,127
仓位参考: Max Pain 195 ｜ Call Wall 202.5（+7.1%，弱）（OI 5.9k） ｜ Put Wall 190（+0.4%，弱）（OI 3.9k）
量化解读： 存量 Call 重｜ATM IV 109.3%｜历史 Rank 99%（近端代理）｜IV/RV 2.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 216,616 股

11-13（MEDIUM △）Top ΔOI: 147P +756 ｜ 242C +593
11-13（MEDIUM △）仓位参考: Max Pain 195 ｜ Call Wall 205（+8.4%，弱）（OI 0.9k） ｜ Put Wall 180（-4.8%，弱）（OI 1.9k）

📆 11-20 Forward Structure
存量OI: C 166.0k / P 167.0k，今日变化ΔOI: C +2.2k / P -1.4k，平值价格ATM: C $13.86 / P $13.80 ｜ ATM IV 75.1%，净 delta 敞口 20k shares
Top ΔOI: C 230 +1,716 ｜ P 155 -1,510 ｜ P 160 -591
仓位参考: Max Pain 175 ｜ Call Wall 200（+5.7%，弱）（OI 13.0k） ｜ Put Wall 180（-4.8%，弱）（OI 10.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 75.1%｜历史 Rank 99%（近端代理）｜IV/RV 1.67×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 20,414 股

11-27（MEDIUM △）Top ΔOI: 220C +491 ｜ 190P +220
11-27（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 200（+5.7%，弱）（OI 0.5k） ｜ Put Wall 180（-4.8%，弱）（OI 1.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/PLTR_morning.json