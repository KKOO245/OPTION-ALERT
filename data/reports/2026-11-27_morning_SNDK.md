# 期权晨报 2026-11-27（快照 10:20 ET）

📊 市场环境

SPY $722.09 ｜ QQQ $642.07
VIX 27.52 ↑2.7%（5D -23.3%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 22.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 73.61 → 今开 79.92（+8.6%） | 较昨收变动（含盘初走势） ｜ 今日高 81.44 ｜ 低 77.10

Options: P/C成交量 0.91 | OI比 0.35 | ATM IV 222.5% | Skew 9.8pp | Term 0.53 | ExpMove ±14.9%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.53，近月 IV 高于远月）｜保护溢价显著（Skew 9.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.35）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.91×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.35×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 12-04（7D）±14.9% ｜ 12-11（14D）±20.1% ｜ 12-18（21D）±23.1% ｜ 12-24（27D）±29.0%
   ⇒ IV–VIX Spread: +195.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,458,218 | GEX Change vs 上次快照 41,276,987 | Flip: Primary Flip: 81.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 1044 / LOW 830 / INVALID 4158
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 81.44（全链重定价，覆盖 91%）
Put Wall 75（现价高于该位 6.4%）
最近结构参考: Flip 81（现价低于该位 2.0%）
量化视角： 负 Gamma（346万，无历史分位）｜负 Gamma 缓解（+4128万）｜现价位于 Flip 下方 1.99%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 75（Put Wall）；上方 80（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 81（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 70.0C — Vol 18,117 | 最新价 $4.60 | OI 181→9071 (ΔOI +8890张) | ΔOI/Volume 49.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8890张（+4911.6% vs前日OI），连续性待观察（方向未知）
12-18 60.0P — Vol 8,524 | 最新价 $3.50 | OI 2414→7825 (ΔOI +5411张) | ΔOI/Volume 63.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5411张（+224.2% vs前日OI），连续性待观察（方向未知）
11-27 75.0C — Vol 14,454 | 最新价 $1.75 | OI 1297→6076 (ΔOI +4779张) | ΔOI/Volume 33.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4779张（+368.5% vs前日OI），连续性待观察（方向未知）
11-27 80.0C — Vol 20,096 | 最新价 $0.45 | OI 4030→8149 (ΔOI +4119张) | ΔOI/Volume 20.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4119张（+102.2% vs前日OI），连续性待观察（方向未知）
12-31 120.0C — Vol 4,079 | 最新价 $0.82 | OI 247→4025 (ΔOI +3778张) | ΔOI/Volume 92.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3778张（+1529.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 26,977 张（Put 5,411 / Call 21,566），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 335.1k / P 116.1k，今日成交量: C 36.3k / P 33.1k，平值价格ATM: C $1.15 / P $1.65 ｜ ATM IV 222.5%，预期波动 ±3.5%，Max Pain 80
Top ΔOI: C 70 +8,890 ｜ C 75 +4,779 ｜ C 80 +4,119

📆 Forward Expiration Structure

12-04  C +16.2k / P +6.8k ｜ Activity HIGH ｜ 7D
12-11  C +6.0k / P -0.3k ｜ Activity MEDIUM △ ｜ 14D
12-18  C +2.6k / P -13.7k ｜ Activity HIGH ｜ 21D
12-24  C +2.2k / P +0.4k ｜ Activity MEDIUM △ ｜ 27D

📆 12-04 Forward Structure
存量OI: C 147.7k / P 71.5k，今日变化ΔOI: C +16.2k / P +6.8k，平值价格ATM: C $5.70 / P $6.20 ｜ ATM IV 133.7%，净 delta 敞口 1.1M shares
Top ΔOI: C 85 +2,936 ｜ C 75 +2,910 ｜ P 73 +2,122
仓位参考: Max Pain 90 ｜ Call Wall 85（+6.5%，弱）（OI 5.6k） ｜ Put Wall 87.5（+9.6%，弱）（OI 3.6k）
量化解读： 存量 Call 重｜ATM IV 133.7%｜历史 Rank 99%（近端代理）｜IV/RV 0.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,127,437 股

12-11（MEDIUM △）Top ΔOI: 70C +1,729 ｜ 85C +1,187
12-11（MEDIUM △）仓位参考: Max Pain 97 ｜ Call Wall 80（+0.2%，弱）（OI 2.8k） ｜ Put Wall 80（+0.2%）（OI 10.4k）

📆 12-18 Forward Structure
存量OI: C 574.5k / P 503.1k，今日变化ΔOI: C +2.6k / P -13.7k，平值价格ATM: C $9.28 / P $9.15 ｜ ATM IV 118.6%，净 delta 敞口 1.8M shares
Top ΔOI: P 60 +5,411 ｜ P 150 -4,975 ｜ P 70 -4,364
仓位参考: Max Pain 108 ｜ Put Wall 75（-6.0%，弱）（OI 43.2k）
量化解读： 存量两侧均衡｜ATM IV 118.6%｜历史 Rank 99%（近端代理）｜IV/RV 0.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,798,414 股

12-24（MEDIUM △）Top ΔOI: 122C +868 ｜ 60P +306
12-24（MEDIUM △）仓位参考: Max Pain 111 ｜ Put Wall 87.5（+9.6%，弱）（OI 1.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/SNDK_morning.json