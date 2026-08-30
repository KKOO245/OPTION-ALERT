# 期权晚报 2026-08-29

📊 市场环境

SPY $769.35 ｜ QQQ $716.43
VIX 14.43 ↑0.0%（5D -9.0%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 54.4（neutral）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **单日价格波动**: -2.5%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 晨报缺失（当日未生成），只报收盘事实
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.98 | OI比 0.76 | ATM IV 74.1% | Skew -2.6pp | Term 1.08 | ExpMove ±8.2%（近端） | Rank 26%
   ⇒ Put/Call Volume: 0.98×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（6D）±8.3% ｜ 09-11（13D）±11.8% ｜ 09-18（20D）±14.8% ｜ 09-25（27D）±17.3%
   ⇒ IV–VIX Spread: +59.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 221.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 596 / LOW 44 / INVALID 164
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: Primary Flip 221.96（全链重定价，覆盖 100%）
Put Wall 200（现价高于该位 4.6%） | Call Wall 300（现价低于该位 30.3%）
最近结构参考: Put Wall 200（现价高于该位 4.6%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall）；上方 300（Call Wall）。
• Gamma 区域：切换参考 222（全链重定价，覆盖 100%）。
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
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=2 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=2）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-29/NBIS_evening.json