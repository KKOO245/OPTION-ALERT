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
🟡 **近现价集中开仓**: 10-09 270C ΔOI +99（距现价 -1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 270.00 → 收盘 272.89（+1.1%） ｜ 今日高 282.00 ｜ 低 265.36 ｜ 昨收 265.63 → 收盘 272.89（+2.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.60 | OI比 1.35 | ATM IV 85.8% | Skew -3.3pp | Term 0.92 | ExpMove ±7.2%（近端） | Rank 46%
量化视角： IV 中性（Rank 46%）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -3.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.35×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（4D）±7.2% ｜ 10-02（11D）±10.5% ｜ 10-09（18D）±15.2% ｜ 10-16（25D）±16.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 7,563,554 | GEX Change vs 上次快照 2,310,046 | Flip: Primary Flip: 253.64（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 608 / LOW 82 / INVALID 238
结构观察区: Primary Flip 253.64（全链重定价，覆盖 100%）
Call Wall 270（弱结构｜现价高于该位 1.1%）
最近结构参考: Call Wall 270（现价高于该位 1.1%）
量化视角： 正 Gamma（756万，无历史分位）｜正 Gamma 增强（+231万）｜现价位于 Flip 上方 7.59%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 260（MaxPain，仅结算参考） / 270（Call Wall，弱结构）。
• Gamma 区域：切换参考 254（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 125.0P — Vol 22 | 最新价 $0.04 | OI 3033→4898 (ΔOI +1865张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1865张（+61.5% vs前日OI），连续性待观察（方向未知）
09-25 250.0P — Vol 2,251 | 最新价 $2.00 | OI 1841→3423 (ΔOI +1582张) | ΔOI/Volume 70.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1582张（+85.9% vs前日OI），连续性待观察（方向未知）
09-25 255.0P — Vol 1,101 | 最新价 $3.00 | OI 344→1541 (ΔOI +1197张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1197张（+348.0% vs前日OI），连续性待观察（方向未知）
09-25 245.0C — Vol 56 | 最新价 $29.90 | OI 435→1612 (ΔOI +1177张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1177张（+270.6% vs前日OI），连续性待观察（方向未知）
09-25 315.0C — Vol 579 | 最新价 $0.93 | OI 236→1322 (ΔOI +1086张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1086张（+460.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,907 张（Put 4,644 / Call 2,263），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +6.8k / P +8.4k ｜ Activity HIGH ｜ 4D
10-02  C +1.3k / P +1.9k ｜ Activity HIGH ｜ 11D
10-09  C +0.5k / P +0.5k ｜ Activity HIGH ｜ 18D
10-16  C +0.9k / P +3.9k ｜ Activity HIGH ｜ 25D

📆 09-25 Forward Structure
存量OI: C 28.8k / P 38.8k，今日变化ΔOI: C +6.8k / P +8.4k，平值价格ATM: C $10.50 / P $9.10 ｜ ATM IV 85.8%，净 delta 敞口 102k shares
Top ΔOI: P 250 +1,582 ｜ P 255 +1,197 ｜ C 245 +1,177
仓位参考: Max Pain 260 ｜ Call Wall 300（+9.9%，弱）（OI 2.8k） ｜ Put Wall 250（-8.4%，弱）（OI 3.4k）
量化解读： 存量 Put 重｜ATM IV 85.8%｜历史 Rank 46%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 101,899 股

📆 10-02 Forward Structure
存量OI: C 17.9k / P 15.4k，今日变化ΔOI: C +1.3k / P +1.9k，平值价格ATM: C $15.65 / P $13.00 ｜ ATM IV 79.2%，净 delta 敞口 7k shares
Top ΔOI: C 300 +478 ｜ P 245 +289 ｜ P 235 +276
仓位参考: Max Pain 250 ｜ Call Wall 270（-1.1%）（OI 5.4k） ｜ Put Wall 250（-8.4%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 79.2%｜历史 Rank 46%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 6,565 股

📆 10-09 Forward Structure
存量OI: C 3.9k / P 7.3k，今日变化ΔOI: C +0.5k / P +0.5k，平值价格ATM: C $20.56 / P $20.96 ｜ ATM IV 78.6%，净 delta 敞口 4k shares
Top ΔOI: C 270 +99
仓位参考: Max Pain 250 ｜ Call Wall 295（+8.1%）（OI 0.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 78.6%｜历史 Rank 46%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,286 股

📆 10-16 Forward Structure
存量OI: C 61.6k / P 66.1k，今日变化ΔOI: C +0.9k / P +3.9k，平值价格ATM: C $23.30 / P $21.10 ｜ ATM IV 78.1%，净 delta 敞口 -7k shares
Top ΔOI: P 210 +770 ｜ P 230 +763
仓位参考: Max Pain 250 ｜ Call Wall 280（+2.6%，弱）（OI 9.0k） ｜ Put Wall 260（-4.7%，弱）（OI 3.5k）
量化解读： 存量两侧均衡｜ATM IV 78.1%｜历史 Rank 46%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 负 6,790 股

📅 事件差分（观察，非因果）: 09-25（4D）ATM IV 85.8% vs 10-02 79.2%（差 +6.5pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/BE_evening.json