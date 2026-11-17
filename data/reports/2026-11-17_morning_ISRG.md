# 期权晨报 2026-11-17（快照 10:20 ET）

📊 市场环境

SPY $734.92 ｜ QQQ $656.95
VIX 22.73 ↓0.8%（5D +16.8%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.8　✅ 今日已公布
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🟡 **事件差分**: 11-20 ATM IV 47.0% vs 11-27 36.1%（差 +10.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 12-11 445C ΔOI +39（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 437.75 → 今开 437.33（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 441.29 ｜ 低 435.00

Options: P/C成交量 1.42 | OI比 1.00 | ATM IV 47.1% | Skew 6.8pp | Term 0.75 | ExpMove ±3.6%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜保护溢价显著（Skew 6.8pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.42）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.42×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.00×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（3D）±3.6% ｜ 11-27（10D）±4.9% ｜ 12-04（17D）±3.9% ｜ 12-11（24D）±7.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,382,149 | GEX Change vs 上次快照 263,627 | Flip: Primary Flip: 423.23（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 271 / LOW 169 / INVALID 526
结构观察区: Primary Flip 423.23（全链重定价，覆盖 91%）
Call Wall 480（弱结构｜现价低于该位 8.6%）
最近结构参考: Flip 423（现价高于该位 3.7%）
量化视角： 正 Gamma（238万，无历史分位）｜正 Gamma 增强（+26万）｜现价位于 Flip 上方 3.70%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 410（MaxPain，仅结算参考）；上方 480（Call Wall，弱结构）。
• Gamma 区域：切换参考 423（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 467.5C — Vol 90 | 最新价 $0.72 | OI 10→91 (ΔOI +81张) | ΔOI/Volume 90.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增81张（+810.0% vs前日OI），连续性待观察（方向未知）
11-20 450.0C — Vol 115 | 最新价 $2.93 | OI 464→520 (ΔOI +56张) | ΔOI/Volume 48.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增56张（+12.1% vs前日OI），连续性待观察（方向未知）
12-18 465.0C — Vol 56 | 最新价 $8.20 | OI 160→205 (ΔOI +45张) | ΔOI/Volume 80.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增45张（+28.1% vs前日OI），连续性待观察（方向未知）
11-20 427.5P — Vol 103 | 最新价 $3.35 | OI 368→408 (ΔOI +40张) | ΔOI/Volume 38.8% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增40张（+10.9% vs前日OI），值得跟踪（方向未知）
12-11 445.0C — Vol 40 | 最新价 $13.50 | OI 11→50 (ΔOI +39张) | ΔOI/Volume 97.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增39张（+354.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 261 张（Put 40 / Call 221），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +87 / P +0.1k ｜ Activity MEDIUM △ ｜ 3D
11-27  C +34 / P +58 ｜ Activity MEDIUM △ ｜ 10D
12-04  C +18 / P +26 ｜ Activity LOW ｜ 17D
12-11  C +51 / P +5 ｜ Activity MEDIUM △ ｜ 24D

📆 11-20 Forward Structure
存量OI: C 10.7k / P 10.7k，今日变化ΔOI: C +87 / P +0.1k，平值价格ATM: C $8.80 / P $7.20 ｜ ATM IV 47.0%，净 delta 敞口 562 shares
Top ΔOI: C 467 +81 ｜ C 450 +56 ｜ P 427 +40
仓位参考: Max Pain 410 ｜ Call Wall 420（-4.3%，弱）（OI 0.8k） ｜ Put Wall 410（-6.6%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 47.0%｜历史 Rank 82%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 562 股

11-27（MEDIUM △）Top ΔOI: 405P +26 ｜ 435P +12
11-27（MEDIUM △）仓位参考: Max Pain 430 ｜ Call Wall 430（-2.0%，弱）（OI 64） ｜ Put Wall 395（-10.0%，弱）（OI 0.2k）

12-04（Activity LOW）仓位参考: Max Pain 450 ｜ Call Wall 475（+8.2%，弱）（OI 81） ｜ Put Wall 405（-7.7%，弱）（OI 24）

12-11（MEDIUM △）Top ΔOI: 445C +39 ｜ 415P +2
12-11（MEDIUM △）仓位参考: Max Pain 440 ｜ Call Wall 450（+2.5%）（OI 0.1k） ｜ Put Wall 435（-0.9%）（OI 23）

📅 事件差分（观察，非因果）: 11-20（3D）ATM IV 47.0% vs 11-27 36.1%（差 +10.9pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/ISRG_morning.json