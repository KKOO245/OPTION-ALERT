# 期权晨报 2026-09-17（快照 11:28 ET）

📊 市场环境

SPY $762.60 ｜ QQQ $nan
VIX 15.87 ↓10.4%（5D -11.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 385P ΔOI +160（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 385P ΔOI +160 占该期限总 OI 21.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 382.29 → 今开 385.01（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 385.90 ｜ 低 378.28

Options: P/C成交量 0.11 | OI比 0.92 | ATM IV 44.5% | Skew -36.8pp | Term 0.82 | ExpMove ±2.8%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜Put 保护异常便宜（Skew -36.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.11×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（1D）±2.8% ｜ 09-25（8D）±4.3% ｜ 10-02（15D）±5.0% ｜ 10-09（22D）±7.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -299,690 | GEX Change vs 上次快照 -1,433,585 | Flip: Primary Flip: 379.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 82%（带内） ｜ IV 有效性: VALID 289 / LOW 205 / INVALID 446
结构观察区: Primary Flip 379.25（全链重定价，覆盖 82%）
Put Wall 350（弱结构｜现价高于该位 8.2%） | Call Wall 400（弱结构｜现价低于该位 5.3%）
最近结构参考: Flip 379（现价低于该位 0.2%）
量化视角： 负 Gamma（30万，无历史分位）｜由正转负（143万）｜现价位于 Flip 下方 0.16%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 350（Put Wall，弱结构） / 372（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 379（全链重定价，覆盖 82%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 385.0P — Vol 170 | 最新价 $12.33 | OI 1→161 (ΔOI +160张) | ΔOI/Volume 94.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增160张（+16000.0% vs前日OI），连续性待观察（方向未知）
10-16 385.0P — Vol 205 | 最新价 $14.77 | OI 98→257 (ΔOI +159张) | ΔOI/Volume 77.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增159张（+162.2% vs前日OI），连续性待观察（方向未知）
09-18 365.0P — Vol 161 | 最新价 $0.50 | OI 487→614 (ΔOI +127张) | ΔOI/Volume 78.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增127张（+26.1% vs前日OI），连续性待观察（方向未知）
09-18 405.0C — Vol 146 | 最新价 $0.24 | OI 192→286 (ΔOI +94张) | ΔOI/Volume 64.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增94张（+49.0% vs前日OI），连续性待观察（方向未知）
09-18 370.0P — Vol 112 | 最新价 $0.80 | OI 791→878 (ΔOI +87张) | ΔOI/Volume 77.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增87张（+11.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 627 张（Put 533 / Call 94），跨 3 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +19 / P +70 ｜ Activity LOW ｜ 1D
09-25  C +78 / P +12 ｜ Activity MEDIUM △ ｜ 8D
10-02  C +32 / P -3 ｜ Activity LOW ｜ 15D
10-09  C +5 / P +0.2k ｜ Activity HIGH ｜ 22D

📆 09-18 Forward Structure
存量OI: C 16.5k / P 15.1k，今日变化ΔOI: C +19 / P +70，平值价格ATM: C $8.35 / P $2.30 ｜ ATM IV 44.5%，净 delta 敞口 -6k shares
Top ΔOI: P 365 +127 ｜ C 405 +94
仓位参考: Max Pain 372 ｜ Call Wall 400（+5.6%，弱）（OI 1.1k） ｜ Put Wall 350（-7.6%，弱）（OI 2.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 44.5%｜历史 Rank 74%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 5,604 股

09-25（MEDIUM △）Top ΔOI: 382C +28 ｜ 400C +20
09-25（MEDIUM △）仓位参考: Max Pain 370 ｜ Call Wall 405（+7.0%，弱）（OI 0.2k） ｜ Put Wall 360（-4.9%，弱）（OI 0.2k）

10-02（Activity LOW）仓位参考: Max Pain 365 ｜ Call Wall 405（+7.0%）（OI 79）

📆 10-09 Forward Structure
存量OI: C 0.4k / P 0.4k，今日变化ΔOI: C +5 / P +0.2k，平值价格ATM: C $17.02 / P $9.80 ｜ ATM IV 33.9%，净 delta 敞口 -8k shares
Top ΔOI: P 385 +160 ｜ C 375 +2 ｜ C 385 +2
仓位参考: Max Pain 380 ｜ Call Wall 380（+0.4%）（OI 0.1k） ｜ Put Wall 385（+1.7%）（OI 0.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 33.9%｜历史 Rank 74%（近端代理）｜净 delta 敞口 负 8,351 股

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 44.5% vs 09-25 34.9%（差 +9.6pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/ISRG_morning.json