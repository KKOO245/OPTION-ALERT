# 期权晨报 2026-11-11（快照 10:20 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $nan
VIX 18.31 ↓5.9%（5D +10.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 395C ΔOI +2,183（距现价 +1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 379.78 → 今开 386.58（+1.8%） | 较昨收变动（含盘初走势） ｜ 今日高 393.98 ｜ 低 386.35

Options: P/C成交量 0.38 | OI比 1.20 | ATM IV 59.1% | Skew 3.0pp | Term 0.56 | ExpMove ±0.0%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构倒挂（Term 0.56，近月 IV 高于远月）｜保护溢价中性（Skew 3.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.20×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±0.0% ｜ 11-16（5D）±3.7% ｜ 11-18（7D）±4.7% ｜ 11-20（9D）±0.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 125,973,888 | GEX Change vs 上次快照 57,956,958 | Flip: Primary Flip: 367.97（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1507 / LOW 245 / INVALID 910
结构观察区: Primary Flip 367.97（全链重定价，覆盖 97%）
Call Wall 400（现价低于该位 2.3%）
最近结构参考: Call Wall 400（现价低于该位 2.3%）
量化视角： 正 Gamma（1.26亿，无历史分位）｜正 Gamma 增强（+5796万）｜现价位于 Flip 上方 6.23%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 375（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 368（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 372.5P — Vol 7,290 | 最新价 $8.50 | OI 589→6507 (ΔOI +5918张) | ΔOI/Volume 81.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5918张（+1004.8% vs前日OI），连续性待观察（方向未知）
11-11 345.0P — Vol 6,129 | 最新价 $0.05 | OI 7666→12729 (ΔOI +5063张) | ΔOI/Volume 82.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5063张（+66.0% vs前日OI），连续性待观察（方向未知）
11-11 375.0P — Vol 45,556 | 最新价 $2.03 | OI 1630→6204 (ΔOI +4574张) | ΔOI/Volume 10.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4574张（+280.6% vs前日OI），连续性待观察（方向未知）
11-11 377.5C — Vol 43,861 | 最新价 $5.05 | OI 688→5054 (ΔOI +4366张) | ΔOI/Volume 9.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4366张（+634.6% vs前日OI），连续性待观察（方向未知）
11-11 360.0P — Vol 14,892 | 最新价 $0.21 | OI 1566→4513 (ΔOI +2947张) | ΔOI/Volume 19.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2947张（+188.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 22,868 张（Put 18,502 / Call 4,366），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $6M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 72.1k / P 86.6k，今日成交量: C 244.2k / P 93.4k，平值价格ATM: C $2.51 / P $2.50 ｜ ATM IV 59.1%，预期波动 ±1.3%，Max Pain 375
Top ΔOI: P 345 +5,063 ｜ P 375 +4,574 ｜ C 377 +4,366

📆 Forward Expiration Structure

11-13  C +9.1k / P +9.9k ｜ Activity HIGH ｜ 2D
11-16  C +2.1k / P +2.8k ｜ Activity HIGH ｜ 5D
11-18  C +1.7k / P +2.1k ｜ Activity HIGH ｜ 7D
11-20  C +1.1k / P +11.3k ｜ Activity HIGH ｜ 9D

📆 11-13 Forward Structure
存量OI: C 162.0k / P 233.1k，今日变化ΔOI: C +9.1k / P +9.9k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 14.1%，净 delta 敞口 367k shares
Top ΔOI: C 395 +2,183 ｜ C 400 +1,890
仓位参考: Max Pain 360 ｜ Call Wall 400（+2.3%）（OI 13.6k）
量化解读： 存量 Put 重｜ATM IV 14.1%｜历史 Rank 70%（近端代理）｜IV/RV 0.25×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 367,151 股

📆 11-16 Forward Structure
存量OI: C 23.3k / P 13.1k，今日变化ΔOI: C +2.1k / P +2.8k，平值价格ATM: C $7.60 / P $6.85 ｜ ATM IV 40.2%，净 delta 敞口 26k shares
Top ΔOI: C 400 +495 ｜ C 415 +323
仓位参考: Max Pain 375 ｜ Call Wall 400（+2.3%，弱）（OI 1.6k） ｜ Put Wall 380（-2.8%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 40.2%｜历史 Rank 70%（近端代理）｜IV/RV 0.71×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 25,968 股

📆 11-18 Forward Structure
存量OI: C 7.5k / P 7.2k，今日变化ΔOI: C +1.7k / P +2.1k，平值价格ATM: C $9.50 / P $9.00 ｜ ATM IV 44.0%，净 delta 敞口 48k shares
Top ΔOI: C 410 +317 ｜ C 390 +225
仓位参考: Max Pain 370 ｜ Call Wall 410（+4.9%，弱）（OI 0.6k） ｜ Put Wall 355（-9.2%，弱）（OI 0.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 44.0%｜历史 Rank 70%（近端代理）｜IV/RV 0.77×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 48,380 股

📆 11-20 Forward Structure
存量OI: C 283.2k / P 309.7k，今日变化ΔOI: C +1.1k / P +11.3k，平值价格ATM: C $0.29 / P $0.00 ｜ ATM IV 17.7%，净 delta 敞口 -95k shares
Top ΔOI: P 372 +5,918
仓位参考: Max Pain 375 ｜ Call Wall 400（+2.3%，弱）（OI 21.3k）
量化解读： 存量两侧均衡｜ATM IV 17.7%｜历史 Rank 70%（近端代理）｜IV/RV 0.31×（近似）｜净 delta 敞口 负 94,630 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/TSLA_morning.json