# 期权晨报 2026-10-01（快照 10:20 ET）

📊 市场环境

SPY $760.36 ｜ QQQ $737.29
VIX 17.57 ↑7.5%（5D +12.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-01

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 54.5 ｜ 前值 54.6　✅ 今日已公布
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 85P ΔOI -588（距现价 -2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-02 94C ΔOI -16,287 占该期限总 OI 10.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 89.0）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 87.80 → 今开 87.69（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 87.69 ｜ 低 86.48

Options: P/C成交量 1.13 | OI比 0.59 | ATM IV 45.1% | Skew -5.5pp | Term 0.90 | ExpMove ±2.2%（近端） | Rank 71%
量化视角： IV 中性（Rank 71%）｜期限结构正常（Term 0.90）｜Put 保护异常便宜（Skew -5.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.13×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±2.2% ｜ 10-09（8D）±4.9% ｜ 10-16（15D）±6.7% ｜ 10-23（22D）±3.3%
   ⇒ IV–VIX Spread: +27.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -35,196,231 | GEX Change vs 上次快照 3,411,674 | Flip: Candidates 89.01 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 79%（带内） ｜ IV 有效性: VALID 405 / LOW 129 / INVALID 330
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈89（全链重定价，覆盖 79%，CONDITIONAL）
Put Wall 90（弱结构｜现价低于该位 3.6%）
最近结构参考: Flip 89（现价低于该位 2.5%）
量化视角： 负 Gamma（3520万，无历史分位）｜负 Gamma 缓解（+341万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 90（Put Wall，弱结构） / 92（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 89（全链重定价，覆盖 79%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 75.0P — Vol 2,000 | 最新价 $0.05 | OI 2329→4319 (ΔOI +1990张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1990张（+85.4% vs前日OI），连续性待观察（方向未知）
10-02 91.0C — Vol 1,853 | 最新价 $0.20 | OI 1483→2664 (ΔOI +1181张) | ΔOI/Volume 63.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1181张（+79.6% vs前日OI），连续性待观察（方向未知）
10-16 90.0C — Vol 925 | 最新价 $2.12 | OI 5191→5730 (ΔOI +539张) | ΔOI/Volume 58.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增539张（+10.4% vs前日OI），连续性待观察（方向未知）
10-16 105.0C — Vol 741 | 最新价 $0.15 | OI 10762→11265 (ΔOI +503张) | ΔOI/Volume 67.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增503张（+4.7% vs前日OI），连续性待观察（方向未知）
10-02 90.0C — Vol 1,434 | 最新价 $0.35 | OI 1905→2378 (ΔOI +473张) | ΔOI/Volume 33.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增473张（+24.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,686 张（Put 1,990 / Call 2,696），跨 3 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C -34.7k / P -7.2k ｜ Activity HIGH ｜ 1D
10-09  C +0.7k / P +2.0k ｜ Activity HIGH ｜ 8D
10-16  C +0.8k / P -2.3k ｜ Activity HIGH ｜ 15D
10-23  C +0.2k / P -0.2k ｜ Activity LOW ｜ 22D

📆 10-02 Forward Structure
存量OI: C 95.4k / P 56.3k，今日变化ΔOI: C -34.7k / P -7.2k，平值价格ATM: C $1.13 / P $0.82 ｜ ATM IV 45.1%，净 delta 敞口 610k shares
Top ΔOI: C 94 -16,287
仓位参考: Max Pain 92 ｜ Put Wall 90（+3.8%，弱）（OI 8.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 45.1%｜历史 Rank 71%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 609,778 股

📆 10-09 Forward Structure
存量OI: C 9.9k / P 17.6k，今日变化ΔOI: C +0.7k / P +2.0k，平值价格ATM: C $2.23 / P $2.03 ｜ ATM IV 39.7%，净 delta 敞口 33k shares
Top ΔOI: C 88 +221 ｜ C 92 +209
仓位参考: Max Pain 92 ｜ Call Wall 90（+3.8%，弱）（OI 0.4k） ｜ Put Wall 90（+3.8%，弱）（OI 1.9k）
量化解读： 存量 Put 重｜ATM IV 39.7%｜历史 Rank 71%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 33,114 股

📆 10-16 Forward Structure
存量OI: C 94.7k / P 103.8k，今日变化ΔOI: C +0.8k / P -2.3k，平值价格ATM: C $3.00 / P $2.81 ｜ ATM IV 39.8%，净 delta 敞口 142k shares
Top ΔOI: P 85 -588 ｜ C 90 +539
仓位参考: Max Pain 92 ｜ Call Wall 90（+3.8%，弱）（OI 5.7k） ｜ Put Wall 90（+3.8%，弱）（OI 10.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 39.8%｜历史 Rank 71%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 141,992 股

10-23（Activity LOW）仓位参考: Max Pain 94 ｜ Call Wall 90（+3.8%，弱）（OI 0.4k） ｜ Put Wall 85（-2.0%，弱）（OI 1.3k）

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 45.1% vs 10-09 39.7%（差 +5.4pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=38 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=38）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/GDX_morning.json