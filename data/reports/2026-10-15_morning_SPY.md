# 期权晨报 2026-10-15（快照 10:20 ET）

📊 市场环境

SPY $771.79 ｜ QQQ $728.00
VIX 17.51 ↑3.8%（5D +13.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 775C ΔOI +9,455（距现价 +1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 769.60 → 今开 766.25（-0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 768.03 ｜ 低 764.44

Options: P/C成交量 1.41 | OI比 1.71 | ATM IV 21.8% | Skew 2.6pp | Term 0.64 | ExpMove ±0.8%（近端） | Rank 89%
量化视角： IV 历史高位（Rank 89%，期权偏贵）｜期限结构倒挂（Term 0.64，近月 IV 高于远月）｜保护溢价中性（Skew 2.6pp）｜当日成交偏 Put（P/C量 1.41）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.41×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.71×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 22% ｜ P/C OI(近端) 39%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 22%）｜近端持仓结构中性（P/C OI 分位 39%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-16（1D）±0.8% ｜ 10-19（4D）±1.0% ｜ 10-20（5D）±1.1% ｜ 10-21（6D）±1.3%
   ⇒ IV–VIX Spread: +4.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,614,123,558 | GEX Change vs 上次快照 -116,064,857 | Flip: Primary Flip: 774.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 2703 / LOW 282 / INVALID 1887
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 774.11（全链重定价，覆盖 98%）
最近结构参考: Flip 774（现价低于该位 1.0%）
量化视角： 负 Gamma（16.14亿，历史分位偏负区，比 78% 的交易日更负）｜负 Gamma 加深（1.16亿）｜现价位于 Flip 下方 0.96%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 770（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 774（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-15 772.0C — Vol 88,702 | 最新价 $1.18 | OI 1501→23849 (ΔOI +22348张) | ΔOI/Volume 25.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22348张（+1488.9% vs前日OI），连续性待观察（方向未知）
10-15 736.0P — Vol 42,819 | 最新价 $0.04 | OI 73→20377 (ΔOI +20304张) | ΔOI/Volume 47.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20304张（+27813.7% vs前日OI），连续性待观察（方向未知）
10-15 738.0P — Vol 22,708 | 最新价 $0.04 | OI 37914→55842 (ΔOI +17928张) | ΔOI/Volume 79.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17928张（+47.3% vs前日OI），连续性待观察（方向未知）
10-15 724.0P — Vol 14,079 | 最新价 $0.03 | OI 17→13916 (ΔOI +13899张) | ΔOI/Volume 98.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13899张（+81758.8% vs前日OI），连续性待观察（方向未知）
10-15 780.0C — Vol 38,910 | 最新价 $0.07 | OI 3798→17545 (ΔOI +13747张) | ΔOI/Volume 35.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13747张（+361.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 88,226 张（Put 52,131 / Call 36,095），跨 1 个期限｜彩票/名义 3 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 231.4k / P 395.5k，今日成交量: C 562.7k / P 794.2k，平值价格ATM: C $1.79 / P $1.83 ｜ ATM IV 21.8%，预期波动 ±0.5%，Max Pain 770
Top ΔOI: C 772 +22,348 ｜ P 736 +20,304 ｜ P 738 +17,928

📆 Forward Expiration Structure

10-16  C +63.4k / P +51.2k ｜ Activity HIGH ｜ 1D
10-19  C +26.6k / P +13.5k ｜ Activity HIGH ｜ 4D
10-20  C +26.2k / P +59.0k ｜ Activity HIGH ｜ 5D
10-21  C +25.6k / P +19.8k ｜ Activity HIGH ｜ 6D

📆 10-16 Forward Structure
存量OI: C 786.9k / P 2503.0k，今日变化ΔOI: C +63.4k / P +51.2k，平值价格ATM: C $3.18 / P $2.89 ｜ ATM IV 16.8%，净 delta 敞口 2.9M shares
Top ΔOI: C 775 +9,455 ｜ P 724 +9,004
仓位参考: Max Pain 770 ｜ Call Wall 785（+2.4%，弱）（OI 56.8k） ｜ Put Wall 750（-2.2%，弱）（OI 66.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 16.8%｜历史 Rank 89%（近端代理）｜IV/RV 2.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,859,478 股

📆 10-19 Forward Structure
存量OI: C 68.0k / P 93.9k，今日变化ΔOI: C +26.6k / P +13.5k，平值价格ATM: C $4.01 / P $3.73 ｜ ATM IV 11.6%，净 delta 敞口 -151k shares
Top ΔOI: P 747 -5,820 ｜ C 815 +3,000 ｜ P 749 +2,891
仓位参考: Max Pain 774 ｜ Call Wall 780（+1.7%，弱）（OI 4.4k） ｜ Put Wall 747（-2.6%，弱）（OI 9.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 11.6%｜历史 Rank 89%（近端代理）｜IV/RV 1.49×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 151,142 股

📆 10-20 Forward Structure
存量OI: C 44.4k / P 87.0k，今日变化ΔOI: C +26.2k / P +59.0k，平值价格ATM: C $4.63 / P $4.19 ｜ ATM IV 12.0%，净 delta 敞口 -706k shares
Top ΔOI: P 751 +12,343 ｜ P 752 +10,255 ｜ P 753 +8,272
仓位参考: Max Pain 774 ｜ Call Wall 789（+2.9%）（OI 4.5k） ｜ Put Wall 751（-2.0%，弱）（OI 12.5k）
量化解读： 存量 Put 重｜ATM IV 12.0%｜历史 Rank 89%（近端代理）｜IV/RV 1.54×（近似）｜净 delta 敞口 负 706,330 股

📆 10-21 Forward Structure
存量OI: C 39.8k / P 79.3k，今日变化ΔOI: C +25.6k / P +19.8k，平值价格ATM: C $5.27 / P $4.74 ｜ ATM IV 12.5%，净 delta 敞口 -59k shares
Top ΔOI: C 773 +2,433 ｜ C 788 +2,392 ｜ C 774 +1,576
仓位参考: Max Pain 773 ｜ Call Wall 788（+2.8%，弱）（OI 2.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 12.5%｜历史 Rank 89%（近端代理）｜IV/RV 1.60×（近似）｜净 delta 敞口 负 58,635 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 16.8% vs 10-19 11.6%（差 +5.2pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/SPY_morning.json