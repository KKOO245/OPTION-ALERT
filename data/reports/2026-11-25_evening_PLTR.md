# 期权晚报 2026-11-25（快照 16:40 ET）

📊 市场环境

SPY $716.70 ｜ QQQ $633.93
VIX 28.29 ↑7.3%（5D +15.2%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.2（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 0.6　✅ 今日已公布
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.7 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 4.3 ｜ 前值 1.5　✅ 今日已公布
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 0.2 ｜ 前值 1.8　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-27 162C ΔOI -1,010（距现价 -0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 154.22 → 收盘 163.59（+6.1%） ｜ 今日高 164.75 ｜ 低 151.51 ｜ 昨收 161.18 → 收盘 163.59（+1.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.64 | OI比 0.56 | ATM IV 57.7% | Skew 5.8pp | Term 1.02 | ExpMove ±3.4%（近端） | Rank 63%
量化视角： IV 中性（Rank 63%）｜期限结构正常（Term 1.02）｜保护溢价中性（Skew 5.8pp）｜存量 Call 偏重（OI比 0.56）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±3.4% ｜ 12-04（9D）±8.0% ｜ 12-11（16D）±10.6% ｜ 12-18（23D）±12.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 39,069,340 | GEX Change vs 上次快照 19,563,315 | Flip: Primary Flip: 152.64（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 502 / LOW 191 / INVALID 221
结构观察区: Primary Flip 152.64（全链重定价，覆盖 99%）
Call Wall 165（弱结构｜现价低于该位 0.9%）
最近结构参考: Call Wall 165（现价低于该位 0.9%）
量化视角： 正 Gamma（3907万，无历史分位）｜正 Gamma 增强（+1956万）｜现价位于 Flip 上方 7.18%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 152（MaxPain，仅结算参考）；上方 165（Call Wall，弱结构）。
• Gamma 区域：切换参考 153（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +2.4k / P +4.2k ｜ Activity HIGH ｜ 2D
12-04  C +2.6k / P +1.8k ｜ Activity HIGH ｜ 9D
12-11  C +1.4k / P +0.3k ｜ Activity HIGH ｜ 16D
12-18  C +1.2k / P +1.2k ｜ Activity MEDIUM △ ｜ 23D

📆 11-27 Forward Structure
存量OI: C 107.2k / P 60.2k，今日变化ΔOI: C +2.4k / P +4.2k，平值价格ATM: C $3.30 / P $2.19 ｜ ATM IV 57.7%，净 delta 敞口 -61k shares
Top ΔOI: C 162 -1,010 ｜ C 175 +980 ｜ C 167 +878
仓位参考: Max Pain 152 ｜ Call Wall 175（+7.0%，弱）（OI 11.7k） ｜ Put Wall 150（-8.3%，弱）（OI 4.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 57.7%｜历史 Rank 63%（近端代理）｜IV/RV 0.85×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 61,158 股

📆 12-04 Forward Structure
存量OI: C 35.4k / P 26.3k，今日变化ΔOI: C +2.6k / P +1.8k，平值价格ATM: C $7.25 / P $5.75 ｜ ATM IV 64.5%，净 delta 敞口 35k shares
Top ΔOI: C 180 +963 ｜ P 150 +294 ｜ C 175 +275
仓位参考: Max Pain 160 ｜ Call Wall 175（+7.0%，弱）（OI 1.9k） ｜ Put Wall 155（-5.3%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 64.5%｜历史 Rank 63%（近端代理）｜IV/RV 0.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 34,722 股

📆 12-11 Forward Structure
存量OI: C 13.5k / P 15.0k，今日变化ΔOI: C +1.4k / P +0.3k，平值价格ATM: C $9.52 / P $7.85 ｜ ATM IV 63.2%，净 delta 敞口 42k shares
Top ΔOI: C 180 +450 ｜ C 148 +298
仓位参考: Max Pain 160 ｜ Call Wall 175（+7.0%，弱）（OI 1.3k） ｜ Put Wall 150（-8.3%，弱）（OI 2.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 63.2%｜历史 Rank 63%（近端代理）｜IV/RV 0.93×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 42,274 股

12-18（MEDIUM △）Top ΔOI: 120P +856 ｜ 125P -745
12-18（MEDIUM △）仓位参考: Max Pain 140 ｜ Call Wall 165（+0.9%，弱）（OI 14.3k） ｜ Put Wall 160（-2.2%，弱）（OI 18.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/PLTR_evening.json