# 期权晨报 2026-11-06（快照 10:20 ET）

📊 市场环境

SPY $740.12 ｜ QQQ $660.07
VIX 24.90 ↓11.6%（5D +28.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
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
🟡 **近现价集中开仓**: 11-20 10P ΔOI +186（距现价 -4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-04 9P ΔOI +140 占该期限总 OI 28.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 9.64 → 今开 10.25（+6.4%） | 较昨收变动（含盘初走势） ｜ 今日高 10.80 ｜ 低 9.90

Options: P/C成交量 3.57 | OI比 0.31 | ATM IV 185.2% | Skew -3.7pp | Term 0.48 | ExpMove ±13.4%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.48，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.7pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.31）+ 当日成交偏 Put（P/C量 3.57）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 3.57×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.31×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（7D）±13.4% ｜ 11-20（14D）±13.8% ｜ 11-27（21D）±15.0% ｜ 12-04（28D）±4.5%
   ⇒ IV–VIX Spread: +160.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 780,936 | GEX Change vs 上次快照 307,608 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 73%（带内） ｜ IV 有效性: VALID 95 / LOW 95 / INVALID 220
结构观察区: NO_CROSS
Put Wall 11（现价低于该位 4.8%）
最近结构参考: Put Wall 11（现价低于该位 4.8%）
量化视角： 正 Gamma（78万，无历史分位）｜正 Gamma 增强（+31万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 11（Put Wall） / 12（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 11.0P — Vol 236 | 最新价 $1.60 | OI 96→283 (ΔOI +187张) | ΔOI/Volume 79.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增187张（+194.8% vs前日OI），连续性待观察（方向未知）
11-20 10.0P — Vol 249 | 最新价 $0.85 | OI 123→309 (ΔOI +186张) | ΔOI/Volume 74.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增186张（+151.2% vs前日OI），连续性待观察（方向未知）
11-13 9.5P — Vol 187 | 最新价 $0.42 | OI 20→202 (ΔOI +182张) | ΔOI/Volume 97.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增182张（+910.0% vs前日OI），连续性待观察（方向未知）
11-13 9.0P — Vol 181 | 最新价 $0.28 | OI 4→181 (ΔOI +177张) | ΔOI/Volume 97.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增177张（+4425.0% vs前日OI），连续性待观察（方向未知）
12-04 9.5P — Vol 140 | 最新价 $0.93 | OI 40→180 (ΔOI +140张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增140张（+350.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 872 张（Put 872 / Call 0），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 3.5k / P 1.1k，今日成交量: C 0.2k / P 0.5k，平值价格ATM: C $0.10 / P $0.82 ｜ ATM IV 185.2%，预期波动 ±8.8%，Max Pain 12
Top ΔOI: P 11 -143 ｜ P 12 -133 ｜ P 13 -87

📆 Forward Expiration Structure

11-13  C +29 / P +0.3k ｜ Activity HIGH ｜ 7D
11-20  C +11 / P +0.2k ｜ Activity HIGH ｜ 14D
11-27  C -4 / P -16 ｜ Activity MEDIUM △ ｜ 21D
12-04  C +17 / P +0.1k ｜ Activity HIGH ｜ 28D

📆 11-13 Forward Structure
存量OI: C 1.4k / P 1.2k，今日变化ΔOI: C +29 / P +0.3k，平值价格ATM: C $0.25 / P $1.15 ｜ ATM IV 97.5%，净 delta 敞口 -7k shares
Top ΔOI: P 9 +182
仓位参考: Max Pain 12 ｜ Call Wall 11.5（+9.8%，弱）（OI 0.1k） ｜ Put Wall 11（+5.1%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 97.5%｜历史 Rank 98%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 7,362 股

📆 11-20 Forward Structure
存量OI: C 4.3k / P 1.9k，今日变化ΔOI: C +11 / P +0.2k，平值价格ATM: C $0.60 / P $0.85 ｜ ATM IV 95.8%，净 delta 敞口 -10k shares
Top ΔOI: P 11 +187 ｜ P 10 +186
仓位参考: Max Pain 15 ｜ Put Wall 10（-4.5%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 95.8%｜历史 Rank 98%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 9,827 股

11-27（MEDIUM △）仓位参考: Max Pain 12

📆 12-04 Forward Structure
存量OI: C 0.1k / P 0.4k，今日变化ΔOI: C +17 / P +0.1k，平值价格ATM: C $0.00 / P $0.47 ｜ ATM IV 88.7%，净 delta 敞口 -4k shares
Top ΔOI: P 9 +140
仓位参考: Max Pain 14 ｜ Call Wall 10（-4.5%，弱）（OI 6） ｜ Put Wall 9.5（-9.3%）（OI 0.2k）
量化解读： 存量 Put 重｜ATM IV 88.7%｜历史 Rank 98%（近端代理）｜IV/RV 1.21×（近似）｜净 delta 敞口 负 4,223 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/NNE_morning.json