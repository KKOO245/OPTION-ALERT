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
🟡 **近现价集中开仓**: 10-26 83P ΔOI +1,518（距现价 +3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-26 83P ΔOI +1,518 占该期限总 OI 16.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 81.16 → 收盘 80.20（-1.2%） ｜ 今日高 81.61 ｜ 低 78.92 ｜ 昨收 81.69 → 收盘 80.20（-1.8%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-28，窗口结束前不做对错判定）

Options: P/C成交量 0.54 | OI比 0.37 | ATM IV 84.3% | Skew 16.6pp | Term 0.50 | ExpMove ±2.1%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.50，近月 IV 高于远月）｜保护溢价显著（Skew 16.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.37）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.37×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-26（3D）±2.1% ｜ 10-28（5D）±3.6% ｜ 10-30（7D）±4.4% ｜ 11-02（10D）±5.6%
   ⇒ IV–VIX Spread: +64.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -17,707,093 | GEX Change vs 上次快照 -2,841,843 | Flip: Primary Flip: 82.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 499 / LOW 147 / INVALID 512
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 82.52（全链重定价，覆盖 86%）
Put Wall 80（弱结构｜现价高于该位 0.2%）
最近结构参考: Put Wall 80（现价高于该位 0.2%）
量化视角： 负 Gamma（1771万，无历史分位）｜负 Gamma 加深（284万）｜现价位于 Flip 下方 2.81%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（Put Wall，弱结构）；上方 85（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 83（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-26  C +0.1k / P +2.5k ｜ Activity HIGH ｜ 3D
10-28  C +0.1k / P +1.0k ｜ Activity HIGH ｜ 5D
10-30  C +34.7k / P +9.5k ｜ Activity HIGH ｜ 7D
11-02  C +85 / P +19 ｜ Activity HIGH ｜ 10D

📆 10-26 Forward Structure
存量OI: C 4.9k / P 4.2k，今日变化ΔOI: C +0.1k / P +2.5k，平值价格ATM: C $0.97 / P $0.72 ｜ ATM IV 29.8%，净 delta 敞口 -188k shares
Top ΔOI: P 83 +1,518 ｜ P 81 +928 ｜ P 80 +117
仓位参考: Max Pain 86 ｜ Put Wall 83（+3.5%）（OI 1.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 29.8%｜历史 Rank 100%（近端代理）｜IV/RV 0.81×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 187,904 股

📆 10-28 Forward Structure
存量OI: C 1.1k / P 4.4k，今日变化ΔOI: C +0.1k / P +1.0k，平值价格ATM: C $1.65 / P $1.24 ｜ ATM IV 40.0%，净 delta 敞口 -9k shares
Top ΔOI: P 75 +924 ｜ C 87 +76 ｜ C 86 +66
仓位参考: Max Pain 87 ｜ Put Wall 84（+4.7%）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 40.0%｜历史 Rank 100%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 9,333 股

📆 10-30 Forward Structure
存量OI: C 74.8k / P 28.5k，今日变化ΔOI: C +34.7k / P +9.5k，平值价格ATM: C $1.98 / P $1.52 ｜ ATM IV 41.4%，净 delta 敞口 264k shares
Top ΔOI: C 85 +10,925 ｜ C 84 +7,106
仓位参考: Max Pain 84 ｜ Call Wall 85（+6.0%，弱）（OI 11.2k） ｜ Put Wall 75（-6.5%）（OI 10.0k）
量化解读： 存量 Call 重｜ATM IV 41.4%｜历史 Rank 100%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 263,589 股

📆 11-02 Forward Structure
存量OI: C 0.3k / P 0.3k，今日变化ΔOI: C +85 / P +19，平值价格ATM: C $2.52 / P $1.98 ｜ ATM IV 39.5%，净 delta 敞口 302 shares
Top ΔOI: P 85 +10 ｜ C 87 +8
仓位参考: Max Pain 88
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 39.5%｜历史 Rank 100%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 正 302 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/GDX_evening.json