# 期权晚报 2026-11-16（快照 16:40 ET）

📊 市场环境

SPY $739.95 ｜ QQQ $661.75
VIX 22.91 ↑18.7%（5D +15.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.8
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 153C ΔOI +1,728（距现价 +4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-27 146P ΔOI +1,079 占该期限总 OI 19.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 150.01 → 收盘 145.88（-2.8%） ｜ 今日高 151.31 ｜ 低 145.50 ｜ 昨收 150.55 → 收盘 145.88（-3.1%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-19，窗口结束前不做对错判定）

Options: P/C成交量 2.64 | OI比 1.85 | ATM IV 48.3% | Skew 4.8pp | Term 0.74 | ExpMove ±4.2%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价中性（Skew 4.8pp）｜当日成交偏 Put（P/C量 2.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.64×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.85×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-20（4D）±4.2% ｜ 11-27（11D）±5.5% ｜ 12-04（18D）±2.0% ｜ 12-11（25D）±2.4%
   ⇒ IV–VIX Spread: +25.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -18,206,288 | GEX Change vs 上次快照 -3,382,517 | Flip: Primary Flip: 151.09（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 394 / LOW 145 / INVALID 363
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 151.09（全链重定价，覆盖 96%）
最近结构参考: Flip 151（现价低于该位 3.4%）
量化视角： 负 Gamma（1821万，无历史分位）｜负 Gamma 加深（338万）｜现价位于 Flip 下方 3.45%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 152（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 151（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 164.0C — Vol 2 | 最新价 $1.04 | OI 537→6063 (ΔOI +5526张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5526张（+1029.0% vs前日OI），连续性待观察（方向未知）
11-20 158.0C — Vol 18 | 最新价 $0.24 | OI 448→2312 (ΔOI +1864张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1864张（+416.1% vs前日OI），连续性待观察（方向未知）
11-20 153.0C — Vol 43 | 最新价 $0.64 | OI 933→2661 (ΔOI +1728张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1728张（+185.2% vs前日OI），连续性待观察（方向未知）
11-20 145.0P — Vol 2,933 | 最新价 $2.54 | OI 6518→7731 (ΔOI +1213张) | ΔOI/Volume 41.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1213张（+18.6% vs前日OI），连续性待观察（方向未知）
11-27 146.0P — Vol 55 | 最新价 $3.88 | OI 27→1106 (ΔOI +1079张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1079张（+3996.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,410 张（Put 2,292 / Call 9,118），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +5.5k / P +1.2k ｜ Activity HIGH ｜ 4D
11-27  C +0.1k / P +1.2k ｜ Activity HIGH ｜ 11D
12-04  C -33 / P +0.2k ｜ Activity MEDIUM △ ｜ 18D
12-11  C +16 / P +34 ｜ Activity MEDIUM △ ｜ 25D

📆 11-20 Forward Structure
存量OI: C 31.6k / P 58.6k，今日变化ΔOI: C +5.5k / P +1.2k，平值价格ATM: C $2.90 / P $3.20 ｜ ATM IV 48.3%，净 delta 敞口 43k shares
Top ΔOI: C 158 +1,864 ｜ C 153 +1,728 ｜ P 145 +1,213
仓位参考: Max Pain 152 ｜ Call Wall 153（+4.9%，弱）（OI 2.7k） ｜ Put Wall 140（-4.0%，弱）（OI 9.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 48.3%｜历史 Rank 96%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 43,300 股

📆 11-27 Forward Structure
存量OI: C 1.4k / P 4.1k，今日变化ΔOI: C +0.1k / P +1.2k，平值价格ATM: C $4.10 / P $3.88 ｜ ATM IV 39.2%，净 delta 敞口 -60k shares
Top ΔOI: P 146 +1,079 ｜ P 150 +79 ｜ C 156 +41
仓位参考: Max Pain 158 ｜ Call Wall 152.5（+4.5%，弱）（OI 0.1k） ｜ Put Wall 146（+0.1%）（OI 1.1k）
量化解读： 存量 Put 重｜ATM IV 39.2%｜历史 Rank 96%（近端代理）｜IV/RV 1.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 59,843 股

12-04（MEDIUM △）Top ΔOI: 148P +59 ｜ 159P +48
12-04（MEDIUM △）仓位参考: Max Pain 161 ｜ Call Wall 152.5（+4.5%，弱）（OI 21） ｜ Put Wall 148（+1.5%，弱）（OI 0.1k）

12-11（MEDIUM △）Top ΔOI: 139P +14 ｜ 159C +11
12-11（MEDIUM △）仓位参考: Max Pain 150 ｜ Call Wall 154（+5.6%，弱）（OI 84） ｜ Put Wall 143（-2.0%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 11-20（4D）ATM IV 48.3% vs 11-27 39.2%（差 +9.2pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/XBI_evening.json