# 期权晨报 2026-09-15（快照 11:20 ET）

📊 市场环境

SPY $758.10 ｜ QQQ $704.54
VIX 17.68 ↑3.4%（5D +12.5%） ｜ Vol Regime: NORMAL
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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,551.99 → 今开 1,569.71（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 1579.99 ｜ 低 1528.00

Options: P/C成交量 0.88 | OI比 1.15 | ATM IV 73.4% | Skew -2.6pp | Term 0.92 | ExpMove ±5.5%（近端） | Rank 27%
量化视角： IV 中性（Rank 27%）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -2.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.88×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.15×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（3D）±5.5% ｜ 09-25（10D）±8.9% ｜ 10-02（17D）±11.4% ｜ 10-09（24D）±13.7%
   ⇒ IV–VIX Spread: +55.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,679,190 | GEX Change vs 上次快照 -492,327 | Flip: Primary Flip: 1597.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 2005 / LOW 474 / INVALID 897
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1597.77（全链重定价，覆盖 100%）
Put Wall 1,500（弱结构｜现价高于该位 2.8%）
最近结构参考: Put Wall 1500（现价高于该位 2.8%）
量化视角： 负 Gamma（568万，无历史分位）｜负 Gamma 加深（49万）｜现价位于 Flip 下方 3.48%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,500（Put Wall，弱结构） / 1,500（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1598（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 1400.0P — Vol 11,956 | 最新价 $5.10 | OI 2028→4093 (ΔOI +2065张) | ΔOI/Volume 17.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2065张（+101.8% vs前日OI），连续性待观察（方向未知）
09-18 1750.0C — Vol 6,312 | 最新价 $4.60 | OI 1729→3451 (ΔOI +1722张) | ΔOI/Volume 27.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1722张（+99.6% vs前日OI），连续性待观察（方向未知）
10-16 1460.0P — Vol 901 | 最新价 $76.50 | OI 184→925 (ΔOI +741张) | ΔOI/Volume 82.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增741张（+402.7% vs前日OI），连续性待观察（方向未知）
09-18 1120.0P — Vol 708 | 最新价 $0.20 | OI 287→953 (ΔOI +666张) | ΔOI/Volume 94.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增666张（+232.1% vs前日OI），连续性待观察（方向未知）
09-18 2000.0C — Vol 1,836 | 最新价 $0.35 | OI 3024→3658 (ΔOI +634张) | ΔOI/Volume 34.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增634张（+21.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,828 张（Put 3,472 / Call 2,356），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +8.5k / P +7.5k ｜ Activity HIGH ｜ 3D
09-25  C +1.8k / P +1.1k ｜ Activity HIGH ｜ 10D
10-02  C +0.9k / P +0.6k ｜ Activity MEDIUM △ ｜ 17D
10-09  C +0.4k / P +0.2k ｜ Activity MEDIUM △ ｜ 24D

📆 09-18 Forward Structure
存量OI: C 84.9k / P 97.5k，今日变化ΔOI: C +8.5k / P +7.5k，平值价格ATM: C $43.40 / P $41.71 ｜ ATM IV 73.4%，净 delta 敞口 195k shares
Top ΔOI: P 1400 +2,065 ｜ C 1750 +1,722
仓位参考: Max Pain 1,500 ｜ Call Wall 1430（-7.3%，弱）（OI 2.2k） ｜ Put Wall 1400（-9.2%，弱）（OI 4.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 73.4%｜历史 Rank 27%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 195,209 股

📆 09-25 Forward Structure
存量OI: C 12.1k / P 18.7k，今日变化ΔOI: C +1.8k / P +1.1k，平值价格ATM: C $69.60 / P $67.24 ｜ ATM IV 66.3%，净 delta 敞口 42k shares
Top ΔOI: C 1800 -185 ｜ C 1530 +170 ｜ C 1650 +170
仓位参考: Max Pain 1,595 ｜ Call Wall 1650（+7.0%，弱）（OI 0.4k） ｜ Put Wall 1500（-2.7%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 66.3%｜历史 Rank 27%（近端代理）｜净 delta 敞口 正 41,975 股

10-02（MEDIUM △）Top ΔOI: 1800C +160 ｜ 1600C +134
10-02（MEDIUM △）仓位参考: Max Pain 1,590 ｜ Call Wall 1600（+3.8%，弱）（OI 0.4k） ｜ Put Wall 1500（-2.7%，弱）（OI 0.4k）

10-09（MEDIUM △）Top ΔOI: 1600C +50 ｜ 1490P +47
10-09（MEDIUM △）仓位参考: Max Pain 1,630 ｜ Call Wall 1600（+3.8%，弱）（OI 0.1k） ｜ Put Wall 1500（-2.7%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 09-18（3D）ATM IV 73.4% vs 09-25 66.3%（差 +7.1pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=22 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=22）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/SNDK_morning.json