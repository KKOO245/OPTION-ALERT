# 期权晨报 2026-09-16（快照 11:22 ET）

📊 市场环境

SPY $760.53 ｜ QQQ $710.92
VIX 16.68 ↓3.0%（5D +1.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75　⏰ 今日
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　⏰ 今日
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　⏰ 今日
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,530.90 → 今开 1,546.62（+1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 1560.58 ｜ 低 1519.54

Options: P/C成交量 0.77 | OI比 1.10 | ATM IV 77.7% | Skew -1.3pp | Term 0.87 | ExpMove ±4.9%（近端） | Rank 32%
量化视角： IV 中性（Rank 32%）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.10×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（2D）±4.9% ｜ 09-25（9D）±8.8% ｜ 10-02（16D）±11.8% ｜ 10-09（23D）±14.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,114,751 | GEX Change vs 上次快照 1,500,184 | Flip: Primary Flip: 1580.39（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1941 / LOW 498 / INVALID 937
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1580.39（全链重定价，覆盖 99%）
Put Wall 1,500（弱结构｜现价高于该位 2.8%）
最近结构参考: Flip 1580（现价低于该位 2.4%）
量化视角： 负 Gamma（511万，无历史分位）｜负 Gamma 缓解（+150万）｜现价位于 Flip 下方 2.38%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,500（Put Wall，弱结构） / 1,500（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1580（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 900.0P — Vol 1,039 | 最新价 $1.56 | OI 1332→2147 (ΔOI +815张) | ΔOI/Volume 78.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增815张（+61.2% vs前日OI），连续性待观察（方向未知）
09-18 1750.0C — Vol 2,674 | 最新价 $2.05 | OI 3451→4200 (ΔOI +749张) | ΔOI/Volume 28.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增749张（+21.7% vs前日OI），连续性待观察（方向未知）
09-18 1700.0C — Vol 2,508 | 最新价 $3.86 | OI 2352→3022 (ΔOI +670张) | ΔOI/Volume 26.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增670张（+28.5% vs前日OI），连续性待观察（方向未知）
09-18 1800.0C — Vol 2,127 | 最新价 $1.00 | OI 3456→4017 (ΔOI +561张) | ΔOI/Volume 26.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增561张（+16.2% vs前日OI），连续性待观察（方向未知）
09-18 1420.0P — Vol 729 | 最新价 $6.75 | OI 854→1409 (ΔOI +555张) | ΔOI/Volume 76.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增555张（+65.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,350 张（Put 1,370 / Call 1,980），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +6.1k / P +3.0k ｜ Activity HIGH ｜ 2D
09-25  C +2.0k / P +0.8k ｜ Activity HIGH ｜ 9D
10-02  C +0.5k / P +83 ｜ Activity HIGH ｜ 16D
10-09  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 23D

📆 09-18 Forward Structure
存量OI: C 91.0k / P 100.5k，今日变化ΔOI: C +6.1k / P +3.0k，平值价格ATM: C $34.84 / P $40.75 ｜ ATM IV 77.7%，净 delta 敞口 99k shares
Top ΔOI: C 1750 +749 ｜ C 1700 +670
仓位参考: Max Pain 1,500 ｜ Call Wall 1430（-7.3%，弱）（OI 2.2k） ｜ Put Wall 1400（-9.3%，弱）（OI 4.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 77.7%｜历史 Rank 32%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 99,309 股

📆 09-25 Forward Structure
存量OI: C 14.2k / P 19.5k，今日变化ΔOI: C +2.0k / P +0.8k，平值价格ATM: C $66.50 / P $70.10 ｜ ATM IV 68.1%，净 delta 敞口 39k shares
Top ΔOI: C 1580 +263 ｜ C 1550 +235
仓位参考: Max Pain 1,580 ｜ Call Wall 1550（+0.5%，弱）（OI 0.5k） ｜ Put Wall 1500（-2.8%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 68.1%｜历史 Rank 32%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 39,349 股

📆 10-02 Forward Structure
存量OI: C 8.8k / P 9.9k，今日变化ΔOI: C +0.5k / P +83，平值价格ATM: C $91.00 / P $91.88 ｜ ATM IV 69.5%，净 delta 敞口 11k shares
Top ΔOI: C 1800 +85 ｜ C 1900 +45
仓位参考: Max Pain 1,580 ｜ Call Wall 1600（+3.7%，弱）（OI 0.5k） ｜ Put Wall 1500（-2.8%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 69.5%｜历史 Rank 32%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 10,531 股

10-09（MEDIUM △）Top ΔOI: 2000C +82 ｜ 1400P +34
10-09（MEDIUM △）仓位参考: Max Pain 1,620 ｜ Call Wall 1600（+3.7%，弱）（OI 0.1k） ｜ Put Wall 1500（-2.8%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 77.7% vs 09-25 68.1%（差 +9.7pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/SNDK_morning.json