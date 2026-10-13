# 期权晨报 2026-10-13（快照 10:20 ET）

📊 市场环境

SPY $777.81 ｜ QQQ $743.57
VIX 15.31 ↑0.7%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.95 ｜ 实际 3.99 ｜ 前值 3.93　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-14 750C ΔOI +2,841（距现价 +0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 746.04 → 今开 739.53（-0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 744.20 ｜ 低 738.84

Options: P/C成交量 0.84 | OI比 2.15 | ATM IV 18.4% | Skew 2.2pp | Term 1.01 | ExpMove ±0.9%（近端） | Rank 51%
量化视角： IV 中性（Rank 51%）｜期限结构正常（Term 1.01）｜保护溢价中性（Skew 2.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.15×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 26% ｜ P/C OI(近端) 83%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 26%）｜近端持仓结构中性（P/C OI 分位 83%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-14（1D）±0.9% ｜ 10-15（2D）±1.2% ｜ 10-16（3D）±1.4% ｜ 10-19（6D）±1.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -375,106,337 | GEX Change vs 上次快照 -95,903,155 | Flip: Primary Flip: 747.58（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 3007 / LOW 305 / INVALID 1696
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 747.58（全链重定价，覆盖 99%）
Call Wall 760（弱结构｜现价低于该位 2.1%）
最近结构参考: Flip 748（现价低于该位 0.5%）
量化视角： 负 Gamma（3.75亿，历史分位 26%，中性区）｜负 Gamma 加深（9590万）｜现价位于 Flip 下方 0.51%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 748（MaxPain，仅结算参考） / 760（Call Wall，弱结构）。
• Gamma 区域：切换参考 748（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 655.0P — Vol 20,086 | 最新价 $0.05 | OI 9103→27322 (ΔOI +18219张) | ΔOI/Volume 90.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18219张（+200.1% vs前日OI），连续性待观察（方向未知）
10-30 770.0C — Vol 16,393 | 最新价 $2.77 | OI 9498→23859 (ΔOI +14361张) | ΔOI/Volume 87.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14361张（+151.2% vs前日OI），连续性待观察（方向未知）
10-13 750.0C — Vol 48,861 | 最新价 $0.57 | OI 1497→11334 (ΔOI +9837张) | ΔOI/Volume 20.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9837张（+657.1% vs前日OI），连续性待观察（方向未知）
10-13 748.0C — Vol 57,136 | 最新价 $1.12 | OI 427→7823 (ΔOI +7396张) | ΔOI/Volume 12.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7396张（+1732.1% vs前日OI），连续性待观察（方向未知）
10-30 640.0P — Vol 8,769 | 最新价 $0.33 | OI 37673→43925 (ΔOI +6252张) | ΔOI/Volume 71.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6252张（+16.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 56,065 张（Put 24,471 / Call 31,594），跨 3 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 102.2k / P 219.4k，今日成交量: C 491.6k / P 413.1k，平值价格ATM: C $1.44 / P $1.50 ｜ ATM IV 18.4%，预期波动 ±0.4%，Max Pain 748
Top ΔOI: C 750 +9,837 ｜ C 748 +7,396 ｜ P 585 +6,006

📆 Forward Expiration Structure

10-14  C +21.7k / P +38.7k ｜ Activity HIGH ｜ 1D
10-15  C +7.6k / P +26.1k ｜ Activity HIGH ｜ 2D
10-16  C +2.4k / P +54.0k ｜ Activity HIGH ｜ 3D
10-19  C +8.8k / P +22.2k ｜ Activity HIGH ｜ 6D

📆 10-14 Forward Structure
存量OI: C 47.7k / P 104.1k，今日变化ΔOI: C +21.7k / P +38.7k，平值价格ATM: C $3.40 / P $3.33 ｜ ATM IV 19.3%，净 delta 敞口 52k shares
Top ΔOI: C 750 +2,841 ｜ C 760 +2,583
仓位参考: Max Pain 748 ｜ Call Wall 750（+0.8%，弱）（OI 3.7k） ｜ Put Wall 730（-1.9%，弱）（OI 5.2k）
量化解读： 存量 Put 重｜ATM IV 19.3%｜历史 Rank 51%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 51,932 股

📆 10-15 Forward Structure
存量OI: C 37.6k / P 75.8k，今日变化ΔOI: C +7.6k / P +26.1k，平值价格ATM: C $4.42 / P $4.21 ｜ ATM IV 18.4%，净 delta 敞口 -80k shares
Top ΔOI: C 770 +2,492 ｜ P 694 +1,613 ｜ C 762 +1,060
仓位参考: Max Pain 749 ｜ Call Wall 765（+2.9%，弱）（OI 2.4k） ｜ Put Wall 725（-2.5%，弱）（OI 2.7k）
量化解读： 存量 Put 重｜ATM IV 18.4%｜历史 Rank 51%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 80,248 股

📆 10-16 Forward Structure
存量OI: C 720.0k / P 1252.0k，今日变化ΔOI: C +2.4k / P +54.0k，平值价格ATM: C $5.32 / P $4.89 ｜ ATM IV 18.1%，净 delta 敞口 -234k shares
Top ΔOI: P 655 +18,219 ｜ C 770 -5,909 ｜ P 740 +4,449
仓位参考: Max Pain 735 ｜ Call Wall 760（+2.2%）（OI 67.9k） ｜ Put Wall 740（-0.5%，弱）（OI 34.2k）
量化解读： 存量 Put 重｜ATM IV 18.1%｜历史 Rank 51%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 234,189 股

📆 10-19 Forward Structure
存量OI: C 26.7k / P 49.1k，今日变化ΔOI: C +8.8k / P +22.2k，平值价格ATM: C $6.11 / P $5.77 ｜ ATM IV 15.0%，净 delta 敞口 21k shares
Top ΔOI: C 766 +1,980
仓位参考: Max Pain 750 ｜ Call Wall 766（+3.0%，弱）（OI 2.3k） ｜ Put Wall 745（+0.2%，弱）（OI 2.7k）
量化解读： 存量 Put 重｜ATM IV 15.0%｜历史 Rank 51%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 正 20,803 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/QQQ_morning.json