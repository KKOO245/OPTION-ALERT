# 期权晨报 2026-09-17（快照 11:28 ET）

📊 市场环境

SPY $760.90 ｜ QQQ $715.82
VIX 15.87 ↓10.4%（5D -11.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 09-18（1D）ATM IV 99.9% vs 09-25 80.7%（差 +19.2pp），覆盖 新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 09-25 220P ΔOI +839（距现价 +4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 209.37 → 今开 230.02（+9.9%） | 较昨收变动（含盘初走势） ｜ 今日高 232.81 ｜ 低 209.65

Options: P/C成交量 0.40 | OI比 1.27 | ATM IV 99.9% | Skew -3.7pp | Term 0.81 | ExpMove ±4.5%（近端） | Rank 42%
量化视角： IV 中性（Rank 42%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.7pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.40×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.27×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（1D）±4.5% ｜ 09-25（8D）±9.6% ｜ 10-02（15D）±13.0% ｜ 10-09（22D）±15.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,677,100 | GEX Change vs 上次快照 4,897,404 | Flip: Primary Flip: 218.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 524 / LOW 72 / INVALID 176
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 218.80（全链重定价，覆盖 94%）
Put Wall 210（弱结构｜现价高于该位 0.4%）
最近结构参考: Put Wall 210（现价高于该位 0.4%）
量化视角： 负 Gamma（968万，无历史分位）｜负 Gamma 缓解（+490万）｜现价位于 Flip 下方 3.63%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 210（Put Wall，弱结构）；上方 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 219（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 240.0C — Vol 1,776 | 最新价 $8.89 | OI 2611→3569 (ΔOI +958张) | ΔOI/Volume 53.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增958张（+36.7% vs前日OI），连续性待观察（方向未知）
09-25 220.0P — Vol 987 | 最新价 $16.88 | OI 497→1336 (ΔOI +839张) | ΔOI/Volume 85.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增839张（+168.8% vs前日OI），连续性待观察（方向未知）
09-25 210.0P — Vol 1,266 | 最新价 $10.80 | OI 552→1363 (ΔOI +811张) | ΔOI/Volume 64.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增811张（+146.9% vs前日OI），连续性待观察（方向未知）
09-25 205.0P — Vol 1,053 | 最新价 $8.05 | OI 734→1511 (ΔOI +777张) | ΔOI/Volume 73.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增777张（+105.9% vs前日OI），连续性待观察（方向未知）
10-16 230.0C — Vol 1,901 | 最新价 $11.40 | OI 2241→2800 (ΔOI +559张) | ΔOI/Volume 29.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增559张（+24.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,944 张（Put 2,427 / Call 1,517），跨 2 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +2.1k / P -0.9k ｜ Activity MEDIUM △ ｜ 1D
09-25  C +1.8k / P +4.3k ｜ Activity HIGH ｜ 8D
10-02  C +0.9k / P +0.9k ｜ Activity HIGH ｜ 15D
10-09  C +0.8k / P +0.5k ｜ Activity HIGH ｜ 22D

📆 09-18 Forward Structure
存量OI: C 142.2k / P 181.2k，今日变化ΔOI: C +2.1k / P -0.9k，平值价格ATM: C $5.00 / P $4.58 ｜ ATM IV 99.9%，净 delta 敞口 93k shares
Top ΔOI: C 227 +389 ｜ C 225 +347
仓位参考: Max Pain 220 ｜ Call Wall 200（-5.2%，弱）（OI 7.0k） ｜ Put Wall 210（-0.4%，弱）（OI 10.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 99.9%｜历史 Rank 42%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 93,226 股

📆 09-25 Forward Structure
存量OI: C 25.2k / P 27.8k，今日变化ΔOI: C +1.8k / P +4.3k，平值价格ATM: C $10.50 / P $9.76 ｜ ATM IV 80.7%，净 delta 敞口 -138k shares
Top ΔOI: P 220 +839 ｜ P 210 +811 ｜ P 205 +777
仓位参考: Max Pain 215 ｜ Call Wall 227.5（+7.9%）（OI 3.0k） ｜ Put Wall 200（-5.2%，弱）（OI 2.3k）
量化解读： 存量两侧均衡｜ATM IV 80.7%｜历史 Rank 42%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 137,712 股

📆 10-02 Forward Structure
存量OI: C 9.8k / P 11.3k，今日变化ΔOI: C +0.9k / P +0.9k，平值价格ATM: C $14.65 / P $12.80 ｜ ATM IV 80.1%，净 delta 敞口 -4k shares
Top ΔOI: P 200 +132
仓位参考: Max Pain 218 ｜ Call Wall 215（+2.0%，弱）（OI 0.4k） ｜ Put Wall 200（-5.2%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 80.1%｜历史 Rank 42%（近端代理）｜净 delta 敞口 负 3,888 股

📆 10-09 Forward Structure
存量OI: C 6.9k / P 7.2k，今日变化ΔOI: C +0.8k / P +0.5k，平值价格ATM: C $17.55 / P $15.95 ｜ ATM IV 80.5%，净 delta 敞口 7k shares
Top ΔOI: C 270 +250 ｜ C 220 +221 ｜ C 225 +191
仓位参考: Max Pain 220 ｜ Call Wall 215（+2.0%，弱）（OI 0.4k） ｜ Put Wall 200（-5.2%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 80.5%｜历史 Rank 42%（近端代理）｜净 delta 敞口 正 7,176 股

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 99.9% vs 09-25 80.7%（差 +19.2pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/NBIS_morning.json