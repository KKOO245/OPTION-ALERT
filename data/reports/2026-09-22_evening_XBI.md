# 期权晚报 2026-09-22（快照 21:00 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $nan
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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 159.11 → 收盘 161.87（+1.7%） ｜ 今日高 162.48 ｜ 低 158.42 ｜ 昨收 158.23 → 收盘 161.87（+2.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 2.27 | OI比 3.66 | ATM IV 33.1% | Skew 1.8pp | Term 0.92 | ExpMove ±3.5%（近端） | Rank 50%
量化视角： IV 中性（Rank 50%）｜期限结构正常（Term 0.92）｜保护溢价薄（Skew 1.8pp）｜当日成交偏 Put（P/C量 2.27）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.27×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 3.66×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（3D）±3.5% ｜ 10-02（10D）±4.5% ｜ 10-09（17D）±1.5% ｜ 10-16（24D）±6.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,283,984 | GEX Change vs 上次快照 5,158,589 | Flip: Primary Flip: 163.24（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 370 / LOW 66 / INVALID 332
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 163.24（全链重定价，覆盖 94%）
最近结构参考: Flip 163（现价低于该位 0.8%）
量化视角： 负 Gamma（528万，无历史分位）｜负 Gamma 缓解（+516万）｜现价位于 Flip 下方 0.84%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 157（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 163（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 10D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 17D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 09-25 Forward Structure
存量OI: C 11.8k / P 43.4k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.77 / P $4.82 ｜ ATM IV 33.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 157 ｜ Call Wall 160（-1.2%，弱）（OI 2.7k） ｜ Put Wall 156（-3.6%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜ATM IV 33.1%｜历史 Rank 50%（近端代理）｜IV/RV 1.55×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-02（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 165（+1.9%）（OI 1.0k） ｜ Put Wall 157（-3.0%，弱）（OI 0.2k）

10-09（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 172（+6.3%，弱）（OI 38）

10-16（Activity LOW）仓位参考: Max Pain 165 ｜ Call Wall 170（+5.0%，弱）（OI 5.0k） ｜ Put Wall 153（-5.5%，弱）（OI 6.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/XBI_evening.json