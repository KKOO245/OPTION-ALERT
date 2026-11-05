# 期权晨报 2026-11-05（快照 10:20 ET）

📊 市场环境

SPY $732.06 ｜ QQQ $647.05
VIX 21.04 ↑26.7%（5D +22.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **事件差分**: 11-06（1D）ATM IV 88.3% vs 11-09 59.8%（差 +28.5pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 385.19 → 今开 374.02（-2.9%） | 较昨收变动（含盘初走势） ｜ 今日高 374.23 ｜ 低 345.61

Options: P/C成交量 1.32 | OI比 1.48 | ATM IV 88.3% | Skew 12.3pp | Term 0.58 | ExpMove ±4.1%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.58，近月 IV 高于远月）｜保护溢价显著（Skew 12.3pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.32）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.32×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.48×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±4.1% ｜ 11-09（4D）±5.2% ｜ 11-11（6D）±6.5% ｜ 11-13（8D）±7.4%
   ⇒ IV–VIX Spread: +67.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -48,763,756 | GEX Change vs 上次快照 -43,903,716 | Flip: Primary Flip: 369.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 1302 / LOW 106 / INVALID 838
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 369.61（全链重定价，覆盖 92%）
最近结构参考: Flip 370（现价低于该位 5.2%）
量化视角： 负 Gamma（4876万，无历史分位）｜负 Gamma 加深（4390万）｜现价位于 Flip 下方 5.24%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 392（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 370（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 360.0P — Vol 18,380 | 最新价 $0.66 | OI 5060→9936 (ΔOI +4876张) | ΔOI/Volume 26.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4876张（+96.4% vs前日OI），连续性待观察（方向未知）
11-06 400.0C — Vol 31,230 | 最新价 $1.55 | OI 8227→11889 (ΔOI +3662张) | ΔOI/Volume 11.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3662张（+44.5% vs前日OI），连续性待观察（方向未知）
11-09 315.0P — Vol 3,016 | 最新价 $0.12 | OI 11→3015 (ΔOI +3004张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3004张（+27309.1% vs前日OI），连续性待观察（方向未知）
11-06 495.0C — Vol 3,045 | 最新价 $0.01 | OI 340→3303 (ΔOI +2963张) | ΔOI/Volume 97.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2963张（+871.5% vs前日OI），连续性待观察（方向未知）
11-06 330.0P — Vol 6,517 | 最新价 $0.09 | OI 6768→9201 (ΔOI +2433张) | ΔOI/Volume 37.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2433张（+36.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 16,938 张（Put 10,313 / Call 6,625），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +18.0k / P +20.2k ｜ Activity HIGH ｜ 1D
11-09  C +8.2k / P +8.2k ｜ Activity HIGH ｜ 4D
11-11  C +4.6k / P +5.3k ｜ Activity HIGH ｜ 6D
11-13  C +5.4k / P +6.2k ｜ Activity HIGH ｜ 8D

📆 11-06 Forward Structure
存量OI: C 188.3k / P 279.0k，今日变化ΔOI: C +18.0k / P +20.2k，平值价格ATM: C $6.65 / P $7.86 ｜ ATM IV 88.3%，净 delta 敞口 -999k shares
Top ΔOI: P 360 +4,876
仓位参考: Max Pain 392 ｜ Call Wall 380（+8.5%，弱）（OI 3.0k） ｜ Put Wall 360（+2.8%，弱）（OI 9.9k）
量化解读： 存量 Put 重｜ATM IV 88.3%｜历史 Rank 93%（近端代理）｜IV/RV 2.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 998,984 股

📆 11-09 Forward Structure
存量OI: C 28.3k / P 23.5k，今日变化ΔOI: C +8.2k / P +8.2k，平值价格ATM: C $8.40 / P $9.80 ｜ ATM IV 59.8%，净 delta 敞口 -347k shares
Top ΔOI: P 315 +3,004 ｜ C 400 +1,479 ｜ P 380 +942
仓位参考: Max Pain 392 ｜ Put Wall 380（+8.5%，弱）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 59.8%｜历史 Rank 93%（近端代理）｜IV/RV 1.70×（近似）｜净 delta 敞口 负 347,471 股

📆 11-11 Forward Structure
存量OI: C 14.6k / P 10.8k，今日变化ΔOI: C +4.6k / P +5.3k，平值价格ATM: C $10.65 / P $12.10 ｜ ATM IV 61.3%，净 delta 敞口 -215k shares
Top ΔOI: P 260 +1,751 ｜ C 390 +1,249 ｜ P 377 +553
仓位参考: Max Pain 390 ｜ Put Wall 350（-0.1%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 61.3%｜历史 Rank 93%（近端代理）｜IV/RV 1.74×（近似）｜净 delta 敞口 负 215,114 股

📆 11-13 Forward Structure
存量OI: C 56.5k / P 43.3k，今日变化ΔOI: C +5.4k / P +6.2k，平值价格ATM: C $12.50 / P $13.40 ｜ ATM IV 61.4%，净 delta 敞口 -269k shares
Top ΔOI: P 380 +587 ｜ P 382 +471
仓位参考: Max Pain 380 ｜ Call Wall 385（+9.9%，弱）（OI 1.9k） ｜ Put Wall 350（-0.1%，弱）（OI 2.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 61.4%｜历史 Rank 93%（近端代理）｜IV/RV 1.75×（近似）｜净 delta 敞口 负 268,844 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 88.3% vs 11-09 59.8%（差 +28.5pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/TSLA_morning.json