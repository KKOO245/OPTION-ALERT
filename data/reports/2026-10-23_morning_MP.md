# 期权晨报 2026-10-23（快照 10:20 ET）

📊 市场环境

SPY $763.05 ｜ QQQ $706.76
VIX 19.93 ↑4.7%（5D -0.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 21.2（extreme fear）
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


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 38.56 → 今开 38.14（-1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 38.32 ｜ 低 37.11

Options: P/C成交量 0.25 | OI比 0.59 | ATM IV 84.5% | Skew -3.5pp | Term 0.77 | ExpMove ±7.2%（近端） | Rank 79%
量化视角： IV 历史高位（Rank 79%，期权偏贵）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.25×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（7D）±7.2% ｜ 11-06（14D）±10.9% ｜ 11-13（21D）±12.2% ｜ 11-20（28D）±15.8%
   ⇒ IV–VIX Spread: +64.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,530,381 | GEX Change vs 上次快照 852,688 | Flip: Primary Flip: 39.09（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 328 / LOW 79 / INVALID 135
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 39.09（全链重定价，覆盖 88%）
Put Wall 40（弱结构｜现价低于该位 4.6%）
最近结构参考: Flip 39（现价低于该位 2.3%）
量化视角： 负 Gamma（153万，无历史分位）｜负 Gamma 缓解（+85万）｜现价位于 Flip 下方 2.34%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 40（Put Wall，弱结构） / 40（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 39（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 47.0C — Vol 732 | 最新价 $0.25 | OI 413→1078 (ΔOI +665张) | ΔOI/Volume 90.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增665张（+161.0% vs前日OI），连续性待观察（方向未知）
10-23 38.5C — Vol 356 | 最新价 $0.60 | OI 32→296 (ΔOI +264张) | ΔOI/Volume 74.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增264张（+825.0% vs前日OI），连续性待观察（方向未知）
10-23 39.0C — Vol 621 | 最新价 $0.38 | OI 31→290 (ΔOI +259张) | ΔOI/Volume 41.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增259张（+835.5% vs前日OI），连续性待观察（方向未知）
11-20 38.0C — Vol 253 | 最新价 $3.20 | OI 175→428 (ΔOI +253张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增253张（+144.6% vs前日OI），连续性待观察（方向未知）
10-23 39.5C — Vol 268 | 最新价 $0.21 | OI 173→383 (ΔOI +210张) | ΔOI/Volume 78.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增210张（+121.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,651 张（Put 0 / Call 1,651），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 11.8k / P 7.0k，今日成交量: C 0.6k / P 89，平值价格ATM: C $0.40 / P $0.30 ｜ ATM IV 84.5%，预期波动 ±1.8%，Max Pain 40
Top ΔOI: C 38 +264 ｜ C 39 +259 ｜ P 42 -218

📆 Forward Expiration Structure

10-30  C +0.5k / P +24 ｜ Activity MEDIUM △ ｜ 7D
11-06  C +0.9k / P +0.4k ｜ Activity MEDIUM △ ｜ 14D
11-13  C -25 / P +46 ｜ Activity LOW ｜ 21D
11-20  C +0.4k / P +0.3k ｜ Activity LOW ｜ 28D

📆 10-30 Forward Structure
存量OI: C 8.8k / P 7.0k，今日变化ΔOI: C +0.5k / P +24，平值价格ATM: C $1.31 / P $1.42 ｜ ATM IV 60.7%，净 delta 敞口 30k shares
Top ΔOI: P 37 +126 ｜ P 50 -75 ｜ P 38 +66
仓位参考: Max Pain 44 ｜ Put Wall 37（-3.1%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 60.7%｜历史 Rank 79%（近端代理）｜IV/RV 1.27×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 30,323 股

11-06（MEDIUM △）Top ΔOI: 42P +129 ｜ 42P +99
11-06（MEDIUM △）仓位参考: Max Pain 43 ｜ Call Wall 40（+4.8%，弱）（OI 0.3k） ｜ Put Wall 38（-0.5%）（OI 0.9k）

11-13（Activity LOW）仓位参考: Max Pain 42 ｜ Call Wall 35（-8.3%，弱）（OI 0.5k） ｜ Put Wall 39（+2.2%）（OI 0.7k）

11-20（Activity LOW）仓位参考: Max Pain 45 ｜ Call Wall 40（+4.8%，弱）（OI 1.0k） ｜ Put Wall 40（+4.8%，弱）（OI 1.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/MP_morning.json