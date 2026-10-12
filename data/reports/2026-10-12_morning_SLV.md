# 期权晨报 2026-10-12（快照 10:20 ET）

📊 市场环境

SPY $777.96 ｜ QQQ $746.04
VIX 15.29 ↑3.0%（5D -1.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.96 ｜ 实际 待公布 ｜ 前值 3.98
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.7 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 10-14 57C ΔOI +773（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 54.78 → 今开 54.72（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 54.74 ｜ 低 54.38

Options: P/C成交量 0.57 | OI比 0.85 | ATM IV 31.3% | Skew 2.7pp | Term 1.06 | ExpMove ±2.2%（近端） | Rank 44%
量化视角： IV 中性（Rank 44%）｜期限结构正常（Term 1.06）｜保护溢价中性（Skew 2.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-14（2D）±2.2% ｜ 10-16（4D）±3.0% ｜ 10-19（7D）±3.4% ｜ 10-21（9D）±3.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 69,585,304 | GEX Change vs 上次快照 39,380,571 | Flip: Primary Flip: 52.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 725 / LOW 196 / INVALID 403
结构观察区: Primary Flip 52.67（全链重定价，覆盖 98%）
Put Wall 50（弱结构｜现价高于该位 9.4%）
最近结构参考: Flip 53（现价高于该位 3.8%）
量化视角： 正 Gamma（6959万，无历史分位）｜正 Gamma 增强（+3938万）｜现价位于 Flip 上方 3.85%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构） / 54（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 53（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 60.5C — Vol 3,438 | 最新价 $0.33 | OI 5707→8285 (ΔOI +2578张) | ΔOI/Volume 75.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2578张（+45.2% vs前日OI），连续性待观察（方向未知）
10-30 48.0P — Vol 2,019 | 最新价 $0.13 | OI 230→2152 (ΔOI +1922张) | ΔOI/Volume 95.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1922张（+835.6% vs前日OI），连续性待观察（方向未知）
10-16 57.0C — Vol 4,637 | 最新价 $0.26 | OI 7408→9228 (ΔOI +1820张) | ΔOI/Volume 39.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1820张（+24.6% vs前日OI），连续性待观察（方向未知）
10-30 49.0P — Vol 2,405 | 最新价 $0.16 | OI 1196→2442 (ΔOI +1246张) | ΔOI/Volume 51.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1246张（+104.2% vs前日OI），连续性待观察（方向未知）
10-16 55.0C — Vol 4,067 | 最新价 $0.84 | OI 21690→22807 (ΔOI +1117张) | ΔOI/Volume 27.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1117张（+5.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,683 张（Put 3,168 / Call 5,515），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 15.9k / P 13.5k，今日成交量: C 3.5k / P 2.0k，平值价格ATM: C $0.29 / P $0.11 ｜ ATM IV 31.3%，预期波动 ±0.7%，Max Pain 54
Top ΔOI: C 55 +965 ｜ P 52 +881 ｜ C 54 -793

📆 Forward Expiration Structure

10-14  C +3.8k / P +1.2k ｜ Activity HIGH ｜ 2D
10-16  C -4.3k / P +1.3k ｜ Activity HIGH ｜ 4D
10-19  C +0.5k / P +0.6k ｜ Activity HIGH ｜ 7D
10-21  C +0.8k / P +0.5k ｜ Activity HIGH ｜ 9D

📆 10-14 Forward Structure
存量OI: C 11.8k / P 8.5k，今日变化ΔOI: C +3.8k / P +1.2k，平值价格ATM: C $0.69 / P $0.52 ｜ ATM IV 35.7%，净 delta 敞口 43k shares
Top ΔOI: C 57 +773 ｜ C 58 +498 ｜ C 56 +430
仓位参考: Max Pain 55 ｜ Call Wall 57（+4.2%，弱）（OI 1.2k） ｜ Put Wall 53.5（-2.2%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 35.7%｜历史 Rank 44%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 43,368 股

📆 10-16 Forward Structure
存量OI: C 474.2k / P 195.0k，今日变化ΔOI: C -4.3k / P +1.3k，平值价格ATM: C $0.94 / P $0.72 ｜ ATM IV 34.3%，净 delta 敞口 12k shares
Top ΔOI: C 57 +1,820 ｜ C 55 +1,117
仓位参考: Max Pain 56 ｜ Call Wall 60（+9.7%，弱）（OI 55.8k） ｜ Put Wall 60（+9.7%，弱）（OI 31.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 34.3%｜历史 Rank 44%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 12,416 股

📆 10-19 Forward Structure
存量OI: C 2.5k / P 1.6k，今日变化ΔOI: C +0.5k / P +0.6k，平值价格ATM: C $1.01 / P $0.83 ｜ ATM IV 29.1%，净 delta 敞口 -7k shares
Top ΔOI: P 55 +171 ｜ P 54 +147 ｜ C 56 +121
仓位参考: Max Pain 54 ｜ Call Wall 56（+2.4%，弱）（OI 0.3k） ｜ Put Wall 55.5（+1.5%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 29.1%｜历史 Rank 44%（近端代理）｜IV/RV 0.91×（近似）｜净 delta 敞口 负 6,611 股

📆 10-21 Forward Structure
存量OI: C 2.2k / P 0.9k，今日变化ΔOI: C +0.8k / P +0.5k，平值价格ATM: C $1.19 / P $0.96 ｜ ATM IV 30.3%，净 delta 敞口 3k shares
Top ΔOI: C 59 +196 ｜ C 60 +100
仓位参考: Max Pain 54 ｜ Call Wall 53.5（-2.2%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 30.3%｜历史 Rank 44%（近端代理）｜IV/RV 0.95×（近似）｜净 delta 敞口 正 2,545 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/SLV_morning.json