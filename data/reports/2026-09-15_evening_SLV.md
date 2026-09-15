# 期权晚报 2026-09-15（快照 16:40 ET）

📊 市场环境

SPY $757.39 ｜ QQQ $704.54
VIX 17.20 ↑0.6%（5D +9.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **近现价集中开仓**: 09-16 57C ΔOI +4,109（距现价 -0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-21 57C ΔOI +3,140 占该期限总 OI 36.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 57.48 → 收盘 57.53（+0.1%） ｜ 今日高 57.75 ｜ 低 56.95 ｜ 昨收 56.84 → 收盘 57.53（+1.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-22，窗口结束前不做对错判定）

Options: P/C成交量 0.55 | OI比 0.94 | ATM IV 53.6% | Skew -1.6pp | Term 0.78 | ExpMove ±2.2%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.94×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-16（1D）±2.2% ｜ 09-18（3D）±3.4% ｜ 09-21（6D）±4.2% ｜ 09-23（8D）±4.8%
   ⇒ IV–VIX Spread: +36.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 38,221,727 | GEX Change vs 上次快照 17,563,443 | Flip: Primary Flip: 56.48（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1043 / LOW 204 / INVALID 371
结构观察区: Primary Flip 56.48（全链重定价，覆盖 100%）
最近结构参考: Flip 56（现价高于该位 1.9%）
量化视角： 正 Gamma（3822万，无历史分位）｜正 Gamma 增强（+1756万）｜现价位于 Flip 上方 1.85%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 58（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 56（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 64.0C — Vol 570 | 最新价 $0.99 | OI 56350→68511 (ΔOI +12161张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12161张（+21.6% vs前日OI），连续性待观察（方向未知）
10-09 100.0C — Vol 23 | 最新价 $0.05 | OI 209→8652 (ΔOI +8443张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8443张（+4039.7% vs前日OI），连续性待观察（方向未知）
09-16 57.5C — Vol 6,150 | 最新价 $0.63 | OI 0→4109 (ΔOI +4109张) | ΔOI/Volume 66.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4109张（前日OI缺失），连续性待观察（方向未知）
09-25 63.5C — Vol 76 | 最新价 $0.28 | OI 1684→5708 (ΔOI +4024张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4024张（+238.9% vs前日OI），连续性待观察（方向未知）
09-18 74.5C — Vol 4,267（Yahoo补） | 最新价 $0.02 | OI 1230→5037 (ΔOI +3807张) | ΔOI/Volume 89.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3807张（+309.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 32,544 张（Put 0 / Call 32,544），跨 5 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-16  C +12.4k / P +7.6k ｜ Activity HIGH ｜ 1D
09-18  C +2.4k / P +3.2k ｜ Activity MEDIUM △ ｜ 3D
09-21  C +4.0k / P +1.1k ｜ Activity HIGH ｜ 6D
09-23  C +0.5k / P +2.4k ｜ Activity HIGH ｜ 8D

📆 09-16 Forward Structure
存量OI: C 26.9k / P 25.2k，今日变化ΔOI: C +12.4k / P +7.6k，平值价格ATM: C $0.63 / P $0.62 ｜ ATM IV 53.6%，净 delta 敞口 224k shares
Top ΔOI: C 57 +4,109 ｜ P 57 +3,420 ｜ C 58 +1,186
仓位参考: Max Pain 58 ｜ Call Wall 57.5（-0.1%，弱）（OI 4.1k） ｜ Put Wall 58（+0.8%，弱）（OI 4.9k）
量化解读： 存量两侧均衡｜ATM IV 53.6%｜历史 Rank 86%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 224,248 股

09-18（MEDIUM △）Top ΔOI: 63C -5,389 ｜ 56P +3,176
09-18（MEDIUM △）仓位参考: Max Pain 60 ｜ Call Wall 60（+4.3%，弱）（OI 42.3k） ｜ Put Wall 55（-4.4%，弱）（OI 21.5k）

📆 09-21 Forward Structure
存量OI: C 6.1k / P 2.6k，今日变化ΔOI: C +4.0k / P +1.1k，平值价格ATM: C $1.25 / P $1.14 ｜ ATM IV 39.0%，净 delta 敞口 168k shares
Top ΔOI: C 57 +3,140 ｜ P 58 +218 ｜ P 56 +170
仓位参考: Max Pain 57 ｜ Call Wall 57（-0.9%）（OI 3.2k） ｜ Put Wall 57（-0.9%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 39.0%｜历史 Rank 86%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 正 167,900 股

📆 09-23 Forward Structure
存量OI: C 1.9k / P 3.8k，今日变化ΔOI: C +0.5k / P +2.4k，平值价格ATM: C $1.40 / P $1.36 ｜ ATM IV 40.7%，净 delta 敞口 -56k shares
Top ΔOI: P 55 +1,097 ｜ P 56 +849
仓位参考: Max Pain 60 ｜ Call Wall 63（+9.5%，弱）（OI 0.3k） ｜ Put Wall 55（-4.4%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 40.7%｜历史 Rank 86%（近端代理）｜IV/RV 1.14×（近似）｜净 delta 敞口 负 55,677 股

📅 事件差分（观察，非因果）: 09-16（1D）ATM IV 53.6% vs 09-18 47.2%（差 +6.4pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/SLV_evening.json