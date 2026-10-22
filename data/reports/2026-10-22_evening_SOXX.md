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
🟡 **近现价集中开仓**: 11-06 460P ΔOI -73（距现价 -3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 489.73 → 收盘 475.69（-2.9%） ｜ 今日高 494.00 ｜ 低 472.21 ｜ 昨收 510.36 → 收盘 475.69（-6.8%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-27，窗口结束前不做对错判定）

Options: P/C成交量 3.70 | OI比 1.30 | ATM IV 61.1% | Skew 1.7pp | Term 0.79 | ExpMove ±2.7%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价薄（Skew 1.7pp）｜当日成交偏 Put（P/C量 3.70）——观察点，非方向信号
   ⇒ Put/Call Volume: 3.70×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.30×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-23（1D）±2.7% ｜ 10-30（8D）±7.0% ｜ 11-06（15D）±8.4% ｜ 11-13（22D）±9.9%
   ⇒ IV–VIX Spread: +42.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -36,286,272 | GEX Change vs 上次快照 -2,144,396 | Flip: Primary Flip: 524.08（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 554 / LOW 290 / INVALID 710
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 524.08（全链重定价，覆盖 93%）
最近结构参考: Flip 524（现价低于该位 9.2%）
量化视角： 负 Gamma（3629万，无历史分位）｜负 Gamma 加深（214万）｜现价位于 Flip 下方 9.23%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 512（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 524（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +1.6k / P -0.8k ｜ Activity HIGH ｜ 1D
10-30  C -0.6k / P -2.1k ｜ Activity MEDIUM △ ｜ 8D
11-06  C -0.3k / P -36 ｜ Activity MEDIUM △ ｜ 15D
11-13  C +0.2k / P +0.4k ｜ Activity HIGH ｜ 22D

📆 10-23 Forward Structure
存量OI: C 14.8k / P 19.4k，今日变化ΔOI: C +1.6k / P -0.8k，平值价格ATM: C $6.87 / P $6.10 ｜ ATM IV 61.1%，净 delta 敞口 67k shares
Top ΔOI: P 500 -884 ｜ C 512 +708 ｜ C 520 +540
仓位参考: Max Pain 512 ｜ Call Wall 500（+5.1%，弱）（OI 1.4k） ｜ Put Wall 490（+3.0%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 61.1%｜历史 Rank 93%（近端代理）｜IV/RV 1.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 66,715 股

10-30（MEDIUM △）Top ΔOI: 500P -2,542 ｜ 475P -361
10-30（MEDIUM △）仓位参考: Max Pain 530

11-06（MEDIUM △）Top ΔOI: 537C -164 ｜ 460P -73
11-06（MEDIUM △）仓位参考: Max Pain 538 ｜ Put Wall 495（+4.1%，弱）（OI 1.0k）

📆 11-13 Forward Structure
存量OI: C 14.2k / P 5.5k，今日变化ΔOI: C +0.2k / P +0.4k，平值价格ATM: C $24.50 / P $22.79 ｜ ATM IV 48.8%，净 delta 敞口 -20k shares
Top ΔOI: P 510 +166 ｜ P 512 +56
仓位参考: Max Pain 520 ｜ Put Wall 460（-3.3%）（OI 3.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 48.8%｜历史 Rank 93%（近端代理）｜IV/RV 1.59×（近似）｜净 delta 敞口 负 19,737 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/SOXX_evening.json