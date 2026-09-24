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
🟡 **近现价集中开仓**: 09-25 227C ΔOI +16,677（距现价 +1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-30 230C ΔOI +6,836 占该期限总 OI 13.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 222.12 → 收盘 224.58（+1.1%） ｜ 今日高 224.90 ｜ 低 221.09 ｜ 昨收 225.51 → 收盘 224.58（-0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.45 | OI比 0.70 | ATM IV 32.2% | Skew 2.0pp | Term 0.95 | ExpMove ±1.4%（近端） | Rank 11%
量化视角： IV 历史低位（Rank 11%，期权偏便宜）｜期限结构正常（Term 0.95）｜保护溢价薄（Skew 2.0pp）｜存量 Call 偏重（OI比 0.70）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.70×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（1D）±1.4% ｜ 09-28（4D）±2.1% ｜ 09-30（6D）±3.0% ｜ 10-02（8D）±3.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 564,098,857 | GEX Change vs 上次快照 -97,085,511 | Flip: Primary Flip: 215.71（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 677 / LOW 209 / INVALID 428
结构观察区: Primary Flip 215.71（全链重定价，覆盖 98%）
Call Wall 230（弱结构｜现价低于该位 2.4%）
最近结构参考: Call Wall 230（现价低于该位 2.4%）
量化视角： 正 Gamma（5.64亿，无历史分位）｜正 Gamma 减弱（9709万）｜现价位于 Flip 上方 4.11%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（MaxPain，仅结算参考）；上方 230（Call Wall，弱结构）。
• Gamma 区域：切换参考 216（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +39.4k / P +36.6k ｜ Activity HIGH ｜ 1D
09-28  C +13.8k / P +16.5k ｜ Activity HIGH ｜ 4D
09-30  C +15.2k / P +7.7k ｜ Activity HIGH ｜ 6D
10-02  C +29.1k / P +28.8k ｜ Activity HIGH ｜ 8D（新行权价 C 0.2k）

📆 09-25 Forward Structure
存量OI: C 517.4k / P 363.5k，今日变化ΔOI: C +39.4k / P +36.6k，平值价格ATM: C $1.35 / P $1.70 ｜ ATM IV 32.2%，净 delta 敞口 -679k shares
Top ΔOI: C 227 +16,677 ｜ P 220 +7,549 ｜ C 240 +6,600
仓位参考: Max Pain 220 ｜ Call Wall 230（+2.4%，弱）（OI 81.4k） ｜ Put Wall 220（-2.0%，弱）（OI 27.0k）
量化解读： 存量 Call 重｜ATM IV 32.2%｜历史 Rank 11%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 679,060 股

📆 09-28 Forward Structure
存量OI: C 52.7k / P 38.8k，今日变化ΔOI: C +13.8k / P +16.5k，平值价格ATM: C $2.18 / P $2.53 ｜ ATM IV 25.1%，净 delta 敞口 -116k shares
Top ΔOI: C 240 +3,203 ｜ P 220 +2,717
仓位参考: Max Pain 220 ｜ Call Wall 235（+4.6%，弱）（OI 11.7k） ｜ Put Wall 220（-2.0%，弱）（OI 3.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 25.1%｜历史 Rank 11%（近端代理）｜IV/RV 0.91×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 116,052 股

📆 09-30 Forward Structure
存量OI: C 30.2k / P 20.2k，今日变化ΔOI: C +15.2k / P +7.7k，平值价格ATM: C $3.17 / P $3.45 ｜ ATM IV 28.6%，净 delta 敞口 208k shares
Top ΔOI: C 230 +6,836 ｜ C 227 +3,505 ｜ C 232 +1,256
仓位参考: Max Pain 220 ｜ Call Wall 230（+2.4%）（OI 8.4k） ｜ Put Wall 212.5（-5.4%，弱）（OI 3.3k）
量化解读： 存量 Call 重｜ATM IV 28.6%｜历史 Rank 11%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 正 207,854 股

📆 10-02 Forward Structure
存量OI: C 208.5k / P 230.4k，今日变化ΔOI: C +29.1k / P +28.8k（新行权价 C 0.2k），平值价格ATM: C $3.90 / P $4.06 ｜ ATM IV 29.7%，净 delta 敞口 -74k shares
Top ΔOI: C 235 +10,469 ｜ C 242 +4,493 ｜ C 240 +4,243
仓位参考: Max Pain 220 ｜ Call Wall 235（+4.6%，弱）（OI 27.0k） ｜ Put Wall 210（-6.5%，弱）（OI 13.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 29.7%｜历史 Rank 11%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 负 74,420 股

📅 事件差分（观察，非因果）: 09-25（1D）ATM IV 32.2% vs 09-28 25.1%（差 +7.1pp）——覆盖 耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/NVDA_evening.json