# 期权晨报 2026-09-16（快照 11:22 ET）

📊 市场环境

SPY $760.53 ｜ QQQ $710.93
VIX 16.68 ↓3.0%（5D +1.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75　⏰ 今日
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　⏰ 今日
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　⏰ 今日
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🔴 **事件差分**: 09-18（2D）ATM IV 67.7% vs 09-25 48.7%（差 +19.0pp），覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 09-18 93C ΔOI +875（距现价 -1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 94P ΔOI +1,027 占该期限总 OI 17.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 94.13 → 今开 95.98（+2.0%） | 较昨收变动（含盘初走势） ｜ 今日高 95.98 ｜ 低 93.80

Options: P/C成交量 0.65 | OI比 1.28 | ATM IV 67.7% | Skew -0.2pp | Term 0.66 | ExpMove ±4.3%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.28×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（2D）±4.3% ｜ 09-25（9D）±6.4% ｜ 10-02（16D）±8.0% ｜ 10-09（23D）±9.2%
   ⇒ IV–VIX Spread: +51.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -17,444,251 | GEX Change vs 上次快照 12,298,738 | Flip: Primary Flip: 95.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 550 / LOW 132 / INVALID 220
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 95.44（全链重定价，覆盖 98%）
最近结构参考: Flip 95（现价低于该位 0.9%）
量化视角： 负 Gamma（1744万，无历史分位）｜负 Gamma 缓解（+1230万）｜现价位于 Flip 下方 0.94%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 92（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 95（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 100.0C — Vol 6,484 | 最新价 $2.86 | OI 6466→10087 (ΔOI +3621张) | ΔOI/Volume 55.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3621张（+56.0% vs前日OI），连续性待观察（方向未知）
10-16 105.0C — Vol 2,804 | 最新价 $1.62 | OI 4504→6770 (ΔOI +2266张) | ΔOI/Volume 80.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2266张（+50.3% vs前日OI），连续性待观察（方向未知）
10-16 82.0P — Vol 2,174 | 最新价 $0.88 | OI 594→2665 (ΔOI +2071张) | ΔOI/Volume 95.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2071张（+348.6% vs前日OI），连续性待观察（方向未知）
10-02 92.5P — Vol 1,671 | 最新价 $2.85 | OI 215→1775 (ΔOI +1560张) | ΔOI/Volume 93.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1560张（+725.6% vs前日OI），连续性待观察（方向未知）
09-25 100.0C — Vol 1,894 | 最新价 $1.00 | OI 3792→5330 (ΔOI +1538张) | ΔOI/Volume 81.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1538张（+40.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,056 张（Put 3,631 / Call 7,425），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0.6k / P -1.5k ｜ Activity HIGH ｜ 2D
09-25  C +2.6k / P +1.6k ｜ Activity HIGH ｜ 9D
10-02  C +0.6k / P +2.4k ｜ Activity MEDIUM △ ｜ 16D
10-09  C +1.2k / P +1.2k ｜ Activity HIGH ｜ 23D

📆 09-18 Forward Structure
存量OI: C 341.6k / P 438.3k，今日变化ΔOI: C +0.6k / P -1.5k，平值价格ATM: C $1.82 / P $2.22 ｜ ATM IV 67.7%，净 delta 敞口 124k shares
Top ΔOI: C 100 -1,176 ｜ C 93 +875 ｜ P 90 -841
仓位参考: Max Pain 92 ｜ Call Wall 100（+5.8%，弱）（OI 29.6k） ｜ Put Wall 90（-4.8%，弱）（OI 42.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 67.7%｜历史 Rank 97%（近端代理）｜IV/RV 1.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 124,043 股

📆 09-25 Forward Structure
存量OI: C 26.6k / P 18.1k，今日变化ΔOI: C +2.6k / P +1.6k，平值价格ATM: C $2.84 / P $3.25 ｜ ATM IV 48.7%，净 delta 敞口 42k shares
Top ΔOI: C 100 +1,538 ｜ P 88 +557
仓位参考: Max Pain 95 ｜ Call Wall 100（+5.8%，弱）（OI 5.3k） ｜ Put Wall 93（-1.6%，弱）（OI 3.8k）
量化解读： 存量 Call 重｜ATM IV 48.7%｜历史 Rank 97%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 42,112 股

10-02（MEDIUM △）Top ΔOI: 92P +1,560 ｜ 100C +282
10-02（MEDIUM △）仓位参考: Max Pain 99 ｜ Call Wall 100（+5.8%，弱）（OI 3.2k） ｜ Put Wall 97（+2.6%）（OI 11.3k）

📆 10-09 Forward Structure
存量OI: C 2.6k / P 3.2k，今日变化ΔOI: C +1.2k / P +1.2k，平值价格ATM: C $4.20 / P $4.55 ｜ ATM IV 45.4%，净 delta 敞口 4k shares
Top ΔOI: P 94 +1,027 ｜ C 94 +602 ｜ C 97 +452
仓位参考: Max Pain 94 ｜ Call Wall 94（-0.6%，弱）（OI 0.6k） ｜ Put Wall 94（-0.6%）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 45.4%｜历史 Rank 97%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 正 4,320 股

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 67.7% vs 09-25 48.7%（差 +19.0pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/GDX_morning.json