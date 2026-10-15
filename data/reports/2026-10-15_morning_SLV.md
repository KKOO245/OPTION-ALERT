# 期权晨报 2026-10-15（快照 10:20 ET）

📊 市场环境

SPY $770.81 ｜ QQQ $723.66
VIX 17.51 ↑3.8%（5D +13.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.9（fear）
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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-16 51C ΔOI +4,377（距现价 -0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 50.22 → 今开 51.25（+2.1%） | 较昨收变动（含盘初走势） ｜ 今日高 51.38 ｜ 低 50.97

Options: P/C成交量 0.49 | OI比 0.37 | ATM IV 39.6% | Skew 2.3pp | Term 0.90 | ExpMove ±1.8%（近端） | Rank 65%
量化视角： IV 中性（Rank 65%）｜期限结构正常（Term 0.90）｜保护溢价中性（Skew 2.3pp）｜存量 Call 偏重（OI比 0.37）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.37×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（1D）±1.8% ｜ 10-19（4D）±2.6% ｜ 10-21（6D）±3.5% ｜ 10-23（8D）±4.1%
   ⇒ IV–VIX Spread: +22.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 31,620,671 | GEX Change vs 上次快照 33,953,525 | Flip: Primary Flip: 49.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 778 / LOW 149 / INVALID 321
结构观察区: Primary Flip 49.77（全链重定价，覆盖 96%）
Put Wall 50（弱结构｜现价高于该位 2.1%）
最近结构参考: Put Wall 50（现价高于该位 2.1%）
量化视角： 正 Gamma（3162万，无历史分位）｜由负转正（+3395万）｜现价位于 Flip 上方 2.62%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构）；上方 55（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 50（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 51.0C — Vol 7,996 | 最新价 $0.35 | OI 820→5197 (ΔOI +4377张) | ΔOI/Volume 54.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4377张（+533.8% vs前日OI），连续性待观察（方向未知）
10-23 55.0C — Vol 4,415 | 最新价 $0.13 | OI 1616→5466 (ΔOI +3850张) | ΔOI/Volume 87.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3850张（+238.2% vs前日OI），连续性待观察（方向未知）
10-16 49.0P — Vol 3,996 | 最新价 $0.27 | OI 1112→3332 (ΔOI +2220张) | ΔOI/Volume 55.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2220张（+199.6% vs前日OI），连续性待观察（方向未知）
10-16 51.5C — Vol 4,233 | 最新价 $0.21 | OI 39→2259 (ΔOI +2220张) | ΔOI/Volume 52.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2220张（+5692.3% vs前日OI），连续性待观察（方向未知）
10-16 52.0C — Vol 4,904 | 最新价 $0.13 | OI 2622→4793 (ΔOI +2171张) | ΔOI/Volume 44.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2171张（+82.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,838 张（Put 2,220 / Call 12,618），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +15.5k / P -15.7k ｜ Activity MEDIUM △ ｜ 1D
10-19  C +3.1k / P +2.8k ｜ Activity HIGH ｜ 4D
10-21  C +4.3k / P +2.7k ｜ Activity HIGH ｜ 6D
10-23  C +12.4k / P +5.4k ｜ Activity HIGH ｜ 8D

📆 10-16 Forward Structure
存量OI: C 490.5k / P 180.8k，今日变化ΔOI: C +15.5k / P -15.7k，平值价格ATM: C $0.53 / P $0.41 ｜ ATM IV 39.6%，净 delta 敞口 2.7M shares
Top ΔOI: P 59 -6,746 ｜ P 60 -6,638 ｜ C 51 +4,377
仓位参考: Max Pain 55 ｜ Call Wall 50（-2.1%，弱）（OI 27.9k） ｜ Put Wall 50（-2.1%，弱）（OI 24.0k）
量化解读： 存量 Call 重｜ATM IV 39.6%｜历史 Rank 65%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,707,005 股

📆 10-19 Forward Structure
存量OI: C 9.0k / P 6.1k，今日变化ΔOI: C +3.1k / P +2.8k，平值价格ATM: C $0.72 / P $0.61 ｜ ATM IV 30.4%，净 delta 敞口 133k shares
Top ΔOI: C 51 +834 ｜ C 51 +621 ｜ P 48 +512
仓位参考: Max Pain 52 ｜ Call Wall 53（+3.8%）（OI 1.3k） ｜ Put Wall 49.5（-3.1%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 30.4%｜历史 Rank 65%（近端代理）｜IV/RV 0.82×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 132,536 股

📆 10-21 Forward Structure
存量OI: C 10.0k / P 5.2k，今日变化ΔOI: C +4.3k / P +2.7k，平值价格ATM: C $1.05 / P $0.73 ｜ ATM IV 32.9%，净 delta 敞口 73k shares
Top ΔOI: C 51 +905 ｜ P 49 +547
仓位参考: Max Pain 51 ｜ Call Wall 51（-0.1%，弱）（OI 0.9k） ｜ Put Wall 49（-4.1%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 32.9%｜历史 Rank 65%（近端代理）｜IV/RV 0.88×（近似）｜净 delta 敞口 正 73,155 股

📆 10-23 Forward Structure
存量OI: C 57.4k / P 40.5k，今日变化ΔOI: C +12.4k / P +5.4k，平值价格ATM: C $1.12 / P $0.99 ｜ ATM IV 34.2%，净 delta 敞口 293k shares
Top ΔOI: C 55 +3,850 ｜ C 50 +2,079 ｜ C 51 +1,861
仓位参考: Max Pain 55 ｜ Call Wall 55（+7.7%，弱）（OI 5.5k） ｜ Put Wall 50（-2.1%，弱）（OI 3.6k）
量化解读： 存量 Call 重｜ATM IV 34.2%｜历史 Rank 65%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 正 292,812 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 39.6% vs 10-19 30.4%（差 +9.1pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/SLV_morning.json