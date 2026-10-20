# 期权晚报 2026-10-20（快照 16:40 ET）

📊 市场环境

SPY $769.05 ｜ QQQ $717.63
VIX 17.31 ↓6.1%（5D +13.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 10-23（3D）ATM IV 104.4% vs 10-30 64.9%（差 +39.5pp），覆盖 建筑许可 Prel、新屋开工
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-23 435C ΔOI +539（距现价 -0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-23 475C ΔOI +1,028 占该期限总 OI 10.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 433.50 → 收盘 438.00（+1.0%） ｜ 今日高 440.40 ｜ 低 432.00 ｜ 昨收 433.18 → 收盘 438.00（+1.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-27，窗口结束前不做对错判定）

Options: P/C成交量 1.22 | OI比 0.89 | ATM IV 104.4% | Skew 0.1pp | Term 0.43 | ExpMove ±7.5%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.43，近月 IV 高于远月）｜保护溢价薄（Skew 0.1pp）｜当日成交偏 Put（P/C量 1.22）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.22×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.89×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（3D）±7.5% ｜ 10-30（10D）±8.7% ｜ 11-06（17D）±9.4% ｜ 11-13（24D）±10.6%
   ⇒ IV–VIX Spread: +87.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,076,774 | GEX Change vs 上次快照 193,407 | Flip: Primary Flip: 403.79（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 395 / LOW 87 / INVALID 484
结构观察区: Primary Flip 403.79（全链重定价，覆盖 100%）
Call Wall 475（弱结构｜现价低于该位 7.8%）
最近结构参考: Call Wall 475（现价低于该位 7.8%）
量化视角： 正 Gamma（208万，无历史分位）｜正 Gamma 增强（+19万）｜现价位于 Flip 上方 8.47%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 420（MaxPain，仅结算参考）；上方 475（Call Wall，弱结构）。
• Gamma 区域：切换参考 404（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +2.4k / P +2.7k ｜ Activity HIGH ｜ 3D
10-30  C +78 / P +80 ｜ Activity MEDIUM △ ｜ 10D
11-06  C +57 / P +36 ｜ Activity HIGH ｜ 17D
11-13  C +40 / P +0.2k ｜ Activity MEDIUM △ ｜ 24D

📆 10-23 Forward Structure
存量OI: C 5.4k / P 4.8k，今日变化ΔOI: C +2.4k / P +2.7k，平值价格ATM: C $16.63 / P $16.00 ｜ ATM IV 104.4%，净 delta 敞口 32k shares
Top ΔOI: C 475 +1,028 ｜ C 435 +539
仓位参考: Max Pain 420 ｜ Call Wall 475（+8.4%）（OI 1.1k） ｜ Put Wall 415（-5.3%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 104.4%｜历史 Rank 100%（近端代理）｜IV/RV 4.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 31,505 股

10-30（MEDIUM △）Top ΔOI: 440C +17 ｜ 450C +13
10-30（MEDIUM △）仓位参考: Max Pain 405 ｜ Call Wall 460（+5.0%，弱）（OI 0.1k） ｜ Put Wall 410（-6.4%，弱）（OI 66）

📆 11-06 Forward Structure
存量OI: C 0.4k / P 0.4k，今日变化ΔOI: C +57 / P +36，平值价格ATM: C $21.01 / P $20.00 ｜ ATM IV 56.0%，净 delta 敞口 1k shares
Top ΔOI: P 407 +20
仓位参考: Max Pain 420 ｜ Call Wall 455（+3.9%，弱）（OI 54） ｜ Put Wall 450（+2.7%，弱）（OI 64）
量化解读： 存量两侧均衡｜ATM IV 56.0%｜历史 Rank 100%（近端代理）｜IV/RV 2.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,009 股

11-13（MEDIUM △）Top ΔOI: 420P +68 ｜ 475C +15
11-13（MEDIUM △）仓位参考: Max Pain 420 ｜ Call Wall 475（+8.4%，弱）（OI 47） ｜ Put Wall 420（-4.1%，弱）（OI 68）

📅 事件差分（观察，非因果）: 10-23（3D）ATM IV 104.4% vs 10-30 64.9%（差 +39.5pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/ISRG_evening.json