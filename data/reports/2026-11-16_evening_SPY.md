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
🟡 **近现价集中开仓**: 11-17 760C ΔOI +3,749（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-19 650P ΔOI +11,458 占该期限总 OI 10.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 749.66 → 收盘 739.95（-1.3%） ｜ 今日高 749.82 ｜ 低 738.07 ｜ 昨收 754.37 → 收盘 739.95（-1.9%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-19，窗口结束前不做对错判定）

Options: P/C成交量 1.46 | OI比 1.00 | ATM IV 20.7% | Skew -0.7pp | Term 0.88 | ExpMove ±1.0%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.7pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.46×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.00×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 23% ｜ P/C OI(近端) 2%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 23%）｜近端持仓极端 Call 重（P/C OI 分位 2%，历史极低区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-17（1D）±1.0% ｜ 11-18（2D）±1.5% ｜ 11-19（3D）±1.8% ｜ 11-20（4D）±0.0%
   ⇒ IV–VIX Spread: -2.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,536,113,233 | GEX Change vs 上次快照 -409,944,530 | Flip: Primary Flip: 756.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 3051 / LOW 428 / INVALID 1543
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 756.90（全链重定价，覆盖 92%）
最近结构参考: Flip 757（现价低于该位 2.2%）
量化视角： 负 Gamma（15.36亿，历史分位偏负区，比 77% 的交易日更负）｜负 Gamma 加深（4.10亿）｜现价位于 Flip 下方 2.24%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 753（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 757（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-19 650.0P — Vol 1,368 | 最新价 $0.12 | OI 32→11490 (ΔOI +11458张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11458张（+35806.2% vs前日OI），连续性待观察（方向未知）
11-20 635.0P — Vol 1,314 | 最新价 $0.13 | OI 9116→20526 (ΔOI +11410张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11410张（+125.2% vs前日OI），连续性待观察（方向未知）
12-04 675.0P — Vol 176 | 最新价 $1.93 | OI 1255→11776 (ΔOI +10521张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10521张（+838.3% vs前日OI），连续性待观察（方向未知）
11-18 731.0P — Vol 12,352 | 最新价 $2.23 | OI 570→10369 (ΔOI +9799张) | ΔOI/Volume 79.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9799张（+1719.1% vs前日OI），连续性待观察（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 43,188 张（Put 43,188 / Call 0），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-17  C +27.8k / P +21.1k ｜ Activity HIGH ｜ 1D
11-18  C +22.8k / P +17.2k ｜ Activity HIGH ｜ 2D
11-19  C +8.8k / P +25.3k ｜ Activity HIGH ｜ 3D
11-20  C +30.5k / P +44.1k ｜ Activity MEDIUM △ ｜ 4D

📆 11-17 Forward Structure
存量OI: C 73.8k / P 73.3k，今日变化ΔOI: C +27.8k / P +21.1k，平值价格ATM: C $3.87 / P $3.71 ｜ ATM IV 24.4%，净 delta 敞口 -757k shares
Top ΔOI: C 760 +3,749 ｜ C 765 +3,225 ｜ C 758 +2,674
仓位参考: Max Pain 753 ｜ Call Wall 760（+2.7%，弱）（OI 5.3k） ｜ Put Wall 750（+1.4%）（OI 4.3k）
量化解读： 存量两侧均衡｜ATM IV 24.4%｜历史 Rank 85%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 757,446 股

📆 11-18 Forward Structure
存量OI: C 78.7k / P 95.4k，今日变化ΔOI: C +22.8k / P +17.2k，平值价格ATM: C $5.53 / P $5.26 ｜ ATM IV 24.6%，净 delta 敞口 -347k shares
Top ΔOI: P 731 +9,799 ｜ C 762 +3,297 ｜ C 767 +3,088
仓位参考: Max Pain 755 ｜ Call Wall 762（+3.0%，弱）（OI 3.7k） ｜ Put Wall 731（-1.2%，弱）（OI 10.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 24.6%｜历史 Rank 85%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 346,758 股

📆 11-19 Forward Structure
存量OI: C 38.8k / P 68.1k，今日变化ΔOI: C +8.8k / P +25.3k，平值价格ATM: C $6.67 / P $6.37 ｜ ATM IV 24.1%，净 delta 敞口 -361k shares
Top ΔOI: P 650 +11,458 ｜ P 750 +1,712
仓位参考: Max Pain 754 ｜ Call Wall 761（+2.8%，弱）（OI 1.8k） ｜ Put Wall 750（+1.4%，弱）（OI 2.4k）
量化解读： 存量 Put 重｜ATM IV 24.1%｜历史 Rank 85%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 负 361,111 股

11-20（MEDIUM △）Top ΔOI: 635P +11,410 ｜ 737P -8,775
11-20（MEDIUM △）仓位参考: Max Pain 757 ｜ Put Wall 725（-2.0%，弱）（OI 66.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/SPY_evening.json