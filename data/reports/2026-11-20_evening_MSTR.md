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

🔍 重点速览
🟡 **近现价集中开仓**: 11-27 80P ΔOI +1,992（距现价 +2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 86.45 → 收盘 77.80（-10.0%） ｜ 今日高 87.95 ｜ 低 77.69 ｜ 昨收 86.13 → 收盘 77.80（-9.7%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-27，窗口结束前不做对错判定）

Options: P/C成交量 1.52 | OI比 0.48 | ATM IV 154.3% | Skew 20.1pp | Term 0.74 | ExpMove ±14.6%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价显著（Skew 20.1pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.48）+ 当日成交偏 Put（P/C量 1.52）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.52×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.48×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（7D）±14.6% ｜ 12-04（14D）±18.9% ｜ 12-11（21D）±22.9% ｜ 12-18（28D）±25.4%
   ⇒ IV–VIX Spread: +118.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -22,332,640 | GEX Change vs 上次快照 4,752,698 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 83%（带内） ｜ IV 有效性: VALID 414 / LOW 194 / INVALID 532
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
量化视角： 负 Gamma（2233万，无历史分位）｜负 Gamma 缓解（+475万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 96（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 1080.0P — Vol 20 | 最新价 $695.05 | OI 0→106 (ΔOI +106张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增106张（量数据缺失），以日内换手为主
12-18 1060.0P — Vol 2 | 最新价 $675.26 | OI 0→32 (ΔOI +32张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增32张（量数据缺失），以日内换手为主
12-18 1040.0P — Vol 4 | 最新价 $678.28 | OI 0→27 (ΔOI +27张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增27张（量数据缺失），以日内换手为主
12-18 840.0P — Vol 3 | 最新价 $473.23 | OI 0→16 (ΔOI +16张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增16张（量数据缺失），以日内换手为主
12-18 820.0P — Vol 1 | 最新价 $449.40 | OI 0→10 (ΔOI +10张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增10张（量数据缺失），以日内换手为主
量化视角： 5 个事件合计 ΔOI ≈ 191 张（Put 191 / Call 0），跨 1 个期限｜有实质成本保护 5 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +4.6k / P +1.8k ｜ Activity MEDIUM △ ｜ 7D（新行权价 C 91.5k / P 36.3k）
12-04  C +1.5k / P -2.4k ｜ Activity HIGH ｜ 14D（新行权价 C 6.5k / P 8.5k）
12-11  C +1.1k / P -32 ｜ Activity HIGH ｜ 21D（新行权价 C 0.1k / P 11）
12-18  C +3.1k / P -1.6k ｜ Activity MEDIUM △ ｜ 28D

📆 11-27 Forward Structure
存量OI: C 146.8k / P 118.4k，今日变化ΔOI: C +4.6k / P +1.8k（新行权价 C 91.5k / P 36.3k），平值价格ATM: C $5.60 / P $5.75 ｜ ATM IV 132.7%，净 delta 敞口 257k shares
Top ΔOI: P 80 +1,992 ｜ C 90 +1,292
仓位参考: Max Pain 93 ｜ Put Wall 80（+2.8%，弱）（OI 8.2k）
量化解读： 存量 Call 重｜ATM IV 132.7%｜历史 Rank 97%（近端代理）｜IV/RV 1.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 256,648 股

📆 12-04 Forward Structure
存量OI: C 26.4k / P 58.8k，今日变化ΔOI: C +1.5k / P -2.4k（新行权价 C 6.5k / P 8.5k），平值价格ATM: C $7.50 / P $7.20 ｜ ATM IV 127.1%，净 delta 敞口 453k shares
Top ΔOI: P 135 -2,025 ｜ P 140 -1,978 ｜ P 130 -931
仓位参考: Max Pain 105 ｜ Put Wall 85（+9.3%，弱）（OI 6.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 127.1%｜历史 Rank 97%（近端代理）｜IV/RV 1.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 453,420 股

📆 12-11 Forward Structure
存量OI: C 8.9k / P 37.6k，今日变化ΔOI: C +1.1k / P -32（新行权价 C 0.1k / P 11），平值价格ATM: C $8.08 / P $9.75 ｜ ATM IV 117.0%，净 delta 敞口 152k shares
Top ΔOI: P 60 +984 ｜ P 145 -825 ｜ P 150 -708
仓位参考: Max Pain 130 ｜ Put Wall 80（+2.8%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 117.0%｜历史 Rank 97%（近端代理）｜IV/RV 1.75×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 151,554 股

12-18（MEDIUM △）Top ΔOI: 55P +3,000 ｜ 155P -2,663
12-18（MEDIUM △）仓位参考: Max Pain 135 ｜ Put Wall 80（+2.8%，弱）（OI 9.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/MSTR_evening.json