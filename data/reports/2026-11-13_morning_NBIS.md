# 期权晨报 2026-11-13（快照 10:20 ET）

📊 市场环境

SPY $750.54 ｜ QQQ $673.76
VIX 19.65 ↑5.1%（5D -23.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **事件差分**: 11-20 ATM IV 121.2% vs 11-27 108.8%（差 +12.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🔵 **期限 OI 集中**: 12-04 130C ΔOI +1,797 占该期限总 OI 11.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 128.64 → 今开 123.52（-4.0%） | 较昨收变动（含盘初走势） ｜ 今日高 123.97 ｜ 低 109.52

Options: P/C成交量 0.80 | OI比 0.47 | ATM IV 199.3% | Skew 11.1pp | Term 0.53 | ExpMove ±14.2%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.53，近月 IV 高于远月）｜保护溢价显著（Skew 11.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.47）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.47×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±14.2% ｜ 11-27（14D）±17.3% ｜ 12-04（21D）±20.7% ｜ 12-11（28D）±23.2%
   ⇒ IV–VIX Spread: +179.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -11,321,557 | GEX Change vs 上次快照 2,569,876 | Flip: Primary Flip: 124.64（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 621 / LOW 116 / INVALID 163
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 124.64（全链重定价，覆盖 99%）
最近结构参考: Flip 125（现价低于该位 9.3%）
量化视角： 负 Gamma（1132万，无历史分位）｜负 Gamma 缓解（+257万）｜现价位于 Flip 下方 9.32%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 135（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 125（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 55.0P — Vol 4,400 | 最新价 $0.04 | OI 3116→6971 (ΔOI +3855张) | ΔOI/Volume 87.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3855张（+123.7% vs前日OI），连续性待观察（方向未知）
11-20 125.0C — Vol 4,836 | 最新价 $9.65 | OI 712→3458 (ΔOI +2746张) | ΔOI/Volume 56.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2746张（+385.7% vs前日OI），连续性待观察（方向未知）
11-13 130.0C — Vol 17,539 | 最新价 $3.30 | OI 395→2850 (ΔOI +2455张) | ΔOI/Volume 14.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2455张（+621.5% vs前日OI），连续性待观察（方向未知）
11-13 140.0C — Vol 24,261 | 最新价 $0.79 | OI 5488→7634 (ΔOI +2146张) | ΔOI/Volume 8.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2146张（+39.1% vs前日OI），连续性待观察（方向未知）
12-04 130.0C — Vol 3,944 | 最新价 $11.91 | OI 42→1839 (ΔOI +1797张) | ΔOI/Volume 45.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1797张（+4278.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,999 张（Put 3,855 / Call 9,144），跨 3 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 134.8k / P 63.5k，今日成交量: C 46.7k / P 37.2k，平值价格ATM: C $2.77 / P $2.16 ｜ ATM IV 199.3%，预期波动 ±4.4%，Max Pain 135
Top ΔOI: C 130 +2,455 ｜ C 140 +2,146 ｜ C 192 +1,793

📆 Forward Expiration Structure

11-20  C +12.0k / P -0.9k ｜ Activity HIGH ｜ 7D
11-27  C +5.6k / P -1.0k ｜ Activity HIGH ｜ 14D
12-04  C +3.9k / P +1.0k ｜ Activity HIGH ｜ 21D
12-11  C +1.0k / P +1.2k ｜ Activity HIGH ｜ 28D

📆 11-20 Forward Structure
存量OI: C 145.3k / P 113.4k，今日变化ΔOI: C +12.0k / P -0.9k，平值价格ATM: C $7.25 / P $8.80 ｜ ATM IV 121.2%，净 delta 敞口 770k shares
Top ΔOI: C 125 +2,746 ｜ P 230 -2,432
仓位参考: Max Pain 160 ｜ Put Wall 115（+1.8%，弱）（OI 9.1k）
量化解读： 存量 Call 重｜ATM IV 121.2%｜历史 Rank 98%（近端代理）｜IV/RV 0.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 770,096 股

📆 11-27 Forward Structure
存量OI: C 23.1k / P 18.6k，今日变化ΔOI: C +5.6k / P -1.0k，平值价格ATM: C $9.00 / P $10.60 ｜ ATM IV 108.8%，净 delta 敞口 207k shares
Top ΔOI: P 230 -1,308 ｜ C 150 +800 ｜ P 80 -757
仓位参考: Max Pain 160 ｜ Put Wall 115（+1.8%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 108.8%｜历史 Rank 98%（近端代理）｜IV/RV 0.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 207,086 股

📆 12-04 Forward Structure
存量OI: C 8.4k / P 7.6k，今日变化ΔOI: C +3.9k / P +1.0k，平值价格ATM: C $10.76 / P $12.60 ｜ ATM IV 105.8%，净 delta 敞口 99k shares
Top ΔOI: C 130 +1,797 ｜ P 80 +1,286 ｜ P 100 -731
仓位参考: Max Pain 130 ｜ Call Wall 120（+6.2%，弱）（OI 0.6k） ｜ Put Wall 115（+1.8%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜ATM IV 105.8%｜历史 Rank 98%（近端代理）｜IV/RV 0.75×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 99,321 股

📆 12-11 Forward Structure
存量OI: C 3.8k / P 5.4k，今日变化ΔOI: C +1.0k / P +1.2k，平值价格ATM: C $12.30 / P $13.98 ｜ ATM IV 105.4%，净 delta 敞口 -18k shares
Top ΔOI: C 130 +429 ｜ P 130 +304
仓位参考: Max Pain 145 ｜ Call Wall 120（+6.2%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜ATM IV 105.4%｜历史 Rank 98%（近端代理）｜IV/RV 0.75×（近似）｜净 delta 敞口 负 18,028 股

📅 事件差分（观察，非因果）: 11-20（7D）ATM IV 121.2% vs 11-27 108.8%（差 +12.4pp）——覆盖 PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/NBIS_morning.json