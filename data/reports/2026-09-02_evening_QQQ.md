# 期权晚报 2026-09-02（快照 17:13 ET）

📊 市场环境

SPY $765.16 ｜ QQQ $709.24
VIX 15.20 ↓7.0%（5D -1.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-03 695P ΔOI +4,012（距现价 -2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-03 535P ΔOI +36,292 占该期限总 OI 23.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 707.11 → 收盘 709.24（+0.3%） ｜ 今日高 709.80 ｜ 低 705.11
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-09，窗口结束前不做对错判定）

Options: P/C成交量 0.99 | OI比 1.80 | ATM IV 48.0% | Skew 1.4pp | Term 0.39 | ExpMove ±0.7%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.39，近月 IV 高于远月）｜保护溢价薄（Skew 1.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.99×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.80×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 27% ｜ P/C OI(近端) 63%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 27%）｜近端持仓结构中性（P/C OI 分位 63%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-03（1D）±0.7% ｜ 09-04（2D）±1.0% ｜ 09-08（6D）±1.4% ｜ 09-09（7D）±1.6%
   ⇒ IV–VIX Spread: +32.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -362,811,509 | GEX Change vs 上次快照 157,127,647 | Flip: Primary Flip: 714.65（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 2332 / LOW 810 / INVALID 1894
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 714.65（全链重定价，覆盖 93%）
Put Wall 700（弱结构｜现价高于该位 1.3%） | Call Wall 750（弱结构｜现价低于该位 5.4%）
最近结构参考: Flip 715（现价低于该位 0.8%）
量化视角： 负 Gamma（3.63亿，历史分位 27%，中性区）｜负 Gamma 缓解（+1.57亿）｜现价位于 Flip 下方 0.76%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 708（MaxPain，仅结算参考） / 750（Call Wall，弱结构）。
• Gamma 区域：切换参考 715（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 690.0P — Vol 1,678 | 最新价 $6.21 | OI 14955→70427 (ΔOI +55472张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增55472张（+370.9% vs前日OI），连续性待观察（方向未知）
09-25 665.0P — Vol 588 | 最新价 $2.80 | OI 1357→56422 (ΔOI +55065张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增55065张（+4057.8% vs前日OI），连续性待观察（方向未知）
09-03 535.0P — Vol 36,293（Yahoo补） | 最新价 $0.01 | OI 60→36352 (ΔOI +36292张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增36292张（+60486.7% vs前日OI），连续性待观察（方向未知）
09-11 750.0C — Vol 12,337 | 最新价 $0.04 | OI 9060→29739 (ΔOI +20679张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20679张（+228.2% vs前日OI），连续性待观察（方向未知）
09-30 695.0P — Vol 1,026 | 最新价 $8.40 | OI 1275→21853 (ΔOI +20578张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20578张（+1614.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 188,086 张（Put 167,407 / Call 20,679），跨 4 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $67M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-03  C +23.0k / P +66.8k ｜ Activity HIGH ｜ 1D
09-04  C +22.8k / P +27.6k ｜ Activity HIGH ｜ 2D
09-08  C +6.1k / P +12.0k ｜ Activity HIGH ｜ 6D
09-09  C +5.0k / P +6.0k ｜ Activity HIGH ｜ 7D

📆 09-03 Forward Structure
存量OI:      C 46.7k / P 110.9k
今日变化ΔOI: C +23.0k / P +66.8k
平值价格ATM:  C 2.76 / P 2.41
隐含波动率 ATM IV:  17.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 332k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 695 ｜ +4,012 ｜ $0.08 ｜ 名义 $32.1k* ｜ -2.0%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：695（-2.0%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 17.6%｜历史 Rank 99%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 332,495 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-04 Forward Structure
存量OI:      C 204.5k / P 271.8k
今日变化ΔOI: C +22.8k / P +27.6k
平值价格ATM:  C 4.07 / P 3.32
隐含波动率 ATM IV:  17.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 1.1M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 705 ｜ +5,139 ｜ $1.99 ｜ 名义 $1.02M* ｜ -0.6%
C 715 ｜ +4,792 ｜ $1.44 ｜ 名义 $690.0k* ｜ +0.8%
P 700 ｜ +4,681 ｜ $0.96 ｜ 名义 $449.4k* ｜ -1.3%
结构参考：715（+0.8%） / 705（-0.6%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 17.6%｜历史 Rank 99%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,141,187 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-08 Forward Structure
存量OI:      C 28.7k / P 53.2k
今日变化ΔOI: C +6.1k / P +12.0k
平值价格ATM:  C 5.30 / P 4.53
隐含波动率 ATM IV:  13.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 106k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 680 ｜ +5,081 ｜ $0.27 ｜ 名义 $137.2k* ｜ -4.1%
C 707 ｜ +1,964 ｜ $6.85 ｜ 名义 $1.35M* ｜ -0.3%
P 700 ｜ +1,713 ｜ $1.91 ｜ 名义 $327.2k* ｜ -1.3%
结构参考：680（-4.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 13.8%｜历史 Rank 99%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 105,793 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-09 Forward Structure
存量OI:      C 21.9k / P 18.4k
今日变化ΔOI: C +5.0k / P +6.0k
平值价格ATM:  C 6.10 / P 5.19
隐含波动率 ATM IV:  15.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 62k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 716 ｜ +1,108 ｜ $2.90 ｜ 名义 $321.3k* ｜ +1.0%
P 696 ｜ +1,073 ｜ $1.78 ｜ 名义 $191.0k* ｜ -1.9%
P 679 ｜ +559 ｜ $0.47 ｜ 名义 $26.3k* ｜ -4.3%
结构参考：716（+1.0%） / 696（-1.9%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 15.8%｜历史 Rank 99%（近端代理）｜净 delta 敞口 正 62,337 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-02/QQQ_evening.json