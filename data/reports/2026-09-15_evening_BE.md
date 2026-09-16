# 期权晚报 2026-09-15（快照 18:31 ET）

📊 市场环境

SPY $757.39 ｜ QQQ $nan
VIX 17.20 ↑0.6%（5D +9.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
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
🟡 **事件差分**: 09-18 ATM IV 93.2% vs 09-25 81.8%（差 +11.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 261.00 → 收盘 259.35（-0.6%） ｜ 今日高 269.83 ｜ 低 257.09 ｜ 昨收 257.05 → 收盘 259.35（+0.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.75 | OI比 0.86 | ATM IV 93.2% | Skew -0.5pp | Term 0.85 | ExpMove ±6.8%（近端） | Rank 55%
量化视角： IV 中性（Rank 55%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.75×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（3D）±6.8% ｜ 09-25（10D）±10.9% ｜ 10-02（17D）±13.7% ｜ 10-09（24D）±16.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 20,089,547 | GEX Change vs 上次快照 -2,360,958 | Flip: Primary Flip: 229.17（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 669 / LOW 101 / INVALID 190
结构观察区: Primary Flip 229.17（全链重定价，覆盖 100%）
Call Wall 250（弱结构｜现价高于该位 3.7%）
最近结构参考: Call Wall 250（现价高于该位 3.7%）
量化视角： 正 Gamma（2009万，无历史分位）｜正 Gamma 减弱（236万）｜现价位于 Flip 上方 13.17%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 240（MaxPain，仅结算参考） / 250（Call Wall，弱结构）。
• Gamma 区域：切换参考 229（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 305.0C — Vol 553 | 最新价 $0.39 | OI 1119→2396 (ΔOI +1277张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1277张（+114.1% vs前日OI），连续性待观察（方向未知）
09-25 150.0P — Vol 4 | 最新价 $0.03 | OI 716→1961 (ΔOI +1245张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1245张（+173.9% vs前日OI），连续性待观察（方向未知）
09-18 262.5C — Vol 801 | 最新价 $6.89 | OI 285→1266 (ΔOI +981张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增981张（+344.2% vs前日OI），连续性待观察（方向未知）
09-25 295.0C — Vol 335 | 最新价 $3.80 | OI 109→970 (ΔOI +861张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增861张（+789.9% vs前日OI），连续性待观察（方向未知）
10-16 300.0C — Vol 1,071 | 最新价 $10.90 | OI 3599→4458 (ΔOI +859张) | ΔOI/Volume 80.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增859张（+23.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,223 张（Put 1,245 / Call 3,978），跨 3 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 3D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 10D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 17D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 09-18 Forward Structure
存量OI: C 146.5k / P 126.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $8.55 / P $9.15 ｜ ATM IV 93.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 240 ｜ Call Wall 250（-3.6%）（OI 21.4k） ｜ Put Wall 240（-7.5%，弱）（OI 3.7k）
量化解读： 存量两侧均衡｜ATM IV 93.2%｜历史 Rank 55%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 245 ｜ Call Wall 280（+8.0%，弱）（OI 1.7k） ｜ Put Wall 245（-5.5%，弱）（OI 1.3k）

10-02（Activity LOW）仓位参考: Max Pain 245 ｜ Call Wall 275（+6.0%，弱）（OI 1.8k） ｜ Put Wall 245（-5.5%，弱）（OI 1.0k）

10-09（Activity LOW）仓位参考: Max Pain 250 ｜ Call Wall 250（-3.6%，弱）（OI 0.2k） ｜ Put Wall 240（-7.5%）（OI 1.4k）

📅 事件差分（观察，非因果）: 09-18（3D）ATM IV 93.2% vs 09-25 81.8%（差 +11.4pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/BE_evening.json