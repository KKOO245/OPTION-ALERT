# 期权晚报 2026-11-16（快照 16:40 ET）

📊 市场环境

SPY $739.95 ｜ QQQ $661.75
VIX 22.91 ↑18.7%（5D +15.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.8
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🟡 **近现价集中开仓**: 11-17 655P ΔOI +2,715（距现价 -1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 671.05 → 收盘 661.75（-1.4%） ｜ 今日高 672.14 ｜ 低 660.48 ｜ 昨收 679.89 → 收盘 661.75（-2.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-19，窗口结束前不做对错判定）

Options: P/C成交量 1.02 | OI比 1.38 | ATM IV 26.4% | Skew 2.3pp | Term 1.09 | ExpMove ±1.6%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构正常（Term 1.09）｜保护溢价中性（Skew 2.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.02×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.38×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 16% ｜ P/C OI(近端) 27%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 16%）｜近端持仓结构中性（P/C OI 分位 27%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-17（1D）±1.6% ｜ 11-18（2D）±2.4% ｜ 11-19（3D）±3.0% ｜ 11-20（4D）±3.4%
   ⇒ IV–VIX Spread: +3.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -614,067,892 | GEX Change vs 上次快照 -13,790,573 | Flip: Primary Flip: 685.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 3473 / LOW 487 / INVALID 1468
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 685.90（全链重定价，覆盖 94%）
Put Wall 680（弱结构｜现价低于该位 2.7%）
最近结构参考: Put Wall 680（现价低于该位 2.7%）
量化视角： 负 Gamma（6.14亿，历史分位偏负区，比 84% 的交易日更负）｜负 Gamma 加深（1379万）｜现价位于 Flip 下方 3.52%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 680（Put Wall，弱结构） / 680（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 686（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-30 550.0P — Vol 365 | 最新价 $0.63 | OI 6387→16334 (ΔOI +9947张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9947张（+155.7% vs前日OI），连续性待观察（方向未知）
11-20 703.0C — Vol 756 | 最新价 $0.47 | OI 1498→8273 (ΔOI +6775张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6775张（+452.3% vs前日OI），连续性待观察（方向未知）
量化视角： 2 个事件合计 ΔOI ≈ 16,722 张（Put 9,947 / Call 6,775），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-17  C +12.4k / P +21.4k ｜ Activity HIGH ｜ 1D
11-18  C +12.6k / P +15.5k ｜ Activity HIGH ｜ 2D
11-19  C +14.2k / P +15.5k ｜ Activity HIGH ｜ 3D
11-20  C +43.0k / P +59.0k ｜ Activity HIGH ｜ 4D

📆 11-17 Forward Structure
存量OI: C 55.6k / P 80.4k，今日变化ΔOI: C +12.4k / P +21.4k，平值价格ATM: C $5.53 / P $5.40 ｜ ATM IV 39.2%，净 delta 敞口 -600k shares
Top ΔOI: P 655 +2,715 ｜ P 659 +2,555 ｜ P 656 +2,480
仓位参考: Max Pain 680 ｜ Put Wall 680（+2.8%）（OI 5.6k）
量化解读： 存量 Put 重｜ATM IV 39.2%｜历史 Rank 81%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 负 600,398 股

📆 11-18 Forward Structure
存量OI: C 37.4k / P 78.7k，今日变化ΔOI: C +12.6k / P +15.5k，平值价格ATM: C $8.17 / P $7.94 ｜ ATM IV 41.1%，净 delta 敞口 -357k shares
Top ΔOI: P 650 +5,031 ｜ P 660 +1,637 ｜ C 700 +1,615
仓位参考: Max Pain 678 ｜ Call Wall 678（+2.5%，弱）（OI 2.0k） ｜ Put Wall 650（-1.8%，弱）（OI 5.6k）
量化解读： 存量 Put 重｜ATM IV 41.1%｜历史 Rank 81%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 357,159 股

📆 11-19 Forward Structure
存量OI: C 31.2k / P 55.0k，今日变化ΔOI: C +14.2k / P +15.5k，平值价格ATM: C $9.97 / P $9.61 ｜ ATM IV 40.7%，净 delta 敞口 -448k shares
Top ΔOI: C 705 +6,548 ｜ P 664 +4,992 ｜ C 725 +1,768
仓位参考: Max Pain 680 ｜ Put Wall 664（+0.3%，弱）（OI 5.1k）
量化解读： 存量 Put 重｜ATM IV 40.7%｜历史 Rank 81%（近端代理）｜IV/RV 1.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 448,165 股

📆 11-20 Forward Structure
存量OI: C 1055.0k / P 1032.3k，今日变化ΔOI: C +43.0k / P +59.0k，平值价格ATM: C $11.39 / P $10.82 ｜ ATM IV 39.8%，净 delta 敞口 244k shares
Top ΔOI: C 703 +6,775 ｜ P 530 +6,569
仓位参考: Max Pain 696 ｜ Call Wall 680（+2.8%，弱）（OI 35.6k） ｜ Put Wall 680（+2.8%）（OI 86.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 39.8%｜历史 Rank 81%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 正 243,699 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/QQQ_evening.json