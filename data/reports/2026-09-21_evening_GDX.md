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
🟡 **近现价集中开仓**: 09-25 97C ΔOI +14,386（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-25 100C ΔOI +15,453 占该期限总 OI 10.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 95.81 → 收盘 94.43（-1.4%） ｜ 今日高 95.91 ｜ 低 93.71 ｜ 昨收 95.48 → 收盘 94.43（-1.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-28，窗口结束前不做对错判定）

Options: P/C成交量 0.98 | OI比 0.33 | ATM IV 47.8% | Skew -2.8pp | Term 0.86 | ExpMove ±4.1%（近端） | Rank 77%
量化视角： IV 历史高位（Rank 77%，期权偏贵）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.33）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.98×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.33×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（4D）±4.1% ｜ 10-02（11D）±6.1% ｜ 10-09（18D）±3.8% ｜ 10-16（25D）±8.6%
   ⇒ IV–VIX Spread: +32.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 24,449,665 | GEX Change vs 上次快照 946,506 | Flip: Primary Flip: 92.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 523 / LOW 94 / INVALID 245
结构观察区: Primary Flip 92.14（全链重定价，覆盖 100%）
Put Wall 90（弱结构｜现价高于该位 4.9%） | Call Wall 100（现价低于该位 5.6%）
最近结构参考: Flip 92（现价高于该位 2.5%）
量化视角： 正 Gamma（2445万，无历史分位）｜正 Gamma 增强（+95万）｜现价位于 Flip 上方 2.48%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 90（Put Wall，弱结构）；上方 95（MaxPain，仅结算参考） / 100（Call Wall）。
• Gamma 区域：切换参考 92（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 100.0C — Vol 1,388 | 最新价 $0.34 | OI 5403→20856 (ΔOI +15453张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15453张（+286.0% vs前日OI），连续性待观察（方向未知）
09-25 97.0C — Vol 2,636 | 最新价 $0.87 | OI 3456→17842 (ΔOI +14386张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14386张（+416.3% vs前日OI），连续性待观察（方向未知）
09-25 90.0P — Vol 1,028 | 最新价 $0.37 | OI 1182→4787 (ΔOI +3605张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3605张（+305.0% vs前日OI），连续性待观察（方向未知）
10-02 77.0P — Vol 3,502（Yahoo补） | 最新价 $0.04 | OI 15→3515 (ΔOI +3500张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3500张（+23333.3% vs前日OI），连续性待观察（方向未知）
09-25 93.0P — Vol 2,346 | 最新价 $1.21 | OI 4051→7215 (ΔOI +3164张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3164张（+78.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 40,108 张（Put 10,269 / Call 29,839），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +32.9k / P +12.1k ｜ Activity HIGH ｜ 4D
10-02  C +7.2k / P +4.4k ｜ Activity HIGH ｜ 11D
10-09  C +0.1k / P +49 ｜ Activity MEDIUM △ ｜ 18D
10-16  C +0.6k / P -0.8k ｜ Activity MEDIUM △ ｜ 25D

📆 09-25 Forward Structure
存量OI: C 106.5k / P 34.9k，今日变化ΔOI: C +32.9k / P +12.1k，平值价格ATM: C $2.27 / P $1.61 ｜ ATM IV 47.8%，净 delta 敞口 554k shares
Top ΔOI: C 100 +15,453 ｜ C 97 +14,386 ｜ P 90 +3,605
仓位参考: Max Pain 95 ｜ Call Wall 100（+5.9%，弱）（OI 20.9k） ｜ Put Wall 93（-1.5%）（OI 7.2k）
量化解读： 存量 Call 重｜ATM IV 47.8%｜历史 Rank 77%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 554,385 股

📆 10-02 Forward Structure
存量OI: C 21.1k / P 32.4k，今日变化ΔOI: C +7.2k / P +4.4k，平值价格ATM: C $2.80 / P $2.92 ｜ ATM IV 42.4%，净 delta 敞口 147k shares
Top ΔOI: C 100 +2,960 ｜ C 104 +1,463
仓位参考: Max Pain 98 ｜ Call Wall 100（+5.9%）（OI 6.2k） ｜ Put Wall 97（+2.7%）（OI 11.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 42.4%｜历史 Rank 77%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 147,252 股

10-09（MEDIUM △）Top ΔOI: 95C +59 ｜ 88P +27
10-09（MEDIUM △）仓位参考: Max Pain 94 ｜ Call Wall 94（-0.5%，弱）（OI 0.7k） ｜ Put Wall 90（-4.7%，弱）（OI 1.9k）

10-16（MEDIUM △）Top ΔOI: 88P -409 ｜ 89P -391
10-16（MEDIUM △）仓位参考: Max Pain 92 ｜ Call Wall 100（+5.9%，弱）（OI 10.3k） ｜ Put Wall 90（-4.7%，弱）（OI 9.6k）

📅 事件差分（观察，非因果）: 09-25（4D）ATM IV 47.8% vs 10-02 42.4%（差 +5.3pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/GDX_evening.json