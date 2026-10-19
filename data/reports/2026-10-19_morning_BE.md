# 期权晨报 2026-10-19（快照 10:20 ET）

📊 市场环境

SPY $766.65 ｜ QQQ $721.12
VIX 18.46 ↓7.7%（5D +21.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 22.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🔴 **事件差分**: 10-23（4D）ATM IV 129.8% vs 10-30 101.7%（差 +28.1pp），覆盖 建筑许可 Prel、新屋开工
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-30 230P ΔOI -2,204（距现价 +2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 221.31 → 今开 233.23（+5.4%） | 较昨收变动（含盘初走势） ｜ 今日高 233.50 ｜ 低 224.20

Options: P/C成交量 0.36 | OI比 1.01 | ATM IV 129.8% | Skew 8.0pp | Term 0.67 | ExpMove ±11.2%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构倒挂（Term 0.67，近月 IV 高于远月）｜保护溢价显著（Skew 8.0pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.01×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（4D）±11.2% ｜ 10-30（11D）±14.5% ｜ 11-06（18D）±17.9% ｜ 11-13（25D）±18.6%
   ⇒ IV–VIX Spread: +111.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,548,677 | GEX Change vs 上次快照 403,503 | Flip: Primary Flip: 256.81（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 603 / LOW 47 / INVALID 178
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 256.81（全链重定价，覆盖 100%）
最近结构参考: Flip 257（现价低于该位 12.2%）
量化视角： 负 Gamma（755万，无历史分位）｜负 Gamma 缓解（+40万）｜现价位于 Flip 下方 12.19%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 248（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 257（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 195.0P — Vol 2,174 | 最新价 $11.67 | OI 1125→2809 (ΔOI +1684张) | ΔOI/Volume 77.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1684张（+149.7% vs前日OI），连续性待观察（方向未知）
10-23 145.0P — Vol 1,614 | 最新价 $0.24 | OI 20→1580 (ΔOI +1560张) | ΔOI/Volume 96.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1560张（+7800.0% vs前日OI），连续性待观察（方向未知）
10-23 190.0C — Vol 1,541 | 最新价 $35.06 | OI 78→1566 (ΔOI +1488张) | ΔOI/Volume 96.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1488张（+1907.7% vs前日OI），连续性待观察（方向未知）
11-20 165.0P — Vol 787 | 最新价 $4.20 | OI 922→1653 (ΔOI +731张) | ΔOI/Volume 92.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增731张（+79.3% vs前日OI），连续性待观察（方向未知）
10-23 180.0P — Vol 1,146 | 最新价 $1.86 | OI 361→1028 (ΔOI +667张) | ΔOI/Volume 58.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增667张（+184.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,130 张（Put 4,642 / Call 1,488），跨 2 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +4.8k / P +8.0k ｜ Activity HIGH ｜ 4D
10-30  C +1.0k / P -1.7k ｜ Activity HIGH ｜ 11D
11-06  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 18D
11-13  C +0.6k / P +0.5k ｜ Activity MEDIUM △ ｜ 25D

📆 10-23 Forward Structure
存量OI: C 37.9k / P 38.1k，今日变化ΔOI: C +4.8k / P +8.0k，平值价格ATM: C $13.00 / P $12.20 ｜ ATM IV 129.8%，净 delta 敞口 127k shares
Top ΔOI: C 190 +1,488 ｜ C 255 -863
仓位参考: Max Pain 248 ｜ Call Wall 230（+2.0%，弱）（OI 1.5k） ｜ Put Wall 230（+2.0%，弱）（OI 2.4k）
量化解读： 存量两侧均衡｜ATM IV 129.8%｜历史 Rank 83%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 127,144 股

📆 10-30 Forward Structure
存量OI: C 18.0k / P 22.6k，今日变化ΔOI: C +1.0k / P -1.7k，平值价格ATM: C $16.51 / P $16.09 ｜ ATM IV 101.7%，净 delta 敞口 154k shares
Top ΔOI: P 230 -2,204 ｜ P 205 +329 ｜ P 285 -280
仓位参考: Max Pain 252 ｜ Call Wall 240（+6.4%，弱）（OI 1.4k） ｜ Put Wall 240（+6.4%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 101.7%｜历史 Rank 83%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 153,990 股

11-06（MEDIUM △）Top ΔOI: 250C +133 ｜ 250P +57
11-06（MEDIUM △）仓位参考: Max Pain 260 ｜ Call Wall 240（+6.4%，弱）（OI 0.2k） ｜ Put Wall 235（+4.2%）（OI 2.8k）

11-13（MEDIUM △）Top ΔOI: 270C +267 ｜ 250C +203
11-13（MEDIUM △）仓位参考: Max Pain 265 ｜ Call Wall 240（+6.4%，弱）（OI 0.3k） ｜ Put Wall 230（+2.0%）（OI 2.2k）

📅 事件差分（观察，非因果）: 10-23（4D）ATM IV 129.8% vs 10-30 101.7%（差 +28.1pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/BE_morning.json