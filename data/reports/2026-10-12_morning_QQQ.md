# 期权晨报 2026-10-12（快照 10:20 ET）

📊 市场环境

SPY $778.10 ｜ QQQ $746.04
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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 10-13 770C ΔOI +2,986（距现价 +3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 751.27 → 今开 749.64（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 749.79 ｜ 低 745.43

Options: P/C成交量 1.16 | OI比 2.63 | ATM IV 15.5% | Skew 1.9pp | Term 1.19 | ExpMove ±0.7%（近端） | Rank 33%
量化视角： IV 中性（Rank 33%）｜期限结构正常偏陡（Term 1.19）｜保护溢价薄（Skew 1.9pp）｜当日成交偏 Put（P/C量 1.16）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.16×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.63×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 29% ｜ P/C OI(近端) 94%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 29%）｜近端 Put 显著偏重（P/C OI 分位 94%，历史高位区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-13（1D）±0.7% ｜ 10-14（2D）±1.1% ｜ 10-15（3D）±1.3% ｜ 10-16（4D）±1.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -328,809,137 | GEX Change vs 上次快照 -416,548,401 | Flip: Primary Flip: 750.82（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 3357 / LOW 329 / INVALID 1380
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 750.82（全链重定价，覆盖 99%）
Call Wall 760（弱结构｜现价低于该位 1.6%）
最近结构参考: Flip 751（现价低于该位 0.4%）
量化视角： 负 Gamma（3.29亿，历史分位 29%，中性区）｜由正转负（4.17亿）｜现价位于 Flip 下方 0.44%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 751（MaxPain，仅结算参考） / 760（Call Wall，弱结构）。
• Gamma 区域：切换参考 751（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-12 560.0P — Vol 34,670 | 最新价 $0.01 | OI 515→34975 (ΔOI +34460张) | ΔOI/Volume 99.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增34460张（+6691.3% vs前日OI），连续性待观察（方向未知）
11-06 710.0P — Vol 10,579 | 最新价 $4.09 | OI 798→10898 (ΔOI +10100张) | ΔOI/Volume 95.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10100张（+1265.7% vs前日OI），连续性待观察（方向未知）
11-13 690.0P — Vol 6,340 | 最新价 $3.22 | OI 8938→15200 (ΔOI +6262张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6262张（+70.1% vs前日OI），连续性待观察（方向未知）
11-13 725.0P — Vol 6,422 | 最新价 $7.89 | OI 9501→15726 (ΔOI +6225张) | ΔOI/Volume 96.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6225张（+65.5% vs前日OI），连续性待观察（方向未知）
10-16 700.0P — Vol 10,925 | 最新价 $0.13 | OI 59812→65862 (ΔOI +6050张) | ΔOI/Volume 55.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6050张（+10.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 63,097 张（Put 63,097 / Call 0），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $11M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 109.4k / P 287.5k，今日成交量: C 308.9k / P 393.8k，平值价格ATM: C $0.94 / P $1.62 ｜ ATM IV 15.5%，预期波动 ±0.3%，Max Pain 751
Top ΔOI: P 560 +34,460 ｜ P 747 +5,093 ｜ P 743 +4,552

📆 Forward Expiration Structure

10-13  C +16.1k / P +31.3k ｜ Activity HIGH ｜ 1D
10-14  C +5.8k / P +18.1k ｜ Activity HIGH ｜ 2D
10-15  C +13.4k / P +4.6k ｜ Activity HIGH ｜ 3D
10-16  C +9.1k / P +44.2k ｜ Activity HIGH ｜ 4D

📆 10-13 Forward Structure
存量OI: C 42.5k / P 123.6k，今日变化ΔOI: C +16.1k / P +31.3k，平值价格ATM: C $2.31 / P $2.89 ｜ ATM IV 14.7%，净 delta 敞口 -438k shares
Top ΔOI: C 770 +2,986 ｜ P 735 +2,224 ｜ P 708 +1,974
仓位参考: Max Pain 751 ｜ Call Wall 760（+1.7%，弱）（OI 2.8k） ｜ Put Wall 750（+0.3%，弱）（OI 12.7k）
量化解读： 存量 Put 重｜ATM IV 14.7%｜历史 Rank 33%（近端代理）｜IV/RV 1.08×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 438,229 股

📆 10-14 Forward Structure
存量OI: C 26.0k / P 65.3k，今日变化ΔOI: C +5.8k / P +18.1k，平值价格ATM: C $3.62 / P $4.21 ｜ ATM IV 16.9%，净 delta 敞口 -202k shares
Top ΔOI: P 725 +1,773 ｜ C 765 +1,274 ｜ P 746 +1,195
仓位参考: Max Pain 751 ｜ Call Wall 755（+1.0%，弱）（OI 2.3k） ｜ Put Wall 730（-2.3%，弱）（OI 2.8k）
量化解读： 存量 Put 重｜ATM IV 16.9%｜历史 Rank 33%（近端代理）｜IV/RV 1.24×（近似）｜净 delta 敞口 负 202,014 股

📆 10-15 Forward Structure
存量OI: C 30.0k / P 49.7k，今日变化ΔOI: C +13.4k / P +4.6k，平值价格ATM: C $4.55 / P $4.98 ｜ ATM IV 16.9%，净 delta 敞口 3k shares
Top ΔOI: C 770 +5,037 ｜ C 767 +1,725 ｜ C 760 +1,698
仓位参考: Max Pain 750 ｜ Call Wall 767（+2.6%，弱）（OI 2.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 16.9%｜历史 Rank 33%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 正 3,373 股

📆 10-16 Forward Structure
存量OI: C 717.6k / P 1198.0k，今日变化ΔOI: C +9.1k / P +44.2k，平值价格ATM: C $5.32 / P $5.80 ｜ ATM IV 17.0%，净 delta 敞口 -469k shares
Top ΔOI: P 700 +6,050 ｜ P 725 -4,089 ｜ P 680 +3,087
仓位参考: Max Pain 734 ｜ Call Wall 760（+1.7%，弱）（OI 66.6k） ｜ Put Wall 740（-1.0%，弱）（OI 29.7k）
量化解读： 存量 Put 重｜ATM IV 17.0%｜历史 Rank 33%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 负 469,031 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/QQQ_morning.json