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
🟡 **单日价格波动**: -3.3%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向

💾 每周本地备份提醒：请在 `D:\git\Option Alert-数据储存` 运行 `git pull`，把本周数据拉到本地。报告由 GitHub 自动发送，本地只做数据镜像。


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 215.71 → 收盘 210.77（-2.3%） ｜ 今日高 222.40 ｜ 低 209.12
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.95 | OI比 0.84 | ATM IV 92.8% | Skew -4.4pp | Term 0.85 | ExpMove ±0.6%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.84×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（7D）±9.1% ｜ 09-11（14D）±13.0% ｜ 09-18（21D）±15.0% ｜ 09-25（28D）±18.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 200.65（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 82%（带内） ｜ IV 有效性: VALID 505 / LOW 76 / INVALID 309
结构观察区: Primary Flip 200.65（全链重定价，覆盖 82%）
Put Wall 180（现价高于该位 17.1%） | Call Wall 250（现价低于该位 15.7%）
最近结构参考: Flip 201（现价高于该位 5.0%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（Put Wall）；上方 250（Call Wall）。
• Gamma 区域：切换参考 201（全链重定价，覆盖 82%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 235.0C — Vol 1,381 | 最新价 $0.33 | OI 1334→2617 (ΔOI +1283张) | ΔOI/Volume 92.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1283张（+96.2% vs前日OI），连续性待观察（方向未知）
08-28 255.0C — Vol 577 | 最新价 $0.03 | OI 336→1292 (ΔOI +956张) | ΔOI/Volume 165.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增956张（+284.5% vs前日OI），连续性待观察（方向未知）
09-11 130.0P — Vol 24 | 最新价 $0.12 | OI 92→961 (ΔOI +869张) | ΔOI/Volume 3620.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增869张（+944.6% vs前日OI），连续性待观察（方向未知）
09-04 145.0P — Vol 7 | 最新价 $0.13 | OI 331→1148 (ΔOI +817张) | ΔOI/Volume 11671.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增817张（+246.8% vs前日OI），连续性待观察（方向未知）
09-18 125.0P — Vol 10 | 最新价 $0.17 | OI 671→1380 (ΔOI +709张) | ΔOI/Volume 7090.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增709张（+105.7% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +6.7k / P +2.5k ｜ Activity HIGH ｜ 7D
09-11  C -1.5k / P -0.9k ｜ Activity HIGH ｜ 14D
09-18  C +3.4k / P +1.7k ｜ Activity HIGH ｜ 21D
09-25  C +0.8k / P +0.7k ｜ Activity HIGH ｜ 28D

📆 09-04 Forward Structure
OI:       C 23.0k / P 28.8k
ΔOI:      C +6.7k / P +2.5k
ATM:      C 9.90 / P 9.20
ATM IV:   81.5%
ΔOI Δ Exposure*: -5k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 275 ｜ +1,929 ｜ $0.35 ｜ 名义 $67.5k* ｜ +30.5%
C 272 ｜ +1,731 ｜ $0.61 ｜ 名义 $105.6k* ｜ +29.3%
C 270 ｜ +762 ｜ $0.51 ｜ 名义 $38.9k* ｜ +28.1%
结构参考：275（+30.5%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 11.8k / P 9.7k
ΔOI:      C -1.5k / P -0.9k
ATM:      C 14.49 / P 12.88
ATM IV:   80.3%
ΔOI Δ Exposure*: -41k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 225 ｜ -1,880 ｜ $8.25 ｜ 名义 $-1.55M* ｜ +6.8%
P 195 ｜ -1,038 ｜ $6.50 ｜ 名义 $-674.7k* ｜ -7.5%
C 240 ｜ +58 ｜ $4.60 ｜ 名义 $26.7k* ｜ +13.9%
结构参考：240（+13.9%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 118.3k / P 93.1k
ΔOI:      C +3.4k / P +1.7k
ATM:      C 16.09 / P 15.55
ATM IV:   79.6%
ΔOI Δ Exposure*: 15k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 225 ｜ +757 ｜ $11.00 ｜ 名义 $832.7k* ｜ +6.8%
C 300 ｜ +551 ｜ $1.02 ｜ 名义 $56.2k* ｜ +42.3%
C 270 ｜ +379 ｜ $2.75 ｜ 名义 $104.2k* ｜ +28.1%
结构参考：225（+6.8%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 6.8k / P 5.9k
ΔOI:      C +0.8k / P +0.7k
ATM:      C 19.80 / P 18.10
ATM IV:   78.9%
ΔOI Δ Exposure*: 5k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 250 ｜ +232 ｜ $7.35 ｜ 名义 $170.5k* ｜ +18.6%
C 230 ｜ +224 ｜ $11.45 ｜ 名义 $256.5k* ｜ +9.1%
P 200 ｜ +201 ｜ $12.45 ｜ 名义 $250.2k* ｜ -5.1%
结构参考：250（+18.6%）上方 / 200（-5.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/BE_evening.json