# 期权晚报 2026-08-29

📊 市场环境

SPY $769.35 ｜ QQQ $716.43
VIX 14.43 ↑0.0%（5D -9.0%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 54.4（neutral）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 晨报缺失（当日未生成），只报收盘事实
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 1.28 | OI比 0.76 | ATM IV 9.4% | Skew 3.3pp | Term 1.81 | ExpMove ±0.7%（近端） | Rank 6%
   ⇒ Put/Call Volume: 1.28×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-31（2D）±0.7% ｜ 09-01（3D）±1.0% ｜ 09-02（4D）±1.2% ｜ 09-03（5D）±1.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 715.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 2872 / LOW 525 / INVALID 2195
结构观察区: Primary Flip 715.68（全链重定价，覆盖 96%）
Put Wall 700（现价高于该位 2.3%） | Call Wall 750（现价低于该位 4.5%）
最近结构参考: Flip 716（现价高于该位 0.1%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall）；上方 750（Call Wall）。
• Gamma 区域：切换参考 716（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

08-31  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-01  C +0 / P +0 ｜ Activity LOW ｜ 3D
09-02  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-03  C +0 / P +0 ｜ Activity LOW ｜ 5D

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-29/QQQ_evening.json