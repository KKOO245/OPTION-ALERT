# 期权晚报 2026-09-29（快照 16:40 ET）

📊 市场环境

SPY $764.20 ｜ QQQ $737.93
VIX 16.04 ↓0.2%（5D +12.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 195C ΔOI +5,620（距现价 +4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 187.34 → 收盘 186.97（-0.2%） ｜ 今日高 188.63 ｜ 低 184.81 ｜ 昨收 187.48 → 收盘 186.97（-0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.73 | OI比 0.62 | ATM IV 48.8% | Skew 2.6pp | Term 0.93 | ExpMove ±3.5%（近端） | Rank 25%
量化视角： IV 历史低位（Rank 25%，期权偏便宜）｜期限结构正常（Term 0.93）｜保护溢价中性（Skew 2.6pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（3D）±3.5% ｜ 10-09（10D）±6.0% ｜ 10-16（17D）±8.0% ｜ 10-23（24D）±9.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 39,251,792 | GEX Change vs 上次快照 2,601,396 | Flip: Primary Flip: 179.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 557 / LOW 108 / INVALID 171
结构观察区: Primary Flip 179.68（全链重定价，覆盖 100%）
Put Wall 170（弱结构｜现价高于该位 10.0%） | Call Wall 200（现价低于该位 6.5%）
最近结构参考: Flip 180（现价高于该位 4.1%）
量化视角： 正 Gamma（3925万，无历史分位）｜正 Gamma 增强（+260万）｜现价位于 Flip 上方 4.06%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Put Wall，弱结构） / 182（MaxPain，仅结算参考）；上方 200（Call Wall）。
• Gamma 区域：切换参考 180（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +28.2k / P +8.3k ｜ Activity HIGH ｜ 3D
10-09  C +3.8k / P +2.0k ｜ Activity HIGH ｜ 10D
10-16  C +3.9k / P +0.3k ｜ Activity HIGH ｜ 17D
10-23  C +0.6k / P +0.7k ｜ Activity HIGH ｜ 24D

📆 10-02 Forward Structure
存量OI: C 128.6k / P 79.3k，今日变化ΔOI: C +28.2k / P +8.3k，平值价格ATM: C $3.13 / P $3.51 ｜ ATM IV 48.8%，净 delta 敞口 264k shares
Top ΔOI: C 200 +8,581 ｜ C 202 +7,500 ｜ C 195 +5,620
仓位参考: Max Pain 182 ｜ Call Wall 200（+7.0%）（OI 25.6k） ｜ Put Wall 177.5（-5.1%）（OI 8.7k）
量化解读： 存量 Call 重｜ATM IV 48.8%｜历史 Rank 25%（近端代理）｜IV/RV 1.55×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 264,442 股

📆 10-09 Forward Structure
存量OI: C 28.7k / P 40.3k，今日变化ΔOI: C +3.8k / P +2.0k，平值价格ATM: C $5.50 / P $5.75 ｜ ATM IV 44.9%，净 delta 敞口 35k shares
Top ΔOI: P 185 +1,333 ｜ C 187 +1,173 ｜ C 200 +340
仓位参考: Max Pain 185 ｜ Call Wall 200（+7.0%，弱）（OI 3.7k） ｜ Put Wall 190（+1.6%，弱）（OI 4.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 44.9%｜历史 Rank 25%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 35,137 股

📆 10-16 Forward Structure
存量OI: C 152.7k / P 169.0k，今日变化ΔOI: C +3.9k / P +0.3k，平值价格ATM: C $7.00 / P $7.90 ｜ ATM IV 44.6%，净 delta 敞口 69k shares
Top ΔOI: C 205 +1,713 ｜ C 200 +798 ｜ P 180 -659
仓位参考: Max Pain 165 ｜ Call Wall 170（-9.1%，弱）（OI 14.7k） ｜ Put Wall 170（-9.1%，弱）（OI 14.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 44.6%｜历史 Rank 25%（近端代理）｜IV/RV 1.41×（近似）｜净 delta 敞口 正 68,806 股

📆 10-23 Forward Structure
存量OI: C 19.7k / P 12.2k，今日变化ΔOI: C +0.6k / P +0.7k，平值价格ATM: C $8.15 / P $9.15 ｜ ATM IV 44.9%，净 delta 敞口 7k shares
Top ΔOI: P 165 +334 ｜ C 190 +232
仓位参考: Max Pain 180 ｜ Call Wall 180（-3.7%）（OI 4.6k） ｜ Put Wall 175（-6.4%）（OI 1.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 44.9%｜历史 Rank 25%（近端代理）｜IV/RV 1.42×（近似）｜净 delta 敞口 正 7,440 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/PLTR_evening.json