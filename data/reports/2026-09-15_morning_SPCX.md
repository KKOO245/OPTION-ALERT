# 期权晨报 2026-09-15（快照 11:20 ET）

📊 市场环境

SPY $758.10 ｜ QQQ $704.54
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
🟡 **近现价集中开仓**: 09-25 150P ΔOI +1,174（距现价 +3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 148.15 → 今开 148.45（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 148.46 ｜ 低 144.22

Options: P/C成交量 0.36 | OI比 0.82 | ATM IV 60.3% | Skew 0.9pp | Term 0.83 | ExpMove ±4.5%（近端） | Rank 50%
量化视角： IV 中性（Rank 50%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价薄（Skew 0.9pp）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（3D）±4.5% ｜ 09-25（10D）±7.2% ｜ 10-02（17D）±8.9% ｜ 10-09（24D）±10.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 22,085,387 | GEX Change vs 上次快照 -37,644,550 | Flip: Primary Flip: 143.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 626 / LOW 116 / INVALID 314
结构观察区: Primary Flip 143.61（全链重定价，覆盖 97%）
最近结构参考: Flip 144（现价高于该位 1.1%）
量化视角： 正 Gamma（2209万，无历史分位）｜正 Gamma 减弱（3764万）｜现价位于 Flip 上方 1.14%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 145（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 144（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 162.5C — Vol 14,383 | 最新价 $0.33 | OI 0→11634 (ΔOI +11634张) | ΔOI/Volume 80.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11634张（前日OI缺失），连续性待观察（方向未知）
10-16 180.0C — Vol 12,888 | 最新价 $1.28 | OI 13889→23299 (ΔOI +9410张) | ΔOI/Volume 73.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9410张（+67.8% vs前日OI），连续性待观察（方向未知）
10-16 160.0C — Vol 16,784 | 最新价 $4.55 | OI 23783→33159 (ΔOI +9376张) | ΔOI/Volume 55.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9376张（+39.4% vs前日OI），连续性待观察（方向未知）
09-18 165.0C — Vol 36,045 | 最新价 $0.22 | OI 30116→39106 (ΔOI +8990张) | ΔOI/Volume 24.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8990张（+29.9% vs前日OI），连续性待观察（方向未知）
10-16 200.0C — Vol 7,710 | 最新价 $0.43 | OI 31475→37989 (ΔOI +6514张) | ΔOI/Volume 84.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6514张（+20.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 45,924 张（Put 0 / Call 45,924），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +28.1k / P +11.5k ｜ Activity HIGH ｜ 3D
09-25  C +6.9k / P +10.2k ｜ Activity HIGH ｜ 10D
10-02  C +1.4k / P +2.0k ｜ Activity HIGH ｜ 17D
10-09  C +1.0k / P +1.0k ｜ Activity HIGH ｜ 24D

📆 09-18 Forward Structure
存量OI: C 658.3k / P 537.4k，今日变化ΔOI: C +28.1k / P +11.5k，平值价格ATM: C $3.42 / P $3.12 ｜ ATM IV 60.3%，净 delta 敞口 -188k shares
Top ΔOI: C 162 +11,634 ｜ C 165 +8,990
仓位参考: Max Pain 145 ｜ Call Wall 155（+6.7%，弱）（OI 58.3k） ｜ Put Wall 150（+3.3%，弱）（OI 46.1k）
量化解读： 存量 Call 重｜ATM IV 60.3%｜历史 Rank 50%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 188,101 股

📆 09-25 Forward Structure
存量OI: C 70.3k / P 83.7k，今日变化ΔOI: C +6.9k / P +10.2k，平值价格ATM: C $5.25 / P $5.14 ｜ ATM IV 53.2%，净 delta 敞口 -175k shares
Top ΔOI: P 134 +4,865 ｜ P 150 +1,174
仓位参考: Max Pain 146 ｜ Call Wall 155（+6.7%，弱）（OI 5.2k） ｜ Put Wall 134（-7.7%，弱）（OI 5.2k）
量化解读： 存量 Put 重｜ATM IV 53.2%｜历史 Rank 50%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 175,241 股

📆 10-02 Forward Structure
存量OI: C 28.9k / P 38.6k，今日变化ΔOI: C +1.4k / P +2.0k，平值价格ATM: C $6.70 / P $6.20 ｜ ATM IV 51.5%，净 delta 敞口 -38k shares
Top ΔOI: P 135 +396 ｜ P 150 +335 ｜ P 134 +246
仓位参考: Max Pain 145 ｜ Call Wall 150（+3.3%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 51.5%｜历史 Rank 50%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 37,643 股

📆 10-09 Forward Structure
存量OI: C 13.0k / P 14.9k，今日变化ΔOI: C +1.0k / P +1.0k，平值价格ATM: C $7.65 / P $7.22 ｜ ATM IV 50.2%，净 delta 敞口 -13k shares
Top ΔOI: P 137 +329
仓位参考: Max Pain 147 ｜ Call Wall 150（+3.3%，弱）（OI 0.8k） ｜ Put Wall 135（-7.1%）（OI 2.9k）
量化解读： 存量两侧均衡｜ATM IV 50.2%｜历史 Rank 50%（近端代理）｜净 delta 敞口 负 13,160 股

📅 事件差分（观察，非因果）: 09-18（3D）ATM IV 60.3% vs 09-25 53.2%（差 +7.1pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/SPCX_morning.json