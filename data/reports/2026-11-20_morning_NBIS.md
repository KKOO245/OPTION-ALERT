# 期权晨报 2026-11-20（快照 10:20 ET）

📊 市场环境

SPY $709.51 ｜ QQQ $630.78
VIX 27.48 ↓3.4%（5D +42.4%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 96.92 → 今开 93.69（-3.3%） | 较昨收变动（含盘初走势） ｜ 今日高 93.97 ｜ 低 88.22

Options: P/C成交量 1.92 | OI比 0.33 | ATM IV 111.2% | Skew -34.1pp | Term 1.08 | ExpMove ±13.6%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构正常（Term 1.08）｜Put 保护异常便宜（Skew -34.1pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.33）+ 当日成交偏 Put（P/C量 1.92）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.92×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.33×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（7D）±13.6% ｜ 12-04（14D）±20.6% ｜ 12-11（21D）±23.2% ｜ 12-18（28D）±26.9%
   ⇒ IV–VIX Spread: +83.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,647,048 | GEX Change vs 上次快照 2,112,726 | Flip: Primary Flip: 93.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 477 / LOW 134 / INVALID 80
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 93.91（全链重定价，覆盖 100%）
最近结构参考: Flip 94（现价低于该位 4.5%）
量化视角： 负 Gamma（765万，无历史分位）｜负 Gamma 缓解（+211万）｜现价位于 Flip 下方 4.55%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 115（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 94（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 110.0C — Vol 7,045 | 最新价 $2.24 | OI 2521→6070 (ΔOI +3549张) | ΔOI/Volume 50.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3549张（+140.8% vs前日OI），连续性待观察（方向未知）
11-20 130.0C — Vol 13,000 | 最新价 $0.03 | OI 17223→20560 (ΔOI +3337张) | ΔOI/Volume 25.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3337张（+19.4% vs前日OI），连续性待观察（方向未知）
11-20 150.0C — Vol 4,136 | 最新价 $0.01 | OI 5632→7312 (ΔOI +1680张) | ΔOI/Volume 40.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1680张（+29.8% vs前日OI），连续性待观察（方向未知）
12-18 120.0C — Vol 2,713 | 最新价 $4.75 | OI 869→2210 (ΔOI +1341张) | ΔOI/Volume 49.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1341张（+154.3% vs前日OI），连续性待观察（方向未知）
11-27 120.0C — Vol 5,080 | 最新价 $0.80 | OI 987→2293 (ΔOI +1306张) | ΔOI/Volume 25.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1306张（+132.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,213 张（Put 0 / Call 11,213），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 216.5k / P 71.1k，今日成交量: C 13.6k / P 26.0k，平值价格ATM: C $2.58 / P $1.59 ｜ ATM IV 111.2%，预期波动 ±4.7%，Max Pain 115
Top ΔOI: P 140 -4,277 ｜ C 130 +3,337 ｜ P 145 -2,555

📆 Forward Expiration Structure

11-27  C +8.6k / P -0.1k ｜ Activity MEDIUM △ ｜ 7D
12-04  C +2.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 14D
12-11  C +0.7k / P +0.4k ｜ Activity HIGH ｜ 21D
12-18  C +2.8k / P -2.5k ｜ Activity HIGH ｜ 28D

📆 11-27 Forward Structure
存量OI: C 52.0k / P 19.3k，今日变化ΔOI: C +8.6k / P -0.1k，平值价格ATM: C $7.00 / P $5.20 ｜ ATM IV 118.6%，净 delta 敞口 266k shares
Top ΔOI: C 110 +3,549
仓位参考: Max Pain 110 ｜ Put Wall 90（+0.4%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 118.6%｜历史 Rank 60%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 正 266,487 股

12-04（MEDIUM △）Top ΔOI: 115C +450 ｜ 100C +411
12-04（MEDIUM △）仓位参考: Max Pain 120 ｜ Put Wall 95（+6.0%，弱）（OI 0.5k）

📆 12-11 Forward Structure
存量OI: C 7.4k / P 9.0k，今日变化ΔOI: C +0.7k / P +0.4k，平值价格ATM: C $11.55 / P $9.25 ｜ ATM IV 121.2%，净 delta 敞口 11k shares
Top ΔOI: C 125 +327 ｜ P 85 +279 ｜ P 95 +139
仓位参考: Max Pain 130 ｜ Put Wall 85（-5.2%，弱）（OI 0.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 121.2%｜历史 Rank 60%（近端代理）｜IV/RV 0.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 10,586 股

📆 12-18 Forward Structure
存量OI: C 132.0k / P 95.1k，今日变化ΔOI: C +2.8k / P -2.5k，平值价格ATM: C $12.95 / P $11.13 ｜ ATM IV 119.8%，净 delta 敞口 484k shares
Top ΔOI: P 200 -1,364 ｜ C 120 +1,341 ｜ P 190 -1,231
仓位参考: Max Pain 155 ｜ Put Wall 90（+0.4%，弱）（OI 3.6k）
量化解读： 存量 Call 重｜ATM IV 119.8%｜历史 Rank 60%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 正 483,948 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/NBIS_morning.json