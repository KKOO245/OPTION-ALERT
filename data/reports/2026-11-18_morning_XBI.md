# 期权晨报 2026-11-18（快照 10:20 ET）

📊 市场环境

SPY $731.20 ｜ QQQ $659.68
VIX 24.58 ↓3.5%（5D +40.5%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 26.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **事件差分**: 11-20 ATM IV 51.8% vs 11-27 37.6%（差 +14.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-20 150C ΔOI +3,843（距现价 +2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-27 143P ΔOI +1,001 占该期限总 OI 13.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 145.28 → 今开 144.86（-0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 147.60 ｜ 低 144.58

Options: P/C成交量 197.75 | OI比 1.75 | ATM IV 51.8% | Skew 12.0pp | Term 0.70 | ExpMove ±3.3%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价显著（Skew 12.0pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 197.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 197.75×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.75×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-20（2D）±3.3% ｜ 11-27（9D）±5.0% ｜ 12-04（16D）±1.5% ｜ 12-11（23D）±4.3%
   ⇒ IV–VIX Spread: +27.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -25,627,832 | GEX Change vs 上次快照 7,864,962 | Flip: Primary Flip: 151.22（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 407 / LOW 143 / INVALID 352
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 151.22（全链重定价，覆盖 93%）
最近结构参考: Flip 151（现价低于该位 3.1%）
量化视角： 负 Gamma（2563万，无历史分位）｜负 Gamma 缓解（+786万）｜现价位于 Flip 下方 3.05%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 151（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 150.0C — Vol 4,054 | 最新价 $0.74 | OI 511→4354 (ΔOI +3843张) | ΔOI/Volume 94.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3843张（+752.0% vs前日OI），连续性待观察（方向未知）
11-20 140.0P — Vol 2,465 | 最新价 $0.80 | OI 9837→11909 (ΔOI +2072张) | ΔOI/Volume 84.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2072张（+21.1% vs前日OI），连续性待观察（方向未知）
11-27 143.0P — Vol 1,061 | 最新价 $2.60 | OI 24→1025 (ΔOI +1001张) | ΔOI/Volume 94.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1001张（+4170.8% vs前日OI），连续性待观察（方向未知）
12-18 143.0P — Vol 1,013 | 最新价 $5.20 | OI 5038→5748 (ΔOI +710张) | ΔOI/Volume 70.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增710张（+14.1% vs前日OI），连续性待观察（方向未知）
12-18 135.0P — Vol 1,350 | 最新价 $2.45 | OI 3663→3963 (ΔOI +300张) | ΔOI/Volume 22.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增300张（+8.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,926 张（Put 4,083 / Call 3,843），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +4.1k / P +1.9k ｜ Activity MEDIUM △ ｜ 2D
11-27  C +0.3k / P +1.2k ｜ Activity HIGH ｜ 9D
12-04  C +59 / P +77 ｜ Activity MEDIUM △ ｜ 16D
12-11  C +0.3k / P +54 ｜ Activity MEDIUM △ ｜ 23D

📆 11-20 Forward Structure
存量OI: C 36.0k / P 62.8k，今日变化ΔOI: C +4.1k / P +1.9k，平值价格ATM: C $1.73 / P $3.15 ｜ ATM IV 51.8%，净 delta 敞口 136k shares
Top ΔOI: C 150 +3,843 ｜ P 140 +2,072 ｜ P 161 -225
仓位参考: Max Pain 150 ｜ Call Wall 150（+2.3%，弱）（OI 4.4k） ｜ Put Wall 140（-4.5%，弱）（OI 11.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 51.8%｜历史 Rank 97%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 135,981 股

📆 11-27 Forward Structure
存量OI: C 1.9k / P 5.3k，今日变化ΔOI: C +0.3k / P +1.2k，平值价格ATM: C $3.05 / P $4.30 ｜ ATM IV 37.6%，净 delta 敞口 -16k shares
Top ΔOI: P 143 +1,001 ｜ P 146 -219
仓位参考: Max Pain 155 ｜ Call Wall 152.5（+4.0%，弱）（OI 0.2k） ｜ Put Wall 143（-2.5%，弱）（OI 1.0k）
量化解读： 存量 Put 重｜ATM IV 37.6%｜历史 Rank 97%（近端代理）｜IV/RV 0.96×（近似）｜净 delta 敞口 负 16,406 股

12-04（MEDIUM △）Top ΔOI: 155P +62 ｜ 144C +50
12-04（MEDIUM △）仓位参考: Max Pain 159 ｜ Call Wall 144（-1.8%，弱）（OI 50） ｜ Put Wall 148（+1.0%，弱）（OI 0.1k）

12-11（MEDIUM △）Top ΔOI: 147C +255 ｜ 139P +23
12-11（MEDIUM △）仓位参考: Max Pain 147 ｜ Call Wall 147（+0.3%）（OI 0.4k） ｜ Put Wall 143（-2.5%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 51.8% vs 11-27 37.6%（差 +14.2pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/XBI_morning.json