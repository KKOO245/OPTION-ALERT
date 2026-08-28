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
🟡 **近现价集中开仓**: 09-04 58P ΔOI +132（距现价 +3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

💾 每周本地备份提醒：请在 `D:\git\Option Alert-数据储存` 运行 `git pull`，把本周数据拉到本地。报告由 GitHub 自动发送，本地只做数据镜像。


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 58.99 → 收盘 56.13（-4.8%） ｜ 今日高 59.80 ｜ 低 55.64
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.44 | OI比 0.53 | ATM IV 70.7% | Skew -8.1pp | Term 0.94 | ExpMove ±0.8%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.53×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（7D）±7.2% ｜ 09-11（14D）±9.9% ｜ 09-18（21D）±12.3% ｜ 09-25（28D）±15.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 54.12（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 305 / LOW 71 / INVALID 150
结构观察区: Primary Flip 54.12（全链重定价，覆盖 90%）
Put Wall 55（现价高于该位 2.1%） | Call Wall 60（现价低于该位 6.4%）
最近结构参考: Put Wall 55（现价高于该位 2.1%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 55（Put Wall）；上方 60（Call Wall）。
• Gamma 区域：切换参考 54（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 50.0P — Vol 21 | 最新价 $1.33 | OI 72→1079 (ΔOI +1007张) | ΔOI/Volume 4795.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1007张（+1398.6% vs前日OI），连续性待观察（方向未知）
08-28 65.0C — Vol 348 | 最新价 $0.03 | OI 1653→1971 (ΔOI +318张) | ΔOI/Volume 91.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增318张（+19.2% vs前日OI），连续性待观察（方向未知）
09-18 65.0C — Vol 187 | 最新价 $1.93 | OI 5230→5433 (ΔOI +203张) | ΔOI/Volume 108.6% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增203张（+3.9% vs前日OI），值得跟踪（方向未知）
09-18 64.0P — Vol 0 | 最新价 $7.15 | OI 0→144 (ΔOI +144张) | ΔOI/Volume N/A | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增144张（量数据缺失），以日内换手为主
08-28 63.0C — Vol 264 | 最新价 $0.09 | OI 1034→1174 (ΔOI +140张) | ΔOI/Volume 53.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增140张（+13.5% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +1.6k / P +0.9k ｜ Activity HIGH ｜ 7D
09-11  C +94 / P +93 ｜ Activity MEDIUM △ ｜ 14D
09-18  C -0.4k / P +29 ｜ Activity MEDIUM △ ｜ 21D
09-25  C +60 / P +0.2k ｜ Activity HIGH ｜ 28D

📆 09-04 Forward Structure
OI:       C 8.7k / P 6.2k
ΔOI:      C +1.6k / P +0.9k
ATM:      C 2.07 / P 1.97
ATM IV:   65.1%
ΔOI Δ Exposure*: 755 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 70 ｜ +934 ｜ $0.10 ｜ 名义 $9.3k* ｜ +24.7%
P 47 ｜ +167 ｜ $0.12 ｜ 名义 $2.0k* ｜ -16.3%
P 58 ｜ +132 ｜ $3.14 ｜ 名义 $41.4k* ｜ +3.3%
结构参考：70（+24.7%）上方 / 47（-16.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 60C +56 ｜ 62C +24

   Top ΔOI: 70C -788 ｜ 63C +143

📆 09-25 Forward Structure
OI:       C 3.1k / P 3.3k
ΔOI:      C +60 / P +0.2k
ATM:      C 4.72 / P 4.00
ATM IV:   66.6%
ΔOI Δ Exposure*: -2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 45 ｜ +100 ｜ $0.41 ｜ 名义 $4.1k* ｜ -19.8%
P 55 ｜ +48 ｜ $3.45 ｜ 名义 $16.6k* ｜ -2.0%
C 63 ｜ +17 ｜ $1.90 ｜ 名义 $3.2k* ｜ +12.2%
结构参考：63（+12.2%）上方 / 45（-19.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/MP_evening.json