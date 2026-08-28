# 期权晚报 2026-08-28

📊 市场环境

SPY $769.35 ｜ QQQ $716.43
VIX 14.43 ↓0.6%（5D -4.6%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 54.4（neutral）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 -79 ｜ 前值 -911　✅ 今日已公布
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-04 1440P ΔOI +1,008（距现价 -3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 1462.8）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

💾 每周本地备份提醒：请在 `D:\git\Option Alert-数据储存` 运行 `git pull`，把本周数据拉到本地。报告由 GitHub 自动发送，本地只做数据镜像。


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,445.54 → 收盘 1,484.98（+2.7%） ｜ 今日高 1517.75 ｜ 低 1435.61
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.62 | OI比 0.67 | ATM IV 84.8% | Skew -1.1pp | Term 0.78 | ExpMove ±0.5%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.67×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（7D）±7.2% ｜ 09-11（14D）±10.1% ｜ 09-18（21D）±12.5% ｜ 09-25（28D）±14.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Candidates 1462.79 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 78%（带内） ｜ IV 有效性: VALID 1844 / LOW 598 / INVALID 1340
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: ≈1463（全链重定价，覆盖 78%，CONDITIONAL）
Put Wall 1,200（现价高于该位 23.7%） | Call Wall 2,000（现价低于该位 25.8%）
最近结构参考: Flip 1463（现价高于该位 1.5%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,200（Put Wall）；上方 2,000（Call Wall）。
• Gamma 区域：切换参考 1463（全链重定价，覆盖 78%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 1700.0C — Vol 8,847 | 最新价 $0.32 | OI 6535→8127 (ΔOI +1592张) | ΔOI/Volume 18.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1592张（+24.4% vs前日OI），连续性待观察（方向未知）
09-04 1280.0P — Vol 35 | 最新价 $7.35 | OI 75→944 (ΔOI +869张) | ΔOI/Volume 2482.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增869张（+1158.7% vs前日OI），连续性待观察（方向未知）
09-04 1465.0P — Vol 41 | 最新价 $57.40 | OI 27→892 (ΔOI +865张) | ΔOI/Volume 2109.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增865张（+3203.7% vs前日OI），连续性待观察（方向未知）
09-04 1720.0C — Vol 73 | 最新价 $8.32 | OI 80→926 (ΔOI +846张) | ΔOI/Volume 1158.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增846张（+1057.5% vs前日OI），连续性待观察（方向未知）
08-28 1650.0C — Vol 3,453 | 最新价 $0.60 | OI 1449→2042 (ΔOI +593张) | ΔOI/Volume 17.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增593张（+40.9% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +4.5k / P +5.2k ｜ Activity HIGH ｜ 7D
09-11  C +0.6k / P +0.5k ｜ Activity HIGH ｜ 14D
09-18  C +1.4k / P +0.2k ｜ Activity MEDIUM △ ｜ 21D
09-25  C +0.5k / P +0.5k ｜ Activity HIGH ｜ 28D

📆 09-04 Forward Structure
OI:       C 24.5k / P 24.2k
ΔOI:      C +4.5k / P +5.2k
ATM:      C 53.72 / P 53.00
ATM IV:   65.0%
ΔOI Δ Exposure*: -18k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 1440 ｜ +1,008 ｜ $35.00 ｜ 名义 $3.53M* ｜ -3.0%
P 1265 ｜ +978 ｜ $2.55 ｜ 名义 $249.4k* ｜ -14.8%
C 1710 ｜ +956 ｜ $4.60 ｜ 名义 $439.8k* ｜ +15.2%
结构参考：1710（+15.2%）上方 / 1440（-3.0%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 5.6k / P 9.5k
ΔOI:      C +0.6k / P +0.5k
ATM:      C 73.00 / P 77.46
ATM IV:   63.5%
ΔOI Δ Exposure*: 11k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 1550 ｜ +106 ｜ $48.47 ｜ 名义 $513.8k* ｜ +4.4%
P 1100 ｜ +47 ｜ $1.20 ｜ 名义 $5.6k* ｜ -25.9%
P 1270 ｜ +38 ｜ $9.39 ｜ 名义 $35.7k* ｜ -14.5%
结构参考：1550（+4.4%）上方 / 1100（-25.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 1700C +364 ｜ 1800C +270

📆 09-25 Forward Structure
OI:       C 4.2k / P 9.2k
ΔOI:      C +0.5k / P +0.5k
ATM:      C 110.30 / P 111.48
ATM IV:   66.2%
ΔOI Δ Exposure*: 3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 1500 ｜ +97 ｜ $104.14 ｜ 名义 $1.01M* ｜ +1.0%
C 1550 ｜ +77 ｜ $95.00 ｜ 名义 $731.5k* ｜ +4.4%
C 1875 ｜ +69 ｜ $24.30 ｜ 名义 $167.7k* ｜ +26.3%
结构参考：1500（+1.0%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/SNDK_evening.json