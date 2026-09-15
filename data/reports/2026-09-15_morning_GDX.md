# 期权晨报 2026-09-15（快照 10:20 ET）

📊 市场环境

SPY $759.03 ｜ QQQ $706.18
VIX 17.08 ↓0.1%（5D +8.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 93P ΔOI +3,128（距现价 -1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-25 104C ΔOI +4,642 占该期限总 OI 11.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 94.14 → 今开 94.62（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 94.75 ｜ 低 93.36

Options: P/C成交量 0.11 | OI比 1.29 | ATM IV 51.9% | Skew -1.4pp | Term 0.85 | ExpMove ±4.0%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.11×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.29×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（3D）±4.0% ｜ 09-25（10D）±6.2% ｜ 10-02（17D）±8.0% ｜ 10-09（24D）±9.2%
   ⇒ IV–VIX Spread: +34.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -27,512,434 | GEX Change vs 上次快照 1,819,456 | Flip: Primary Flip: 95.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 553 / LOW 144 / INVALID 205
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 95.44（全链重定价，覆盖 98%）
最近结构参考: Flip 95（现价低于该位 1.4%）
量化视角： 负 Gamma（2751万，无历史分位）｜负 Gamma 缓解（+182万）｜现价位于 Flip 下方 1.43%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 92（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 95（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 104.0C — Vol 4,845 | 最新价 $0.57 | OI 495→5137 (ΔOI +4642张) | ΔOI/Volume 95.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4642张（+937.8% vs前日OI），连续性待观察（方向未知）
09-25 100.0C — Vol 3,933 | 最新价 $1.10 | OI 421→3792 (ΔOI +3371张) | ΔOI/Volume 85.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3371张（+800.7% vs前日OI），连续性待观察（方向未知）
09-25 93.0P — Vol 3,281 | 最新价 $2.40 | OI 636→3764 (ΔOI +3128张) | ΔOI/Volume 95.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3128张（+491.8% vs前日OI），连续性待观察（方向未知）
09-18 100.0C — Vol 4,005 | 最新价 $0.37 | OI 28162→30773 (ΔOI +2611张) | ΔOI/Volume 65.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2611张（+9.3% vs前日OI），连续性待观察（方向未知）
09-18 87.0P — Vol 2,602 | 最新价 $0.17 | OI 1690→3542 (ΔOI +1852张) | ΔOI/Volume 71.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1852张（+109.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 15,604 张（Put 4,980 / Call 10,624），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +6.4k / P +0.7k ｜ Activity MEDIUM △ ｜ 3D
09-25  C +9.2k / P +3.8k ｜ Activity HIGH ｜ 10D
10-02  C +2.3k / P -3.6k ｜ Activity HIGH ｜ 17D
10-09  C +0.1k / P +0.4k ｜ Activity MEDIUM △ ｜ 24D

📆 09-18 Forward Structure
存量OI: C 340.9k / P 439.8k，今日变化ΔOI: C +6.4k / P +0.7k，平值价格ATM: C $2.00 / P $1.75 ｜ ATM IV 51.9%，净 delta 敞口 191k shares
Top ΔOI: P 85 -2,774 ｜ C 100 +2,611 ｜ P 87 +1,852
仓位参考: Max Pain 92 ｜ Call Wall 100（+6.3%，弱）（OI 30.8k） ｜ Put Wall 90（-4.3%，弱）（OI 43.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 51.9%｜历史 Rank 85%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 190,758 股

📆 09-25 Forward Structure
存量OI: C 24.1k / P 16.5k，今日变化ΔOI: C +9.2k / P +3.8k，平值价格ATM: C $3.01 / P $2.81 ｜ ATM IV 45.4%，净 delta 敞口 7k shares
Top ΔOI: C 104 +4,642 ｜ C 100 +3,371 ｜ P 93 +3,128
仓位参考: Max Pain 95 ｜ Call Wall 100（+6.3%，弱）（OI 3.8k） ｜ Put Wall 93（-1.1%，弱）（OI 3.8k）
量化解读： 存量 Call 重｜ATM IV 45.4%｜历史 Rank 85%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 7,406 股

📆 10-02 Forward Structure
存量OI: C 11.8k / P 24.1k，今日变化ΔOI: C +2.3k / P -3.6k，平值价格ATM: C $4.10 / P $3.46 ｜ ATM IV 45.1%，净 delta 敞口 299k shares
Top ΔOI: P 97 -3,733 ｜ C 100 +1,848 ｜ C 95 +170
仓位参考: Max Pain 99 ｜ Call Wall 100（+6.3%，弱）（OI 2.9k） ｜ Put Wall 97（+3.1%）（OI 11.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 45.1%｜历史 Rank 85%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 299,180 股

10-09（MEDIUM △）Top ΔOI: 94P +207 ｜ 102C +80
10-09（MEDIUM △）仓位参考: Max Pain 98 ｜ Call Wall 85（-9.6%）（OI 0.2k） ｜ Put Wall 85（-9.6%，弱）（OI 0.4k）

📅 事件差分（观察，非因果）: 09-18（3D）ATM IV 51.9% vs 09-25 45.4%（差 +6.4pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/GDX_morning.json