# 期权晚报 2026-10-23（快照 16:40 ET）

📊 市场环境

SPY $759.97 ｜ QQQ $704.40
VIX 19.45 ↑2.2%（5D -2.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 21.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 12.40 → 收盘 12.16（-1.9%） ｜ 今日高 12.45 ｜ 低 11.95 ｜ 昨收 12.53 → 收盘 12.16（-3.0%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-30，窗口结束前不做对错判定）

Options: P/C成交量 1.24 | OI比 0.14 | ATM IV 129.2% | Skew 39.8pp | Term 0.63 | ExpMove ±7.2%（近端） | Rank 75%
量化视角： IV 中性（Rank 75%）｜期限结构倒挂（Term 0.63，近月 IV 高于远月）｜保护溢价显著（Skew 39.8pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.14）+ 当日成交偏 Put（P/C量 1.24）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.24×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.14×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（7D）±7.2% ｜ 11-06（14D）±17.5% ｜ 11-13（21D）±3.3% ｜ 11-20（28D）±31.1%
   ⇒ IV–VIX Spread: +109.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 695,852 | GEX Change vs 上次快照 -63,552 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 107 / LOW 82 / INVALID 217
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
量化视角： 正 Gamma（70万，无历史分位）｜正 Gamma 减弱（6万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +31 / P +0.1k ｜ Activity MEDIUM △ ｜ 7D
11-06  C +0 / P +45 ｜ Activity LOW ｜ 14D
11-13  C +4 / P +5 ｜ Activity LOW ｜ 21D
11-20  C +24 / P +14 ｜ Activity MEDIUM △ ｜ 28D

📆 10-30 Forward Structure
存量OI: C 7.1k / P 1.5k，今日变化ΔOI: C +31 / P +0.1k，平值价格ATM: C $0.49 / P $0.38 ｜ ATM IV 74.9%，净 delta 敞口 -828 shares
Top ΔOI: P 12 +159 ｜ C 13 +27
仓位参考: Max Pain 14 ｜ Put Wall 12（-1.3%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 74.9%｜历史 Rank 75%（近端代理）｜IV/RV 1.22×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 828 股

11-06（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 13（+6.9%，弱）（OI 78）

11-13（Activity LOW）仓位参考: Max Pain 14 ｜ Put Wall 13（+6.9%，弱）（OI 70）

11-20（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 12（-1.3%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/NNE_evening.json