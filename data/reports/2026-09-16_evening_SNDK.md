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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,546.62 → 收盘 1,519.97（-1.7%） ｜ 今日高 1560.58 ｜ 低 1504.20 ｜ 昨收 1,530.90 → 收盘 1,519.97（-0.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-21，窗口结束前不做对错判定）

Options: P/C成交量 0.84 | OI比 1.10 | ATM IV 76.8% | Skew -0.0pp | Term 0.89 | ExpMove ±4.6%（近端） | Rank 31%
量化视角： IV 中性（Rank 31%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.10×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（2D）±4.6% ｜ 09-25（9D）±8.8% ｜ 10-02（16D）±11.7% ｜ 10-09（23D）±14.1%
   ⇒ IV–VIX Spread: +59.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,741,446 | GEX Change vs 上次快照 -4,626,695 | Flip: Primary Flip: 1581.24（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1818 / LOW 538 / INVALID 1020
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1581.24（全链重定价，覆盖 98%）
Put Wall 1,500（弱结构｜现价高于该位 1.3%）
最近结构参考: Put Wall 1500（现价高于该位 1.3%）
量化视角： 负 Gamma（974万，无历史分位）｜负 Gamma 加深（463万）｜现价位于 Flip 下方 3.87%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,500（Put Wall，弱结构） / 1,500（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1581（全链重定价，覆盖 98%）。
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
存量OI: C 91.0k / P 100.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $35.40 / P $34.24 ｜ ATM IV 76.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 1,500 ｜ Call Wall 1430（-5.9%，弱）（OI 2.2k） ｜ Put Wall 1400（-7.9%，弱）（OI 4.6k）
量化解读： 存量两侧均衡｜ATM IV 76.8%｜历史 Rank 31%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 1,580 ｜ Call Wall 1550（+2.0%，弱）（OI 0.5k） ｜ Put Wall 1500（-1.3%，弱）（OI 1.8k）

10-02（Activity LOW）仓位参考: Max Pain 1,580 ｜ Call Wall 1600（+5.3%，弱）（OI 0.5k） ｜ Put Wall 1500（-1.3%，弱）（OI 0.4k）

10-09（Activity LOW）仓位参考: Max Pain 1,620 ｜ Call Wall 1600（+5.3%，弱）（OI 0.1k） ｜ Put Wall 1500（-1.3%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 76.8% vs 09-25 67.8%（差 +9.0pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=22 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=22）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/SNDK_evening.json