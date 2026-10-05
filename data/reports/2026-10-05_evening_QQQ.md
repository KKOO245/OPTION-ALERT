# 期权晚报 2026-10-05（快照 16:51 ET）

📊 市场环境

SPY $774.83 ｜ QQQ $756.20
VIX 15.52 ↑1.4%（5D -3.4%） ｜ Vol Regime: NORMAL
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
🟡 **近现价集中开仓**: 10-06 740P ΔOI +24,771（距现价 -2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-06 740P ΔOI +24,771 占该期限总 OI 18.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 749.34 → 收盘 756.20（+0.9%） ｜ 今日高 756.91 ｜ 低 749.08 ｜ 昨收 749.58 → 收盘 756.20（+0.9%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-10-08，窗口结束前不做对错判定）

Options: P/C成交量 1.34 | OI比 2.51 | ATM IV 10.4% | Skew 2.3pp | Term 1.84 | ExpMove ±0.6%（近端） | Rank 10%
量化视角： IV 历史低位（Rank 10%，期权偏便宜）｜期限结构正常偏陡（Term 1.84）｜保护溢价中性（Skew 2.3pp）｜当日成交偏 Put（P/C量 1.34）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.34×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.51×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 91% ｜ P/C OI(近端) 92%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 91%）｜近端 Put 显著偏重（P/C OI 分位 92%，历史高位区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-06（1D）±0.6% ｜ 10-07（2D）±0.9% ｜ 10-08（3D）±1.2% ｜ 10-09（4D）±1.4%
   ⇒ IV–VIX Spread: -5.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 552,283,703 | GEX Change vs 上次快照 166,706,007 | Flip: Primary Flip: 745.79（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2815 / LOW 293 / INVALID 2066
结构观察区: Primary Flip 745.79（全链重定价，覆盖 94%）
Call Wall 760（现价低于该位 0.5%）
最近结构参考: Call Wall 760（现价低于该位 0.5%）
量化视角： 正 Gamma（5.52亿，历史分位偏正区，比 91% 的交易日更正）｜正 Gamma 增强（+1.67亿）｜现价位于 Flip 上方 1.40%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 749（MaxPain，仅结算参考）；上方 760（Call Wall）。
• Gamma 区域：切换参考 746（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 480.0P — Vol 6 | 最新价 $0.03 | OI 516→26689 (ΔOI +26173张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26173张（+5072.3% vs前日OI），连续性待观察（方向未知）
10-06 740.0P — Vol 69,001 | 最新价 $0.08 | OI 759→25530 (ΔOI +24771张) | ΔOI/Volume 35.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24771张（+3263.6% vs前日OI），连续性待观察（方向未知）
10-16 780.0C — Vol 2,095 | 最新价 $1.36 | OI 11414→19826 (ΔOI +8412张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8412张（+73.7% vs前日OI），连续性待观察（方向未知）
10-09 515.0P — Vol 2,000 | 最新价 $0.01 | OI 231→8169 (ΔOI +7938张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7938张（+3436.4% vs前日OI），连续性待观察（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 67,294 张（Put 58,882 / Call 8,412），跨 3 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-06  C +10.4k / P +43.7k ｜ Activity HIGH ｜ 1D
10-07  C +10.3k / P +18.9k ｜ Activity HIGH ｜ 2D
10-08  C +4.5k / P +14.3k ｜ Activity HIGH ｜ 3D
10-09  C +19.9k / P +79.5k ｜ Activity HIGH ｜ 4D

📆 10-06 Forward Structure
存量OI: C 33.7k / P 103.3k，今日变化ΔOI: C +10.4k / P +43.7k，平值价格ATM: C $2.40 / P $2.28 ｜ ATM IV 14.6%，净 delta 敞口 250k shares
Top ΔOI: P 740 +24,771 ｜ P 738 +1,898 ｜ P 749 +1,296
仓位参考: Max Pain 745 ｜ Call Wall 770（+1.8%，弱）（OI 2.9k） ｜ Put Wall 740（-2.1%）（OI 25.5k）
量化解读： 存量 Put 重｜ATM IV 14.6%｜历史 Rank 10%（近端代理）｜IV/RV 1.03×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 250,262 股

📆 10-07 Forward Structure
存量OI: C 38.3k / P 77.6k，今日变化ΔOI: C +10.3k / P +18.9k，平值价格ATM: C $3.56 / P $3.35 ｜ ATM IV 15.4%，净 delta 敞口 188k shares
Top ΔOI: C 760 +3,818 ｜ P 738 +1,388
仓位参考: Max Pain 743 ｜ Call Wall 760（+0.5%）（OI 5.4k）
量化解读： 存量 Put 重｜ATM IV 15.4%｜历史 Rank 10%（近端代理）｜IV/RV 1.08×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 188,426 股

📆 10-08 Forward Structure
存量OI: C 20.3k / P 57.5k，今日变化ΔOI: C +4.5k / P +14.3k，平值价格ATM: C $4.50 / P $4.33 ｜ ATM IV 15.8%，净 delta 敞口 65k shares
Top ΔOI: P 721 +2,331 ｜ P 749 +2,202 ｜ C 755 +1,097
仓位参考: Max Pain 745 ｜ Call Wall 740（-2.1%，弱）（OI 1.5k） ｜ Put Wall 749（-1.0%，弱）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 15.8%｜历史 Rank 10%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 正 65,436 股

📆 10-09 Forward Structure
存量OI: C 151.9k / P 255.0k，今日变化ΔOI: C +19.9k / P +79.5k，平值价格ATM: C $5.43 / P $4.89 ｜ ATM IV 16.2%，净 delta 敞口 -156k shares
Top ΔOI: P 749 +7,132 ｜ P 681 +4,636
仓位参考: Max Pain 742 ｜ Call Wall 754（-0.3%）（OI 21.1k） ｜ Put Wall 749（-1.0%，弱）（OI 7.2k）
量化解读： 存量 Put 重｜ATM IV 16.2%｜历史 Rank 10%（近端代理）｜IV/RV 1.14×（近似）｜净 delta 敞口 负 155,579 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/QQQ_evening.json