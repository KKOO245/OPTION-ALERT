# 期权晨报 2026-08-31

📊 市场环境

SPY $765.79 ｜ QQQ $714.47
VIX 15.33 ↑6.2%（5D -3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 50.4（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-01 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.3 ｜ 实际 待公布 ｜ 前值 7.359
- 周二 09-01 10:00　【高】ISM 制造业 PMI　预测 55.2 ｜ 实际 待公布 ｜ 前值 55.6
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🔵 **Flip 状态**: CONDITIONAL（Candidates: 2.2）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读


## CCO

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
CCO  昨收 2.34 → 今晨 2.35（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 2.35 ｜ 低 2.34

Options: P/C量 N/A | OI比 0.28 | ATM IV 62.1% | Skew N/A | Term N/A | ExpMove ±10.7%（近端） | Rank 9%
   ⇒ Put/Call Volume: 数据不足 → 方向 Unknown
   ⇒ Put/Call OI: 0.28×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（18D）±16.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Candidates 2.21 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 38%（带内） ｜ IV 有效性: VALID 0 / LOW 3 / INVALID 11
结构观察区: ≈2（全链重定价，覆盖 38%，CONDITIONAL）
最近结构参考: Flip 2（现价高于该位 6.1%）
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 2（全链重定价，覆盖 38%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 18D

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/CCO_morning.json