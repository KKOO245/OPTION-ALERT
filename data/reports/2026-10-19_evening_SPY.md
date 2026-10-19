# 期权晚报 2026-10-19（快照 16:40 ET）

📊 市场环境

SPY $766.48 ｜ QQQ $718.36
VIX 18.44 ↓7.8%（5D +21.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 23.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🟡 **近现价集中开仓**: 10-20 731P ΔOI +9,672（距现价 -4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 767.23 → 收盘 766.48（-0.1%） ｜ 今日高 770.46 ｜ 低 765.82 ｜ 昨收 763.25 → 收盘 766.48（+0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.04 | OI比 2.14 | ATM IV 15.6% | Skew 1.0pp | Term 0.91 | ExpMove ±0.6%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构正常（Term 0.91）｜保护溢价薄（Skew 1.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.04×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.14×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 33% ｜ P/C OI(近端) 71%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 33%）｜近端持仓结构中性（P/C OI 分位 71%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-20（1D）±0.6% ｜ 10-21（2D）±0.8% ｜ 10-22（3D）±1.0% ｜ 10-23（4D）±1.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,027,622,102 | GEX Change vs 上次快照 85,373,815 | Flip: Primary Flip: 773.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 2762 / LOW 337 / INVALID 1637
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 773.36（全链重定价，覆盖 92%）
最近结构参考: Flip 773（现价低于该位 0.9%）
量化视角： 负 Gamma（10.28亿，历史分位 33%，中性区）｜负 Gamma 缓解（+8537万）｜现价位于 Flip 下方 0.89%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 766（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 773（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 750.0P — Vol 92,173 | 最新价 $2.93 | OI 28359→115566 (ΔOI +87207张) | ΔOI/Volume 94.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增87207张（+307.5% vs前日OI），连续性待观察（方向未知）
10-30 735.0P — Vol 85,313 | 最新价 $1.48 | OI 14184→95224 (ΔOI +81040张) | ΔOI/Volume 95.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增81040张（+571.4% vs前日OI），连续性待观察（方向未知）
10-30 510.0P — Vol 175 | 最新价 $0.04 | OI 3002→36307 (ΔOI +33305张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33305张（+1109.4% vs前日OI），连续性待观察（方向未知）
10-30 515.0P — Vol 29,664（Yahoo补） | 最新价 $0.16 | OI 657→29833 (ΔOI +29176张) | ΔOI/Volume 98.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29176张（+4440.8% vs前日OI），连续性待观察（方向未知）
10-23 790.0C — Vol 3,675 | 最新价 $0.03 | OI 12800→36380 (ΔOI +23580张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23580张（+184.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 254,308 张（Put 230,728 / Call 23,580），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $38M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-20  C +36.6k / P +55.2k ｜ Activity HIGH ｜ 1D
10-21  C +23.8k / P +68.0k ｜ Activity HIGH ｜ 2D
10-22  C +38.4k / P +43.3k ｜ Activity HIGH ｜ 3D
10-23  C +79.7k / P +136.5k ｜ Activity HIGH ｜ 4D

📆 10-20 Forward Structure
存量OI: C 98.9k / P 187.7k，今日变化ΔOI: C +36.6k / P +55.2k，平值价格ATM: C $2.70 / P $1.68 ｜ ATM IV 13.4%，净 delta 敞口 393k shares
Top ΔOI: P 625 +10,585 ｜ P 731 +9,672 ｜ P 734 +7,559
仓位参考: Max Pain 770 ｜ Call Wall 775（+1.1%，弱）（OI 6.1k） ｜ Put Wall 751（-2.0%，弱）（OI 12.3k）
量化解读： 存量 Put 重｜ATM IV 13.4%｜历史 Rank 68%（近端代理）｜IV/RV 1.56×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 392,609 股

📆 10-21 Forward Structure
存量OI: C 81.3k / P 191.1k，今日变化ΔOI: C +23.8k / P +68.0k，平值价格ATM: C $3.82 / P $2.67 ｜ ATM IV 14.1%，净 delta 敞口 -32k shares
Top ΔOI: P 741 +14,519 ｜ P 731 +7,844 ｜ P 705 +5,288
仓位参考: Max Pain 769 ｜ Call Wall 773（+0.9%，弱）（OI 3.2k） ｜ Put Wall 746（-2.7%，弱）（OI 10.6k）
量化解读： 存量 Put 重｜ATM IV 14.1%｜历史 Rank 68%（近端代理）｜IV/RV 1.64×（近似）｜净 delta 敞口 负 31,584 股

📆 10-22 Forward Structure
存量OI: C 71.0k / P 75.2k，今日变化ΔOI: C +38.4k / P +43.3k，平值价格ATM: C $4.62 / P $3.37 ｜ ATM IV 14.3%，净 delta 敞口 103k shares
Top ΔOI: C 780 +5,040 ｜ C 784 +4,895 ｜ P 740 +4,766
仓位参考: Max Pain 771 ｜ Call Wall 780（+1.8%，弱）（OI 6.2k） ｜ Put Wall 745（-2.8%，弱）（OI 4.2k）
量化解读： 存量两侧均衡｜ATM IV 14.3%｜历史 Rank 68%（近端代理）｜IV/RV 1.66×（近似）｜净 delta 敞口 正 103,361 股

📆 10-23 Forward Structure
存量OI: C 277.6k / P 500.8k，今日变化ΔOI: C +79.7k / P +136.5k，平值价格ATM: C $5.48 / P $4.02 ｜ ATM IV 14.5%，净 delta 敞口 -753k shares
Top ΔOI: C 790 +23,580 ｜ C 780 +15,472 ｜ P 769 +12,737
仓位参考: Max Pain 770 ｜ Call Wall 780（+1.8%，弱）（OI 24.1k） ｜ Put Wall 745（-2.8%，弱）（OI 38.8k）
量化解读： 存量 Put 重｜ATM IV 14.5%｜历史 Rank 68%（近端代理）｜IV/RV 1.69×（近似）｜净 delta 敞口 负 753,420 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/SPY_evening.json