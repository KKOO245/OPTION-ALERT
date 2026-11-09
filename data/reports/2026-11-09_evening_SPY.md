# 期权晚报 2026-11-09（快照 16:40 ET）

📊 市场环境

SPY $752.69 ｜ QQQ $679.35
VIX 19.92 ↓22.3%（5D -5.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周二 11-10 08:30　【高】Core Inflation Rate YoY　预测 2.8 ｜ 实际 待公布 ｜ 前值 2.6
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.6
- 周二 11-10 08:30　【高】Inflation Rate YoY　预测 3.9 ｜ 实际 待公布 ｜ 前值 3.7
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-10 753C ΔOI +4,464（距现价 +0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 741.95 → 收盘 752.69（+1.4%） ｜ 今日高 755.42 ｜ 低 741.09 ｜ 昨收 735.29 → 收盘 752.69（+2.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.95 | OI比 1.80 | ATM IV 16.1% | Skew -2.7pp | Term 0.99 | ExpMove ±0.8%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构正常（Term 0.99）｜Put 保护异常便宜（Skew -2.7pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.80×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 42% ｜ P/C OI(近端) 47%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 42%）｜近端持仓结构中性（P/C OI 分位 47%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-10（1D）±0.8% ｜ 11-11（2D）±1.1% ｜ 11-12（3D）±1.3% ｜ 11-13（4D）±1.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -637,738,734 | GEX Change vs 上次快照 278,835,829 | Flip: Primary Flip: 759.97（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3305 / LOW 313 / INVALID 1598
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 759.97（全链重定价，覆盖 96%）
最近结构参考: Flip 760（现价低于该位 1.0%）
量化视角： 负 Gamma（6.38亿，历史分位 42%，中性区）｜负 Gamma 缓解（+2.79亿）｜现价位于 Flip 下方 0.96%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 741（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 760（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 710.0P — Vol 123,426 | 最新价 $1.21 | OI 23684→131906 (ΔOI +108222张) | ΔOI/Volume 87.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增108222张（+456.9% vs前日OI），连续性待观察（方向未知）
11-13 715.0P — Vol 60,427 | 最新价 $0.34 | OI 10487→64985 (ΔOI +54498张) | ΔOI/Volume 90.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增54498张（+519.7% vs前日OI），连续性待观察（方向未知）
11-13 730.0P — Vol 79,924 | 最新价 $0.93 | OI 25107→70316 (ΔOI +45209张) | ΔOI/Volume 56.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增45209张（+180.1% vs前日OI），连续性待观察（方向未知）
11-20 725.0P — Vol 125,460 | 最新价 $2.23 | OI 110852→153423 (ΔOI +42571张) | ΔOI/Volume 33.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增42571张（+38.4% vs前日OI），连续性待观察（方向未知）
11-27 720.0P — Vol 22,820 | 最新价 $2.78 | OI 3280→45727 (ΔOI +42447张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增42447张（+1294.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 292,947 张（Put 292,947 / Call 0），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $34M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-10  C +30.5k / P +19.3k ｜ Activity HIGH ｜ 1D
11-11  C +17.9k / P +7.4k ｜ Activity HIGH ｜ 2D
11-12  C +6.8k / P +8.1k ｜ Activity HIGH ｜ 3D
11-13  C +30.4k / P +147.0k ｜ Activity HIGH ｜ 4D

📆 11-10 Forward Structure
存量OI: C 139.6k / P 96.3k，今日变化ΔOI: C +30.5k / P +19.3k，平值价格ATM: C $3.14 / P $2.94 ｜ ATM IV 19.2%，净 delta 敞口 1.6M shares
Top ΔOI: C 753 +4,464 ｜ C 748 +4,215
仓位参考: Max Pain 740 ｜ Call Wall 740（-1.7%，弱）（OI 12.4k） ｜ Put Wall 734（-2.5%）（OI 10.0k）
量化解读： 存量 Call 重｜ATM IV 19.2%｜历史 Rank 70%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,557,438 股

📆 11-11 Forward Structure
存量OI: C 76.3k / P 80.4k，今日变化ΔOI: C +17.9k / P +7.4k，平值价格ATM: C $4.16 / P $3.97 ｜ ATM IV 18.1%，净 delta 敞口 588k shares
Top ΔOI: P 716 +5,039 ｜ C 770 +3,760 ｜ P 725 -1,641
仓位参考: Max Pain 746 ｜ Call Wall 770（+2.3%）（OI 6.7k） ｜ Put Wall 750（-0.4%，弱）（OI 3.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 18.1%｜历史 Rank 70%（近端代理）｜IV/RV 0.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 588,134 股

📆 11-12 Forward Structure
存量OI: C 55.4k / P 58.4k，今日变化ΔOI: C +6.8k / P +8.1k，平值价格ATM: C $5.00 / P $4.72 ｜ ATM IV 18.0%，净 delta 敞口 208k shares
Top ΔOI: P 725 +2,686 ｜ C 760 +1,275 ｜ P 735 +949
仓位参考: Max Pain 748 ｜ Call Wall 775（+3.0%）（OI 6.7k） ｜ Put Wall 735（-2.4%，弱）（OI 2.5k）
量化解读： 存量两侧均衡｜ATM IV 18.0%｜历史 Rank 70%（近端代理）｜IV/RV 0.88×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 207,940 股

📆 11-13 Forward Structure
存量OI: C 284.7k / P 488.3k，今日变化ΔOI: C +30.4k / P +147.0k，平值价格ATM: C $5.95 / P $5.45 ｜ ATM IV 17.9%，净 delta 敞口 854k shares
Top ΔOI: P 715 +54,498 ｜ P 730 +45,209 ｜ P 655 +9,014
仓位参考: Max Pain 750 ｜ Call Wall 750（-0.4%，弱）（OI 11.2k） ｜ Put Wall 745（-1.0%，弱）（OI 28.8k）
量化解读： 存量 Put 重｜ATM IV 17.9%｜历史 Rank 70%（近端代理）｜IV/RV 0.88×（近似）｜净 delta 敞口 正 853,680 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/SPY_evening.json