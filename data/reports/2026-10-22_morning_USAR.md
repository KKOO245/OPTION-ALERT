# 期权晨报 2026-10-22（快照 10:20 ET）

📊 市场环境

SPY $766.63 ｜ QQQ $710.80
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
🟡 **近现价集中开仓**: 10-23 10C ΔOI +1,617（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 10.23 → 今开 9.75（-4.7%） | 较昨收变动（含盘初走势） ｜ 今日高 10.06 ｜ 低 9.66

Options: P/C成交量 0.44 | OI比 0.24 | ATM IV 90.7% | Skew -0.2pp | Term 0.98 | ExpMove ±4.8%（近端） | Rank 22%
量化视角： IV 历史低位（Rank 22%，期权偏便宜）｜期限结构正常（Term 0.98）｜Put 保护异常便宜（Skew -0.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.24）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.24×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（1D）±4.8% ｜ 10-30（8D）±9.8% ｜ 11-06（15D）±13.2% ｜ 11-13（22D）±18.9%
   ⇒ IV–VIX Spread: +72.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 841,308 | GEX Change vs 上次快照 -894,226 | Flip: Primary Flip: 9.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 210 / LOW 84 / INVALID 142
结构观察区: Primary Flip 9.77（全链重定价，覆盖 95%）
Put Wall 10（弱结构｜现价低于该位 1.2%）
最近结构参考: Put Wall 10（现价低于该位 1.2%）
量化视角： 正 Gamma（84万，无历史分位）｜正 Gamma 减弱（89万）｜现价位于 Flip 上方 1.16%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（Put Wall，弱结构） / 10（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 10（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 10.0C — Vol 1,836 | 最新价 $0.36 | OI 855→2472 (ΔOI +1617张) | ΔOI/Volume 88.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1617张（+189.1% vs前日OI），连续性待观察（方向未知）
10-23 11.0C — Vol 1,906 | 最新价 $0.05 | OI 2116→3234 (ΔOI +1118张) | ΔOI/Volume 58.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1118张（+52.8% vs前日OI），连续性待观察（方向未知）
10-23 10.0P — Vol 1,366 | 最新价 $0.18 | OI 786→1818 (ΔOI +1032张) | ΔOI/Volume 75.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1032张（+131.3% vs前日OI），连续性待观察（方向未知）
11-06 13.0C — Vol 681 | 最新价 $0.09 | OI 330→609 (ΔOI +279张) | ΔOI/Volume 41.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增279张（+84.5% vs前日OI），连续性待观察（方向未知）
10-30 11.5C — Vol 335 | 最新价 $0.11 | OI 2742→2997 (ΔOI +255张) | ΔOI/Volume 76.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增255张（+9.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,301 张（Put 1,032 / Call 3,269），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +2.6k / P +0.8k ｜ Activity MEDIUM △ ｜ 1D
10-30  C +0.4k / P +0.1k ｜ Activity MEDIUM △ ｜ 8D
11-06  C +0.6k / P -56 ｜ Activity MEDIUM △ ｜ 15D
11-13  C +0.2k / P -3 ｜ Activity MEDIUM △ ｜ 22D

📆 10-23 Forward Structure
存量OI: C 26.3k / P 6.4k，今日变化ΔOI: C +2.6k / P +0.8k，平值价格ATM: C $0.18 / P $0.29 ｜ ATM IV 90.7%，净 delta 敞口 34k shares
Top ΔOI: C 10 +1,617 ｜ P 10 +1,032
仓位参考: Max Pain 10 ｜ Call Wall 10.5（+6.2%，弱）（OI 2.5k） ｜ Put Wall 10（+1.2%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 90.7%｜历史 Rank 22%（近端代理）｜IV/RV 1.65×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 33,761 股

10-30（MEDIUM △）Top ΔOI: 9P +87
10-30（MEDIUM △）仓位参考: Max Pain 12 ｜ Call Wall 10（+1.2%，弱）（OI 0.8k） ｜ Put Wall 9（-9.0%，弱）（OI 0.7k）

11-06（MEDIUM △）仓位参考: Max Pain 12 ｜ Put Wall 9（-9.0%）（OI 1.5k）

11-13（MEDIUM △）仓位参考: Max Pain 14 ｜ Call Wall 10.5（+6.2%，弱）（OI 0.3k） ｜ Put Wall 10.5（+6.2%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/USAR_morning.json