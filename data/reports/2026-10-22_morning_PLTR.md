# 期权晨报 2026-10-22（快照 10:20 ET）

📊 市场环境

SPY $766.63 ｜ QQQ $711.01
VIX 17.91 ↑7.4%（5D +8.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 195P ΔOI +2,011（距现价 -3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 201.72 → 今开 200.98（-0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 202.63 ｜ 低 199.95

Options: P/C成交量 0.56 | OI比 1.01 | ATM IV 57.0% | Skew 5.1pp | Term 1.10 | ExpMove ±2.7%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构正常（Term 1.10）｜保护溢价中性（Skew 5.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.01×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（1D）±2.7% ｜ 10-30（8D）±5.9% ｜ 11-06（15D）±12.3% ｜ 11-13（22D）±13.2%
   ⇒ IV–VIX Spread: +39.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 76,762,649 | GEX Change vs 上次快照 -3,520,846 | Flip: Primary Flip: 189.08（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 636 / LOW 87 / INVALID 193
结构观察区: Primary Flip 189.08（全链重定价，覆盖 100%）
Put Wall 190（弱结构｜现价高于该位 5.9%） | Call Wall 200（弱结构｜现价高于该位 0.6%）
最近结构参考: Call Wall 200（现价高于该位 0.6%）
量化视角： 正 Gamma（7676万，无历史分位）｜正 Gamma 减弱（352万）｜现价位于 Flip 上方 6.43%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（Put Wall，弱结构） / 190（MaxPain，仅结算参考） / 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 189（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 195.0P — Vol 18,108 | 最新价 $0.93 | OI 4127→6138 (ΔOI +2011张) | ΔOI/Volume 11.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2011张（+48.7% vs前日OI），连续性待观察（方向未知）
10-30 130.0P — Vol 2,820 | 最新价 $0.06 | OI 1949→3798 (ΔOI +1849张) | ΔOI/Volume 65.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1849张（+94.9% vs前日OI），连续性待观察（方向未知）
10-23 202.5C — Vol 15,254 | 最新价 $2.75 | OI 5705→7108 (ΔOI +1403张) | ΔOI/Volume 9.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1403张（+24.6% vs前日OI），连续性待观察（方向未知）
10-30 207.5C — Vol 2,646 | 最新价 $3.60 | OI 1069→2311 (ΔOI +1242张) | ΔOI/Volume 46.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1242张（+116.2% vs前日OI），连续性待观察（方向未知）
10-30 220.0C — Vol 2,707 | 最新价 $0.91 | OI 2726→3875 (ΔOI +1149张) | ΔOI/Volume 42.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1149张（+42.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,654 张（Put 3,860 / Call 3,794），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +0.8k / P +9.5k ｜ Activity HIGH ｜ 1D
10-30  C +6.3k / P -0.4k ｜ Activity HIGH ｜ 8D
11-06  C +3.0k / P +2.1k ｜ Activity MEDIUM △ ｜ 15D
11-13  C +1.1k / P +0.9k ｜ Activity MEDIUM △ ｜ 22D

📆 10-23 Forward Structure
存量OI: C 132.5k / P 134.2k，今日变化ΔOI: C +0.8k / P +9.5k，平值价格ATM: C $3.25 / P $2.27 ｜ ATM IV 57.0%，净 delta 敞口 -40k shares
Top ΔOI: P 195 +2,011 ｜ C 202 +1,403
仓位参考: Max Pain 190 ｜ Call Wall 205（+1.9%，弱）（OI 17.0k） ｜ Put Wall 190（-5.6%，弱）（OI 8.7k）
量化解读： 存量两侧均衡｜ATM IV 57.0%｜历史 Rank 90%（近端代理）｜IV/RV 1.30×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 40,299 股

📆 10-30 Forward Structure
存量OI: C 56.8k / P 80.0k，今日变化ΔOI: C +6.3k / P -0.4k，平值价格ATM: C $6.50 / P $5.35 ｜ ATM IV 49.4%，净 delta 敞口 23k shares
仓位参考: Max Pain 190 ｜ Call Wall 210（+4.4%，弱）（OI 4.4k） ｜ Put Wall 190（-5.6%，弱）（OI 6.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 49.4%｜历史 Rank 90%（近端代理）｜IV/RV 1.13×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 22,928 股

11-06（MEDIUM △）Top ΔOI: 215C +414
11-06（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 215（+6.8%，弱）（OI 2.1k） ｜ Put Wall 190（-5.6%，弱）（OI 3.0k）

11-13（MEDIUM △）Top ΔOI: 192C +143
11-13（MEDIUM △）仓位参考: Max Pain 192 ｜ Call Wall 210（+4.4%，弱）（OI 1.2k） ｜ Put Wall 185（-8.1%，弱）（OI 0.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/PLTR_morning.json