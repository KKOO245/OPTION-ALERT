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
🟡 **近现价集中开仓**: 11-13 48C ΔOI +4,510（距现价 +2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-18 49C ΔOI +1,851 占该期限总 OI 17.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 46.48 → 今开 47.40（+2.0%） | 较昨收变动（含盘初走势） ｜ 今日高 47.41 ｜ 低 47.08

Options: P/C成交量 0.88 | OI比 0.63 | ATM IV 40.5% | Skew 5.0pp | Term 0.96 | ExpMove ±2.7%（近端） | Rank 66%
量化视角： IV 中性（Rank 66%）｜期限结构正常（Term 0.96）｜保护溢价中性（Skew 5.0pp）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.88×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±2.7% ｜ 11-16（5D）±3.4% ｜ 11-18（7D）±4.3% ｜ 11-20（9D）±5.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 62,338,572 | GEX Change vs 上次快照 41,638,811 | Flip: Primary Flip: 45.75（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 695 / LOW 166 / INVALID 439
结构观察区: Primary Flip 45.75（全链重定价，覆盖 96%）
最近结构参考: Flip 46（现价高于该位 3.0%）
量化视角： 正 Gamma（6234万，无历史分位）｜正 Gamma 增强（+4164万）｜现价位于 Flip 上方 2.98%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 46（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 46（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-11 54.0C — Vol 5,285 | 最新价 $0.34 | OI 401→5605 (ΔOI +5204张) | ΔOI/Volume 98.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5204张（+1297.8% vs前日OI），连续性待观察（方向未知）
12-11 52.0C — Vol 5,273 | 最新价 $0.60 | OI 597→5702 (ΔOI +5105张) | ΔOI/Volume 96.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5105张（+855.1% vs前日OI），连续性待观察（方向未知）
11-13 48.5C — Vol 5,287 | 最新价 $0.18 | OI 1453→5963 (ΔOI +4510张) | ΔOI/Volume 85.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4510张（+310.4% vs前日OI），连续性待观察（方向未知）
12-04 47.0C — Vol 3,091 | 最新价 $1.72 | OI 290→2824 (ΔOI +2534张) | ΔOI/Volume 82.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2534张（+873.8% vs前日OI），连续性待观察（方向未知）
11-18 49.0C — Vol 1,994 | 最新价 $0.33 | OI 119→1970 (ΔOI +1851张) | ΔOI/Volume 92.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1851张（+1555.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 19,204 张（Put 0 / Call 19,204），跨 4 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 35.4k / P 22.2k，今日成交量: C 4.7k / P 4.1k，平值价格ATM: C $0.29 / P $0.14 ｜ ATM IV 40.5%，预期波动 ±0.9%，Max Pain 46
Top ΔOI: C 46 +1,016 ｜ C 47 +790 ｜ C 49 +598

📆 Forward Expiration Structure

11-13  C +13.1k / P +2.9k ｜ Activity HIGH ｜ 2D
11-16  C +2.0k / P +1.3k ｜ Activity HIGH ｜ 5D
11-18  C +2.4k / P +2.8k ｜ Activity HIGH ｜ 7D
11-20  C -9.5k / P +0.3k ｜ Activity MEDIUM △ ｜ 9D

📆 11-13 Forward Structure
存量OI: C 82.4k / P 38.4k，今日变化ΔOI: C +13.1k / P +2.9k，平值价格ATM: C $0.71 / P $0.57 ｜ ATM IV 42.0%，净 delta 敞口 221k shares
Top ΔOI: C 48 +4,510 ｜ C 49 +1,274 ｜ C 51 +1,175
仓位参考: Max Pain 48 ｜ Call Wall 50（+6.1%）（OI 9.7k） ｜ Put Wall 45（-4.5%，弱）（OI 4.2k）
量化解读： 存量 Call 重｜ATM IV 42.0%｜历史 Rank 66%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 220,732 股

📆 11-16 Forward Structure
存量OI: C 10.1k / P 4.1k，今日变化ΔOI: C +2.0k / P +1.3k，平值价格ATM: C $0.86 / P $0.72 ｜ ATM IV 34.7%，净 delta 敞口 49k shares
Top ΔOI: C 49 +351
仓位参考: Max Pain 47 ｜ Call Wall 50（+6.1%）（OI 2.1k） ｜ Put Wall 45.5（-3.4%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 34.7%｜历史 Rank 66%（近端代理）｜IV/RV 0.83×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 49,419 股

📆 11-18 Forward Structure
存量OI: C 4.6k / P 6.2k，今日变化ΔOI: C +2.4k / P +2.8k，平值价格ATM: C $1.09 / P $0.94 ｜ ATM IV 37.7%，净 delta 敞口 40k shares
Top ΔOI: C 49 +1,851 ｜ P 44 -793
仓位参考: Max Pain 46 ｜ Call Wall 49（+4.0%）（OI 2.0k） ｜ Put Wall 44.5（-5.6%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜ATM IV 37.7%｜历史 Rank 66%（近端代理）｜IV/RV 0.90×（近似）｜净 delta 敞口 正 40,036 股

11-20（MEDIUM △）Top ΔOI: 48C -1,914 ｜ 47C +1,815
11-20（MEDIUM △）仓位参考: Max Pain 50 ｜ Call Wall 50（+6.1%，弱）（OI 20.6k） ｜ Put Wall 50（+6.1%，弱）（OI 12.5k）

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 42.0% vs 11-16 34.7%（差 +7.3pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/SLV_morning.json