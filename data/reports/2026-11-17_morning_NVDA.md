# 期权晨报 2026-11-17（快照 10:20 ET）

📊 市场环境

SPY $737.44 ｜ QQQ $658.34
VIX 22.73 ↓0.8%（5D +16.8%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.8　✅ 今日已公布
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **事件差分**: 11-18（1D）ATM IV 172.2% vs 11-20 114.1%（差 +58.1pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-18 160C ΔOI +10,600（距现价 +3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 156.14 → 今开 156.91（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 157.46 ｜ 低 153.44

Options: P/C成交量 0.87 | OI比 0.81 | ATM IV 172.2% | Skew -1.1pp | Term 0.34 | ExpMove ±8.1%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.34，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.87×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-18（1D）±8.1% ｜ 11-20（3D）±0.3% ｜ 11-23（6D）±10.0% ｜ 11-25（8D）±10.9%
   ⇒ IV–VIX Spread: +149.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -21,533,097 | GEX Change vs 上次快照 34,369,048 | Flip: Primary Flip: 157.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1260 / LOW 209 / INVALID 605
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 157.00（全链重定价，覆盖 100%）
最近结构参考: Flip 157（现价低于该位 1.2%）
量化视角： 负 Gamma（2153万，无历史分位）｜负 Gamma 缓解（+3437万）｜现价位于 Flip 下方 1.19%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 160（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 157（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 170.0C — Vol 33,191 | 最新价 $6.25 | OI 44663→66094 (ΔOI +21431张) | ΔOI/Volume 64.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21431张（+48.0% vs前日OI），连续性待观察（方向未知）
11-18 160.0C — Vol 35,166 | 最新价 $4.81 | OI 3995→14595 (ΔOI +10600张) | ΔOI/Volume 30.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10600张（+265.3% vs前日OI），连续性待观察（方向未知）
11-20 170.0C — Vol 33,180 | 最新价 $2.69 | OI 47389→56583 (ΔOI +9194张) | ΔOI/Volume 27.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9194张（+19.4% vs前日OI），连续性待观察（方向未知）
12-11 225.0C — Vol 14,527 | 最新价 $0.36 | OI 4871→13859 (ΔOI +8988张) | ΔOI/Volume 61.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8988张（+184.5% vs前日OI），连续性待观察（方向未知）
11-20 187.5C — Vol 11,591 | 最新价 $0.59 | OI 10706→18942 (ΔOI +8236张) | ΔOI/Volume 71.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8236张（+76.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 58,449 张（Put 0 / Call 58,449），跨 4 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-18  C +72.6k / P +53.1k ｜ Activity HIGH ｜ 1D
11-20  C +76.3k / P +32.3k ｜ Activity HIGH ｜ 3D
11-23  C +10.1k / P +5.7k ｜ Activity HIGH ｜ 6D
11-25  C +6.6k / P +2.9k ｜ Activity HIGH ｜ 8D

📆 11-18 Forward Structure
存量OI: C 244.2k / P 196.7k，今日变化ΔOI: C +72.6k / P +53.1k，平值价格ATM: C $6.34 / P $6.19 ｜ ATM IV 172.2%，净 delta 敞口 1.2M shares
Top ΔOI: C 160 +10,600 ｜ C 170 +6,621 ｜ P 140 +5,846
仓位参考: Max Pain 160 ｜ Call Wall 170（+9.6%，弱）（OI 16.2k） ｜ Put Wall 150（-3.3%，弱）（OI 18.6k）
量化解读： 存量 Call 重｜ATM IV 172.2%｜历史 Rank 100%（近端代理）｜IV/RV 3.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,180,197 股

📆 11-20 Forward Structure
存量OI: C 1453.5k / P 965.1k，今日变化ΔOI: C +76.3k / P +32.3k，平值价格ATM: C $0.00 / P $0.40 ｜ ATM IV 114.1%，净 delta 敞口 1.9M shares
Top ΔOI: C 170 +9,194 ｜ C 187 +8,236 ｜ C 190 +8,194
仓位参考: Max Pain 182 ｜ Call Wall 170（+9.6%，弱）（OI 56.6k） ｜ Put Wall 150（-3.3%，弱）（OI 49.0k）
量化解读： 存量 Call 重｜ATM IV 114.1%｜历史 Rank 100%（近端代理）｜IV/RV 2.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,882,826 股

📆 11-23 Forward Structure
存量OI: C 44.0k / P 24.3k，今日变化ΔOI: C +10.1k / P +5.7k，平值价格ATM: C $7.85 / P $7.70 ｜ ATM IV 96.0%，净 delta 敞口 217k shares
Top ΔOI: P 145 +2,006 ｜ C 160 +1,796
仓位参考: Max Pain 160 ｜ Call Wall 160（+3.1%，弱）（OI 3.2k） ｜ Put Wall 145（-6.5%，弱）（OI 2.6k）
量化解读： 存量 Call 重｜ATM IV 96.0%｜历史 Rank 100%（近端代理）｜IV/RV 1.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 216,631 股

📆 11-25 Forward Structure
存量OI: C 26.3k / P 8.7k，今日变化ΔOI: C +6.6k / P +2.9k，平值价格ATM: C $8.60 / P $8.30 ｜ ATM IV 90.0%，净 delta 敞口 124k shares
Top ΔOI: C 157 +937 ｜ C 167 +751 ｜ C 170 +596
仓位参考: Max Pain 158 ｜ Call Wall 165（+6.4%，弱）（OI 3.2k） ｜ Put Wall 150（-3.3%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 90.0%｜历史 Rank 100%（近端代理）｜IV/RV 1.75×（近似）｜净 delta 敞口 正 124,459 股

📅 事件差分（观察，非因果）: 11-18（1D）ATM IV 172.2% vs 11-20 114.1%（差 +58.1pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=98 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=98）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/NVDA_morning.json