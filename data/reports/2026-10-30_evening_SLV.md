# 期权晚报 2026-10-30（快照 16:40 ET）

📊 市场环境

SPY $755.72 ｜ QQQ $690.49
VIX 19.42 ↑12.9%（5D -0.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-04 46P ΔOI +286（距现价 +3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-09 43P ΔOI +646 占该期限总 OI 18.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 44.99 → 收盘 44.60（-0.9%） ｜ 今日高 45.06 ｜ 低 44.11 ｜ 昨收 47.28 → 收盘 44.60（-5.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-04，窗口结束前不做对错判定）

Options: P/C成交量 0.87 | OI比 0.37 | ATM IV 130.3% | Skew -19.4pp | Term 0.33 | ExpMove ±2.6%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.33，近月 IV 高于远月）｜Put 保护异常便宜（Skew -19.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.37）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.87×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.37×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-02（3D）±2.6% ｜ 11-04（5D）±4.3% ｜ 11-06（7D）±5.3% ｜ 11-09（10D）±6.4%
   ⇒ IV–VIX Spread: +110.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -28,899,534 | GEX Change vs 上次快照 3,957,405 | Flip: Primary Flip: 46.94（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 578 / LOW 114 / INVALID 468
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 46.94（全链重定价，覆盖 84%）
最近结构参考: Flip 47（现价低于该位 5.0%）
量化视角： 负 Gamma（2890万，无历史分位）｜负 Gamma 缓解（+396万）｜现价位于 Flip 下方 4.98%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 48（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 47（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-02  C +2.2k / P +1.2k ｜ Activity HIGH ｜ 3D
11-04  C +1.9k / P +1.4k ｜ Activity HIGH ｜ 5D
11-06  C +8.7k / P +2.3k ｜ Activity HIGH ｜ 7D
11-09  C +0.6k / P +0.9k ｜ Activity HIGH ｜ 10D

📆 11-02 Forward Structure
存量OI: C 10.1k / P 8.8k，今日变化ΔOI: C +2.2k / P +1.2k，平值价格ATM: C $0.63 / P $0.55 ｜ ATM IV 34.9%，净 delta 敞口 -62k shares
Top ΔOI: C 47 +885 ｜ C 48 +733 ｜ P 47 +298
仓位参考: Max Pain 48 ｜ Call Wall 49（+9.9%，弱）（OI 1.0k） ｜ Put Wall 47.5（+6.5%，弱）（OI 1.2k）
量化解读： 存量两侧均衡｜ATM IV 34.9%｜历史 Rank 99%（近端代理）｜IV/RV 0.92×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 62,413 股

📆 11-04 Forward Structure
存量OI: C 14.2k / P 7.4k，今日变化ΔOI: C +1.9k / P +1.4k，平值价格ATM: C $0.97 / P $0.93 ｜ ATM IV 44.9%，净 delta 敞口 -52k shares
Top ΔOI: C 48 +704 ｜ C 48 +333 ｜ P 46 +286
仓位参考: Max Pain 48 ｜ Call Wall 48.5（+8.7%，弱）（OI 1.0k） ｜ Put Wall 44（-1.3%）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 44.9%｜历史 Rank 99%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 51,788 股

📆 11-06 Forward Structure
存量OI: C 118.3k / P 31.9k，今日变化ΔOI: C +8.7k / P +2.3k，平值价格ATM: C $1.20 / P $1.15 ｜ ATM IV 46.8%，净 delta 敞口 68k shares
仓位参考: Max Pain 50 ｜ Put Wall 43（-3.6%，弱）（OI 3.5k）
量化解读： 存量 Call 重｜ATM IV 46.8%｜历史 Rank 99%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 67,966 股

📆 11-09 Forward Structure
存量OI: C 1.8k / P 1.7k，今日变化ΔOI: C +0.6k / P +0.9k，平值价格ATM: C $1.35 / P $1.50 ｜ ATM IV 43.5%，净 delta 敞口 -24k shares
Top ΔOI: P 43 +646 ｜ C 47 +284 ｜ P 47 +195
仓位参考: Max Pain 47 ｜ Call Wall 47（+5.4%，弱）（OI 0.3k） ｜ Put Wall 43（-3.6%）（OI 0.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 43.5%｜历史 Rank 99%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 负 23,511 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/SLV_evening.json