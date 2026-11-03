# 期权晨报 2026-11-03（快照 10:20 ET）

📊 市场环境

SPY $755.37 ｜ QQQ $685.28
VIX 21.03 ↓0.6%（5D +20.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-03

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.1 ｜ 实际 7.523 ｜ 前值 7.19　✅ 今日已公布
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **事件差分**: 11-06（3D）ATM IV 79.7% vs 11-13 60.9%（差 +18.8pp），覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-13 170P ΔOI +552（距现价 -0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 178.34 → 今开 167.90（-5.9%） | 较昨收变动（含盘初走势） ｜ 今日高 172.66 ｜ 低 165.25

Options: P/C成交量 0.70 | OI比 1.20 | ATM IV 79.7% | Skew 1.4pp | Term 0.64 | ExpMove ±5.9%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.64，近月 IV 高于远月）｜保护溢价薄（Skew 1.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.70×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.20×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（3D）±5.9% ｜ 11-13（10D）±8.0% ｜ 11-20（17D）±9.9% ｜ 11-27（24D）±11.2%
   ⇒ IV–VIX Spread: +58.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -19,399,524 | GEX Change vs 上次快照 -25,995,053 | Flip: Primary Flip: 177.94（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 678 / LOW 66 / INVALID 162
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 177.94（全链重定价，覆盖 100%）
最近结构参考: Flip 178（现价低于该位 4.1%）
量化视角： 负 Gamma（1940万，无历史分位）｜由正转负（2600万）｜现价位于 Flip 下方 4.12%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 188（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 178（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 225.0C — Vol 16,046 | 最新价 $0.79 | OI 2526→13008 (ΔOI +10482张) | ΔOI/Volume 65.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10482张（+415.0% vs前日OI），连续性待观察（方向未知）
11-06 125.0P — Vol 13,600 | 最新价 $0.76 | OI 1977→11511 (ΔOI +9534张) | ΔOI/Volume 70.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9534张（+482.2% vs前日OI），连续性待观察（方向未知）
11-06 120.0P — Vol 13,222 | 最新价 $0.60 | OI 2100→9818 (ΔOI +7718张) | ΔOI/Volume 58.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7718张（+367.5% vs前日OI），连续性待观察（方向未知）
11-06 80.0P — Vol 9,476 | 最新价 $0.07 | OI 665→8280 (ΔOI +7615张) | ΔOI/Volume 80.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7615张（+1145.1% vs前日OI），连续性待观察（方向未知）
11-06 95.0P — Vol 10,000 | 最新价 $0.17 | OI 4211→11639 (ΔOI +7428张) | ΔOI/Volume 74.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7428张（+176.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 42,777 张（Put 32,295 / Call 10,482），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +50.9k / P +102.8k ｜ Activity HIGH ｜ 3D
11-13  C +4.7k / P +3.9k ｜ Activity HIGH ｜ 10D
11-20  C +5.1k / P +6.2k ｜ Activity HIGH ｜ 17D
11-27  C +1.2k / P +2.4k ｜ Activity HIGH ｜ 24D

📆 11-06 Forward Structure
存量OI: C 172.5k / P 207.5k，今日变化ΔOI: C +50.9k / P +102.8k，平值价格ATM: C $4.80 / P $5.31 ｜ ATM IV 79.7%，净 delta 敞口 -942k shares
仓位参考: Max Pain 188 ｜ Call Wall 187.5（+9.9%，弱）（OI 12.0k） ｜ Put Wall 170（-0.4%，弱）（OI 7.7k）
量化解读： 存量 Put 重｜ATM IV 79.7%｜历史 Rank 95%（近端代理）｜IV/RV 1.73×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 941,552 股

📆 11-13 Forward Structure
存量OI: C 28.8k / P 27.4k，今日变化ΔOI: C +4.7k / P +3.9k，平值价格ATM: C $6.75 / P $6.90 ｜ ATM IV 60.9%，净 delta 敞口 -7k shares
Top ΔOI: P 150 +789 ｜ C 185 +559 ｜ P 170 +552
仓位参考: Max Pain 188 ｜ Call Wall 185（+8.4%，弱）（OI 0.8k） ｜ Put Wall 155（-9.2%，弱）（OI 1.9k）
量化解读： 存量两侧均衡｜ATM IV 60.9%｜历史 Rank 95%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 6,554 股

📆 11-20 Forward Structure
存量OI: C 170.5k / P 176.3k，今日变化ΔOI: C +5.1k / P +6.2k，平值价格ATM: C $8.25 / P $8.67 ｜ ATM IV 56.9%，净 delta 敞口 -119k shares
Top ΔOI: P 160 +1,364 ｜ C 215 +1,269 ｜ C 200 +960
仓位参考: Max Pain 178 ｜ Call Wall 165（-3.3%，弱）（OI 11.7k） ｜ Put Wall 180（+5.5%，弱）（OI 11.1k）
量化解读： 存量两侧均衡｜ATM IV 56.9%｜历史 Rank 95%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 119,057 股

📆 11-27 Forward Structure
存量OI: C 11.6k / P 14.2k，今日变化ΔOI: C +1.2k / P +2.4k，平值价格ATM: C $9.52 / P $9.50 ｜ ATM IV 53.4%，净 delta 敞口 1k shares
仓位参考: Max Pain 190 ｜ Call Wall 160（-6.2%，弱）（OI 0.5k） ｜ Put Wall 180（+5.5%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜ATM IV 53.4%｜历史 Rank 95%（近端代理）｜IV/RV 1.16×（近似）｜净 delta 敞口 正 1,116 股

📅 事件差分（观察，非因果）: 11-06（3D）ATM IV 79.7% vs 11-13 60.9%（差 +18.8pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=72 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=72）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/PLTR_morning.json