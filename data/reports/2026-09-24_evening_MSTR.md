# 期权晚报 2026-09-24（快照 16:40 ET）

📊 市场环境

SPY $767.18 ｜ QQQ $741.10
VIX 15.67 ↑3.2%（5D -11.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 36.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **事件差分**: 09-25 ATM IV 79.5% vs 10-02 68.1%（差 +11.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-25 160P ΔOI +6,588（距现价 -1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 161.00 → 收盘 161.61（+0.4%） ｜ 今日高 165.14 ｜ 低 158.29 ｜ 昨收 162.20 → 收盘 161.61（-0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.47 | OI比 0.75 | ATM IV 79.5% | Skew -12.6pp | Term 0.84 | ExpMove ±3.3%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜Put 保护异常便宜（Skew -12.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（1D）±3.3% ｜ 10-02（8D）±8.1% ｜ 10-09（15D）±10.6% ｜ 10-16（22D）±13.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 70,580,538 | GEX Change vs 上次快照 8,808,875 | Flip: Primary Flip: 137.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 859 / LOW 103 / INVALID 182
结构观察区: Primary Flip 137.88（全链重定价，覆盖 99%）
最近结构参考: Flip 138（现价高于该位 17.2%）
量化视角： 正 Gamma（7058万，无历史分位）｜正 Gamma 增强（+881万）｜现价位于 Flip 上方 17.21%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 142（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 138（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +44.6k / P +20.3k ｜ Activity HIGH ｜ 1D（新行权价 C 0.2k）
10-02  C +10.9k / P +35.2k ｜ Activity HIGH ｜ 8D（新行权价 C 1.1k / P 83）
10-09  C +4.2k / P +5.4k ｜ Activity HIGH ｜ 15D
10-16  C -0.8k / P +8.4k ｜ Activity HIGH ｜ 22D

📆 09-25 Forward Structure
存量OI: C 309.3k / P 231.0k，今日变化ΔOI: C +44.6k / P +20.3k（新行权价 C 0.2k），平值价格ATM: C $2.31 / P $3.05 ｜ ATM IV 79.5%，净 delta 敞口 -336k shares
Top ΔOI: C 172 +9,890 ｜ C 177 +9,448 ｜ P 160 +6,588
仓位参考: Max Pain 142 ｜ Call Wall 155（-4.1%，弱）（OI 20.1k） ｜ Put Wall 160（-1.0%，弱）（OI 10.7k）
量化解读： 存量 Call 重｜ATM IV 79.5%｜历史 Rank 48%（近端代理）｜IV/RV 0.80×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 336,147 股

📆 10-02 Forward Structure
存量OI: C 63.9k / P 107.1k，今日变化ΔOI: C +10.9k / P +35.2k（新行权价 C 1.1k / P 83），平值价格ATM: C $6.25 / P $6.80 ｜ ATM IV 68.1%，净 delta 敞口 -820k shares
Top ΔOI: P 162 +9,712 ｜ P 150 +8,473
仓位参考: Max Pain 155 ｜ Call Wall 175（+8.3%，弱）（OI 4.1k） ｜ Put Wall 150（-7.2%，弱）（OI 10.8k）
量化解读： 存量 Put 重｜ATM IV 68.1%｜历史 Rank 48%（近端代理）｜IV/RV 0.69×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 819,540 股

📆 10-09 Forward Structure
存量OI: C 30.1k / P 44.5k，今日变化ΔOI: C +4.2k / P +5.4k，平值价格ATM: C $8.57 / P $8.62 ｜ ATM IV 66.7%，净 delta 敞口 -28k shares
Top ΔOI: C 172 +2,090
仓位参考: Max Pain 144 ｜ Call Wall 160（-1.0%，弱）（OI 5.1k） ｜ Put Wall 155（-4.1%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 66.7%｜历史 Rank 48%（近端代理）｜IV/RV 0.67×（近似）｜净 delta 敞口 负 28,062 股

📆 10-16 Forward Structure
存量OI: C 160.6k / P 141.7k，今日变化ΔOI: C -0.8k / P +8.4k，平值价格ATM: C $10.50 / P $10.75 ｜ ATM IV 67.1%，净 delta 敞口 -338k shares
Top ΔOI: C 175 +2,247 ｜ P 160 +1,406 ｜ C 180 -1,382
仓位参考: Max Pain 120 ｜ Call Wall 155（-4.1%，弱）（OI 10.4k） ｜ Put Wall 160（-1.0%，弱）（OI 4.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 67.1%｜历史 Rank 48%（近端代理）｜IV/RV 0.68×（近似）｜净 delta 敞口 负 337,968 股

📅 事件差分（观察，非因果）: 09-25（1D）ATM IV 79.5% vs 10-02 68.1%（差 +11.4pp）——覆盖 耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/MSTR_evening.json