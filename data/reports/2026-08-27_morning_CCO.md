# 期权晨报 2026-08-27

📊 市场环境

SPY $770.63 ｜ QQQ $719.18
VIX 14.49 ↓4.7%（5D -9.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 58.3（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911


## CCO

🔍 重点速览
🔵 **Flip 状态**: CONDITIONAL（Candidates: 2.2）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
CCO  昨收 2.40 → 今晨 2.38（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 2.39 ｜ 低 2.38

Options: P/C量 N/A | OI比 0.28 | ATM IV 64.3% | Skew N/A | Term N/A | ExpMove ±12.6%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 数据不足 → 方向 Unknown
   ⇒ Put/Call OI: 0.28×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（22D）±15.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Candidates 2.20 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 待盘点 ｜ IV 有效性: VALID 0 / LOW 2 / INVALID 12
结构观察区: ≈2（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 2: +19.2% | 距 Call Wall 3: -20.5%
最近结构参考: Flip 2（距现价 +8.4%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 2（Put Wall）；上方 3（Call Wall）。
• Gamma 区域：切换参考 2（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 22D

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/CCO_morning.json