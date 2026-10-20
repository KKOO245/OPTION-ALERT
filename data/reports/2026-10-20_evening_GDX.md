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
🟡 **近现价集中开仓**: 10-21 84P ΔOI +605（距现价 -2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-26 91C ΔOI +1,804 占该期限总 OI 42.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 85.62 → 收盘 86.10（+0.6%） ｜ 今日高 88.47 ｜ 低 84.80 ｜ 昨收 86.47 → 收盘 86.10（-0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.43 | OI比 1.50 | ATM IV 40.7% | Skew -1.4pp | Term 0.99 | ExpMove ±1.7%（近端） | Rank 59%
量化视角： IV 中性（Rank 59%）｜期限结构正常（Term 0.99）｜Put 保护异常便宜（Skew -1.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.50×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-21（1D）±1.7% ｜ 10-23（3D）±3.1% ｜ 10-26（6D）±3.7% ｜ 10-28（8D）±5.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 20,002,785 | GEX Change vs 上次快照 1,716,453 | Flip: Primary Flip: 85.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 589 / LOW 137 / INVALID 484
结构观察区: Primary Flip 85.00（全链重定价，覆盖 98%）
最近结构参考: Flip 85（现价高于该位 1.3%）
量化视角： 正 Gamma（2000万，无历史分位）｜正 Gamma 增强（+172万）｜现价位于 Flip 上方 1.30%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 87（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 85（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-21  C +0.8k / P +1.1k ｜ Activity HIGH ｜ 1D
10-23  C +4.2k / P +1.0k ｜ Activity HIGH ｜ 3D
10-26  C +1.9k / P +84 ｜ Activity HIGH ｜ 6D
10-28  C +0.2k / P +0.1k ｜ Activity HIGH ｜ 8D

📆 10-21 Forward Structure
存量OI: C 4.3k / P 6.5k，今日变化ΔOI: C +0.8k / P +1.1k，平值价格ATM: C $0.81 / P $0.65 ｜ ATM IV 40.7%，净 delta 敞口 -11k shares
Top ΔOI: P 84 +605 ｜ C 89 +242 ｜ P 81 +219
仓位参考: Max Pain 87 ｜ Call Wall 87（+1.0%，弱）（OI 0.4k） ｜ Put Wall 84（-2.4%，弱）（OI 0.7k）
量化解读： 存量 Put 重｜ATM IV 40.7%｜历史 Rank 59%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 11,070 股

📆 10-23 Forward Structure
存量OI: C 96.1k / P 33.0k，今日变化ΔOI: C +4.2k / P +1.0k，平值价格ATM: C $1.59 / P $1.05 ｜ ATM IV 42.5%，净 delta 敞口 6k shares
Top ΔOI: C 91 +2,442 ｜ P 80 +481
仓位参考: Max Pain 86 ｜ Call Wall 90（+4.5%，弱）（OI 11.8k） ｜ Put Wall 85（-1.3%，弱）（OI 5.3k）
量化解读： 存量 Call 重｜ATM IV 42.5%｜历史 Rank 59%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 6,332 股

📆 10-26 Forward Structure
存量OI: C 3.0k / P 1.2k，今日变化ΔOI: C +1.9k / P +84，平值价格ATM: C $1.65 / P $1.50 ｜ ATM IV 36.9%，净 delta 敞口 23k shares
Top ΔOI: C 91 +1,804 ｜ C 90 +44 ｜ P 90 +43
仓位参考: Max Pain 86 ｜ Call Wall 91（+5.7%）（OI 1.8k） ｜ Put Wall 90（+4.5%，弱）（OI 85）
量化解读： 存量 Call 重｜ATM IV 36.9%｜历史 Rank 59%（近端代理）｜IV/RV 1.01×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 22,988 股

📆 10-28 Forward Structure
存量OI: C 0.3k / P 1.9k，今日变化ΔOI: C +0.2k / P +0.1k，平值价格ATM: C $2.43 / P $1.84 ｜ ATM IV 40.5%，净 delta 敞口 7k shares
Top ΔOI: C 88 +222 ｜ P 79 +39 ｜ P 84 +25
仓位参考: Max Pain 87 ｜ Call Wall 88（+2.2%）（OI 0.2k） ｜ Put Wall 84（-2.4%）（OI 1.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 40.5%｜历史 Rank 59%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 正 7,252 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/GDX_evening.json