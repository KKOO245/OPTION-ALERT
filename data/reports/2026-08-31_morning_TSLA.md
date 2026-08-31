# 期权晨报 2026-08-31

📊 市场环境

SPY $765.66 ｜ QQQ $715.06
VIX 15.22 ↑5.5%（5D -4.0%） ｜ Vol Regime: NORMAL
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
🟡 **单日价格波动**: +4.6%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 360C ΔOI +5,341（距现价 -1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 348.75 → 今晨 364.80（+4.6%） | 较昨收变动（含盘初走势） ｜ 今日高 367.15 ｜ 低 347.15

Options: P/C量 0.73 | OI比 0.50 | ATM IV 56.9% | Skew 0.5pp | Term 0.73 | ExpMove ±2.9%（近端） | Rank 64%
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.50×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-02（2D）±2.9% ｜ 09-04（4D）±4.2% ｜ 09-09（9D）±5.2% ｜ 09-11（11D）±5.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 136,331,882 | GEX Change N/A | Flip: Primary Flip: 340.49（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1169 / LOW 217 / INVALID 808
结构观察区: Primary Flip 340.49（全链重定价，覆盖 97%）
Put Wall 340（弱结构｜现价高于该位 7.3%） | Call Wall 400（弱结构｜现价低于该位 8.8%）
最近结构参考: Flip 340（现价高于该位 7.1%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 340（Put Wall，弱结构）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 340（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 130.0P — Vol 1 | 最新价 $0.01 | OI 1000→22347 (ΔOI +21347张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21347张（+2134.7% vs前日OI），连续性待观察（方向未知）
09-11 220.0P — Vol 0 | 最新价 $0.08 | OI 606→14187 (ΔOI +13581张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13581张（+2241.1% vs前日OI），连续性待观察（方向未知）
09-11 180.0P — Vol 0 | 最新价 $0.05 | OI 16→12508 (ΔOI +12492张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12492张（+78075.0% vs前日OI），连续性待观察（方向未知）
09-02 165.0P — Vol 0 | 最新价 $0.01 | OI 22→7022 (ΔOI +7000张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7000张（+31818.2% vs前日OI），连续性待观察（方向未知）
08-31 347.5P — Vol 20,657 | 最新价 $0.16 | OI 1189→7145 (ΔOI +5956张) | ΔOI/Volume 28.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5956张（+500.9% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-02  C +16.6k / P +25.0k ｜ Activity HIGH ｜ 2D
09-04  C +46.3k / P +54.4k ｜ Activity HIGH ｜ 4D
09-09  C +3.1k / P +1.0k ｜ Activity HIGH ｜ 9D
09-11  C +6.9k / P +28.2k ｜ Activity HIGH ｜ 11D

📆 09-02 Forward Structure
OI:       C 36.8k / P 37.4k
ΔOI:      C +16.6k / P +25.0k
ATM:      C 5.09 / P 5.57
ATM IV:   48.1%
ΔOI Δ Exposure*: 619k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 165 ｜ +7,000 ｜ $0.01 ｜ 名义 $7.0k* ｜ -54.8%
C 400 ｜ +3,518 ｜ $0.16 ｜ 名义 $56.3k* ｜ +9.6%
P 310 ｜ +3,007 ｜ $0.04 ｜ 名义 $12.0k* ｜ -15.0%
结构参考：400（+9.6%）上方 / 165（-54.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 148.1k / P 132.1k
ΔOI:      C +46.3k / P +54.4k
ATM:      C 7.40 / P 7.80
ATM IV:   48.8%
ΔOI Δ Exposure*: 1.7M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 130 ｜ +21,347 ｜ $0.01 ｜ 名义 $21.3k* ｜ -64.4%
P 200 ｜ +5,775 ｜ $0.01 ｜ 名义 $5.8k* ｜ -45.2%
C 360 ｜ +5,341 ｜ $10.17 ｜ 名义 $5.43M* ｜ -1.3%
结构参考：130（-64.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-09 Forward Structure
OI:       C 8.3k / P 2.9k
ΔOI:      C +3.1k / P +1.0k
ATM:      C 9.30 / P 9.50
ATM IV:   40.2%
ΔOI Δ Exposure*: 112k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 400 ｜ +680 ｜ $1.25 ｜ 名义 $85.0k* ｜ +9.6%
C 380 ｜ +527 ｜ $4.00 ｜ 名义 $210.8k* ｜ +4.2%
C 355 ｜ +334 ｜ $14.05 ｜ 名义 $469.3k* ｜ -2.7%
结构参考：400（+9.6%）上方 / 355（-2.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 60.3k / P 52.8k
ΔOI:      C +6.9k / P +28.2k
ATM:      C 10.70 / P 10.60
ATM IV:   41.6%
ΔOI Δ Exposure*: 158k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 220 ｜ +13,581 ｜ $0.05 ｜ 名义 $67.9k* ｜ -39.7%
P 180 ｜ +12,492 ｜ $0.03 ｜ 名义 $37.5k* ｜ -50.7%
C 510 ｜ +1,971 ｜ $0.09 ｜ 名义 $17.7k* ｜ +39.8%
结构参考：510（+39.8%）上方 / 220（-39.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/TSLA_morning.json