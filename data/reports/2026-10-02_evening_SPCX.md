# 期权晚报 2026-10-02（快照 16:40 ET）

📊 市场环境

SPY $769.64 ｜ QQQ $749.58
VIX 15.31 ↓6.6%（5D +3.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 155C ΔOI +2,254（距现价 -2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 149.55 → 收盘 158.96（+6.3%） ｜ 今日高 159.84 ｜ 低 149.34 ｜ 昨收 148.07 → 收盘 158.96（+7.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.98 | OI比 1.00 | ATM IV 45.9% | Skew 6.3pp | Term 0.95 | ExpMove ±4.6%（近端） | Rank 5%
量化视角： IV 历史低位（Rank 5%，期权偏便宜）｜期限结构正常（Term 0.95）｜保护溢价显著（Skew 6.3pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.98×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.00×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（7D）±4.6% ｜ 10-16（14D）±6.5% ｜ 10-23（21D）±8.1% ｜ 10-30（28D）±9.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 146,994,719 | GEX Change vs 上次快照 27,201,837 | Flip: Primary Flip: 146.04（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 469 / LOW 111 / INVALID 342
结构观察区: Primary Flip 146.04（全链重定价，覆盖 86%）
Call Wall 160（弱结构｜现价低于该位 0.6%）
最近结构参考: Call Wall 160（现价低于该位 0.6%）
量化视角： 正 Gamma（1.47亿，无历史分位）｜正 Gamma 增强（+2720万）｜现价位于 Flip 上方 8.84%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 149（MaxPain，仅结算参考）；上方 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 146（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +13.2k / P +16.8k ｜ Activity HIGH ｜ 7D
10-16  C +2.3k / P -0.8k ｜ Activity MEDIUM △ ｜ 14D
10-23  C +1.5k / P +0.7k ｜ Activity HIGH ｜ 21D
10-30  C +2.0k / P +1.6k ｜ Activity MEDIUM △ ｜ 28D

📆 10-09 Forward Structure
存量OI: C 98.0k / P 74.9k，今日变化ΔOI: C +13.2k / P +16.8k，平值价格ATM: C $3.15 / P $4.10 ｜ ATM IV 40.8%，净 delta 敞口 524k shares
Top ΔOI: P 142 +6,248 ｜ C 155 +2,254 ｜ P 146 +2,248
仓位参考: Max Pain 150 ｜ Call Wall 155（-2.5%，弱）（OI 8.7k） ｜ Put Wall 145（-8.8%，弱）（OI 4.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 40.8%｜历史 Rank 5%（近端代理）｜IV/RV 1.09×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 523,832 股

10-16（MEDIUM △）Top ΔOI: 170C +4,483 ｜ 145C -3,270
10-16（MEDIUM △）仓位参考: Max Pain 143 ｜ Call Wall 160（+0.7%）（OI 42.4k） ｜ Put Wall 150（-5.6%，弱）（OI 20.2k）

📆 10-23 Forward Structure
存量OI: C 29.0k / P 25.5k，今日变化ΔOI: C +1.5k / P +0.7k，平值价格ATM: C $6.00 / P $6.83 ｜ ATM IV 42.1%，净 delta 敞口 66k shares
Top ΔOI: C 152 +394 ｜ P 145 +265 ｜ C 150 +230
仓位参考: Max Pain 148 ｜ Call Wall 150（-5.6%，弱）（OI 3.8k） ｜ Put Wall 145（-8.8%，弱）（OI 2.6k）
量化解读： 存量两侧均衡｜ATM IV 42.1%｜历史 Rank 5%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 正 66,488 股

10-30（MEDIUM △）Top ΔOI: 152C +617
10-30（MEDIUM △）仓位参考: Max Pain 150 ｜ Call Wall 160（+0.7%，弱）（OI 2.8k） ｜ Put Wall 145（-8.8%，弱）（OI 3.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/SPCX_evening.json