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
🟡 **单日价格波动**: -3.4%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 185P ΔOI +1,070（距现价 +3.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-04 202C ΔOI +9,601 占该期限总 OI 12.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

💾 每周本地备份提醒：请在 `D:\git\Option Alert-数据储存` 运行 `git pull`，把本周数据拉到本地。报告由 GitHub 自动发送，本地只做数据镜像。


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 186.02 → 收盘 178.64（-4.0%） ｜ 今日高 189.10 ｜ 低 176.06
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.54 | OI比 0.73 | ATM IV 56.0% | Skew -3.9pp | Term 1.09 | ExpMove ±0.7%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（7D）±6.6% ｜ 09-11（14D）±9.0% ｜ 09-18（21D）±11.8% ｜ 09-25（28D）±11.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 82%（带内） ｜ IV 有效性: VALID 527 / LOW 169 / INVALID 404
结构观察区: NO_CROSS
Put Wall 100（现价高于该位 78.6%） | Call Wall 200（现价低于该位 10.7%）
最近结构参考: Call Wall 200（现价低于该位 10.7%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 100（Put Wall）；上方 200（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 185.0C — Vol 264 | 最新价 $10.50 | OI 522→3552 (ΔOI +3030张) | ΔOI/Volume 1147.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3030张（+580.5% vs前日OI），连续性待观察（方向未知）
09-04 192.5C — Vol 513 | 最新价 $6.94 | OI 269→2164 (ΔOI +1895张) | ΔOI/Volume 369.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1895张（+704.5% vs前日OI），连续性待观察（方向未知）
09-18 75.0P — Vol 20 | 最新价 $0.05 | OI 664→2323 (ΔOI +1659张) | ΔOI/Volume 8295.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1659张（+249.8% vs前日OI），连续性待观察（方向未知）
08-28 210.0C — Vol 3,934 | 最新价 $0.20 | OI 2534→3713 (ΔOI +1179张) | ΔOI/Volume 30.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1179张（+46.5% vs前日OI），连续性待观察（方向未知）
09-04 190.0C — Vol 941 | 最新价 $8.00 | OI 1218→1871 (ΔOI +653张) | ΔOI/Volume 69.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增653张（+53.6% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +23.5k / P +5.8k ｜ Activity HIGH ｜ 7D
09-11  C +2.3k / P +0.2k ｜ Activity HIGH ｜ 14D
09-18  C +0.8k / P -0.7k ｜ Activity MEDIUM △ ｜ 21D
09-25  C +0.8k / P +0.6k ｜ Activity HIGH ｜ 28D

📆 09-04 Forward Structure
OI:       C 53.3k / P 25.7k
ΔOI:      C +23.5k / P +5.8k
ATM:      C 6.70 / P 5.10
ATM IV:   59.5%
ΔOI Δ Exposure*: -5k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 202 ｜ +9,601 ｜ $0.77 ｜ 名义 $739.3k* ｜ +13.4%
C 195 ｜ +9,532 ｜ $1.48 ｜ 名义 $1.41M* ｜ +9.2%
P 185 ｜ +1,070 ｜ $9.75 ｜ 名义 $1.04M* ｜ +3.6%
结构参考：202（+13.4%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 11.7k / P 7.6k
ΔOI:      C +2.3k / P +0.2k
ATM:      C 8.81 / P 7.30
ATM IV:   57.8%
ΔOI Δ Exposure*: 15k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 200 ｜ +705 ｜ $2.20 ｜ 名义 $155.1k* ｜ +12.0%
C 205 ｜ +534 ｜ $1.50 ｜ 名义 $80.1k* ｜ +14.8%
C 220 ｜ +511 ｜ $0.65 ｜ 名义 $33.2k* ｜ +23.2%
结构参考：200（+12.0%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 140P -1,321 ｜ 187C +265

📆 09-25 Forward Structure
OI:       C 7.1k / P 6.4k
ΔOI:      C +0.8k / P +0.6k
ATM:      C 12.65 / P 8.70
ATM IV:   61.2%
ΔOI Δ Exposure*: -13k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 190 ｜ +304 ｜ $18.81 ｜ 名义 $571.8k* ｜ +6.4%
C 190 ｜ +260 ｜ $8.00 ｜ 名义 $208.0k* ｜ +6.4%
C 240 ｜ +155 ｜ $1.10 ｜ 名义 $17.1k* ｜ +34.3%
结构参考：190（+6.4%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/COIN_evening.json