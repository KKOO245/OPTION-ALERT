# 期权晨报 2026-09-28（快照 10:20 ET）

📊 市场环境

SPY $765.39 ｜ QQQ $736.53
VIX 15.89 ↑6.9%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.24 ｜ 实际 待公布 ｜ 前值 7.271
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 54.9 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 84 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 09-29 736P ΔOI +24,300（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 744.50 → 今开 740.46（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 741.42 ｜ 低 735.31

Options: P/C成交量 1.21 | OI比 1.96 | ATM IV 20.8% | Skew 1.8pp | Term 0.92 | ExpMove ±0.8%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构正常（Term 0.92）｜保护溢价薄（Skew 1.8pp）｜当日成交偏 Put（P/C量 1.21）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.21×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.96×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 28% ｜ P/C OI(近端) 74%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 28%）｜近端持仓结构中性（P/C OI 分位 74%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-29（1D）±0.8% ｜ 09-30（2D）±1.2% ｜ 10-01（3D）±1.5% ｜ 10-02（4D）±1.7%
   ⇒ IV–VIX Spread: +4.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -336,342,083 | GEX Change vs 上次快照 -760,141,211 | Flip: Primary Flip: 741.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 3413 / LOW 347 / INVALID 1562
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 741.67（全链重定价，覆盖 98%）
Put Wall 730（弱结构｜现价高于该位 1.1%） | Call Wall 760（现价低于该位 2.8%）
最近结构参考: Flip 742（现价低于该位 0.4%）
量化视角： 负 Gamma（3.36亿，历史分位 28%，中性区）｜由正转负（7.60亿）｜现价位于 Flip 下方 0.45%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 730（Put Wall，弱结构）；上方 742（MaxPain，仅结算参考） / 760（Call Wall）。
• Gamma 区域：切换参考 742（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 725.0P — Vol 39,074 | 最新价 $9.58 | OI 2018→40444 (ΔOI +38426张) | ΔOI/Volume 98.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增38426张（+1904.2% vs前日OI），连续性待观察（方向未知）
10-30 685.0P — Vol 39,226 | 最新价 $3.35 | OI 4569→39801 (ΔOI +35232张) | ΔOI/Volume 89.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增35232张（+771.1% vs前日OI），连续性待观察（方向未知）
09-29 736.0P — Vol 49,431 | 最新价 $1.45 | OI 355→24655 (ΔOI +24300张) | ΔOI/Volume 49.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24300张（+6845.1% vs前日OI），连续性待观察（方向未知）
09-28 738.0P — Vol 41,788 | 最新价 $1.03 | OI 2189→25551 (ΔOI +23362张) | ΔOI/Volume 55.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23362张（+1067.2% vs前日OI），连续性待观察（方向未知）
09-29 730.0P — Vol 32,609 | 最新价 $0.67 | OI 14713→30832 (ΔOI +16119张) | ΔOI/Volume 49.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16119张（+109.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 137,439 张（Put 137,439 / Call 0），跨 3 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $55M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 145.7k / P 286.2k，今日成交量: C 376.6k / P 456.0k，平值价格ATM: C $1.63 / P $1.65 ｜ ATM IV 20.8%，预期波动 ±0.4%，Max Pain 742
Top ΔOI: P 738 +23,362 ｜ P 595 +11,367 ｜ C 750 +8,548

📆 Forward Expiration Structure

09-29  C +13.5k / P +56.1k ｜ Activity HIGH ｜ 1D
09-30  C -36.4k / P +21.1k ｜ Activity HIGH ｜ 2D
10-01  C +8.1k / P +7.8k ｜ Activity HIGH ｜ 3D
10-02  C +47.9k / P +83.7k ｜ Activity HIGH ｜ 4D

📆 09-29 Forward Structure
存量OI: C 54.4k / P 159.0k，今日变化ΔOI: C +13.5k / P +56.1k，平值价格ATM: C $3.18 / P $3.10 ｜ ATM IV 18.1%，净 delta 敞口 -1.8M shares
Top ΔOI: P 736 +24,300 ｜ P 730 +16,119 ｜ C 760 +3,228
仓位参考: Max Pain 740 ｜ Call Wall 760（+2.9%，弱）（OI 3.9k） ｜ Put Wall 730（-1.1%，弱）（OI 30.8k）
量化解读： 存量 Put 重｜ATM IV 18.1%｜历史 Rank 64%（近端代理）｜IV/RV 1.24×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,793,459 股

📆 09-30 Forward Structure
存量OI: C 313.4k / P 545.6k，今日变化ΔOI: C -36.4k / P +21.1k，平值价格ATM: C $4.50 / P $4.43 ｜ ATM IV 19.4%，净 delta 敞口 -4.7M shares
Top ΔOI: P 736 +11,352 ｜ C 725 -10,884 ｜ C 726 -9,629
仓位参考: Max Pain 726 ｜ Call Wall 726（-1.7%）（OI 35.5k） ｜ Put Wall 720（-2.5%，弱）（OI 47.2k）
量化解读： 存量 Put 重｜ATM IV 19.4%｜历史 Rank 64%（近端代理）｜IV/RV 1.33×（近似）｜净 delta 敞口 负 4,701,594 股

📆 10-01 Forward Structure
存量OI: C 38.4k / P 51.9k，今日变化ΔOI: C +8.1k / P +7.8k，平值价格ATM: C $5.61 / P $5.39 ｜ ATM IV 19.5%，净 delta 敞口 -132k shares
Top ΔOI: C 764 +2,486 ｜ C 751 +1,269 ｜ P 713 +1,006
仓位参考: Max Pain 740 ｜ Call Wall 740（+0.2%）（OI 6.1k） ｜ Put Wall 740（+0.2%，弱）（OI 4.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 19.5%｜历史 Rank 64%（近端代理）｜IV/RV 1.33×（近似）｜净 delta 敞口 负 132,006 股

📆 10-02 Forward Structure
存量OI: C 197.4k / P 383.8k，今日变化ΔOI: C +47.9k / P +83.7k，平值价格ATM: C $6.49 / P $6.01 ｜ ATM IV 19.6%，净 delta 敞口 -855k shares
Top ΔOI: C 754 +11,162 ｜ C 760 +8,715
仓位参考: Max Pain 730 ｜ Call Wall 725（-1.8%）（OI 34.3k） ｜ Put Wall 730（-1.1%，弱）（OI 51.1k）
量化解读： 存量 Put 重｜ATM IV 19.6%｜历史 Rank 64%（近端代理）｜IV/RV 1.34×（近似）｜净 delta 敞口 负 854,843 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=29 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=29）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/QQQ_morning.json