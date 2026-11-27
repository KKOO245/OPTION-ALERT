# 期权晚报 2026-11-27（快照 16:40 ET）

📊 市场环境

SPY $728.32 ｜ QQQ $650.99
VIX 23.81 ↓11.2%（5D -33.7%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-30 420C ΔOI -5,716（距现价 +5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-30 260P ΔOI +10,067 占该期限总 OI 16.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 391.33 → 收盘 400.00（+2.2%） ｜ 今日高 401.18 ｜ 低 384.66 ｜ 昨收 380.14 → 收盘 400.00（+5.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.55 | OI比 1.52 | ATM IV 25.8% | Skew -0.2pp | Term 2.18 | ExpMove ±2.8%（近端） | Rank 2%
量化视角： IV 历史低位（Rank 2%，期权偏便宜）｜期限结构正常偏陡（Term 2.18）｜Put 保护异常便宜（Skew -0.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.52×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-30（3D）±2.8% ｜ 12-02（5D）±4.5% ｜ 12-04（7D）±0.0% ｜ 12-07（10D）±6.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 98,249,440 | GEX Change vs 上次快照 6,841,780 | Flip: Primary Flip: 367.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 1016 / LOW 212 / INVALID 1172
结构观察区: Primary Flip 367.41（全链重定价，覆盖 84%）
Call Wall 400（弱结构｜现价高于该位 0.0%）
最近结构参考: Call Wall 400（现价高于该位 0.0%）
量化视角： 正 Gamma（9825万，无历史分位）｜正 Gamma 增强（+684万）｜现价位于 Flip 上方 8.87%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 368（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 367（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-30  C +2.2k / P +18.6k ｜ Activity HIGH ｜ 3D
12-02  C +4.1k / P +3.0k ｜ Activity HIGH ｜ 5D
12-04  C +21.4k / P +30.5k ｜ Activity HIGH ｜ 7D
12-07  C +1.3k / P +0.6k ｜ Activity HIGH ｜ 10D

📆 11-30 Forward Structure
存量OI: C 28.9k / P 32.9k，今日变化ΔOI: C +2.2k / P +18.6k，平值价格ATM: C $5.60 / P $5.40 ｜ ATM IV 38.0%，净 delta 敞口 410k shares
Top ΔOI: C 420 -5,716
仓位参考: Max Pain 380 ｜ Call Wall 420（+5.0%）（OI 5.1k）
量化解读： 存量两侧均衡｜ATM IV 38.0%｜历史 Rank 2%（近端代理）｜IV/RV 0.52×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 409,938 股

📆 12-02 Forward Structure
存量OI: C 11.4k / P 11.3k，今日变化ΔOI: C +4.1k / P +3.0k，平值价格ATM: C $9.00 / P $8.80 ｜ ATM IV 47.4%，净 delta 敞口 234k shares
Top ΔOI: P 352 -2,401 ｜ C 395 +922
仓位参考: Max Pain 372 ｜ Call Wall 395（-1.2%，弱）（OI 1.5k） ｜ Put Wall 365（-8.8%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 47.4%｜历史 Rank 2%（近端代理）｜IV/RV 0.65×（近似）｜净 delta 敞口 正 234,326 股

📆 12-04 Forward Structure
存量OI: C 81.4k / P 88.7k，今日变化ΔOI: C +21.4k / P +30.5k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 65.6%，净 delta 敞口 1.1M shares
Top ΔOI: P 210 +10,050 ｜ C 392 +4,438
仓位参考: Max Pain 375 ｜ Call Wall 400（+0.0%，弱）（OI 7.3k）
量化解读： 存量两侧均衡｜ATM IV 65.6%｜历史 Rank 2%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,071,057 股

📆 12-07 Forward Structure
存量OI: C 3.7k / P 1.7k，今日变化ΔOI: C +1.3k / P +0.6k，平值价格ATM: C $13.15 / P $12.50 ｜ ATM IV 48.3%，净 delta 敞口 32k shares
Top ΔOI: P 365 +139
仓位参考: Max Pain 382 ｜ Call Wall 430（+7.5%，弱）（OI 0.3k） ｜ Put Wall 400（+0.0%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 48.3%｜历史 Rank 2%（近端代理）｜IV/RV 0.67×（近似）｜净 delta 敞口 正 31,650 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/TSLA_evening.json