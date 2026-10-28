# 期权晨报 2026-10-28（快照 10:20 ET）

📊 市场环境

SPY $770.58 ｜ QQQ $721.83
VIX 17.36 ↓0.9%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　⏰ 今日
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4　⏰ 今日
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　⏰ 今日
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 730C ΔOI +8,261（距现价 +1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 721.25 → 今开 724.12（+0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 724.73 ｜ 低 720.30

Options: P/C成交量 1.23 | OI比 1.92 | ATM IV 42.0% | Skew 5.0pp | Term 0.51 | ExpMove ±1.5%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.51，近月 IV 高于远月）｜保护溢价中性（Skew 5.0pp）｜当日成交偏 Put（P/C量 1.23）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.23×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.92×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 30% ｜ P/C OI(近端) 71%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 30%）｜近端持仓结构中性（P/C OI 分位 71%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-29（1D）±1.5% ｜ 10-30（2D）±1.8% ｜ 11-02（5D）±2.1% ｜ 11-03（6D）±2.3%
   ⇒ IV–VIX Spread: +24.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -309,371,384 | GEX Change vs 上次快照 -32,094,126 | Flip: Primary Flip: 728.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 2857 / LOW 231 / INVALID 1208
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 728.02（全链重定价，覆盖 99%）
最近结构参考: Flip 728（现价低于该位 0.8%）
量化视角： 负 Gamma（3.09亿，历史分位 30%，中性区）｜负 Gamma 加深（3209万）｜现价位于 Flip 下方 0.82%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 719（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 728（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 730.0C — Vol 15,625 | 最新价 $2.99 | OI 13989→22250 (ΔOI +8261张) | ΔOI/Volume 52.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8261张（+59.0% vs前日OI），连续性待观察（方向未知）
10-29 535.0P — Vol 8,280 | 最新价 $0.01 | OI 2924→10390 (ΔOI +7466张) | ΔOI/Volume 90.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7466张（+255.3% vs前日OI），连续性待观察（方向未知）
10-30 740.0C — Vol 19,035 | 最新价 $0.72 | OI 21379→28745 (ΔOI +7366张) | ΔOI/Volume 38.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7366张（+34.5% vs前日OI），连续性待观察（方向未知）
10-28 671.0P — Vol 7,473 | 最新价 $0.02 | OI 0→7316 (ΔOI +7316张) | ΔOI/Volume 97.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7316张（前日OI缺失），连续性待观察（方向未知）
10-28 670.0P — Vol 8,256 | 最新价 $0.04 | OI 1911→9129 (ΔOI +7218张) | ΔOI/Volume 87.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7218张（+377.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 37,627 张（Put 22,000 / Call 15,627），跨 3 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 110.8k / P 213.0k，今日成交量: C 247.5k / P 303.4k，平值价格ATM: C $3.65 / P $2.93 ｜ ATM IV 42.0%，预期波动 ±0.9%，Max Pain 719
Top ΔOI: P 671 +7,316 ｜ P 670 +7,218 ｜ P 676 +5,874

📆 Forward Expiration Structure

10-29  C +11.7k / P +46.3k ｜ Activity HIGH ｜ 1D
10-30  C +25.1k / P +40.2k ｜ Activity MEDIUM △ ｜ 2D
11-02  C -19.2k / P +3.8k ｜ Activity HIGH ｜ 5D
11-03  C +3.6k / P +7.0k ｜ Activity HIGH ｜ 6D

📆 10-29 Forward Structure
存量OI: C 53.7k / P 118.5k，今日变化ΔOI: C +11.7k / P +46.3k，平值价格ATM: C $5.66 / P $4.86 ｜ ATM IV 30.9%，净 delta 敞口 -122k shares
仓位参考: Max Pain 719 ｜ Call Wall 725（+0.4%）（OI 4.1k） ｜ Put Wall 718（-0.6%，弱）（OI 2.9k）
量化解读： 存量 Put 重｜ATM IV 30.9%｜历史 Rank 98%（近端代理）｜IV/RV 1.68×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 122,179 股

10-30（MEDIUM △）Top ΔOI: 730C +8,261 ｜ 740C +7,366
10-30（MEDIUM △）仓位参考: Max Pain 723 ｜ Call Wall 740（+2.5%，弱）（OI 28.7k） ｜ Put Wall 710（-1.7%，弱）（OI 26.0k）

📆 11-02 Forward Structure
存量OI: C 41.5k / P 50.5k，今日变化ΔOI: C -19.2k / P +3.8k，平值价格ATM: C $8.10 / P $7.26 ｜ ATM IV 21.7%，净 delta 敞口 -791k shares
Top ΔOI: C 720 -7,291 ｜ C 740 -7,250 ｜ C 730 -6,584
仓位参考: Max Pain 715 ｜ Call Wall 740（+2.5%，弱）（OI 8.4k） ｜ Put Wall 710（-1.7%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 21.7%｜历史 Rank 98%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 负 791,145 股

📆 11-03 Forward Structure
存量OI: C 20.5k / P 37.6k，今日变化ΔOI: C +3.6k / P +7.0k，平值价格ATM: C $8.83 / P $7.88 ｜ ATM IV 22.2%，净 delta 敞口 -21k shares
Top ΔOI: P 650 +1,156 ｜ P 685 +457
仓位参考: Max Pain 712 ｜ Call Wall 710（-1.7%）（OI 2.6k）
量化解读： 存量 Put 重｜ATM IV 22.2%｜历史 Rank 98%（近端代理）｜IV/RV 1.21×（近似）｜净 delta 敞口 负 20,769 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/QQQ_morning.json