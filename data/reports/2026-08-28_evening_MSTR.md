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
🟡 **单日价格波动**: -4.2%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-11 124C ΔOI +646（距现价 -2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

💾 每周本地备份提醒：请在 `D:\git\Option Alert-数据储存` 运行 `git pull`，把本周数据拉到本地。报告由 GitHub 自动发送，本地只做数据镜像。


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 134.02 → 收盘 127.31（-5.0%） ｜ 今日高 135.96 ｜ 低 126.34
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.43 | OI比 0.83 | ATM IV 50.7% | Skew -3.5pp | Term 1.32 | ExpMove ±0.3%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（7D）±7.5% ｜ 09-11（14D）±10.1% ｜ 09-18（21D）±12.6% ｜ 09-25（28D）±14.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 80%（带内） ｜ IV 有效性: VALID 817 / LOW 111 / INVALID 426
结构观察区: NO_CROSS
Put Wall 60（现价高于该位 112.2%） | Call Wall 100（现价高于该位 27.3%）
最近结构参考: Call Wall 100（现价高于该位 27.3%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 60（Put Wall）；上方 100（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 130.0C — Vol 30,388 | 最新价 $7.85 | OI 22587→33158 (ΔOI +10571张) | ΔOI/Volume 34.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10571张（+46.8% vs前日OI），连续性待观察（方向未知）
08-28 128.0C — Vol 15,146 | 最新价 $9.90 | OI 9948→18083 (ΔOI +8135张) | ΔOI/Volume 53.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8135张（+81.8% vs前日OI），连续性待观察（方向未知）
08-28 150.0C — Vol 22,072 | 最新价 $0.33 | OI 6821→12646 (ΔOI +5825张) | ΔOI/Volume 26.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5825张（+85.4% vs前日OI），连续性待观察（方向未知）
08-28 126.0C — Vol 6,155 | 最新价 $11.79 | OI 1835→7335 (ΔOI +5500张) | ΔOI/Volume 89.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5500张（+299.7% vs前日OI），连续性待观察（方向未知）
08-28 125.0C — Vol 9,374 | 最新价 $12.94 | OI 3280→7770 (ΔOI +4490张) | ΔOI/Volume 47.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4490张（+136.9% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +81.5k / P +21.4k ｜ Activity HIGH ｜ 7D
09-11  C +2.8k / P +3.4k ｜ Activity HIGH ｜ 14D
09-18  C +8.6k / P +3.4k ｜ Activity HIGH ｜ 21D
09-25  C +0.6k / P +1.0k ｜ Activity HIGH ｜ 28D

📆 09-04 Forward Structure
OI:       C 133.7k / P 128.1k
ΔOI:      C +81.5k / P +21.4k
ATM:      C 4.99 / P 4.57
ATM IV:   67.4%
ΔOI Δ Exposure*: 249k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 140 ｜ +18,138 ｜ $1.24 ｜ 名义 $2.25M* ｜ +10.0%
C 146 ｜ +16,454 ｜ $0.70 ｜ 名义 $1.15M* ｜ +14.7%
C 147 ｜ +8,288 ｜ $0.65 ｜ 名义 $538.7k* ｜ +15.5%
结构参考：140（+10.0%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 23.4k / P 50.4k
ΔOI:      C +2.8k / P +3.4k
ATM:      C 6.66 / P 6.16
ATM IV:   63.4%
ΔOI Δ Exposure*: -9k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 85 ｜ +1,683 ｜ $0.15 ｜ 名义 $25.2k* ｜ -33.2%
C 140 ｜ +843 ｜ $2.50 ｜ 名义 $210.8k* ｜ +10.0%
C 124 ｜ +646 ｜ $8.40 ｜ 名义 $542.6k* ｜ -2.6%
结构参考：140（+10.0%）上方 / 85（-33.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 257.7k / P 176.0k
ΔOI:      C +8.6k / P +3.4k
ATM:      C 8.40 / P 7.68
ATM IV:   66.2%
ΔOI Δ Exposure*: -177k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 200 ｜ +3,657 ｜ $0.32 ｜ 名义 $117.0k* ｜ +57.1%
C 180 ｜ +2,838 ｜ $0.57 ｜ 名义 $161.8k* ｜ +41.4%
C 220 ｜ +2,651 ｜ $0.15 ｜ 名义 $39.8k* ｜ +72.8%
结构参考：200（+57.1%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 13.9k / P 17.3k
ΔOI:      C +0.6k / P +1.0k
ATM:      C 9.75 / P 8.68
ATM IV:   67.1%
ΔOI Δ Exposure*: -42k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 140 ｜ -393 ｜ $5.15 ｜ 名义 $-202.4k* ｜ +10.0%
P 130 ｜ +305 ｜ $10.80 ｜ 名义 $329.4k* ｜ +2.1%
P 120 ｜ +255 ｜ $5.60 ｜ 名义 $142.8k* ｜ -5.7%
结构参考：130（+2.1%）上方 / 120（-5.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/MSTR_evening.json