# 期权晨报 2026-11-19（快照 10:20 ET）

📊 市场环境

SPY $714.27 ｜ QQQ $645.04
VIX 22.66 ↓7.7%（5D +21.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 18.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-27 114C ΔOI +3,565（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 110.51 → 今开 114.43（+3.6%） | 较昨收变动（含盘初走势） ｜ 今日高 115.54 ｜ 低 111.46

Options: P/C成交量 0.43 | OI比 0.44 | ATM IV 92.5% | Skew 8.5pp | Term 0.78 | ExpMove ±4.4%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价显著（Skew 8.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±4.4% ｜ 11-27（8D）±8.5% ｜ 12-04（15D）±11.3% ｜ 12-11（22D）±14.1%
   ⇒ IV–VIX Spread: +69.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,441,629 | GEX Change vs 上次快照 7,031,448 | Flip: Primary Flip: 118.66（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 384 / LOW 227 / INVALID 415
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 118.66（全链重定价，覆盖 98%）
Put Wall 110（弱结构｜现价高于该位 3.8%）
最近结构参考: Flip 119（现价低于该位 3.7%）
量化视角： 负 Gamma（544万，无历史分位）｜负 Gamma 缓解（+703万）｜现价位于 Flip 下方 3.74%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 110（Put Wall，弱结构）；上方 130（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 119（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 114.0C — Vol 4,099 | 最新价 $3.60 | OI 16→3581 (ΔOI +3565张) | ΔOI/Volume 87.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3565张（+22281.2% vs前日OI），连续性待观察（方向未知）
11-27 118.0C — Vol 3,615 | 最新价 $2.35 | OI 72→3593 (ΔOI +3521张) | ΔOI/Volume 97.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3521张（+4890.3% vs前日OI），连续性待观察（方向未知）
11-27 120.0C — Vol 2,604 | 最新价 $1.78 | OI 141→2388 (ΔOI +2247张) | ΔOI/Volume 86.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2247张（+1593.6% vs前日OI），连续性待观察（方向未知）
11-27 116.0C — Vol 2,398 | 最新价 $3.10 | OI 155→2167 (ΔOI +2012张) | ΔOI/Volume 83.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2012张（+1298.1% vs前日OI），连续性待观察（方向未知）
11-20 105.0P — Vol 3,150 | 最新价 $1.17 | OI 5079→6481 (ΔOI +1402张) | ΔOI/Volume 44.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1402张（+27.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,747 张（Put 1,402 / Call 11,345），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C -3.1k / P -3.4k ｜ Activity HIGH ｜ 1D
11-27  C +12.2k / P +1.6k ｜ Activity HIGH ｜ 8D
12-04  C +0.9k / P +1.2k ｜ Activity MEDIUM △ ｜ 15D
12-11  C +0.3k / P +0.6k ｜ Activity MEDIUM △ ｜ 22D

📆 11-20 Forward Structure
存量OI: C 135.6k / P 60.3k，今日变化ΔOI: C -3.1k / P -3.4k，平值价格ATM: C $2.59 / P $2.41 ｜ ATM IV 92.5%，净 delta 敞口 695k shares
Top ΔOI: P 140 -2,316
仓位参考: Max Pain 130 ｜ Put Wall 105（-8.1%，弱）（OI 6.5k）
量化解读： 存量 Call 重｜ATM IV 92.5%｜历史 Rank 82%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 695,085 股

📆 11-27 Forward Structure
存量OI: C 24.4k / P 11.5k，今日变化ΔOI: C +12.2k / P +1.6k，平值价格ATM: C $5.00 / P $4.70 ｜ ATM IV 70.6%，净 delta 敞口 501k shares
Top ΔOI: C 114 +3,565 ｜ C 118 +3,521 ｜ C 120 +2,247
仓位参考: Max Pain 115 ｜ Call Wall 118（+3.3%，弱）（OI 3.6k） ｜ Put Wall 110（-3.7%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 70.6%｜历史 Rank 82%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 正 500,569 股

12-04（MEDIUM △）Top ΔOI: 100P +613
12-04（MEDIUM △）仓位参考: Max Pain 135 ｜ Put Wall 120（+5.1%，弱）（OI 0.9k）

12-11（MEDIUM △）Top ΔOI: 100P +333 ｜ 110C +95
12-11（MEDIUM △）仓位参考: Max Pain 135 ｜ Call Wall 125（+9.4%，弱）（OI 0.2k） ｜ Put Wall 120（+5.1%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/COIN_morning.json