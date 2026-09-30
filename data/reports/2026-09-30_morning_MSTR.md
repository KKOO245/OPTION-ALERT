# 期权晨报 2026-09-30（快照 10:20 ET）

📊 市场环境

SPY $769.13 ｜ QQQ $743.57
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
🟡 **事件差分**: 10-02 ATM IV 80.7% vs 10-09 66.6%（差 +14.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-02 162P ΔOI -2,712（距现价 +3.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 154.67 → 今开 160.82（+4.0%） | 较昨收变动（含盘初走势） ｜ 今日高 163.53 ｜ 低 154.15

Options: P/C成交量 0.23 | OI比 0.81 | ATM IV 80.7% | Skew -7.0pp | Term 0.82 | ExpMove ±4.8%（近端） | Rank 51%
量化视角： IV 中性（Rank 51%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜Put 保护异常便宜（Skew -7.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.23×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（2D）±4.8% ｜ 10-09（9D）±8.3% ｜ 10-16（16D）±10.9% ｜ 10-23（23D）±13.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 54,308,355 | GEX Change vs 上次快照 20,147,803 | Flip: Primary Flip: 147.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 776 / LOW 72 / INVALID 194
结构观察区: Primary Flip 147.31（全链重定价，覆盖 100%）
Call Wall 170（弱结构｜现价低于该位 7.8%）
最近结构参考: Flip 147（现价高于该位 6.4%）
量化视角： 正 Gamma（5431万，无历史分位）｜正 Gamma 增强（+2015万）｜现价位于 Flip 上方 6.42%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 155（MaxPain，仅结算参考）；上方 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 147（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 165.0C — Vol 5,619 | 最新价 $6.50 | OI 1041→5144 (ΔOI +4103张) | ΔOI/Volume 73.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4103张（+394.1% vs前日OI），连续性待观察（方向未知）
10-02 167.5C — Vol 6,803 | 最新价 $0.95 | OI 15748→18553 (ΔOI +2805张) | ΔOI/Volume 41.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2805张（+17.8% vs前日OI），连续性待观察（方向未知）
10-09 118.0P — Vol 2,166 | 最新价 $0.20 | OI 79→2167 (ΔOI +2088张) | ΔOI/Volume 96.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2088张（+2643.0% vs前日OI），连续性待观察（方向未知）
10-02 160.0P — Vol 5,502 | 最新价 $7.80 | OI 3905→5506 (ΔOI +1601张) | ΔOI/Volume 29.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1601张（+41.0% vs前日OI），连续性待观察（方向未知）
10-02 175.0C — Vol 7,076 | 最新价 $0.40 | OI 13735→15150 (ΔOI +1415张) | ΔOI/Volume 20.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1415张（+10.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,012 张（Put 3,689 / Call 8,323），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +1.2k / P -1.1k ｜ Activity MEDIUM △ ｜ 2D
10-09  C +4.8k / P +4.6k ｜ Activity HIGH ｜ 9D
10-16  C -17 / P +1.7k ｜ Activity HIGH ｜ 16D
10-23  C +6.8k / P +1.9k ｜ Activity HIGH ｜ 23D

📆 10-02 Forward Structure
存量OI: C 240.6k / P 194.3k，今日变化ΔOI: C +1.2k / P -1.1k，平值价格ATM: C $3.60 / P $4.00 ｜ ATM IV 80.7%，净 delta 敞口 260k shares
Top ΔOI: C 170 -3,839 ｜ C 167 +2,805 ｜ P 162 -2,712
仓位参考: Max Pain 155 ｜ Call Wall 170（+8.4%，弱）（OI 41.0k） ｜ Put Wall 150（-4.3%，弱）（OI 10.8k）
量化解读： 存量 Call 重｜ATM IV 80.7%｜历史 Rank 51%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 259,993 股

📆 10-09 Forward Structure
存量OI: C 43.1k / P 58.7k，今日变化ΔOI: C +4.8k / P +4.6k，平值价格ATM: C $6.32 / P $6.70 ｜ ATM IV 66.6%，净 delta 敞口 15k shares
Top ΔOI: C 182 +747 ｜ C 160 +746
仓位参考: Max Pain 150 ｜ Call Wall 165（+5.2%，弱）（OI 5.2k） ｜ Put Wall 155（-1.1%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 66.6%｜历史 Rank 51%（近端代理）｜IV/RV 0.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 14,804 股

📆 10-16 Forward Structure
存量OI: C 172.8k / P 144.3k，今日变化ΔOI: C -17 / P +1.7k，平值价格ATM: C $7.80 / P $9.30 ｜ ATM IV 66.0%，净 delta 敞口 7k shares
Top ΔOI: C 190 -1,133 ｜ C 175 -488 ｜ C 170 +431
仓位参考: Max Pain 120 ｜ Call Wall 155（-1.1%，弱）（OI 10.4k） ｜ Put Wall 160（+2.1%，弱）（OI 4.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 66.0%｜历史 Rank 51%（近端代理）｜IV/RV 0.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 7,345 股

📆 10-23 Forward Structure
存量OI: C 22.6k / P 25.1k，今日变化ΔOI: C +6.8k / P +1.9k，平值价格ATM: C $9.70 / P $11.00 ｜ ATM IV 65.3%，净 delta 敞口 225k shares
Top ΔOI: C 165 +4,103 ｜ C 162 +1,124 ｜ C 167 +501
仓位参考: Max Pain 160 ｜ Call Wall 165（+5.2%）（OI 5.1k） ｜ Put Wall 155（-1.1%，弱）（OI 2.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 65.3%｜历史 Rank 51%（近端代理）｜IV/RV 0.85×（近似）｜净 delta 敞口 正 225,319 股

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 80.7% vs 10-09 66.6%（差 +14.1pp）——覆盖 PCE 物价 Price Index MoM、Personal Spending MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/MSTR_morning.json