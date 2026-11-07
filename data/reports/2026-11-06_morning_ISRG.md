# 期权晨报 2026-11-06（快照 10:20 ET）

📊 市场环境

SPY $735.29 ｜ QQQ $656.10
VIX 24.90 ↓11.6%（5D +28.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 22.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 165 ｜ 前值 60　✅ 今日已公布
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 4.1 ｜ 前值 4.2　✅ 今日已公布
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 51 ｜ 前值 46.3　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 475P ΔOI +40（距现价 +3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 468.52 → 今开 456.49（-2.6%） | 较昨收变动（含盘初走势） ｜ 今日高 463.15 ｜ 低 456.00

Options: P/C成交量 0.47 | OI比 0.64 | ATM IV 98.8% | Skew -72.0pp | Term 0.37 | ExpMove ±5.3%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.37，近月 IV 高于远月）｜Put 保护异常便宜（Skew -72.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（7D）±5.3% ｜ 11-20（14D）±6.2% ｜ 11-27（21D）±10.1% ｜ 12-04（28D）±9.4%
   ⇒ IV–VIX Spread: +73.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,731,948 | GEX Change vs 上次快照 -252,784 | Flip: Primary Flip: 411.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 304 / LOW 182 / INVALID 484
结构观察区: Primary Flip 411.43（全链重定价，覆盖 88%）
最近结构参考: Flip 411（现价高于该位 11.5%）
量化视角： 正 Gamma（273万，无历史分位）｜正 Gamma 减弱（25万）｜现价位于 Flip 上方 11.52%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 435（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 411（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 462.5P — Vol 165 | 最新价 $10.90 | OI 0→141 (ΔOI +141张) | ΔOI/Volume 85.5% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增141张（前日OI缺失），值得跟踪（方向未知）
11-20 500.0P — Vol 70 | 最新价 $36.30 | OI 0→70 (ΔOI +70张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增70张（前日OI缺失），值得跟踪（方向未知）
11-20 475.0P — Vol 78 | 最新价 $21.04 | OI 35→75 (ΔOI +40张) | ΔOI/Volume 51.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增40张（+114.3% vs前日OI），连续性待观察（方向未知）
11-20 460.0P — Vol 60 | 最新价 $11.10 | OI 66→101 (ΔOI +35张) | ΔOI/Volume 58.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增35张（+53.0% vs前日OI），连续性待观察（方向未知）
11-06 472.5C — Vol 44 | 最新价 $1.80 | OI 10→40 (ΔOI +30张) | ΔOI/Volume 68.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30张（+300.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 316 张（Put 286 / Call 30），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 3.0k / P 1.9k，今日成交量: C 78 / P 16，平值价格ATM: C $5.20 / P $4.75 ｜ ATM IV 98.8%，预期波动 ±2.2%，Max Pain 435
Top ΔOI: C 472 +30 ｜ C 480 +29 ｜ C 477 +16

📆 Forward Expiration Structure

11-13  C +49 / P +0.2k ｜ Activity MEDIUM △ ｜ 7D
11-20  C -42 / P +0.1k ｜ Activity MEDIUM △ ｜ 14D
11-27  C +5 / P +3 ｜ Activity MEDIUM △ ｜ 21D
12-04  C +19 / P +8 ｜ Activity LOW ｜ 28D

📆 11-13 Forward Structure
存量OI: C 1.1k / P 1.3k，今日变化ΔOI: C +49 / P +0.2k，平值价格ATM: C $15.28 / P $9.15 ｜ ATM IV 42.1%，净 delta 敞口 -9k shares
Top ΔOI: P 462 +141 ｜ P 482 +20
仓位参考: Max Pain 440 ｜ Call Wall 440（-4.1%，弱）（OI 0.1k） ｜ Put Wall 462.5（+0.8%，弱）（OI 0.1k）
量化解读： 存量 Put 重｜ATM IV 42.1%｜历史 Rank 98%（近端代理）｜IV/RV 1.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 9,018 股

11-20（MEDIUM △）Top ΔOI: 500P +70 ｜ 475P +40
11-20（MEDIUM △）仓位参考: Max Pain 405 ｜ Call Wall 420（-8.5%，弱）（OI 0.8k） ｜ Put Wall 427.5（-6.8%，弱）（OI 0.4k）

11-27（MEDIUM △）Top ΔOI: 470C +3 ｜ 430P +1
11-27（MEDIUM △）仓位参考: Max Pain 430 ｜ Call Wall 430（-6.3%，弱）（OI 64）

12-04（Activity LOW）仓位参考: Max Pain 440 ｜ Call Wall 475（+3.5%）（OI 92） ｜ Put Wall 420（-8.5%，弱）（OI 17）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/ISRG_morning.json