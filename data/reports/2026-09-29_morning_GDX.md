# 期权晨报 2026-09-29（快照 10:20 ET）

📊 市场环境

SPY $764.20 ｜ QQQ $nan
VIX 15.96 ↓0.7%（5D +12.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 90C ΔOI +2,859（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 80P ΔOI +2,381 占该期限总 OI 10.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 87.89 → 今开 88.75（+1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 89.09 ｜ 低 88.22

Options: P/C成交量 0.21 | OI比 0.48 | ATM IV 49.1% | Skew 1.6pp | Term 0.86 | ExpMove ±3.5%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价薄（Skew 1.6pp）｜存量 Call 偏重（OI比 0.48）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.21×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.48×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（3D）±3.5% ｜ 10-09（10D）±5.5% ｜ 10-16（17D）±7.1% ｜ 10-23（24D）±8.9%
   ⇒ IV–VIX Spread: +33.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,996,313 | GEX Change vs 上次快照 9,302,436 | Flip: Primary Flip: 89.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 443 / LOW 100 / INVALID 269
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 89.50（全链重定价，覆盖 98%）
Put Wall 90（弱结构｜现价低于该位 1.3%） | Call Wall 94（弱结构｜现价低于该位 5.5%）
最近结构参考: Flip 89（现价低于该位 0.8%）
量化视角： 负 Gamma（1000万，无历史分位）｜负 Gamma 缓解（+930万）｜现价位于 Flip 下方 0.79%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 90（Put Wall，弱结构） / 94（MaxPain，仅结算参考） / 94（Call Wall，弱结构）。
• Gamma 区域：切换参考 89（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 90.5C — Vol 3,076 | 最新价 $0.73 | OI 6→2865 (ΔOI +2859张) | ΔOI/Volume 93.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2859张（+47650.0% vs前日OI），连续性待观察（方向未知）
10-09 80.0P — Vol 2,506 | 最新价 $0.34 | OI 2683→5064 (ΔOI +2381张) | ΔOI/Volume 95.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2381张（+88.7% vs前日OI），连续性待观察（方向未知）
10-02 85.0P — Vol 2,893 | 最新价 $0.57 | OI 936→3177 (ΔOI +2241张) | ΔOI/Volume 77.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2241张（+239.4% vs前日OI），连续性待观察（方向未知）
10-02 84.0P — Vol 3,499 | 最新价 $0.40 | OI 271→2353 (ΔOI +2082张) | ΔOI/Volume 59.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2082张（+768.3% vs前日OI），连续性待观察（方向未知）
10-02 90.0C — Vol 2,854 | 最新价 $0.85 | OI 63→1942 (ΔOI +1879张) | ΔOI/Volume 65.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1879张（+2982.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,442 张（Put 6,704 / Call 4,738），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +13.0k / P +8.1k ｜ Activity MEDIUM △ ｜ 3D
10-09  C +1.8k / P +2.9k ｜ Activity HIGH ｜ 10D
10-16  C -0.7k / P +2.3k ｜ Activity HIGH ｜ 17D
10-23  C +0.3k / P +0.1k ｜ Activity MEDIUM △ ｜ 24D

📆 10-02 Forward Structure
存量OI: C 129.8k / P 61.7k，今日变化ΔOI: C +13.0k / P +8.1k，平值价格ATM: C $1.55 / P $1.55 ｜ ATM IV 49.1%，净 delta 敞口 513k shares
Top ΔOI: C 90 +2,859 ｜ P 99 -2,776 ｜ P 85 +2,241
仓位参考: Max Pain 94 ｜ Call Wall 94（+5.9%，弱）（OI 35.8k） ｜ Put Wall 90（+1.4%，弱）（OI 9.1k）
量化解读： 存量 Call 重｜ATM IV 49.1%｜历史 Rank 80%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 513,270 股

📆 10-09 Forward Structure
存量OI: C 8.6k / P 15.1k，今日变化ΔOI: C +1.8k / P +2.9k，平值价格ATM: C $2.30 / P $2.62 ｜ ATM IV 42.3%，净 delta 敞口 4k shares
Top ΔOI: P 80 +2,381 ｜ C 95 +346
仓位参考: Max Pain 94 ｜ Call Wall 94（+5.9%，弱）（OI 0.7k） ｜ Put Wall 90（+1.4%，弱）（OI 1.9k）
量化解读： 存量 Put 重｜ATM IV 42.3%｜历史 Rank 80%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,031 股

📆 10-16 Forward Structure
存量OI: C 94.0k / P 102.7k，今日变化ΔOI: C -0.7k / P +2.3k，平值价格ATM: C $3.05 / P $3.26 ｜ ATM IV 41.5%，净 delta 敞口 -7k shares
Top ΔOI: P 90 +1,422 ｜ P 88 +830
仓位参考: Max Pain 92 ｜ Call Wall 90（+1.4%，弱）（OI 5.3k） ｜ Put Wall 90（+1.4%，弱）（OI 10.9k）
量化解读： 存量两侧均衡｜ATM IV 41.5%｜历史 Rank 80%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 负 7,466 股

10-23（MEDIUM △）Top ΔOI: 80P -130 ｜ 88P +124
10-23（MEDIUM △）仓位参考: Max Pain 95 ｜ Call Wall 91（+2.5%，弱）（OI 0.2k） ｜ Put Wall 93（+4.7%，弱）（OI 1.3k）

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 49.1% vs 10-09 42.3%（差 +6.8pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/GDX_morning.json