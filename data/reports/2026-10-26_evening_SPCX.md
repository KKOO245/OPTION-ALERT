# 期权晚报 2026-10-26（快照 21:54 ET）

📊 市场环境

SPY $765.37 ｜ QQQ $712.20
VIX 18.39 ↓5.5%（5D -0.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：无更新，来源自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 待公布 ｜ 前值 0
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 147.93 → 收盘 146.90（-0.7%） ｜ 今日高 150.24 ｜ 低 144.57 ｜ 昨收 147.49 → 收盘 146.90（-0.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-29，窗口结束前不做对错判定）

Options: P/C成交量 0.58 | OI比 0.89 | ATM IV 57.9% | Skew 0.9pp | Term 0.88 | ExpMove ±3.4%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价薄（Skew 0.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.89×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-28（2D）±3.4% ｜ 10-30（4D）±4.8% ｜ 11-02（7D）±5.3% ｜ 11-04（9D）±7.1%
   ⇒ IV–VIX Spread: +39.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -33,335,141 | GEX Change vs 上次快照 -10,016,072 | Flip: Primary Flip: 150.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 766 / LOW 129 / INVALID 429
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 150.44（全链重定价，覆盖 99%）
最近结构参考: Flip 150（现价低于该位 2.4%）
量化视角： 负 Gamma（3334万，无历史分位）｜负 Gamma 加深（1002万）｜现价位于 Flip 下方 2.35%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 150（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 155.0C — Vol 21,931 | 最新价 $0.95 | OI 8864→16145 (ΔOI +7281张) | ΔOI/Volume 33.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7281张（+82.1% vs前日OI），连续性待观察（方向未知）
10-30 90.0P — Vol 6,892（Yahoo补） | 最新价 $0.02 | OI 760→7486 (ΔOI +6726张) | ΔOI/Volume 97.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6726张（+885.0% vs前日OI），连续性待观察（方向未知）
10-30 85.0P — Vol 555 | 最新价 $0.01 | OI 823→7246 (ΔOI +6423张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6423张（+780.4% vs前日OI），连续性待观察（方向未知）
11-20 90.0P — Vol 67 | 最新价 $0.12 | OI 5225→9842 (ΔOI +4617张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4617张（+88.4% vs前日OI），连续性待观察（方向未知）
10-30 95.0P — Vol 86 | 最新价 $0.02 | OI 4258→7433 (ΔOI +3175张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3175张（+74.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 28,222 张（Put 20,941 / Call 7,281），跨 2 个期限｜远端彩票/名义（4 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-28  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-02  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-04  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 10-28 Forward Structure
存量OI: C 27.3k / P 24.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.50 / P $2.56 ｜ ATM IV 57.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 150 ｜ Call Wall 155（+5.5%，弱）（OI 3.7k） ｜ Put Wall 160（+8.9%）（OI 3.5k）
量化解读： 存量两侧均衡｜ATM IV 57.9%｜历史 Rank 64%（近端代理）｜IV/RV 0.97×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-30（Activity LOW）仓位参考: Max Pain 152 ｜ Call Wall 155（+5.5%，弱）（OI 16.1k） ｜ Put Wall 150（+2.1%）（OI 15.0k）

11-02（Activity LOW）仓位参考: Max Pain 149 ｜ Call Wall 160（+8.9%，弱）（OI 1.4k） ｜ Put Wall 155（+5.5%，弱）（OI 0.5k）

11-04（Activity LOW）仓位参考: Max Pain 148 ｜ Call Wall 155（+5.5%，弱）（OI 0.8k） ｜ Put Wall 150（+2.1%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=67 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=67）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/SPCX_evening.json