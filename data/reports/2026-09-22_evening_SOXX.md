# 期权晚报 2026-09-22（快照 16:40 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $747.46
VIX 14.21 ↓4.4%（5D -17.4%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 560C ΔOI +225（距现价 -2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 553.76 → 收盘 572.78（+3.4%） ｜ 今日高 573.50 ｜ 低 553.44 ｜ 昨收 559.34 → 收盘 572.78（+2.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.08 | OI比 1.49 | ATM IV 35.1% | Skew 2.3pp | Term 1.10 | ExpMove ±1.2%（近端） | Rank 56%
量化视角： IV 中性（Rank 56%）｜期限结构正常（Term 1.10）｜保护溢价中性（Skew 2.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.08×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.49×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（3D）±1.2% ｜ 10-02（10D）±1.8% ｜ 10-09（17D）±8.5% ｜ 10-16（24D）±7.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 12,771,917 | GEX Change vs 上次快照 4,175,838 | Flip: Primary Flip: 549.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 509 / LOW 239 / INVALID 758
结构观察区: Primary Flip 549.35（全链重定价，覆盖 96%）
Call Wall 600（现价低于该位 4.5%）
最近结构参考: Flip 549（现价高于该位 4.3%）
量化视角： 正 Gamma（1277万，无历史分位）｜正 Gamma 增强（+418万）｜现价位于 Flip 上方 4.27%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 530（MaxPain，仅结算参考）；上方 600（Call Wall）。
• Gamma 区域：切换参考 549（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +0.5k / P +1.2k ｜ Activity HIGH ｜ 3D
10-02  C +0.6k / P +0.8k ｜ Activity HIGH ｜ 10D
10-09  C +0.1k / P +57 ｜ Activity MEDIUM △ ｜ 17D
10-16  C +3.9k / P +1.2k ｜ Activity HIGH ｜ 24D

📆 09-25 Forward Structure
存量OI: C 11.5k / P 17.2k，今日变化ΔOI: C +0.5k / P +1.2k，平值价格ATM: C $7.18 / P $0.00 ｜ ATM IV 35.1%，净 delta 敞口 -282 shares
Top ΔOI: P 522 +288 ｜ P 550 +261 ｜ C 560 +225
仓位参考: Max Pain 530 ｜ Call Wall 580（+1.3%，弱）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 35.1%｜历史 Rank 56%（近端代理）｜IV/RV 0.92×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 282 股

📆 10-02 Forward Structure
存量OI: C 12.2k / P 11.9k，今日变化ΔOI: C +0.6k / P +0.8k，平值价格ATM: C $10.10 / P $0.00 ｜ ATM IV 36.2%，净 delta 敞口 20k shares
Top ΔOI: C 600 +134
仓位参考: Max Pain 520 ｜ Call Wall 542.5（-5.3%，弱）（OI 2.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 36.2%｜历史 Rank 56%（近端代理）｜IV/RV 0.95×（近似）｜净 delta 敞口 正 20,127 股

10-09（MEDIUM △）Top ΔOI: 530C +53 ｜ 525C -37
10-09（MEDIUM △）仓位参考: Max Pain 518 ｜ Call Wall 537.5（-6.2%，弱）（OI 0.4k）

📆 10-16 Forward Structure
存量OI: C 44.8k / P 81.3k，今日变化ΔOI: C +3.9k / P +1.2k，平值价格ATM: C $21.00 / P $23.70 ｜ ATM IV 38.0%，净 delta 敞口 59k shares
Top ΔOI: C 600 +4,498 ｜ C 550 -1,157 ｜ P 530 +1,082
仓位参考: Max Pain 525 ｜ Call Wall 600（+4.8%）（OI 13.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 38.0%｜历史 Rank 56%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 正 59,166 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/SOXX_evening.json