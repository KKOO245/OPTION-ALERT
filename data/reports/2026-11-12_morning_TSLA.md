# 期权晨报 2026-11-12（快照 10:20 ET）

📊 市场环境

SPY $756.94 ｜ QQQ $685.64
VIX 18.45 ↑5.5%（5D -34.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **事件差分**: 11-13 ATM IV 51.0% vs 11-16 38.7%（差 +12.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-13 400C ΔOI +6,064（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-18 392P ΔOI +2,202 占该期限总 OI 10.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 390.84 → 今开 385.85（-1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 396.20 ｜ 低 385.20

Options: P/C成交量 0.42 | OI比 1.38 | ATM IV 51.0% | Skew 3.5pp | Term 0.70 | ExpMove ±2.4%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价中性（Skew 3.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.38×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±2.4% ｜ 11-16（4D）±3.4% ｜ 11-18（6D）±4.5% ｜ 11-20（8D）±5.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 100,147,279 | GEX Change vs 上次快照 3,912,416 | Flip: Primary Flip: 371.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1422 / LOW 190 / INVALID 1034
结构观察区: Primary Flip 371.87（全链重定价，覆盖 97%）
Call Wall 400（现价低于该位 2.2%）
最近结构参考: Call Wall 400（现价低于该位 2.2%）
量化视角： 正 Gamma（1.00亿，无历史分位）｜正 Gamma 增强（+391万）｜现价位于 Flip 上方 5.24%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 368（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 372（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 250.0P — Vol 10,881 | 最新价 $0.09 | OI 48293→57919 (ΔOI +9626张) | ΔOI/Volume 88.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9626张（+19.9% vs前日OI），连续性待观察（方向未知）
11-13 400.0C — Vol 35,339 | 最新价 $1.94 | OI 13604→19668 (ΔOI +6064张) | ΔOI/Volume 17.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6064张（+44.6% vs前日OI），连续性待观察（方向未知）
11-13 392.5C — Vol 18,334 | 最新价 $4.58 | OI 1586→7163 (ΔOI +5577张) | ΔOI/Volume 30.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5577张（+351.6% vs前日OI），连续性待观察（方向未知）
11-13 410.0C — Vol 10,799 | 最新价 $0.50 | OI 4367→7303 (ΔOI +2936张) | ΔOI/Volume 27.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2936张（+67.2% vs前日OI），连续性待观察（方向未知）
11-13 370.0P — Vol 10,662 | 最新价 $0.61 | OI 2829→5464 (ΔOI +2635张) | ΔOI/Volume 24.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2635张（+93.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 26,838 张（Put 12,261 / Call 14,577），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +21.5k / P +20.9k ｜ Activity HIGH ｜ 1D
11-16  C +8.0k / P +7.4k ｜ Activity HIGH ｜ 4D
11-18  C +2.5k / P +4.7k ｜ Activity HIGH ｜ 6D
11-20  C +2.4k / P +18.7k ｜ Activity MEDIUM △ ｜ 8D

📆 11-13 Forward Structure
存量OI: C 183.5k / P 254.0k，今日变化ΔOI: C +21.5k / P +20.9k，平值价格ATM: C $4.45 / P $5.05 ｜ ATM IV 51.0%，净 delta 敞口 -165k shares
Top ΔOI: C 400 +6,064 ｜ C 392 +5,577 ｜ C 410 +2,936
仓位参考: Max Pain 368 ｜ Call Wall 400（+2.2%）（OI 19.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 51.0%｜历史 Rank 48%（近端代理）｜IV/RV 0.88×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 165,395 股

📆 11-16 Forward Structure
存量OI: C 31.3k / P 20.6k，今日变化ΔOI: C +8.0k / P +7.4k，平值价格ATM: C $6.25 / P $7.00 ｜ ATM IV 38.7%，净 delta 敞口 30k shares
Top ΔOI: P 360 +1,510
仓位参考: Max Pain 378 ｜ Call Wall 400（+2.2%，弱）（OI 2.0k） ｜ Put Wall 360（-8.0%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 38.7%｜历史 Rank 48%（近端代理）｜IV/RV 0.67×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 30,256 股

📆 11-18 Forward Structure
存量OI: C 10.1k / P 11.9k，今日变化ΔOI: C +2.5k / P +4.7k，平值价格ATM: C $8.45 / P $9.00 ｜ ATM IV 43.2%，净 delta 敞口 -120k shares
Top ΔOI: P 392 +2,202 ｜ P 387 +543 ｜ C 430 +266
仓位参考: Max Pain 390 ｜ Call Wall 410（+4.8%，弱）（OI 0.9k） ｜ Put Wall 392.5（+0.3%）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 43.2%｜历史 Rank 48%（近端代理）｜IV/RV 0.75×（近似）｜净 delta 敞口 负 119,591 股

11-20（MEDIUM △）Top ΔOI: 250P +9,626 ｜ 372P -2,570
11-20（MEDIUM △）仓位参考: Max Pain 375 ｜ Call Wall 400（+2.2%，弱）（OI 21.8k）

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 51.0% vs 11-16 38.7%（差 +12.4pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/TSLA_morning.json