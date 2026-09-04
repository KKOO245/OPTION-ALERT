# 期权晨报 2026-09-04（快照 10:52 ET）

📊 市场环境

SPY $771.00 ｜ QQQ $717.79
VIX 14.12 ↓1.4%（5D -2.1%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **单日价格波动**: -3.9%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-11 190C ΔOI -1,548（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 192.70 → 今开 185.30（-3.8%） | 较昨收变动（含盘初走势） ｜ 今日高 189.00 ｜ 低 182.89

Options: P/C成交量 0.57 | OI比 0.59 | ATM IV 78.3% | Skew -5.3pp | Term 0.82 | ExpMove ±6.6%（近端） | Rank 55%
量化视角： IV 中性（Rank 55%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（7D）±6.6% ｜ 09-18（14D）±10.1% ｜ 09-25（21D）±12.0% ｜ 10-02（28D）±14.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 33,748,308 | GEX Change vs 上次快照 -11,873,777 | Flip: Primary Flip: 165.46（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 559 / LOW 194 / INVALID 307
结构观察区: Primary Flip 165.46（全链重定价，覆盖 97%）
Call Wall 200（弱结构｜现价低于该位 7.4%）
最近结构参考: Call Wall 200（现价低于该位 7.4%）
量化视角： 正 Gamma（3375万，无历史分位）｜正 Gamma 减弱（1187万）｜现价位于 Flip 上方 11.91%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 165（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 205.0C — Vol 152 | 最新价 $1.52 | OI 1006→5300 (ΔOI +4294张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4294张（+426.8% vs前日OI），连续性待观察（方向未知）
09-11 197.5C — Vol 44 | 最新价 $2.77 | OI 158→3628 (ΔOI +3470张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3470张（+2196.2% vs前日OI），连续性待观察（方向未知）
09-04 197.5C — Vol 3,171 | 最新价 $0.06 | OI 817→3299 (ΔOI +2482张) | ΔOI/Volume 78.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2482张（+303.8% vs前日OI），连续性待观察（方向未知）
09-18 320.0C — Vol 2,009（Yahoo补） | 最新价 $0.14 | OI 972→2707 (ΔOI +1735张) | ΔOI/Volume 86.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1735张（+178.5% vs前日OI），连续性待观察（方向未知）
09-04 190.0P — Vol 1,063 | 最新价 $4.45 | OI 1171→2711 (ΔOI +1540张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1540张（+131.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 13,521 张（Put 1,540 / Call 11,981），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +12.4k / P +5.0k ｜ Activity HIGH ｜ 7D
09-18  C +2.7k / P +0.9k ｜ Activity HIGH ｜ 14D
09-25  C +0.5k / P +0.2k ｜ Activity HIGH ｜ 21D
10-02  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 42.9k / P 20.1k
今日变化ΔOI: C +12.4k / P +5.0k
平值价格ATM:  C 6.35 / P 5.95
隐含波动率 ATM IV:  58.8%
净 delta 敞口变化 ΔOI Δ Exposure*: -17k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 205 ｜ +4,294 ｜ $1.30 ｜ 名义 $558.2k* ｜ +10.7%
C 197 ｜ +3,470 ｜ $2.41 ｜ 名义 $836.3k* ｜ +6.7%
C 190 ｜ -1,548 ｜ $4.22 ｜ 名义 $-653.3k* ｜ +2.6%
结构参考：205（+10.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 58.8%｜历史 Rank 55%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 17,169 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 175.5k / P 86.9k
今日变化ΔOI: C +2.7k / P +0.9k
平值价格ATM:  C 9.37 / P 9.40
隐含波动率 ATM IV:  62.2%
净 delta 敞口变化 ΔOI Δ Exposure*: -48k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 62.2%｜历史 Rank 55%（近端代理）｜净 delta 敞口 负 48,022 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 8.6k / P 7.4k
今日变化ΔOI: C +0.5k / P +0.2k
平值价格ATM:  C 11.30 / P 11.00
隐含波动率 ATM IV:  62.7%
净 delta 敞口变化 ΔOI Δ Exposure*: -3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 192 ｜ +91 ｜ $15.70 ｜ 名义 $142.9k* ｜ +4.0%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：192（+4.0%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜ATM IV 62.7%｜历史 Rank 55%（近端代理）｜净 delta 敞口 负 3,116 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/COIN_morning.json