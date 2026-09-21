# 期权晨报 2026-09-21（快照 10:20 ET）

📊 市场环境

SPY $767.46 ｜ QQQ $734.26
VIX 14.85 ↑0.3%（5D -13.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 32.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 220P ΔOI +3,004（距现价 -1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 223.54 → 今开 225.99（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 229.75 ｜ 低 221.30

Options: P/C成交量 0.41 | OI比 0.99 | ATM IV 87.1% | Skew -2.2pp | Term 0.91 | ExpMove ±7.4%（近端） | Rank 19%
量化视角： IV 历史低位（Rank 19%，期权偏便宜）｜期限结构正常（Term 0.91）｜Put 保护异常便宜（Skew -2.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.41×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.99×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（4D）±7.4% ｜ 10-02（11D）±10.8% ｜ 10-09（18D）±14.2% ｜ 10-16（25D）±0.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,941,957 | GEX Change vs 上次快照 281,297 | Flip: Primary Flip: 215.01（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 491 / LOW 37 / INVALID 198
结构观察区: Primary Flip 215.01（全链重定价，覆盖 100%）
最近结构参考: Flip 215（现价高于该位 4.0%）
量化视角： 正 Gamma（494万，无历史分位）｜正 Gamma 增强（+28万）｜现价位于 Flip 上方 3.95%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 215（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 220.0P — Vol 4,348 | 最新价 $7.35 | OI 553→3557 (ΔOI +3004张) | ΔOI/Volume 69.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3004张（+543.2% vs前日OI），连续性待观察（方向未知）
10-16 100.0P — Vol 3,957 | 最新价 $0.07 | OI 1333→4162 (ΔOI +2829张) | ΔOI/Volume 71.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2829张（+212.2% vs前日OI），连续性待观察（方向未知）
09-25 230.0C — Vol 8,709 | 最新价 $6.42 | OI 2326→4804 (ΔOI +2478张) | ΔOI/Volume 28.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2478张（+106.5% vs前日OI），连续性待观察（方向未知）
10-02 220.0P — Vol 1,525 | 最新价 $10.96 | OI 352→1811 (ΔOI +1459张) | ΔOI/Volume 95.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1459张（+414.5% vs前日OI），连续性待观察（方向未知）
10-16 300.0C — Vol 3,513 | 最新价 $3.07 | OI 5306→6710 (ΔOI +1404张) | ΔOI/Volume 40.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1404张（+26.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,174 张（Put 7,292 / Call 3,882），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +8.5k / P +10.5k ｜ Activity HIGH ｜ 4D
10-02  C +2.4k / P +2.7k ｜ Activity HIGH ｜ 11D
10-09  C +0.7k / P +1.2k ｜ Activity HIGH ｜ 18D
10-16  C +6.3k / P +5.2k ｜ Activity MEDIUM △ ｜ 25D

📆 09-25 Forward Structure
存量OI: C 44.1k / P 43.5k，今日变化ΔOI: C +8.5k / P +10.5k，平值价格ATM: C $8.95 / P $7.60 ｜ ATM IV 87.1%，净 delta 敞口 9k shares
Top ΔOI: P 220 +3,004 ｜ C 230 +2,478 ｜ P 210 +1,388
仓位参考: Max Pain 220 ｜ Call Wall 230（+2.9%，弱）（OI 4.8k） ｜ Put Wall 220（-1.6%，弱）（OI 3.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 87.1%｜历史 Rank 19%（近端代理）｜IV/RV 1.49×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 9,205 股

📆 10-02 Forward Structure
存量OI: C 14.0k / P 14.9k，今日变化ΔOI: C +2.4k / P +2.7k，平值价格ATM: C $13.64 / P $10.45 ｜ ATM IV 81.4%，净 delta 敞口 3k shares
Top ΔOI: P 220 +1,459 ｜ C 210 +785 ｜ P 197 +447
仓位参考: Max Pain 220 ｜ Call Wall 210（-6.0%，弱）（OI 1.1k） ｜ Put Wall 220（-1.6%，弱）（OI 1.8k）
量化解读： 存量两侧均衡｜ATM IV 81.4%｜历史 Rank 19%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,408 股

📆 10-09 Forward Structure
存量OI: C 8.7k / P 9.1k，今日变化ΔOI: C +0.7k / P +1.2k，平值价格ATM: C $16.72 / P $15.08 ｜ ATM IV 80.3%，净 delta 敞口 -356 shares
Top ΔOI: P 210 +338 ｜ C 225 +286 ｜ P 205 +275
仓位参考: Max Pain 220 ｜ Call Wall 240（+7.4%）（OI 1.7k） ｜ Put Wall 210（-6.0%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜ATM IV 80.3%｜历史 Rank 19%（近端代理）｜IV/RV 1.37×（近似）｜净 delta 敞口 负 356 股

10-16（MEDIUM △）Top ΔOI: 300C +1,404 ｜ 175P +937
10-16（MEDIUM △）仓位参考: Max Pain 210 ｜ Call Wall 240（+7.4%，弱）（OI 4.8k） ｜ Put Wall 210（-6.0%，弱）（OI 3.1k）

📅 事件差分（观察，非因果）: 09-25（4D）ATM IV 87.1% vs 10-02 81.4%（差 +5.7pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/NBIS_morning.json