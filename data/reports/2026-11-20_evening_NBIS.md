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


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 93.69 → 收盘 81.31（-13.2%） ｜ 今日高 93.97 ｜ 低 80.67 ｜ 昨收 96.92 → 收盘 81.31（-16.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-27，窗口结束前不做对错判定）

Options: P/C成交量 0.78 | OI比 0.35 | ATM IV 229.7% | Skew 32.6pp | Term 0.63 | ExpMove ±17.3%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.63，近月 IV 高于远月）｜保护溢价显著（Skew 32.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.35）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.35×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（7D）±17.3% ｜ 12-04（14D）±11.8% ｜ 12-11（21D）±27.8% ｜ 12-18（28D）±31.3%
   ⇒ IV–VIX Spread: +193.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,966,604 | GEX Change vs 上次快照 1,680,444 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 82%（带内） ｜ IV 有效性: VALID 359 / LOW 114 / INVALID 565
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
量化视角： 负 Gamma（597万，无历史分位）｜负 Gamma 缓解（+168万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 115（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 410.0P — Vol 2 | 最新价 $241.49 | OI 0→95 (ΔOI +95张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增95张（量数据缺失），以日内换手为主
12-18 290.0P — Vol 1 | 最新价 $70.05 | OI 0→5 (ΔOI +5张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增5张（量数据缺失），以日内换手为主
11-27 275.0P — Vol 0 | 最新价 $56.25 | OI 0→1 (ΔOI +1张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增1张（量数据缺失），以日内换手为主
量化视角： 3 个事件合计 ΔOI ≈ 101 张（Put 101 / Call 0），跨 2 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +8.6k / P -0.1k ｜ Activity HIGH ｜ 7D（新行权价 C 3.2k / P 1.2k）
12-04  C +2.2k / P +0.1k ｜ Activity HIGH ｜ 14D（新行权价 C 1.3k / P 0.5k）
12-11  C +0.7k / P +0.4k ｜ Activity HIGH ｜ 21D（新行权价 P 59）
12-18  C +2.8k / P -2.6k ｜ Activity MEDIUM △ ｜ 28D

📆 11-27 Forward Structure
存量OI: C 55.2k / P 20.5k，今日变化ΔOI: C +8.6k / P -0.1k（新行权价 C 3.2k / P 1.2k），平值价格ATM: C $7.20 / P $6.90 ｜ ATM IV 159.2%，净 delta 敞口 188k shares
Top ΔOI: C 110 +3,549
仓位参考: Max Pain 110 ｜ Put Wall 80（-1.6%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 159.2%｜历史 Rank 100%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 187,906 股

📆 12-04 Forward Structure
存量OI: C 18.9k / P 8.9k，今日变化ΔOI: C +2.2k / P +0.1k（新行权价 C 1.3k / P 0.5k），平值价格ATM: C $0.00 / P $9.55 ｜ ATM IV 152.2%，净 delta 敞口 34k shares
Top ΔOI: C 100 +411
仓位参考: Max Pain 115 ｜ Put Wall 80（-1.6%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 152.2%｜历史 Rank 100%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 34,116 股

📆 12-11 Forward Structure
存量OI: C 7.4k / P 9.0k，今日变化ΔOI: C +0.7k / P +0.4k（新行权价 P 59），平值价格ATM: C $11.85 / P $10.77 ｜ ATM IV 148.5%，净 delta 敞口 1k shares
Top ΔOI: P 85 +279 ｜ P 95 +139
仓位参考: Max Pain 130 ｜ Put Wall 85（+4.5%，弱）（OI 0.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 148.5%｜历史 Rank 100%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,428 股

12-18（MEDIUM △）Top ΔOI: 200P -1,364 ｜ 120C +1,341
12-18（MEDIUM △）仓位参考: Max Pain 155 ｜ Put Wall 80（-1.6%，弱）（OI 6.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/NBIS_evening.json