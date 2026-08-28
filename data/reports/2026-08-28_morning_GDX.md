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
🟡 **近现价集中开仓**: 09-04 100P ΔOI +582（距现价 -1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 103.69 → 今晨 101.91（-1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 104.74 ｜ 低 100.37

Options: P/C量 0.45 | OI比 0.64 | ATM IV 55.6% | Skew -2.0pp | Term 0.82 | ExpMove ±1.1%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（7D）±5.0% ｜ 09-11（14D）±6.5% ｜ 09-18（21D）±9.0% ｜ 09-25（28D）±10.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 99.79（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 621 / LOW 207 / INVALID 214
结构观察区: Primary Flip 99.79（全链重定价，覆盖 88%）
Put Wall 80（现价高于该位 27.4%） | Call Wall 104（现价低于该位 2.0%）
最近结构参考: Call Wall 104（现价低于该位 2.0%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（Put Wall）；上方 104（Call Wall）。
• Gamma 区域：切换参考 100（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 108.0C — Vol 11,236 | 最新价 $0.03 | OI 18191→29441 (ΔOI +11250张) | ΔOI/Volume 100.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11250张（+61.8% vs前日OI），连续性待观察（方向未知）
10-02 97.0P — Vol 2 | 最新价 $3.70 | OI 5123→15153 (ΔOI +10030张) | ΔOI/Volume 501500.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10030张（+195.8% vs前日OI），连续性待观察（方向未知）
08-28 102.0P — Vol 1,919 | 最新价 $0.62 | OI 3109→11213 (ΔOI +8104张) | ΔOI/Volume 422.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8104张（+260.7% vs前日OI），连续性待观察（方向未知）
08-28 105.0C — Vol 10,328 | 最新价 $0.01 | OI 13023→17590 (ΔOI +4567张) | ΔOI/Volume 44.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4567张（+35.1% vs前日OI），连续性待观察（方向未知）
09-18 104.0P — Vol 116 | 最新价 $4.97 | OI 830→5317 (ΔOI +4487张) | ΔOI/Volume 3868.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4487张（+540.6% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +2.2k / P +1.0k ｜ Activity HIGH ｜ 7D
09-11  C +0.1k / P +0.5k ｜ Activity HIGH ｜ 14D
09-18  C +3.5k / P +5.5k ｜ Activity HIGH ｜ 21D
09-25  C +89 / P +0.7k ｜ Activity HIGH ｜ 28D

📆 09-04 Forward Structure
OI:       C 16.8k / P 59.2k
ΔOI:      C +2.2k / P +1.0k
ATM:      C 2.45 / P 2.60
ATM IV:   43.0%
ΔOI Δ Exposure*: 4k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 110 ｜ +1,368 ｜ $0.43 ｜ 名义 $58.8k* ｜ +7.9%
P 100 ｜ +582 ｜ $1.64 ｜ 名义 $95.4k* ｜ -1.9%
P 95 ｜ -519 ｜ $0.42 ｜ 名义 $-21.8k* ｜ -6.8%
结构参考：110（+7.9%）上方 / 100（-1.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 10.6k / P 19.9k
ΔOI:      C +0.1k / P +0.5k
ATM:      C 3.40 / P 3.23
ATM IV:   42.0%
ΔOI Δ Exposure*: -10k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 100 ｜ +266 ｜ $2.15 ｜ 名义 $57.2k* ｜ -1.9%
P 98 ｜ +85 ｜ $1.48 ｜ 名义 $12.6k* ｜ -3.8%
P 85 ｜ +80 ｜ $0.09 ｜ 名义 $720* ｜ -16.6%
结构参考：100（-1.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 251.4k / P 381.6k
ΔOI:      C +3.5k / P +5.5k
ATM:      C 4.94 / P 4.20
ATM IV:   44.3%
ΔOI Δ Exposure*: -120k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 104 ｜ +4,487 ｜ $4.97 ｜ 名义 $2.23M* ｜ +2.1%
C 100 ｜ +2,531 ｜ $5.46 ｜ 名义 $1.38M* ｜ -1.9%
P 85 ｜ -1,685 ｜ $0.23 ｜ 名义 $-38.8k* ｜ -16.6%
结构参考：104（+2.1%）上方 / 100（-1.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 5.0k / P 5.4k
ΔOI:      C +89 / P +0.7k
ATM:      C 5.59 / P 5.50
ATM IV:   45.4%
ΔOI Δ Exposure*: -12k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 95 ｜ +340 ｜ $2.09 ｜ 名义 $71.1k* ｜ -6.8%
P 86 ｜ +174 ｜ $0.43 ｜ 名义 $7.5k* ｜ -15.6%
P 96 ｜ +76 ｜ $2.40 ｜ 名义 $18.2k* ｜ -5.8%
结构参考：95（-6.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/GDX_morning.json