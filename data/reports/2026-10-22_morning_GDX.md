# 期权晨报 2026-10-22（快照 10:20 ET）

📊 市场环境

SPY $766.63 ｜ QQQ $710.93
VIX 17.91 ↑7.4%（5D +8.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-23 87C ΔOI +1,283（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 86.72 → 今开 83.85（-3.3%） | 较昨收变动（含盘初走势） ｜ 今日高 83.89 ｜ 低 82.68

Options: P/C成交量 0.01 | OI比 0.34 | ATM IV 51.9% | Skew 2.6pp | Term 0.80 | ExpMove ±2.5%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价中性（Skew 2.6pp）｜存量 Call 偏重（OI比 0.34）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.01×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.34×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（1D）±2.5% ｜ 10-26（4D）±4.4% ｜ 10-28（6D）±5.4% ｜ 10-30（8D）±7.0%
   ⇒ IV–VIX Spread: +33.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -24,164,801 | GEX Change vs 上次快照 -55,407,918 | Flip: Primary Flip: 84.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 568 / LOW 152 / INVALID 428
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 84.68（全链重定价，覆盖 96%）
Put Wall 80（弱结构｜现价高于该位 4.0%）
最近结构参考: Flip 85（现价低于该位 1.7%）
量化视角： 负 Gamma（2416万，无历史分位）｜由正转负（5541万）｜现价位于 Flip 下方 1.71%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（Put Wall，弱结构）；上方 86（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 85（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 60.0P — Vol 3,000 | 最新价 $0.03 | OI 3014→6014 (ΔOI +3000张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3000张（+99.5% vs前日OI），连续性待观察（方向未知）
10-23 87.0C — Vol 2,158 | 最新价 $1.04 | OI 1071→2354 (ΔOI +1283张) | ΔOI/Volume 59.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1283张（+119.8% vs前日OI），连续性待观察（方向未知）
11-20 92.5C — Vol 850 | 最新价 $1.93 | OI 6→853 (ΔOI +847张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增847张（+14116.7% vs前日OI），连续性待观察（方向未知）
10-23 88.0C — Vol 1,160 | 最新价 $0.61 | OI 9773→10300 (ΔOI +527张) | ΔOI/Volume 45.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增527张（+5.4% vs前日OI），连续性待观察（方向未知）
10-23 86.5C — Vol 663 | 最新价 $0.65 | OI 180→582 (ΔOI +402张) | ΔOI/Volume 60.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增402张（+223.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,059 张（Put 3,000 / Call 3,059），跨 3 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C -1.8k / P -0.7k ｜ Activity HIGH ｜ 1D
10-26  C +0.4k / P +81 ｜ Activity MEDIUM △ ｜ 4D
10-28  C +0.2k / P +0.2k ｜ Activity MEDIUM △ ｜ 6D
10-30  C +0.1k / P +3.2k ｜ Activity HIGH ｜ 8D

📆 10-23 Forward Structure
存量OI: C 95.7k / P 32.8k，今日变化ΔOI: C -1.8k / P -0.7k，平值价格ATM: C $1.17 / P $0.91 ｜ ATM IV 51.8%，净 delta 敞口 65k shares
Top ΔOI: C 90 -2,323 ｜ C 87 +1,283
仓位参考: Max Pain 86 ｜ Call Wall 88（+5.7%，弱）（OI 10.3k） ｜ Put Wall 85（+2.1%，弱）（OI 5.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 51.8%｜历史 Rank 85%（近端代理）｜IV/RV 1.67×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 64,745 股

10-26（MEDIUM △）Top ΔOI: 89C +144 ｜ 88C +99
10-26（MEDIUM △）仓位参考: Max Pain 86 ｜ Put Wall 85（+2.1%，弱）（OI 0.2k）

10-28（MEDIUM △）Top ΔOI: 77P +149 ｜ 89C +101
10-28（MEDIUM △）仓位参考: Max Pain 87 ｜ Call Wall 88（+5.7%，弱）（OI 0.3k） ｜ Put Wall 84（+0.9%）（OI 2.1k）

📆 10-30 Forward Structure
存量OI: C 40.1k / P 19.0k，今日变化ΔOI: C +0.1k / P +3.2k，平值价格ATM: C $3.75 / P $2.05 ｜ ATM IV 44.6%，净 delta 敞口 -15k shares
Top ΔOI: P 84 +221
仓位参考: Max Pain 87 ｜ Call Wall 87（+4.5%，弱）（OI 5.7k） ｜ Put Wall 85（+2.1%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 44.6%｜历史 Rank 85%（近端代理）｜IV/RV 1.44×（近似）｜净 delta 敞口 负 15,187 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/GDX_morning.json