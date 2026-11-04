# 期权晨报 2026-11-04（快照 10:20 ET）

📊 市场环境

SPY $767.05 ｜ QQQ $696.66
VIX 17.01 ↓18.3%（5D +0.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-04

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 54.5 ｜ 前值 54.9　✅ 今日已公布
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-05 670P ΔOI +9,854（距现价 -4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-10 710C ΔOI +7,094 占该期限总 OI 14.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 685.28 → 今开 688.44（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 701.45 ｜ 低 687.90

Options: P/C成交量 0.68 | OI比 1.89 | ATM IV 36.8% | Skew 5.0pp | Term 0.62 | ExpMove ±1.4%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.62，近月 IV 高于远月）｜保护溢价中性（Skew 5.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.68×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.89×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 22% ｜ P/C OI(近端) 70%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 22%）｜近端持仓结构中性（P/C OI 分位 70%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-05（1D）±1.4% ｜ 11-06（2D）±1.9% ｜ 11-09（5D）±2.3% ｜ 11-10（6D）±2.6%
   ⇒ IV–VIX Spread: +19.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -448,816,304 | GEX Change vs 上次快照 276,518,067 | Flip: Primary Flip: 711.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 2972 / LOW 173 / INVALID 1425
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 711.41（全链重定价，覆盖 99%）
Put Wall 680（弱结构｜现价高于该位 2.7%）
最近结构参考: Flip 711（现价低于该位 1.8%）
量化视角： 负 Gamma（4.49亿，历史分位偏负区，比 78% 的交易日更负）｜负 Gamma 缓解（+2.77亿）｜现价位于 Flip 下方 1.80%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 680（Put Wall，弱结构） / 692（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 711（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 668.0P — Vol 11,967 | 最新价 $4.25 | OI 0→11661 (ΔOI +11661张) | ΔOI/Volume 97.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11661张（前日OI缺失），连续性待观察（方向未知）
11-05 670.0P — Vol 12,631 | 最新价 $3.59 | OI 1414→11268 (ΔOI +9854张) | ΔOI/Volume 78.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9854张（+696.9% vs前日OI），连续性待观察（方向未知）
11-06 475.0P — Vol 10,478 | 最新价 $0.02 | OI 3197→13031 (ΔOI +9834张) | ΔOI/Volume 93.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9834张（+307.6% vs前日OI），连续性待观察（方向未知）
11-20 705.0C — Vol 9,778 | 最新价 $9.42 | OI 7251→15083 (ΔOI +7832张) | ΔOI/Volume 80.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7832张（+108.0% vs前日OI），连续性待观察（方向未知）
11-20 715.0C — Vol 14,355 | 最新价 $6.03 | OI 21889→29441 (ΔOI +7552张) | ΔOI/Volume 52.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7552张（+34.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 46,733 张（Put 31,349 / Call 15,384），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $8M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 135.9k / P 257.2k，今日成交量: C 628.9k / P 430.3k，平值价格ATM: C $2.70 / P $2.84 ｜ ATM IV 36.8%，预期波动 ±0.8%，Max Pain 692
Top ΔOI: P 670 +6,855 ｜ P 660 +6,797 ｜ P 545 +6,177

📆 Forward Expiration Structure

11-05  C +17.4k / P +32.2k ｜ Activity HIGH ｜ 1D
11-06  C +36.8k / P +72.0k ｜ Activity HIGH ｜ 2D
11-09  C +5.1k / P +14.4k ｜ Activity HIGH ｜ 5D
11-10  C +17.4k / P +6.9k ｜ Activity HIGH ｜ 6D

📆 11-05 Forward Structure
存量OI: C 55.9k / P 60.4k，今日变化ΔOI: C +17.4k / P +32.2k，平值价格ATM: C $4.76 / P $4.92 ｜ ATM IV 29.6%，净 delta 敞口 530k shares
Top ΔOI: P 670 +9,854 ｜ P 680 +1,760
仓位参考: Max Pain 693 ｜ Call Wall 710（+1.6%，弱）（OI 4.7k） ｜ Put Wall 680（-2.7%，弱）（OI 3.0k）
量化解读： 存量两侧均衡｜ATM IV 29.6%｜历史 Rank 95%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 530,243 股

📆 11-06 Forward Structure
存量OI: C 414.8k / P 603.4k，今日变化ΔOI: C +36.8k / P +72.0k，平值价格ATM: C $6.63 / P $6.36 ｜ ATM IV 30.0%，净 delta 敞口 785k shares
Top ΔOI: P 668 +11,661 ｜ P 672 +7,155
仓位参考: Max Pain 713 ｜ Call Wall 715（+2.4%，弱）（OI 22.9k） ｜ Put Wall 713（+2.1%，弱）（OI 53.6k）
量化解读： 存量 Put 重｜ATM IV 30.0%｜历史 Rank 95%（近端代理）｜IV/RV 1.35×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 784,512 股

📆 11-09 Forward Structure
存量OI: C 27.8k / P 43.0k，今日变化ΔOI: C +5.1k / P +14.4k，平值价格ATM: C $8.22 / P $8.12 ｜ ATM IV 23.6%，净 delta 敞口 68k shares
Top ΔOI: P 640 +4,558 ｜ P 685 +3,042 ｜ P 630 +2,864
仓位参考: Max Pain 700 ｜ Call Wall 715（+2.4%，弱）（OI 2.2k） ｜ Put Wall 685（-1.9%，弱）（OI 4.1k）
量化解读： 存量 Put 重｜ATM IV 23.6%｜历史 Rank 95%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 正 68,285 股

📆 11-10 Forward Structure
存量OI: C 34.4k / P 15.0k，今日变化ΔOI: C +17.4k / P +6.9k，平值价格ATM: C $8.90 / P $9.18 ｜ ATM IV 24.7%，净 delta 敞口 374k shares
Top ΔOI: C 710 +7,094 ｜ C 720 +6,574 ｜ P 671 +1,310
仓位参考: Max Pain 691 ｜ Call Wall 710（+1.6%，弱）（OI 8.3k） ｜ Put Wall 686（-1.8%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 24.7%｜历史 Rank 95%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 正 374,257 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/QQQ_morning.json