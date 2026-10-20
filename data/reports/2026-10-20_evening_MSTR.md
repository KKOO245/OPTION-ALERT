# 期权晚报 2026-10-20（快照 16:40 ET）

📊 市场环境

SPY $769.05 ｜ QQQ $717.63
VIX 17.31 ↓6.1%（5D +13.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 145C ΔOI +5,930（距现价 +1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 133.76 → 收盘 142.72（+6.7%） ｜ 今日高 146.75 ｜ 低 133.60 ｜ 昨收 136.02 → 收盘 142.72（+4.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.73 | OI比 0.76 | ATM IV 74.4% | Skew 0.0pp | Term 0.92 | ExpMove ±5.4%（近端） | Rank 37%
量化视角： IV 中性（Rank 37%）｜期限结构正常（Term 0.92）｜保护溢价薄（Skew 0.0pp）｜存量 Call 偏重（OI比 0.76）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（3D）±5.4% ｜ 10-30（10D）±9.6% ｜ 11-06（17D）±12.4% ｜ 11-13（24D）±14.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 54,272,524 | GEX Change vs 上次快照 23,202,769 | Flip: Primary Flip: 132.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 639 / LOW 72 / INVALID 193
结构观察区: Primary Flip 132.68（全链重定价，覆盖 100%）
Call Wall 135（弱结构｜现价高于该位 5.7%）
最近结构参考: Call Wall 135（现价高于该位 5.7%）
量化视角： 正 Gamma（5427万，无历史分位）｜正 Gamma 增强（+2320万）｜现价位于 Flip 上方 7.56%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 141（MaxPain，仅结算参考） / 135（Call Wall，弱结构）。
• Gamma 区域：切换参考 133（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +21.6k / P +3.7k ｜ Activity HIGH ｜ 3D
10-30  C +2.5k / P +8.1k ｜ Activity HIGH ｜ 10D
11-06  C +1.3k / P +3.3k ｜ Activity HIGH ｜ 17D
11-13  C +1.5k / P +3.6k ｜ Activity HIGH ｜ 24D

📆 10-23 Forward Structure
存量OI: C 230.3k / P 174.5k，今日变化ΔOI: C +21.6k / P +3.7k，平值价格ATM: C $3.77 / P $3.95 ｜ ATM IV 74.4%，净 delta 敞口 846k shares
Top ΔOI: C 150 +6,322 ｜ C 145 +5,930 ｜ C 141 +2,238
仓位参考: Max Pain 141 ｜ Call Wall 155（+8.6%，弱）（OI 26.4k） ｜ Put Wall 140（-1.9%，弱）（OI 6.5k）
量化解读： 存量 Call 重｜ATM IV 74.4%｜历史 Rank 37%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 846,038 股

📆 10-30 Forward Structure
存量OI: C 47.1k / P 78.1k，今日变化ΔOI: C +2.5k / P +8.1k，平值价格ATM: C $6.80 / P $6.89 ｜ ATM IV 72.6%，净 delta 敞口 69k shares
Top ΔOI: P 115 +4,047 ｜ P 125 -1,011
仓位参考: Max Pain 155 ｜ Call Wall 155（+8.6%，弱）（OI 2.1k） ｜ Put Wall 155（+8.6%，弱）（OI 3.9k）
量化解读： 存量 Put 重｜ATM IV 72.6%｜历史 Rank 37%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 69,426 股

📆 11-06 Forward Structure
存量OI: C 13.8k / P 29.0k，今日变化ΔOI: C +1.3k / P +3.3k，平值价格ATM: C $8.90 / P $8.82 ｜ ATM IV 71.2%，净 delta 敞口 13k shares
仓位参考: Max Pain 160 ｜ Call Wall 155（+8.6%，弱）（OI 0.8k） ｜ Put Wall 155（+8.6%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜ATM IV 71.2%｜历史 Rank 37%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 13,055 股

📆 11-13 Forward Structure
存量OI: C 12.0k / P 23.0k，今日变化ΔOI: C +1.5k / P +3.6k，平值价格ATM: C $10.35 / P $10.13 ｜ ATM IV 69.8%，净 delta 敞口 -3k shares
仓位参考: Max Pain 160 ｜ Call Wall 144（+0.9%，弱）（OI 0.7k） ｜ Put Wall 155（+8.6%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜ATM IV 69.8%｜历史 Rank 37%（近端代理）｜IV/RV 1.22×（近似）｜净 delta 敞口 负 3,228 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/MSTR_evening.json