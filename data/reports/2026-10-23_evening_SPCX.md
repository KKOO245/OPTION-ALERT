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
🟡 **近现价集中开仓**: 10-28 148P ΔOI -3,008（距现价 +0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 147.93 → 收盘 147.49（-0.3%） ｜ 今日高 149.74 ｜ 低 144.09 ｜ 昨收 144.75 → 收盘 147.49（+1.9%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-30，窗口结束前不做对错判定）

Options: P/C成交量 0.74 | OI比 0.86 | ATM IV 89.2% | Skew -0.9pp | Term 0.59 | ExpMove ±3.0%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.59，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.74×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-26（3D）±3.0% ｜ 10-28（5D）±4.8% ｜ 10-30（7D）±5.9% ｜ 11-02（10D）±6.7%
   ⇒ IV–VIX Spread: +69.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -21,848,412 | GEX Change vs 上次快照 -3,044,763 | Flip: Primary Flip: 150.01（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 845 / LOW 167 / INVALID 464
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 150.01（全链重定价，覆盖 88%）
Put Wall 140（弱结构｜现价高于该位 5.4%） | Call Wall 160（弱结构｜现价低于该位 7.8%）
最近结构参考: Flip 150（现价低于该位 1.7%）
量化视角： 负 Gamma（2185万，无历史分位）｜负 Gamma 加深（304万）｜现价位于 Flip 下方 1.68%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（Put Wall，弱结构）；上方 150（MaxPain，仅结算参考） / 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 150（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-26  C +16.8k / P +17.9k ｜ Activity HIGH ｜ 3D
10-28  C +8.2k / P -1.1k ｜ Activity HIGH ｜ 5D
10-30  C +14.8k / P +8.4k ｜ Activity HIGH ｜ 7D
11-02  C +3.8k / P +0.9k ｜ Activity HIGH ｜ 10D

📆 10-26 Forward Structure
存量OI: C 41.7k / P 44.3k，今日变化ΔOI: C +16.8k / P +17.9k，平值价格ATM: C $2.45 / P $1.94 ｜ ATM IV 40.9%，净 delta 敞口 320k shares
Top ΔOI: P 140 +7,819 ｜ C 160 +4,455 ｜ P 138 +4,000
仓位参考: Max Pain 152 ｜ Call Wall 160（+8.5%，弱）（OI 6.3k） ｜ Put Wall 140（-5.1%）（OI 8.6k）
量化解读： 存量两侧均衡｜ATM IV 40.9%｜历史 Rank 96%（近端代理）｜IV/RV 0.63×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 319,522 股

📆 10-28 Forward Structure
存量OI: C 17.8k / P 20.1k，今日变化ΔOI: C +8.2k / P -1.1k，平值价格ATM: C $3.75 / P $3.35 ｜ ATM IV 50.1%，净 delta 敞口 511k shares
Top ΔOI: P 148 -3,008 ｜ P 160 -2,887 ｜ C 155 +1,507
仓位参考: Max Pain 155 ｜ Call Wall 160（+8.5%，弱）（OI 2.2k） ｜ Put Wall 160（+8.5%）（OI 3.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 50.1%｜历史 Rank 96%（近端代理）｜IV/RV 0.77×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 511,482 股

📆 10-30 Forward Structure
存量OI: C 166.3k / P 137.2k，今日变化ΔOI: C +14.8k / P +8.4k，平值价格ATM: C $4.65 / P $4.00 ｜ ATM IV 53.1%，净 delta 敞口 200k shares
Top ΔOI: C 155 +3,822 ｜ C 157 +3,706 ｜ P 144 +3,277
仓位参考: Max Pain 155 ｜ Call Wall 160（+8.5%，弱）（OI 10.3k） ｜ Put Wall 150（+1.7%）（OI 14.6k）
量化解读： 存量 Call 重｜ATM IV 53.1%｜历史 Rank 96%（近端代理）｜IV/RV 0.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 199,647 股

📆 11-02 Forward Structure
存量OI: C 8.9k / P 5.0k，今日变化ΔOI: C +3.8k / P +0.9k，平值价格ATM: C $4.88 / P $5.00 ｜ ATM IV 48.8%，净 delta 敞口 71k shares
Top ΔOI: C 155 +643 ｜ C 150 +544
仓位参考: Max Pain 150 ｜ Call Wall 160（+8.5%）（OI 1.3k） ｜ Put Wall 155（+5.1%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 48.8%｜历史 Rank 96%（近端代理）｜IV/RV 0.75×（近似）｜净 delta 敞口 正 71,365 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/SPCX_evening.json