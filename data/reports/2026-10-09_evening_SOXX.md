# 期权晚报 2026-10-09（快照 16:40 ET）

📊 市场环境

SPY $778.57 ｜ QQQ $751.27
VIX 14.84 ↓3.7%（5D -3.1%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 45.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 46.3 ｜ 前值 48.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 555P ΔOI +714（距现价 -0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-23 500P ΔOI +1,248 占该期限总 OI 11.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 570.69 → 收盘 559.40（-2.0%） ｜ 今日高 571.34 ｜ 低 557.27 ｜ 昨收 563.28 → 收盘 559.40（-0.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-14，窗口结束前不做对错判定）

Options: P/C成交量 0.42 | OI比 1.84 | ATM IV 77.4% | Skew 9.7pp | Term 0.48 | ExpMove ±3.7%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.48，近月 IV 高于远月）｜保护溢价显著（Skew 9.7pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.84×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±3.7% ｜ 10-23（14D）±5.3% ｜ 10-30（21D）±6.8% ｜ 11-06（28D）±8.5%
   ⇒ IV–VIX Spread: +62.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -11,087,824 | GEX Change vs 上次快照 3,353,272 | Flip: Primary Flip: 575.74（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 551 / LOW 243 / INVALID 752
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 575.74（全链重定价，覆盖 90%）
最近结构参考: Flip 576（现价低于该位 2.8%）
量化视角： 负 Gamma（1109万，无历史分位）｜负 Gamma 缓解（+335万）｜现价位于 Flip 下方 2.84%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 560（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 576（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C -0.4k / P +3.9k ｜ Activity HIGH ｜ 7D
10-23  C +0.2k / P +2.5k ｜ Activity HIGH ｜ 14D
10-30  C +5 / P +7.0k ｜ Activity HIGH ｜ 21D
11-06  C +0.1k / P +0.1k ｜ Activity HIGH ｜ 28D

📆 10-16 Forward Structure
存量OI: C 37.5k / P 104.7k，今日变化ΔOI: C -0.4k / P +3.9k，平值价格ATM: C $10.10 / P $10.82 ｜ ATM IV 33.9%，净 delta 敞口 -28k shares
仓位参考: Max Pain 535 ｜ Call Wall 550（-1.7%，弱）（OI 2.2k） ｜ Put Wall 530（-5.3%，弱）（OI 4.8k）
量化解读： 存量 Put 重｜ATM IV 33.9%｜历史 Rank 98%（近端代理）｜IV/RV 1.13×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 27,846 股

📆 10-23 Forward Structure
存量OI: C 1.6k / P 9.1k，今日变化ΔOI: C +0.2k / P +2.5k，平值价格ATM: C $15.29 / P $14.50 ｜ ATM IV 34.4%，净 delta 敞口 -49k shares
Top ΔOI: P 500 +1,248 ｜ P 555 +714 ｜ P 560 +180
仓位参考: Max Pain 560 ｜ Call Wall 525（-6.1%，弱）（OI 0.1k） ｜ Put Wall 555（-0.8%，弱）（OI 0.8k）
量化解读： 存量 Put 重｜ATM IV 34.4%｜历史 Rank 98%（近端代理）｜IV/RV 1.14×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 48,503 股

📆 10-30 Forward Structure
存量OI: C 6.0k / P 27.5k，今日变化ΔOI: C +5 / P +7.0k，平值价格ATM: C $19.22 / P $18.70 ｜ ATM IV 36.0%，净 delta 敞口 -87k shares
Top ΔOI: P 485 +3,503 ｜ P 480 +2,973 ｜ P 567 +425
仓位参考: Max Pain 568 ｜ Put Wall 550（-1.7%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜ATM IV 36.0%｜历史 Rank 98%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 负 87,141 股

📆 11-06 Forward Structure
存量OI: C 0.8k / P 1.4k，今日变化ΔOI: C +0.1k / P +0.1k，平值价格ATM: C $24.80 / P $22.50 ｜ ATM IV 37.5%，净 delta 敞口 -359 shares
Top ΔOI: C 567 +93 ｜ P 600 +30
仓位参考: Max Pain 568 ｜ Call Wall 567.5（+1.4%）（OI 0.2k） ｜ Put Wall 592.5（+5.9%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 37.5%｜历史 Rank 98%（近端代理）｜IV/RV 1.24×（近似）｜净 delta 敞口 负 359 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/SOXX_evening.json