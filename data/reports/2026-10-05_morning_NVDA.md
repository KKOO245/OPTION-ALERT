# 期权晨报 2026-10-05（快照 10:20 ET）

📊 市场环境

SPY $771.25 ｜ QQQ $753.47
VIX 15.75 ↑2.9%（5D -2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 43.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 10-05 10:00　【高】ISM 非制造业 PMI　预测 55 ｜ 实际 54.9 ｜ 前值 55.4　✅ 今日已公布
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-07 240C ΔOI +5,039（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 233.95 → 今开 236.07（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 237.86 ｜ 低 235.15

Options: P/C成交量 0.50 | OI比 1.56 | ATM IV 33.4% | Skew 2.9pp | Term 0.90 | ExpMove ±1.9%（近端） | Rank 16%
量化视角： IV 历史低位（Rank 16%，期权偏便宜）｜期限结构正常（Term 0.90）｜保护溢价中性（Skew 2.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.56×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-07（2D）±1.9% ｜ 10-09（4D）±2.7% ｜ 10-12（7D）±3.0% ｜ 10-14（9D）±3.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 556,645,757 | GEX Change vs 上次快照 173,322,000 | Flip: Primary Flip: 223.83（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 653 / LOW 189 / INVALID 532
结构观察区: Primary Flip 223.83（全链重定价，覆盖 97%）
Put Wall 220（弱结构｜现价高于该位 7.8%） | Call Wall 240（弱结构｜现价低于该位 1.2%）
最近结构参考: Call Wall 240（现价低于该位 1.2%）
量化视角： 正 Gamma（5.57亿，无历史分位）｜正 Gamma 增强（+1.73亿）｜现价位于 Flip 上方 5.96%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（Put Wall，弱结构） / 232（MaxPain，仅结算参考）；上方 240（Call Wall，弱结构）。
• Gamma 区域：切换参考 224（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 240.0C — Vol 115,412 | 最新价 $1.18 | OI 19594→78334 (ΔOI +58740张) | ΔOI/Volume 50.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增58740张（+299.8% vs前日OI），连续性待观察（方向未知）
10-09 110.0P — Vol 37,127 | 最新价 $0.01 | OI 9921→46135 (ΔOI +36214张) | ΔOI/Volume 97.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增36214张（+365.0% vs前日OI），连续性待观察（方向未知）
10-09 245.0C — Vol 61,785 | 最新价 $0.41 | OI 11268→43713 (ΔOI +32445张) | ΔOI/Volume 52.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增32445张（+287.9% vs前日OI），连续性待观察（方向未知）
10-09 247.5C — Vol 41,486 | 最新价 $0.24 | OI 2344→33368 (ΔOI +31024张) | ΔOI/Volume 74.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31024张（+1323.5% vs前日OI），连续性待观察（方向未知）
10-05 150.0P — Vol 29,345 | 最新价 $0.01 | OI 5→28426 (ΔOI +28421张) | ΔOI/Volume 96.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增28421张（+568420.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 186,844 张（Put 64,635 / Call 122,209），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 111.2k / P 173.3k，今日成交量: C 251.4k / P 155.7k，平值价格ATM: C $0.69 / P $1.05 ｜ ATM IV 33.4%，预期波动 ±0.7%，Max Pain 232
Top ΔOI: P 150 +28,421 ｜ P 145 +25,038 ｜ C 240 +12,630

📆 Forward Expiration Structure

10-07  C +28.8k / P +17.8k ｜ Activity HIGH ｜ 2D
10-09  C +152.5k / P +118.9k ｜ Activity HIGH ｜ 4D
10-12  C +4.0k / P +4.0k ｜ Activity HIGH ｜ 7D
10-14  C +1.7k / P +1.6k ｜ Activity HIGH ｜ 9D

📆 10-07 Forward Structure
存量OI: C 59.5k / P 41.5k，今日变化ΔOI: C +28.8k / P +17.8k，平值价格ATM: C $2.11 / P $2.47 ｜ ATM IV 30.3%，净 delta 敞口 260k shares
Top ΔOI: C 250 +5,612 ｜ C 240 +5,039 ｜ C 242 +5,033
仓位参考: Max Pain 230 ｜ Call Wall 247.5（+4.4%，弱）（OI 9.9k） ｜ Put Wall 230（-3.0%）（OI 10.2k）
量化解读： 存量 Call 重｜ATM IV 30.3%｜历史 Rank 16%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 259,578 股

📆 10-09 Forward Structure
存量OI: C 342.2k / P 356.7k，今日变化ΔOI: C +152.5k / P +118.9k，平值价格ATM: C $3.03 / P $3.27 ｜ ATM IV 30.4%，净 delta 敞口 2.5M shares
Top ΔOI: C 240 +58,740 ｜ C 245 +32,445
仓位参考: Max Pain 230 ｜ Call Wall 240（+1.2%）（OI 78.3k） ｜ Put Wall 230（-3.0%，弱）（OI 26.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 30.4%｜历史 Rank 16%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,489,274 股

📆 10-12 Forward Structure
存量OI: C 13.3k / P 7.9k，今日变化ΔOI: C +4.0k / P +4.0k，平值价格ATM: C $3.45 / P $3.70 ｜ ATM IV 26.7%，净 delta 敞口 100k shares
Top ΔOI: C 240 +1,848 ｜ P 222 +1,257 ｜ P 220 +583
仓位参考: Max Pain 230 ｜ Call Wall 240（+1.2%）（OI 4.7k） ｜ Put Wall 222.5（-6.2%）（OI 1.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 26.7%｜历史 Rank 16%（近端代理）｜IV/RV 1.28×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 100,263 股

📆 10-14 Forward Structure
存量OI: C 6.0k / P 3.2k，今日变化ΔOI: C +1.7k / P +1.6k，平值价格ATM: C $4.15 / P $4.30 ｜ ATM IV 28.4%，净 delta 敞口 28k shares
Top ΔOI: P 215 +521 ｜ C 237 +420 ｜ C 250 +332
仓位参考: Max Pain 230 ｜ Call Wall 255（+7.5%，弱）（OI 1.0k） ｜ Put Wall 215（-9.3%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 28.4%｜历史 Rank 16%（近端代理）｜IV/RV 1.36×（近似）｜净 delta 敞口 正 28,204 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/NVDA_morning.json