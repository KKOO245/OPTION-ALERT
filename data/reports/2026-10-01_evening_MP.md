# 期权晚报 2026-10-01（快照 16:40 ET）

📊 市场环境

SPY $763.99 ｜ QQQ $742.03
VIX 16.39 ↑0.3%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-01

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 54.5 ｜ 前值 54.6　✅ 今日已公布
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 47P ΔOI +1,046（距现价 +2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 46.51 → 收盘 46.09（-0.9%） ｜ 今日高 46.89 ｜ 低 44.49 ｜ 昨收 47.29 → 收盘 46.09（-2.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-06，窗口结束前不做对错判定）

Options: P/C成交量 0.99 | OI比 0.68 | ATM IV 57.0% | Skew -5.3pp | Term 0.97 | ExpMove ±2.5%（近端） | Rank 30%
量化视角： IV 中性（Rank 30%）｜期限结构正常（Term 0.97）｜Put 保护异常便宜（Skew -5.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.99×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±2.5% ｜ 10-09（8D）±6.6% ｜ 10-16（15D）±9.4% ｜ 10-23（22D）±10.4%
   ⇒ IV–VIX Spread: +40.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,528,975 | GEX Change vs 上次快照 58,995 | Flip: Primary Flip: 47.66（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 298 / LOW 68 / INVALID 90
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 47.66（全链重定价，覆盖 96%）
Put Wall 45（弱结构｜现价高于该位 2.4%） | Call Wall 50（弱结构｜现价低于该位 7.8%）
最近结构参考: Put Wall 45（现价高于该位 2.4%）
量化视角： 负 Gamma（453万，无历史分位）｜负 Gamma 缓解（+6万）｜现价位于 Flip 下方 3.30%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 45（Put Wall，弱结构）；上方 49（MaxPain，仅结算参考） / 50（Call Wall，弱结构）。
• Gamma 区域：切换参考 48（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +0.9k / P -0.2k ｜ Activity HIGH ｜ 1D
10-09  C +0.3k / P +1.1k ｜ Activity HIGH ｜ 8D
10-16  C +1.8k / P -0.9k ｜ Activity HIGH ｜ 15D
10-23  C +0.2k / P -12 ｜ Activity HIGH ｜ 22D

📆 10-02 Forward Structure
存量OI: C 13.5k / P 9.2k，今日变化ΔOI: C +0.9k / P -0.2k，平值价格ATM: C $0.64 / P $0.52 ｜ ATM IV 57.0%，净 delta 敞口 14k shares
Top ΔOI: C 50 +505 ｜ C 48 +178 ｜ C 48 +111
仓位参考: Max Pain 49 ｜ Call Wall 50（+8.5%，弱）（OI 1.5k） ｜ Put Wall 50（+8.5%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 57.0%｜历史 Rank 30%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 13,566 股

📆 10-09 Forward Structure
存量OI: C 6.1k / P 5.6k，今日变化ΔOI: C +0.3k / P +1.1k，平值价格ATM: C $1.54 / P $1.52 ｜ ATM IV 54.4%，净 delta 敞口 -74k shares
Top ΔOI: P 47 +1,046 ｜ C 50 -233
仓位参考: Max Pain 50 ｜ Call Wall 50（+8.5%，弱）（OI 0.5k） ｜ Put Wall 47（+2.0%）（OI 2.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 54.4%｜历史 Rank 30%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 73,542 股

📆 10-16 Forward Structure
存量OI: C 19.2k / P 14.7k，今日变化ΔOI: C +1.8k / P -0.9k，平值价格ATM: C $2.19 / P $2.13 ｜ ATM IV 54.3%，净 delta 敞口 152k shares
Top ΔOI: P 55 -1,008 ｜ C 50 +876 ｜ C 47 +459
仓位参考: Max Pain 50 ｜ Call Wall 50（+8.5%，弱）（OI 4.0k） ｜ Put Wall 45（-2.4%，弱）（OI 3.6k）
量化解读： 存量 Call 重｜ATM IV 54.3%｜历史 Rank 30%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 152,223 股

📆 10-23 Forward Structure
存量OI: C 2.1k / P 1.5k，今日变化ΔOI: C +0.2k / P -12，平值价格ATM: C $2.45 / P $2.35 ｜ ATM IV 52.6%，净 delta 敞口 6k shares
仓位参考: Max Pain 51 ｜ Call Wall 50（+8.5%，弱）（OI 0.1k） ｜ Put Wall 45（-2.4%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 52.6%｜历史 Rank 30%（近端代理）｜IV/RV 1.14×（近似）｜净 delta 敞口 正 6,161 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=38 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=38）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/MP_evening.json