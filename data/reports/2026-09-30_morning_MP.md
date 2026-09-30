# 期权晨报 2026-09-30（快照 10:20 ET）

📊 市场环境

SPY $769.13 ｜ QQQ $743.60
VIX 15.68 ↓2.2%（5D +3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 10-02 ATM IV 65.9% vs 10-09 55.0%（差 +10.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-02 48C ΔOI +194（距现价 +0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 45.43 → 今开 45.95（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 48.56 ｜ 低 45.93

Options: P/C成交量 0.34 | OI比 0.74 | ATM IV 65.9% | Skew -1.6pp | Term 0.84 | ExpMove ±4.3%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（2D）±4.3% ｜ 10-09（9D）±9.4% ｜ 10-16（16D）±9.3% ｜ 10-23（23D）±10.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,721,326 | GEX Change vs 上次快照 3,401,166 | Flip: Primary Flip: 48.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 291 / LOW 61 / INVALID 94
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 48.56（全链重定价，覆盖 98%）
Put Wall 45（弱结构｜现价高于该位 5.7%） | Call Wall 50（弱结构｜现价低于该位 4.9%）
最近结构参考: Flip 49（现价低于该位 2.1%）
量化视角： 负 Gamma（172万，无历史分位）｜负 Gamma 缓解（+340万）｜现价位于 Flip 下方 2.06%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 45（Put Wall，弱结构）；上方 49（MaxPain，仅结算参考） / 50（Call Wall，弱结构）。
• Gamma 区域：切换参考 49（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 40.0P — Vol 494 | 最新价 $0.15 | OI 63→474 (ΔOI +411张) | ΔOI/Volume 83.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增411张（+652.4% vs前日OI），连续性待观察（方向未知）
10-09 50.0C — Vol 545 | 最新价 $0.38 | OI 344→705 (ΔOI +361张) | ΔOI/Volume 66.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增361张（+104.9% vs前日OI），连续性待观察（方向未知）
10-16 45.0P — Vol 1,017 | 最新价 $1.80 | OI 3309→3605 (ΔOI +296张) | ΔOI/Volume 29.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增296张（+8.9% vs前日OI），连续性待观察（方向未知）
10-02 44.5P — Vol 426 | 最新价 $0.54 | OI 120→356 (ΔOI +236张) | ΔOI/Volume 55.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增236张（+196.7% vs前日OI），连续性待观察（方向未知）
10-02 49.5C — Vol 240 | 最新价 $0.10 | OI 233→432 (ΔOI +199张) | ΔOI/Volume 82.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增199张（+85.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,503 张（Put 943 / Call 560），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +1.0k / P +0.1k ｜ Activity HIGH ｜ 2D
10-09  C +1.0k / P +1.0k ｜ Activity HIGH ｜ 9D
10-16  C +0.2k / P +1.0k ｜ Activity MEDIUM △ ｜ 16D
10-23  C +0.2k / P +0.2k ｜ Activity MEDIUM △ ｜ 23D

📆 10-02 Forward Structure
存量OI: C 12.6k / P 9.4k，今日变化ΔOI: C +1.0k / P +0.1k，平值价格ATM: C $1.00 / P $1.06 ｜ ATM IV 65.9%，净 delta 敞口 104k shares
Top ΔOI: P 44 +236 ｜ C 49 +199 ｜ C 48 +194
仓位参考: Max Pain 49 ｜ Call Wall 49（+3.0%，弱）（OI 1.2k） ｜ Put Wall 50（+5.1%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 65.9%｜历史 Rank 48%（近端代理）｜IV/RV 1.53×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 103,746 股

📆 10-09 Forward Structure
存量OI: C 5.7k / P 4.4k，今日变化ΔOI: C +1.0k / P +1.0k，平值价格ATM: C $1.50 / P $2.97 ｜ ATM IV 55.0%，净 delta 敞口 24k shares
Top ΔOI: C 50 +361 ｜ C 46 +135
仓位参考: Max Pain 50 ｜ Call Wall 50（+5.1%，弱）（OI 0.7k） ｜ Put Wall 47（-1.2%）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 55.0%｜历史 Rank 48%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 23,754 股

10-16（MEDIUM △）Top ΔOI: 45P +296
10-16（MEDIUM △）仓位参考: Max Pain 50 ｜ Call Wall 50（+5.1%，弱）（OI 3.2k） ｜ Put Wall 45（-5.4%，弱）（OI 3.6k）

10-23（MEDIUM △）Top ΔOI: 54P +62 ｜ 45C +36
10-23（MEDIUM △）仓位参考: Max Pain 52 ｜ Call Wall 50（+5.1%，弱）（OI 97） ｜ Put Wall 45（-5.4%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 65.9% vs 10-09 55.0%（差 +10.9pp）——覆盖 PCE 物价 Price Index MoM、Personal Spending MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/MP_morning.json