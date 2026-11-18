# 期权晚报 2026-11-18（快照 16:40 ET）

📊 市场环境

SPY $730.20 ｜ QQQ $659.51
VIX 24.56 ↓3.5%（5D +40.4%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 11-20（2D）ATM IV 74.1% vs 11-23 57.4%（差 +16.8pp），覆盖 新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-20 145C ΔOI -6,971（距现价 +1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 143.23 → 收盘 143.50（+0.2%） ｜ 今日高 146.30 ｜ 低 141.22 ｜ 昨收 141.70 → 收盘 143.50（+1.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.72 | OI比 0.79 | ATM IV 71.3% | Skew 10.2pp | Term 0.75 | ExpMove ±4.4%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜保护溢价显著（Skew 10.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.72×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（2D）±4.4% ｜ 11-23（5D）±5.3% ｜ 11-25（7D）±6.3% ｜ 11-27（9D）±6.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 61,085,009 | GEX Change vs 上次快照 -10,433,044 | Flip: Primary Flip: 140.13（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 720 / LOW 249 / INVALID 595
结构观察区: Primary Flip 140.13（全链重定价，覆盖 94%）
Put Wall 140（弱结构｜现价高于该位 2.5%）
最近结构参考: Flip 140（现价高于该位 2.4%）
量化视角： 正 Gamma（6109万，无历史分位）｜正 Gamma 减弱（1043万）｜现价位于 Flip 上方 2.40%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（Put Wall，弱结构） / 138（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 140（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C -2.1k / P -0.3k ｜ Activity MEDIUM △ ｜ 2D
11-23  C +4.4k / P +2.6k ｜ Activity HIGH ｜ 5D
11-25  C +1.1k / P +0.5k ｜ Activity HIGH ｜ 7D
11-27  C +4.7k / P +4.4k ｜ Activity HIGH ｜ 9D

📆 11-20 Forward Structure
存量OI: C 534.3k / P 439.4k，今日变化ΔOI: C -2.1k / P -0.3k，平值价格ATM: C $3.40 / P $2.89 ｜ ATM IV 74.1%，净 delta 敞口 158k shares
Top ΔOI: C 145 -6,971 ｜ C 150 +6,302
仓位参考: Max Pain 145 ｜ Call Wall 150（+4.5%，弱）（OI 47.9k） ｜ Put Wall 135（-5.9%，弱）（OI 41.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 74.1%｜历史 Rank 74%（近端代理）｜IV/RV 1.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 157,562 股

📆 11-23 Forward Structure
存量OI: C 10.8k / P 7.5k，今日变化ΔOI: C +4.4k / P +2.6k，平值价格ATM: C $4.05 / P $3.60 ｜ ATM IV 57.4%，净 delta 敞口 51k shares
Top ΔOI: C 150 +1,170 ｜ C 152 +917 ｜ P 140 +888
仓位参考: Max Pain 140 ｜ Call Wall 150（+4.5%）（OI 2.6k） ｜ Put Wall 140（-2.4%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 57.4%｜历史 Rank 74%（近端代理）｜IV/RV 0.93×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 50,963 股

📆 11-25 Forward Structure
存量OI: C 3.8k / P 2.9k，今日变化ΔOI: C +1.1k / P +0.5k，平值价格ATM: C $4.85 / P $4.15 ｜ ATM IV 58.0%，净 delta 敞口 33k shares
Top ΔOI: C 150 +186 ｜ C 142 +173
仓位参考: Max Pain 139 ｜ Call Wall 150（+4.5%，弱）（OI 0.7k） ｜ Put Wall 130（-9.4%）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 58.0%｜历史 Rank 74%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 32,746 股

📆 11-27 Forward Structure
存量OI: C 127.8k / P 57.4k，今日变化ΔOI: C +4.7k / P +4.4k，平值价格ATM: C $5.20 / P $4.70 ｜ ATM IV 54.8%，净 delta 敞口 54k shares
Top ΔOI: C 150 +1,204
仓位参考: Max Pain 140 ｜ Call Wall 150（+4.5%，弱）（OI 9.4k） ｜ Put Wall 140（-2.4%，弱）（OI 3.6k）
量化解读： 存量 Call 重｜ATM IV 54.8%｜历史 Rank 74%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 正 54,267 股

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 74.1% vs 11-23 57.4%（差 +16.8pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/SPCX_evening.json