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
🟡 **近现价集中开仓**: 10-02 182P ΔOI +672（距现价 -1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 185.09 → 收盘 184.99（-0.1%） ｜ 今日高 185.54 ｜ 低 182.03 ｜ 昨收 183.09 → 收盘 184.99（+1.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.54 | OI比 0.72 | ATM IV 49.5% | Skew 1.4pp | Term 0.93 | ExpMove ±3.6%（近端） | Rank 27%
量化视角： IV 中性（Rank 27%）｜期限结构正常（Term 0.93）｜保护溢价薄（Skew 1.4pp）｜存量 Call 偏重（OI比 0.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（3D）±3.6% ｜ 10-02（10D）±6.2% ｜ 10-09（17D）±7.9% ｜ 10-16（24D）±9.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 79,573,070 | GEX Change vs 上次快照 3,921,151 | Flip: Primary Flip: 170.84（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 607 / LOW 93 / INVALID 140
结构观察区: Primary Flip 170.84（全链重定价，覆盖 100%）
Put Wall 170（弱结构｜现价高于该位 8.8%） | Call Wall 180（弱结构｜现价高于该位 2.8%）
最近结构参考: Call Wall 180（现价高于该位 2.8%）
量化视角： 正 Gamma（7957万，无历史分位）｜正 Gamma 增强（+392万）｜现价位于 Flip 上方 8.28%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Put Wall，弱结构） / 175（MaxPain，仅结算参考） / 180（Call Wall，弱结构）。
• Gamma 区域：切换参考 171（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +28.1k / P +10.4k ｜ Activity HIGH ｜ 3D
10-02  C +4.6k / P +4.3k ｜ Activity HIGH ｜ 10D
10-09  C +1.9k / P +0.7k ｜ Activity HIGH ｜ 17D
10-16  C +9.8k / P +0.4k ｜ Activity HIGH ｜ 24D

📆 09-25 Forward Structure
存量OI: C 129.8k / P 93.1k，今日变化ΔOI: C +28.1k / P +10.4k，平值价格ATM: C $3.34 / P $3.30 ｜ ATM IV 49.5%，净 delta 敞口 197k shares
Top ΔOI: C 195 +10,076 ｜ C 197 +8,750 ｜ P 170 +2,653
仓位参考: Max Pain 175 ｜ Call Wall 180（-2.7%，弱）（OI 23.0k） ｜ Put Wall 170（-8.1%，弱）（OI 8.8k）
量化解读： 存量 Call 重｜ATM IV 49.5%｜历史 Rank 27%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 197,253 股

📆 10-02 Forward Structure
存量OI: C 31.5k / P 36.5k，今日变化ΔOI: C +4.6k / P +4.3k，平值价格ATM: C $5.78 / P $5.60 ｜ ATM IV 46.5%，净 delta 敞口 61k shares
Top ΔOI: C 200 +1,542 ｜ P 182 +672
仓位参考: Max Pain 175 ｜ Call Wall 200（+8.1%，弱）（OI 4.3k） ｜ Put Wall 170（-8.1%）（OI 5.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 46.5%｜历史 Rank 27%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 61,190 股

📆 10-09 Forward Structure
存量OI: C 16.6k / P 23.9k，今日变化ΔOI: C +1.9k / P +0.7k，平值价格ATM: C $7.45 / P $7.13 ｜ ATM IV 45.9%，净 delta 敞口 25k shares
Top ΔOI: C 200 +369
仓位参考: Max Pain 175 ｜ Call Wall 177.5（-4.0%，弱）（OI 3.1k） ｜ Put Wall 170（-8.1%，弱）（OI 3.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 45.9%｜历史 Rank 27%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 24,987 股

📆 10-16 Forward Structure
存量OI: C 138.8k / P 154.1k，今日变化ΔOI: C +9.8k / P +0.4k，平值价格ATM: C $8.94 / P $8.50 ｜ ATM IV 45.9%，净 delta 敞口 105k shares
Top ΔOI: C 225 +5,395 ｜ P 150 -864 ｜ C 200 +821
仓位参考: Max Pain 160 ｜ Call Wall 170（-8.1%，弱）（OI 15.5k） ｜ Put Wall 170（-8.1%，弱）（OI 14.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 45.9%｜历史 Rank 27%（近端代理）｜净 delta 敞口 正 105,499 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/PLTR_evening.json