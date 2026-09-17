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


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 507.50 → 收盘 502.06（-1.1%） ｜ 今日高 510.37 ｜ 低 496.81 ｜ 昨收 498.85 → 收盘 502.06（+0.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.51 | OI比 0.90 | ATM IV 40.9% | Skew 4.7pp | Term 0.93 | ExpMove ±2.5%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构正常（Term 0.93）｜保护溢价中性（Skew 4.7pp）｜当日成交偏 Put（P/C量 1.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.51×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（2D）±2.5% ｜ 09-25（9D）±4.7% ｜ 10-02（16D）±6.4% ｜ 10-09（23D）±7.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -42,365,063 | GEX Change vs 上次快照 -9,235,404 | Flip: Primary Flip: 524.26（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 560 / LOW 353 / INVALID 713
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 524.26（全链重定价，覆盖 88%）
最近结构参考: Flip 524（现价低于该位 4.2%）
量化视角： 负 Gamma（4237万，无历史分位）｜负 Gamma 加深（924万）｜现价位于 Flip 下方 4.23%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 520（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 524（全链重定价，覆盖 88%）。
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
存量OI: C 104.3k / P 94.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.36 / P $6.99 ｜ ATM IV 40.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 520 ｜ Call Wall 535（+6.6%，弱）（OI 3.8k） ｜ Put Wall 480（-4.4%，弱）（OI 8.0k）
量化解读： 存量两侧均衡｜ATM IV 40.9%｜历史 Rank 72%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 520 ｜ Put Wall 480（-4.4%，弱）（OI 2.0k）

10-02（Activity LOW）仓位参考: Max Pain 512 ｜ Call Wall 542.5（+8.1%，弱）（OI 2.8k） ｜ Put Wall 470（-6.4%）（OI 3.0k）

10-09（Activity LOW）仓位参考: Max Pain 510 ｜ Call Wall 525（+4.6%）（OI 1.6k） ｜ Put Wall 465（-7.4%）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/SOXX_evening.json