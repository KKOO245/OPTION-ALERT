# 期权晨报 2026-08-28

📊 市场环境

SPY $769.34 ｜ QQQ $716.43
VIX 14.19 ↓2.2%（5D -6.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 54.4（neutral）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 -79 ｜ 前值 -911　✅ 今日已公布
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布　✅ 今日已公布

🔍 重点速览
🟡 **单日价格波动**: -3.4%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 15C ΔOI +172（距现价 +3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-25 20C ΔOI +1,040 占该期限总 OI 14.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## UUUU

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
UUUU  昨收 15.74 → 今晨 15.04（-4.4%） | 较昨收变动（含盘初走势） ｜ 今日高 15.88 ｜ 低 14.84

Options: P/C量 0.21 | OI比 0.42 | ATM IV 110.2% | Skew -2.4pp | Term 0.65 | ExpMove ±2.2%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.21×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.42×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（7D）±7.9% ｜ 09-11（14D）±10.6% ｜ 09-18（21D）±13.2% ｜ 09-25（28D）±17.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 204 / LOW 51 / INVALID 155
结构观察区: NO_CROSS
Put Wall 11（现价高于该位 36.8%） | Call Wall 18（现价低于该位 16.4%）
最近结构参考: Call Wall 18（现价低于该位 16.4%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 11（Put Wall）；上方 18（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 20.0C — Vol 41 | 最新价 $0.18 | OI 2119→3159 (ΔOI +1040张) | ΔOI/Volume 2536.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1040张（+49.1% vs前日OI），连续性待观察（方向未知）
09-25 18.0C — Vol 9 | 最新价 $0.39 | OI 252→1214 (ΔOI +962张) | ΔOI/Volume 10688.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增962张（+381.8% vs前日OI），连续性待观察（方向未知）
09-04 15.5C — Vol 122 | 最新价 $0.36 | OI 434→606 (ΔOI +172张) | ΔOI/Volume 141.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增172张（+39.6% vs前日OI），连续性待观察（方向未知）
09-04 15.0C — Vol 178 | 最新价 $0.64 | OI 759→922 (ΔOI +163张) | ΔOI/Volume 91.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增163张（+21.5% vs前日OI），连续性待观察（方向未知）
08-28 15.5C — Vol 138 | 最新价 $0.06 | OI 860→1006 (ΔOI +146张) | ΔOI/Volume 105.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增146张（+17.0% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +0.6k / P +0.2k ｜ Activity HIGH ｜ 7D
09-11  C +0.2k / P +23 ｜ Activity HIGH ｜ 14D
09-18  C +0.1k / P +5 ｜ Activity MEDIUM △ ｜ 21D
09-25  C +2.0k / P +82 ｜ Activity HIGH ｜ 28D

📆 09-04 Forward Structure
OI:       C 8.0k / P 3.1k
ΔOI:      C +0.6k / P +0.2k
ATM:      C 0.64 / P 0.55
ATM IV:   72.8%
ΔOI Δ Exposure*: 11k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 15 ｜ +172 ｜ $0.36 ｜ 名义 $6.2k* ｜ +3.0%
C 15 ｜ +163 ｜ $0.64 ｜ 名义 $10.4k* ｜ -0.3%
P 15 ｜ +123 ｜ $0.55 ｜ 名义 $6.8k* ｜ -0.3%
结构参考：15（+3.0%）上方 / 15（-0.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 2.9k / P 2.5k
ΔOI:      C +0.2k / P +23
ATM:      C 0.93 / P 0.66
ATM IV:   68.9%
ΔOI Δ Exposure*: 4k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 16 ｜ +91 ｜ $0.49 ｜ 名义 $4.5k* ｜ +6.3%
C 17 ｜ +49 ｜ $0.33 ｜ 名义 $1.6k* ｜ +13.0%
P 13 ｜ -28 ｜ $0.10 ｜ 名义 $-280* ｜ -13.6%
结构参考：16（+6.3%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 16C +66 ｜ 15C +52

📆 09-25 Forward Structure
OI:       C 6.0k / P 1.0k
ΔOI:      C +2.0k / P +82
ATM:      C 1.60 / P 1.10
ATM IV:   71.4%
ΔOI Δ Exposure*: 34k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 20 ｜ +1,040 ｜ $0.18 ｜ 名义 $18.7k* ｜ +32.9%
C 18 ｜ +962 ｜ $0.39 ｜ 名义 $37.5k* ｜ +19.6%
P 14 ｜ +27 ｜ $0.50 ｜ 名义 $1.4k* ｜ -6.9%
结构参考：20（+32.9%）上方 / 14（-6.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/UUUU_morning.json