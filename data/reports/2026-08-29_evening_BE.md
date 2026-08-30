# 期权晚报 2026-08-29

📊 市场环境

SPY $769.35 ｜ QQQ $716.43
VIX 14.43 ↑0.0%（5D -9.0%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 54.4（neutral）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **单日价格波动**: -2.4%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 晨报缺失（当日未生成），只报收盘事实
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 1.21 | OI比 1.25 | ATM IV 81.5% | Skew -5.2pp | Term 0.97 | ExpMove ±9.0%（近端） | Rank 26%
   ⇒ Put/Call Volume: 1.21×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.25×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-04（6D）±9.1% ｜ 09-11（13D）±13.0% ｜ 09-18（20D）±15.0% ｜ 09-25（27D）±18.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 202.37（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 526 / LOW 47 / INVALID 225
结构观察区: Primary Flip 202.37（全链重定价，覆盖 100%）
Put Wall 180（现价高于该位 17.1%） | Call Wall 250（现价低于该位 15.7%）
最近结构参考: Flip 202（现价高于该位 4.2%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（Put Wall）；上方 250（Call Wall）。
• Gamma 区域：切换参考 202（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-04  C +0 / P +0 ｜ Activity LOW ｜ 6D
09-11  C +0 / P +0 ｜ Activity LOW ｜ 13D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 20D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 27D

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-29/BE_evening.json