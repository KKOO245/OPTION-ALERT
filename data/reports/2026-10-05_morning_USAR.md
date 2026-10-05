# 期权晨报 2026-10-05（快照 10:20 ET）

📊 市场环境

SPY $774.71 ｜ QQQ $756.20
VIX 15.75 ↑2.9%（5D -2.0%） ｜ Vol Regime: NORMAL
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
🟡 **近现价集中开仓**: 10-09 14C ΔOI +915（距现价 +3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 13.59 → 今开 13.66（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 13.76 ｜ 低 13.28

Options: P/C成交量 0.20 | OI比 0.52 | ATM IV 55.3% | Skew -3.5pp | Term 1.26 | ExpMove ±6.4%（近端） | Rank 20%
量化视角： IV 历史低位（Rank 20%，期权偏便宜）｜期限结构正常偏陡（Term 1.26）｜Put 保护异常便宜（Skew -3.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.52）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.20×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.52×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（4D）±6.4% ｜ 10-16（11D）±9.8% ｜ 10-23（18D）±13.1% ｜ 10-30（25D）±15.0%
   ⇒ IV–VIX Spread: +39.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,442,697 | GEX Change vs 上次快照 -230,814 | Flip: Primary Flip: 14.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 197 / LOW 59 / INVALID 134
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 14.36（全链重定价，覆盖 100%）
最近结构参考: Flip 14（现价低于该位 6.0%）
量化视角： 负 Gamma（244万，无历史分位）｜负 Gamma 加深（23万）｜现价位于 Flip 下方 6.00%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 15（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 14（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 14.5C — Vol 1,788 | 最新价 $0.15 | OI 368→1602 (ΔOI +1234张) | ΔOI/Volume 69.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1234张（+335.3% vs前日OI），连续性待观察（方向未知）
10-09 14.0C — Vol 5,483 | 最新价 $0.28 | OI 177→1092 (ΔOI +915张) | ΔOI/Volume 16.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增915张（+517.0% vs前日OI），连续性待观察（方向未知）
10-09 15.0C — Vol 877 | 最新价 $0.08 | OI 1093→1675 (ΔOI +582张) | ΔOI/Volume 66.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增582张（+53.2% vs前日OI），连续性待观察（方向未知）
10-09 14.0P — Vol 672 | 最新价 $0.66 | OI 804→1345 (ΔOI +541张) | ΔOI/Volume 80.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增541张（+67.3% vs前日OI），连续性待观察（方向未知）
10-23 16.5P — Vol 331 | 最新价 $3.04 | OI 514→829 (ΔOI +315张) | ΔOI/Volume 95.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增315张（+61.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,587 张（Put 856 / Call 2,731），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +3.3k / P +0.7k ｜ Activity HIGH ｜ 4D
10-16  C +0.6k / P -40 ｜ Activity HIGH ｜ 11D
10-23  C +76 / P +0.6k ｜ Activity HIGH ｜ 18D
10-30  C +0.6k / P +0.5k ｜ Activity HIGH ｜ 25D

📆 10-09 Forward Structure
存量OI: C 14.1k / P 7.3k，今日变化ΔOI: C +3.3k / P +0.7k，平值价格ATM: C $0.49 / P $0.37 ｜ ATM IV 55.3%，净 delta 敞口 75k shares
Top ΔOI: C 14 +1,234 ｜ C 14 +915
仓位参考: Max Pain 15 ｜ Call Wall 14.5（+7.4%，弱）（OI 1.6k） ｜ Put Wall 14（+3.7%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 55.3%｜历史 Rank 20%（近端代理）｜IV/RV 1.08×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 75,320 股

📆 10-16 Forward Structure
存量OI: C 47.6k / P 16.8k，今日变化ΔOI: C +0.6k / P -40，平值价格ATM: C $0.72 / P $0.60 ｜ ATM IV 64.6%，净 delta 敞口 41k shares
Top ΔOI: P 16 -292
仓位参考: Max Pain 16 ｜ Put Wall 14（+3.7%，弱）（OI 2.0k）
量化解读： 存量 Call 重｜ATM IV 64.6%｜历史 Rank 20%（近端代理）｜IV/RV 1.26×（近似）｜净 delta 敞口 正 41,463 股

📆 10-23 Forward Structure
存量OI: C 9.9k / P 5.0k，今日变化ΔOI: C +76 / P +0.6k，平值价格ATM: C $1.02 / P $0.75 ｜ ATM IV 66.5%，净 delta 敞口 -37k shares
Top ΔOI: P 16 +315
仓位参考: Max Pain 17 ｜ Put Wall 14（+3.7%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 66.5%｜历史 Rank 20%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 37,494 股

📆 10-30 Forward Structure
存量OI: C 4.5k / P 6.4k，今日变化ΔOI: C +0.6k / P +0.5k，平值价格ATM: C $1.10 / P $0.93 ｜ ATM IV 65.4%，净 delta 敞口 -11k shares
Top ΔOI: P 17 +237 ｜ C 14 +159
仓位参考: Max Pain 16 ｜ Call Wall 14（+3.7%，弱）（OI 0.3k） ｜ Put Wall 14（+3.7%）（OI 2.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 65.4%｜历史 Rank 20%（近端代理）｜IV/RV 1.28×（近似）｜净 delta 敞口 负 11,140 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=40 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=40）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/USAR_morning.json