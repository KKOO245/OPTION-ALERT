# 期权晨报 2026-10-09（快照 10:20 ET）

📊 市场环境

SPY $778.69 ｜ QQQ $751.27
VIX 15.10 ↓2.0%（5D -1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 46.3 ｜ 前值 48.1　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 415.41 → 今开 416.39（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 427.53 ｜ 低 415.86

Options: P/C成交量 0.63 | OI比 0.51 | ATM IV 65.6% | Skew -2.0pp | Term 0.71 | ExpMove ±6.9%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±6.9% ｜ 10-23（14D）±10.2% ｜ 10-30（21D）±8.4% ｜ 11-06（28D）±4.1%
   ⇒ IV–VIX Spread: +50.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,158,987 | GEX Change vs 上次快照 -1,104,012 | Flip: Primary Flip: 397.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 277 / LOW 137 / INVALID 450
结构观察区: Primary Flip 397.02（全链重定价，覆盖 86%）
Call Wall 420（弱结构｜现价高于该位 1.2%）
最近结构参考: Call Wall 420（现价高于该位 1.2%）
量化视角： 正 Gamma（416万，无历史分位）｜正 Gamma 减弱（110万）｜现价位于 Flip 上方 7.09%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 395（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 397（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 435.0C — Vol 346 | 最新价 $1.55 | OI 240→284 (ΔOI +44张) | ΔOI/Volume 12.7% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增44张（+18.3% vs前日OI），值得跟踪（方向未知）
10-16 375.0P — Vol 63 | 最新价 $0.40 | OI 229→266 (ΔOI +37张) | ΔOI/Volume 58.7% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增37张（+16.2% vs前日OI），值得跟踪（方向未知）
10-09 402.5P — Vol 27 | 最新价 $0.55 | OI 15→39 (ΔOI +24张) | ΔOI/Volume 88.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24张（+160.0% vs前日OI），连续性待观察（方向未知）
10-16 430.0C — Vol 36 | 最新价 $2.75 | OI 361→381 (ΔOI +20张) | ΔOI/Volume 55.6% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增20张（+5.5% vs前日OI），值得跟踪（方向未知）
10-16 432.5C — Vol 19 | 最新价 $1.85 | OI 0→19 (ΔOI +19张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增19张（前日OI缺失），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 144 张（Put 61 / Call 83），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 3.3k / P 1.7k，今日成交量: C 97 / P 61，平值价格ATM: C $1.83 / P $4.25 ｜ ATM IV 65.6%，预期波动 ±1.4%，Max Pain 395
Top ΔOI: P 402 +24 ｜ P 405 +14 ｜ P 410 +10

📆 Forward Expiration Structure

10-16  C +60 / P +33 ｜ Activity MEDIUM △ ｜ 7D
10-23  C +25 / P +12 ｜ Activity MEDIUM △ ｜ 14D
10-30  C +18 / P +51 ｜ Activity MEDIUM △ ｜ 21D
11-06  C +4 / P +3 ｜ Activity MEDIUM △ ｜ 28D

📆 10-16 Forward Structure
存量OI: C 10.8k / P 10.6k，今日变化ΔOI: C +60 / P +33，平值价格ATM: C $8.00 / P $21.30 ｜ ATM IV 33.3%，净 delta 敞口 -1k shares
Top ΔOI: C 420 -59 ｜ C 435 +44
仓位参考: Max Pain 390 ｜ Call Wall 400（-5.9%，弱）（OI 0.9k） ｜ Put Wall 400（-5.9%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 33.3%｜历史 Rank 97%（近端代理）｜IV/RV 1.37×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,251 股

10-23（MEDIUM △）Top ΔOI: 400P +8 ｜ 430C +6
10-23（MEDIUM △）仓位参考: Max Pain 415 ｜ Call Wall 425（-0.0%）（OI 0.5k） ｜ Put Wall 415（-2.4%）（OI 0.5k）

10-30（MEDIUM △）仓位参考: Max Pain 395 ｜ Call Wall 460（+8.2%，弱）（OI 94） ｜ Put Wall 400（-5.9%，弱）（OI 45）

11-06（MEDIUM △）Top ΔOI: 425C +8 ｜ 450C -3
11-06（MEDIUM △）仓位参考: Max Pain 400 ｜ Call Wall 455（+7.0%，弱）（OI 49） ｜ Put Wall 400（-5.9%，弱）（OI 35）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/ISRG_morning.json