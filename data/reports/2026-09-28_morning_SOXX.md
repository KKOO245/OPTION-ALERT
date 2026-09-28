# 期权晨报 2026-09-28（快照 10:20 ET）

📊 市场环境

SPY $765.39 ｜ QQQ $736.53
VIX 15.89 ↑6.9%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.24 ｜ 实际 待公布 ｜ 前值 7.271
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 54.9 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 84 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🔵 **期限 OI 集中**: 10-02 420P ΔOI +9,981 占该期限总 OI 24.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 572.68 → 今开 568.60（-0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 570.85 ｜ 低 557.14

Options: P/C成交量 2.17 | OI比 1.62 | ATM IV 39.9% | Skew -2.6pp | Term 0.96 | ExpMove ±4.8%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构正常（Term 0.96）｜Put 保护异常便宜（Skew -2.6pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 2.17）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.17×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.62×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（4D）±4.8% ｜ 10-09（11D）±7.0% ｜ 10-16（18D）±6.5% ｜ 10-23（25D）±3.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,649,524 | GEX Change vs 上次快照 -4,838,376 | Flip: Primary Flip: 556.95（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 493 / LOW 221 / INVALID 816
结构观察区: Primary Flip 556.95（全链重定价，覆盖 98%）
最近结构参考: Flip 557（现价高于该位 1.0%）
量化视角： 正 Gamma（265万，无历史分位）｜正 Gamma 减弱（484万）｜现价位于 Flip 上方 1.04%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 542（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 557（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 420.0P — Vol 10,027 | 最新价 $0.08 | OI 696→10677 (ΔOI +9981张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9981张（+1434.0% vs前日OI），连续性待观察（方向未知）
10-16 520.0P — Vol 795 | 最新价 $4.25 | OI 3311→3881 (ΔOI +570张) | ΔOI/Volume 71.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增570张（+17.2% vs前日OI），连续性待观察（方向未知）
10-02 485.0P — Vol 327 | 最新价 $0.28 | OI 1351→1672 (ΔOI +321张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增321张（+23.8% vs前日OI），连续性待观察（方向未知）
10-30 660.0C — Vol 300 | 最新价 $5.10 | OI 1→301 (ΔOI +300张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增300张（+30000.0% vs前日OI），连续性待观察（方向未知）
10-30 620.0C — Vol 200 | 最新价 $12.40 | OI 4→202 (ΔOI +198张) | ΔOI/Volume 99.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增198张（+4950.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,370 张（Put 10,872 / Call 498），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +0.4k / P +11.1k ｜ Activity HIGH ｜ 4D
10-09  C +48 / P +0.2k ｜ Activity MEDIUM △ ｜ 11D
10-16  C -0.5k / P -50 ｜ Activity MEDIUM △ ｜ 18D
10-23  C +59 / P +32 ｜ Activity HIGH ｜ 25D

📆 10-02 Forward Structure
存量OI: C 15.4k / P 24.9k，今日变化ΔOI: C +0.4k / P +11.1k，平值价格ATM: C $17.40 / P $9.81 ｜ ATM IV 39.9%，净 delta 敞口 -29k shares
Top ΔOI: P 420 +9,981
仓位参考: Max Pain 542 ｜ Call Wall 542.5（-3.6%，弱）（OI 2.8k）
量化解读： 存量 Put 重｜ATM IV 39.9%｜历史 Rank 70%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 29,284 股

10-09（MEDIUM △）Top ΔOI: 550P +82 ｜ 540P +58
10-09（MEDIUM △）仓位参考: Max Pain 525 ｜ Call Wall 537.5（-4.5%，弱）（OI 0.4k） ｜ Put Wall 550（-2.3%，弱）（OI 0.1k）

10-16（MEDIUM △）Top ΔOI: 520P +570 ｜ 600C -488
10-16（MEDIUM △）仓位参考: Max Pain 530 ｜ Call Wall 550（-2.3%，弱）（OI 2.3k） ｜ Put Wall 530（-5.8%，弱）（OI 4.8k）

📆 10-23 Forward Structure
存量OI: C 0.9k / P 4.9k，今日变化ΔOI: C +59 / P +32，平值价格ATM: C $0.00 / P $21.30 ｜ ATM IV 37.9%，净 delta 敞口 3k shares
Top ΔOI: P 510 -28 ｜ C 510 +20
仓位参考: Max Pain 525 ｜ Call Wall 570（+1.3%，弱）（OI 84）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 37.9%｜历史 Rank 70%（近端代理）｜IV/RV 1.02×（近似）｜净 delta 敞口 正 3,315 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/SOXX_morning.json