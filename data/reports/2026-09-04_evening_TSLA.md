# 期权晚报 2026-09-04（快照 16:40 ET）

📊 市场环境

SPY $770.19 ｜ QQQ $718.96
VIX 14.53 ↑1.5%（5D +0.7%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-09 360P ΔOI +12,815（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 362.18 → 收盘 354.08（-2.2%） ｜ 今日高 364.69 ｜ 低 351.32
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-09，窗口结束前不做对错判定）

Options: P/C成交量 0.78 | OI比 0.95 | ATM IV 32.4% | Skew 3.2pp | Term 1.22 | ExpMove ±3.0%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常偏陡（Term 1.22）｜保护溢价中性（Skew 3.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.95×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-09（5D）±3.0% ｜ 09-11（7D）±4.1% ｜ 09-14（10D）±4.5% ｜ 09-16（12D）±5.5%
   ⇒ IV–VIX Spread: +17.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -20,939,472 | GEX Change vs 上次快照 -24,010,811 | Flip: Primary Flip: 358.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 1031 / LOW 135 / INVALID 612
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 358.50（全链重定价，覆盖 85%）
Put Wall 360（弱结构｜现价低于该位 1.6%）
最近结构参考: Flip 358（现价低于该位 1.2%）
量化视角： 负 Gamma（2094万，无历史分位）｜由正转负（2401万）｜现价位于 Flip 下方 1.23%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 360（Put Wall，弱结构）；上方 362（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 358（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-09 360.0P — Vol 26,904 | 最新价 $8.99 | OI 348→13163 (ΔOI +12815张) | ΔOI/Volume 47.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12815张（+3682.5% vs前日OI），连续性待观察（方向未知）
09-09 400.0C — Vol 25,259 | 最新价 $0.23 | OI 7750→18850 (ΔOI +11100张) | ΔOI/Volume 43.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11100张（+143.2% vs前日OI），连续性待观察（方向未知）
09-04 400.0C — Vol 17,257 | 最新价 $0.01 | OI 18760→28420 (ΔOI +9660张) | ΔOI/Volume 56.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9660张（+51.5% vs前日OI），连续性待观察（方向未知）
09-04 365.0P — Vol 20,250 | 最新价 $11.00 | OI 2070→10903 (ΔOI +8833张) | ΔOI/Volume 43.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8833张（+426.7% vs前日OI），连续性待观察（方向未知）
09-04 370.0P — Vol 13,903 | 最新价 $16.10 | OI 2486→11235 (ΔOI +8749张) | ΔOI/Volume 62.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8749张（+351.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 51,157 张（Put 30,397 / Call 20,760），跨 2 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $35M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-09  C +25.5k / P +32.6k ｜ Activity HIGH ｜ 5D
09-11  C +20.8k / P +32.7k ｜ Activity HIGH ｜ 7D
09-14  C +2.9k / P +2.5k ｜ Activity HIGH ｜ 10D
09-16  C +1.1k / P +1.5k ｜ Activity HIGH ｜ 12D

📆 09-09 Forward Structure
存量OI:      C 84.1k / P 50.0k
今日变化ΔOI: C +25.5k / P +32.6k
平值价格ATM:  C 4.80 / P 5.80
隐含波动率 ATM IV:  32.0%
净 delta 敞口变化 ΔOI Δ Exposure*: -1.9M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 360 ｜ +12,815 ｜ $8.99 ｜ 名义 $11.52M* ｜ +1.7%
C 400 ｜ +11,100 ｜ $0.23 ｜ 名义 $255.3k* ｜ +13.0%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：360（+1.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 32.0%｜历史 Rank 3%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,853,204 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 117.6k / P 108.3k
今日变化ΔOI: C +20.8k / P +32.7k
平值价格ATM:  C 6.80 / P 7.65
隐含波动率 ATM IV:  36.4%
净 delta 敞口变化 ΔOI Δ Exposure*: -1.5M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 407 ｜ +6,284 ｜ $0.32 ｜ 名义 $201.1k* ｜ +15.1%
C 392 ｜ +5,928 ｜ $0.52 ｜ 名义 $308.3k* ｜ +10.9%
C 400 ｜ -4,636 ｜ $0.39 ｜ 名义 $-180.8k* ｜ +13.0%
结构参考：407（+15.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 36.4%｜历史 Rank 3%（近端代理）｜净 delta 敞口 负 1,507,525 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-14 Forward Structure
存量OI:      C 7.8k / P 5.4k
今日变化ΔOI: C +2.9k / P +2.5k
平值价格ATM:  C 7.75 / P 8.17
隐含波动率 ATM IV:  34.5%
净 delta 敞口变化 ΔOI Δ Exposure*: -137k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 370 ｜ +619 ｜ $18.92 ｜ 名义 $1.17M* ｜ +4.5%
C 380 ｜ +482 ｜ $1.47 ｜ 名义 $70.9k* ｜ +7.3%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：370（+4.5%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 34.5%｜历史 Rank 3%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 137,155 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-16 Forward Structure
存量OI:      C 3.7k / P 2.4k
今日变化ΔOI: C +1.1k / P +1.5k
平值价格ATM:  C 9.18 / P 10.10
隐含波动率 ATM IV:  37.2%
净 delta 敞口变化 ΔOI Δ Exposure*: -75k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 360 ｜ +522 ｜ $12.60 ｜ 名义 $657.7k* ｜ +1.7%
P 370 ｜ +170 ｜ $19.96 ｜ 名义 $339.3k* ｜ +4.5%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：360（+1.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 37.2%｜历史 Rank 3%（近端代理）｜净 delta 敞口 负 75,159 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=11 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=11）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/TSLA_evening.json