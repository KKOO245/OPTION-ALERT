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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-23 14P ΔOI +66（距现价 -4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 15.26 → 今开 15.40（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 15.46 ｜ 低 14.92

Options: P/C成交量 6.12 | OI比 0.34 | ATM IV 168.2% | Skew 2.1pp | Term 0.42 | ExpMove ±6.8%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.42，近月 IV 高于远月）｜保护溢价中性（Skew 2.1pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.34）+ 当日成交偏 Put（P/C量 6.12）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 6.12×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.34×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±6.8% ｜ 10-23（14D）±10.4% ｜ 10-30（21D）±16.0% ｜ 11-06（28D）±18.8%
   ⇒ IV–VIX Spread: +153.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 1,270,580 | GEX Change vs 上次快照 711,156 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 80%（带内） ｜ IV 有效性: VALID 142 / LOW 104 / INVALID 182
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 15（现价高于该位 1.0%）
最近结构参考: Put Wall 15（现价高于该位 1.0%）
量化视角： 正 Gamma（127万，无历史分位）｜正 Gamma 增强（+71万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall）；上方 16（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 14.5P — Vol 364 | 最新价 $0.40 | OI 79→424 (ΔOI +345张) | ΔOI/Volume 94.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增345张（+436.7% vs前日OI），连续性待观察（方向未知）
10-30 14.5C — Vol 93 | 最新价 $1.40 | OI 0→93 (ΔOI +93张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增93张（前日OI缺失），值得跟踪（方向未知）
10-16 17.0P — Vol 83 | 最新价 $1.95 | OI 650→724 (ΔOI +74张) | ΔOI/Volume 89.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增74张（+11.4% vs前日OI），连续性待观察（方向未知）
10-23 14.5P — Vol 71 | 最新价 $0.45 | OI 31→97 (ΔOI +66张) | ΔOI/Volume 93.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增66张（+212.9% vs前日OI），连续性待观察（方向未知）
10-23 17.0C — Vol 50 | 最新价 $0.26 | OI 94→144 (ΔOI +50张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增50张（+53.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 628 张（Put 485 / Call 143），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 7.8k / P 2.6k，今日成交量: C 32 / P 0.2k，平值价格ATM: C $0.35 / P $0.20 ｜ ATM IV 168.2%，预期波动 ±3.6%，Max Pain 16
Top ΔOI: P 17 -77 ｜ P 20 -61 ｜ C 16 -34

📆 Forward Expiration Structure

10-16  C +15 / P -0.2k ｜ Activity MEDIUM △ ｜ 7D
10-23  C +63 / P +63 ｜ Activity HIGH ｜ 14D
10-30  C +81 / P +52 ｜ Activity MEDIUM △ ｜ 21D
11-06  C +46 / P +55 ｜ Activity MEDIUM △ ｜ 28D

📆 10-16 Forward Structure
存量OI: C 21.8k / P 5.4k，今日变化ΔOI: C +15 / P -0.2k，平值价格ATM: C $0.45 / P $0.58 ｜ ATM IV 70.7%，净 delta 敞口 47k shares
Top ΔOI: P 14 +345 ｜ P 29 -337 ｜ P 25 -145
仓位参考: Max Pain 18 ｜ Put Wall 15（-1.0%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 70.7%｜历史 Rank 94%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 46,772 股

📆 10-23 Forward Structure
存量OI: C 5.1k / P 1.1k，今日变化ΔOI: C +63 / P +63，平值价格ATM: C $0.80 / P $0.77 ｜ ATM IV 68.4%，净 delta 敞口 -2k shares
Top ΔOI: P 14 +66 ｜ P 14 -58
仓位参考: Max Pain 17 ｜ Put Wall 14（-7.6%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 68.4%｜历史 Rank 94%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 负 1,717 股

10-30（MEDIUM △）Top ΔOI: 14C +93 ｜ 16P +30
10-30（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 14（-7.6%）（OI 0.3k）

11-06（MEDIUM △）Top ΔOI: 15P +41 ｜ 14C +21
11-06（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 15.5（+2.3%，弱）（OI 62）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/NNE_morning.json