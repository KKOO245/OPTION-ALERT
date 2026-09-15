# 期权晨报 2026-09-15（快照 11:20 ET）

📊 市场环境

SPY $756.82 ｜ QQQ $705.57
VIX 17.68 ↑3.4%（5D +12.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.1（fear）
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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-16 57P ΔOI +3,420（距现价 +0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-21 57C ΔOI +3,140 占该期限总 OI 36.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 56.84 → 今开 57.48（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 57.73 ｜ 低 56.95

Options: P/C成交量 0.84 | OI比 0.94 | ATM IV 52.1% | Skew -1.5pp | Term 0.83 | ExpMove ±2.4%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.94×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-16（1D）±2.4% ｜ 09-18（3D）±3.9% ｜ 09-21（6D）±4.4% ｜ 09-23（8D）±5.3%
   ⇒ IV–VIX Spread: +34.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 20,658,284 | GEX Change vs 上次快照 7,093,139 | Flip: Primary Flip: 56.39（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 950 / LOW 199 / INVALID 469
结构观察区: Primary Flip 56.39（全链重定价，覆盖 99%）
最近结构参考: Flip 56（现价高于该位 1.1%）
量化视角： 正 Gamma（2066万，无历史分位）｜正 Gamma 增强（+709万）｜现价位于 Flip 上方 1.06%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 58（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 56（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 64.0C — Vol 12,399 | 最新价 $0.94 | OI 56350→68511 (ΔOI +12161张) | ΔOI/Volume 98.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12161张（+21.6% vs前日OI），连续性待观察（方向未知）
10-09 100.0C — Vol 8,859 | 最新价 $0.04 | OI 209→8652 (ΔOI +8443张) | ΔOI/Volume 95.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8443张（+4039.7% vs前日OI），连续性待观察（方向未知）
09-16 57.5C — Vol 4,870 | 最新价 $0.54 | OI 0→4109 (ΔOI +4109张) | ΔOI/Volume 84.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4109张（前日OI缺失），连续性待观察（方向未知）
09-25 63.5C — Vol 4,482 | 最新价 $0.29 | OI 1684→5708 (ΔOI +4024张) | ΔOI/Volume 89.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4024张（+238.9% vs前日OI），连续性待观察（方向未知）
09-18 74.5C — Vol 4,267 | 最新价 $0.02 | OI 1230→5037 (ΔOI +3807张) | ΔOI/Volume 89.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3807张（+309.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 32,544 张（Put 0 / Call 32,544），跨 5 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-16  C +12.4k / P +7.6k ｜ Activity HIGH ｜ 1D
09-18  C +2.4k / P +3.2k ｜ Activity HIGH ｜ 3D
09-21  C +4.0k / P +1.1k ｜ Activity HIGH ｜ 6D
09-23  C +0.5k / P +2.4k ｜ Activity HIGH ｜ 8D

📆 09-16 Forward Structure
存量OI: C 26.9k / P 25.2k，今日变化ΔOI: C +12.4k / P +7.6k，平值价格ATM: C $0.71 / P $0.66 ｜ ATM IV 52.1%，净 delta 敞口 93k shares
Top ΔOI: C 57 +4,109 ｜ P 57 +3,420 ｜ C 58 +1,186
仓位参考: Max Pain 58 ｜ Call Wall 57.5（+0.9%，弱）（OI 4.1k） ｜ Put Wall 58（+1.8%，弱）（OI 4.9k）
量化解读： 存量两侧均衡｜ATM IV 52.1%｜历史 Rank 85%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 93,269 股

📆 09-18 Forward Structure
存量OI: C 967.5k / P 466.0k，今日变化ΔOI: C +2.4k / P +3.2k，平值价格ATM: C $1.16 / P $1.08 ｜ ATM IV 52.3%，净 delta 敞口 152k shares
Top ΔOI: C 63 -5,389 ｜ P 56 +3,176
仓位参考: Max Pain 60 ｜ Call Wall 60（+5.3%，弱）（OI 42.3k） ｜ Put Wall 55（-3.5%，弱）（OI 21.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 52.3%｜历史 Rank 85%（近端代理）｜IV/RV 1.47×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 152,475 股

📆 09-21 Forward Structure
存量OI: C 6.1k / P 2.6k，今日变化ΔOI: C +4.0k / P +1.1k，平值价格ATM: C $1.26 / P $1.23 ｜ ATM IV 42.9%，净 delta 敞口 141k shares
Top ΔOI: C 57 +3,140 ｜ P 58 +218 ｜ P 56 +170
仓位参考: Max Pain 57 ｜ Call Wall 57（+0.0%）（OI 3.2k） ｜ Put Wall 57（+0.0%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 42.9%｜历史 Rank 85%（近端代理）｜IV/RV 1.20×（近似）｜净 delta 敞口 正 141,226 股

📆 09-23 Forward Structure
存量OI: C 1.9k / P 3.8k，今日变化ΔOI: C +0.5k / P +2.4k，平值价格ATM: C $1.59 / P $1.44 ｜ ATM IV 43.8%，净 delta 敞口 -68k shares
Top ΔOI: P 55 +1,097 ｜ P 56 +849
仓位参考: Max Pain 60 ｜ Call Wall 58（+1.8%，弱）（OI 0.3k） ｜ Put Wall 55（-3.5%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 43.8%｜历史 Rank 85%（近端代理）｜IV/RV 1.23×（近似）｜净 delta 敞口 负 68,333 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/SLV_morning.json