# 期权晚报 2026-11-12（快照 16:40 ET）

📊 市场环境

SPY $757.12 ｜ QQQ $688.17
VIX 18.70 ↑6.9%（5D -33.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-16 165P ΔOI +3,100（距现价 -0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 150.99 → 收盘 166.19（+10.1%） ｜ 今日高 167.14 ｜ 低 148.80 ｜ 昨收 173.73 → 收盘 166.19（-4.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.98 | OI比 0.71 | ATM IV 53.4% | Skew 3.1pp | Term 1.12 | ExpMove ±0.4%（近端） | Rank 77%
量化视角： IV 历史高位（Rank 77%，期权偏贵）｜期限结构正常（Term 1.12）｜保护溢价中性（Skew 3.1pp）｜存量 Call 偏重（OI比 0.71）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.98×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.71×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±0.4% ｜ 11-16（4D）±5.5% ｜ 11-18（6D）±9.7% ｜ 11-20（8D）±0.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -92,304,820 | GEX Change vs 上次快照 31,587,490 | Flip: Primary Flip: 171.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1179 / LOW 249 / INVALID 726
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 171.15（全链重定价，覆盖 100%）
最近结构参考: Flip 171（现价低于该位 2.9%）
量化视角： 负 Gamma（9230万，无历史分位）｜负 Gamma 缓解（+3159万）｜现价位于 Flip 下方 2.90%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 178（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 171（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +77.6k / P +18.8k ｜ Activity MEDIUM △ ｜ 1D
11-16  C +21.1k / P +13.6k ｜ Activity HIGH ｜ 4D
11-18  C +14.5k / P +11.4k ｜ Activity HIGH ｜ 6D
11-20  C +6.1k / P +17.6k ｜ Activity MEDIUM △ ｜ 8D

📆 11-13 Forward Structure
存量OI: C 593.3k / P 423.0k，今日变化ΔOI: C +77.6k / P +18.8k，平值价格ATM: C $0.35 / P $0.30 ｜ ATM IV 16.6%，净 delta 敞口 1.8M shares
Top ΔOI: C 185 +22,054 ｜ C 180 +11,053
仓位参考: Max Pain 178 ｜ Call Wall 180（+8.3%，弱）（OI 33.0k） ｜ Put Wall 160（-3.7%，弱）（OI 25.3k）
量化解读： 存量 Call 重｜ATM IV 16.6%｜历史 Rank 77%（近端代理）｜IV/RV 0.32×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,803,679 股

📆 11-16 Forward Structure
存量OI: C 122.3k / P 56.9k，今日变化ΔOI: C +21.1k / P +13.6k，平值价格ATM: C $5.25 / P $3.90 ｜ ATM IV 65.2%，净 delta 敞口 -523k shares
Top ΔOI: P 165 +3,100
仓位参考: Max Pain 175 ｜ Call Wall 182.5（+9.8%，弱）（OI 11.0k） ｜ Put Wall 155（-6.7%，弱）（OI 6.9k）
量化解读： 存量 Call 重｜ATM IV 65.2%｜历史 Rank 77%（近端代理）｜IV/RV 1.25×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 522,984 股

📆 11-18 Forward Structure
存量OI: C 87.2k / P 50.4k，今日变化ΔOI: C +14.5k / P +11.4k，平值价格ATM: C $8.65 / P $7.42 ｜ ATM IV 93.5%，净 delta 敞口 -56k shares
Top ΔOI: C 175 +3,253 ｜ C 195 +1,868 ｜ C 180 +1,744
仓位参考: Max Pain 175 ｜ Call Wall 180（+8.3%，弱）（OI 6.6k） ｜ Put Wall 160（-3.7%）（OI 5.4k）
量化解读： 存量 Call 重｜ATM IV 93.5%｜历史 Rank 77%（近端代理）｜IV/RV 1.80×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 56,466 股

11-20（MEDIUM △）Top ΔOI: 220C -15,391 ｜ 182C +10,773
11-20（MEDIUM △）仓位参考: Max Pain 200 ｜ Call Wall 180（+8.3%，弱）（OI 22.5k） ｜ Put Wall 170（+2.3%，弱）（OI 40.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/NVDA_evening.json