# 期权晨报 2026-11-03（快照 10:20 ET）

📊 市场环境

SPY $755.34 ｜ QQQ $685.28
VIX 21.03 ↓0.6%（5D +20.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-03

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.1 ｜ 实际 7.523 ｜ 前值 7.19　✅ 今日已公布
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-05 720C ΔOI +3,419（距现价 +5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 681.09 → 今开 684.20（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 687.28 ｜ 低 683.18

Options: P/C成交量 0.79 | OI比 1.31 | ATM IV 38.7% | Skew 3.7pp | Term 0.69 | ExpMove ±2.0%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价中性（Skew 3.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.79×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.31×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 14% ｜ P/C OI(近端) 22%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 14%）｜近端持仓结构中性（P/C OI 分位 22%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-04（1D）±2.0% ｜ 11-05（2D）±2.5% ｜ 11-06（3D）±3.0% ｜ 11-09（6D）±3.3%
   ⇒ IV–VIX Spread: +17.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -678,539,666 | GEX Change vs 上次快照 83,016,867 | Flip: Primary Flip: 712.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 2394 / LOW 221 / INVALID 1889
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 712.45（全链重定价，覆盖 98%）
Put Wall 680（弱结构｜现价高于该位 0.8%）
最近结构参考: Put Wall 680（现价高于该位 0.8%）
量化视角： 负 Gamma（6.79亿，历史分位偏负区，比 86% 的交易日更负）｜负 Gamma 缓解（+8302万）｜现价位于 Flip 下方 3.79%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 680（Put Wall，弱结构）；上方 688（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 712（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 605.0P — Vol 24,502 | 最新价 $0.23 | OI 4251→26089 (ΔOI +21838张) | ΔOI/Volume 89.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21838张（+513.7% vs前日OI），连续性待观察（方向未知）
11-04 505.0P — Vol 20,878 | 最新价 $0.01 | OI 174→18997 (ΔOI +18823张) | ΔOI/Volume 90.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18823张（+10817.8% vs前日OI），连续性待观察（方向未知）
11-06 725.0C — Vol 20,135 | 最新价 $0.57 | OI 12116→25412 (ΔOI +13296张) | ΔOI/Volume 66.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13296张（+109.7% vs前日OI），连续性待观察（方向未知）
11-06 735.0C — Vol 12,661 | 最新价 $0.23 | OI 15406→25786 (ΔOI +10380张) | ΔOI/Volume 82.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10380张（+67.4% vs前日OI），连续性待观察（方向未知）
11-04 515.0P — Vol 11,114 | 最新价 $0.04 | OI 14→8998 (ΔOI +8984张) | ΔOI/Volume 80.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8984张（+64171.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 73,321 张（Put 49,645 / Call 23,676），跨 2 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 139.0k / P 182.7k，今日成交量: C 384.2k / P 302.9k，平值价格ATM: C $2.79 / P $2.93 ｜ ATM IV 38.7%，预期波动 ±0.8%，Max Pain 688
Top ΔOI: P 670 +6,477 ｜ C 690 +5,791 ｜ P 665 +5,153

📆 Forward Expiration Structure

11-04  C +29.9k / P +94.9k ｜ Activity HIGH ｜ 1D
11-05  C +12.0k / P +9.6k ｜ Activity HIGH ｜ 2D
11-06  C +84.4k / P +63.6k ｜ Activity HIGH ｜ 3D
11-09  C +7.3k / P +11.6k ｜ Activity HIGH ｜ 6D

📆 11-04 Forward Structure
存量OI: C 82.0k / P 173.2k，今日变化ΔOI: C +29.9k / P +94.9k，平值价格ATM: C $6.84 / P $6.87 ｜ ATM IV 42.5%，净 delta 敞口 -851k shares
仓位参考: Max Pain 695 ｜ Call Wall 700（+2.1%，弱）（OI 4.3k） ｜ Put Wall 685（-0.1%，弱）（OI 10.9k）
量化解读： 存量 Put 重｜ATM IV 42.5%｜历史 Rank 96%（近端代理）｜IV/RV 1.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 851,264 股

📆 11-05 Forward Structure
存量OI: C 38.5k / P 28.2k，今日变化ΔOI: C +12.0k / P +9.6k，平值价格ATM: C $8.73 / P $8.72 ｜ ATM IV 40.4%，净 delta 敞口 61k shares
Top ΔOI: C 720 +3,419 ｜ C 740 +1,377
仓位参考: Max Pain 700 ｜ Call Wall 700（+2.1%，弱）（OI 2.9k） ｜ Put Wall 685（-0.1%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 40.4%｜历史 Rank 96%（近端代理）｜IV/RV 1.85×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 60,950 股

📆 11-06 Forward Structure
存量OI: C 378.0k / P 531.4k，今日变化ΔOI: C +84.4k / P +63.6k，平值价格ATM: C $10.47 / P $10.20 ｜ ATM IV 39.8%，净 delta 敞口 575k shares
Top ΔOI: P 605 +21,838 ｜ C 725 +13,296 ｜ C 735 +10,380
仓位参考: Max Pain 713 ｜ Call Wall 700（+2.1%，弱）（OI 14.9k） ｜ Put Wall 675（-1.5%，弱）（OI 44.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 39.8%｜历史 Rank 96%（近端代理）｜IV/RV 1.82×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 575,405 股

📆 11-09 Forward Structure
存量OI: C 22.7k / P 28.6k，今日变化ΔOI: C +7.3k / P +11.6k，平值价格ATM: C $11.79 / P $11.06 ｜ ATM IV 32.2%，净 delta 敞口 -123k shares
Top ΔOI: P 680 +1,999 ｜ C 730 +1,571
仓位参考: Max Pain 705 ｜ Call Wall 705（+2.9%，弱）（OI 1.7k） ｜ Put Wall 675（-1.5%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜ATM IV 32.2%｜历史 Rank 96%（近端代理）｜IV/RV 1.47×（近似）｜净 delta 敞口 负 123,393 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/QQQ_morning.json