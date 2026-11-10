# 期权晨报 2026-11-10（快照 10:20 ET）

📊 市场环境

SPY $751.28 ｜ QQQ $676.55
VIX 19.85 ↓0.3%（5D -4.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔵 **期限 OI 集中**: 11-16 450C ΔOI +4,921 占该期限总 OI 15.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 378.05 → 今开 370.54（-2.0%） | 较昨收变动（含盘初走势） ｜ 今日高 377.89 ｜ 低 370.43

Options: P/C成交量 0.60 | OI比 1.21 | ATM IV 52.0% | Skew 5.1pp | Term 0.67 | ExpMove ±2.5%（近端） | Rank 50%
量化视角： IV 中性（Rank 50%）｜期限结构倒挂（Term 0.67，近月 IV 高于远月）｜保护溢价中性（Skew 5.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.21×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-11（1D）±2.5% ｜ 11-13（3D）±3.9% ｜ 11-16（6D）±4.6% ｜ 11-18（8D）±5.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 57,979,682 | GEX Change vs 上次快照 -1,290,831 | Flip: Primary Flip: 363.29（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1444 / LOW 165 / INVALID 979
结构观察区: Primary Flip 363.29（全链重定价，覆盖 100%）
Call Wall 400（现价低于该位 5.7%）
最近结构参考: Flip 363（现价高于该位 3.8%）
量化视角： 正 Gamma（5798万，无历史分位）｜正 Gamma 减弱（129万）｜现价位于 Flip 上方 3.82%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 372（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 363（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-11 345.0P — Vol 12,023 | 最新价 $0.33 | OI 376→7666 (ΔOI +7290张) | ΔOI/Volume 60.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7290张（+1938.8% vs前日OI），连续性待观察（方向未知）
11-20 90.0P — Vol 5,651 | 最新价 $0.01 | OI 439→6083 (ΔOI +5644张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5644张（+1285.7% vs前日OI），连续性待观察（方向未知）
11-13 400.0C — Vol 15,024 | 最新价 $1.33 | OI 6221→11714 (ΔOI +5493张) | ΔOI/Volume 36.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5493张（+88.3% vs前日OI），连续性待观察（方向未知）
11-13 305.0P — Vol 5,979 | 最新价 $0.15 | OI 1091→6476 (ΔOI +5385张) | ΔOI/Volume 90.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5385张（+493.6% vs前日OI），连续性待观察（方向未知）
11-20 100.0P — Vol 5,053 | 最新价 $0.01 | OI 6100→11060 (ΔOI +4960张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4960张（+81.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 28,772 张（Put 23,279 / Call 5,493），跨 3 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-11  C +15.6k / P +29.9k ｜ Activity HIGH ｜ 1D
11-13  C +28.8k / P +35.5k ｜ Activity HIGH ｜ 3D
11-16  C +9.3k / P +4.2k ｜ Activity HIGH ｜ 6D
11-18  C +1.2k / P +1.6k ｜ Activity HIGH ｜ 8D

📆 11-11 Forward Structure
存量OI: C 45.9k / P 55.7k，今日变化ΔOI: C +15.6k / P +29.9k，平值价格ATM: C $4.34 / P $4.95 ｜ ATM IV 51.9%，净 delta 敞口 -146k shares
Top ΔOI: P 345 +7,290 ｜ C 400 +2,228 ｜ P 350 +1,684
仓位参考: Max Pain 372 ｜ Call Wall 400（+6.1%，弱）（OI 4.1k） ｜ Put Wall 345（-8.5%）（OI 7.7k）
量化解读： 存量 Put 重｜ATM IV 51.9%｜历史 Rank 50%（近端代理）｜IV/RV 0.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 146,085 股

📆 11-13 Forward Structure
存量OI: C 152.8k / P 223.3k，今日变化ΔOI: C +28.8k / P +35.5k，平值价格ATM: C $7.10 / P $7.50 ｜ ATM IV 51.3%，净 delta 敞口 21k shares
Top ΔOI: C 400 +5,493 ｜ P 305 +5,385
仓位参考: Max Pain 362 ｜ Call Wall 400（+6.1%，弱）（OI 11.7k）
量化解读： 存量 Put 重｜ATM IV 51.3%｜历史 Rank 50%（近端代理）｜IV/RV 0.88×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 21,255 股

📆 11-16 Forward Structure
存量OI: C 21.2k / P 10.3k，今日变化ΔOI: C +9.3k / P +4.2k，平值价格ATM: C $8.40 / P $9.08 ｜ ATM IV 43.1%，净 delta 敞口 852 shares
Top ΔOI: C 450 +4,921 ｜ P 337 +595
仓位参考: Max Pain 370 ｜ Call Wall 400（+6.1%，弱）（OI 1.2k） ｜ Put Wall 380（+0.7%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 43.1%｜历史 Rank 50%（近端代理）｜IV/RV 0.74×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 852 股

📆 11-18 Forward Structure
存量OI: C 5.8k / P 5.1k，今日变化ΔOI: C +1.2k / P +1.6k，平值价格ATM: C $11.00 / P $10.50 ｜ ATM IV 46.3%，净 delta 敞口 -38k shares
Top ΔOI: C 400 +198 ｜ C 410 +195 ｜ P 360 +130
仓位参考: Max Pain 368 ｜ Call Wall 400（+6.1%，弱）（OI 0.4k） ｜ Put Wall 350（-7.2%，弱）（OI 0.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 46.3%｜历史 Rank 50%（近端代理）｜IV/RV 0.80×（近似）｜净 delta 敞口 负 37,559 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/TSLA_morning.json