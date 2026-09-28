# 期权晚报 2026-09-28（快照 16:40 ET）

📊 市场环境

SPY $765.61 ｜ QQQ $736.53
VIX 16.07 ↑8.1%（5D +8.1%） ｜ Vol Regime: NORMAL
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
🟡 **近现价集中开仓**: 10-16 85P ΔOI +675（距现价 -3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-02 94C ΔOI +34,895 占该期限总 OI 20.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 88.16 → 收盘 87.89（-0.3%） ｜ 今日高 89.43 ｜ 低 87.36 ｜ 昨收 92.87 → 收盘 87.89（-5.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-01，窗口结束前不做对错判定）

Options: P/C成交量 0.84 | OI比 0.46 | ATM IV 45.8% | Skew 0.8pp | Term 0.92 | ExpMove ±3.7%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构正常（Term 0.92）｜保护溢价薄（Skew 0.8pp）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（4D）±3.7% ｜ 10-09（11D）±5.7% ｜ 10-16（18D）±7.4% ｜ 10-23（25D）±8.9%
   ⇒ IV–VIX Spread: +29.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -12,303,253 | GEX Change vs 上次快照 -15,032,445 | Flip: Primary Flip: 89.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 453 / LOW 86 / INVALID 265
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 89.15（全链重定价，覆盖 96%）
Put Wall 90（弱结构｜现价低于该位 2.3%）
最近结构参考: Flip 89（现价低于该位 1.4%）
量化视角： 负 Gamma（1230万，无历史分位）｜由正转负（1503万）｜现价位于 Flip 下方 1.41%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 90（Put Wall，弱结构） / 94（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 89（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 94.0C — Vol 1,030 | 最新价 $0.21 | OI 693→35588 (ΔOI +34895张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增34895张（+5035.4% vs前日OI），连续性待观察（方向未知）
10-02 97.0C — Vol 490 | 最新价 $0.18 | OI 2066→28128 (ΔOI +26062张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26062张（+1261.5% vs前日OI），连续性待观察（方向未知）
10-02 98.0C — Vol 282 | 最新价 $0.15 | OI 2615→15300 (ΔOI +12685张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12685张（+485.1% vs前日OI），连续性待观察（方向未知）
10-02 90.0P — Vol 1,328 | 最新价 $2.92 | OI 5598→9104 (ΔOI +3506张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3506张（+62.6% vs前日OI），连续性待观察（方向未知）
10-02 86.0P — Vol 2,325 | 最新价 $0.83 | OI 3243→6439 (ΔOI +3196张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3196张（+98.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 80,344 张（Put 6,702 / Call 73,642），跨 1 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +77.7k / P +10.4k ｜ Activity HIGH ｜ 4D
10-09  C +1.0k / P +2.6k ｜ Activity HIGH ｜ 11D
10-16  C +0.6k / P -2 ｜ Activity MEDIUM △ ｜ 18D
10-23  C -61 / P +73 ｜ Activity MEDIUM △ ｜ 25D

📆 10-02 Forward Structure
存量OI: C 116.8k / P 53.6k，今日变化ΔOI: C +77.7k / P +10.4k，平值价格ATM: C $1.68 / P $1.61 ｜ ATM IV 45.8%，净 delta 敞口 -92k shares
Top ΔOI: C 94 +34,895 ｜ C 97 +26,062 ｜ C 98 +12,685
仓位参考: Max Pain 94 ｜ Put Wall 90（+2.4%，弱）（OI 9.1k）
量化解读： 存量 Call 重｜ATM IV 45.8%｜历史 Rank 74%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 92,087 股

📆 10-09 Forward Structure
存量OI: C 6.8k / P 12.2k，今日变化ΔOI: C +1.0k / P +2.6k，平值价格ATM: C $2.64 / P $2.40 ｜ ATM IV 44.1%，净 delta 敞口 955 shares
Top ΔOI: P 87 +410
仓位参考: Max Pain 94 ｜ Call Wall 85（-3.3%，弱）（OI 0.2k） ｜ Put Wall 90（+2.4%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 44.1%｜历史 Rank 74%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 955 股

10-16（MEDIUM △）Top ΔOI: 85P +675 ｜ 90P -508
10-16（MEDIUM △）仓位参考: Max Pain 93 ｜ Call Wall 90（+2.4%，弱）（OI 5.2k） ｜ Put Wall 90（+2.4%，弱）（OI 9.5k）

10-23（MEDIUM △）Top ΔOI: 96C -67 ｜ 93P +34
10-23（MEDIUM △）仓位参考: Max Pain 95 ｜ Put Wall 93（+5.8%，弱）（OI 1.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=29 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=29）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/GDX_evening.json