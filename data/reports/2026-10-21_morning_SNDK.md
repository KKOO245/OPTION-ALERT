# 期权晨报 2026-10-21（快照 10:20 ET）

📊 市场环境

SPY $773.28 ｜ QQQ $725.20
VIX 17.20 ↓0.6%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,365.38 → 今开 1,417.00（+3.8%） | 较昨收变动（含盘初走势） ｜ 今日高 1424.48 ｜ 低 1327.62

Options: P/C成交量 0.50 | OI比 0.83 | ATM IV 82.3% | Skew 1.8pp | Term 0.90 | ExpMove ±5.2%（近端） | Rank 41%
量化视角： IV 中性（Rank 41%）｜期限结构正常（Term 0.90）｜保护溢价薄（Skew 1.8pp）｜存量 Call 偏重（OI比 0.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（2D）±5.2% ｜ 10-30（9D）±12.2% ｜ 11-06（16D）±14.7% ｜ 11-13（23D）±15.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,194,195 | GEX Change vs 上次快照 1,968,516 | Flip: Primary Flip: 1378.60（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1938 / LOW 478 / INVALID 1038
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1378.60（全链重定价，覆盖 99%）
Call Wall 1,500（现价低于该位 9.0%）
最近结构参考: Flip 1379（现价低于该位 0.9%）
量化视角： 负 Gamma（119万，无历史分位）｜负 Gamma 缓解（+197万）｜现价位于 Flip 下方 0.94%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,405（MaxPain，仅结算参考） / 1,500（Call Wall）。
• Gamma 区域：切换参考 1379（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 700.0P — Vol 404 | 最新价 $0.05 | OI 1556→2016 (ΔOI +460张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增460张（+29.6% vs前日OI），值得跟踪（方向未知）
10-23 1000.0P — Vol 769 | 最新价 $0.18 | OI 1521→1917 (ΔOI +396张) | ΔOI/Volume 51.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增396张（+26.0% vs前日OI），连续性待观察（方向未知）
10-30 2860.0C — Vol 464 | 最新价 $0.07 | OI 1337→1643 (ΔOI +306张) | ΔOI/Volume 66.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增306张（+22.9% vs前日OI），连续性待观察（方向未知）
10-30 1350.0C — Vol 370 | 最新价 $94.90 | OI 324→630 (ΔOI +306张) | ΔOI/Volume 82.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增306张（+94.4% vs前日OI），连续性待观察（方向未知）
10-23 1500.0C — Vol 4,123 | 最新价 $4.20 | OI 2941→3221 (ΔOI +280张) | ΔOI/Volume 6.8% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增280张（+9.5% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,748 张（Put 856 / Call 892），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +3.8k / P +1.8k ｜ Activity HIGH ｜ 2D
10-30  C +1.3k / P +0.9k ｜ Activity HIGH ｜ 9D
11-06  C +0.5k / P +78 ｜ Activity MEDIUM △ ｜ 16D
11-13  C +0.4k / P -49 ｜ Activity MEDIUM △ ｜ 23D

📆 10-23 Forward Structure
存量OI: C 47.1k / P 39.1k，今日变化ΔOI: C +3.8k / P +1.8k，平值价格ATM: C $35.20 / P $36.00 ｜ ATM IV 82.3%，净 delta 敞口 174k shares
Top ΔOI: C 1500 +280
仓位参考: Max Pain 1,405 ｜ Call Wall 1500（+9.8%）（OI 3.2k） ｜ Put Wall 1250（-8.5%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 82.3%｜历史 Rank 41%（近端代理）｜IV/RV 1.66×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 174,221 股

📆 10-30 Forward Structure
存量OI: C 26.1k / P 17.2k，今日变化ΔOI: C +1.3k / P +0.9k，平值价格ATM: C $81.03 / P $85.30 ｜ ATM IV 92.2%，净 delta 敞口 15k shares
Top ΔOI: C 1350 +306
仓位参考: Max Pain 1,500 ｜ Call Wall 1500（+9.8%，弱）（OI 1.4k） ｜ Put Wall 1400（+2.5%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 92.2%｜历史 Rank 41%（近端代理）｜IV/RV 1.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 15,213 股

11-06（MEDIUM △）Top ΔOI: 1040P -122 ｜ 1280P +52
11-06（MEDIUM △）仓位参考: Max Pain 1,500 ｜ Call Wall 1400（+2.5%，弱）（OI 0.7k） ｜ Put Wall 1400（+2.5%，弱）（OI 0.4k）

11-13（MEDIUM △）Top ΔOI: 1040P -121 ｜ 1280P +45
11-13（MEDIUM △）仓位参考: Max Pain 1,500 ｜ Call Wall 1480（+8.4%，弱）（OI 0.2k） ｜ Put Wall 1300（-4.8%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/SNDK_morning.json