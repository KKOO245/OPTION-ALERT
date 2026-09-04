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
🟡 **近现价集中开仓**: 09-11 160P ΔOI +331（距现价 -2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 162.74 → 收盘 163.81（+0.7%） ｜ 今日高 164.35 ｜ 低 162.51
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 2.94 | OI比 1.60 | ATM IV 33.1% | Skew -2.4pp | Term 0.98 | ExpMove ±3.3%（近端） | Rank 51%
量化视角： IV 中性（Rank 51%）｜期限结构正常（Term 0.98）｜Put 保护异常便宜（Skew -2.4pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 2.94）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.94×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.60×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-11（7D）±3.3% ｜ 09-18（14D）±4.7% ｜ 09-25（21D）±8.0% ｜ 10-02（28D）±7.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -18,583,351 | GEX Change vs 上次快照 1,574,499 | Flip: Primary Flip: 166.84（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 323 / LOW 165 / INVALID 392
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 166.84（全链重定价，覆盖 92%）
Put Wall 158（弱结构｜现价高于该位 3.7%） | Call Wall 170（弱结构｜现价低于该位 3.6%）
最近结构参考: Flip 167（现价低于该位 1.8%）
量化视角： 负 Gamma（1858万，无历史分位）｜负 Gamma 缓解（+157万）｜现价位于 Flip 下方 1.81%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 158（Put Wall，弱结构）；上方 164（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 167（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 162.5P — Vol 2,004 | 最新价 $0.74 | OI 23→1004 (ΔOI +981张) | ΔOI/Volume 49.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增981张（+4265.2% vs前日OI），连续性待观察（方向未知）
09-04 168.0C — Vol 772 | 最新价 $0.17 | OI 1115→1548 (ΔOI +433张) | ΔOI/Volume 56.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增433张（+38.8% vs前日OI），连续性待观察（方向未知）
09-11 160.0P — Vol 363 | 最新价 $1.20 | OI 108→439 (ΔOI +331张) | ΔOI/Volume 91.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增331张（+306.5% vs前日OI），连续性待观察（方向未知）
09-04 170.0C — Vol 602 | 最新价 $0.03 | OI 742→986 (ΔOI +244张) | ΔOI/Volume 40.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增244张（+32.9% vs前日OI），连续性待观察（方向未知）
09-18 165.0P — Vol 187 | 最新价 $4.45 | OI 52→229 (ΔOI +177张) | ΔOI/Volume 94.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增177张（+340.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,166 张（Put 1,489 / Call 677），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +60 / P +0.8k ｜ Activity HIGH ｜ 7D
09-18  C +0.1k / P -51 ｜ Activity MEDIUM △ ｜ 14D
09-25  C +32 / P +2 ｜ Activity MEDIUM △ ｜ 21D
10-02  C +43 / P +52 ｜ Activity HIGH ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 2.2k / P 9.0k
今日变化ΔOI: C +60 / P +0.8k
平值价格ATM:  C 2.67 / P 2.77
隐含波动率 ATM IV:  28.2%
净 delta 敞口变化 ΔOI Δ Exposure*: -17k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 160 ｜ +331 ｜ $1.20 ｜ 名义 $39.7k* ｜ -2.3%
P 157 ｜ +167 ｜ $0.42 ｜ 名义 $7.0k* ｜ -4.2%
P 155 ｜ +161 ｜ $0.32 ｜ 名义 $5.2k* ｜ -5.4%
结构参考：160（-2.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 28.2%｜历史 Rank 51%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 16,616 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 160P -354 ｜ 165P +177

09-25（MEDIUM △）Top ΔOI: 171C +20 ｜ 153P +9

📆 10-02 Forward Structure
存量OI:      C 0.7k / P 0.8k
今日变化ΔOI: C +43 / P +52
平值价格ATM:  C 6.90 / P 5.40
隐含波动率 ATM IV:  32.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 578 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 174 ｜ +45 ｜ $2.01 ｜ 名义 $9.0k* ｜ +6.2%
P 150 ｜ +21 ｜ $1.22 ｜ 名义 $2.6k* ｜ -8.4%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：174（+6.2%） / 150（-8.4%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜ATM IV 32.5%｜历史 Rank 51%（近端代理）｜净 delta 敞口 正 578 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/XBI_evening.json