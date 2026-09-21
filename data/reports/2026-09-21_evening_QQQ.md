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
🟡 **近现价集中开仓**: 09-22 731C ΔOI +3,845（距现价 -1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 727.95 → 收盘 741.47（+1.9%） ｜ 今日高 743.22 ｜ 低 727.82 ｜ 昨收 721.45 → 收盘 741.47（+2.8%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-09-24，窗口结束前不做对错判定）

Options: P/C成交量 1.10 | OI比 1.81 | ATM IV 13.4% | Skew -0.0pp | Term 1.33 | ExpMove ±0.7%（近端） | Rank 20%
量化视角： IV 历史低位（Rank 20%，期权偏便宜）｜期限结构正常偏陡（Term 1.33）｜Put 保护异常便宜（Skew -0.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.10×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.81×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 91% ｜ P/C OI(近端) 64%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 91%）｜近端持仓结构中性（P/C OI 分位 64%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-22（1D）±0.7% ｜ 09-23（2D）±0.9% ｜ 09-24（3D）±1.2% ｜ 09-25（4D）±1.4%
   ⇒ IV–VIX Spread: -1.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 560,748,914 | GEX Change vs 上次快照 -285,826,913 | Flip: Primary Flip: 720.54（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 3142 / LOW 273 / INVALID 1841
结构观察区: Primary Flip 720.54（全链重定价，覆盖 94%）
Call Wall 725（弱结构｜现价高于该位 2.3%）
最近结构参考: Call Wall 725（现价高于该位 2.3%）
量化视角： 正 Gamma（5.61亿，历史分位偏正区，比 91% 的交易日更正）｜正 Gamma 减弱（2.86亿）｜现价位于 Flip 上方 2.90%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 719（MaxPain，仅结算参考） / 725（Call Wall，弱结构）。
• Gamma 区域：切换参考 721（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 705.0P — Vol 3,586 | 最新价 $0.30 | OI 3066→32706 (ΔOI +29640张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29640张（+966.7% vs前日OI），连续性待观察（方向未知）
10-02 725.0C — Vol 781 | 最新价 $21.13 | OI 11487→34735 (ΔOI +23248张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23248张（+202.4% vs前日OI），连续性待观察（方向未知）
10-16 695.0P — Vol 4,152 | 最新价 $2.74 | OI 24205→37683 (ΔOI +13478张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13478张（+55.7% vs前日OI），连续性待观察（方向未知）
10-16 705.0P — Vol 2,783 | 最新价 $3.72 | OI 30645→43833 (ΔOI +13188张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13188张（+43.0% vs前日OI），连续性待观察（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 79,554 张（Put 56,306 / Call 23,248），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $9M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-22  C +21.0k / P +23.5k ｜ Activity HIGH ｜ 1D
09-23  C +21.7k / P +12.3k ｜ Activity HIGH ｜ 2D
09-24  C +10.2k / P +4.6k ｜ Activity HIGH ｜ 3D
09-25  C +28.8k / P +46.8k ｜ Activity HIGH ｜ 4D

📆 09-22 Forward Structure
存量OI: C 60.5k / P 64.0k，今日变化ΔOI: C +21.0k / P +23.5k，平值价格ATM: C $2.64 / P $2.36 ｜ ATM IV 16.0%，净 delta 敞口 1.9M shares
Top ΔOI: C 731 +3,845 ｜ C 732 +2,703 ｜ C 730 +2,235
仓位参考: Max Pain 718 ｜ Call Wall 731（-1.4%，弱）（OI 4.8k） ｜ Put Wall 720（-2.9%，弱）（OI 1.4k）
量化解读： 存量两侧均衡｜ATM IV 16.0%｜历史 Rank 20%（近端代理）｜IV/RV 1.36×（近似）｜净 delta 敞口 正 1,887,931 股

📆 09-23 Forward Structure
存量OI: C 45.5k / P 49.2k，今日变化ΔOI: C +21.7k / P +12.3k，平值价格ATM: C $3.70 / P $3.35 ｜ ATM IV 16.1%，净 delta 敞口 1.8M shares
Top ΔOI: C 720 +8,604 ｜ P 699 +2,528 ｜ P 696 +2,418
仓位参考: Max Pain 717 ｜ Call Wall 720（-2.9%）（OI 10.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 16.1%｜历史 Rank 20%（近端代理）｜IV/RV 1.37×（近似）｜净 delta 敞口 正 1,813,683 股

📆 09-24 Forward Structure
存量OI: C 27.1k / P 40.2k，今日变化ΔOI: C +10.2k / P +4.6k，平值价格ATM: C $4.58 / P $4.26 ｜ ATM IV 16.5%，净 delta 敞口 777k shares
Top ΔOI: C 732 +4,300 ｜ C 730 +1,402 ｜ C 735 +669
仓位参考: Max Pain 716 ｜ Call Wall 732（-1.3%）（OI 4.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 16.5%｜历史 Rank 20%（近端代理）｜IV/RV 1.40×（近似）｜净 delta 敞口 正 776,905 股

📆 09-25 Forward Structure
存量OI: C 121.0k / P 359.4k，今日变化ΔOI: C +28.8k / P +46.8k，平值价格ATM: C $5.54 / P $4.95 ｜ ATM IV 16.8%，净 delta 敞口 1.7M shares
Top ΔOI: P 705 +29,640 ｜ P 665 -18,605 ｜ P 690 -9,335
仓位参考: Max Pain 718 ｜ Call Wall 730（-1.5%）（OI 11.1k）
量化解读： 存量 Put 重｜ATM IV 16.8%｜历史 Rank 20%（近端代理）｜IV/RV 1.43×（近似）｜净 delta 敞口 正 1,718,567 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/QQQ_evening.json