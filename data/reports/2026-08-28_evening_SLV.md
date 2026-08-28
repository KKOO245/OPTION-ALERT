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
🟡 **单日价格波动**: -4.4%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 08-31 62P ΔOI +549（距现价 +3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-02 60P ΔOI +2,199 占该期限总 OI 10.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

💾 每周本地备份提醒：请在 `D:\git\Option Alert-数据储存` 运行 `git pull`，把本周数据拉到本地。报告由 GitHub 自动发送，本地只做数据镜像。


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 63.93 → 收盘 60.02（-6.1%） ｜ 今日高 64.29 ｜ 低 59.73
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.80 | OI比 0.57 | ATM IV 92.4% | Skew -3.3pp | Term 0.45 | ExpMove ±0.4%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.80×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.57×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-31（3D）±2.1% ｜ 09-02（5D）±3.3% ｜ 09-04（7D）±4.4% ｜ 09-09（12D）±5.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 54.22（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 1003 / LOW 277 / INVALID 600
结构观察区: Primary Flip 54.22（全链重定价，覆盖 92%）
Put Wall 50（现价高于该位 20.0%） | Call Wall 70（现价低于该位 14.3%）
最近结构参考: Flip 54（现价高于该位 10.7%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall）；上方 70（Call Wall）。
• Gamma 区域：切换参考 54（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 62.0C — Vol 5,031 | 最新价 $1.99 | OI 2563→4701 (ΔOI +2138张) | ΔOI/Volume 42.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2138张（+83.4% vs前日OI），连续性待观察（方向未知）
09-18 63.0C — Vol 2,826 | 最新价 $2.65 | OI 64445→65758 (ΔOI +1313张) | ΔOI/Volume 46.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1313张（+2.0% vs前日OI），连续性待观察（方向未知）
08-28 60.0P — Vol 5,023 | 最新价 $0.04 | OI 3120→4433 (ΔOI +1313张) | ΔOI/Volume 26.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1313张（+42.1% vs前日OI），连续性待观察（方向未知）
08-28 58.0P — Vol 548 | 最新价 $0.01 | OI 1892→3071 (ΔOI +1179张) | ΔOI/Volume 215.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1179张（+62.3% vs前日OI），连续性待观察（方向未知）
08-28 62.5C — Vol 5,841 | 最新价 $0.80 | OI 777→1899 (ΔOI +1122张) | ΔOI/Volume 19.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1122张（+144.4% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-31  C +4.8k / P +1.3k ｜ Activity HIGH ｜ 3D
09-02  C +4.6k / P +3.0k ｜ Activity HIGH ｜ 5D
09-04  C +11.3k / P +3.0k ｜ Activity HIGH ｜ 7D
09-09  C +1.1k / P +0.4k ｜ Activity HIGH ｜ 12D

📆 08-31 Forward Structure
OI:       C 55.8k / P 9.9k
ΔOI:      C +4.8k / P +1.3k
ATM:      C 0.64 / P 0.61
ATM IV:   28.6%
ΔOI Δ Exposure*: -79k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 64 ｜ +1,522 ｜ $0.03 ｜ 名义 $4.6k* ｜ +6.6%
C 74 ｜ +931 ｜ $0.01 ｜ 名义 $931* ｜ +23.3%
P 62 ｜ +549 ｜ $2.01 ｜ 名义 $110.3k* ｜ +3.3%
结构参考：64（+6.6%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 14.8k / P 7.0k
ΔOI:      C +4.6k / P +3.0k
ATM:      C 1.03 / P 0.96
ATM IV:   33.9%
ΔOI Δ Exposure*: -129k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 60 ｜ +2,199 ｜ $0.96 ｜ 名义 $211.1k* ｜ -0.0%
C 69 ｜ +1,945 ｜ $0.03 ｜ 名义 $5.8k* ｜ +15.0%
C 67 ｜ +547 ｜ $0.05 ｜ 名义 $2.7k* ｜ +11.6%
结构参考：69（+15.0%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 70.7k / P 33.4k
ΔOI:      C +11.3k / P +3.0k
ATM:      C 1.36 / P 1.29
ATM IV:   39.3%
ΔOI Δ Exposure*: -175k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 69 ｜ +4,060 ｜ $0.05 ｜ 名义 $20.3k* ｜ +15.0%
C 67 ｜ +4,026 ｜ $0.11 ｜ 名义 $44.3k* ｜ +11.6%
P 63 ｜ +1,566 ｜ $3.82 ｜ 名义 $598.2k* ｜ +5.8%
结构参考：69（+15.0%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-09 Forward Structure
OI:       C 2.4k / P 1.1k
ΔOI:      C +1.1k / P +0.4k
ATM:      C 1.63 / P 1.65
ATM IV:   36.7%
ΔOI Δ Exposure*: 13k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 63 ｜ +262 ｜ $0.55 ｜ 名义 $14.4k* ｜ +5.8%
C 62 ｜ +146 ｜ $0.73 ｜ 名义 $10.7k* ｜ +4.1%
C 62 ｜ +138 ｜ $0.87 ｜ 名义 $12.0k* ｜ +3.3%
结构参考：63（+5.8%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/SLV_evening.json