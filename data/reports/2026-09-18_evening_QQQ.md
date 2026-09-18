# 期权晚报 2026-09-18（快照 16:40 ET）

📊 市场环境

SPY $761.69 ｜ QQQ $721.45
VIX 14.81 ↓4.1%（5D -6.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 29.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-21 715P ΔOI +13,509（距现价 -0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-24 655P ΔOI +7,773 占该期限总 OI 14.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 718.84 → 收盘 721.45（+0.4%） ｜ 今日高 721.72 ｜ 低 715.08 ｜ 昨收 716.92 → 收盘 721.45（+0.6%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-25，窗口结束前不做对错判定）

Options: P/C成交量 0.99 | OI比 1.33 | ATM IV 24.7% | Skew 1.8pp | Term 0.67 | ExpMove ±0.7%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.67，近月 IV 高于远月）｜保护溢价薄（Skew 1.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.99×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.33×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 77% ｜ P/C OI(近端) 23%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 77%）｜近端持仓结构中性（P/C OI 分位 23%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-21（3D）±0.7% ｜ 09-22（4D）±1.0% ｜ 09-23（5D）±1.2% ｜ 09-24（6D）±1.4%
   ⇒ IV–VIX Spread: +9.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 273,487,640 | GEX Change vs 上次快照 260,949,360 | Flip: Candidates 717.41 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 78%（带内） ｜ IV 有效性: VALID 2692 / LOW 435 / INVALID 2109
结构观察区: ≈717（全链重定价，覆盖 78%，CONDITIONAL）
Call Wall 720（弱结构｜现价高于该位 0.2%）
最近结构参考: Call Wall 720（现价高于该位 0.2%）
量化视角： 正 Gamma（2.73亿，历史分位偏正区，比 77% 的交易日更正）｜正 Gamma 增强（+2.61亿）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 701（MaxPain，仅结算参考） / 720（Call Wall，弱结构）。
• Gamma 区域：切换参考 717（全链重定价，覆盖 78%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-21  C +31.1k / P +55.7k ｜ Activity HIGH ｜ 3D
09-22  C +13.1k / P +9.9k ｜ Activity HIGH ｜ 4D
09-23  C +6.1k / P +12.4k ｜ Activity HIGH ｜ 5D
09-24  C +7.9k / P +19.9k ｜ Activity HIGH ｜ 6D

📆 09-21 Forward Structure
存量OI: C 62.9k / P 153.6k，今日变化ΔOI: C +31.1k / P +55.7k，平值价格ATM: C $2.96 / P $2.19 ｜ ATM IV 9.1%，净 delta 敞口 616k shares
Top ΔOI: P 715 +13,509 ｜ P 710 +7,470 ｜ C 735 +5,980
仓位参考: Max Pain 715 ｜ Call Wall 735（+1.9%）（OI 8.2k） ｜ Put Wall 715（-0.9%）（OI 20.8k）
量化解读： 存量 Put 重｜ATM IV 9.1%｜历史 Rank 78%（近端代理）｜IV/RV 0.73×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 616,117 股

📆 09-22 Forward Structure
存量OI: C 39.5k / P 40.5k，今日变化ΔOI: C +13.1k / P +9.9k，平值价格ATM: C $3.94 / P $3.06 ｜ ATM IV 11.3%，净 delta 敞口 179k shares
Top ΔOI: C 740 +1,298
仓位参考: Max Pain 713 ｜ Call Wall 725（+0.5%，弱）（OI 2.3k） ｜ Put Wall 715（-0.9%，弱）（OI 1.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 11.3%｜历史 Rank 78%（近端代理）｜IV/RV 0.90×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 179,417 股

📆 09-23 Forward Structure
存量OI: C 23.8k / P 36.8k，今日变化ΔOI: C +6.1k / P +12.4k，平值价格ATM: C $5.00 / P $3.85 ｜ ATM IV 12.6%，净 delta 敞口 -57k shares
Top ΔOI: P 697 +2,411 ｜ P 717 +1,520
仓位参考: Max Pain 714 ｜ Call Wall 735（+1.9%，弱）（OI 2.2k） ｜ Put Wall 717（-0.6%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜ATM IV 12.6%｜历史 Rank 78%（近端代理）｜IV/RV 1.01×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 56,998 股

📆 09-24 Forward Structure
存量OI: C 16.9k / P 35.7k，今日变化ΔOI: C +7.9k / P +19.9k，平值价格ATM: C $5.59 / P $4.60 ｜ ATM IV 13.5%，净 delta 敞口 24k shares
Top ΔOI: P 655 +7,773 ｜ C 729 +1,302 ｜ P 699 +1,262
仓位参考: Max Pain 715 ｜ Call Wall 729（+1.0%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜ATM IV 13.5%｜历史 Rank 78%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 正 24,453 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/QQQ_evening.json