# 期权晚报 2026-08-31

📊 市场环境

SPY $767.05 ｜ QQQ $716.76
VIX 14.92 ↑3.4%（5D -5.9%） ｜ Vol Regime: LOW
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
🟡 **近现价集中开仓**: 09-02 230C ΔOI +5,422（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-09 240C ΔOI +65,132 占该期限总 OI 47.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 218.86 → 收盘 220.78（+0.9%） ｜ 今日高 221.30 ｜ 低 216.21
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.73 | OI比 0.53 | ATM IV 45.1% | Skew -4.0pp | Term 0.69 | ExpMove ±1.9%（近端） | Rank 56%
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.53×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-02（2D）±1.9% ｜ 09-04（4D）±2.8% ｜ 09-09（9D）±3.7% ｜ 09-11（11D）±4.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 459,773,568 | GEX Change vs 上次快照 -27,687,758 | Flip: Primary Flip: 209.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 563 / LOW 249 / INVALID 524
结构观察区: Primary Flip 209.92（全链重定价，覆盖 94%）
Put Wall 200（弱结构｜现价高于该位 10.4%） | Call Wall 240（弱结构｜现价低于该位 8.0%）
最近结构参考: Flip 210（现价高于该位 5.2%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 240（Call Wall，弱结构）。
• Gamma 区域：切换参考 210（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-31 390.0C — Vol 28 | 最新价 $0.01 | OI 5308→89473 (ΔOI +84165张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增84165张（+1585.6% vs前日OI），连续性待观察（方向未知）
09-09 240.0C — Vol 31,526 | 最新价 $0.17 | OI 13035→78167 (ΔOI +65132张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增65132张（+499.7% vs前日OI），连续性待观察（方向未知）
10-02 200.0P — Vol 1,230 | 最新价 $1.70 | OI 1453→61970 (ΔOI +60517张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增60517张（+4165.0% vs前日OI），连续性待观察（方向未知）
08-31 220.0C — Vol 499,470 | 最新价 $0.75 | OI 7133→40957 (ΔOI +33824张) | ΔOI/Volume 6.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33824张（+474.2% vs前日OI），连续性待观察（方向未知）
08-31 135.0P — Vol 26,641（Yahoo补） | 最新价 $0.01 | OI 145→26695 (ΔOI +26550张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26550张（+18310.3% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-02  C +32.3k / P +14.2k ｜ Activity HIGH ｜ 2D
09-04  C -32.1k / P +51.9k ｜ Activity HIGH ｜ 4D
09-09  C +80.5k / P +4.1k ｜ Activity HIGH ｜ 9D
09-11  C +16.1k / P +17.0k ｜ Activity HIGH ｜ 11D

📆 09-02 Forward Structure
OI:       C 88.6k / P 57.8k
ΔOI:      C +32.3k / P +14.2k
ATM:      C 2.38 / P 1.83
ATM IV:   32.3%
ΔOI Δ Exposure*: 553k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 190 ｜ +6,215 ｜ $0.04 ｜ 名义 $24.9k* ｜ -13.9%
C 230 ｜ +5,422 ｜ $0.17 ｜ 名义 $92.2k* ｜ +4.2%
C 220 ｜ +4,153 ｜ $2.38 ｜ 名义 $988.4k* ｜ -0.4%
结构参考：230（+4.2%）上方 / 190（-13.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 545.2k / P 376.5k
ΔOI:      C -32.1k / P +51.9k
ATM:      C 3.45 / P 2.77
ATM IV:   33.8%
ΔOI Δ Exposure*: 337k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 235 ｜ -57,389 ｜ $0.20 ｜ 名义 $-1.15M* ｜ +6.4%
C 245 ｜ -53,597 ｜ $0.06 ｜ 名义 $-321.6k* ｜ +11.0%
P 190 ｜ -37,427 ｜ $0.07 ｜ 名义 $-262.0k* ｜ -13.9%
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-09 Forward Structure
OI:       C 125.3k / P 12.5k
ΔOI:      C +80.5k / P +4.1k
ATM:      C 4.65 / P 3.45
ATM IV:   28.4%
ΔOI Δ Exposure*: 548k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 240 ｜ +65,132 ｜ $0.17 ｜ 名义 $1.11M* ｜ +8.7%
C 250 ｜ +5,329 ｜ $0.05 ｜ 名义 $26.6k* ｜ +13.2%
C 235 ｜ +1,972 ｜ $0.47 ｜ 名义 $92.7k* ｜ +6.4%
结构参考：240（+8.7%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 123.2k / P 91.7k
ΔOI:      C +16.1k / P +17.0k
ATM:      C 5.10 / P 4.05
ATM IV:   30.1%
ΔOI Δ Exposure*: 217k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 230 ｜ +5,436 ｜ $1.52 ｜ 名义 $826.3k* ｜ +4.2%
P 130 ｜ +5,069 ｜ $0.03 ｜ 名义 $15.2k* ｜ -41.1%
P 200 ｜ +2,586 ｜ $0.36 ｜ 名义 $93.1k* ｜ -9.4%
结构参考：230（+4.2%）上方 / 130（-41.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/NVDA_evening.json