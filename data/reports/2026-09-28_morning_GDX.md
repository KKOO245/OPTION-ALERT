# 期权晨报 2026-09-28（快照 10:20 ET）

📊 市场环境

SPY $765.39 ｜ QQQ $736.53
VIX 15.89 ↑6.9%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.24 ｜ 实际 待公布 ｜ 前值 7.271
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 54.9 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 84 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🔵 **期限 OI 集中**: 10-02 94C ΔOI +34,895 占该期限总 OI 20.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 92.87 → 今开 88.16（-5.1%） | 较昨收变动（含盘初走势） ｜ 今日高 89.43 ｜ 低 87.36

Options: P/C成交量 0.84 | OI比 0.46 | ATM IV 49.6% | Skew 1.2pp | Term 0.88 | ExpMove ±4.7%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价薄（Skew 1.2pp）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（4D）±4.7% ｜ 10-09（11D）±3.5% ｜ 10-16（18D）±6.5% ｜ 10-23（25D）±11.8%
   ⇒ IV–VIX Spread: +33.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 2,729,191 | GEX Change vs 上次快照 9,907,667 | Flip: Primary Flip: 89.09（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 455 / LOW 79 / INVALID 270
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 89.09（全链重定价，覆盖 96%）
Put Wall 90（弱结构｜现价低于该位 0.7%） | Call Wall 94（弱结构｜现价低于该位 4.9%）
最近结构参考: Flip 89（现价高于该位 0.3%）
量化视角： 正 Gamma（273万，无历史分位）｜由负转正（+991万）｜现价位于 Flip 上方 0.30%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 90（Put Wall，弱结构） / 94（MaxPain，仅结算参考） / 94（Call Wall，弱结构）。
• Gamma 区域：切换参考 89（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 94.0C — Vol 35,937 | 最新价 $1.55 | OI 693→35588 (ΔOI +34895张) | ΔOI/Volume 97.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增34895张（+5035.4% vs前日OI），连续性待观察（方向未知）
10-02 97.0C — Vol 26,636 | 最新价 $0.67 | OI 2066→28128 (ΔOI +26062张) | ΔOI/Volume 97.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26062张（+1261.5% vs前日OI），连续性待观察（方向未知）
10-02 98.0C — Vol 13,120 | 最新价 $0.48 | OI 2615→15300 (ΔOI +12685张) | ΔOI/Volume 96.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12685张（+485.1% vs前日OI），连续性待观察（方向未知）
10-02 90.0P — Vol 4,130 | 最新价 $0.85 | OI 5598→9104 (ΔOI +3506张) | ΔOI/Volume 84.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3506张（+62.6% vs前日OI），连续性待观察（方向未知）
10-02 86.0P — Vol 3,227 | 最新价 $0.22 | OI 3243→6439 (ΔOI +3196张) | ΔOI/Volume 99.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3196张（+98.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 80,344 张（Put 6,702 / Call 73,642），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +77.7k / P +10.4k ｜ Activity HIGH ｜ 4D
10-09  C +1.0k / P +2.6k ｜ Activity HIGH ｜ 11D
10-16  C +0.6k / P -2 ｜ Activity MEDIUM △ ｜ 18D
10-23  C -61 / P +73 ｜ Activity MEDIUM △ ｜ 25D

📆 10-02 Forward Structure
存量OI: C 116.8k / P 53.6k，今日变化ΔOI: C +77.7k / P +10.4k，平值价格ATM: C $1.58 / P $2.60 ｜ ATM IV 49.6%，净 delta 敞口 391k shares
Top ΔOI: C 94 +34,895 ｜ C 97 +26,062 ｜ C 98 +12,685
仓位参考: Max Pain 94 ｜ Call Wall 94（+5.2%，弱）（OI 35.6k） ｜ Put Wall 90（+0.7%，弱）（OI 9.1k）
量化解读： 存量 Call 重｜ATM IV 49.6%｜历史 Rank 81%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 391,364 股

📆 10-09 Forward Structure
存量OI: C 6.8k / P 12.2k，今日变化ΔOI: C +1.0k / P +2.6k，平值价格ATM: C $0.00 / P $3.09 ｜ ATM IV 42.5%，净 delta 敞口 6k shares
Top ΔOI: P 87 +410
仓位参考: Max Pain 94 ｜ Call Wall 94（+5.2%，弱）（OI 0.7k） ｜ Put Wall 90（+0.7%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 42.5%｜历史 Rank 81%（近端代理）｜IV/RV 1.10×（近似）｜净 delta 敞口 正 6,198 股

10-16（MEDIUM △）Top ΔOI: 85P +675 ｜ 90P -508
10-16（MEDIUM △）仓位参考: Max Pain 93 ｜ Call Wall 95（+6.3%，弱）（OI 6.2k） ｜ Put Wall 90（+0.7%，弱）（OI 9.5k）

10-23（MEDIUM △）Top ΔOI: 96C -67 ｜ 93P +34
10-23（MEDIUM △）仓位参考: Max Pain 95 ｜ Call Wall 95（+6.3%，弱）（OI 0.3k） ｜ Put Wall 93（+4.1%，弱）（OI 1.3k）

📅 事件差分（观察，非因果）: 10-02（4D）ATM IV 49.6% vs 10-09 42.5%（差 +7.1pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=29 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=29）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/GDX_morning.json