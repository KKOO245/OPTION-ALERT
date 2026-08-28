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
🟡 **单日价格波动**: -2.5%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 15C ΔOI +163（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-25 20C ΔOI +1,040 占该期限总 OI 14.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

💾 每周本地备份提醒：请在 `D:\git\Option Alert-数据储存` 运行 `git pull`，把本周数据拉到本地。报告由 GitHub 自动发送，本地只做数据镜像。


## UUUU

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
UUUU: 今开 15.85 → 收盘 14.67（-7.4%） ｜ 今日高 15.88 ｜ 低 14.53
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.32 | OI比 0.42 | ATM IV 202.6% | Skew -1.5pp | Term 0.35 | ExpMove ±1.2%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.32×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.42×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（7D）±7.2% ｜ 09-11（14D）±10.9% ｜ 09-18（21D）±13.0% ｜ 09-25（28D）±17.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 75%（带内） ｜ IV 有效性: VALID 194 / LOW 56 / INVALID 160
结构观察区: NO_CROSS
Put Wall 11（现价高于该位 33.4%） | Call Wall 18（现价低于该位 18.5%）
最近结构参考: Call Wall 18（现价低于该位 18.5%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 11（Put Wall）；上方 18（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 15.0C — Vol 298 | 最新价 $1.10 | OI 332→759 (ΔOI +427张) | ΔOI/Volume 143.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增427张（+128.6% vs前日OI），连续性待观察（方向未知）
09-04 14.5P — Vol 34 | 最新价 $0.20 | OI 197→489 (ΔOI +292张) | ΔOI/Volume 858.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增292张（+148.2% vs前日OI），连续性待观察（方向未知）
09-18 20.0C — Vol 36 | 最新价 $0.16 | OI 1839→2015 (ΔOI +176张) | ΔOI/Volume 488.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增176张（+9.6% vs前日OI），连续性待观察（方向未知）
09-18 21.0C — Vol 1 | 最新价 $0.16 | OI 191→339 (ΔOI +148张) | ΔOI/Volume 14800.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增148张（+77.5% vs前日OI），连续性待观察（方向未知）
08-28 17.0C — Vol 289 | 最新价 $0.02 | OI 1582→1719 (ΔOI +137张) | ΔOI/Volume 47.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增137张（+8.7% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +0.6k / P +0.2k ｜ Activity HIGH ｜ 7D
09-11  C +0.2k / P +23 ｜ Activity HIGH ｜ 14D
09-18  C +0.1k / P +5 ｜ Activity MEDIUM △ ｜ 21D
09-25  C +2.0k / P +82 ｜ Activity HIGH ｜ 28D

📆 09-04 Forward Structure
OI:       C 8.0k / P 3.1k
ΔOI:      C +0.6k / P +0.2k
ATM:      C 0.61 / P 0.44
ATM IV:   68.7%
ΔOI Δ Exposure*: 3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 15 ｜ +172 ｜ $0.22 ｜ 名义 $3.8k* ｜ +5.7%
C 15 ｜ +163 ｜ $0.42 ｜ 名义 $6.8k* ｜ +2.2%
P 15 ｜ +123 ｜ $0.77 ｜ 名义 $9.5k* ｜ +2.2%
结构参考：15（+5.7%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 2.9k / P 2.5k
ΔOI:      C +0.2k / P +23
ATM:      C 0.92 / P 0.68
ATM IV:   61.9%
ΔOI Δ Exposure*: 3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 16 ｜ +91 ｜ $0.30 ｜ 名义 $2.7k* ｜ +9.1%
C 17 ｜ +49 ｜ $0.14 ｜ 名义 $686* ｜ +15.9%
P 13 ｜ -28 ｜ $0.15 ｜ 名义 $-420* ｜ -11.4%
结构参考：16（+9.1%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 16C +66 ｜ 15C +52

📆 09-25 Forward Structure
OI:       C 6.0k / P 1.0k
ΔOI:      C +2.0k / P +82
ATM:      C 1.57 / P 1.01
ATM IV:   70.6%
ΔOI Δ Exposure*: 27k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 20 ｜ +1,040 ｜ $0.13 ｜ 名义 $13.5k* ｜ +36.3%
C 18 ｜ +962 ｜ $0.30 ｜ 名义 $28.9k* ｜ +22.7%
P 14 ｜ +27 ｜ $0.83 ｜ 名义 $2.2k* ｜ -4.6%
结构参考：20（+36.3%）上方 / 14（-4.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 09-04（7D）ATM IV 68.7% vs 09-11 61.9%（差 +6.9pp）——覆盖 Non Farm Payrolls Annual Revision Prel、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/UUUU_evening.json