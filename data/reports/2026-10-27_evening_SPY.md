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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-28 793C ΔOI +7,272（距现价 +3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 767.34 → 收盘 769.66（+0.3%） ｜ 今日高 771.13 ｜ 低 765.21 ｜ 昨收 765.37 → 收盘 769.66（+0.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.99 | OI比 1.48 | ATM IV 11.7% | Skew 0.9pp | Term 1.19 | ExpMove ±0.7%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构正常偏陡（Term 1.19）｜保护溢价薄（Skew 0.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.99×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.48×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 45% ｜ P/C OI(近端) 22%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 45%）｜近端持仓结构中性（P/C OI 分位 22%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-28（1D）±0.7% ｜ 10-29（2D）±1.0% ｜ 10-30（3D）±1.2% ｜ 11-02（6D）±1.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -472,540,329 | GEX Change vs 上次快照 612,688,561 | Flip: Primary Flip: 773.28（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 3039 / LOW 368 / INVALID 1389
结构观察区: Primary Flip 773.28（全链重定价，覆盖 95%）
最近结构参考: Flip 773（现价低于该位 0.5%）
量化视角： 负 Gamma（4.73亿，历史分位 45%，中性区）｜负 Gamma 缓解（+6.13亿）｜现价位于 Flip 下方 0.47%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 767（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 773（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 755.0P — Vol 66,604 | 最新价 $2.06 | OI 23470→150938 (ΔOI +127468张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增127468张（+543.1% vs前日OI），连续性待观察（方向未知）
10-30 745.0P — Vol 63,266 | 最新价 $0.83 | OI 81237→157799 (ΔOI +76562张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增76562张（+94.2% vs前日OI），连续性待观察（方向未知）
11-20 722.0P — Vol 17,231 | 最新价 $2.88 | OI 6260→24947 (ΔOI +18687张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18687张（+298.5% vs前日OI），连续性待观察（方向未知）
11-20 700.0P — Vol 970 | 最新价 $1.71 | OI 75322→87048 (ΔOI +11726张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增11726张（+15.6% vs前日OI），值得跟踪（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 234,443 张（Put 234,443 / Call 0），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $34M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-28  C +38.2k / P +35.4k ｜ Activity HIGH ｜ 1D
10-29  C +5.6k / P +40.8k ｜ Activity HIGH ｜ 2D
10-30  C +28.7k / P -44.4k ｜ Activity MEDIUM △ ｜ 3D
11-02  C +8.1k / P +12.2k ｜ Activity HIGH ｜ 6D

📆 10-28 Forward Structure
存量OI: C 100.0k / P 135.7k，今日变化ΔOI: C +38.2k / P +35.4k，平值价格ATM: C $2.64 / P $2.60 ｜ ATM IV 16.2%，净 delta 敞口 519k shares
Top ΔOI: C 793 +7,272 ｜ C 792 +6,725 ｜ P 760 +3,991
仓位参考: Max Pain 767 ｜ Call Wall 792（+2.9%，弱）（OI 7.4k） ｜ Put Wall 760（-1.3%，弱）（OI 7.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 16.2%｜历史 Rank 40%（近端代理）｜IV/RV 1.77×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 519,255 股

📆 10-29 Forward Structure
存量OI: C 43.6k / P 120.8k，今日变化ΔOI: C +5.6k / P +40.8k，平值价格ATM: C $3.79 / P $3.61 ｜ ATM IV 16.2%，净 delta 敞口 -84k shares
Top ΔOI: P 758 +15,538 ｜ P 748 +14,873 ｜ P 715 +1,645
仓位参考: Max Pain 766 ｜ Call Wall 790（+2.6%，弱）（OI 3.0k） ｜ Put Wall 748（-2.8%，弱）（OI 17.8k）
量化解读： 存量 Put 重｜ATM IV 16.2%｜历史 Rank 40%（近端代理）｜IV/RV 1.77×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 84,293 股

10-30（MEDIUM △）Top ΔOI: 755P -55,030 ｜ 745P -50,387
10-30（MEDIUM △）仓位参考: Max Pain 765 ｜ Call Wall 780（+1.3%，弱）（OI 27.1k） ｜ Put Wall 755（-1.9%，弱）（OI 95.9k）

📆 11-02 Forward Structure
存量OI: C 27.6k / P 41.0k，今日变化ΔOI: C +8.1k / P +12.2k，平值价格ATM: C $5.41 / P $4.86 ｜ ATM IV 12.9%，净 delta 敞口 98k shares
Top ΔOI: P 759 +2,159 ｜ P 765 +1,624 ｜ C 806 +1,488
仓位参考: Max Pain 765 ｜ Call Wall 791（+2.8%，弱）（OI 1.7k） ｜ Put Wall 750（-2.6%，弱）（OI 4.8k）
量化解读： 存量 Put 重｜ATM IV 12.9%｜历史 Rank 40%（近端代理）｜IV/RV 1.41×（近似）｜净 delta 敞口 正 97,628 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/SPY_evening.json