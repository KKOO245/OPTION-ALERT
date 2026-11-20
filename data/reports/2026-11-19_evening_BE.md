# 期权晚报 2026-11-19（快照 16:40 ET）

📊 市场环境

SPY $715.87 ｜ QQQ $nan
VIX 28.44 ↑15.8%（5D +52.1%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 18.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-27 172C ΔOI +267（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 181.00 → 收盘 168.11（-7.1%） ｜ 今日高 187.00 ｜ 低 166.17 ｜ 昨收 170.98 → 收盘 168.11（-1.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-24，窗口结束前不做对错判定）

Options: P/C成交量 0.93 | OI比 0.75 | ATM IV 145.0% | Skew 17.8pp | Term 0.69 | ExpMove ±6.0%（近端） | Rank 89%
量化视角： IV 历史高位（Rank 89%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价显著（Skew 17.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.93×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±6.0% ｜ 11-27（8D）±12.2% ｜ 12-04（15D）±16.3% ｜ 12-11（22D）±19.9%
   ⇒ IV–VIX Spread: +116.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,964,581 | GEX Change vs 上次快照 -7,467,625 | Flip: Primary Flip: 185.21（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 498 / LOW 122 / INVALID 182
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 185.21（全链重定价，覆盖 100%）
最近结构参考: Flip 185（现价低于该位 9.2%）
量化视角： 负 Gamma（1096万，无历史分位）｜负 Gamma 加深（747万）｜现价位于 Flip 下方 9.23%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 190（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 185（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +4.1k / P -7.7k ｜ Activity HIGH ｜ 1D
11-27  C +1.5k / P +0.7k ｜ Activity HIGH ｜ 8D
12-04  C +0.5k / P +0.4k ｜ Activity HIGH ｜ 15D
12-11  C +33 / P +0.2k ｜ Activity HIGH ｜ 22D

📆 11-20 Forward Structure
存量OI: C 109.5k / P 82.1k，今日变化ΔOI: C +4.1k / P -7.7k，平值价格ATM: C $5.30 / P $4.80 ｜ ATM IV 144.9%，净 delta 敞口 852k shares
Top ΔOI: P 240 -2,141 ｜ P 230 -1,721
仓位参考: Max Pain 190 ｜ Call Wall 180（+7.1%，弱）（OI 3.5k） ｜ Put Wall 170（+1.1%，弱）（OI 4.1k）
量化解读： 存量 Call 重｜ATM IV 144.9%｜历史 Rank 89%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 851,666 股

📆 11-27 Forward Structure
存量OI: C 17.5k / P 13.5k，今日变化ΔOI: C +1.5k / P +0.7k，平值价格ATM: C $10.65 / P $9.95 ｜ ATM IV 104.4%，净 delta 敞口 34k shares
Top ΔOI: C 172 +267
仓位参考: Max Pain 195 ｜ Call Wall 175（+4.1%，弱）（OI 0.5k） ｜ Put Wall 175（+4.1%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 104.4%｜历史 Rank 89%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 33,928 股

📆 12-04 Forward Structure
存量OI: C 9.2k / P 8.2k，今日变化ΔOI: C +0.5k / P +0.4k，平值价格ATM: C $14.30 / P $13.07 ｜ ATM IV 104.2%，净 delta 敞口 -178 shares
仓位参考: Max Pain 200 ｜ Call Wall 180（+7.1%，弱）（OI 0.3k） ｜ Put Wall 170（+1.1%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜ATM IV 104.2%｜历史 Rank 89%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 178 股

📆 12-11 Forward Structure
存量OI: C 3.8k / P 4.7k，今日变化ΔOI: C +33 / P +0.2k，平值价格ATM: C $15.94 / P $17.48 ｜ ATM IV 102.9%，净 delta 敞口 -3k shares
仓位参考: Max Pain 205 ｜ Put Wall 175（+4.1%）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 102.9%｜历史 Rank 89%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 负 3,388 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/BE_evening.json