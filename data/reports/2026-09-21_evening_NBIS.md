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
🟡 **近现价集中开仓**: 09-25 230C ΔOI +2,478（距现价 -1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 225.99 → 收盘 232.80（+3.0%） ｜ 今日高 237.96 ｜ 低 221.30 ｜ 昨收 223.54 → 收盘 232.80（+4.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.42 | OI比 0.99 | ATM IV 88.6% | Skew -2.2pp | Term 0.94 | ExpMove ±7.5%（近端） | Rank 22%
量化视角： IV 历史低位（Rank 22%，期权偏便宜）｜期限结构正常（Term 0.94）｜Put 保护异常便宜（Skew -2.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.99×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（4D）±7.5% ｜ 10-02（11D）±11.6% ｜ 10-09（18D）±14.6% ｜ 10-16（25D）±17.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,760,543 | GEX Change vs 上次快照 3,818,587 | Flip: Primary Flip: 215.57（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 519 / LOW 35 / INVALID 172
结构观察区: Primary Flip 215.57（全链重定价，覆盖 100%）
最近结构参考: Flip 216（现价高于该位 8.0%）
量化视角： 正 Gamma（876万，无历史分位）｜正 Gamma 增强（+382万）｜现价位于 Flip 上方 7.99%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 216（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 220.0P — Vol 3,689 | 最新价 $3.50 | OI 553→3557 (ΔOI +3004张) | ΔOI/Volume 81.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3004张（+543.2% vs前日OI），连续性待观察（方向未知）
10-16 100.0P — Vol 34 | 最新价 $0.07 | OI 1333→4162 (ΔOI +2829张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2829张（+212.2% vs前日OI），连续性待观察（方向未知）
09-25 230.0C — Vol 6,089 | 最新价 $10.20 | OI 2326→4804 (ΔOI +2478张) | ΔOI/Volume 40.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2478张（+106.5% vs前日OI），连续性待观察（方向未知）
10-02 220.0P — Vol 440 | 最新价 $7.30 | OI 352→1811 (ΔOI +1459张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1459张（+414.5% vs前日OI），连续性待观察（方向未知）
10-16 300.0C — Vol 2,565 | 最新价 $4.37 | OI 5306→6710 (ΔOI +1404张) | ΔOI/Volume 54.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1404张（+26.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,174 张（Put 7,292 / Call 3,882），跨 3 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +8.5k / P +10.5k ｜ Activity HIGH ｜ 4D
10-02  C +2.4k / P +2.7k ｜ Activity HIGH ｜ 11D
10-09  C +0.7k / P +1.2k ｜ Activity HIGH ｜ 18D
10-16  C +6.3k / P +5.2k ｜ Activity HIGH ｜ 25D

📆 09-25 Forward Structure
存量OI: C 44.1k / P 43.5k，今日变化ΔOI: C +8.5k / P +10.5k，平值价格ATM: C $9.00 / P $8.50 ｜ ATM IV 88.6%，净 delta 敞口 216k shares
Top ΔOI: P 220 +3,004 ｜ C 230 +2,478 ｜ P 210 +1,388
仓位参考: Max Pain 220 ｜ Call Wall 230（-1.2%，弱）（OI 4.8k） ｜ Put Wall 220（-5.5%，弱）（OI 3.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 88.6%｜历史 Rank 22%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 216,147 股

📆 10-02 Forward Structure
存量OI: C 14.0k / P 14.9k，今日变化ΔOI: C +2.4k / P +2.7k，平值价格ATM: C $14.00 / P $12.90 ｜ ATM IV 81.9%，净 delta 敞口 41k shares
Top ΔOI: P 220 +1,459 ｜ C 210 +785 ｜ P 197 +447
仓位参考: Max Pain 220 ｜ Call Wall 210（-9.8%，弱）（OI 1.1k） ｜ Put Wall 220（-5.5%，弱）（OI 1.8k）
量化解读： 存量两侧均衡｜ATM IV 81.9%｜历史 Rank 22%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 40,894 股

📆 10-09 Forward Structure
存量OI: C 8.7k / P 9.1k，今日变化ΔOI: C +0.7k / P +1.2k，平值价格ATM: C $17.70 / P $16.35 ｜ ATM IV 82.5%，净 delta 敞口 14k shares
Top ΔOI: P 210 +338 ｜ C 225 +286 ｜ P 205 +275
仓位参考: Max Pain 220 ｜ Call Wall 240（+3.1%）（OI 1.7k） ｜ Put Wall 210（-9.8%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜ATM IV 82.5%｜历史 Rank 22%（近端代理）｜IV/RV 1.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 13,648 股

📆 10-16 Forward Structure
存量OI: C 49.0k / P 72.2k，今日变化ΔOI: C +6.3k / P +5.2k，平值价格ATM: C $23.05 / P $18.51 ｜ ATM IV 81.3%，净 delta 敞口 231k shares
Top ΔOI: C 300 +1,404 ｜ P 175 +937
仓位参考: Max Pain 210 ｜ Call Wall 240（+3.1%，弱）（OI 4.8k） ｜ Put Wall 210（-9.8%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 81.3%｜历史 Rank 22%（近端代理）｜IV/RV 1.39×（近似）｜净 delta 敞口 正 231,361 股

📅 事件差分（观察，非因果）: 09-25（4D）ATM IV 88.6% vs 10-02 81.9%（差 +6.6pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/NBIS_evening.json