# 期权晨报 2026-08-31

📊 市场环境

SPY $767.29 ｜ QQQ $716.76
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
🟡 **近现价集中开仓**: 09-09 61C ΔOI +710（距现价 +2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-09 79C ΔOI +1,000 占该期限总 OI 10.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 60.02 → 今晨 60.00（-0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 60.42 ｜ 低 59.66

Options: P/C量 0.60 | OI比 0.25 | ATM IV 34.2% | Skew 0.2pp | Term 1.20 | ExpMove ±2.4%（近端） | Rank 57%
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.25×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-02（2D）±2.4% ｜ 09-04（4D）±3.7% ｜ 09-09（9D）±4.6% ｜ 09-11（11D）±5.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 112,922,693 | GEX Change N/A | Flip: Primary Flip: 54.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 1035 / LOW 271 / INVALID 540
结构观察区: Primary Flip 54.96（全链重定价，覆盖 96%）
最近结构参考: Flip 55（现价高于该位 9.2%）
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 55（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 75.0C — Vol 11 | 最新价 $0.22 | OI 2608→7811 (ΔOI +5203张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5203张（+199.5% vs前日OI），连续性待观察（方向未知）
09-25 70.0C — Vol 114 | 最新价 $0.46 | OI 46087→49082 (ΔOI +2995张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增2995张（+6.5% vs前日OI），值得跟踪（方向未知）
09-11 64.0C — Vol 157 | 最新价 $0.52 | OI 571→3245 (ΔOI +2674张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2674张（+468.3% vs前日OI），连续性待观察（方向未知）
09-18 65.0C — Vol 782 | 最新价 $0.74 | OI 43035→45419 (ΔOI +2384张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增2384张（+5.5% vs前日OI），值得跟踪（方向未知）
08-31 62.0C — Vol 105 | 最新价 $0.04 | OI 904→3196 (ΔOI +2292张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2292张（+253.5% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-02  C +3.8k / P +3.8k ｜ Activity HIGH ｜ 2D
09-04  C +9.3k / P +6.9k ｜ Activity HIGH ｜ 4D
09-09  C +4.0k / P +1.7k ｜ Activity HIGH ｜ 9D
09-11  C +3.1k / P +2.7k ｜ Activity HIGH ｜ 11D

📆 09-02 Forward Structure
OI:       C 18.6k / P 10.9k
ΔOI:      C +3.8k / P +3.8k
ATM:      C 0.69 / P 0.74
ATM IV:   39.6%
ΔOI Δ Exposure*: -254k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 64 ｜ +1,786 ｜ $4.13 ｜ 名义 $737.6k* ｜ +6.7%
C 66 ｜ +975 ｜ $0.02 ｜ 名义 $1.9k* ｜ +10.8%
C 66 ｜ +858 ｜ $0.02 ｜ 名义 $1.7k* ｜ +10.0%
结构参考：64（+6.7%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 80.0k / P 40.3k
ΔOI:      C +9.3k / P +6.9k
ATM:      C 1.10 / P 1.10
ATM IV:   43.2%
ΔOI Δ Exposure*: -289k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 64 ｜ +2,014 ｜ $0.12 ｜ 名义 $24.2k* ｜ +7.5%
C 68 ｜ +1,549 ｜ $0.05 ｜ 名义 $7.7k* ｜ +13.3%
C 65 ｜ +1,321 ｜ $0.10 ｜ 名义 $13.2k* ｜ +8.3%
结构参考：64（+7.5%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-09 Forward Structure
OI:       C 6.4k / P 2.8k
ΔOI:      C +4.0k / P +1.7k
ATM:      C 1.40 / P 1.38
ATM IV:   36.8%
ΔOI Δ Exposure*: 10k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 79 ｜ +1,000 ｜ $0.06 ｜ 名义 $6.0k* ｜ +31.7%
C 61 ｜ +710 ｜ $0.79 ｜ 名义 $56.1k* ｜ +2.5%
C 71 ｜ +500 ｜ $0.29 ｜ 名义 $14.5k* ｜ +19.2%
结构参考：79（+31.7%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 42.4k / P 14.8k
ΔOI:      C +3.1k / P +2.7k
ATM:      C 1.66 / P 1.59
ATM IV:   39.5%
ΔOI Δ Exposure*: -37k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 64 ｜ +2,674 ｜ $0.49 ｜ 名义 $131.0k* ｜ +6.7%
C 80 ｜ -1,241 ｜ $0.03 ｜ 名义 $-3.7k* ｜ +33.3%
C 63 ｜ +943 ｜ $0.70 ｜ 名义 $66.0k* ｜ +5.0%
结构参考：64（+6.7%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/SLV_morning.json