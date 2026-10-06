# 期权晚报 2026-10-06（快照 16:40 ET）

📊 市场环境

SPY $779.09 ｜ QQQ $759.66
VIX 15.01 ↓3.3%（5D -6.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.3（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 195C ΔOI +6,306（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 191.00 → 收盘 192.07（+0.6%） ｜ 今日高 194.56 ｜ 低 190.25 ｜ 昨收 189.40 → 收盘 192.07（+1.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.38 | OI比 0.62 | ATM IV 44.5% | Skew 1.8pp | Term 1.27 | ExpMove ±3.2%（近端） | Rank 24%
量化视角： IV 历史低位（Rank 24%，期权偏便宜）｜期限结构正常偏陡（Term 1.27）｜保护溢价薄（Skew 1.8pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（3D）±3.2% ｜ 10-16（10D）±5.5% ｜ 10-23（17D）±7.2% ｜ 10-30（24D）±8.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 69,935,274 | GEX Change vs 上次快照 -8,152,474 | Flip: Primary Flip: 181.01（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 568 / LOW 81 / INVALID 163
结构观察区: Primary Flip 181.01（全链重定价，覆盖 100%）
Call Wall 200（弱结构｜现价低于该位 4.0%）
最近结构参考: Call Wall 200（现价低于该位 4.0%）
量化视角： 正 Gamma（6994万，无历史分位）｜正 Gamma 减弱（815万）｜现价位于 Flip 上方 6.11%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 188（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 181（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +26.4k / P +7.5k ｜ Activity HIGH ｜ 3D
10-16  C -2.1k / P +4.2k ｜ Activity HIGH ｜ 10D
10-23  C +1.4k / P +1.9k ｜ Activity HIGH ｜ 17D
10-30  C +1.4k / P +1.3k ｜ Activity HIGH ｜ 24D

📆 10-09 Forward Structure
存量OI: C 117.1k / P 72.7k，今日变化ΔOI: C +26.4k / P +7.5k，平值价格ATM: C $3.05 / P $3.20 ｜ ATM IV 44.5%，净 delta 敞口 387k shares
Top ΔOI: C 205 +10,249 ｜ C 195 +6,306 ｜ C 202 +2,814
仓位参考: Max Pain 188 ｜ Call Wall 205（+6.7%，弱）（OI 20.5k） ｜ Put Wall 185（-3.7%，弱）（OI 7.0k）
量化解读： 存量 Call 重｜ATM IV 44.5%｜历史 Rank 24%（近端代理）｜IV/RV 1.97×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 386,514 股

📆 10-16 Forward Structure
存量OI: C 155.3k / P 192.1k，今日变化ΔOI: C -2.1k / P +4.2k，平值价格ATM: C $5.25 / P $5.35 ｜ ATM IV 41.9%，净 delta 敞口 -487k shares
Top ΔOI: C 170 -6,445 ｜ C 192 +1,129 ｜ C 182 +1,061
仓位参考: Max Pain 170 ｜ Call Wall 200（+4.1%）（OI 16.4k） ｜ Put Wall 175（-8.9%，弱）（OI 9.0k）
量化解读： 存量 Put 重｜ATM IV 41.9%｜历史 Rank 24%（近端代理）｜IV/RV 1.86×（近似）｜净 delta 敞口 负 487,248 股

📆 10-23 Forward Structure
存量OI: C 23.7k / P 18.1k，今日变化ΔOI: C +1.4k / P +1.9k，平值价格ATM: C $6.93 / P $6.82 ｜ ATM IV 41.4%，净 delta 敞口 33k shares
Top ΔOI: C 192 +609 ｜ P 175 +301
仓位参考: Max Pain 180 ｜ Call Wall 180（-6.3%）（OI 4.6k） ｜ Put Wall 175（-8.9%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 41.4%｜历史 Rank 24%（近端代理）｜IV/RV 1.84×（近似）｜净 delta 敞口 正 32,816 股

📆 10-30 Forward Structure
存量OI: C 26.2k / P 17.8k，今日变化ΔOI: C +1.4k / P +1.3k，平值价格ATM: C $8.43 / P $8.27 ｜ ATM IV 42.3%，净 delta 敞口 42k shares
Top ΔOI: C 185 +471 ｜ P 187 +296
仓位参考: Max Pain 182 ｜ Call Wall 192.5（+0.2%，弱）（OI 2.7k） ｜ Put Wall 180（-6.3%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 42.3%｜历史 Rank 24%（近端代理）｜IV/RV 1.88×（近似）｜净 delta 敞口 正 41,764 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/PLTR_evening.json