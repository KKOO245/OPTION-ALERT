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
🟡 **近现价集中开仓**: 10-30 1300P ΔOI +216（距现价 +3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,317.26 → 收盘 1,260.93（-4.3%） ｜ 今日高 1355.00 ｜ 低 1244.61 ｜ 昨收 1,378.22 → 收盘 1,260.93（-8.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-27，窗口结束前不做对错判定）

Options: P/C成交量 0.88 | OI比 0.84 | ATM IV 103.7% | Skew 7.5pp | Term 0.77 | ExpMove ±4.4%（近端） | Rank 61%
量化视角： IV 中性（Rank 61%）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价显著（Skew 7.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.84）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.88×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.84×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（1D）±4.4% ｜ 10-30（8D）±12.1% ｜ 11-06（15D）±15.1% ｜ 11-13（22D）±16.3%
   ⇒ IV–VIX Spread: +84.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,407,374 | GEX Change vs 上次快照 -5,139,642 | Flip: Primary Flip: 1368.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1890 / LOW 570 / INVALID 1026
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1368.18（全链重定价，覆盖 99%）
最近结构参考: Flip 1368（现价低于该位 7.8%）
量化视角： 负 Gamma（941万，无历史分位）｜负 Gamma 加深（514万）｜现价位于 Flip 下方 7.84%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,400（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1368（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +3.2k / P +3.0k ｜ Activity MEDIUM △ ｜ 1D
10-30  C +2.2k / P +1.3k ｜ Activity HIGH ｜ 8D
11-06  C +0.8k / P +0.2k ｜ Activity HIGH ｜ 15D
11-13  C +0.3k / P +0.3k ｜ Activity HIGH ｜ 22D

📆 10-23 Forward Structure
存量OI: C 50.4k / P 42.2k，今日变化ΔOI: C +3.2k / P +3.0k，平值价格ATM: C $28.58 / P $27.20 ｜ ATM IV 103.7%，净 delta 敞口 -192k shares
Top ΔOI: P 1380 +635
仓位参考: Max Pain 1,400 ｜ Put Wall 1250（-0.9%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 103.7%｜历史 Rank 61%（近端代理）｜IV/RV 2.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 191,998 股

📆 10-30 Forward Structure
存量OI: C 28.2k / P 18.5k，今日变化ΔOI: C +2.2k / P +1.3k，平值价格ATM: C $76.75 / P $75.86 ｜ ATM IV 101.8%，净 delta 敞口 -10k shares
Top ΔOI: C 1800 +454 ｜ P 1300 +216
仓位参考: Max Pain 1,480 ｜ Call Wall 1350（+7.1%，弱）（OI 0.7k） ｜ Put Wall 1350（+7.1%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 101.8%｜历史 Rank 61%（近端代理）｜IV/RV 2.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 9,606 股

📆 11-06 Forward Structure
存量OI: C 10.0k / P 7.5k，今日变化ΔOI: C +0.8k / P +0.2k，平值价格ATM: C $97.00 / P $93.04 ｜ ATM IV 88.9%，净 delta 敞口 5k shares
Top ΔOI: C 1700 +99
仓位参考: Max Pain 1,495 ｜ Put Wall 1200（-4.8%）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 88.9%｜历史 Rank 61%（近端代理）｜IV/RV 1.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,094 股

📆 11-13 Forward Structure
存量OI: C 4.6k / P 4.2k，今日变化ΔOI: C +0.3k / P +0.3k，平值价格ATM: C $105.00 / P $100.30 ｜ ATM IV 82.7%，净 delta 敞口 -2k shares
Top ΔOI: C 1320 +51
仓位参考: Max Pain 1,500 ｜ Put Wall 1300（+3.1%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜ATM IV 82.7%｜历史 Rank 61%（近端代理）｜IV/RV 1.65×（近似）｜净 delta 敞口 负 2,125 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/SNDK_evening.json