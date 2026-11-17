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


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 749.66 → 收盘 739.95（-1.3%） ｜ 今日高 749.82 ｜ 低 738.07 ｜ 昨收 754.37 → 收盘 739.95（-1.9%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-19，窗口结束前不做对错判定）

Options: P/C成交量 1.23 | OI比 0.99 | ATM IV 24.4% | Skew 3.2pp | Term 0.75 | ExpMove ±1.0%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜保护溢价中性（Skew 3.2pp）｜当日成交偏 Put（P/C量 1.23）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.23×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.99×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 22% ｜ P/C OI(近端) 2%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 22%）｜近端持仓极端 Call 重（P/C OI 分位 2%，历史极低区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-17（1D）±1.0% ｜ 11-18（2D）±1.5% ｜ 11-19（3D）±1.8% ｜ 11-20（4D）±0.0%
   ⇒ IV–VIX Spread: +1.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,580,296,232 | GEX Change vs 上次快照 -454,127,530 | Flip: Primary Flip: 757.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 3009 / LOW 306 / INVALID 1377
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 757.15（全链重定价，覆盖 95%）
最近结构参考: Flip 757（现价低于该位 2.3%）
量化视角： 负 Gamma（15.80亿，历史分位偏负区，比 78% 的交易日更负）｜负 Gamma 加深（4.54亿）｜现价位于 Flip 下方 2.27%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 753（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 757（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-17  C +0 / P +0 ｜ Activity LOW ｜ 1D
11-18  C +0 / P +0 ｜ Activity LOW ｜ 2D
11-19  C +0 / P +0 ｜ Activity LOW ｜ 3D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 4D

📆 11-17 Forward Structure
存量OI: C 73.8k / P 73.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.87 / P $3.71 ｜ ATM IV 24.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 753 ｜ Call Wall 760（+2.7%，弱）（OI 5.3k） ｜ Put Wall 750（+1.4%）（OI 4.3k）
量化解读： 存量两侧均衡｜ATM IV 24.4%｜历史 Rank 92%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-18（Activity LOW）仓位参考: Max Pain 755 ｜ Call Wall 762（+3.0%，弱）（OI 3.7k） ｜ Put Wall 731（-1.2%，弱）（OI 10.4k）

11-19（Activity LOW）仓位参考: Max Pain 754 ｜ Call Wall 761（+2.8%，弱）（OI 1.8k） ｜ Put Wall 750（+1.4%，弱）（OI 2.4k）

11-20（Activity LOW）仓位参考: Max Pain 757 ｜ Put Wall 725（-2.0%，弱）（OI 66.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=98 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=98）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/SPY_evening.json