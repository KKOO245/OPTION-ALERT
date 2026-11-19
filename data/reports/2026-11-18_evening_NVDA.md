# 期权晚报 2026-11-18（快照 16:40 ET）

📊 市场环境

SPY $730.20 ｜ QQQ $nan
VIX 24.56 ↓3.5%（5D +40.4%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-23 150P ΔOI +1,863（距现价 -0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 159.19 → 收盘 150.96（-5.2%） ｜ 今日高 159.70 ｜ 低 150.40 ｜ 昨收 155.46 → 收盘 150.96（-2.9%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-23，窗口结束前不做对错判定）

Options: P/C成交量 0.77 | OI比 0.78 | ATM IV 62.2% | Skew -19.8pp | Term 0.65 | ExpMove ±0.4%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.65，近月 IV 高于远月）｜Put 保护异常便宜（Skew -19.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（2D）±0.4% ｜ 11-23（5D）±5.7% ｜ 11-25（7D）±6.7% ｜ 11-27（9D）±0.3%
   ⇒ IV–VIX Spread: +37.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -130,993,080 | GEX Change vs 上次快照 -97,758,031 | Flip: Primary Flip: 157.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 1077 / LOW 300 / INVALID 735
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 157.18（全链重定价，覆盖 91%）
最近结构参考: Flip 157（现价低于该位 4.0%）
量化视角： 负 Gamma（1.31亿，无历史分位）｜负 Gamma 加深（9776万）｜现价位于 Flip 下方 3.96%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 158（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 157（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +118.6k / P +47.0k ｜ Activity HIGH ｜ 2D
11-23  C +11.1k / P +10.3k ｜ Activity HIGH ｜ 5D
11-25  C +5.5k / P +3.7k ｜ Activity HIGH ｜ 7D
11-27  C +27.7k / P +0.5k ｜ Activity HIGH ｜ 9D

📆 11-20 Forward Structure
存量OI: C 1572.1k / P 1012.1k，今日变化ΔOI: C +118.6k / P +47.0k，平值价格ATM: C $0.55 / P $0.00 ｜ ATM IV 63.9%，净 delta 敞口 3.7M shares
Top ΔOI: C 170 +15,703 ｜ C 185 +12,841 ｜ P 135 +12,036
仓位参考: Max Pain 180 ｜ Call Wall 165（+9.3%，弱）（OI 31.2k） ｜ Put Wall 150（-0.6%，弱）（OI 51.0k）
量化解读： 存量 Call 重｜ATM IV 63.9%｜历史 Rank 85%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,677,859 股

📆 11-23 Forward Structure
存量OI: C 55.2k / P 34.6k，今日变化ΔOI: C +11.1k / P +10.3k，平值价格ATM: C $4.75 / P $3.80 ｜ ATM IV 59.9%，净 delta 敞口 -15k shares
Top ΔOI: P 135 +2,004 ｜ P 150 +1,863 ｜ P 140 +1,429
仓位参考: Max Pain 160 ｜ Call Wall 160（+6.0%，弱）（OI 4.2k） ｜ Put Wall 150（-0.6%，弱）（OI 4.3k）
量化解读： 存量 Call 重｜ATM IV 59.9%｜历史 Rank 85%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 15,375 股

📆 11-25 Forward Structure
存量OI: C 31.7k / P 12.3k，今日变化ΔOI: C +5.5k / P +3.7k，平值价格ATM: C $5.55 / P $4.51 ｜ ATM IV 60.1%，净 delta 敞口 -7k shares
Top ΔOI: C 165 -533
仓位参考: Max Pain 158 ｜ Call Wall 165（+9.3%，弱）（OI 2.6k） ｜ Put Wall 140（-7.3%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 60.1%｜历史 Rank 85%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 6,656 股

📆 11-27 Forward Structure
存量OI: C 225.3k / P 163.8k，今日变化ΔOI: C +27.7k / P +0.5k，平值价格ATM: C $0.49 / P $0.00 ｜ ATM IV 41.7%，净 delta 敞口 558k shares
Top ΔOI: C 185 +8,028 ｜ P 145 -5,553 ｜ C 182 -3,797
仓位参考: Max Pain 178 ｜ Call Wall 160（+6.0%，弱）（OI 7.6k） ｜ Put Wall 165（+9.3%，弱）（OI 12.7k）
量化解读： 存量 Call 重｜ATM IV 41.7%｜历史 Rank 85%（近端代理）｜IV/RV 0.83×（近似）｜净 delta 敞口 正 557,854 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/NVDA_evening.json