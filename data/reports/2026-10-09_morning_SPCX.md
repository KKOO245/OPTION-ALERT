# 期权晨报 2026-10-09（快照 10:20 ET）

📊 市场环境

SPY $778.57 ｜ QQQ $751.27
VIX 15.10 ↓2.0%（5D -1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 46.3 ｜ 前值 48.1　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-12 162C ΔOI +3,149（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 160.57 → 今开 165.34（+3.0%） | 较昨收变动（含盘初走势） ｜ 今日高 166.38 ｜ 低 161.57

Options: P/C成交量 0.49 | OI比 1.02 | ATM IV 74.7% | Skew -2.1pp | Term 0.66 | ExpMove ±2.7%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.02×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-12（3D）±2.7% ｜ 10-14（5D）±4.0% ｜ 10-16（7D）±5.0% ｜ 10-19（10D）±5.5%
   ⇒ IV–VIX Spread: +59.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 58,007,840 | GEX Change vs 上次快照 57,629,878 | Flip: Primary Flip: 158.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 716 / LOW 147 / INVALID 437
结构观察区: Primary Flip 158.91（全链重定价，覆盖 96%）
最近结构参考: Flip 159（现价高于该位 2.6%）
量化视角： 正 Gamma（5801万，无历史分位）｜正 Gamma 增强（+5763万）｜现价位于 Flip 上方 2.57%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 162（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 159（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 167.5C — Vol 46,841 | 最新价 $0.15 | OI 7880→14275 (ΔOI +6395张) | ΔOI/Volume 13.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6395张（+81.2% vs前日OI），连续性待观察（方向未知）
10-09 165.0C — Vol 56,426 | 最新价 $0.40 | OI 9027→12887 (ΔOI +3860张) | ΔOI/Volume 6.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3860张（+42.8% vs前日OI），连续性待观察（方向未知）
10-16 152.5P — Vol 6,116 | 最新价 $1.37 | OI 3250→6664 (ΔOI +3414张) | ΔOI/Volume 55.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3414张（+105.0% vs前日OI），连续性待观察（方向未知）
10-12 162.5C — Vol 8,096 | 最新价 $1.75 | OI 322→3471 (ΔOI +3149张) | ΔOI/Volume 38.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3149张（+978.0% vs前日OI），连续性待观察（方向未知）
10-16 160.0P — Vol 14,790 | 最新价 $3.95 | OI 8464→11531 (ΔOI +3067张) | ΔOI/Volume 20.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3067张（+36.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 19,885 张（Put 6,481 / Call 13,404），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 206.3k / P 210.7k，今日成交量: C 138.4k / P 67.8k，平值价格ATM: C $1.50 / P $1.12 ｜ ATM IV 74.7%，预期波动 ±1.6%，Max Pain 162
Top ΔOI: P 175 -6,853 ｜ C 167 +6,395 ｜ C 165 +3,860

📆 Forward Expiration Structure

10-12  C +10.3k / P +1.4k ｜ Activity HIGH ｜ 3D
10-14  C +4.1k / P +2.8k ｜ Activity HIGH ｜ 5D
10-16  C +9.3k / P +11.6k ｜ Activity HIGH ｜ 7D
10-19  C -0.8k / P -2 ｜ Activity HIGH ｜ 10D

📆 10-12 Forward Structure
存量OI: C 46.4k / P 20.5k，今日变化ΔOI: C +10.3k / P +1.4k，平值价格ATM: C $2.40 / P $2.05 ｜ ATM IV 36.3%，净 delta 敞口 509k shares
Top ΔOI: C 162 +3,149 ｜ C 165 +2,783 ｜ P 165 -1,424
仓位参考: Max Pain 165 ｜ Call Wall 170（+4.3%，弱）（OI 6.7k） ｜ Put Wall 150（-8.0%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 36.3%｜历史 Rank 94%（近端代理）｜IV/RV 0.76×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 509,099 股

📆 10-14 Forward Structure
存量OI: C 11.3k / P 6.6k，今日变化ΔOI: C +4.1k / P +2.8k，平值价格ATM: C $3.52 / P $3.07 ｜ ATM IV 42.6%，净 delta 敞口 48k shares
Top ΔOI: C 170 +797 ｜ C 167 +673 ｜ C 165 +596
仓位参考: Max Pain 168 ｜ Call Wall 170（+4.3%，弱）（OI 1.7k） ｜ Put Wall 165（+1.2%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 42.6%｜历史 Rank 94%（近端代理）｜IV/RV 0.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 47,715 股

📆 10-16 Forward Structure
存量OI: C 358.1k / P 388.1k，今日变化ΔOI: C +9.3k / P +11.6k，平值价格ATM: C $4.30 / P $3.84 ｜ ATM IV 44.8%，净 delta 敞口 68k shares
Top ΔOI: P 152 +3,414 ｜ P 160 +3,067 ｜ C 170 +2,997
仓位参考: Max Pain 150 ｜ Call Wall 170（+4.3%，弱）（OI 28.2k） ｜ Put Wall 150（-8.0%，弱）（OI 24.6k）
量化解读： 存量两侧均衡｜ATM IV 44.8%｜历史 Rank 94%（近端代理）｜IV/RV 0.93×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 68,145 股

📆 10-19 Forward Structure
存量OI: C 7.0k / P 4.0k，今日变化ΔOI: C -0.8k / P -2，平值价格ATM: C $4.55 / P $4.50 ｜ ATM IV 41.6%，净 delta 敞口 11k shares
Top ΔOI: C 180 -702 ｜ C 175 -85
仓位参考: Max Pain 168 ｜ Put Wall 165（+1.2%）（OI 1.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 41.6%｜历史 Rank 94%（近端代理）｜IV/RV 0.87×（近似）｜净 delta 敞口 正 10,639 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/SPCX_morning.json