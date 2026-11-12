# 期权晚报 2026-11-12（快照 16:40 ET）

📊 市场环境

SPY $757.12 ｜ QQQ $688.17
VIX 18.70 ↑6.9%（5D -33.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **事件差分**: 11-13（1D）ATM IV 56.5% vs 11-16 41.3%（差 +15.2pp），覆盖 成屋销售、PPI 生产者物价 MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-13 400C ΔOI +6,064（距现价 +0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-18 392P ΔOI +2,202 占该期限总 OI 10.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 385.85 → 收盘 397.45（+3.0%） ｜ 今日高 401.22 ｜ 低 385.20 ｜ 昨收 390.84 → 收盘 397.45（+1.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.46 | OI比 1.38 | ATM IV 56.5% | Skew 0.6pp | Term 0.70 | ExpMove ±2.4%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价薄（Skew 0.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.38×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±2.4% ｜ 11-16（4D）±3.5% ｜ 11-18（6D）±4.8% ｜ 11-20（8D）±5.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 126,802,430 | GEX Change vs 上次快照 26,655,151 | Flip: Primary Flip: 373.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1410 / LOW 188 / INVALID 1048
结构观察区: Primary Flip 373.27（全链重定价，覆盖 97%）
Call Wall 400（现价低于该位 0.6%）
最近结构参考: Call Wall 400（现价低于该位 0.6%）
量化视角： 正 Gamma（1.27亿，无历史分位）｜正 Gamma 增强（+2666万）｜现价位于 Flip 上方 6.48%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 368（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 373（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +21.5k / P +20.9k ｜ Activity HIGH ｜ 1D
11-16  C +8.0k / P +7.4k ｜ Activity HIGH ｜ 4D
11-18  C +2.5k / P +4.7k ｜ Activity HIGH ｜ 6D
11-20  C +2.4k / P +18.7k ｜ Activity HIGH ｜ 8D

📆 11-13 Forward Structure
存量OI: C 183.5k / P 254.0k，今日变化ΔOI: C +21.5k / P +20.9k，平值价格ATM: C $4.90 / P $4.69 ｜ ATM IV 56.5%，净 delta 敞口 327k shares
Top ΔOI: C 400 +6,064 ｜ C 392 +5,577 ｜ C 410 +2,936
仓位参考: Max Pain 368 ｜ Call Wall 400（+0.6%）（OI 19.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 56.5%｜历史 Rank 64%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 326,637 股

📆 11-16 Forward Structure
存量OI: C 31.3k / P 20.6k，今日变化ΔOI: C +8.0k / P +7.4k，平值价格ATM: C $6.70 / P $7.15 ｜ ATM IV 41.3%，净 delta 敞口 106k shares
Top ΔOI: P 360 +1,510
仓位参考: Max Pain 378 ｜ Call Wall 400（+0.6%，弱）（OI 2.0k） ｜ Put Wall 360（-9.4%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 41.3%｜历史 Rank 64%（近端代理）｜IV/RV 0.72×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 105,981 股

📆 11-18 Forward Structure
存量OI: C 10.1k / P 11.9k，今日变化ΔOI: C +2.5k / P +4.7k，平值价格ATM: C $9.70 / P $9.55 ｜ ATM IV 45.3%，净 delta 敞口 -66k shares
Top ΔOI: P 392 +2,202 ｜ P 387 +543 ｜ C 430 +266
仓位参考: Max Pain 390 ｜ Call Wall 410（+3.2%，弱）（OI 0.9k） ｜ Put Wall 392.5（-1.2%）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 45.3%｜历史 Rank 64%（近端代理）｜IV/RV 0.79×（近似）｜净 delta 敞口 负 65,744 股

📆 11-20 Forward Structure
存量OI: C 285.6k / P 328.4k，今日变化ΔOI: C +2.4k / P +18.7k，平值价格ATM: C $11.25 / P $10.95 ｜ ATM IV 47.3%，净 delta 敞口 4k shares
Top ΔOI: P 250 +9,626 ｜ P 372 -2,570
仓位参考: Max Pain 375 ｜ Call Wall 400（+0.6%，弱）（OI 21.8k）
量化解读： 存量两侧均衡｜ATM IV 47.3%｜历史 Rank 64%（近端代理）｜IV/RV 0.82×（近似）｜净 delta 敞口 正 4,257 股

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 56.5% vs 11-16 41.3%（差 +15.2pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/TSLA_evening.json