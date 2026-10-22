# 期权晚报 2026-10-22（快照 16:40 ET）

📊 市场环境

SPY $763.96 ｜ QQQ $704.47
VIX 19.03 ↑14.1%（5D +15.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 19.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-26 48P ΔOI +1,261（距现价 -1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 50.26 → 收盘 49.34（-1.8%） ｜ 今日高 50.33 ｜ 低 49.20 ｜ 昨收 52.26 → 收盘 49.34（-5.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-27，窗口结束前不做对错判定）

Options: P/C成交量 1.33 | OI比 0.60 | ATM IV 48.8% | Skew 1.0pp | Term 0.80 | ExpMove ±2.1%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价薄（Skew 1.0pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.60）+ 当日成交偏 Put（P/C量 1.33）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.33×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（1D）±2.1% ｜ 10-26（4D）±2.9% ｜ 10-28（6D）±4.2% ｜ 10-30（8D）±5.1%
   ⇒ IV–VIX Spread: +29.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,516,934 | GEX Change vs 上次快照 -1,929,498 | Flip: Primary Flip: 49.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 683 / LOW 118 / INVALID 399
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 49.61（全链重定价，覆盖 93%）
Put Wall 50（弱结构｜现价低于该位 1.3%）
最近结构参考: Flip 50（现价低于该位 0.5%）
量化视角： 负 Gamma（552万，无历史分位）｜负 Gamma 加深（193万）｜现价位于 Flip 下方 0.55%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 50（Put Wall，弱结构） / 52（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 50（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +5.2k / P -1.4k ｜ Activity HIGH ｜ 1D
10-26  C +2.1k / P +3.0k ｜ Activity HIGH ｜ 4D
10-28  C +2.1k / P +2.4k ｜ Activity HIGH ｜ 6D
10-30  C +3.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 8D

📆 10-23 Forward Structure
存量OI: C 77.0k / P 45.8k，今日变化ΔOI: C +5.2k / P -1.4k，平值价格ATM: C $0.45 / P $0.57 ｜ ATM IV 48.8%，净 delta 敞口 288k shares
Top ΔOI: C 52 +1,394 ｜ C 53 +1,311 ｜ C 52 +1,195
仓位参考: Max Pain 52 ｜ Call Wall 52（+5.4%，弱）（OI 5.7k） ｜ Put Wall 51（+3.4%，弱）（OI 4.4k）
量化解读： 存量 Call 重｜ATM IV 48.8%｜历史 Rank 82%（近端代理）｜IV/RV 1.54×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 287,566 股

📆 10-26 Forward Structure
存量OI: C 7.3k / P 6.9k，今日变化ΔOI: C +2.1k / P +3.0k，平值价格ATM: C $0.65 / P $0.76 ｜ ATM IV 34.1%，净 delta 敞口 -123k shares
Top ΔOI: P 48 +1,261 ｜ P 49 +1,185
仓位参考: Max Pain 50 ｜ Call Wall 50.5（+2.4%）（OI 1.5k） ｜ Put Wall 49（-0.7%，弱）（OI 1.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 34.1%｜历史 Rank 82%（近端代理）｜IV/RV 1.07×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 123,167 股

📆 10-28 Forward Structure
存量OI: C 5.4k / P 5.4k，今日变化ΔOI: C +2.1k / P +2.4k，平值价格ATM: C $0.96 / P $1.11 ｜ ATM IV 40.4%，净 delta 敞口 -75k shares
Top ΔOI: P 48 +645
仓位参考: Max Pain 52 ｜ Call Wall 53（+7.4%，弱）（OI 0.6k） ｜ Put Wall 48（-2.7%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 40.4%｜历史 Rank 82%（近端代理）｜IV/RV 1.27×（近似）｜净 delta 敞口 负 74,977 股

10-30（MEDIUM △）Top ΔOI: 50P -545
10-30（MEDIUM △）仓位参考: Max Pain 54 ｜ Call Wall 54（+9.4%，弱）（OI 2.5k） ｜ Put Wall 50（+1.3%，弱）（OI 3.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/SLV_evening.json