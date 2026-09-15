# 期权晚报 2026-09-15（快照 16:40 ET）

📊 市场环境

SPY $757.39 ｜ QQQ $704.54
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
🟡 **近现价集中开仓**: 09-25 150P ΔOI +1,174（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 148.45 → 收盘 143.49（-3.3%） ｜ 今日高 148.46 ｜ 低 142.87 ｜ 昨收 148.15 → 收盘 143.49（-3.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.77 | OI比 0.82 | ATM IV 62.5% | Skew 2.8pp | Term 0.81 | ExpMove ±4.5%（近端） | Rank 55%
量化视角： IV 中性（Rank 55%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价中性（Skew 2.8pp）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（3D）±4.5% ｜ 09-25（10D）±7.1% ｜ 10-02（17D）±9.0% ｜ 10-09（24D）±10.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,348,200 | GEX Change vs 上次快照 -16,737,186 | Flip: Primary Flip: 143.04（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 624 / LOW 119 / INVALID 313
结构观察区: Primary Flip 143.04（全链重定价，覆盖 100%）
最近结构参考: Flip 143（现价高于该位 0.3%）
量化视角： 正 Gamma（535万，无历史分位）｜正 Gamma 减弱（1674万）｜现价位于 Flip 上方 0.32%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 145（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 143（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 162.5C — Vol 3,360 | 最新价 $0.08 | OI 0→11634 (ΔOI +11634张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增11634张（前日OI缺失），值得跟踪（方向未知）
10-16 180.0C — Vol 1,866 | 最新价 $0.83 | OI 13889→23299 (ΔOI +9410张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9410张（+67.8% vs前日OI），连续性待观察（方向未知）
10-16 160.0C — Vol 8,723 | 最新价 $3.05 | OI 23783→33159 (ΔOI +9376张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9376张（+39.4% vs前日OI），连续性待观察（方向未知）
09-18 165.0C — Vol 15,018 | 最新价 $0.06 | OI 30116→39106 (ΔOI +8990张) | ΔOI/Volume 59.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8990张（+29.9% vs前日OI），连续性待观察（方向未知）
10-16 200.0C — Vol 2,367 | 最新价 $0.28 | OI 31475→37989 (ΔOI +6514张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6514张（+20.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 45,924 张（Put 0 / Call 45,924），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +28.1k / P +11.5k ｜ Activity MEDIUM △ ｜ 3D
09-25  C +6.9k / P +10.2k ｜ Activity HIGH ｜ 10D
10-02  C +1.4k / P +2.0k ｜ Activity HIGH ｜ 17D
10-09  C +1.0k / P +1.0k ｜ Activity HIGH ｜ 24D

📆 09-18 Forward Structure
存量OI: C 658.3k / P 537.4k，今日变化ΔOI: C +28.1k / P +11.5k，平值价格ATM: C $3.54 / P $2.96 ｜ ATM IV 62.5%，净 delta 敞口 -324k shares
Top ΔOI: C 162 +11,634 ｜ C 165 +8,990
仓位参考: Max Pain 145 ｜ Call Wall 155（+8.0%，弱）（OI 58.3k） ｜ Put Wall 150（+4.5%，弱）（OI 46.1k）
量化解读： 存量 Call 重｜ATM IV 62.5%｜历史 Rank 55%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 323,641 股

📆 09-25 Forward Structure
存量OI: C 70.3k / P 83.7k，今日变化ΔOI: C +6.9k / P +10.2k，平值价格ATM: C $5.40 / P $4.85 ｜ ATM IV 54.4%，净 delta 敞口 -229k shares
Top ΔOI: P 134 +4,865 ｜ P 150 +1,174
仓位参考: Max Pain 146 ｜ Call Wall 155（+8.0%，弱）（OI 5.2k） ｜ Put Wall 134（-6.6%，弱）（OI 5.2k）
量化解读： 存量 Put 重｜ATM IV 54.4%｜历史 Rank 55%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 228,707 股

📆 10-02 Forward Structure
存量OI: C 28.9k / P 38.6k，今日变化ΔOI: C +1.4k / P +2.0k，平值价格ATM: C $6.80 / P $6.11 ｜ ATM IV 52.2%，净 delta 敞口 -47k shares
Top ΔOI: P 135 +396 ｜ P 150 +335 ｜ P 134 +246
仓位参考: Max Pain 145 ｜ Call Wall 150（+4.5%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 52.2%｜历史 Rank 55%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 47,013 股

📆 10-09 Forward Structure
存量OI: C 13.0k / P 14.9k，今日变化ΔOI: C +1.0k / P +1.0k，平值价格ATM: C $7.85 / P $6.92 ｜ ATM IV 50.9%，净 delta 敞口 -17k shares
Top ΔOI: P 137 +329
仓位参考: Max Pain 147 ｜ Call Wall 150（+4.5%，弱）（OI 0.8k） ｜ Put Wall 135（-5.9%）（OI 2.9k）
量化解读： 存量两侧均衡｜ATM IV 50.9%｜历史 Rank 55%（近端代理）｜净 delta 敞口 负 17,380 股

📅 事件差分（观察，非因果）: 09-18（3D）ATM IV 62.5% vs 09-25 54.4%（差 +8.1pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/SPCX_evening.json