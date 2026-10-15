# 期权晚报 2026-10-15（快照 16:40 ET）

📊 市场环境

SPY $771.79 ｜ QQQ $728.00
VIX 16.46 ↓2.4%（5D +6.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 505P ΔOI +1,017（距现价 -1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-30 450P ΔOI +6,514 占该期限总 OI 11.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 550.7）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 500.41 → 收盘 514.71（+2.9%） ｜ 今日高 517.12 ｜ 低 495.79 ｜ 昨收 519.42 → 收盘 514.71（-0.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 2.09 | OI比 2.32 | ATM IV 39.2% | Skew 2.4pp | Term 1.05 | ExpMove ±2.0%（近端） | Rank 67%
量化视角： IV 中性（Rank 67%）｜期限结构正常（Term 1.05）｜保护溢价中性（Skew 2.4pp）｜当日成交偏 Put（P/C量 2.09）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.09×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.32×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-16（1D）±2.0% ｜ 10-23（8D）±4.8% ｜ 10-30（15D）±6.8% ｜ 11-06（22D）±11.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -47,746,217 | GEX Change vs 上次快照 12,255,249 | Flip: Candidates 550.70 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 80%（带内） ｜ IV 有效性: VALID 529 / LOW 439 / INVALID 684
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈551（全链重定价，覆盖 80%，CONDITIONAL）
Put Wall 500（弱结构｜现价高于该位 2.9%）
最近结构参考: Put Wall 500（现价高于该位 2.9%）
量化视角： 负 Gamma（4775万，无历史分位）｜负 Gamma 缓解（+1226万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 500（Put Wall，弱结构）；上方 538（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 551（全链重定价，覆盖 80%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +0.6k / P +1.7k ｜ Activity MEDIUM △ ｜ 1D
10-23  C +0.6k / P +1.1k ｜ Activity HIGH ｜ 8D
10-30  C +1.1k / P +13.9k ｜ Activity HIGH ｜ 15D
11-06  C +0.2k / P +88 ｜ Activity HIGH ｜ 22D

📆 10-16 Forward Structure
存量OI: C 46.0k / P 106.7k，今日变化ΔOI: C +0.6k / P +1.7k，平值价格ATM: C $5.20 / P $5.10 ｜ ATM IV 39.2%，净 delta 敞口 46k shares
Top ΔOI: P 505 +1,017 ｜ P 495 +947 ｜ P 530 -864
仓位参考: Max Pain 538 ｜ Call Wall 510（-0.9%，弱）（OI 2.1k） ｜ Put Wall 520（+1.0%，弱）（OI 5.9k）
量化解读： 存量 Put 重｜ATM IV 39.2%｜历史 Rank 67%（近端代理）｜IV/RV 1.39×（近似）｜净 delta 敞口 正 45,556 股

📆 10-23 Forward Structure
存量OI: C 4.0k / P 14.5k，今日变化ΔOI: C +0.6k / P +1.1k，平值价格ATM: C $13.16 / P $11.40 ｜ ATM IV 42.5%，净 delta 敞口 -12k shares
Top ΔOI: P 490 +480 ｜ C 525 +140 ｜ P 520 +121
仓位参考: Max Pain 555 ｜ Call Wall 525（+2.0%，弱）（OI 0.3k） ｜ Put Wall 510（-0.9%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 42.5%｜历史 Rank 67%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 11,991 股

📆 10-30 Forward Structure
存量OI: C 7.6k / P 48.5k，今日变化ΔOI: C +1.1k / P +13.9k，平值价格ATM: C $17.80 / P $17.33 ｜ ATM IV 41.6%，净 delta 敞口 -279k shares
Top ΔOI: P 450 +6,514 ｜ P 500 +6,338 ｜ P 490 +664
仓位参考: Max Pain 560 ｜ Put Wall 500（-2.9%）（OI 17.1k）
量化解读： 存量 Put 重｜ATM IV 41.6%｜历史 Rank 67%（近端代理）｜IV/RV 1.48×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 278,528 股

📆 11-06 Forward Structure
存量OI: C 1.4k / P 2.1k，今日变化ΔOI: C +0.2k / P +88，平值价格ATM: C $29.30 / P $28.40 ｜ ATM IV 39.7%，净 delta 敞口 7k shares
Top ΔOI: C 550 +184 ｜ P 570 -87 ｜ P 510 +45
仓位参考: Max Pain 568 ｜ Put Wall 500（-2.9%，弱）（OI 0.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 39.7%｜历史 Rank 67%（近端代理）｜IV/RV 1.41×（近似）｜净 delta 敞口 正 6,586 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/SOXX_evening.json