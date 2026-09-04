# 期权晨报 2026-09-04（快照 10:20 ET）

📊 市场环境

SPY $772.01 ｜ QQQ $719.74
VIX 14.05 ↓1.9%（5D -2.6%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 43.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-11 54P ΔOI +145（距现价 -1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 53.78 → 今开 56.57（+5.2%） | 较昨收变动（含盘初走势） ｜ 今日高 58.52 ｜ 低 54.54

Options: P/C成交量 0.41 | OI比 0.74 | ATM IV 70.4% | Skew -2.2pp | Term 0.96 | ExpMove ±7.2%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构正常（Term 0.96）｜Put 保护异常便宜（Skew -2.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.41×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（7D）±7.2% ｜ 09-18（14D）±9.8% ｜ 09-25（21D）±12.3% ｜ 10-02（28D）±14.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 754,951 | GEX Change vs 上次快照 3,348,479 | Flip: Primary Flip: 54.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 301 / LOW 88 / INVALID 105
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 54.53（全链重定价，覆盖 98%）
Put Wall 55（弱结构｜现价低于该位 0.3%） | Call Wall 60（弱结构｜现价低于该位 8.6%）
最近结构参考: Put Wall 55（现价低于该位 0.3%）
量化视角： 正 Gamma（75万，无历史分位）｜由负转正（+335万）｜现价位于 Flip 上方 0.54%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 55（Put Wall，弱结构）；上方 54（MaxPain，仅结算参考） / 60（Call Wall，弱结构）。
• Gamma 区域：切换参考 55（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 65.0C — Vol 1,057 | 最新价 $0.08 | OI 452→1483 (ΔOI +1031张) | ΔOI/Volume 97.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1031张（+228.1% vs前日OI），连续性待观察（方向未知）
09-18 55.0C — Vol 388 | 最新价 $1.97 | OI 3214→3455 (ΔOI +241张) | ΔOI/Volume 62.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增241张（+7.5% vs前日OI），连续性待观察（方向未知）
09-04 55.0C — Vol 618 | 最新价 $0.35 | OI 1038→1276 (ΔOI +238张) | ΔOI/Volume 38.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增238张（+22.9% vs前日OI），连续性待观察（方向未知）
09-18 60.0C — Vol 401 | 最新价 $0.79 | OI 6140→6366 (ΔOI +226张) | ΔOI/Volume 56.4% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增226张（+3.7% vs前日OI），值得跟踪（方向未知）
09-04 54.0C — Vol 650 | 最新价 $0.70 | OI 290→497 (ΔOI +207张) | ΔOI/Volume 31.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增207张（+71.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,943 张（Put 0 / Call 1,943），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +1.8k / P +0.6k ｜ Activity HIGH ｜ 7D
09-18  C +0.5k / P -75 ｜ Activity HIGH ｜ 14D
09-25  C +15 / P +73 ｜ Activity MEDIUM △ ｜ 21D
10-02  C +0.1k / P +0.3k ｜ Activity HIGH ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 6.2k / P 4.5k
今日变化ΔOI: C +1.8k / P +0.6k
平值价格ATM:  C 1.38 / P 2.55
隐含波动率 ATM IV:  58.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 14k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 54 ｜ +145 ｜ $2.25 ｜ 名义 $32.6k* ｜ -1.5%
P 52 ｜ +137 ｜ $1.05 ｜ 名义 $14.4k* ｜ -5.1%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：54（-1.5%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 58.3%｜历史 Rank 54%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 14,131 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 47.8k / P 44.2k
今日变化ΔOI: C +0.5k / P -75
平值价格ATM:  C 1.97 / P 3.40
隐含波动率 ATM IV:  59.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 36k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 55 ｜ +241 ｜ $1.97 ｜ 名义 $47.5k* ｜ +0.3%
C 60 ｜ +226 ｜ $0.79 ｜ 名义 $17.9k* ｜ +9.5%
P 80 ｜ -101 ｜ $25.29 ｜ 名义 $-255.4k* ｜ +45.9%
结构参考：55（+0.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜ATM IV 59.0%｜历史 Rank 54%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 35,781 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 1.9k / P 2.7k
今日变化ΔOI: C +0.1k / P +0.3k
平值价格ATM:  C 3.45 / P 4.45
隐含波动率 ATM IV:  67.3%
净 delta 敞口变化 ΔOI Δ Exposure*: -3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 53 ｜ +121 ｜ $3.35 ｜ 名义 $40.5k* ｜ -3.3%
C 59 ｜ +23 ｜ $2.00 ｜ 名义 $4.6k* ｜ +7.6%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：59（+7.6%） / 53（-3.3%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 67.3%｜历史 Rank 54%（近端代理）｜净 delta 敞口 负 3,367 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/MP_morning.json