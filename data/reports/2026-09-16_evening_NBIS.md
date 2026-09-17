# 期权晚报 2026-09-16（快照 21:12 ET）

📊 市场环境

SPY $754.05 ｜ QQQ $704.72
VIX 17.71 ↑3.0%（5D +7.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 3.75　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　✅ 今日已公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **事件差分**: 09-18 ATM IV 91.7% vs 09-25 78.3%（差 +13.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 212.09 → 收盘 209.37（-1.3%） ｜ 今日高 220.40 ｜ 低 208.48 ｜ 昨收 207.37 → 收盘 209.37（+1.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.65 | OI比 1.30 | ATM IV 91.7% | Skew -2.0pp | Term 0.86 | ExpMove ±5.4%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.30×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（2D）±5.4% ｜ 09-25（9D）±10.0% ｜ 10-02（16D）±13.4% ｜ 10-09（23D）±15.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -14,574,505 | GEX Change vs 上次快照 -5,613,027 | Flip: Primary Flip: 224.62（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 518 / LOW 84 / INVALID 164
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 224.62（全链重定价，覆盖 99%）
Put Wall 200（弱结构｜现价高于该位 4.7%）
最近结构参考: Put Wall 200（现价高于该位 4.7%）
量化视角： 负 Gamma（1457万，无历史分位）｜负 Gamma 加深（561万）｜现价位于 Flip 下方 6.79%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 225（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 9D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-18 Forward Structure
存量OI: C 140.1k / P 182.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.36 / P $5.98 ｜ ATM IV 91.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 220 ｜ Call Wall 200（-4.5%，弱）（OI 7.2k） ｜ Put Wall 210（+0.3%，弱）（OI 10.5k）
量化解读： 存量 Put 重｜ATM IV 91.7%｜历史 Rank 26%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 212 ｜ Call Wall 227.5（+8.7%）（OI 3.0k） ｜ Put Wall 200（-4.5%，弱）（OI 2.3k）

10-02（Activity LOW）仓位参考: Max Pain 220 ｜ Call Wall 210（+0.3%，弱）（OI 0.3k） ｜ Put Wall 190（-9.3%，弱）（OI 0.7k）

10-09（Activity LOW）仓位参考: Max Pain 220 ｜ Call Wall 215（+2.7%，弱）（OI 0.4k） ｜ Put Wall 200（-4.5%，弱）（OI 0.7k）

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 91.7% vs 09-25 78.3%（差 +13.3pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/NBIS_evening.json