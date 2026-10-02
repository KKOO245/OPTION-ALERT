# 期权晨报 2026-10-02（快照 10:20 ET）

📊 市场环境

SPY $771.73 ｜ QQQ $753.99
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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,787.69 → 今开 1,773.12（-0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 1774.23 ｜ 低 1721.00

Options: P/C成交量 0.50 | OI比 0.81 | ATM IV 87.2% | Skew -6.7pp | Term 0.80 | ExpMove ±7.0%（近端） | Rank 42%
量化视角： IV 中性（Rank 42%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（7D）±7.0% ｜ 10-16（14D）±9.8% ｜ 10-23（21D）±13.7% ｜ 10-30（28D）±15.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,495,070 | GEX Change vs 上次快照 -6,832,414 | Flip: Primary Flip: 1712.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1638 / LOW 493 / INVALID 1147
结构观察区: Primary Flip 1712.11（全链重定价，覆盖 98%）
最近结构参考: Flip 1712（现价高于该位 1.9%）
量化视角： 正 Gamma（550万，无历史分位）｜正 Gamma 减弱（683万）｜现价位于 Flip 上方 1.94%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,715（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1712（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 900.0P — Vol 1,505 | 最新价 $0.19 | OI 111→1512 (ΔOI +1401张) | ΔOI/Volume 93.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1401张（+1262.2% vs前日OI），连续性待观察（方向未知）
10-09 800.0P — Vol 737 | 最新价 $0.05 | OI 27→737 (ΔOI +710张) | ΔOI/Volume 96.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增710张（+2629.6% vs前日OI），连续性待观察（方向未知）
10-02 1900.0C — Vol 9,190 | 最新价 $3.20 | OI 3406→3967 (ΔOI +561张) | ΔOI/Volume 6.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增561张（+16.5% vs前日OI），连续性待观察（方向未知）
10-02 1850.0C — Vol 5,210 | 最新价 $8.00 | OI 1337→1801 (ΔOI +464张) | ΔOI/Volume 8.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增464张（+34.7% vs前日OI），连续性待观察（方向未知）
10-02 1670.0P — Vol 812 | 最新价 $1.01 | OI 228→634 (ΔOI +406张) | ΔOI/Volume 50.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增406张（+178.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,542 张（Put 2,517 / Call 1,025），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 54.2k / P 44.1k，今日成交量: C 28.3k / P 14.2k，平值价格ATM: C $15.55 / P $17.50 ｜ ATM IV 87.2%，预期波动 ±1.9%，Max Pain 1,715
Top ΔOI: P 900 -1,247 ｜ C 2000 -1,000 ｜ C 1900 +561

📆 Forward Expiration Structure

10-09  C +3.0k / P +5.2k ｜ Activity HIGH ｜ 7D
10-16  C +1.1k / P +1.0k ｜ Activity HIGH ｜ 14D
10-23  C +1.4k / P +0.4k ｜ Activity HIGH ｜ 21D
10-30  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 28D

📆 10-09 Forward Structure
存量OI: C 17.4k / P 19.7k，今日变化ΔOI: C +3.0k / P +5.2k，平值价格ATM: C $59.00 / P $63.10 ｜ ATM IV 60.8%，净 delta 敞口 13k shares
Top ΔOI: C 1900 +380
仓位参考: Max Pain 1,675 ｜ Call Wall 1900（+8.9%，弱）（OI 0.9k） ｜ Put Wall 1800（+3.1%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜ATM IV 60.8%｜历史 Rank 42%（近端代理）｜IV/RV 0.96×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 13,410 股

📆 10-16 Forward Structure
存量OI: C 39.7k / P 49.9k，今日变化ΔOI: C +1.1k / P +1.0k，平值价格ATM: C $83.83 / P $86.72 ｜ ATM IV 61.9%，净 delta 敞口 -17k shares
Top ΔOI: C 2300 +208 ｜ P 1670 +206
仓位参考: Max Pain 1,670 ｜ Call Wall 1900（+8.9%，弱）（OI 1.2k） ｜ Put Wall 1600（-8.3%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 61.9%｜历史 Rank 42%（近端代理）｜IV/RV 0.98×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 17,029 股

📆 10-23 Forward Structure
存量OI: C 6.6k / P 7.9k，今日变化ΔOI: C +1.4k / P +0.4k，平值价格ATM: C $125.15 / P $114.15 ｜ ATM IV 63.6%，净 delta 敞口 23k shares
Top ΔOI: C 2290 +170 ｜ C 2500 +101 ｜ C 1900 +87
仓位参考: Max Pain 1,740 ｜ Call Wall 1800（+3.1%，弱）（OI 0.3k） ｜ Put Wall 1650（-5.5%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 63.6%｜历史 Rank 42%（近端代理）｜IV/RV 1.00×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 22,753 股

10-30（MEDIUM △）Top ΔOI: 1860C +50 ｜ 2250C +48
10-30（MEDIUM △）仓位参考: Max Pain 1,725 ｜ Call Wall 1700（-2.6%，弱）（OI 0.1k） ｜ Put Wall 1600（-8.3%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/SNDK_morning.json