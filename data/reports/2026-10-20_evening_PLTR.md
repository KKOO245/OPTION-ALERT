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
🟡 **近现价集中开仓**: 10-23 190P ΔOI +2,683（距现价 -1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 192.18 → 收盘 192.60（+0.2%） ｜ 今日高 196.11 ｜ 低 189.42 ｜ 昨收 194.15 → 收盘 192.60（-0.8%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-27，窗口结束前不做对错判定）

Options: P/C成交量 0.89 | OI比 0.91 | ATM IV 53.6% | Skew 4.2pp | Term 1.18 | ExpMove ±3.9%（近端） | Rank 75%
量化视角： IV 历史高位（Rank 75%，期权偏贵）｜期限结构正常偏陡（Term 1.18）｜保护溢价中性（Skew 4.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.89×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.91×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（3D）±3.9% ｜ 10-30（10D）±6.7% ｜ 11-06（17D）±12.4% ｜ 11-13（24D）±14.4%
   ⇒ IV–VIX Spread: +36.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 31,763,883 | GEX Change vs 上次快照 -2,087,580 | Flip: Primary Flip: 185.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 651 / LOW 64 / INVALID 197
结构观察区: Primary Flip 185.43（全链重定价，覆盖 100%）
Put Wall 190（弱结构｜现价高于该位 1.4%） | Call Wall 200（弱结构｜现价低于该位 3.7%）
最近结构参考: Put Wall 190（现价高于该位 1.4%）
量化视角： 正 Gamma（3176万，无历史分位）｜正 Gamma 减弱（209万）｜现价位于 Flip 上方 3.87%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（Put Wall，弱结构） / 190（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 185（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +20.3k / P +14.7k ｜ Activity HIGH ｜ 3D
10-30  C +3.1k / P +27.7k ｜ Activity HIGH ｜ 10D
11-06  C +2.4k / P +3.0k ｜ Activity HIGH ｜ 17D
11-13  C +0.5k / P +1.9k ｜ Activity HIGH ｜ 24D

📆 10-23 Forward Structure
存量OI: C 127.6k / P 115.7k，今日变化ΔOI: C +20.3k / P +14.7k，平值价格ATM: C $3.72 / P $3.70 ｜ ATM IV 53.6%，净 delta 敞口 -187k shares
Top ΔOI: C 205 +8,307 ｜ C 207 +7,882 ｜ P 190 +2,683
仓位参考: Max Pain 190 ｜ Call Wall 205（+6.4%，弱）（OI 16.1k） ｜ Put Wall 190（-1.3%，弱）（OI 6.4k）
量化解读： 存量两侧均衡｜ATM IV 53.6%｜历史 Rank 75%（近端代理）｜IV/RV 1.31×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 187,197 股

📆 10-30 Forward Structure
存量OI: C 48.4k / P 76.3k，今日变化ΔOI: C +3.1k / P +27.7k，平值价格ATM: C $6.47 / P $6.34 ｜ ATM IV 50.5%，净 delta 敞口 -177k shares
Top ΔOI: P 167 +4,990 ｜ P 165 +4,711 ｜ P 162 +4,543
仓位参考: Max Pain 190 ｜ Call Wall 200（+3.8%，弱）（OI 3.7k） ｜ Put Wall 190（-1.3%，弱）（OI 6.9k）
量化解读： 存量 Put 重｜ATM IV 50.5%｜历史 Rank 75%（近端代理）｜IV/RV 1.23×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 176,942 股

📆 11-06 Forward Structure
存量OI: C 24.9k / P 24.6k，今日变化ΔOI: C +2.4k / P +3.0k，平值价格ATM: C $12.26 / P $11.65 ｜ ATM IV 73.3%，净 delta 敞口 23k shares
Top ΔOI: P 165 +356
仓位参考: Max Pain 190 ｜ Call Wall 205（+6.4%，弱）（OI 1.6k） ｜ Put Wall 190（-1.3%，弱）（OI 3.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 73.3%｜历史 Rank 75%（近端代理）｜IV/RV 1.79×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 22,536 股

📆 11-13 Forward Structure
存量OI: C 9.7k / P 12.5k，今日变化ΔOI: C +0.5k / P +1.9k，平值价格ATM: C $14.65 / P $13.02 ｜ ATM IV 67.0%，净 delta 敞口 -15k shares
仓位参考: Max Pain 192 ｜ Call Wall 210（+9.0%，弱）（OI 1.0k） ｜ Put Wall 180（-6.5%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 67.0%｜历史 Rank 75%（近端代理）｜IV/RV 1.63×（近似）｜净 delta 敞口 负 14,714 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/PLTR_evening.json