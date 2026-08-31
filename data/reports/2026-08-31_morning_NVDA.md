# 期权晨报 2026-08-31

📊 市场环境

SPY $767.25 ｜ QQQ $716.76
VIX 15.16 ↑5.1%（5D -4.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 49.7（neutral）
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
🟡 **近现价集中开仓**: 09-02 230C ΔOI +5,422（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-09 240C ΔOI +65,132 占该期限总 OI 47.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 217.55 → 今晨 220.03（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 220.60 ｜ 低 216.21

Options: P/C量 0.74 | OI比 0.53 | ATM IV 35.1% | Skew -1.3pp | Term 0.89 | ExpMove ±2.0%（近端） | Rank 18%
   ⇒ Put/Call Volume: 0.74×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.53×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-02（2D）±2.0% ｜ 09-04（4D）±2.9% ｜ 09-09（9D）±3.7% ｜ 09-11（11D）±4.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 487,461,326 | GEX Change N/A | Flip: Primary Flip: 210.71（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 618 / LOW 217 / INVALID 501
结构观察区: Primary Flip 210.71（全链重定价，覆盖 96%）
Put Wall 200（弱结构｜现价高于该位 10.0%） | Call Wall 240（弱结构｜现价低于该位 8.3%）
最近结构参考: Flip 211（现价高于该位 4.4%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 240（Call Wall，弱结构）。
• Gamma 区域：切换参考 211（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-31 390.0C — Vol 26 | 最新价 $0.01 | OI 5308→89473 (ΔOI +84165张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增84165张（+1585.6% vs前日OI），连续性待观察（方向未知）
09-09 240.0C — Vol 568 | 最新价 $0.28 | OI 13035→78167 (ΔOI +65132张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增65132张（+499.7% vs前日OI），连续性待观察（方向未知）
10-02 200.0P — Vol 220 | 最新价 $2.06 | OI 1453→61970 (ΔOI +60517张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增60517张（+4165.0% vs前日OI），连续性待观察（方向未知）
08-31 220.0C — Vol 73,189 | 最新价 $0.71 | OI 7133→40957 (ΔOI +33824张) | ΔOI/Volume 46.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33824张（+474.2% vs前日OI），连续性待观察（方向未知）
08-31 135.0P — Vol 0 | 最新价 $0.01 | OI 145→26695 (ΔOI +26550张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26550张（+18310.3% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-02  C +32.3k / P +14.2k ｜ Activity HIGH ｜ 2D
09-04  C -32.1k / P +51.9k ｜ Activity HIGH ｜ 4D
09-09  C +80.5k / P +4.1k ｜ Activity HIGH ｜ 9D
09-11  C +16.1k / P +17.0k ｜ Activity HIGH ｜ 11D

📆 09-02 Forward Structure
OI:       C 88.6k / P 57.8k
ΔOI:      C +32.3k / P +14.2k
ATM:      C 2.18 / P 2.22
ATM IV:   32.4%
ΔOI Δ Exposure*: 434k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 190 ｜ +6,215 ｜ $0.03 ｜ 名义 $18.6k* ｜ -13.6%
C 230 ｜ +5,422 ｜ $0.16 ｜ 名义 $86.8k* ｜ +4.5%
C 220 ｜ +4,153 ｜ $2.18 ｜ 名义 $905.4k* ｜ -0.0%
结构参考：230（+4.5%）上方 / 190（-13.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 545.2k / P 376.5k
ΔOI:      C -32.1k / P +51.9k
ATM:      C 3.25 / P 3.07
ATM IV:   33.8%
ΔOI Δ Exposure*: 113k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 235 ｜ -57,389 ｜ $0.20 ｜ 名义 $-1.15M* ｜ +6.8%
C 245 ｜ -53,597 ｜ $0.06 ｜ 名义 $-321.6k* ｜ +11.3%
P 190 ｜ -37,427 ｜ $0.07 ｜ 名义 $-262.0k* ｜ -13.6%
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-09 Forward Structure
OI:       C 125.3k / P 12.5k
ΔOI:      C +80.5k / P +4.1k
ATM:      C 4.10 / P 3.95
ATM IV:   28.9%
ΔOI Δ Exposure*: 572k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 240 ｜ +65,132 ｜ $0.24 ｜ 名义 $1.56M* ｜ +9.1%
C 250 ｜ +5,329 ｜ $0.09 ｜ 名义 $48.0k* ｜ +13.6%
C 235 ｜ +1,972 ｜ $0.46 ｜ 名义 $90.7k* ｜ +6.8%
结构参考：240（+9.1%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 123.2k / P 91.7k
ΔOI:      C +16.1k / P +17.0k
ATM:      C 4.69 / P 4.65
ATM IV:   30.2%
ΔOI Δ Exposure*: 162k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 230 ｜ +5,436 ｜ $1.35 ｜ 名义 $733.9k* ｜ +4.5%
P 130 ｜ +5,069 ｜ $0.02 ｜ 名义 $10.1k* ｜ -40.9%
P 200 ｜ +2,586 ｜ $0.39 ｜ 名义 $100.9k* ｜ -9.1%
结构参考：230（+4.5%）上方 / 130（-40.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/NVDA_morning.json