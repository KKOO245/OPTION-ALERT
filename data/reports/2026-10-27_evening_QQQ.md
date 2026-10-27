# 期权晚报 2026-10-27（快照 16:40 ET）

📊 市场环境

SPY $769.66 ｜ QQQ $721.25
VIX 17.52 ↓4.7%（5D +1.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 1.8 ｜ 前值 0.1　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 700P ΔOI -27,479（距现价 -2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 715.10 → 收盘 721.25（+0.9%） ｜ 今日高 722.86 ｜ 低 713.59 ｜ 昨收 712.20 → 收盘 721.25（+1.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.00 | OI比 1.32 | ATM IV 17.4% | Skew -4.6pp | Term 1.24 | ExpMove ±1.0%（近端） | Rank 45%
量化视角： IV 中性（Rank 45%）｜期限结构正常偏陡（Term 1.24）｜Put 保护异常便宜（Skew -4.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.00×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.32×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 35% ｜ P/C OI(近端) 23%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 35%）｜近端持仓结构中性（P/C OI 分位 23%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-28（1D）±1.0% ｜ 10-29（2D）±1.6% ｜ 10-30（3D）±1.9% ｜ 11-02（6D）±2.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -219,338,235 | GEX Change vs 上次快照 237,277,746 | Flip: Primary Flip: 726.57（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 2901 / LOW 357 / INVALID 1292
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 726.57（全链重定价，覆盖 96%）
最近结构参考: Flip 727（现价低于该位 0.7%）
量化视角： 负 Gamma（2.19亿，历史分位 35%，中性区）｜负 Gamma 缓解（+2.37亿）｜现价位于 Flip 下方 0.73%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 712（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 727（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-02 740.0C — Vol 1,961 | 最新价 $0.76 | OI 736→15988 (ΔOI +15252张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15252张（+2072.3% vs前日OI），连续性待观察（方向未知）
11-20 680.0P — Vol 9,208 | 最新价 $7.48 | OI 65697→76958 (ΔOI +11261张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增11261张（+17.1% vs前日OI），值得跟踪（方向未知）
11-06 713.0P — Vol 3,383 | 最新价 $12.42 | OI 39314→49355 (ΔOI +10041张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10041张（+25.5% vs前日OI），连续性待观察（方向未知）
11-02 720.0C — Vol 1,459 | 最新价 $5.74 | OI 871→9366 (ΔOI +8495张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8495张（+975.3% vs前日OI），连续性待观察（方向未知）
11-02 725.0C — Vol 400 | 最新价 $3.67 | OI 696→8355 (ΔOI +7659张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7659张（+1100.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 52,708 张（Put 21,302 / Call 31,406），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $21M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-28  C +20.6k / P +45.1k ｜ Activity HIGH ｜ 1D
10-29  C +6.0k / P +17.7k ｜ Activity HIGH ｜ 2D
10-30  C +22.7k / P -22.4k ｜ Activity HIGH ｜ 3D
11-02  C +3.5k / P +1.1k ｜ Activity HIGH ｜ 6D

📆 10-28 Forward Structure
存量OI: C 63.0k / P 98.9k，今日变化ΔOI: C +20.6k / P +45.1k，平值价格ATM: C $3.69 / P $3.74 ｜ ATM IV 24.5%，净 delta 敞口 656k shares
仓位参考: Max Pain 715 ｜ Call Wall 715（-0.9%，弱）（OI 4.1k） ｜ Put Wall 710（-1.6%，弱）（OI 4.6k）
量化解读： 存量 Put 重｜ATM IV 24.5%｜历史 Rank 45%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 655,559 股

📆 10-29 Forward Structure
存量OI: C 42.0k / P 72.2k，今日变化ΔOI: C +6.0k / P +17.7k，平值价格ATM: C $5.82 / P $5.72 ｜ ATM IV 26.8%，净 delta 敞口 174k shares
Top ΔOI: P 660 +2,022
仓位参考: Max Pain 717 ｜ Call Wall 725（+0.5%，弱）（OI 2.3k） ｜ Put Wall 705（-2.3%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 26.8%｜历史 Rank 45%（近端代理）｜IV/RV 1.49×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 174,051 股

📆 10-30 Forward Structure
存量OI: C 363.3k / P 759.4k，今日变化ΔOI: C +22.7k / P -22.4k，平值价格ATM: C $7.09 / P $6.73 ｜ ATM IV 26.3%，净 delta 敞口 2.5M shares
Top ΔOI: P 700 -27,479 ｜ P 618 +20,908 ｜ P 690 -18,725
仓位参考: Max Pain 722 ｜ Call Wall 740（+2.6%，弱）（OI 21.4k） ｜ Put Wall 700（-2.9%，弱）（OI 44.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 26.3%｜历史 Rank 45%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,512,015 股

📆 11-02 Forward Structure
存量OI: C 60.7k / P 46.7k，今日变化ΔOI: C +3.5k / P +1.1k，平值价格ATM: C $8.47 / P $7.68 ｜ ATM IV 21.3%，净 delta 敞口 76k shares
Top ΔOI: P 675 -2,115 ｜ P 665 -1,335
仓位参考: Max Pain 714 ｜ Call Wall 740（+2.6%）（OI 15.7k） ｜ Put Wall 710（-1.6%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 21.3%｜历史 Rank 45%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 正 76,382 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/QQQ_evening.json