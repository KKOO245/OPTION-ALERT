# 期权晨报 2026-10-02（快照 10:20 ET）

📊 市场环境

SPY $771.73 ｜ QQQ $754.00
VIX 15.56 ↓5.1%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-09 155C ΔOI +2,254（距现价 -0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 148.07 → 今开 149.55（+1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 157.34 ｜ 低 149.34

Options: P/C成交量 0.44 | OI比 1.00 | ATM IV 78.9% | Skew -1.3pp | Term 0.57 | ExpMove ±5.0%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.57，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.00×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（7D）±5.0% ｜ 10-16（14D）±6.9% ｜ 10-23（21D）±8.3% ｜ 10-30（28D）±9.9%
   ⇒ IV–VIX Spread: +63.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 119,792,881 | GEX Change vs 上次快照 120,842,300 | Flip: Primary Flip: 147.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 478 / LOW 129 / INVALID 315
结构观察区: Primary Flip 147.89（全链重定价，覆盖 99%）
Call Wall 160（弱结构｜现价低于该位 2.6%）
最近结构参考: Call Wall 160（现价低于该位 2.6%）
量化视角： 正 Gamma（1.20亿，无历史分位）｜由负转正（+1.21亿）｜现价位于 Flip 上方 5.43%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 149（MaxPain，仅结算参考）；上方 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 148（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 142.0P — Vol 7,089 | 最新价 $1.25 | OI 1431→7679 (ΔOI +6248张) | ΔOI/Volume 88.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6248张（+436.6% vs前日OI），连续性待观察（方向未知）
10-16 170.0C — Vol 11,164 | 最新价 $0.35 | OI 19100→23583 (ΔOI +4483张) | ΔOI/Volume 40.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4483张（+23.5% vs前日OI），连续性待观察（方向未知）
10-09 155.0C — Vol 19,846 | 最新价 $1.22 | OI 6461→8715 (ΔOI +2254张) | ΔOI/Volume 11.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2254张（+34.9% vs前日OI），连续性待观察（方向未知）
10-09 146.0P — Vol 3,571 | 最新价 $2.56 | OI 1239→3487 (ΔOI +2248张) | ΔOI/Volume 63.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2248张（+181.4% vs前日OI），连续性待观察（方向未知）
10-02 155.0C — Vol 78,612 | 最新价 $0.09 | OI 24311→26239 (ΔOI +1928张) | ΔOI/Volume 2.5% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增1928张（+7.9% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 17,161 张（Put 8,496 / Call 8,665），跨 3 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 204.0k / P 204.1k，今日成交量: C 126.1k / P 55.6k，平值价格ATM: C $1.82 / P $0.94 ｜ ATM IV 78.9%，预期波动 ±1.8%，Max Pain 149
Top ΔOI: P 140 -3,365 ｜ C 155 +1,928 ｜ P 160 -1,446

📆 Forward Expiration Structure

10-09  C +13.2k / P +16.8k ｜ Activity HIGH ｜ 7D
10-16  C +2.3k / P -0.8k ｜ Activity MEDIUM △ ｜ 14D
10-23  C +1.5k / P +0.7k ｜ Activity HIGH ｜ 21D
10-30  C +2.0k / P +1.6k ｜ Activity HIGH ｜ 28D

📆 10-09 Forward Structure
存量OI: C 98.0k / P 74.9k，今日变化ΔOI: C +13.2k / P +16.8k，平值价格ATM: C $4.40 / P $3.40 ｜ ATM IV 44.2%，净 delta 敞口 328k shares
Top ΔOI: P 142 +6,248 ｜ C 155 +2,254 ｜ P 146 +2,248
仓位参考: Max Pain 150 ｜ Call Wall 155（-0.6%，弱）（OI 8.7k） ｜ Put Wall 142（-8.9%，弱）（OI 7.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 44.2%｜历史 Rank 98%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 正 328,312 股

10-16（MEDIUM △）Top ΔOI: 170C +4,483 ｜ 145C -3,270
10-16（MEDIUM △）仓位参考: Max Pain 143 ｜ Call Wall 160（+2.6%）（OI 42.4k） ｜ Put Wall 150（-3.8%，弱）（OI 20.2k）

📆 10-23 Forward Structure
存量OI: C 29.0k / P 25.5k，今日变化ΔOI: C +1.5k / P +0.7k，平值价格ATM: C $7.05 / P $5.85 ｜ ATM IV 43.4%，净 delta 敞口 54k shares
Top ΔOI: C 152 +394 ｜ P 145 +265 ｜ C 150 +230
仓位参考: Max Pain 148 ｜ Call Wall 150（-3.8%，弱）（OI 3.8k） ｜ Put Wall 145（-7.0%，弱）（OI 2.6k）
量化解读： 存量两侧均衡｜ATM IV 43.4%｜历史 Rank 98%（近端代理）｜IV/RV 1.16×（近似）｜净 delta 敞口 正 53,586 股

📆 10-30 Forward Structure
存量OI: C 30.8k / P 42.4k，今日变化ΔOI: C +2.0k / P +1.6k，平值价格ATM: C $8.38 / P $7.07 ｜ ATM IV 44.6%，净 delta 敞口 51k shares
Top ΔOI: C 152 +617
仓位参考: Max Pain 150 ｜ Call Wall 160（+2.6%，弱）（OI 2.8k） ｜ Put Wall 145（-7.0%，弱）（OI 3.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 44.6%｜历史 Rank 98%（近端代理）｜IV/RV 1.20×（近似）｜净 delta 敞口 正 50,888 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/SPCX_morning.json