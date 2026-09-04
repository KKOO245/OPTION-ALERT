# 期权晚报 2026-09-04（快照 16:40 ET）

📊 市场环境

SPY $770.19 ｜ QQQ $718.96
VIX 14.53 ↑1.5%（5D +0.7%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 509.40 → 收盘 519.86（+2.1%） ｜ 今日高 520.55 ｜ 低 507.25
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.60 | OI比 0.79 | ATM IV 41.1% | Skew -4.1pp | Term 0.90 | ExpMove ±3.5%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构正常（Term 0.90）｜Put 保护异常便宜（Skew -4.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（7D）±3.5% ｜ 09-18（14D）±5.5% ｜ 09-25（21D）±6.9% ｜ 10-02（28D）±8.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 1,431,017 | GEX Change vs 上次快照 175,721 | Flip: Primary Flip: 518.64（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 497 / LOW 304 / INVALID 761
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 518.64（全链重定价，覆盖 92%）
最近结构参考: Flip 519（现价高于该位 0.2%）
量化视角： 正 Gamma（143万，无历史分位）｜正 Gamma 增强（+18万）｜现价位于 Flip 上方 0.24%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 519（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 550.0C — Vol 306 | 最新价 $3.91 | OI 366→1661 (ΔOI +1295张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1295张（+353.8% vs前日OI），连续性待观察（方向未知）
09-04 520.0C — Vol 2,394 | 最新价 $0.09 | OI 570→1068 (ΔOI +498张) | ΔOI/Volume 20.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增498张（+87.4% vs前日OI），连续性待观察（方向未知）
09-04 500.0C — Vol 131 | 最新价 $16.51 | OI 286→664 (ΔOI +378张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增378张（+132.2% vs前日OI），值得跟踪（方向未知）
09-04 515.0C — Vol 822 | 最新价 $1.40 | OI 860→1186 (ΔOI +326张) | ΔOI/Volume 39.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增326张（+37.9% vs前日OI），连续性待观察（方向未知）
09-18 500.0C — Vol 179 | 最新价 $24.90 | OI 895→1137 (ΔOI +242张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增242张（+27.0% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,739 张（Put 0 / Call 2,739），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0.3k / P -1.5k ｜ Activity HIGH ｜ 7D
09-18  C +1.2k / P -1.2k ｜ Activity HIGH ｜ 14D
09-25  C -9 / P +34 ｜ Activity LOW ｜ 21D
10-02  C +97 / P +0.3k ｜ Activity HIGH ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 12.4k / P 14.2k
今日变化ΔOI: C +0.3k / P -1.5k
平值价格ATM:  C 7.65 / P 10.50
隐含波动率 ATM IV:  31.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 114k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 550 ｜ -785 ｜ $33.68 ｜ 名义 $-2.64M* ｜ +5.8%
P 485 ｜ -457 ｜ $1.16 ｜ 名义 $-53.0k* ｜ -6.7%
P 500 ｜ -341 ｜ $3.30 ｜ 名义 $-112.5k* ｜ -3.8%
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 31.4%｜历史 Rank 74%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 113,563 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 81.0k / P 89.7k
今日变化ΔOI: C +1.2k / P -1.2k
平值价格ATM:  C 13.09 / P 15.60
隐含波动率 ATM IV:  35.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 83k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 550 ｜ +1,295 ｜ $3.91 ｜ 名义 $506.3k* ｜ +5.8%
P 485 ｜ -571 ｜ $4.20 ｜ 名义 $-239.8k* ｜ -6.7%
P 450 ｜ -501 ｜ $1.00 ｜ 名义 $-50.1k* ｜ -13.4%
结构参考：550（+5.8%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 35.0%｜历史 Rank 74%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 83,330 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 5.4k / P 6.6k
今日变化ΔOI: C +97 / P +0.3k
平值价格ATM:  C 19.90 / P 21.94
隐含波动率 ATM IV:  37.2%
净 delta 敞口变化 ΔOI Δ Exposure*: -6k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 495 ｜ +80 ｜ $11.40 ｜ 名义 $91.2k* ｜ -4.8%
P 500 ｜ +61 ｜ $13.40 ｜ 名义 $81.7k* ｜ -3.8%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：495（-4.8%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 37.2%｜历史 Rank 74%（近端代理）｜净 delta 敞口 负 6,398 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/SOXX_evening.json