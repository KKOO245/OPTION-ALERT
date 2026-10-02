# 期权晚报 2026-10-01（快照 21:00 ET）

📊 市场环境

SPY $763.99 ｜ QQQ $742.03
VIX 16.39 ↑0.3%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-01

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 54.5 ｜ 前值 54.6　✅ 今日已公布
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 742.51 → 收盘 742.03（-0.1%） ｜ 今日高 744.67 ｜ 低 736.27 ｜ 昨收 739.77 → 收盘 742.03（+0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.33 | OI比 1.88 | ATM IV 22.0% | Skew 3.4pp | Term 0.90 | ExpMove ±0.9%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜保护溢价中性（Skew 3.4pp）｜当日成交偏 Put（P/C量 1.33）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.33×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.88×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 54% ｜ P/C OI(近端) 68%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 54%）｜近端持仓结构中性（P/C OI 分位 68%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-02（1D）±0.9% ｜ 10-05（4D）±1.3% ｜ 10-06（5D）±1.6% ｜ 10-07（6D）±1.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 19,908,964 | GEX Change vs 上次快照 155,964,845 | Flip: Primary Flip: 741.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 2744 / LOW 206 / INVALID 1676
结构观察区: Primary Flip 741.77（全链重定价，覆盖 98%）
Call Wall 760（现价低于该位 2.4%）
最近结构参考: Flip 742（现价高于该位 0.0%）
量化视角： 正 Gamma（1991万，历史分位 54%，中性区）｜由负转正（+1.56亿）｜现价位于 Flip 上方 0.03%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 735（MaxPain，仅结算参考）；上方 760（Call Wall）。
• Gamma 区域：切换参考 742（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-05  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-06  C +0 / P +0 ｜ Activity LOW ｜ 5D
10-07  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 10-02 Forward Structure
存量OI: C 257.6k / P 483.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.11 / P $2.91 ｜ ATM IV 22.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 735 ｜ Call Wall 725（-2.3%）（OI 35.1k） ｜ Put Wall 730（-1.6%，弱）（OI 48.9k）
量化解读： 存量 Put 重｜ATM IV 22.0%｜历史 Rank 69%（近端代理）｜IV/RV 1.50×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-05（Activity LOW）仓位参考: Max Pain 740 ｜ Call Wall 760（+2.4%，弱）（OI 8.0k） ｜ Put Wall 725（-2.3%，弱）（OI 7.7k）

10-06（Activity LOW）仓位参考: Max Pain 738 ｜ Call Wall 740（-0.3%，弱）（OI 1.4k） ｜ Put Wall 736（-0.8%，弱）（OI 3.9k）

10-07（Activity LOW）仓位参考: Max Pain 739 ｜ Call Wall 740（-0.3%，弱）（OI 2.3k）

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 22.0% vs 10-05 15.7%（差 +6.4pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/QQQ_evening.json