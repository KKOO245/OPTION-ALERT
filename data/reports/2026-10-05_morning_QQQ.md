# 期权晨报 2026-10-05（快照 10:20 ET）

📊 市场环境

SPY $774.78 ｜ QQQ $756.20
VIX 15.75 ↑2.9%（5D -2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 43.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 10-05 10:00　【高】ISM 非制造业 PMI　预测 55 ｜ 实际 54.9 ｜ 前值 55.4　✅ 今日已公布
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-06 740P ΔOI +24,771（距现价 -1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-06 740P ΔOI +24,771 占该期限总 OI 18.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 749.58 → 今开 749.34（-0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 753.46 ｜ 低 749.08

Options: P/C成交量 0.86 | OI比 2.51 | ATM IV 19.0% | Skew 2.5pp | Term 1.02 | ExpMove ±0.8%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构正常（Term 1.02）｜保护溢价中性（Skew 2.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.86×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.51×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 84% ｜ P/C OI(近端) 92%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 84%）｜近端 Put 显著偏重（P/C OI 分位 92%，历史高位区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-06（1D）±0.8% ｜ 10-07（2D）±1.1% ｜ 10-08（3D）±1.3% ｜ 10-09（4D）±1.5%
   ⇒ IV–VIX Spread: +3.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 385,577,696 | GEX Change vs 上次快照 -33,900,559 | Flip: Primary Flip: 746.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 3148 / LOW 245 / INVALID 1781
结构观察区: Primary Flip 746.89（全链重定价，覆盖 98%）
Call Wall 760（现价低于该位 1.1%）
最近结构参考: Flip 747（现价高于该位 0.7%）
量化视角： 正 Gamma（3.86亿，历史分位偏正区，比 84% 的交易日更正）｜正 Gamma 减弱（3390万）｜现价位于 Flip 上方 0.67%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 749（MaxPain，仅结算参考）；上方 760（Call Wall）。
• Gamma 区域：切换参考 747（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 480.0P — Vol 26,760 | 最新价 $0.03 | OI 516→26689 (ΔOI +26173张) | ΔOI/Volume 97.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26173张（+5072.3% vs前日OI），连续性待观察（方向未知）
10-06 740.0P — Vol 29,723 | 最新价 $1.20 | OI 759→25530 (ΔOI +24771张) | ΔOI/Volume 83.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24771张（+3263.6% vs前日OI），连续性待观察（方向未知）
10-05 560.0P — Vol 10,178 | 最新价 $0.01 | OI 1006→10608 (ΔOI +9602张) | ΔOI/Volume 94.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9602张（+954.5% vs前日OI），连续性待观察（方向未知）
10-16 780.0C — Vol 14,560 | 最新价 $1.01 | OI 11414→19826 (ΔOI +8412张) | ΔOI/Volume 57.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8412张（+73.7% vs前日OI），连续性待观察（方向未知）
10-09 515.0P — Vol 10,058 | 最新价 $0.03 | OI 231→8169 (ΔOI +7938张) | ΔOI/Volume 78.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7938张（+3436.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 76,896 张（Put 68,484 / Call 8,412），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 115.6k / P 289.9k，今日成交量: C 427.0k / P 377.8k，平值价格ATM: C $1.38 / P $1.69 ｜ ATM IV 19.0%，预期波动 ±0.4%，Max Pain 749
Top ΔOI: P 560 +9,602 ｜ P 736 -6,712 ｜ P 748 +6,178

📆 Forward Expiration Structure

10-06  C +10.4k / P +43.7k ｜ Activity HIGH ｜ 1D
10-07  C +10.3k / P +18.9k ｜ Activity HIGH ｜ 2D
10-08  C +4.5k / P +14.3k ｜ Activity HIGH ｜ 3D
10-09  C +19.9k / P +79.5k ｜ Activity HIGH ｜ 4D

📆 10-06 Forward Structure
存量OI: C 33.7k / P 103.3k，今日变化ΔOI: C +10.4k / P +43.7k，平值价格ATM: C $2.80 / P $3.05 ｜ ATM IV 16.6%，净 delta 敞口 -243k shares
Top ΔOI: P 740 +24,771 ｜ P 738 +1,898 ｜ P 749 +1,296
仓位参考: Max Pain 745 ｜ Call Wall 770（+2.4%，弱）（OI 2.9k） ｜ Put Wall 740（-1.6%）（OI 25.5k）
量化解读： 存量 Put 重｜ATM IV 16.6%｜历史 Rank 54%（近端代理）｜IV/RV 1.16×（近似）｜净 delta 敞口 负 242,867 股

📆 10-07 Forward Structure
存量OI: C 38.3k / P 77.6k，今日变化ΔOI: C +10.3k / P +18.9k，平值价格ATM: C $3.90 / P $4.09 ｜ ATM IV 16.7%，净 delta 敞口 -29k shares
Top ΔOI: C 760 +3,818 ｜ P 738 +1,388
仓位参考: Max Pain 743 ｜ Call Wall 760（+1.1%）（OI 5.4k）
量化解读： 存量 Put 重｜ATM IV 16.7%｜历史 Rank 54%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 负 28,759 股

📆 10-08 Forward Structure
存量OI: C 20.3k / P 57.5k，今日变化ΔOI: C +4.5k / P +14.3k，平值价格ATM: C $4.70 / P $4.81 ｜ ATM IV 16.8%，净 delta 敞口 -56k shares
Top ΔOI: P 721 +2,331 ｜ P 749 +2,202 ｜ C 755 +1,097
仓位参考: Max Pain 745 ｜ Call Wall 740（-1.6%，弱）（OI 1.5k） ｜ Put Wall 749（-0.4%，弱）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 16.8%｜历史 Rank 54%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 负 55,852 股

📆 10-09 Forward Structure
存量OI: C 151.9k / P 255.0k，今日变化ΔOI: C +19.9k / P +79.5k，平值价格ATM: C $5.64 / P $5.49 ｜ ATM IV 17.1%，净 delta 敞口 -665k shares
Top ΔOI: P 749 +7,132 ｜ P 681 +4,636
仓位参考: Max Pain 742 ｜ Call Wall 754（+0.3%）（OI 21.1k） ｜ Put Wall 730（-2.9%，弱）（OI 26.9k）
量化解读： 存量 Put 重｜ATM IV 17.1%｜历史 Rank 54%（近端代理）｜IV/RV 1.20×（近似）｜净 delta 敞口 负 664,920 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime RANGE | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/QQQ_morning.json