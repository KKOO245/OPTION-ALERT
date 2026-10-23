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
🟡 **近现价集中开仓**: 10-26 50C ΔOI +960（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-28 50C ΔOI +2,252 占该期限总 OI 13.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 48.60 → 收盘 48.72（+0.3%） ｜ 今日高 48.97 ｜ 低 47.87 ｜ 昨收 49.34 → 收盘 48.72（-1.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-30，窗口结束前不做对错判定）

Options: P/C成交量 0.64 | OI比 0.44 | ATM IV 48.5% | Skew -16.2pp | Term 0.81 | ExpMove ±2.1%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜Put 保护异常便宜（Skew -16.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-26（3D）±2.1% ｜ 10-28（5D）±3.6% ｜ 10-30（7D）±4.4% ｜ 11-02（10D）±5.0%
   ⇒ IV–VIX Spread: +29.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,459,828 | GEX Change vs 上次快照 -4,815,051 | Flip: Primary Flip: 49.23（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 686 / LOW 105 / INVALID 409
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 49.23（全链重定价，覆盖 90%）
Put Wall 50（弱结构｜现价低于该位 2.6%）
最近结构参考: Flip 49（现价低于该位 1.0%）
量化视角： 负 Gamma（1046万，无历史分位）｜负 Gamma 加深（482万）｜现价位于 Flip 下方 1.04%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 50（Put Wall，弱结构） / 50（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 49（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-26  C +4.6k / P +5.2k ｜ Activity HIGH ｜ 3D
10-28  C +3.5k / P +2.8k ｜ Activity HIGH ｜ 5D
10-30  C +4.4k / P +32 ｜ Activity HIGH ｜ 7D
11-02  C +0.7k / P +0.3k ｜ Activity HIGH ｜ 10D

📆 10-26 Forward Structure
存量OI: C 12.0k / P 12.1k，今日变化ΔOI: C +4.6k / P +5.2k，平值价格ATM: C $0.62 / P $0.40 ｜ ATM IV 27.5%，净 delta 敞口 -41k shares
Top ΔOI: P 45 +1,002 ｜ C 50 +960
仓位参考: Max Pain 50 ｜ Call Wall 50.5（+3.7%）（OI 2.3k） ｜ Put Wall 48.5（-0.5%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜ATM IV 27.5%｜历史 Rank 81%（近端代理）｜IV/RV 0.75×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 40,648 股

📆 10-28 Forward Structure
存量OI: C 8.9k / P 8.2k，今日变化ΔOI: C +3.5k / P +2.8k，平值价格ATM: C $0.96 / P $0.78 ｜ ATM IV 39.1%，净 delta 敞口 12k shares
Top ΔOI: C 50 +2,252 ｜ P 44 +635 ｜ P 48 +441
仓位参考: Max Pain 50 ｜ Call Wall 50（+2.6%）（OI 2.4k） ｜ Put Wall 48（-1.5%）（OI 1.2k）
量化解读： 存量两侧均衡｜ATM IV 39.1%｜历史 Rank 81%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 12,396 股

📆 10-30 Forward Structure
存量OI: C 78.4k / P 29.2k，今日变化ΔOI: C +4.4k / P +32，平值价格ATM: C $1.21 / P $0.94 ｜ ATM IV 40.4%，净 delta 敞口 262k shares
Top ΔOI: C 50 +1,144
仓位参考: Max Pain 52 ｜ Call Wall 53.5（+9.8%，弱）（OI 1.6k） ｜ Put Wall 50（+2.6%，弱）（OI 3.5k）
量化解读： 存量 Call 重｜ATM IV 40.4%｜历史 Rank 81%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 262,013 股

📆 11-02 Forward Structure
存量OI: C 1.4k / P 0.9k，今日变化ΔOI: C +0.7k / P +0.3k，平值价格ATM: C $1.35 / P $1.07 ｜ ATM IV 37.0%，净 delta 敞口 6k shares
Top ΔOI: C 50 +330 ｜ C 50 +147
仓位参考: Max Pain 50 ｜ Call Wall 50.5（+3.7%）（OI 0.3k） ｜ Put Wall 46（-5.6%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 37.0%｜历史 Rank 81%（近端代理）｜IV/RV 1.00×（近似）｜净 delta 敞口 正 5,746 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/SLV_evening.json