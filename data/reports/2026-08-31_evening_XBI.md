# 期权晚报 2026-08-31

📊 市场环境

SPY $767.05 ｜ QQQ $716.76
VIX 14.92 ↑3.4%（5D -5.9%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 49.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-01 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.3 ｜ 实际 待公布 ｜ 前值 7.359
- 周二 09-01 10:00　【高】ISM 制造业 PMI　预测 55.2 ｜ 实际 待公布 ｜ 前值 55.6
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-04 161P ΔOI +1,735（距现价 -0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-04 161P ΔOI +1,735 占该期限总 OI 12.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 161.00 → 收盘 162.50（+0.9%） ｜ 今日高 163.22 ｜ 低 159.62
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 2.32 | OI比 2.10 | ATM IV 33.1% | Skew 5.0pp | Term 0.96 | ExpMove ±2.5%（近端） | Rank 50%
   ⇒ Put/Call Volume: 2.32×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.10×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-04（4D）±2.5% ｜ 09-11（11D）±4.0% ｜ 09-18（18D）±6.7% ｜ 09-25（25D）±5.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,505,257 | GEX Change vs 上次快照 3,093,503 | Flip: Primary Flip: 166.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 350 / LOW 95 / INVALID 427
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 166.02（全链重定价，覆盖 99%）
Put Wall 155（弱结构｜现价高于该位 4.8%） | Call Wall 155（弱结构｜现价高于该位 4.8%）
最近结构参考: Flip 166（现价低于该位 2.1%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 155（Put Wall，弱结构）；上方 155（Call Wall，弱结构）。
• Gamma 区域：切换参考 166（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 159.0P — Vol 17 | 最新价 $2.57 | OI 10→2504 (ΔOI +2494张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2494张（+24940.0% vs前日OI），连续性待观察（方向未知）
09-04 161.0P — Vol 8 | 最新价 $2.15 | OI 92→1827 (ΔOI +1735张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1735张（+1885.9% vs前日OI），连续性待观察（方向未知）
09-11 152.0P — Vol 1（Yahoo补） | 最新价 $0.42 | OI 20→1514 (ΔOI +1494张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1494张（+7470.0% vs前日OI），连续性待观察（方向未知）
09-04 163.0P — Vol 253 | 最新价 $3.70 | OI 31→1513 (ΔOI +1482张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1482张（+4780.6% vs前日OI），连续性待观察（方向未知）
09-04 158.0P — Vol 459 | 最新价 $1.20 | OI 198→1292 (ΔOI +1094张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1094张（+552.5% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +2.0k / P +5.2k ｜ Activity HIGH ｜ 4D
09-11  C +66 / P +5.1k ｜ Activity HIGH ｜ 11D
09-18  C +74 / P -1.9k ｜ Activity HIGH ｜ 18D
09-25  C +34 / P +0.1k ｜ Activity MEDIUM △ ｜ 25D

📆 09-04 Forward Structure
OI:       C 4.6k / P 9.6k
ΔOI:      C +2.0k / P +5.2k
ATM:      C 1.60 / P 2.50
ATM IV:   33.1%
ΔOI Δ Exposure*: -194k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 161 ｜ +1,735 ｜ $2.15 ｜ 名义 $373.0k* ｜ -0.9%
P 163 ｜ +1,482 ｜ $3.70 ｜ 名义 $548.3k* ｜ +0.3%
P 158 ｜ +1,094 ｜ $1.20 ｜ 名义 $131.3k* ｜ -2.8%
结构参考：163（+0.3%）上方 / 161（-0.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 1.2k / P 6.6k
ΔOI:      C +66 / P +5.1k
ATM:      C 2.73 / P 3.69
ATM IV:   31.2%
ΔOI Δ Exposure*: -137k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 159 ｜ +2,494 ｜ $2.57 ｜ 名义 $641.0k* ｜ -2.2%
P 152 ｜ +1,494 ｜ $0.42 ｜ 名义 $62.7k* ｜ -6.5%
P 153 ｜ +997 ｜ $0.64 ｜ 名义 $63.8k* ｜ -5.8%
结构参考：159（-2.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 71.5k / P 99.1k
ΔOI:      C +74 / P -1.9k
ATM:      C 6.70 / P 4.23
ATM IV:   30.5%
ΔOI Δ Exposure*: 107k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 163 ｜ -1,526 ｜ $5.52 ｜ 名义 $-842.4k* ｜ +0.3%
P 155 ｜ +1,072 ｜ $2.03 ｜ 名义 $217.6k* ｜ -4.6%
P 153 ｜ -899 ｜ $1.56 ｜ 名义 $-140.2k* ｜ -5.8%
结构参考：155（-4.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 185C +27 ｜ 145P +26

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/XBI_evening.json