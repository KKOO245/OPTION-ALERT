# 期权晨报 2026-08-27

📊 市场环境

SPY $770.53 ｜ QQQ $719.11
VIX 14.49 ↓4.7%（5D -9.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 58.3（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911


## QQQ

🔍 重点速览
🟡 **近现价集中开仓**: 08-28 730C ΔOI +5,931（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 717.78 → 今晨 719.09（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 719.58 ｜ 低 714.53

Options: P/C量 1.08 | OI比 1.43 | ATM IV 19.6% | Skew 3.2pp | Term 0.90 | ExpMove ±0.4%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 1.08×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.43×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 08-28（1D）±0.9% ｜ 08-31（4D）±1.2% ｜ 09-01（5D）±1.4% ｜ 09-02（6D）±1.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 711.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 3041 / LOW 459 / INVALID 2240
结构观察区: ≈712（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 700: +2.7% | 距 Call Wall 730: -1.5%
最近结构参考: Flip 712（距现价 +1.1%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall）；上方 730（Call Wall）。
• Gamma 区域：切换参考 712（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 425.0P — Vol 0 | 最新价 $0.01 | OI 39→18641 (ΔOI +18602张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18602张（+47697.4% vs前日OI），连续性待观察（方向未知）
08-28 625.0P — Vol 1 | 最新价 $0.02 | OI 942→17225 (ΔOI +16283张) | ΔOI/Volume 1628300.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16283张（+1728.6% vs前日OI），连续性待观察（方向未知）
08-27 700.0P — Vol 7,682 | 最新价 $0.01 | OI 3548→13827 (ΔOI +10279张) | ΔOI/Volume 133.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10279张（+289.7% vs前日OI），连续性待观察（方向未知）
09-30 715.0C — Vol 156 | 最新价 $18.07 | OI 544→10403 (ΔOI +9859张) | ΔOI/Volume 6319.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9859张（+1812.3% vs前日OI），连续性待观察（方向未知）
09-30 730.0C — Vol 799 | 最新价 $10.68 | OI 4744→12936 (ΔOI +8192张) | ΔOI/Volume 1025.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8192张（+172.7% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +18.7k / P +24.8k ｜ Activity HIGH ｜ 1D
08-31  C +22.6k / P +8.9k ｜ Activity HIGH ｜ 4D
09-01  C +4.2k / P +14.9k ｜ Activity HIGH ｜ 5D
09-02  C +5.1k / P +9.3k ｜ Activity HIGH ｜ 6D

📆 08-28 Forward Structure
OI:       C 340.3k / P 317.2k
ΔOI:      C +18.7k / P +24.8k
ATM:      C 3.34 / P 3.11
ATM IV:   19.3%
ΔOI Δ Exposure*: 738k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 625 ｜ +16,283 ｜ $0.02 ｜ 名义 $32.6k* ｜ -13.1%
C 730 ｜ +5,931 ｜ $0.20 ｜ 名义 $118.6k* ｜ +1.5%
P 689 ｜ +2,390 ｜ $0.05 ｜ 名义 $11.9k* ｜ -4.2%
结构参考：730（+1.5%）上方 / 625（-13.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 08-31 Forward Structure
OI:       C 388.0k / P 252.6k
ΔOI:      C +22.6k / P +8.9k
ATM:      C 4.59 / P 4.25
ATM IV:   14.3%
ΔOI Δ Exposure*: 672k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 740 ｜ +6,511 ｜ $0.09 ｜ 名义 $58.6k* ｜ +2.9%
C 725 ｜ +5,856 ｜ $1.94 ｜ 名义 $1.14M* ｜ +0.8%
C 716 ｜ +5,128 ｜ $6.43 ｜ 名义 $3.30M* ｜ -0.4%
结构参考：740（+2.9%）上方 / 716（-0.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-01 Forward Structure
OI:       C 29.2k / P 51.0k
ΔOI:      C +4.2k / P +14.9k
ATM:      C 5.33 / P 5.00
ATM IV:   15.0%
ΔOI Δ Exposure*: 177k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 675 ｜ +7,834 ｜ $0.17 ｜ 名义 $133.2k* ｜ -6.1%
P 676 ｜ +2,344 ｜ $0.18 ｜ 名义 $42.2k* ｜ -6.0%
C 710 ｜ +1,722 ｜ $11.28 ｜ 名义 $1.94M* ｜ -1.3%
结构参考：675（-6.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 13.3k / P 22.4k
ΔOI:      C +5.1k / P +9.3k
ATM:      C 5.97 / P 5.67
ATM IV:   15.5%
ΔOI Δ Exposure*: 117k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 685 ｜ +2,076 ｜ $0.37 ｜ 名义 $76.8k* ｜ -4.7%
P 693 ｜ +1,152 ｜ $0.68 ｜ 名义 $78.3k* ｜ -3.6%
C 728 ｜ +1,082 ｜ $2.19 ｜ 名义 $237.0k* ｜ +1.2%
结构参考：728（+1.2%）上方 / 685（-4.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 08-28（1D）ATM IV 19.3% vs 08-31 14.3%（差 +5.0pp）——覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/QQQ_morning.json