# 期权晨报 2026-09-21（快照 10:20 ET）

📊 市场环境

SPY $773.06 ｜ QQQ $741.47
VIX 14.85 ↑0.3%（5D -13.2%） ｜ Vol Regime: LOW
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
🟡 **近现价集中开仓**: 09-25 255P ΔOI +1,197（距现价 -4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 265.63 → 今开 270.00（+1.6%） | 较昨收变动（含盘初走势） ｜ 今日高 275.99 ｜ 低 265.36

Options: P/C成交量 0.74 | OI比 1.35 | ATM IV 83.8% | Skew -1.4pp | Term 0.91 | ExpMove ±7.3%（近端） | Rank 43%
量化视角： IV 中性（Rank 43%）｜期限结构正常（Term 0.91）｜Put 保护异常便宜（Skew -1.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.74×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.35×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（4D）±7.3% ｜ 10-02（11D）±10.6% ｜ 10-09（18D）±13.6% ｜ 10-16（25D）±16.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,253,507 | GEX Change vs 上次快照 -1,226,742 | Flip: Primary Flip: 253.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 544 / LOW 82 / INVALID 302
结构观察区: Primary Flip 253.67（全链重定价，覆盖 100%）
Call Wall 270（弱结构｜现价低于该位 1.4%）
最近结构参考: Call Wall 270（现价低于该位 1.4%）
量化视角： 正 Gamma（525万，无历史分位）｜正 Gamma 减弱（123万）｜现价位于 Flip 上方 4.97%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 260（MaxPain，仅结算参考）；上方 270（Call Wall，弱结构）。
• Gamma 区域：切换参考 254（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 125.0P — Vol 2,033 | 最新价 $0.10 | OI 3033→4898 (ΔOI +1865张) | ΔOI/Volume 91.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1865张（+61.5% vs前日OI），连续性待观察（方向未知）
09-25 250.0P — Vol 2,347 | 最新价 $4.40 | OI 1841→3423 (ΔOI +1582张) | ΔOI/Volume 67.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1582张（+85.9% vs前日OI），连续性待观察（方向未知）
09-25 255.0P — Vol 1,375 | 最新价 $5.88 | OI 344→1541 (ΔOI +1197张) | ΔOI/Volume 87.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1197张（+348.0% vs前日OI），连续性待观察（方向未知）
09-25 245.0C — Vol 2,420 | 最新价 $24.08 | OI 435→1612 (ΔOI +1177张) | ΔOI/Volume 48.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1177张（+270.6% vs前日OI），连续性待观察（方向未知）
09-25 315.0C — Vol 1,587 | 最新价 $1.23 | OI 236→1322 (ΔOI +1086张) | ΔOI/Volume 68.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1086张（+460.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,907 张（Put 4,644 / Call 2,263），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +6.8k / P +8.4k ｜ Activity HIGH ｜ 4D
10-02  C +1.3k / P +1.9k ｜ Activity MEDIUM △ ｜ 11D
10-09  C +0.5k / P +0.5k ｜ Activity MEDIUM △ ｜ 18D
10-16  C +0.9k / P +3.9k ｜ Activity HIGH ｜ 25D

📆 09-25 Forward Structure
存量OI: C 28.8k / P 38.8k，今日变化ΔOI: C +6.8k / P +8.4k，平值价格ATM: C $9.20 / P $10.20 ｜ ATM IV 83.8%，净 delta 敞口 8k shares
Top ΔOI: P 250 +1,582 ｜ P 255 +1,197 ｜ C 245 +1,177
仓位参考: Max Pain 260 ｜ Call Wall 280（+5.2%，弱）（OI 2.6k） ｜ Put Wall 250（-6.1%，弱）（OI 3.4k）
量化解读： 存量 Put 重｜ATM IV 83.8%｜历史 Rank 43%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 7,739 股

10-02（MEDIUM △）Top ΔOI: 300C +478 ｜ 245P +289
10-02（MEDIUM △）仓位参考: Max Pain 250 ｜ Call Wall 270（+1.4%）（OI 5.4k） ｜ Put Wall 245（-8.0%）（OI 1.4k）

10-09（MEDIUM △）Top ΔOI: 270C +99
10-09（MEDIUM △）仓位参考: Max Pain 250 ｜ Call Wall 260（-2.4%，弱）（OI 0.2k） ｜ Put Wall 240（-9.9%）（OI 1.5k）

📆 10-16 Forward Structure
存量OI: C 61.6k / P 66.1k，今日变化ΔOI: C +0.9k / P +3.9k，平值价格ATM: C $21.95 / P $20.72 ｜ ATM IV 75.9%，净 delta 敞口 -17k shares
Top ΔOI: P 210 +770 ｜ P 230 +763
仓位参考: Max Pain 250 ｜ Call Wall 280（+5.2%，弱）（OI 9.0k） ｜ Put Wall 240（-9.9%，弱）（OI 3.8k）
量化解读： 存量两侧均衡｜ATM IV 75.9%｜历史 Rank 43%（近端代理）｜IV/RV 1.03×（近似）｜净 delta 敞口 负 17,348 股

📅 事件差分（观察，非因果）: 09-25（4D）ATM IV 83.8% vs 10-02 77.2%（差 +6.6pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/BE_morning.json