# 期权晚报 2026-10-05（快照 16:51 ET）

📊 市场环境

SPY $774.83 ｜ QQQ $756.20
VIX 15.52 ↑1.4%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 43.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 10-05 10:00　【高】ISM 非制造业 PMI　预测 55 ｜ 实际 54.9 ｜ 前值 55.4　✅ 今日已公布
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-07 382C ΔOI +4,274（距现价 +1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 368.80 → 收盘 378.73（+2.7%） ｜ 今日高 381.59 ｜ 低 364.91 ｜ 昨收 370.59 → 收盘 378.73（+2.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.69 | OI比 0.48 | ATM IV 20.7% | Skew 11.2pp | Term 2.10 | ExpMove ±2.3%（近端） | Rank 20%
量化视角： IV 历史低位（Rank 20%，期权偏便宜）｜期限结构正常偏陡（Term 2.10）｜保护溢价显著（Skew 11.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.48）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.69×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.48×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-07（2D）±2.3% ｜ 10-09（4D）±3.5% ｜ 10-12（7D）±3.8% ｜ 10-14（9D）±4.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 160,288,475 | GEX Change vs 上次快照 17,385,251 | Flip: Primary Flip: 354.13（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 1124 / LOW 150 / INVALID 594
结构观察区: Primary Flip 354.13（全链重定价，覆盖 88%）
Call Wall 400（弱结构｜现价低于该位 5.3%）
最近结构参考: Call Wall 400（现价低于该位 5.3%）
量化视角： 正 Gamma（1.60亿，无历史分位）｜正 Gamma 增强（+1739万）｜现价位于 Flip 上方 6.95%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 365（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 354（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 200.0P — Vol 14 | 最新价 $0.04 | OI 3943→29669 (ΔOI +25726张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增25726张（+652.5% vs前日OI），连续性待观察（方向未知）
10-09 150.0P — Vol 2 | 最新价 $0.01 | OI 18544→38774 (ΔOI +20230张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20230张（+109.1% vs前日OI），连续性待观察（方向未知）
10-09 230.0P — Vol 324 | 最新价 $0.01 | OI 1182→19988 (ΔOI +18806张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18806张（+1591.0% vs前日OI），连续性待观察（方向未知）
10-09 372.5C — Vol 8,916 | 最新价 $9.94 | OI 913→13384 (ΔOI +12471张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12471张（+1365.9% vs前日OI），连续性待观察（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 77,233 张（Put 64,762 / Call 12,471），跨 2 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-07  C +11.5k / P +14.3k ｜ Activity HIGH ｜ 2D
10-09  C +55.3k / P +85.1k ｜ Activity HIGH ｜ 4D
10-12  C +4.3k / P +2.1k ｜ Activity HIGH ｜ 7D
10-14  C +0.9k / P +0.9k ｜ Activity HIGH ｜ 9D

📆 10-07 Forward Structure
存量OI: C 25.7k / P 21.8k，今日变化ΔOI: C +11.5k / P +14.3k，平值价格ATM: C $4.95 / P $3.70 ｜ ATM IV 38.8%，净 delta 敞口 257k shares
Top ΔOI: C 382 +4,274 ｜ P 350 +1,746
仓位参考: Max Pain 365 ｜ Call Wall 382.5（+1.0%）（OI 4.5k） ｜ Put Wall 350（-7.6%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 38.8%｜历史 Rank 20%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 257,338 股

📆 10-09 Forward Structure
存量OI: C 145.8k / P 168.8k，今日变化ΔOI: C +55.3k / P +85.1k，平值价格ATM: C $7.65 / P $5.50 ｜ ATM IV 39.1%，净 delta 敞口 1.7M shares
Top ΔOI: C 372 +12,471
仓位参考: Max Pain 362 ｜ Call Wall 372.5（-1.6%，弱）（OI 13.4k）
量化解读： 存量两侧均衡｜ATM IV 39.1%｜历史 Rank 20%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,707,397 股

📆 10-12 Forward Structure
存量OI: C 10.3k / P 7.2k，今日变化ΔOI: C +4.3k / P +2.1k，平值价格ATM: C $7.94 / P $6.39 ｜ ATM IV 33.8%，净 delta 敞口 121k shares
Top ΔOI: C 380 +1,231 ｜ C 377 +653 ｜ C 375 +624
仓位参考: Max Pain 360 ｜ Call Wall 380（+0.3%，弱）（OI 1.6k） ｜ Put Wall 350（-7.6%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 33.8%｜历史 Rank 20%（近端代理）｜IV/RV 1.18×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 121,401 股

📆 10-14 Forward Structure
存量OI: C 3.8k / P 2.1k，今日变化ΔOI: C +0.9k / P +0.9k，平值价格ATM: C $9.36 / P $7.90 ｜ ATM IV 36.2%，净 delta 敞口 9k shares
Top ΔOI: C 372 +176 ｜ C 400 +157 ｜ P 370 +153
仓位参考: Max Pain 362 ｜ Call Wall 400（+5.6%，弱）（OI 0.4k） ｜ Put Wall 370（-2.3%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 36.2%｜历史 Rank 20%（近端代理）｜IV/RV 1.27×（近似）｜净 delta 敞口 正 9,325 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/TSLA_evening.json