# 期权晨报 2026-09-25（快照 10:20 ET）

📊 市场环境

SPY $769.28 ｜ QQQ $741.40
VIX 15.83 ↑1.0%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 0 ｜ 前值 0.9　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 399.52 → 今开 397.64（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 399.84 ｜ 低 391.95

Options: P/C成交量 5.67 | OI比 0.68 | ATM IV 70.0% | Skew -2.2pp | Term 0.60 | ExpMove ±4.0%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.60，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.2pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.68）+ 当日成交偏 Put（P/C量 5.67）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 5.67×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±4.0% ｜ 10-09（14D）±5.4% ｜ 10-16（21D）±5.6% ｜ 10-23（28D）±9.9%
   ⇒ IV–VIX Spread: +54.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,119,432 | GEX Change vs 上次快照 -1,371,537 | Flip: Primary Flip: 385.08（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 286 / LOW 172 / INVALID 438
结构观察区: Primary Flip 385.08（全链重定价，覆盖 93%）
Call Wall 400（弱结构｜现价低于该位 1.4%）
最近结构参考: Call Wall 400（现价低于该位 1.4%）
量化视角： 正 Gamma（112万，无历史分位）｜正 Gamma 减弱（137万）｜现价位于 Flip 上方 2.46%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 390（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 385（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 420.0C — Vol 149 | 最新价 $0.23 | OI 163→296 (ΔOI +133张) | ΔOI/Volume 89.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增133张（+81.6% vs前日OI），连续性待观察（方向未知）
09-25 387.5P — Vol 135 | 最新价 $0.30 | OI 65→195 (ΔOI +130张) | ΔOI/Volume 96.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增130张（+200.0% vs前日OI），连续性待观察（方向未知）
09-25 392.5P — Vol 135 | 最新价 $0.87 | OI 73→200 (ΔOI +127张) | ΔOI/Volume 94.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增127张（+174.0% vs前日OI），连续性待观察（方向未知）
09-25 415.0C — Vol 166 | 最新价 $0.35 | OI 286→370 (ΔOI +84张) | ΔOI/Volume 50.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增84张（+29.4% vs前日OI），连续性待观察（方向未知）
10-23 300.0P — Vol 110 | 最新价 $0.55 | OI 5→65 (ΔOI +60张) | ΔOI/Volume 54.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增60张（+1200.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 534 张（Put 317 / Call 217），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 2.7k / P 1.9k，今日成交量: C 0.2k / P 0.4k，平值价格ATM: C $4.50 / P $1.52 ｜ ATM IV 70.0%，预期波动 ±1.5%，Max Pain 390
Top ΔOI: C 420 +133 ｜ P 387 +130 ｜ P 392 +127

📆 Forward Expiration Structure

10-02  C +31 / P +55 ｜ Activity MEDIUM △ ｜ 7D
10-09  C +16 / P +4 ｜ Activity LOW ｜ 14D
10-16  C +33 / P -14 ｜ Activity MEDIUM △ ｜ 21D
10-23  C +19 / P +0.1k ｜ Activity HIGH ｜ 28D

📆 10-02 Forward Structure
存量OI: C 1.2k / P 3.1k，今日变化ΔOI: C +31 / P +55，平值价格ATM: C $9.46 / P $6.40 ｜ ATM IV 34.4%，净 delta 敞口 -2k shares
Top ΔOI: P 400 +37 ｜ C 395 +14 ｜ C 400 +11
仓位参考: Max Pain 378 ｜ Call Wall 410（+3.9%）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 34.4%｜历史 Rank 95%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,683 股

10-09（Activity LOW）仓位参考: Max Pain 370 ｜ Call Wall 420（+6.5%，弱）（OI 0.1k） ｜ Put Wall 385（-2.4%，弱）（OI 16）

10-16（MEDIUM △）仓位参考: Max Pain 380 ｜ Call Wall 400（+1.4%，弱）（OI 1.0k） ｜ Put Wall 380（-3.7%，弱）（OI 0.6k）

📆 10-23 Forward Structure
存量OI: C 0.8k / P 0.6k，今日变化ΔOI: C +19 / P +0.1k，平值价格ATM: C $23.70 / P $15.36 ｜ ATM IV 42.1%，净 delta 敞口 -464 shares
Top ΔOI: P 400 +16
仓位参考: Max Pain 395 ｜ Call Wall 415（+5.2%，弱）（OI 62） ｜ Put Wall 420（+6.5%，弱）（OI 92）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 42.1%｜历史 Rank 95%（近端代理）｜净 delta 敞口 负 464 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/ISRG_morning.json