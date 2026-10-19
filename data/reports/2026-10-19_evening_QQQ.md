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
🟡 **近现价集中开仓**: 10-20 700P ΔOI +5,465（距现价 -2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-22 695P ΔOI +10,130 占该期限总 OI 13.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 719.61 → 收盘 718.36（-0.2%） ｜ 今日高 724.55 ｜ 低 716.57 ｜ 昨收 709.80 → 收盘 718.36（+1.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.11 | OI比 1.38 | ATM IV 18.6% | Skew 0.9pp | Term 1.16 | ExpMove ±0.9%（近端） | Rank 52%
量化视角： IV 中性（Rank 52%）｜期限结构正常偏陡（Term 1.16）｜保护溢价薄（Skew 0.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.11×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.38×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 15% ｜ P/C OI(近端) 27%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 15%）｜近端持仓结构中性（P/C OI 分位 27%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-20（1D）±0.9% ｜ 10-21（2D）±1.4% ｜ 10-22（3D）±1.7% ｜ 10-23（4D）±2.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -632,934,267 | GEX Change vs 上次快照 58,270,706 | Flip: Primary Flip: 732.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2831 / LOW 382 / INVALID 1829
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 732.14（全链重定价，覆盖 94%）
Put Wall 700（弱结构｜现价高于该位 2.6%）
最近结构参考: Flip 732（现价低于该位 1.9%）
量化视角： 负 Gamma（6.33亿，历史分位偏负区，比 85% 的交易日更负）｜负 Gamma 缓解（+5827万）｜现价位于 Flip 下方 1.88%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构） / 717（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 732（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 675.0P — Vol 25,015 | 最新价 $2.31 | OI 11732→66889 (ΔOI +55157张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增55157张（+470.1% vs前日OI），连续性待观察（方向未知）
10-30 690.0P — Vol 3,201 | 最新价 $3.91 | OI 42111→69818 (ΔOI +27707张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27707张（+65.8% vs前日OI），连续性待观察（方向未知）
11-20 705.0P — Vol 1,056 | 最新价 $12.54 | OI 10324→34872 (ΔOI +24548张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24548张（+237.8% vs前日OI），连续性待观察（方向未知）
11-06 769.0C — Vol 125 | 最新价 $0.69 | OI 15342→30308 (ΔOI +14966张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14966张（+97.5% vs前日OI），连续性待观察（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 122,378 张（Put 107,412 / Call 14,966），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $54M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-20  C +41.5k / P +47.1k ｜ Activity HIGH ｜ 1D
10-21  C +26.3k / P +17.3k ｜ Activity HIGH ｜ 2D
10-22  C +7.5k / P +16.4k ｜ Activity HIGH ｜ 3D
10-23  C +59.2k / P +97.6k ｜ Activity HIGH ｜ 4D

📆 10-20 Forward Structure
存量OI: C 99.2k / P 106.5k，今日变化ΔOI: C +41.5k / P +47.1k，平值价格ATM: C $3.81 / P $2.98 ｜ ATM IV 22.3%，净 delta 敞口 1.2M shares
Top ΔOI: P 700 +5,465 ｜ P 705 +4,001
仓位参考: Max Pain 719 ｜ Call Wall 733（+2.0%，弱）（OI 7.4k） ｜ Put Wall 705（-1.9%，弱）（OI 10.8k）
量化解读： 存量两侧均衡｜ATM IV 22.3%｜历史 Rank 52%（近端代理）｜IV/RV 1.45×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,235,372 股

📆 10-21 Forward Structure
存量OI: C 57.8k / P 56.7k，今日变化ΔOI: C +26.3k / P +17.3k，平值价格ATM: C $5.42 / P $4.49 ｜ ATM IV 23.4%，净 delta 敞口 718k shares
Top ΔOI: P 700 +4,861 ｜ C 743 +2,233 ｜ C 742 +2,055
仓位参考: Max Pain 720 ｜ Call Wall 730（+1.6%，弱）（OI 2.1k） ｜ Put Wall 700（-2.6%）（OI 5.8k）
量化解读： 存量两侧均衡｜ATM IV 23.4%｜历史 Rank 52%（近端代理）｜IV/RV 1.52×（近似）｜净 delta 敞口 正 718,189 股

📆 10-22 Forward Structure
存量OI: C 28.1k / P 45.7k，今日变化ΔOI: C +7.5k / P +16.4k，平值价格ATM: C $6.56 / P $5.70 ｜ ATM IV 23.8%，净 delta 敞口 3k shares
Top ΔOI: P 695 +10,130 ｜ P 718 +1,454 ｜ P 705 -1,210
仓位参考: Max Pain 724 ｜ Call Wall 730（+1.6%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 23.8%｜历史 Rank 52%（近端代理）｜IV/RV 1.55×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,574 股

📆 10-23 Forward Structure
存量OI: C 252.9k / P 350.8k，今日变化ΔOI: C +59.2k / P +97.6k，平值价格ATM: C $7.66 / P $6.61 ｜ ATM IV 23.8%，净 delta 敞口 940k shares
Top ΔOI: P 711 +12,262 ｜ C 740 +8,588 ｜ P 690 +8,020
仓位参考: Max Pain 727 ｜ Call Wall 735（+2.3%，弱）（OI 22.4k） ｜ Put Wall 711（-1.0%，弱）（OI 40.4k）
量化解读： 存量 Put 重｜ATM IV 23.8%｜历史 Rank 52%（近端代理）｜IV/RV 1.55×（近似）｜净 delta 敞口 正 939,994 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/QQQ_evening.json