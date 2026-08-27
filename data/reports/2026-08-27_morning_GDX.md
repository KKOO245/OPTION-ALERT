# 期权晨报 2026-08-27

📊 市场环境

SPY $770.63 ｜ QQQ $719.27
VIX 14.49 ↓4.7%（5D -9.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 58.3（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911


## GDX

🔍 重点速览
🟡 **近现价集中开仓**: 08-28 108C ΔOI +5,287（距现价 +4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 102.76 → 今晨 103.42（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 104.11 ｜ 低 101.69

Options: P/C量 1.34 | OI比 0.66 | ATM IV 54.8% | Skew -3.0pp | Term 0.84 | ExpMove ±2.6%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 1.34×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.66×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-28（1D）±2.6% ｜ 09-04（8D）±5.4% ｜ 09-11（15D）±7.5% ｜ 09-18（22D）±8.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 99.74（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 548 / LOW 203 / INVALID 291
结构观察区: ≈100（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 80: +29.3% | 距 Call Wall 104: -0.6%
最近结构参考: Call Wall 104（距现价 -0.6%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（Put Wall）；上方 104（Call Wall）。
• Gamma 区域：切换参考 100（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 108.0C — Vol 15 | 最新价 $0.23 | OI 12904→18191 (ΔOI +5287张) | ΔOI/Volume 35246.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5287张（+41.0% vs前日OI），连续性待观察（方向未知）
09-18 99.0P — Vol 7 | 最新价 $2.36 | OI 1682→6051 (ΔOI +4369张) | ΔOI/Volume 62414.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4369张（+259.8% vs前日OI），连续性待观察（方向未知）
09-04 100.0P — Vol 401 | 最新价 $1.37 | OI 2879→6745 (ΔOI +3866张) | ΔOI/Volume 964.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3866张（+134.3% vs前日OI），连续性待观察（方向未知）
09-18 85.0P — Vol 11 | 最新价 $0.22 | OI 29096→31509 (ΔOI +2413张) | ΔOI/Volume 21936.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2413张（+8.3% vs前日OI），连续性待观察（方向未知）
09-18 89.0P — Vol 7 | 最新价 $0.47 | OI 3304→5635 (ΔOI +2331张) | ΔOI/Volume 33300.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2331张（+70.5% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +5.5k / P +3.1k ｜ Activity HIGH ｜ 1D
09-04  C +1.8k / P +6.5k ｜ Activity HIGH ｜ 8D
09-11  C +73 / P -9 ｜ Activity MEDIUM △ ｜ 15D
09-18  C -6.8k / P +5.4k ｜ Activity HIGH ｜ 22D

📆 08-28 Forward Structure
OI:       C 133.7k / P 88.4k
ΔOI:      C +5.5k / P +3.1k
ATM:      C 1.60 / P 1.10
ATM IV:   54.8%
ΔOI Δ Exposure*: -130k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 108 ｜ +5,287 ｜ $0.23 ｜ 名义 $121.6k* ｜ +4.4%
C 104 ｜ -3,393 ｜ $1.14 ｜ 名义 $-386.8k* ｜ +0.6%
C 110 ｜ +1,927 ｜ $0.08 ｜ 名义 $15.4k* ｜ +6.4%
结构参考：108（+4.4%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 14.6k / P 58.2k
ΔOI:      C +1.8k / P +6.5k
ATM:      C 3.09 / P 2.54
ATM IV:   45.5%
ΔOI Δ Exposure*: -170k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 100 ｜ +3,866 ｜ $1.37 ｜ 名义 $529.6k* ｜ -3.3%
P 95 ｜ +1,356 ｜ $0.39 ｜ 名义 $52.9k* ｜ -8.1%
C 116 ｜ +1,013 ｜ $0.31 ｜ 名义 $31.4k* ｜ +12.2%
结构参考：116（+12.2%）上方 / 100（-3.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 97P +162 ｜ 90P -145

📆 09-18 Forward Structure
OI:       C 248.0k / P 376.1k
ΔOI:      C -6.8k / P +5.4k
ATM:      C 4.95 / P 4.20
ATM IV:   45.8%
ΔOI Δ Exposure*: -709k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 95 ｜ -4,385 ｜ $10.55 ｜ 名义 $-4.63M* ｜ -8.1%
P 99 ｜ +4,369 ｜ $2.36 ｜ 名义 $1.03M* ｜ -4.3%
P 85 ｜ +2,413 ｜ $0.22 ｜ 名义 $53.1k* ｜ -17.8%
结构参考：99（-4.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 08-28（1D）ATM IV 54.8% vs 09-04 45.5%（差 +9.2pp）——覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/GDX_morning.json