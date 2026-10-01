# 期权晨报 2026-10-01（快照 10:20 ET）

📊 市场环境

SPY $760.36 ｜ QQQ $737.43
VIX 17.57 ↑7.5%（5D +12.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-01

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 54.5 ｜ 前值 54.6　✅ 今日已公布
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 10-02（1D）ATM IV 91.5% vs 10-09 75.3%（差 +16.1pp），覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-02 282C ΔOI +670（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 276.98 → 今开 284.62（+2.8%） | 较昨收变动（含盘初走势） ｜ 今日高 287.15 ｜ 低 275.77

Options: P/C成交量 0.55 | OI比 1.10 | ATM IV 91.5% | Skew -2.7pp | Term 0.90 | ExpMove ±4.3%（近端） | Rank 53%
量化视角： IV 中性（Rank 53%）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.7pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.10×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（1D）±4.3% ｜ 10-09（8D）±8.6% ｜ 10-16（15D）±12.1% ｜ 10-23（22D）±14.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,364,980 | GEX Change vs 上次快照 -280,352 | Flip: Primary Flip: 273.65（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 639 / LOW 93 / INVALID 158
结构观察区: Primary Flip 273.65（全链重定价，覆盖 100%）
Call Wall 300（弱结构｜现价低于该位 7.9%）
最近结构参考: Flip 274（现价高于该位 1.0%）
量化视角： 正 Gamma（236万，无历史分位）｜正 Gamma 减弱（28万）｜现价位于 Flip 上方 0.98%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 280（MaxPain，仅结算参考） / 300（Call Wall，弱结构）。
• Gamma 区域：切换参考 274（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 310.0C — Vol 2,582 | 最新价 $7.00 | OI 2348→4114 (ΔOI +1766张) | ΔOI/Volume 68.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1766张（+75.2% vs前日OI），连续性待观察（方向未知）
10-02 282.5C — Vol 1,563 | 最新价 $4.88 | OI 355→1025 (ΔOI +670张) | ΔOI/Volume 42.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增670张（+188.7% vs前日OI），连续性待观察（方向未知）
10-09 290.0C — Vol 989 | 最新价 $8.25 | OI 250→874 (ΔOI +624张) | ΔOI/Volume 63.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增624张（+249.6% vs前日OI），连续性待观察（方向未知）
10-30 190.0P — Vol 678 | 最新价 $1.26 | OI 455→1073 (ΔOI +618张) | ΔOI/Volume 91.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增618张（+135.8% vs前日OI），连续性待观察（方向未知）
10-02 290.0C — Vol 2,040 | 最新价 $2.70 | OI 2232→2713 (ΔOI +481张) | ΔOI/Volume 23.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增481张（+21.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,159 张（Put 618 / Call 3,541），跨 4 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +0.9k / P +1.8k ｜ Activity HIGH ｜ 1D
10-09  C +2.5k / P +2.8k ｜ Activity HIGH ｜ 8D
10-16  C +2.0k / P +1.8k ｜ Activity MEDIUM △ ｜ 15D
10-23  C +1.2k / P +0.9k ｜ Activity MEDIUM △ ｜ 22D

📆 10-02 Forward Structure
存量OI: C 50.4k / P 55.3k，今日变化ΔOI: C +0.9k / P +1.8k，平值价格ATM: C $6.13 / P $5.80 ｜ ATM IV 91.5%，净 delta 敞口 -20k shares
Top ΔOI: C 282 +670 ｜ C 290 +481 ｜ P 270 +447
仓位参考: Max Pain 280 ｜ Call Wall 300（+8.6%）（OI 5.2k） ｜ Put Wall 260（-5.9%，弱）（OI 3.2k）
量化解读： 存量两侧均衡｜ATM IV 91.5%｜历史 Rank 53%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 19,981 股

📆 10-09 Forward Structure
存量OI: C 15.1k / P 19.1k，今日变化ΔOI: C +2.5k / P +2.8k，平值价格ATM: C $12.80 / P $11.00 ｜ ATM IV 75.3%，净 delta 敞口 41k shares
Top ΔOI: C 290 +624 ｜ C 277 +441 ｜ P 250 +365
仓位参考: Max Pain 272 ｜ Call Wall 300（+8.6%，弱）（OI 1.0k） ｜ Put Wall 250（-9.5%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜ATM IV 75.3%｜历史 Rank 53%（近端代理）｜IV/RV 0.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 41,038 股

10-16（MEDIUM △）Top ΔOI: 310C +1,766 ｜ 245P +214
10-16（MEDIUM △）仓位参考: Max Pain 260 ｜ Call Wall 270（-2.3%，弱）（OI 8.3k） ｜ Put Wall 260（-5.9%，弱）（OI 3.7k）

10-23（MEDIUM △）Top ΔOI: 300C +226
10-23（MEDIUM △）仓位参考: Max Pain 270 ｜ Call Wall 300（+8.6%，弱）（OI 1.0k） ｜ Put Wall 280（+1.3%，弱）（OI 0.6k）

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 91.5% vs 10-09 75.3%（差 +16.1pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/BE_morning.json