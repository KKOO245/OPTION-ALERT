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
🟡 **近现价集中开仓**: 11-27 141P ΔOI +204（距现价 +0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-04 141P ΔOI +2,166 占该期限总 OI 53.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 142.88 → 收盘 140.18（-1.9%） ｜ 今日高 145.48 ｜ 低 139.87 ｜ 昨收 144.12 → 收盘 140.18（-2.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-25，窗口结束前不做对错判定）

Options: P/C成交量 0.60 | OI比 1.32 | ATM IV 65.5% | Skew -7.2pp | Term 0.56 | ExpMove ±6.9%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.56，近月 IV 高于远月）｜Put 保护异常便宜（Skew -7.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.32×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-27（7D）±6.9% ｜ 12-04（14D）±9.0% ｜ 12-11（21D）±2.5% ｜ 12-18（28D）±9.3%
   ⇒ IV–VIX Spread: +29.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -36,450,119 | GEX Change vs 上次快照 6,068,777 | Flip: Primary Flip: 147.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 376 / LOW 195 / INVALID 369
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 147.56（全链重定价，覆盖 90%）
最近结构参考: Flip 148（现价低于该位 5.0%）
量化视角： 负 Gamma（3645万，无历史分位）｜负 Gamma 缓解（+607万）｜现价位于 Flip 下方 5.00%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 149（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 148（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 174.0P — Vol 18 | 最新价 $18.05 | OI 86→105 (ΔOI +19张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增19张（+22.1% vs前日OI），值得跟踪（方向未知）
12-18 180.0P — Vol 1 | 最新价 $32.57 | OI 0→10 (ΔOI +10张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增10张（量数据缺失），以日内换手为主
量化视角： 2 个事件合计 ΔOI ≈ 29 张（Put 29 / Call 0），跨 1 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +0.6k / P +0.2k ｜ Activity HIGH ｜ 7D（新行权价 C 0.5k / P 5）
12-04  C +8 / P +2.5k ｜ Activity HIGH ｜ 14D（新行权价 C 0.1k / P 10）
12-11  C +0 / P +64 ｜ Activity HIGH ｜ 21D（新行权价 C 0.4k / P 37）
12-18  C +2.3k / P +32.3k ｜ Activity HIGH ｜ 28D

📆 11-27 Forward Structure
存量OI: C 3.2k / P 5.5k，今日变化ΔOI: C +0.6k / P +0.2k（新行权价 C 0.5k / P 5），平值价格ATM: C $8.44 / P $1.22 ｜ ATM IV 38.0%，净 delta 敞口 6k shares
Top ΔOI: C 151 +369 ｜ P 141 +204 ｜ P 135 -109
仓位参考: Max Pain 150 ｜ Call Wall 135（-3.7%，弱）（OI 0.2k） ｜ Put Wall 143（+2.0%，弱）（OI 1.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 38.0%｜历史 Rank 99%（近端代理）｜IV/RV 1.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 6,153 股

📆 12-04 Forward Structure
存量OI: C 0.5k / P 3.5k，今日变化ΔOI: C +8 / P +2.5k（新行权价 C 0.1k / P 10），平值价格ATM: C $9.85 / P $2.80 ｜ ATM IV 42.4%，净 delta 敞口 -90k shares
Top ΔOI: P 141 +2,166 ｜ P 135 +200 ｜ P 145 +192
仓位参考: Max Pain 156 ｜ Call Wall 144（+2.7%，弱）（OI 50） ｜ Put Wall 141（+0.6%）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 42.4%｜历史 Rank 99%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 89,528 股

📆 12-11 Forward Structure
存量OI: C 0.8k / P 1.1k，今日变化ΔOI: C +0 / P +64（新行权价 C 0.4k / P 37），平值价格ATM: C $0.00 / P $3.58 ｜ ATM IV 39.1%，净 delta 敞口 -2k shares
Top ΔOI: P 136 +40 ｜ P 141 +23 ｜ P 152 +1
仓位参考: Max Pain 147 ｜ Call Wall 147（+4.9%）（OI 0.4k） ｜ Put Wall 135（-3.7%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 39.1%｜历史 Rank 99%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,952 股

📆 12-18 Forward Structure
存量OI: C 160.9k / P 119.1k，今日变化ΔOI: C +2.3k / P +32.3k，平值价格ATM: C $8.95 / P $4.16 ｜ ATM IV 36.7%，净 delta 敞口 502k shares
Top ΔOI: P 35 +35,536 ｜ P 70 +3,839 ｜ P 133 -3,143
仓位参考: Max Pain 135 ｜ Call Wall 135（-3.7%，弱）（OI 11.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 36.7%｜历史 Rank 99%（近端代理）｜IV/RV 0.98×（近似）｜净 delta 敞口 正 502,161 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/XBI_evening.json