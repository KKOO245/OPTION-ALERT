# 期权晨报 2026-11-02（快照 10:20 ET）

📊 市场环境

SPY $753.20 ｜ QQQ $681.09
VIX 18.83 ↓3.0%（5D +2.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 22.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 11-02 10:00　【高】ISM 制造业 PMI　预测 54.6 ｜ 实际 55.5 ｜ 前值 54.5　✅ 今日已公布
- 周一 11-02 19:00　【高】Midterm Elections　实际 待公布　⏰ 今日
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.13 ｜ 实际 待公布 ｜ 前值 7.079
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48.2 ｜ 实际 待公布 ｜ 前值 48

🔍 重点速览
🟡 **近现价集中开仓**: 11-06 153P ΔOI +3,018（距现价 -1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-06 153P ΔOI +3,018 占该期限总 OI 21.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 155.98 → 今开 156.41（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 157.12 ｜ 低 154.09

Options: P/C成交量 3.00 | OI比 1.64 | ATM IV 43.4% | Skew -2.1pp | Term 0.86 | ExpMove ±3.9%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.1pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 3.00）——观察点，非方向信号
   ⇒ Put/Call Volume: 3.00×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.64×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（4D）±3.9% ｜ 11-13（11D）±4.8% ｜ 11-20（18D）±6.8% ｜ 11-27（25D）±7.1%
   ⇒ IV–VIX Spread: +24.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,234,283 | GEX Change vs 上次快照 -4,991,601 | Flip: Primary Flip: 160.59（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 340 / LOW 55 / INVALID 377
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 160.59（全链重定价，覆盖 99%）
Call Wall 165（现价低于该位 5.9%）
最近结构参考: Flip 161（现价低于该位 3.3%）
量化视角： 负 Gamma（723万，无历史分位）｜负 Gamma 加深（499万）｜现价位于 Flip 下方 3.27%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 153（MaxPain，仅结算参考）；上方 165（Call Wall）。
• Gamma 区域：切换参考 161（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 135.0P — Vol 3,369 | 最新价 $0.18 | OI 859→4118 (ΔOI +3259张) | ΔOI/Volume 96.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3259张（+379.4% vs前日OI），连续性待观察（方向未知）
11-06 153.0P — Vol 3,099 | 最新价 $2.05 | OI 52→3070 (ΔOI +3018张) | ΔOI/Volume 97.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3018张（+5803.9% vs前日OI），连续性待观察（方向未知）
11-20 145.0P — Vol 3,022 | 最新价 $1.89 | OI 7588→10402 (ΔOI +2814张) | ΔOI/Volume 93.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2814张（+37.1% vs前日OI），连续性待观察（方向未知）
11-06 142.0C — Vol 1,500 | 最新价 $13.49 | OI 26→1526 (ΔOI +1500张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1500张（+5769.2% vs前日OI），连续性待观察（方向未知）
11-20 143.0P — Vol 1,005 | 最新价 $1.47 | OI 1337→2337 (ΔOI +1000张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1000张（+74.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,591 张（Put 10,091 / Call 1,500），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +2.1k / P +2.5k ｜ Activity HIGH ｜ 4D
11-13  C +0.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 11D
11-20  C +0.9k / P +8.6k ｜ Activity HIGH ｜ 18D
11-27  C +0.2k / P +0.2k ｜ Activity MEDIUM △ ｜ 25D

📆 11-06 Forward Structure
存量OI: C 5.4k / P 8.8k，今日变化ΔOI: C +2.1k / P +2.5k，平值价格ATM: C $3.00 / P $3.06 ｜ ATM IV 43.4%，净 delta 敞口 54k shares
Top ΔOI: P 153 +3,018 ｜ C 142 +1,500 ｜ P 151 -871
仓位参考: Max Pain 153 ｜ Call Wall 159（+2.4%，弱）（OI 0.4k） ｜ Put Wall 153（-1.5%）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 43.4%｜历史 Rank 91%（近端代理）｜IV/RV 1.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 53,590 股

11-13（MEDIUM △）Top ΔOI: 148P +112 ｜ 147P +64
11-13（MEDIUM △）仓位参考: Max Pain 153 ｜ Call Wall 160（+3.0%）（OI 0.4k） ｜ Put Wall 148（-4.7%，弱）（OI 0.3k）

📆 11-20 Forward Structure
存量OI: C 23.1k / P 46.6k，今日变化ΔOI: C +0.9k / P +8.6k，平值价格ATM: C $5.63 / P $4.86 ｜ ATM IV 40.1%，净 delta 敞口 -121k shares
Top ΔOI: P 135 +3,259 ｜ P 145 +2,814 ｜ P 143 +1,000
仓位参考: Max Pain 154 ｜ Call Wall 165（+6.2%）（OI 7.3k） ｜ Put Wall 147（-5.4%，弱）（OI 5.6k）
量化解读： 存量 Put 重｜ATM IV 40.1%｜历史 Rank 91%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 121,331 股

11-27（MEDIUM △）Top ΔOI: 157P +126 ｜ 157C +112
11-27（MEDIUM △）仓位参考: Max Pain 158 ｜ Call Wall 157（+1.1%，弱）（OI 0.1k） ｜ Put Wall 156（+0.4%）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/XBI_morning.json