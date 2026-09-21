# 期权晚报 2026-09-21（快照 16:40 ET）

📊 市场环境

SPY $773.50 ｜ QQQ $741.47
VIX 14.87 ↑0.4%（5D -13.0%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 33.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 17C ΔOI +136（距现价 -0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 16.56 → 收盘 17.10（+3.3%） ｜ 今日高 17.26 ｜ 低 16.35 ｜ 昨收 15.73 → 收盘 17.10（+8.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.12 | OI比 0.52 | ATM IV 78.7% | Skew 11.3pp | Term 1.03 | ExpMove ±6.9%（近端） | Rank 6%
量化视角： IV 历史低位（Rank 6%，期权偏便宜）｜期限结构正常（Term 1.03）｜保护溢价显著（Skew 11.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.52）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.12×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.52×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（4D）±6.9% ｜ 10-02（11D）±11.5% ｜ 10-09（18D）±17.4% ｜ 10-16（25D）±16.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,472,946 | GEX Change vs 上次快照 -238,783 | Flip: Primary Flip: 15.59（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 223 / LOW 74 / INVALID 159
结构观察区: Primary Flip 15.59（全链重定价，覆盖 100%）
最近结构参考: Flip 16（现价高于该位 9.7%）
量化视角： 正 Gamma（147万，无历史分位）｜正 Gamma 减弱（24万）｜现价位于 Flip 上方 9.72%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 17（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 14.5P — Vol 36 | 最新价 $0.06 | OI 139→576 (ΔOI +437张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增437张（+314.4% vs前日OI），值得跟踪（方向未知）
09-25 16.0C — Vol 83 | 最新价 $1.15 | OI 30→351 (ΔOI +321张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增321张（+1070.0% vs前日OI），值得跟踪（方向未知）
10-02 17.0C — Vol 160 | 最新价 $0.85 | OI 21→157 (ΔOI +136张) | ΔOI/Volume 85.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增136张（+647.6% vs前日OI），连续性待观察（方向未知）
09-25 16.0P — Vol 13 | 最新价 $0.27 | OI 103→210 (ΔOI +107张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增107张（+103.9% vs前日OI），值得跟踪（方向未知）
10-02 26.0P — Vol 88（Yahoo补） | 最新价 $10.24 | OI 4→92 (ΔOI +88张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增88张（+2200.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,089 张（Put 632 / Call 457），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +0.6k / P +0.7k ｜ Activity HIGH ｜ 4D
10-02  C +0.3k / P +0.2k ｜ Activity HIGH ｜ 11D
10-09  C +45 / P +0.1k ｜ Activity MEDIUM △ ｜ 18D
10-16  C -0.7k / P +33 ｜ Activity MEDIUM △ ｜ 25D

📆 09-25 Forward Structure
存量OI: C 6.1k / P 3.2k，今日变化ΔOI: C +0.6k / P +0.7k，平值价格ATM: C $0.50 / P $0.68 ｜ ATM IV 78.7%，净 delta 敞口 33k shares
Top ΔOI: C 16 +321 ｜ P 16 +107
仓位参考: Max Pain 17 ｜ Put Wall 15.5（-9.4%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 78.7%｜历史 Rank 6%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 正 33,493 股

📆 10-02 Forward Structure
存量OI: C 3.1k / P 1.2k，今日变化ΔOI: C +0.3k / P +0.2k，平值价格ATM: C $0.85 / P $1.12 ｜ ATM IV 79.0%，净 delta 敞口 5k shares
Top ΔOI: C 17 +136 ｜ P 26 +88
仓位参考: Max Pain 18 ｜ Put Wall 18.5（+8.2%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 79.0%｜历史 Rank 6%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 正 5,209 股

10-09（MEDIUM △）Top ΔOI: 17P +50 ｜ 17C +23
10-09（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 16（-6.4%）（OI 0.1k）

10-16（MEDIUM △）Top ΔOI: 18C -798 ｜ 17C +43
10-16（MEDIUM △）仓位参考: Max Pain 20 ｜ Put Wall 17（-0.6%，弱）（OI 0.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/NNE_evening.json