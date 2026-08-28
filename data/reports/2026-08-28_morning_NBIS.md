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
🟡 **单日价格波动**: -3.7%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 210P ΔOI +985（距现价 -0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 214.44 → 今晨 211.47（-1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 214.28 ｜ 低 206.55

Options: P/C量 0.41 | OI比 0.79 | ATM IV 93.7% | Skew -2.5pp | Term 0.86 | ExpMove ±1.9%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.41×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（7D）±8.8% ｜ 09-11（14D）±12.3% ｜ 09-18（21D）±15.3% ｜ 09-25（28D）±17.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 211.20（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 620 / LOW 94 / INVALID 180
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: Primary Flip 211.20（全链重定价，覆盖 96%）
Put Wall 200（现价高于该位 5.7%） | Call Wall 250（现价低于该位 15.4%）
最近结构参考: Flip 211（现价高于该位 0.1%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall）；上方 250（Call Wall）。
• Gamma 区域：切换参考 211（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 200.0P — Vol 977 | 最新价 $4.50 | OI 1241→4011 (ΔOI +2770张) | ΔOI/Volume 283.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2770张（+223.2% vs前日OI），连续性待观察（方向未知）
08-28 222.5C — Vol 442 | 最新价 $0.06 | OI 396→2536 (ΔOI +2140张) | ΔOI/Volume 484.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2140张（+540.4% vs前日OI），连续性待观察（方向未知）
09-04 300.0C — Vol 441 | 最新价 $0.12 | OI 1280→2342 (ΔOI +1062张) | ΔOI/Volume 240.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1062张（+83.0% vs前日OI），连续性待观察（方向未知）
09-04 210.0P — Vol 263 | 最新价 $8.63 | OI 986→1971 (ΔOI +985张) | ΔOI/Volume 374.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增985张（+99.9% vs前日OI），连续性待观察（方向未知）
09-04 230.0C — Vol 1,825 | 最新价 $3.20 | OI 751→1626 (ΔOI +875张) | ΔOI/Volume 48.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增875张（+116.5% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +7.1k / P +7.3k ｜ Activity HIGH ｜ 7D
09-11  C +2.9k / P +0.5k ｜ Activity HIGH ｜ 14D
09-18  C +0.9k / P +0.2k ｜ Activity HIGH ｜ 21D
09-25  C +0.8k / P +0.7k ｜ Activity HIGH ｜ 28D

📆 09-04 Forward Structure
OI:       C 39.1k / P 29.9k
ΔOI:      C +7.1k / P +7.3k
ATM:      C 8.85 / P 9.87
ATM IV:   77.3%
ΔOI Δ Exposure*: -123k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 200 ｜ +2,770 ｜ $4.50 ｜ 名义 $1.25M* ｜ -5.4%
C 300 ｜ +1,062 ｜ $0.12 ｜ 名义 $12.7k* ｜ +41.9%
P 210 ｜ +985 ｜ $8.63 ｜ 名义 $850.1k* ｜ -0.7%
结构参考：300（+41.9%）上方 / 200（-5.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 10.5k / P 12.2k
ΔOI:      C +2.9k / P +0.5k
ATM:      C 12.10 / P 13.85
ATM IV:   76.5%
ΔOI Δ Exposure*: 12k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 260 ｜ +539 ｜ $1.74 ｜ 名义 $93.8k* ｜ +23.0%
C 300 ｜ +478 ｜ $0.63 ｜ 名义 $30.1k* ｜ +41.9%
C 280 ｜ +402 ｜ $0.94 ｜ 名义 $37.8k* ｜ +32.4%
结构参考：260（+23.0%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 95.6k / P 148.2k
ΔOI:      C +0.9k / P +0.2k
ATM:      C 15.65 / P 16.80
ATM IV:   78.9%
ΔOI Δ Exposure*: -2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 310 ｜ +574 ｜ $0.90 ｜ 名义 $51.7k* ｜ +46.6%
P 210 ｜ +457 ｜ $15.18 ｜ 名义 $693.7k* ｜ -0.7%
C 225 ｜ +199 ｜ $10.95 ｜ 名义 $217.9k* ｜ +6.4%
结构参考：310（+46.6%）上方 / 210（-0.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 6.8k / P 9.6k
ΔOI:      C +0.8k / P +0.7k
ATM:      C 19.56 / P 17.75
ATM IV:   80.1%
ΔOI Δ Exposure*: 3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 110 ｜ +199 ｜ $0.32 ｜ 名义 $6.4k* ｜ -48.0%
C 350 ｜ +157 ｜ $0.86 ｜ 名义 $13.5k* ｜ +65.5%
C 300 ｜ +143 ｜ $2.27 ｜ 名义 $32.5k* ｜ +41.9%
结构参考：350（+65.5%）上方 / 110（-48.0%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/NBIS_morning.json