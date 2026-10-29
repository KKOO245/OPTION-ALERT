# 期权晨报 2026-10-28（快照 10:20 ET）

📊 市场环境

SPY $772.31 ｜ QQQ $725.61
VIX 17.36 ↓0.9%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 4　✅ 今日已公布
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 200P ΔOI +3,003（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 198.73 → 今开 197.01（-0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 198.72 ｜ 低 193.35

Options: P/C成交量 0.55 | OI比 0.99 | ATM IV 57.0% | Skew 3.6pp | Term 1.11 | ExpMove ±3.6%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构正常（Term 1.11）｜保护溢价中性（Skew 3.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.99×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（2D）±3.6% ｜ 11-06（9D）±11.8% ｜ 11-13（16D）±13.1% ｜ 11-20（23D）±13.8%
   ⇒ IV–VIX Spread: +39.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 31,779,307 | GEX Change vs 上次快照 -22,915,545 | Flip: Primary Flip: 190.16（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 697 / LOW 62 / INVALID 179
结构观察区: Primary Flip 190.16（全链重定价，覆盖 100%）
Put Wall 180（弱结构｜现价高于该位 8.7%） | Call Wall 210（弱结构｜现价低于该位 6.8%）
最近结构参考: Flip 190（现价高于该位 2.9%）
量化视角： 正 Gamma（3178万，无历史分位）｜正 Gamma 减弱（2292万）｜现价位于 Flip 上方 2.93%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（Put Wall，弱结构） / 195（MaxPain，仅结算参考）；上方 210（Call Wall，弱结构）。
• Gamma 区域：切换参考 190（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 200.0P — Vol 8,454 | 最新价 $4.35 | OI 2836→5839 (ΔOI +3003张) | ΔOI/Volume 35.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3003张（+105.9% vs前日OI），连续性待观察（方向未知）
11-06 240.0C — Vol 3,304 | 最新价 $1.36 | OI 1389→4139 (ΔOI +2750张) | ΔOI/Volume 83.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2750张（+198.0% vs前日OI），连续性待观察（方向未知）
11-06 420.0C — Vol 1,770 | 最新价 $0.01 | OI 212→1982 (ΔOI +1770张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1770张（+834.9% vs前日OI），连续性待观察（方向未知）
10-30 210.0C — Vol 9,939 | 最新价 $0.56 | OI 15584→17136 (ΔOI +1552张) | ΔOI/Volume 15.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1552张（+10.0% vs前日OI），连续性待观察（方向未知）
11-06 200.0P — Vol 1,494 | 最新价 $12.11 | OI 1324→2394 (ΔOI +1070张) | ΔOI/Volume 71.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1070张（+80.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 10,145 张（Put 4,073 / Call 6,072），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +2.0k / P +4.6k ｜ Activity HIGH ｜ 2D
11-06  C +9.1k / P +4.7k ｜ Activity HIGH ｜ 9D
11-13  C +2.0k / P +0.3k ｜ Activity MEDIUM △ ｜ 16D
11-20  C +1.3k / P -0.4k ｜ Activity MEDIUM △ ｜ 23D

📆 10-30 Forward Structure
存量OI: C 129.9k / P 129.2k，今日变化ΔOI: C +2.0k / P +4.6k，平值价格ATM: C $3.50 / P $3.55 ｜ ATM IV 57.0%，净 delta 敞口 -341k shares
Top ΔOI: P 200 +3,003 ｜ C 210 +1,552 ｜ P 197 +1,045
仓位参考: Max Pain 195 ｜ Call Wall 210（+7.3%，弱）（OI 17.1k） ｜ Put Wall 180（-8.0%，弱）（OI 9.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 57.0%｜历史 Rank 86%（近端代理）｜IV/RV 1.27×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 341,199 股

📆 11-06 Forward Structure
存量OI: C 48.7k / P 52.9k，今日变化ΔOI: C +9.1k / P +4.7k，平值价格ATM: C $11.60 / P $11.45 ｜ ATM IV 92.6%，净 delta 敞口 -31k shares
Top ΔOI: C 240 +2,750 ｜ P 200 +1,070
仓位参考: Max Pain 195 ｜ Call Wall 215（+9.9%，弱）（OI 3.3k） ｜ Put Wall 190（-2.9%，弱）（OI 3.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 92.6%｜历史 Rank 86%（近端代理）｜IV/RV 2.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 30,506 股

11-13（MEDIUM △）Top ΔOI: 207C +283 ｜ 195C +159
11-13（MEDIUM △）仓位参考: Max Pain 195 ｜ Call Wall 210（+7.3%，弱）（OI 1.4k） ｜ Put Wall 180（-8.0%，弱）（OI 1.4k）

11-20（MEDIUM △）Top ΔOI: 185P -773 ｜ 180P -562
11-20（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 200（+2.2%，弱）（OI 12.8k） ｜ Put Wall 185（-5.5%，弱）（OI 10.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/PLTR_morning.json