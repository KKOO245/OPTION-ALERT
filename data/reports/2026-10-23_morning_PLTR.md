# 期权晨报 2026-10-23（快照 10:20 ET）

📊 市场环境

SPY $763.09 ｜ QQQ $706.84
VIX 19.93 ↑4.7%（5D -0.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 22.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 196.19 → 今开 195.02（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 195.71 ｜ 低 190.57

Options: P/C成交量 0.58 | OI比 0.94 | ATM IV 75.0% | Skew 4.2pp | Term 0.88 | ExpMove ±5.7%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价中性（Skew 4.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.94×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（7D）±5.7% ｜ 11-06（14D）±12.7% ｜ 11-13（21D）±13.8% ｜ 11-20（28D）±14.6%
   ⇒ IV–VIX Spread: +55.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 45,907,797 | GEX Change vs 上次快照 -1,874,850 | Flip: Primary Flip: 187.59（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 593 / LOW 89 / INVALID 268
结构观察区: Primary Flip 187.59（全链重定价，覆盖 98%）
Put Wall 180（弱结构｜现价高于该位 8.4%） | Call Wall 200（弱结构｜现价低于该位 2.5%）
最近结构参考: Call Wall 200（现价低于该位 2.5%）
量化视角： 正 Gamma（4591万，无历史分位）｜正 Gamma 减弱（187万）｜现价位于 Flip 上方 4.00%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（Put Wall，弱结构） / 192（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 188（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 210.0C — Vol 11,349 | 最新价 $0.06 | OI 8093→10896 (ΔOI +2803张) | ΔOI/Volume 24.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2803张（+34.6% vs前日OI），连续性待观察（方向未知）
10-30 212.5C — Vol 4,720 | 最新价 $1.11 | OI 1699→4459 (ΔOI +2760张) | ΔOI/Volume 58.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2760张（+162.4% vs前日OI），连续性待观察（方向未知）
10-30 120.0P — Vol 3,180 | 最新价 $0.05 | OI 1688→4333 (ΔOI +2645张) | ΔOI/Volume 83.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2645张（+156.7% vs前日OI），连续性待观察（方向未知）
10-30 205.0C — Vol 6,239 | 最新价 $2.66 | OI 4004→6617 (ΔOI +2613张) | ΔOI/Volume 41.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2613张（+65.3% vs前日OI），连续性待观察（方向未知）
10-23 200.0C — Vol 19,503 | 最新价 $1.11 | OI 11919→13432 (ΔOI +1513张) | ΔOI/Volume 7.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1513张（+12.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,334 张（Put 2,645 / Call 9,689），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 135.7k / P 127.6k，今日成交量: C 51.5k / P 29.9k，平值价格ATM: C $1.80 / P $1.41 ｜ ATM IV 75.0%，预期波动 ±1.6%，Max Pain 192
Top ΔOI: C 210 +2,803 ｜ C 190 -2,317 ｜ P 190 -2,299

📆 Forward Expiration Structure

10-30  C +8.2k / P +6.9k ｜ Activity HIGH ｜ 7D
11-06  C +0.8k / P +1.3k ｜ Activity HIGH ｜ 14D
11-13  C +0.5k / P +1.1k ｜ Activity MEDIUM △ ｜ 21D
11-20  C +2.7k / P +1.7k ｜ Activity HIGH ｜ 28D

📆 10-30 Forward Structure
存量OI: C 65.0k / P 86.9k，今日变化ΔOI: C +8.2k / P +6.9k，平值价格ATM: C $5.90 / P $5.30 ｜ ATM IV 50.9%，净 delta 敞口 137k shares
Top ΔOI: C 212 +2,760 ｜ C 205 +2,613
仓位参考: Max Pain 190 ｜ Call Wall 205（+5.1%，弱）（OI 6.6k） ｜ Put Wall 190（-2.6%，弱）（OI 6.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 50.9%｜历史 Rank 100%（近端代理）｜IV/RV 1.13×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 137,462 股

📆 11-06 Forward Structure
存量OI: C 30.3k / P 31.0k，今日变化ΔOI: C +0.8k / P +1.3k，平值价格ATM: C $12.50 / P $12.25 ｜ ATM IV 80.0%，净 delta 敞口 1k shares
Top ΔOI: P 180 +601 ｜ C 195 +170
仓位参考: Max Pain 190 ｜ Call Wall 205（+5.1%，弱）（OI 1.7k） ｜ Put Wall 190（-2.6%，弱）（OI 3.1k）
量化解读： 存量两侧均衡｜ATM IV 80.0%｜历史 Rank 100%（近端代理）｜IV/RV 1.77×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,444 股

11-13（MEDIUM △）Top ΔOI: 165P +162
11-13（MEDIUM △）仓位参考: Max Pain 195 ｜ Call Wall 210（+7.6%，弱）（OI 1.2k） ｜ Put Wall 180（-7.7%，弱）（OI 1.3k）

📆 11-20 Forward Structure
存量OI: C 160.1k / P 165.8k，今日变化ΔOI: C +2.7k / P +1.7k，平值价格ATM: C $14.57 / P $13.92 ｜ ATM IV 66.1%，净 delta 敞口 25k shares
Top ΔOI: C 190 +413 ｜ P 197 +290
仓位参考: Max Pain 175 ｜ Call Wall 200（+2.5%，弱）（OI 13.0k） ｜ Put Wall 185（-5.2%，弱）（OI 10.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 66.1%｜历史 Rank 100%（近端代理）｜IV/RV 1.46×（近似）｜净 delta 敞口 正 24,518 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/PLTR_morning.json