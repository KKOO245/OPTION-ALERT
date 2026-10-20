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
🟡 **近现价集中开仓**: 10-23 146P ΔOI +1,802（距现价 -4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 148.03 → 收盘 153.24（+3.5%） ｜ 今日高 153.97 ｜ 低 147.76 ｜ 昨收 147.86 → 收盘 153.24（+3.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 2.44 | OI比 1.10 | ATM IV 35.2% | Skew 5.3pp | Term 0.95 | ExpMove ±2.6%（近端） | Rank 61%
量化视角： IV 中性（Rank 61%）｜期限结构正常（Term 0.95）｜保护溢价中性（Skew 5.3pp）｜当日成交偏 Put（P/C量 2.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.44×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.10×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（3D）±2.6% ｜ 10-30（10D）±4.3% ｜ 11-06（17D）±5.3% ｜ 11-13（24D）±5.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,125,306 | GEX Change vs 上次快照 5,586,895 | Flip: Primary Flip: 161.74（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 352 / LOW 97 / INVALID 325
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 161.74（全链重定价，覆盖 94%）
Call Wall 155（现价低于该位 1.1%）
最近结构参考: Call Wall 155（现价低于该位 1.1%）
量化视角： 负 Gamma（713万，无历史分位）｜负 Gamma 缓解（+559万）｜现价位于 Flip 下方 5.26%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 146（MaxPain，仅结算参考）；上方 155（Call Wall）。
• Gamma 区域：切换参考 162（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +1.6k / P +2.5k ｜ Activity HIGH ｜ 3D
10-30  C +0.6k / P +1.8k ｜ Activity HIGH ｜ 10D
11-06  C +0.1k / P +33 ｜ Activity MEDIUM △ ｜ 17D
11-13  C +95 / P +86 ｜ Activity HIGH ｜ 24D

📆 10-23 Forward Structure
存量OI: C 19.0k / P 20.8k，今日变化ΔOI: C +1.6k / P +2.5k，平值价格ATM: C $2.20 / P $1.83 ｜ ATM IV 35.2%，净 delta 敞口 32k shares
Top ΔOI: P 146 +1,802 ｜ C 155 +767 ｜ C 156 +644
仓位参考: Max Pain 146 ｜ Call Wall 148（-3.4%，弱）（OI 3.0k） ｜ Put Wall 144（-6.0%，弱）（OI 3.1k）
量化解读： 存量两侧均衡｜ATM IV 35.2%｜历史 Rank 61%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 32,069 股

📆 10-30 Forward Structure
存量OI: C 6.0k / P 47.8k，今日变化ΔOI: C +0.6k / P +1.8k，平值价格ATM: C $3.35 / P $3.20 ｜ ATM IV 33.2%，净 delta 敞口 11k shares
Top ΔOI: P 140 +995 ｜ P 143 +655 ｜ P 142 +147
仓位参考: Max Pain 152 ｜ Call Wall 155（+1.1%）（OI 1.7k） ｜ Put Wall 150（-2.1%，弱）（OI 6.5k）
量化解读： 存量 Put 重｜ATM IV 33.2%｜历史 Rank 61%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 正 10,928 股

11-06（MEDIUM △）Top ΔOI: 140P +60 ｜ 159C +44
11-06（MEDIUM △）仓位参考: Max Pain 152 ｜ Call Wall 155（+1.1%，弱）（OI 0.3k） ｜ Put Wall 145（-5.4%，弱）（OI 0.4k）

📆 11-13 Forward Structure
存量OI: C 0.4k / P 1.8k，今日变化ΔOI: C +95 / P +86，平值价格ATM: C $3.00 / P $4.90 ｜ ATM IV 33.9%，净 delta 敞口 6k shares
Top ΔOI: C 120 +59
仓位参考: Max Pain 153 ｜ Call Wall 154（+0.5%，弱）（OI 21） ｜ Put Wall 153（-0.2%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 33.9%｜历史 Rank 61%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 正 6,356 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/XBI_evening.json