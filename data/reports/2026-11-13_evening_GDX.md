# 期权晚报 2026-11-13（快照 16:40 ET）

📊 市场环境

SPY $754.37 ｜ QQQ $679.89
VIX 19.30 ↑3.2%（5D -24.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-16 79P ΔOI +788（距现价 -3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-16 79P ΔOI +788 占该期限总 OI 12.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 81.90 → 收盘 81.64（-0.3%） ｜ 今日高 82.89 ｜ 低 81.29 ｜ 昨收 81.84 → 收盘 81.64（-0.2%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-18，窗口结束前不做对错判定）

Options: P/C成交量 2.93 | OI比 0.57 | ATM IV 103.0% | Skew 4.8pp | Term 0.41 | ExpMove ±2.2%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.41，近月 IV 高于远月）｜保护溢价中性（Skew 4.8pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.57）+ 当日成交偏 Put（P/C量 2.93）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 2.93×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.57×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-16（3D）±2.2% ｜ 11-18（5D）±3.6% ｜ 11-20（7D）±4.7% ｜ 11-23（10D）±5.1%
   ⇒ IV–VIX Spread: +83.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -33,294,189 | GEX Change vs 上次快照 -10,759,944 | Flip: Primary Flip: 83.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 541 / LOW 230 / INVALID 487
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 83.88（全链重定价，覆盖 86%）
最近结构参考: Flip 84（现价低于该位 2.7%）
量化视角： 负 Gamma（3329万，无历史分位）｜负 Gamma 加深（1076万）｜现价位于 Flip 下方 2.67%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 83（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 84（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-16  C +0.8k / P +0.8k ｜ Activity HIGH ｜ 3D
11-18  C +0.2k / P +0.3k ｜ Activity HIGH ｜ 5D
11-20  C +33.7k / P -0.4k ｜ Activity HIGH ｜ 7D
11-23  C +28 / P +90 ｜ Activity MEDIUM △ ｜ 10D

📆 11-16 Forward Structure
存量OI: C 3.3k / P 2.9k，今日变化ΔOI: C +0.8k / P +0.8k，平值价格ATM: C $0.72 / P $1.06 ｜ ATM IV 30.1%，净 delta 敞口 7k shares
Top ΔOI: P 79 +788 ｜ C 87 +528 ｜ P 80 +103
仓位参考: Max Pain 85 ｜ Put Wall 79（-3.2%）（OI 1.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 30.1%｜历史 Rank 100%（近端代理）｜IV/RV 0.53×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 7,480 股

📆 11-18 Forward Structure
存量OI: C 0.9k / P 1.2k，今日变化ΔOI: C +0.2k / P +0.3k，平值价格ATM: C $1.40 / P $1.53 ｜ ATM IV 38.5%，净 delta 敞口 -8k shares
Top ΔOI: P 80 +153 ｜ C 87 +94 ｜ P 82 +81
仓位参考: Max Pain 85 ｜ Call Wall 86（+5.3%，弱）（OI 0.1k） ｜ Put Wall 84（+2.9%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜ATM IV 38.5%｜历史 Rank 100%（近端代理）｜IV/RV 0.67×（近似）｜净 delta 敞口 负 7,779 股

📆 11-20 Forward Structure
存量OI: C 135.1k / P 170.4k，今日变化ΔOI: C +33.7k / P -0.4k，平值价格ATM: C $1.75 / P $2.05 ｜ ATM IV 42.9%，净 delta 敞口 863k shares
Top ΔOI: C 87 +10,455 ｜ C 84 +9,214 ｜ C 88 +4,908
仓位参考: Max Pain 85 ｜ Call Wall 84（+2.9%，弱）（OI 17.7k） ｜ Put Wall 80（-2.0%，弱）（OI 24.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 42.9%｜历史 Rank 100%（近端代理）｜IV/RV 0.75×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 863,463 股

11-23（MEDIUM △）Top ΔOI: 83P +29 ｜ 78P +22
11-23（MEDIUM △）仓位参考: Max Pain 86 ｜ Call Wall 83（+1.7%，弱）（OI 24） ｜ Put Wall 83（+1.7%，弱）（OI 33）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/GDX_evening.json