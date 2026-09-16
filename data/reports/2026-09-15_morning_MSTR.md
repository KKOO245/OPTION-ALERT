# 期权晨报 2026-09-15（快照 11:20 ET）

📊 市场环境

SPY $757.39 ｜ QQQ $nan
VIX 17.68 ↑3.4%（5D +12.5%） ｜ Vol Regime: NORMAL
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
🟡 **事件差分**: 09-18 ATM IV 89.0% vs 09-25 74.3%（差 +14.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 136.94 → 今开 131.65（-3.9%） | 较昨收变动（含盘初走势） ｜ 今日高 134.00 ｜ 低 128.50

Options: P/C成交量 1.21 | OI比 0.60 | ATM IV 89.0% | Skew -6.3pp | Term 0.80 | ExpMove ±6.7%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.3pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.60）+ 当日成交偏 Put（P/C量 1.21）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.21×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（3D）±6.7% ｜ 09-25（10D）±10.1% ｜ 10-02（17D）±12.6% ｜ 10-09（24D）±14.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 53,958,310 | GEX Change vs 上次快照 -27,015,830 | Flip: Primary Flip: 118.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 861 / LOW 104 / INVALID 233
结构观察区: Primary Flip 118.61（全链重定价，覆盖 100%）
最近结构参考: Flip 119（现价高于该位 9.2%）
量化视角： 正 Gamma（5396万，无历史分位）｜正 Gamma 减弱（2702万）｜现价位于 Flip 上方 9.20%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 122（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 119（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 80.0P — Vol 4,499 | 最新价 $0.02 | OI 30489→34942 (ΔOI +4453张) | ΔOI/Volume 99.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4453张（+14.6% vs前日OI），连续性待观察（方向未知）
09-18 200.0C — Vol 6,997 | 最新价 $0.04 | OI 22993→26257 (ΔOI +3264张) | ΔOI/Volume 46.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3264张（+14.2% vs前日OI），连续性待观察（方向未知）
09-18 150.0C — Vol 12,095 | 最新价 $1.42 | OI 16313→18330 (ΔOI +2017张) | ΔOI/Volume 16.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2017张（+12.4% vs前日OI），连续性待观察（方向未知）
09-18 155.0C — Vol 5,220 | 最新价 $0.86 | OI 2974→4847 (ΔOI +1873张) | ΔOI/Volume 35.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1873张（+63.0% vs前日OI），连续性待观察（方向未知）
09-18 120.0P — Vol 4,956 | 最新价 $0.43 | OI 8782→10338 (ΔOI +1556张) | ΔOI/Volume 31.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1556张（+17.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 13,163 张（Put 6,009 / Call 7,154），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +14.2k / P +12.3k ｜ Activity HIGH ｜ 3D
09-25  C +4.4k / P +2.4k ｜ Activity HIGH ｜ 10D
10-02  C +1.3k / P +2.6k ｜ Activity HIGH ｜ 17D
10-09  C +0.3k / P +2.2k ｜ Activity HIGH ｜ 24D

📆 09-18 Forward Structure
存量OI: C 474.7k / P 286.1k，今日变化ΔOI: C +14.2k / P +12.3k，平值价格ATM: C $4.60 / P $4.03 ｜ ATM IV 89.0%，净 delta 敞口 -371k shares
Top ΔOI: C 150 +2,017
仓位参考: Max Pain 122 ｜ Call Wall 140（+8.1%，弱）（OI 25.9k） ｜ Put Wall 120（-7.4%，弱）（OI 10.3k）
量化解读： 存量 Call 重｜ATM IV 89.0%｜历史 Rank 64%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 370,864 股

📆 09-25 Forward Structure
存量OI: C 30.0k / P 52.4k，今日变化ΔOI: C +4.4k / P +2.4k，平值价格ATM: C $6.59 / P $6.51 ｜ ATM IV 74.3%，净 delta 敞口 25k shares
仓位参考: Max Pain 127 ｜ Call Wall 140（+8.1%，弱）（OI 2.3k） ｜ Put Wall 125（-3.5%，弱）（OI 2.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 74.3%｜历史 Rank 64%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 24,732 股

📆 10-02 Forward Structure
存量OI: C 23.0k / P 36.6k，今日变化ΔOI: C +1.3k / P +2.6k，平值价格ATM: C $7.92 / P $8.45 ｜ ATM IV 71.4%，净 delta 敞口 -38k shares
仓位参考: Max Pain 130 ｜ Call Wall 140（+8.1%，弱）（OI 0.8k） ｜ Put Wall 130（+0.4%，弱）（OI 2.6k）
量化解读： 存量 Put 重｜ATM IV 71.4%｜历史 Rank 64%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 38,269 股

📆 10-09 Forward Structure
存量OI: C 6.3k / P 18.9k，今日变化ΔOI: C +0.3k / P +2.2k，平值价格ATM: C $9.53 / P $9.30 ｜ ATM IV 70.7%，净 delta 敞口 -43k shares
仓位参考: Max Pain 135 ｜ Call Wall 135（+4.2%，弱）（OI 0.3k） ｜ Put Wall 130（+0.4%，弱）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 70.7%｜历史 Rank 64%（近端代理）｜净 delta 敞口 负 43,100 股

📅 事件差分（观察，非因果）: 09-18（3D）ATM IV 89.0% vs 09-25 74.3%（差 +14.7pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/MSTR_morning.json