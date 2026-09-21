# 期权晚报 2026-09-21（快照 16:40 ET）

📊 市场环境

SPY $773.50 ｜ QQQ $741.47
VIX 14.87 ↑0.4%（5D -13.0%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 33.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-22 745P ΔOI +10,973（距现价 -3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 766.25 → 收盘 773.50（+0.9%） ｜ 今日高 774.89 ｜ 低 766.03 ｜ 昨收 761.69 → 收盘 773.50（+1.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.74 | OI比 1.67 | ATM IV 12.3% | Skew -0.3pp | Term 1.00 | ExpMove ±0.4%（近端） | Rank 47%
量化视角： IV 中性（Rank 47%）｜期限结构正常（Term 1.00）｜Put 保护异常便宜（Skew -0.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.74×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.67×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 75% ｜ P/C OI(近端) 36%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 75%）｜近端持仓结构中性（P/C OI 分位 36%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-22（1D）±0.4% ｜ 09-23（2D）±0.6% ｜ 09-24（3D）±0.8% ｜ 09-25（4D）±0.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 929,656,857 | GEX Change vs 上次快照 442,456,152 | Flip: Primary Flip: 766.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 3073 / LOW 378 / INVALID 1745
结构观察区: Primary Flip 766.42（全链重定价，覆盖 97%）
最近结构参考: Flip 766（现价高于该位 0.9%）
量化视角： 正 Gamma（9.30亿，历史分位 75%，中性区）｜正 Gamma 增强（+4.42亿）｜现价位于 Flip 上方 0.92%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 761（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 766（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-22 722.0P — Vol 508 | 最新价 $0.01 | OI 309→21264 (ΔOI +20955张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20955张（+6781.6% vs前日OI），连续性待观察（方向未知）
09-22 725.0P — Vol 1,385 | 最新价 $0.01 | OI 1695→17120 (ΔOI +15425张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15425张（+910.0% vs前日OI），连续性待观察（方向未知）
09-25 755.0P — Vol 10,403 | 最新价 $0.38 | OI 5941→19104 (ΔOI +13163张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13163张（+221.6% vs前日OI），连续性待观察（方向未知）
10-16 740.0P — Vol 7,029 | 最新价 $2.13 | OI 31086→43805 (ΔOI +12719张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12719张（+40.9% vs前日OI），连续性待观察（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 62,262 张（Put 62,262 / Call 0），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜彩票/名义 2 档（价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-22  C +24.6k / P +73.3k ｜ Activity HIGH ｜ 1D
09-23  C +22.8k / P +26.3k ｜ Activity HIGH ｜ 2D
09-24  C +9.7k / P +6.3k ｜ Activity HIGH ｜ 3D
09-25  C +37.6k / P +54.0k ｜ Activity HIGH ｜ 4D

📆 09-22 Forward Structure
存量OI: C 99.7k / P 121.7k，今日变化ΔOI: C +24.6k / P +73.3k，平值价格ATM: C $1.87 / P $1.43 ｜ ATM IV 10.1%，净 delta 敞口 1.9M shares
Top ΔOI: P 722 +20,955 ｜ P 725 +15,425 ｜ P 745 +10,973
仓位参考: Max Pain 760 ｜ Call Wall 789（+2.0%，弱）（OI 12.7k）
量化解读： 存量 Put 重｜ATM IV 10.1%｜历史 Rank 47%（近端代理）｜IV/RV 1.14×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,947,228 股

📆 09-23 Forward Structure
存量OI: C 67.4k / P 65.3k，今日变化ΔOI: C +22.8k / P +26.3k，平值价格ATM: C $2.64 / P $2.14 ｜ ATM IV 10.4%，净 delta 敞口 1.3M shares
Top ΔOI: P 755 +4,834 ｜ P 745 +4,673 ｜ C 765 +2,601
仓位参考: Max Pain 760 ｜ Call Wall 760（-1.7%，弱）（OI 4.4k） ｜ Put Wall 755（-2.4%，弱）（OI 6.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 10.4%｜历史 Rank 47%（近端代理）｜IV/RV 1.17×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,254,701 股

📆 09-24 Forward Structure
存量OI: C 43.1k / P 51.3k，今日变化ΔOI: C +9.7k / P +6.3k，平值价格ATM: C $3.30 / P $2.74 ｜ ATM IV 10.7%，净 delta 敞口 539k shares
Top ΔOI: C 771 +4,835 ｜ P 727 +2,514 ｜ C 770 +641
仓位参考: Max Pain 760 ｜ Call Wall 771（-0.3%）（OI 5.3k） ｜ Put Wall 752（-2.8%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 10.7%｜历史 Rank 47%（近端代理）｜IV/RV 1.21×（近似）｜净 delta 敞口 正 538,747 股

📆 09-25 Forward Structure
存量OI: C 263.3k / P 563.8k，今日变化ΔOI: C +37.6k / P +54.0k，平值价格ATM: C $3.98 / P $3.21 ｜ ATM IV 11.0%，净 delta 敞口 1.6M shares
Top ΔOI: P 755 +13,163
仓位参考: Max Pain 762 ｜ Call Wall 790（+2.1%，弱）（OI 29.7k）
量化解读： 存量 Put 重｜ATM IV 11.0%｜历史 Rank 47%（近端代理）｜IV/RV 1.24×（近似）｜净 delta 敞口 正 1,609,960 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/SPY_evening.json