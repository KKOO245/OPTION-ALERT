# 期权晨报 2026-09-01（快照 10:20 ET）

📊 市场环境

SPY $762.30 ｜ QQQ $708.35
VIX 15.71 ↑5.3%（5D +1.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.2（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-01 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.3 ｜ 实际 7.271 ｜ 前值 7.182　✅ 今日已公布
- 周二 09-01 10:00　【高】ISM 制造业 PMI　预测 55.2 ｜ 实际 54.6 ｜ 前值 55.6　✅ 今日已公布
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## PLTR

Options: P/C成交量 0.66 | OI比 0.82 | ATM IV 51.8% | Skew 1.5pp | Term 0.88 | ExpMove ±3.9%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价薄（Skew 1.5pp）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（3D）±3.9% ｜ 09-11（10D）±6.1% ｜ 09-18（17D）±7.7% ｜ 09-25（24D）±9.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 58,583,483 | GEX Change N/A | Flip: Primary Flip: 172.85（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 492 / LOW 142 / INVALID 292
结构观察区: Primary Flip 172.85（全链重定价，覆盖 100%）
Call Wall 190（弱结构｜现价低于该位 3.3%）
最近结构参考: Call Wall 190（现价低于该位 3.3%）
量化视角： 正 Gamma（5858万，无历史分位）｜现价位于 Flip 上方 6.34%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 173（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-04  C N/A / P N/A ｜ Activity LOW ｜ 3D（新上架）
09-11  C N/A / P N/A ｜ Activity LOW ｜ 10D（新上架）
09-18  C N/A / P N/A ｜ Activity LOW ｜ 17D（新上架）
09-25  C N/A / P N/A ｜ Activity LOW ｜ 24D（新上架）

📅 事件差分（观察，非因果）: 09-04（3D）ATM IV 51.8% vs 09-11 44.0%（差 +7.7pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 C ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-01/PLTR_morning.json