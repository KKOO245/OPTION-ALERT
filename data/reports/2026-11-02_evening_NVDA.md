# 期权晚报 2026-11-02（快照 16:40 ET）

📊 市场环境

SPY $752.10 ｜ QQQ $681.09
VIX 21.15 ↑8.9%（5D +15.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 22.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 11-02 10:00　【高】ISM 制造业 PMI　预测 54.6 ｜ 实际 55.5 ｜ 前值 54.5　✅ 今日已公布
- 周一 11-02 19:00　【高】Midterm Elections　实际 待公布　⏰ 今日
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.13 ｜ 实际 待公布 ｜ 前值 7.079
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48.2 ｜ 实际 待公布 ｜ 前值 48

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-04 200P ΔOI +5,798（距现价 -1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 207.59 → 收盘 202.06（-2.7%） ｜ 今日高 209.98 ｜ 低 201.66 ｜ 昨收 204.64 → 收盘 202.06（-1.3%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-11-05，窗口结束前不做对错判定）

Options: P/C成交量 0.69 | OI比 1.33 | ATM IV 33.4% | Skew 17.9pp | Term 1.45 | ExpMove ±3.4%（近端） | Rank 16%
量化视角： IV 历史低位（Rank 16%，期权偏便宜）｜期限结构正常偏陡（Term 1.45）｜保护溢价显著（Skew 17.9pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.69×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.33×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-04（2D）±3.4% ｜ 11-06（4D）±4.5% ｜ 11-09（7D）±5.1% ｜ 11-11（9D）±6.0%
   ⇒ IV–VIX Spread: +12.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 686,511 | GEX Change vs 上次快照 -119,853,975 | Flip: Primary Flip: 202.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 678 / LOW 185 / INVALID 567
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 202.02（全链重定价，覆盖 96%）
Put Wall 190（弱结构｜现价高于该位 6.3%）
最近结构参考: Flip 202（现价高于该位 0.0%）
量化视角： 正 Gamma（69万，无历史分位）｜正 Gamma 减弱（1.20亿）｜现价位于 Flip 上方 0.02%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（Put Wall，弱结构）；上方 208（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 202（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 215.0C — Vol 5,180 | 最新价 $4.65 | OI 14664→52891 (ΔOI +38227张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增38227张（+260.7% vs前日OI），连续性待观察（方向未知）
11-06 220.0C — Vol 35,142 | 最新价 $0.20 | OI 10363→46241 (ΔOI +35878张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增35878张（+346.2% vs前日OI），连续性待观察（方向未知）
11-20 237.5C — Vol 780 | 最新价 $0.75 | OI 2139→37199 (ΔOI +35060张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增35060张（+1639.1% vs前日OI），连续性待观察（方向未知）
11-06 212.5C — Vol 14,811 | 最新价 $0.94 | OI 2499→36302 (ΔOI +33803张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33803张（+1352.7% vs前日OI），连续性待观察（方向未知）
11-06 207.5C — Vol 12,063 | 最新价 $2.23 | OI 327→24072 (ΔOI +23745张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23745张（+7261.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 166,713 张（Put 0 / Call 166,713），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-04  C +24.0k / P +24.0k ｜ Activity HIGH ｜ 2D
11-06  C +146.6k / P +81.2k ｜ Activity HIGH ｜ 4D
11-09  C +3.3k / P +3.4k ｜ Activity HIGH ｜ 7D
11-11  C +2.4k / P +5.6k ｜ Activity HIGH ｜ 9D

📆 11-04 Forward Structure
存量OI: C 44.1k / P 41.6k，今日变化ΔOI: C +24.0k / P +24.0k，平值价格ATM: C $3.24 / P $3.55 ｜ ATM IV 56.5%，净 delta 敞口 -201k shares
Top ΔOI: P 200 +5,798 ｜ P 185 +4,079
仓位参考: Max Pain 208 ｜ Call Wall 220（+8.9%，弱）（OI 4.1k） ｜ Put Wall 200（-1.0%，弱）（OI 7.2k）
量化解读： 存量两侧均衡｜ATM IV 56.5%｜历史 Rank 16%（近端代理）｜IV/RV 1.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 200,703 股

📆 11-06 Forward Structure
存量OI: C 312.2k / P 246.0k，今日变化ΔOI: C +146.6k / P +81.2k，平值价格ATM: C $4.40 / P $4.65 ｜ ATM IV 53.5%，净 delta 敞口 2.0M shares
Top ΔOI: C 220 +35,878 ｜ C 212 +33,803 ｜ C 207 +23,745
仓位参考: Max Pain 210 ｜ Call Wall 220（+8.9%，弱）（OI 46.2k） ｜ Put Wall 200（-1.0%，弱）（OI 19.0k）
量化解读： 存量 Call 重｜ATM IV 53.5%｜历史 Rank 16%（近端代理）｜IV/RV 1.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,979,225 股

📆 11-09 Forward Structure
存量OI: C 6.6k / P 5.7k，今日变化ΔOI: C +3.3k / P +3.4k，平值价格ATM: C $5.00 / P $5.24 ｜ ATM IV 45.8%，净 delta 敞口 -31k shares
Top ΔOI: P 187 +835 ｜ C 210 +393
仓位参考: Max Pain 210 ｜ Call Wall 220（+8.9%，弱）（OI 0.8k） ｜ Put Wall 187.5（-7.2%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 45.8%｜历史 Rank 16%（近端代理）｜IV/RV 1.53×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 31,283 股

📆 11-11 Forward Structure
存量OI: C 4.7k / P 10.4k，今日变化ΔOI: C +2.4k / P +5.6k，平值价格ATM: C $6.05 / P $6.10 ｜ ATM IV 45.7%，净 delta 敞口 -42k shares
Top ΔOI: P 190 +2,572
仓位参考: Max Pain 210 ｜ Call Wall 220（+8.9%，弱）（OI 0.6k） ｜ Put Wall 190（-6.0%）（OI 4.8k）
量化解读： 存量 Put 重｜ATM IV 45.7%｜历史 Rank 16%（近端代理）｜IV/RV 1.52×（近似）｜净 delta 敞口 负 41,590 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/NVDA_evening.json