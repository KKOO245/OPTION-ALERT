# 期权晨报 2026-09-25（快照 10:20 ET）

📊 市场环境

SPY $766.83 ｜ QQQ $740.98
VIX 15.83 ↑1.0%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 0 ｜ 前值 0.9　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 152P ΔOI +1,895（距现价 -1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 156.05 → 今开 156.80（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 157.16 ｜ 低 153.85

Options: P/C成交量 0.14 | OI比 3.23 | ATM IV 60.0% | Skew -3.5pp | Term 0.55 | ExpMove ±4.3%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.55，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.14×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 3.23×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±4.3% ｜ 10-09（14D）±4.6% ｜ 10-16（21D）±6.9% ｜ 10-23（28D）±7.1%
   ⇒ IV–VIX Spread: +44.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -53,928,851 | GEX Change vs 上次快照 -5,696,807 | Flip: Primary Flip: 166.30（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 351 / LOW 102 / INVALID 327
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 166.30（全链重定价，覆盖 86%）
Put Wall 150（现价高于该位 3.3%）
最近结构参考: Put Wall 150（现价高于该位 3.3%）
量化视角： 负 Gamma（5393万，无历史分位）｜负 Gamma 加深（570万）｜现价位于 Flip 下方 6.80%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall）；上方 157（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 166（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 151.0P — Vol 3,012 | 最新价 $0.10 | OI 2871→5127 (ΔOI +2256张) | ΔOI/Volume 74.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2256张（+78.6% vs前日OI），连续性待观察（方向未知）
10-02 152.0P — Vol 1,996 | 最新价 $1.36 | OI 63→1958 (ΔOI +1895张) | ΔOI/Volume 94.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1895张（+3007.9% vs前日OI），连续性待观察（方向未知）
09-25 157.0C — Vol 2,598 | 最新价 $0.48 | OI 477→2110 (ΔOI +1633张) | ΔOI/Volume 62.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1633张（+342.4% vs前日OI），连续性待观察（方向未知）
09-25 154.0P — Vol 3,561 | 最新价 $0.51 | OI 3906→4969 (ΔOI +1063张) | ΔOI/Volume 29.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1063张（+27.2% vs前日OI），连续性待观察（方向未知）
10-16 147.0P — Vol 737 | 最新价 $1.73 | OI 1615→2343 (ΔOI +728张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增728张（+45.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,575 张（Put 5,942 / Call 1,633），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 14.8k / P 47.9k，今日成交量: C 0.6k / P 3.6k，平值价格ATM: C $1.10 / P $0.91 ｜ ATM IV 60.0%，预期波动 ±1.3%，Max Pain 157
Top ΔOI: P 151 +2,256 ｜ C 157 +1,633 ｜ P 154 +1,063

📆 Forward Expiration Structure

10-02  C +1.3k / P +4.6k ｜ Activity HIGH ｜ 7D
10-09  C +0.1k / P +77 ｜ Activity MEDIUM △ ｜ 14D
10-16  C -96 / P +8 ｜ Activity LOW ｜ 21D
10-23  C +0.1k / P +74 ｜ Activity MEDIUM △ ｜ 28D

📆 10-02 Forward Structure
存量OI: C 4.8k / P 23.1k，今日变化ΔOI: C +1.3k / P +4.6k，平值价格ATM: C $3.76 / P $2.86 ｜ ATM IV 35.9%，净 delta 敞口 -92k shares
Top ΔOI: P 152 +1,895 ｜ P 153 +676 ｜ P 146 +616
仓位参考: Max Pain 157 ｜ Call Wall 165（+6.5%，弱）（OI 1.0k） ｜ Put Wall 148（-4.5%）（OI 10.1k）
量化解读： 存量 Put 重｜ATM IV 35.9%｜历史 Rank 99%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 92,140 股

10-09（MEDIUM △）Top ΔOI: 158C +58 ｜ 147P +33
10-09（MEDIUM △）仓位参考: Max Pain 157 ｜ Call Wall 158（+1.9%，弱）（OI 0.1k） ｜ Put Wall 145（-6.4%，弱）（OI 1.0k）

10-16（Activity LOW）仓位参考: Max Pain 162 ｜ Call Wall 165（+6.5%，弱）（OI 2.9k） ｜ Put Wall 150（-3.2%）（OI 20.9k）

10-23（MEDIUM △）Top ΔOI: 167C +48 ｜ 140P +36
10-23（MEDIUM △）仓位参考: Max Pain 162 ｜ Call Wall 162（+4.5%，弱）（OI 52） ｜ Put Wall 145（-6.4%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/XBI_morning.json