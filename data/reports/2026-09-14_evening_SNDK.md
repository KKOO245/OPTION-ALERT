# 期权晚报 2026-09-14（快照 16:48 ET）

📊 市场环境

SPY $760.88 ｜ QQQ $709.18
VIX 17.10 ↑8.0%（5D +11.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.9 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **单日价格波动**: -4.9%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,521.53 → 收盘 1,551.99（+2.0%） ｜ 今日高 1581.84 ｜ 低 1505.00 ｜ 昨收 1,633.35 → 收盘 1,551.99（-5.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-17，窗口结束前不做对错判定）

Options: P/C成交量 0.81 | OI比 1.18 | ATM IV 70.8% | Skew -2.2pp | Term 0.97 | ExpMove ±5.9%（近端） | Rank 25%
量化视角： IV 历史低位（Rank 25%，期权偏便宜）｜期限结构正常（Term 0.97）｜Put 保护异常便宜（Skew -2.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.81×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.18×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（4D）±5.9% ｜ 09-25（11D）±9.5% ｜ 10-02（18D）±12.4% ｜ 10-09（25D）±13.8%
   ⇒ IV–VIX Spread: +53.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,186,863 | GEX Change vs 上次快照 724,430 | Flip: Primary Flip: 1624.17（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1960 / LOW 438 / INVALID 978
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1624.17（全链重定价，覆盖 100%）
Put Wall 1,500（弱结构｜现价高于该位 3.5%）
最近结构参考: Put Wall 1500（现价高于该位 3.5%）
量化视角： 负 Gamma（519万，无历史分位）｜负 Gamma 缓解（+72万）｜现价位于 Flip 下方 4.44%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,500（Put Wall，弱结构） / 1,500（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1624（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 1800.0C — Vol 4,670 | 最新价 $2.65 | OI 2086→3050 (ΔOI +964张) | ΔOI/Volume 20.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增964张（+46.2% vs前日OI），连续性待观察（方向未知）
09-18 1750.0C — Vol 6,312 | 最新价 $4.60 | OI 905→1729 (ΔOI +824张) | ΔOI/Volume 13.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增824张（+91.0% vs前日OI），连续性待观察（方向未知）
09-18 1450.0P — Vol 2,151 | 最新价 $11.60 | OI 2915→3614 (ΔOI +699张) | ΔOI/Volume 32.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增699张（+24.0% vs前日OI），连续性待观察（方向未知）
09-18 1000.0P — Vol 339 | 最新价 $0.09 | OI 2801→3438 (ΔOI +637张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增637张（+22.7% vs前日OI），连续性待观察（方向未知）
09-25 1800.0C — Vol 806 | 最新价 $12.90 | OI 362→953 (ΔOI +591张) | ΔOI/Volume 73.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增591张（+163.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,715 张（Put 1,336 / Call 2,379），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 11D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 09-18 Forward Structure
存量OI: C 76.4k / P 90.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $47.70 / P $44.20 ｜ ATM IV 70.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 1,500 ｜ Call Wall 1430（-7.9%，弱）（OI 2.2k） ｜ Put Wall 1450（-6.6%，弱）（OI 3.6k）
量化解读： 存量两侧均衡｜ATM IV 70.8%｜历史 Rank 25%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 1,605 ｜ Call Wall 1700（+9.5%，弱）（OI 0.4k） ｜ Put Wall 1500（-3.3%，弱）（OI 1.8k）

10-02（Activity LOW）仓位参考: Max Pain 1,600 ｜ Call Wall 1600（+3.1%，弱）（OI 0.3k） ｜ Put Wall 1500（-3.3%，弱）（OI 0.4k）

10-09（Activity LOW）仓位参考: Max Pain 1,640 ｜ Call Wall 1700（+9.5%，弱）（OI 0.1k） ｜ Put Wall 1500（-3.3%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=16 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=16）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/SNDK_evening.json