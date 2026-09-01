# 期权晨报 2026-09-01（快照 10:20 ET）

📊 市场环境

SPY $762.30 ｜ QQQ $708.35
VIX 15.71 ↑5.3%（5D +1.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.2（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-01 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.3 ｜ 实际 7.271 ｜ 前值 7.182　✅ 今日已公布
- 周二 09-01 10:00　【高】ISM 制造业 PMI　预测 55.2 ｜ 实际 54.6 ｜ 前值 55.6　✅ 今日已公布
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 09-04（3D）ATM IV 100.4% vs 09-11 85.1%（差 +15.3pp），覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 206.30 → 今开 203.50（-1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 207.23 ｜ 低 197.50

Options: P/C成交量 0.72 | OI比 1.17 | ATM IV 100.4% | Skew -11.1pp | Term 0.79 | ExpMove ±7.6%（近端） | Rank 61%
量化视角： IV 中性（Rank 61%）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜Put 保护异常便宜（Skew -11.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.72×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.17×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（3D）±7.6% ｜ 09-11（10D）±11.2% ｜ 09-18（17D）±14.1% ｜ 09-25（24D）±16.3%
   ⇒ IV–VIX Spread: +84.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,048,295 | GEX Change vs 上次快照 -3,620,237 | Flip: Primary Flip: 204.48（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 568 / LOW 77 / INVALID 153
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 204.48（全链重定价，覆盖 100%）
最近结构参考: Flip 204（现价低于该位 1.8%）
量化视角： 负 Gamma（305万，无历史分位）｜由正转负（362万）｜现价位于 Flip 下方 1.82%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 204（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 182.5P — Vol 23 | 最新价 $3.12 | OI 32→1175 (ΔOI +1143张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1143张（+3571.9% vs前日OI），连续性待观察（方向未知）
09-04 185.0P — Vol 295 | 最新价 $1.75 | OI 3325→4340 (ΔOI +1015张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1015张（+30.5% vs前日OI），连续性待观察（方向未知）
09-04 250.0C — Vol 464 | 最新价 $0.25 | OI 3440→4414 (ΔOI +974张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增974张（+28.3% vs前日OI），连续性待观察（方向未知）
09-04 245.0C — Vol 36 | 最新价 $0.35 | OI 627→1588 (ΔOI +961张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增961张（+153.3% vs前日OI），连续性待观察（方向未知）
09-04 190.0P — Vol 162 | 最新价 $3.00 | OI 2206→3105 (ΔOI +899张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增899张（+40.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,992 张（Put 3,057 / Call 1,935），跨 2 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +8.3k / P +6.5k ｜ Activity HIGH ｜ 3D
09-11  C +1.9k / P +3.4k ｜ Activity HIGH ｜ 10D
09-18  C +0.3k / P +0.4k ｜ Activity MEDIUM △ ｜ 17D
09-25  C +0.4k / P +0.5k ｜ Activity MEDIUM △ ｜ 24D

📆 09-04 Forward Structure
存量OI:      C 37.6k / P 43.9k
今日变化ΔOI: C +8.3k / P +6.5k
平值价格ATM:  C 7.98 / P 7.26
隐含波动率 ATM IV:  100.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 68k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 185 ｜ +1,015 ｜ $1.75 ｜ 名义 $177.6k* ｜ -7.9%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：185（-7.9%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 100.4%｜历史 Rank 61%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 68,273 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 14.5k / P 14.7k
今日变化ΔOI: C +1.9k / P +3.4k
平值价格ATM:  C 11.70 / P 10.73
隐含波动率 ATM IV:  85.1%
净 delta 敞口变化 ΔOI Δ Exposure*: -27k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 182 ｜ +1,143 ｜ $3.12 ｜ 名义 $356.6k* ｜ -9.1%
C 215 ｜ +428 ｜ $6.45 ｜ 名义 $276.1k* ｜ +7.1%
C 220 ｜ +296 ｜ $5.16 ｜ 名义 $152.7k* ｜ +9.6%
结构参考：215（+7.1%） / 182（-9.1%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜ATM IV 85.1%｜历史 Rank 61%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 26,555 股（方向不可观测）——方向不可观测，观察点，非方向信号

   Top ΔOI: 210C -1,398 ｜ 280C +850

   Top ΔOI: 180P +92

📅 事件差分（观察，非因果）: 09-04（3D）ATM IV 100.4% vs 09-11 85.1%（差 +15.3pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=4 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=4）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-01/BE_morning.json