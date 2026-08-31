# 期权晨报 2026-08-31

📊 市场环境

SPY $765.90 ｜ QQQ $714.54
VIX 15.33 ↑6.2%（5D -3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 50.4（neutral）
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
🟡 **近现价集中开仓**: 09-02 220C ΔOI +4,153（距现价 +0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-09 240C ΔOI +65,132 占该期限总 OI 47.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 217.55 → 今晨 218.81（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 220.26 ｜ 低 216.21

Options: P/C量 0.97 | OI比 0.53 | ATM IV 48.2% | Skew 1.9pp | Term 0.67 | ExpMove ±1.1%（近端） | Rank 65%
   ⇒ Put/Call Volume: 0.97×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.53×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-02（2D）±2.3% ｜ 09-04（4D）±3.1% ｜ 09-09（9D）±4.0% ｜ 09-11（11D）±4.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 210.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 657 / LOW 219 / INVALID 460
结构观察区: Primary Flip 210.41（全链重定价，覆盖 98%）
Put Wall 200（弱结构｜现价高于该位 9.4%） | Call Wall 240（弱结构｜现价低于该位 8.8%）
最近结构参考: Flip 210（现价高于该位 4.0%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 240（Call Wall，弱结构）。
• Gamma 区域：切换参考 210（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-31 390.0C — Vol 26 | 最新价 $0.01 | OI 5308→89473 (ΔOI +84165张) | ΔOI/Volume 323711.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增84165张（+1585.6% vs前日OI），连续性待观察（方向未知）
09-09 240.0C — Vol 568 | 最新价 $0.28 | OI 13035→78167 (ΔOI +65132张) | ΔOI/Volume 11466.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增65132张（+499.7% vs前日OI），连续性待观察（方向未知）
10-02 200.0P — Vol 220 | 最新价 $2.06 | OI 1453→61970 (ΔOI +60517张) | ΔOI/Volume 27507.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增60517张（+4165.0% vs前日OI），连续性待观察（方向未知）
08-31 220.0C — Vol 73,189 | 最新价 $0.71 | OI 7133→40957 (ΔOI +33824张) | ΔOI/Volume 46.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33824张（+474.2% vs前日OI），连续性待观察（方向未知）
08-31 135.0P — Vol 0 | 最新价 $0.01 | OI 145→26695 (ΔOI +26550张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26550张（+18310.3% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-02  C +32.3k / P +14.2k ｜ Activity HIGH ｜ 2D
09-04  C -32.1k / P +51.9k ｜ Activity HIGH ｜ 4D
09-09  C +80.5k / P +4.1k ｜ Activity HIGH ｜ 9D
09-11  C +16.1k / P +17.0k ｜ Activity HIGH ｜ 11D

📆 09-02 Forward Structure
OI:       C 88.6k / P 57.8k
ΔOI:      C +32.3k / P +14.2k
ATM:      C 2.07 / P 2.97
ATM IV:   36.3%
ΔOI Δ Exposure*: 348k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 190 ｜ +6,215 ｜ $0.05 ｜ 名义 $31.1k* ｜ -13.2%
C 230 ｜ +5,422 ｜ $0.18 ｜ 名义 $97.6k* ｜ +5.1%
C 220 ｜ +4,153 ｜ $2.07 ｜ 名义 $859.7k* ｜ +0.5%
结构参考：230（+5.1%）上方 / 190（-13.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 545.2k / P 376.5k
ΔOI:      C -32.1k / P +51.9k
ATM:      C 3.10 / P 3.80
ATM IV:   36.4%
ΔOI Δ Exposure*: -95k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 235 ｜ -57,389 ｜ $0.24 ｜ 名义 $-1.38M* ｜ +7.4%
C 245 ｜ -53,597 ｜ $0.07 ｜ 名义 $-375.2k* ｜ +12.0%
P 190 ｜ -37,427 ｜ $0.08 ｜ 名义 $-299.4k* ｜ -13.2%
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-09 Forward Structure
OI:       C 125.3k / P 12.5k
ΔOI:      C +80.5k / P +4.1k
ATM:      C 3.93 / P 4.75
ATM IV:   30.6%
ΔOI Δ Exposure*: 591k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 240 ｜ +65,132 ｜ $0.28 ｜ 名义 $1.82M* ｜ +9.7%
C 250 ｜ +5,329 ｜ $0.10 ｜ 名义 $53.3k* ｜ +14.3%
C 235 ｜ +1,972 ｜ $0.53 ｜ 名义 $104.5k* ｜ +7.4%
结构参考：240（+9.7%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 123.2k / P 91.7k
ΔOI:      C +16.1k / P +17.0k
ATM:      C 4.50 / P 5.42
ATM IV:   31.9%
ΔOI Δ Exposure*: 133k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 230 ｜ +5,436 ｜ $1.44 ｜ 名义 $782.8k* ｜ +5.1%
P 130 ｜ +5,069 ｜ $0.02 ｜ 名义 $10.1k* ｜ -40.6%
P 200 ｜ +2,586 ｜ $0.48 ｜ 名义 $124.1k* ｜ -8.6%
结构参考：230（+5.1%）上方 / 130（-40.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/NVDA_morning.json