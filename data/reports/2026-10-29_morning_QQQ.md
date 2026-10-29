# 期权晨报 2026-10-29（快照 10:20 ET）

📊 市场环境

SPY $769.48 ｜ QQQ $716.11
VIX 16.74 ↓1.0%（5D -12.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 690P ΔOI -6,665（距现价 -3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 725.61 → 今开 716.57（-1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 716.99 ｜ 低 711.62

Options: P/C成交量 1.10 | OI比 1.94 | ATM IV 36.9% | Skew 3.1pp | Term 0.57 | ExpMove ±1.3%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.57，近月 IV 高于远月）｜保护溢价中性（Skew 3.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.10×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.94×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 14% ｜ P/C OI(近端) 73%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 14%）｜近端持仓结构中性（P/C OI 分位 73%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-30（1D）±1.3% ｜ 11-02（4D）±1.7% ｜ 11-03（5D）±2.0% ｜ 11-04（6D）±2.4%
   ⇒ IV–VIX Spread: +20.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -682,689,122 | GEX Change vs 上次快照 -596,129,058 | Flip: Primary Flip: 727.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 2683 / LOW 288 / INVALID 1055
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 727.14（全链重定价，覆盖 97%）
最近结构参考: Flip 727（现价低于该位 1.5%）
量化视角： 负 Gamma（6.83亿，历史分位偏负区，比 86% 的交易日更负）｜负 Gamma 加深（5.96亿）｜现价位于 Flip 下方 1.49%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 722（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 727（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 700.0P — Vol 16,415 | 最新价 $3.45 | OI 16789→23974 (ΔOI +7185张) | ΔOI/Volume 43.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7185张（+42.8% vs前日OI），连续性待观察（方向未知）
11-20 710.0P — Vol 9,227 | 最新价 $10.00 | OI 14377→20419 (ΔOI +6042张) | ΔOI/Volume 65.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6042张（+42.0% vs前日OI），连续性待观察（方向未知）
11-03 635.0P — Vol 5,839 | 最新价 $0.06 | OI 97→5882 (ΔOI +5785张) | ΔOI/Volume 99.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5785张（+5963.9% vs前日OI），连续性待观察（方向未知）
11-20 715.0C — Vol 30,176 | 最新价 $22.90 | OI 13109→18758 (ΔOI +5649张) | ΔOI/Volume 18.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5649张（+43.1% vs前日OI），连续性待观察（方向未知）
11-20 740.0C — Vol 6,762 | 最新价 $8.70 | OI 22077→27627 (ΔOI +5550张) | ΔOI/Volume 82.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5550张（+25.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 30,211 张（Put 19,012 / Call 11,199），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $9M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 96.9k / P 187.8k，今日成交量: C 412.7k / P 455.4k，平值价格ATM: C $3.21 / P $2.51 ｜ ATM IV 36.9%，预期波动 ±0.8%，Max Pain 722
Top ΔOI: P 710 +5,248 ｜ C 733 +4,736 ｜ P 720 +3,530

📆 Forward Expiration Structure

10-30  C +7.8k / P +9.7k ｜ Activity MEDIUM △ ｜ 1D
11-02  C +6.3k / P +15.1k ｜ Activity HIGH ｜ 4D
11-03  C +2.5k / P +14.9k ｜ Activity HIGH ｜ 5D
11-04  C +3.0k / P +6.2k ｜ Activity HIGH ｜ 6D

📆 10-30 Forward Structure
存量OI: C 396.3k / P 809.4k，今日变化ΔOI: C +7.8k / P +9.7k，平值价格ATM: C $5.10 / P $4.18 ｜ ATM IV 27.4%，净 delta 敞口 -412k shares
Top ΔOI: P 690 -6,665 ｜ P 700 -5,828
仓位参考: Max Pain 723 ｜ Call Wall 730（+1.9%，弱）（OI 19.8k） ｜ Put Wall 700（-2.3%，弱）（OI 42.1k）
量化解读： 存量 Put 重｜ATM IV 27.4%｜历史 Rank 96%（近端代理）｜IV/RV 1.48×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 411,843 股

📆 11-02 Forward Structure
存量OI: C 47.8k / P 65.6k，今日变化ΔOI: C +6.3k / P +15.1k，平值价格ATM: C $6.44 / P $5.59 ｜ ATM IV 19.3%，净 delta 敞口 -296k shares
Top ΔOI: P 703 +5,113 ｜ P 670 -2,673 ｜ P 715 +2,022
仓位参考: Max Pain 719 ｜ Call Wall 725（+1.2%，弱）（OI 8.3k） ｜ Put Wall 695（-3.0%，弱）（OI 7.0k）
量化解读： 存量 Put 重｜ATM IV 19.3%｜历史 Rank 96%（近端代理）｜IV/RV 1.04×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 295,739 股

📆 11-03 Forward Structure
存量OI: C 23.1k / P 52.5k，今日变化ΔOI: C +2.5k / P +14.9k，平值价格ATM: C $7.42 / P $6.66 ｜ ATM IV 20.2%，净 delta 敞口 -44k shares
Top ΔOI: P 675 +1,364
仓位参考: Max Pain 714 ｜ Call Wall 710（-0.9%）（OI 2.7k）
量化解读： 存量 Put 重｜ATM IV 20.2%｜历史 Rank 96%（近端代理）｜IV/RV 1.09×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 44,493 股

📆 11-04 Forward Structure
存量OI: C 16.7k / P 29.3k，今日变化ΔOI: C +3.0k / P +6.2k，平值价格ATM: C $8.65 / P $8.18 ｜ ATM IV 22.0%，净 delta 敞口 -149k shares
Top ΔOI: P 700 +970 ｜ P 722 +502 ｜ P 665 +447
仓位参考: Max Pain 720 ｜ Call Wall 730（+1.9%，弱）（OI 0.9k） ｜ Put Wall 715（-0.2%，弱）（OI 3.7k）
量化解读： 存量 Put 重｜ATM IV 22.0%｜历史 Rank 96%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 负 149,395 股

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 27.4% vs 11-02 19.3%（差 +8.1pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/QQQ_morning.json