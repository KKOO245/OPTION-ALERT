# 期权晨报 2026-08-31

📊 市场环境

SPY $765.41 ｜ QQQ $714.99
VIX 15.19 ↑5.3%（5D -4.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 49.9（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-01 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.3 ｜ 实际 待公布 ｜ 前值 7.359
- 周二 09-01 10:00　【高】ISM 制造业 PMI　预测 55.2 ｜ 实际 待公布 ｜ 前值 55.6
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 09-04 161P ΔOI +1,735（距现价 -0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-04 161P ΔOI +1,735 占该期限总 OI 12.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 162.38 → 今晨 161.19（-0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 161.69 ｜ 低 159.62

Options: P/C量 2.32 | OI比 2.10 | ATM IV 32.6% | Skew 5.0pp | Term 0.94 | ExpMove ±2.7%（近端） | Rank 48%
   ⇒ Put/Call Volume: 2.32×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.10×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-04（4D）±2.7% ｜ 09-11（11D）±4.0% ｜ 09-18（18D）±5.6% ｜ 09-25（25D）±10.9%
   ⇒ IV–VIX Spread: +17.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -12,927,727 | GEX Change vs 上次快照 -7,938,106 | Flip: Primary Flip: 166.01（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 350 / LOW 95 / INVALID 427
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 166.01（全链重定价，覆盖 99%）
Put Wall 155（弱结构｜现价高于该位 4.0%） | Call Wall 155（弱结构｜现价高于该位 4.0%）
最近结构参考: Flip 166（现价低于该位 2.9%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 155（Put Wall，弱结构）；上方 155（Call Wall，弱结构）。
• Gamma 区域：切换参考 166（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 159.0P — Vol 2,500 | 最新价 $1.86 | OI 10→2504 (ΔOI +2494张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2494张（+24940.0% vs前日OI），连续性待观察（方向未知）
09-04 161.0P — Vol 1,862 | 最新价 $1.82 | OI 92→1827 (ΔOI +1735张) | ΔOI/Volume 93.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1735张（+1885.9% vs前日OI），连续性待观察（方向未知）
09-11 152.0P — Vol 1,500 | 最新价 $0.42 | OI 20→1514 (ΔOI +1494张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1494张（+7470.0% vs前日OI），连续性待观察（方向未知）
09-04 163.0P — Vol 1,531 | 最新价 $2.84 | OI 31→1513 (ΔOI +1482张) | ΔOI/Volume 96.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1482张（+4780.6% vs前日OI），连续性待观察（方向未知）
09-04 158.0P — Vol 1,103 | 最新价 $0.92 | OI 198→1292 (ΔOI +1094张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1094张（+552.5% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +2.0k / P +5.2k ｜ Activity HIGH ｜ 4D
09-11  C +66 / P +5.1k ｜ Activity HIGH ｜ 11D
09-18  C +74 / P -1.9k ｜ Activity HIGH ｜ 18D
09-25  C +34 / P +0.1k ｜ Activity MEDIUM △ ｜ 25D

📆 09-04 Forward Structure
OI:       C 4.6k / P 9.6k
ΔOI:      C +2.0k / P +5.2k
ATM:      C 2.25 / P 2.15
ATM IV:   32.6%
ΔOI Δ Exposure*: -194k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 161 ｜ +1,735 ｜ $2.15 ｜ 名义 $373.0k* ｜ -0.1%
P 163 ｜ +1,482 ｜ $3.70 ｜ 名义 $548.3k* ｜ +1.1%
P 158 ｜ +1,094 ｜ $1.20 ｜ 名义 $131.3k* ｜ -2.0%
结构参考：163（+1.1%）上方 / 161（-0.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 1.2k / P 6.6k
ΔOI:      C +66 / P +5.1k
ATM:      C 3.18 / P 3.32
ATM IV:   29.4%
ΔOI Δ Exposure*: -137k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 159 ｜ +2,494 ｜ $2.57 ｜ 名义 $641.0k* ｜ -1.4%
P 152 ｜ +1,494 ｜ $0.42 ｜ 名义 $62.7k* ｜ -5.7%
P 153 ｜ +997 ｜ $0.64 ｜ 名义 $63.8k* ｜ -5.1%
结构参考：159（-1.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 71.5k / P 99.1k
ΔOI:      C +74 / P -1.9k
ATM:      C 4.70 / P 4.35
ATM IV:   30.3%
ΔOI Δ Exposure*: 107k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 163 ｜ -1,526 ｜ $5.52 ｜ 名义 $-842.4k* ｜ +1.1%
P 155 ｜ +1,072 ｜ $2.03 ｜ 名义 $217.6k* ｜ -3.8%
P 153 ｜ -899 ｜ $1.56 ｜ 名义 $-140.2k* ｜ -5.1%
结构参考：155（-3.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 185C +27 ｜ 145P +26

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=3 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=3）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/XBI_morning.json