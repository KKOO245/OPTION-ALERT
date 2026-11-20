# 期权晚报 2026-11-20（快照 16:40 ET）

📊 市场环境

SPY $689.81 ｜ QQQ $608.45
VIX 35.89 ↑26.2%（5D +86.0%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 9.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 9.62 → 收盘 9.10（-5.5%） ｜ 今日高 10.09 ｜ 低 8.97 ｜ 昨收 9.97 → 收盘 9.10（-8.7%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-27，窗口结束前不做对错判定）

Options: P/C成交量 0.36 | OI比 0.24 | ATM IV 280.1% | Skew 19.6pp | Term 0.31 | ExpMove ±15.8%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.31，近月 IV 高于远月）｜保护溢价显著（Skew 19.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.24）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.24×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（7D）±15.8% ｜ 12-04（14D）±19.3% ｜ 12-11（21D）±37.4% ｜ 12-18（28D）±36.8%
   ⇒ IV–VIX Spread: +244.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 397,206 | GEX Change vs 上次快照 48,037 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 96 / LOW 63 / INVALID 211
结构观察区: NO_CROSS
Put Wall 10（弱结构｜现价低于该位 9.0%）
最近结构参考: Put Wall 10（现价低于该位 9.0%）
量化视角： 正 Gamma（40万，无历史分位）｜正 Gamma 增强（+5万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（Put Wall，弱结构） / 12（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C -4 / P -7 ｜ Activity LOW ｜ 7D（新行权价 C 12 / P 1）
12-04  C +42 / P +16 ｜ Activity LOW ｜ 14D（新行权价 C 0.2k / P 2）
12-11  C +31 / P +0 ｜ Activity LOW ｜ 21D（新行权价 P 5）
12-18  C -2 / P +0.1k ｜ Activity MEDIUM △ ｜ 28D（新行权价 P 1）

📆 11-27 Forward Structure
存量OI: C 5.0k / P 0.8k，今日变化ΔOI: C -4 / P -7（新行权价 C 12 / P 1），平值价格ATM: C $1.17 / P $0.27 ｜ ATM IV 86.4%，净 delta 敞口 2k shares
Top ΔOI: P 9 +11
仓位参考: Max Pain 12 ｜ Put Wall 10（+9.9%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 86.4%｜历史 Rank 100%（近端代理）｜IV/RV 0.91×（近似）｜净 delta 敞口 正 1,968 股

12-04（Activity LOW）仓位参考: Max Pain 11 ｜ Put Wall 9.5（+4.4%）（OI 0.2k）

12-11（Activity LOW）仓位参考: Max Pain 11 ｜ Call Wall 10（+9.9%，弱）（OI 34） ｜ Put Wall 9（-1.1%，弱）（OI 8）

12-18（MEDIUM △）Top ΔOI: 9P +143
12-18（MEDIUM △）仓位参考: Max Pain 11 ｜ Call Wall 10（+9.9%，弱）（OI 60） ｜ Put Wall 9（-1.1%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/NNE_evening.json