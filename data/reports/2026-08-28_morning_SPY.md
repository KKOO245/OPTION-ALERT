# 期权晨报 2026-08-28

📊 市场环境

SPY $769.24 ｜ QQQ $716.43
VIX 14.19 ↓2.2%（5D -6.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 54.4（neutral）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 -79 ｜ 前值 -911　✅ 今日已公布
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 08-31 745P ΔOI -10,053（距现价 -3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 771.10 → 今晨 774.46（+0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 775.29 ｜ 低 769.78

Options: P/C量 0.98 | OI比 1.52 | ATM IV 13.3% | Skew 2.4pp | Term 0.85 | ExpMove ±0.3%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.98×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.52×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 08-31（3D）±0.5% ｜ 09-01（4D）±0.7% ｜ 09-02（5D）±0.8% ｜ 09-03（6D）±0.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 771.20（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 3381 / LOW 535 / INVALID 1852
结构观察区: Primary Flip 771.20（全链重定价，覆盖 95%）
Put Wall 535（现价高于该位 44.8%） | Call Wall 800（现价低于该位 3.2%）
最近结构参考: Flip 771（现价高于该位 0.4%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 535（Put Wall）；上方 800（Call Wall）。
• Gamma 区域：切换参考 771（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 765.0P — Vol 18,658 | 最新价 $1.36 | OI 6791→52483 (ΔOI +45692张) | ΔOI/Volume 244.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增45692张（+672.8% vs前日OI），连续性待观察（方向未知）
09-18 734.0P — Vol 7,199 | 最新价 $1.24 | OI 7877→26271 (ΔOI +18394张) | ΔOI/Volume 255.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18394张（+233.5% vs前日OI），连续性待观察（方向未知）
08-28 747.0P — Vol 19,824 | 最新价 $0.01 | OI 1666→17762 (ΔOI +16096张) | ΔOI/Volume 81.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16096张（+966.1% vs前日OI），连续性待观察（方向未知）
09-18 750.0P — Vol 6,139 | 最新价 $2.36 | OI 40137→53259 (ΔOI +13122张) | ΔOI/Volume 213.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13122张（+32.7% vs前日OI），连续性待观察（方向未知）
08-28 748.0P — Vol 2,307 | 最新价 $0.01 | OI 3749→16420 (ΔOI +12671张) | ΔOI/Volume 549.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12671张（+338.0% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-31  C +14.9k / P +14.2k ｜ Activity MEDIUM △ ｜ 3D
09-01  C +8.0k / P +8.2k ｜ Activity HIGH ｜ 4D
09-02  C +10.9k / P +30.9k ｜ Activity HIGH ｜ 5D
09-03  C +8.5k / P +9.5k ｜ Activity HIGH ｜ 6D

   Top ΔOI: 745P -10,053 ｜ 780C +3,966

📆 09-01 Forward Structure
OI:       C 53.9k / P 48.6k
ΔOI:      C +8.0k / P +8.2k
ATM:      C 2.92 / P 2.30
ATM IV:   7.8%
ΔOI Δ Exposure*: 263k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 777 ｜ +1,629 ｜ $1.43 ｜ 名义 $232.9k* ｜ +0.3%
C 775 ｜ +1,019 ｜ $2.34 ｜ 名义 $238.4k* ｜ +0.1%
P 761 ｜ +1,001 ｜ $0.22 ｜ 名义 $22.0k* ｜ -1.7%
结构参考：777（+0.3%）上方 / 761（-1.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 35.5k / P 62.8k
ΔOI:      C +10.9k / P +30.9k
ATM:      C 3.43 / P 2.82
ATM IV:   8.4%
ΔOI Δ Exposure*: 113k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 766 ｜ +9,776 ｜ $0.83 ｜ 名义 $811.4k* ｜ -1.1%
P 690 ｜ +7,999 ｜ $0.03 ｜ 名义 $24.0k* ｜ -10.9%
P 700 ｜ +5,214 ｜ $0.05 ｜ 名义 $26.1k* ｜ -9.6%
结构参考：766（-1.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-03 Forward Structure
OI:       C 27.6k / P 28.6k
ΔOI:      C +8.5k / P +9.5k
ATM:      C 4.06 / P 3.33
ATM IV:   8.9%
ΔOI Δ Exposure*: 193k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 775 ｜ +2,498 ｜ $3.41 ｜ 名义 $851.8k* ｜ +0.1%
P 769 ｜ +1,245 ｜ $1.66 ｜ 名义 $206.7k* ｜ -0.7%
P 718 ｜ +1,000 ｜ $0.10 ｜ 名义 $10.0k* ｜ -7.3%
结构参考：775（+0.1%）上方 / 769（-0.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/SPY_morning.json