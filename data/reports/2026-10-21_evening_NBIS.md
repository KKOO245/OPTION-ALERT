# 期权晚报 2026-10-21（快照 16:40 ET）

📊 市场环境

SPY $773.09 ｜ QQQ $725.20
VIX 16.68 ↓3.6%（5D -1.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 180C ΔOI +1,129（距现价 +4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 176.07 → 收盘 171.57（-2.6%） ｜ 今日高 178.85 ｜ 低 164.00 ｜ 昨收 171.45 → 收盘 171.57（+0.1%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-26，窗口结束前不做对错判定）

Options: P/C成交量 0.41 | OI比 0.62 | ATM IV 107.4% | Skew 1.3pp | Term 0.88 | ExpMove ±6.5%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价薄（Skew 1.3pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.41×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（2D）±6.5% ｜ 10-30（9D）±11.7% ｜ 11-06（16D）±15.8% ｜ 11-13（23D）±19.7%
   ⇒ IV–VIX Spread: +90.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,159,474 | GEX Change vs 上次快照 -211,556 | Flip: Primary Flip: 174.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 563 / LOW 53 / INVALID 194
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 174.35（全链重定价，覆盖 100%）
最近结构参考: Flip 174（现价低于该位 1.6%）
量化视角： 负 Gamma（316万，无历史分位）｜负 Gamma 加深（21万）｜现价位于 Flip 下方 1.59%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 180（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 174（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +10.1k / P +3.0k ｜ Activity HIGH ｜ 2D
10-30  C +6.4k / P +3.1k ｜ Activity HIGH ｜ 9D
11-06  C +1.8k / P +0.6k ｜ Activity HIGH ｜ 16D
11-13  C +0.6k / P +0.3k ｜ Activity HIGH ｜ 23D

📆 10-23 Forward Structure
存量OI: C 105.4k / P 65.2k，今日变化ΔOI: C +10.1k / P +3.0k，平值价格ATM: C $5.10 / P $6.05 ｜ ATM IV 107.4%，净 delta 敞口 176k shares
Top ΔOI: C 180 +1,129
仓位参考: Max Pain 180 ｜ Call Wall 180（+4.9%，弱）（OI 5.5k） ｜ Put Wall 165（-3.8%，弱）（OI 4.4k）
量化解读： 存量 Call 重｜ATM IV 107.4%｜历史 Rank 58%（近端代理）｜IV/RV 1.38×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 176,310 股

📆 10-30 Forward Structure
存量OI: C 49.7k / P 39.1k，今日变化ΔOI: C +6.4k / P +3.1k，平值价格ATM: C $9.77 / P $10.30 ｜ ATM IV 93.5%，净 delta 敞口 82k shares
Top ΔOI: C 225 +1,944 ｜ C 170 +948
仓位参考: Max Pain 208 ｜ Call Wall 175（+2.0%，弱）（OI 1.4k） ｜ Put Wall 165（-3.8%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 93.5%｜历史 Rank 58%（近端代理）｜IV/RV 1.20×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 82,360 股

📆 11-06 Forward Structure
存量OI: C 31.2k / P 17.1k，今日变化ΔOI: C +1.8k / P +0.6k，平值价格ATM: C $13.95 / P $13.20 ｜ ATM IV 90.7%，净 delta 敞口 10k shares
Top ΔOI: C 230 +418 ｜ P 165 +229 ｜ C 200 +206
仓位参考: Max Pain 210 ｜ Put Wall 170（-0.9%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 90.7%｜历史 Rank 58%（近端代理）｜IV/RV 1.16×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 10,423 股

📆 11-13 Forward Structure
存量OI: C 12.3k / P 15.6k，今日变化ΔOI: C +0.6k / P +0.3k，平值价格ATM: C $18.03 / P $15.80 ｜ ATM IV 100.1%，净 delta 敞口 15k shares
Top ΔOI: P 165 +158 ｜ C 200 +147 ｜ C 170 +84
仓位参考: Max Pain 205 ｜ Call Wall 180（+4.9%，弱）（OI 0.4k） ｜ Put Wall 165（-3.8%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 100.1%｜历史 Rank 58%（近端代理）｜IV/RV 1.28×（近似）｜净 delta 敞口 正 14,787 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/NBIS_evening.json