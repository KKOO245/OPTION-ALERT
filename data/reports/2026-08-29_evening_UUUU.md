# 期权晚报 2026-08-29

📊 市场环境

SPY $769.35 ｜ QQQ $716.43
VIX 14.43 ↑0.0%（5D -9.0%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 54.4（neutral）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **单日价格波动**: -6.8%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## UUUU

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
UUUU: 晨报缺失（当日未生成），只报收盘事实
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.46 | OI比 0.39 | ATM IV 68.7% | Skew -1.5pp | Term 1.05 | ExpMove ±7.6%（近端） | Rank 26%
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.39×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（6D）±7.2% ｜ 09-11（13D）±10.9% ｜ 09-18（20D）±13.0% ｜ 09-25（27D）±17.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 194 / LOW 48 / INVALID 164
结构观察区: NO_CROSS
Put Wall 12（现价高于该位 22.3%） | Call Wall 18（现价低于该位 18.5%）
最近结构参考: Call Wall 18（现价低于该位 18.5%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 12（Put Wall）；上方 18（Call Wall）。
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

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-29/UUUU_evening.json