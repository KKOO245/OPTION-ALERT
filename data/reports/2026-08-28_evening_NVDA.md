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
🟡 **单日价格波动**: -2.9%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 08-31 225C ΔOI +6,754（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-04 235C ΔOI +125,068 占该期限总 OI 13.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

💾 每周本地备份提醒：请在 `D:\git\Option Alert-数据储存` 运行 `git pull`，把本周数据拉到本地。报告由 GitHub 自动发送，本地只做数据镜像。


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 227.33 → 收盘 217.55（-4.3%） ｜ 今日高 229.26 ｜ 低 216.81
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.61 | OI比 0.73 | ATM IV 23.8% | Skew 0.6pp | Term 1.35 | ExpMove ±0.1%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-31（3D）±1.8% ｜ 09-02（5D）±3.0% ｜ 09-04（7D）±3.7% ｜ 09-09（12D）±4.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 205.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 671 / LOW 212 / INVALID 425
结构观察区: Primary Flip 205.43（全链重定价，覆盖 84%）
Put Wall 190（现价高于该位 14.5%） | Call Wall 240（现价低于该位 9.4%）
最近结构参考: Flip 205（现价高于该位 5.9%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（Put Wall）；上方 240（Call Wall）。
• Gamma 区域：切换参考 205（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 220.0C — Vol 126,703 | 最新价 $8.25 | OI 60397→96107 (ΔOI +35710张) | ΔOI/Volume 28.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增35710张（+59.1% vs前日OI），连续性待观察（方向未知）
08-28 200.0P — Vol 63,437 | 最新价 $0.03 | OI 36789→58748 (ΔOI +21959张) | ΔOI/Volume 34.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21959张（+59.7% vs前日OI），连续性待观察（方向未知）
08-28 230.0C — Vol 684,401 | 最新价 $1.15 | OI 194582→210864 (ΔOI +16282张) | ΔOI/Volume 2.4% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增16282张（+8.4% vs前日OI），值得跟踪（方向未知）
08-28 235.0C — Vol 209,455 | 最新价 $0.25 | OI 41317→57195 (ΔOI +15878张) | ΔOI/Volume 7.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15878张（+38.4% vs前日OI），连续性待观察（方向未知）
09-04 115.0P — Vol 339 | 最新价 $0.01 | OI 16267→31530 (ΔOI +15263张) | ΔOI/Volume 4502.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15263张（+93.8% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-31  C +24.6k / P +27.5k ｜ Activity HIGH ｜ 3D
09-02  C +5.4k / P +22.9k ｜ Activity HIGH ｜ 5D
09-04  C +365.3k / P +74.9k ｜ Activity HIGH ｜ 7D
09-09  C +30.5k / P +4.7k ｜ Activity HIGH ｜ 12D

📆 08-31 Forward Structure
OI:       C 141.7k / P 90.3k
ΔOI:      C +24.6k / P +27.5k
ATM:      C 1.99 / P 1.89
ATM IV:   24.9%
ΔOI Δ Exposure*: -2.2M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 235 ｜ +7,817 ｜ $0.04 ｜ 名义 $31.3k* ｜ +8.0%
C 225 ｜ +6,754 ｜ $0.18 ｜ 名义 $121.6k* ｜ +3.4%
C 230 ｜ +4,566 ｜ $0.05 ｜ 名义 $22.8k* ｜ +5.7%
结构参考：235（+8.0%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 56.3k / P 43.5k
ΔOI:      C +5.4k / P +22.9k
ATM:      C 3.30 / P 3.19
ATM IV:   31.8%
ΔOI Δ Exposure*: -1.0M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 202 ｜ +3,455 ｜ $0.23 ｜ 名义 $79.5k* ｜ -6.9%
P 220 ｜ +3,329 ｜ $4.65 ｜ 名义 $1.55M* ｜ +1.1%
P 207 ｜ +3,190 ｜ $0.50 ｜ 名义 $159.5k* ｜ -4.6%
结构参考：220（+1.1%）上方 / 202（-6.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 577.4k / P 324.6k
ΔOI:      C +365.3k / P +74.9k
ATM:      C 4.15 / P 3.90
ATM IV:   33.0%
ΔOI Δ Exposure*: -852k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 235 ｜ +125,068 ｜ $0.36 ｜ 名义 $4.50M* ｜ +8.0%
C 245 ｜ +110,437 ｜ $0.13 ｜ 名义 $1.44M* ｜ +12.6%
C 225 ｜ +47,158 ｜ $1.46 ｜ 名义 $6.89M* ｜ +3.4%
结构参考：235（+8.0%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-09 Forward Structure
OI:       C 44.8k / P 8.5k
ΔOI:      C +30.5k / P +4.7k
ATM:      C 5.15 / P 4.53
ATM IV:   30.2%
ΔOI Δ Exposure*: 9k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 240 ｜ +11,671 ｜ $0.39 ｜ 名义 $455.2k* ｜ +10.3%
C 230 ｜ +8,891 ｜ $1.15 ｜ 名义 $1.02M* ｜ +5.7%
C 250 ｜ +6,481 ｜ $0.15 ｜ 名义 $97.2k* ｜ +14.9%
结构参考：240（+10.3%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/NVDA_evening.json