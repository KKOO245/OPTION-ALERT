# 期权晚报 2026-09-22（快照 16:40 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $747.46
VIX 14.21 ↓4.4%（5D -17.4%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 160C ΔOI +11,373（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 151.70 → 收盘 154.72（+2.0%） ｜ 今日高 154.94 ｜ 低 150.55 ｜ 昨收 151.85 → 收盘 154.72（+1.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.51 | OI比 0.88 | ATM IV 54.0% | Skew -0.4pp | Term 0.89 | ExpMove ±3.9%（近端） | Rank 27%
量化视角： IV 中性（Rank 27%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.88×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（3D）±3.9% ｜ 10-02（10D）±6.7% ｜ 10-09（17D）±8.4% ｜ 10-16（24D）±10.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 41,483,523 | GEX Change vs 上次快照 2,114,469 | Flip: Primary Flip: 151.40（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 548 / LOW 104 / INVALID 338
结构观察区: Primary Flip 151.40（全链重定价，覆盖 100%）
Call Wall 160（弱结构｜现价低于该位 3.3%）
最近结构参考: Flip 151（现价高于该位 2.2%）
量化视角： 正 Gamma（4148万，无历史分位）｜正 Gamma 增强（+211万）｜现价位于 Flip 上方 2.19%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（MaxPain，仅结算参考）；上方 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 151（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +65.3k / P +23.4k ｜ Activity HIGH ｜ 3D
10-02  C +13.0k / P +12.6k ｜ Activity HIGH ｜ 10D
10-09  C +3.5k / P +3.3k ｜ Activity HIGH ｜ 17D
10-16  C +19.1k / P +9.3k ｜ Activity HIGH ｜ 24D

📆 09-25 Forward Structure
存量OI: C 221.8k / P 195.2k，今日变化ΔOI: C +65.3k / P +23.4k，平值价格ATM: C $2.92 / P $3.15 ｜ ATM IV 54.0%，净 delta 敞口 719k shares
Top ΔOI: C 172 +15,012 ｜ C 160 +11,373 ｜ C 170 +7,555
仓位参考: Max Pain 150 ｜ Call Wall 170（+9.9%，弱）（OI 29.7k） ｜ Put Wall 140（-9.5%，弱）（OI 16.8k）
量化解读： 存量两侧均衡｜ATM IV 54.0%｜历史 Rank 27%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 719,179 股

📆 10-02 Forward Structure
存量OI: C 65.6k / P 77.4k，今日变化ΔOI: C +13.0k / P +12.6k，平值价格ATM: C $5.10 / P $5.26 ｜ ATM IV 50.4%，净 delta 敞口 22k shares
Top ΔOI: P 135 +3,471 ｜ C 175 +1,999
仓位参考: Max Pain 150 ｜ Call Wall 170（+9.9%，弱）（OI 8.3k） ｜ Put Wall 150（-3.1%，弱）（OI 4.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 50.4%｜历史 Rank 27%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 22,146 股

📆 10-09 Forward Structure
存量OI: C 24.1k / P 26.9k，今日变化ΔOI: C +3.5k / P +3.3k，平值价格ATM: C $6.53 / P $6.52 ｜ ATM IV 48.9%，净 delta 敞口 42k shares
Top ΔOI: C 160 +909 ｜ P 135 +632 ｜ C 155 +467
仓位参考: Max Pain 149 ｜ Call Wall 160（+3.4%，弱）（OI 2.5k） ｜ Put Wall 140（-9.5%，弱）（OI 1.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 48.9%｜历史 Rank 27%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 42,231 股

📆 10-16 Forward Structure
存量OI: C 314.8k / P 398.1k，今日变化ΔOI: C +19.1k / P +9.3k，平值价格ATM: C $7.70 / P $7.71 ｜ ATM IV 48.7%，净 delta 敞口 77k shares
Top ΔOI: C 172 +11,473 ｜ P 157 +4,126 ｜ P 150 +2,173
仓位参考: Max Pain 150 ｜ Call Wall 160（+3.4%，弱）（OI 35.2k） ｜ Put Wall 155（+0.2%，弱）（OI 49.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 48.7%｜历史 Rank 27%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 正 77,460 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/SPCX_evening.json