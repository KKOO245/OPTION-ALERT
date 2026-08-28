# 期权晚报 2026-08-28

📊 市场环境

SPY $769.35 ｜ QQQ $716.43
VIX 14.43 ↓0.6%（5D -4.6%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 54.4（neutral）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 -79 ｜ 前值 -911　✅ 今日已公布
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

💾 每周本地备份提醒：请在 `D:\git\Option Alert-数据储存` 运行 `git pull`，把本周数据拉到本地。报告由 GitHub 自动发送，本地只做数据镜像。


## CCO

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
CCO: 今开 2.39 → 收盘 2.34（-2.1%） ｜ 今日高 2.39 ｜ 低 2.33
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 N/A | OI比 0.28 | ATM IV 209.0% | Skew N/A | Term N/A | ExpMove ±21.4%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 数据不足 → 方向 Unknown
   ⇒ Put/Call OI: 0.28×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（21D）±16.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 38%（带内） ｜ IV 有效性: VALID 0 / LOW 3 / INVALID 11
结构观察区: NO_CROSS
Put Wall 2（现价高于该位 17.0%） | Call Wall 3（现价低于该位 22.0%）
最近结构参考: Put Wall 2（现价高于该位 17.0%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 2（Put Wall）；上方 3（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 21D

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/CCO_evening.json