# 期权晚报 2026-09-17（快照 21:08 ET）

📊 市场环境

SPY $762.60 ｜ QQQ $nan
VIX 15.44 ↓12.8%（5D -13.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览
🔵 **Flip 状态**: CONDITIONAL（Candidates: 523.3）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 517.53 → 收盘 519.10（+0.3%） ｜ 今日高 520.42 ｜ 低 514.80 ｜ 昨收 502.06 → 收盘 519.10（+3.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 2.70 | OI比 0.88 | ATM IV 29.8% | Skew -0.6pp | Term 1.19 | ExpMove ±1.3%（近端） | Rank 35%
量化视角： IV 中性（Rank 35%）｜期限结构正常偏陡（Term 1.19）｜Put 保护异常便宜（Skew -0.6pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 2.70）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.70×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.88×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（1D）±1.3% ｜ 09-25（8D）±3.8% ｜ 10-02（15D）±5.5% ｜ 10-09（22D）±7.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -13,042,908 | GEX Change vs 上次快照 3,807,375 | Flip: Candidates 523.34 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 77%（带内） ｜ IV 有效性: VALID 521 / LOW 395 / INVALID 710
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈523（全链重定价，覆盖 77%，CONDITIONAL）
最近结构参考: Flip 523（现价低于该位 0.8%）
量化视角： 负 Gamma（1304万，无历史分位）｜负 Gamma 缓解（+381万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 518（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 523（全链重定价，覆盖 77%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 8D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 15D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 22D

📆 09-18 Forward Structure
存量OI: C 104.9k / P 92.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.40 / P $3.58 ｜ ATM IV 29.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 518 ｜ Call Wall 560（+7.9%，弱）（OI 14.6k） ｜ Put Wall 480（-7.5%，弱）（OI 8.6k）
量化解读： 存量两侧均衡｜ATM IV 29.8%｜历史 Rank 35%（近端代理）｜IV/RV 0.85×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 515 ｜ Put Wall 480（-7.5%，弱）（OI 2.0k）

10-02（Activity LOW）仓位参考: Max Pain 505 ｜ Call Wall 542.5（+4.5%，弱）（OI 2.8k） ｜ Put Wall 470（-9.5%）（OI 3.0k）

10-09（Activity LOW）仓位参考: Max Pain 510 ｜ Call Wall 525（+1.1%）（OI 1.6k） ｜ Put Wall 485（-6.6%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/SOXX_evening.json