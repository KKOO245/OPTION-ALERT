# 期权晨报 2026-09-01（快照 10:20 ET）

📊 市场环境

SPY $763.56 ｜ QQQ $709.16
VIX 15.71 ↑5.3%（5D +1.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 46.4（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-01 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.3 ｜ 实际 7.271 ｜ 前值 7.182　✅ 今日已公布
- 周二 09-01 10:00　【高】ISM 制造业 PMI　预测 55.2 ｜ 实际 54.6 ｜ 前值 55.6　✅ 今日已公布
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 09-02 725C ΔOI +4,579（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 716.76 → 今开 707.43（-1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 708.80 ｜ 低 705.62

Options: P/C成交量 1.06 | OI比 2.08 | ATM IV 20.0% | Skew 1.8pp | Term 0.88 | ExpMove ±0.8%（近端） | Rank 59%
量化视角： IV 中性（Rank 59%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价薄（Skew 1.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.06×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.08×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 16% ｜ P/C OI(近端) 81%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 16%）｜近端持仓结构中性（P/C OI 分位 81%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-02（1D）±0.8% ｜ 09-03（2D）±1.1% ｜ 09-04（3D）±1.4% ｜ 09-08（7D）±1.7%
   ⇒ IV–VIX Spread: +4.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -602,529,314 | GEX Change vs 上次快照 -548,309,238 | Flip: Primary Flip: 716.04（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 2767 / LOW 517 / INVALID 2042
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 716.04（全链重定价，覆盖 97%）
Put Wall 700（弱结构｜现价高于该位 1.0%） | Call Wall 730（弱结构｜现价低于该位 3.2%）
最近结构参考: Put Wall 700（现价高于该位 1.0%）
量化视角： 负 Gamma（6.03亿，历史分位 16%，偏负区）｜负 Gamma 加深（5.48亿）｜现价位于 Flip 下方 1.27%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 730（Call Wall，弱结构）。
• Gamma 区域：切换参考 716（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 625.0P — Vol 1 | 最新价 $0.06 | OI 988→21404 (ΔOI +20416张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20416张（+2066.4% vs前日OI），连续性待观察（方向未知）
09-01 708.0P — Vol 34,126 | 最新价 $1.81 | OI 505→11060 (ΔOI +10555张) | ΔOI/Volume 30.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10555张（+2090.1% vs前日OI），连续性待观察（方向未知）
09-18 730.0C — Vol 379 | 最新价 $2.48 | OI 34671→44975 (ΔOI +10304张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10304张（+29.7% vs前日OI），连续性待观察（方向未知）
09-30 705.0P — Vol 153 | 最新价 $12.57 | OI 5711→11317 (ΔOI +5606张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5606张（+98.2% vs前日OI），连续性待观察（方向未知）
09-01 710.0P — Vol 6,391 | 最新价 $3.10 | OI 2498→7813 (ΔOI +5315张) | ΔOI/Volume 83.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5315张（+212.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 52,196 张（Put 41,892 / Call 10,304），跨 4 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $11M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-02  C +17.5k / P +26.1k ｜ Activity HIGH ｜ 1D
09-03  C +3.1k / P +3.4k ｜ Activity HIGH ｜ 2D
09-04  C +15.4k / P +55.0k ｜ Activity HIGH ｜ 3D
09-08  C +5.0k / P +23.8k ｜ Activity HIGH ｜ 7D

📆 09-02 Forward Structure
存量OI:      C 40.1k / P 89.1k
今日变化ΔOI: C +17.5k / P +26.1k
平值价格ATM:  C 3.19 / P 2.69
隐含波动率 ATM IV:  17.6%
净 delta 敞口变化 ΔOI Δ Exposure*: -803k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 725 ｜ +4,579 ｜ $0.04 ｜ 名义 $18.3k* ｜ +2.6%
P 698 ｜ +2,803 ｜ $0.58 ｜ 名义 $162.6k* ｜ -1.3%
C 726 ｜ +2,683 ｜ $0.04 ｜ 名义 $10.7k* ｜ +2.7%
结构参考：725（+2.6%） / 698（-1.3%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 17.6%｜历史 Rank 59%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 803,108 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-03 Forward Structure
存量OI:      C 23.7k / P 44.1k
今日变化ΔOI: C +3.1k / P +3.4k
平值价格ATM:  C 4.22 / P 3.64
隐含波动率 ATM IV:  17.8%
净 delta 敞口变化 ΔOI Δ Exposure*: -256k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 660 ｜ -3,703 ｜ $0.08 ｜ 名义 $-29.6k* ｜ -6.6%
P 710 ｜ +1,985 ｜ $5.47 ｜ 名义 $1.09M* ｜ +0.4%
P 678 ｜ +901 ｜ $0.10 ｜ 名义 $9.0k* ｜ -4.1%
结构参考：710（+0.4%） / 678（-4.1%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 17.8%｜历史 Rank 59%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 255,686 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-04 Forward Structure
存量OI:      C 181.7k / P 244.2k
今日变化ΔOI: C +15.4k / P +55.0k
平值价格ATM:  C 5.29 / P 4.52
隐含波动率 ATM IV:  18.3%
净 delta 敞口变化 ΔOI Δ Exposure*: -194k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 625 ｜ +20,416 ｜ $0.06 ｜ 名义 $122.5k* ｜ -11.6%
P 675 ｜ +5,315 ｜ $0.27 ｜ 名义 $143.5k* ｜ -4.5%
P 658 ｜ +3,411 ｜ $0.11 ｜ 名义 $37.5k* ｜ -6.9%
结构参考：625（-11.6%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 18.3%｜历史 Rank 59%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 194,287 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-08 Forward Structure
存量OI:      C 22.6k / P 41.2k
今日变化ΔOI: C +5.0k / P +23.8k
平值价格ATM:  C 6.33 / P 5.49
隐含波动率 ATM IV:  14.9%
净 delta 敞口变化 ΔOI Δ Exposure*: -57k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 14.9%｜历史 Rank 59%（近端代理）｜净 delta 敞口 负 56,601 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=4 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=4）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-01/QQQ_morning.json