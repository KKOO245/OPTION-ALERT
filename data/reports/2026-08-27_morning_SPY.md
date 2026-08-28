# 期权晨报 2026-08-27

📊 市场环境

SPY $771.10 ｜ QQQ $721.11
VIX 14.49 ↓4.7%（5D -9.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 58.2（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 08-28 778C ΔOI +3,347（距现价 +1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 769.98 → 今晨 770.53（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 771.10 ｜ 低 767.16

Options: P/C量 0.84 | OI比 1.26 | ATM IV 12.8% | Skew 2.6pp | Term 0.92 | ExpMove ±0.3%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.26×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 08-28（1D）±0.6% ｜ 08-31（4D）±0.8% ｜ 09-01（5D）±0.9% ｜ 09-02（6D）±1.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 768.78（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 3086 / LOW 504 / INVALID 2266
结构观察区: ≈769（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 535: +44.0% | 距 Call Wall 800: -3.7%
最近结构参考: Flip 769（距现价 +0.2%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 535（Put Wall）；上方 800（Call Wall）。
• Gamma 区域：切换参考 769（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-30 800.0C — Vol 1,054 | 最新价 $1.50 | OI 50235→64519 (ΔOI +14284张) | ΔOI/Volume 1355.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14284张（+28.4% vs前日OI），连续性待观察（方向未知）
09-04 760.0P — Vol 34,718 | 最新价 $1.69 | OI 44755→57595 (ΔOI +12840张) | ΔOI/Volume 37.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12840张（+28.7% vs前日OI），连续性待观察（方向未知）
08-31 745.0P — Vol 13,772 | 最新价 $0.08 | OI 10095→22058 (ΔOI +11963张) | ΔOI/Volume 86.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11963张（+118.5% vs前日OI），连续性待观察（方向未知）
09-04 747.0P — Vol 5,766 | 最新价 $0.55 | OI 785→11075 (ΔOI +10290张) | ΔOI/Volume 178.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10290张（+1310.8% vs前日OI），连续性待观察（方向未知）
08-27 732.0P — Vol 0 | 最新价 $0.03 | OI 435→6718 (ΔOI +6283张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6283张（+1444.4% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +16.2k / P +12.1k ｜ Activity HIGH ｜ 1D
08-31  C +13.0k / P +23.3k ｜ Activity HIGH ｜ 4D
09-01  C +9.1k / P +8.2k ｜ Activity HIGH ｜ 5D
09-02  C +6.4k / P +9.6k ｜ Activity HIGH ｜ 6D

📆 08-28 Forward Structure
OI:       C 236.3k / P 320.6k
ΔOI:      C +16.2k / P +12.1k
ATM:      C 2.27 / P 2.42
ATM IV:   13.1%
ΔOI Δ Exposure*: 279k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 712 ｜ +4,985 ｜ $0.01 ｜ 名义 $5.0k* ｜ -7.6%
P 713 ｜ +4,146 ｜ $0.02 ｜ 名义 $8.3k* ｜ -7.5%
C 778 ｜ +3,347 ｜ $0.22 ｜ 名义 $73.6k* ｜ +1.0%
结构参考：778（+1.0%）上方 / 712（-7.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 08-31 Forward Structure
OI:       C 331.2k / P 723.3k
ΔOI:      C +13.0k / P +23.3k
ATM:      C 3.01 / P 3.07
ATM IV:   9.2%
ΔOI Δ Exposure*: 386k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 745 ｜ +11,963 ｜ $0.08 ｜ 名义 $95.7k* ｜ -3.3%
C 769 ｜ +3,699 ｜ $4.20 ｜ 名义 $1.55M* ｜ -0.2%
P 711 ｜ +3,401 ｜ $0.04 ｜ 名义 $13.6k* ｜ -7.7%
结构参考：745（-3.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-01 Forward Structure
OI:       C 45.9k / P 40.4k
ΔOI:      C +9.1k / P +8.2k
ATM:      C 3.47 / P 3.58
ATM IV:   9.5%
ΔOI Δ Exposure*: 233k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 782 ｜ +3,564 ｜ $0.27 ｜ 名义 $96.2k* ｜ +1.5%
P 739 ｜ +2,147 ｜ $0.11 ｜ 名义 $23.6k* ｜ -4.1%
P 761 ｜ +2,063 ｜ $0.92 ｜ 名义 $189.8k* ｜ -1.2%
结构参考：782（+1.5%）上方 / 739（-4.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 24.6k / P 31.9k
ΔOI:      C +6.4k / P +9.6k
ATM:      C 3.99 / P 4.01
ATM IV:   9.8%
ΔOI Δ Exposure*: 211k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 750 ｜ +1,325 ｜ $0.35 ｜ 名义 $46.4k* ｜ -2.7%
P 766 ｜ +1,003 ｜ $2.31 ｜ 名义 $231.7k* ｜ -0.6%
C 775 ｜ +988 ｜ $1.98 ｜ 名义 $195.6k* ｜ +0.6%
结构参考：775（+0.6%）上方 / 750（-2.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/SPY_morning.json