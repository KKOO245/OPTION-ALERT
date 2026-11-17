# 期权晚报 2026-11-16（快照 21:00 ET）

📊 市场环境

SPY $739.95 ｜ QQQ $661.75
VIX 22.91 ↑18.7%（5D +15.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.8
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 80.46 → 收盘 78.95（-1.9%） ｜ 今日高 81.80 ｜ 低 78.83 ｜ 昨收 81.64 → 收盘 78.95（-3.3%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-19，窗口结束前不做对错判定）

Options: P/C成交量 1.71 | OI比 0.85 | ATM IV 53.1% | Skew 1.4pp | Term 0.86 | ExpMove ±3.0%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价薄（Skew 1.4pp）｜当日成交偏 Put（P/C量 1.71）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.71×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-18（2D）±3.0% ｜ 11-20（4D）±4.4% ｜ 11-23（7D）±7.7% ｜ 11-25（9D）±2.8%
   ⇒ IV–VIX Spread: +30.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -55,549,978 | GEX Change vs 上次快照 -33,943,218 | Flip: Primary Flip: 81.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 507 / LOW 200 / INVALID 497
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 81.88（全链重定价，覆盖 94%）
Put Wall 75（弱结构｜现价高于该位 5.3%）
最近结构参考: Flip 82（现价低于该位 3.6%）
量化视角： 负 Gamma（5555万，无历史分位）｜负 Gamma 加深（3394万）｜现价位于 Flip 下方 3.58%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 75（Put Wall，弱结构）；上方 84（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 82（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-18  C +0 / P +0 ｜ Activity LOW ｜ 2D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-23  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-25  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 11-18 Forward Structure
存量OI: C 1.6k / P 1.4k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.15 / P $1.21 ｜ ATM IV 53.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 84 ｜ Put Wall 84（+6.4%，弱）（OI 0.2k）
量化解读： 存量两侧均衡｜ATM IV 53.1%｜历史 Rank 86%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-20（Activity LOW）仓位参考: Max Pain 84 ｜ Call Wall 84（+6.4%，弱）（OI 22.3k） ｜ Put Wall 80（+1.3%，弱）（OI 24.1k）

11-23（Activity LOW）仓位参考: Max Pain 86 ｜ Call Wall 83（+5.1%，弱）（OI 24） ｜ Put Wall 81（+2.6%，弱）（OI 40）

11-25（Activity LOW）仓位参考: Max Pain 84 ｜ Call Wall 83（+5.1%）（OI 0.2k） ｜ Put Wall 80（+1.3%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=98 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=98）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/GDX_evening.json