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
🟡 **近现价集中开仓**: 12-02 155C ΔOI +8,751（距现价 +3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 151.94 → 收盘 150.49（-1.0%） ｜ 今日高 151.98 ｜ 低 145.39 ｜ 昨收 149.30 → 收盘 150.49（+0.8%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-04，窗口结束前不做对错判定）

Options: P/C成交量 0.64 | OI比 0.68 | ATM IV 71.3% | Skew -8.0pp | Term 1.01 | ExpMove ±4.1%（近端） | Rank 89%
量化视角： IV 历史高位（Rank 89%，期权偏贵）｜期限结构正常（Term 1.01）｜Put 保护异常便宜（Skew -8.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-30（3D）±4.1% ｜ 12-02（5D）±7.4% ｜ 12-04（7D）±0.0% ｜ 12-07（10D）±9.9%
   ⇒ IV–VIX Spread: +47.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 108,175,800 | GEX Change vs 上次快照 8,995,319 | Flip: Primary Flip: 143.26（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 1210 / LOW 231 / INVALID 1131
结构观察区: Primary Flip 143.26（全链重定价，覆盖 89%）
最近结构参考: Flip 143（现价高于该位 5.0%）
量化视角： 正 Gamma（1.08亿，无历史分位）｜正 Gamma 增强（+900万）｜现价位于 Flip 上方 5.04%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 143（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-30  C +33.5k / P +39.6k ｜ Activity HIGH ｜ 3D
12-02  C +13.4k / P +9.7k ｜ Activity HIGH ｜ 5D
12-04  C +111.0k / P +70.9k ｜ Activity HIGH ｜ 7D
12-07  C +5.3k / P +2.7k ｜ Activity HIGH ｜ 10D

📆 11-30 Forward Structure
存量OI: C 139.9k / P 109.1k，今日变化ΔOI: C +33.5k / P +39.6k，平值价格ATM: C $3.20 / P $3.00 ｜ ATM IV 58.2%，净 delta 敞口 246k shares
Top ΔOI: C 160 +5,590 ｜ P 128 +5,018
仓位参考: Max Pain 150 ｜ Call Wall 160（+6.3%，弱）（OI 10.7k） ｜ Put Wall 140（-7.0%，弱）（OI 6.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 58.2%｜历史 Rank 89%（近端代理）｜IV/RV 0.46×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 246,152 股

📆 12-02 Forward Structure
存量OI: C 80.7k / P 33.4k，今日变化ΔOI: C +13.4k / P +9.7k，平值价格ATM: C $5.80 / P $5.32 ｜ ATM IV 77.7%，净 delta 敞口 361k shares
Top ΔOI: C 155 +8,751 ｜ C 167 -7,693 ｜ C 160 +2,482
仓位参考: Max Pain 152 ｜ Call Wall 155（+3.0%，弱）（OI 10.4k） ｜ Put Wall 145（-3.6%，弱）（OI 3.4k）
量化解读： 存量 Call 重｜ATM IV 77.7%｜历史 Rank 89%（近端代理）｜IV/RV 0.61×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 360,723 股

📆 12-04 Forward Structure
存量OI: C 385.0k / P 250.7k，今日变化ΔOI: C +111.0k / P +70.9k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 85.1%，净 delta 敞口 4.4M shares
Top ΔOI: C 152 +23,677 ｜ C 160 +23,162
仓位参考: Max Pain 150 ｜ Call Wall 160（+6.3%）（OI 39.3k） ｜ Put Wall 160（+6.3%，弱）（OI 10.5k）
量化解读： 存量 Call 重｜ATM IV 85.1%｜历史 Rank 89%（近端代理）｜IV/RV 0.67×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,425,424 股

📆 12-07 Forward Structure
存量OI: C 22.3k / P 8.8k，今日变化ΔOI: C +5.3k / P +2.7k，平值价格ATM: C $7.60 / P $7.38 ｜ ATM IV 75.9%，净 delta 敞口 199k shares
Top ΔOI: C 160 +867 ｜ C 155 +699
仓位参考: Max Pain 150 ｜ Call Wall 160（+6.3%，弱）（OI 2.3k） ｜ Put Wall 150（-0.3%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 75.9%｜历史 Rank 89%（近端代理）｜IV/RV 0.60×（近似）｜净 delta 敞口 正 198,623 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/NVDA_evening.json