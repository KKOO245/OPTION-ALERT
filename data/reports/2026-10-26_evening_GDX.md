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


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 81.16 → 收盘 81.02（-0.2%） ｜ 今日高 81.39 ｜ 低 79.08 ｜ 昨收 80.20 → 收盘 81.02（+1.0%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-02，窗口结束前不做对错判定）

Options: P/C成交量 0.84 | OI比 2.80 | ATM IV 46.8% | Skew 0.7pp | Term 0.86 | ExpMove ±2.8%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价薄（Skew 0.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.80×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-28（2D）±2.8% ｜ 10-30（4D）±4.0% ｜ 11-02（7D）±4.7% ｜ 11-04（9D）±5.2%
   ⇒ IV–VIX Spread: +28.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 26,974,345 | GEX Change vs 上次快照 -895,410 | Flip: Primary Flip: 79.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 503 / LOW 134 / INVALID 471
结构观察区: Primary Flip 79.33（全链重定价，覆盖 97%）
Put Wall 80（弱结构｜现价高于该位 1.3%） | Call Wall 85（弱结构｜现价低于该位 4.7%）
最近结构参考: Put Wall 80（现价高于该位 1.3%）
量化视角： 正 Gamma（2697万，无历史分位）｜正 Gamma 减弱（90万）｜现价位于 Flip 上方 2.12%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（Put Wall，弱结构）；上方 85（MaxPain，仅结算参考） / 85（Call Wall，弱结构）。
• Gamma 区域：切换参考 79（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 82.0C — Vol 606 | 最新价 $1.14 | OI 502→19113 (ΔOI +18611张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18611张（+3707.4% vs前日OI），连续性待观察（方向未知）
10-30 85.0C — Vol 1,299 | 最新价 $0.35 | OI 11174→27547 (ΔOI +16373张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16373张（+146.5% vs前日OI），连续性待观察（方向未知）
10-30 83.0C — Vol 1,134 | 最新价 $0.83 | OI 58→9138 (ΔOI +9080张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9080张（+15655.2% vs前日OI），连续性待观察（方向未知）
10-30 81.0C — Vol 386 | 最新价 $1.62 | OI 73→9151 (ΔOI +9078张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9078张（+12435.6% vs前日OI），连续性待观察（方向未知）
10-30 76.0P — Vol 264 | 最新价 $0.22 | OI 35→4059 (ΔOI +4024张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4024张（+11497.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 57,166 张（Put 4,024 / Call 53,142），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-28  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-02  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-04  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 10-28 Forward Structure
存量OI: C 1.9k / P 5.4k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.11 / P $1.13 ｜ ATM IV 46.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 85 ｜ Call Wall 86（+6.1%，弱）（OI 0.2k） ｜ Put Wall 84（+3.7%，弱）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 46.8%｜历史 Rank 76%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-30（Activity LOW）仓位参考: Max Pain 81 ｜ Call Wall 85（+4.9%，弱）（OI 27.5k） ｜ Put Wall 76（-6.2%，弱）（OI 4.1k）

11-02（Activity LOW）仓位参考: Max Pain 86 ｜ Call Wall 86（+6.1%）（OI 0.5k） ｜ Put Wall 81（-0.0%）（OI 0.3k）

11-04（Activity LOW）仓位参考: Max Pain 81 ｜ Call Wall 83（+2.4%，弱）（OI 0.2k） ｜ Put Wall 80（-1.3%，弱）（OI 17）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/GDX_evening.json