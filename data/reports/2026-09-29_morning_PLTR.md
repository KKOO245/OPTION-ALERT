# 期权晨报 2026-09-29（快照 10:20 ET）

📊 市场环境

SPY $764.73 ｜ QQQ $737.93
VIX 15.96 ↓0.7%（5D +12.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 195C ΔOI +5,620（距现价 +4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 187.48 → 今开 187.34（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 188.63 ｜ 低 184.81

Options: P/C成交量 0.92 | OI比 0.62 | ATM IV 52.2% | Skew 1.9pp | Term 0.89 | ExpMove ±4.0%（近端） | Rank 56%
量化视角： IV 中性（Rank 56%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜保护溢价薄（Skew 1.9pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.92×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（3D）±4.0% ｜ 10-09（10D）±6.3% ｜ 10-16（17D）±8.0% ｜ 10-23（24D）±9.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 36,650,396 | GEX Change vs 上次快照 4,136,217 | Flip: Primary Flip: 179.04（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 606 / LOW 66 / INVALID 164
结构观察区: Primary Flip 179.04（全链重定价，覆盖 100%）
Put Wall 170（弱结构｜现价高于该位 9.6%） | Call Wall 200（现价低于该位 6.8%）
最近结构参考: Flip 179（现价高于该位 4.1%）
量化视角： 正 Gamma（3665万，无历史分位）｜正 Gamma 增强（+414万）｜现价位于 Flip 上方 4.09%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Put Wall，弱结构） / 182（MaxPain，仅结算参考）；上方 200（Call Wall）。
• Gamma 区域：切换参考 179（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 200.0C — Vol 19,056 | 最新价 $0.55 | OI 17051→25632 (ΔOI +8581张) | ΔOI/Volume 45.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8581张（+50.3% vs前日OI），连续性待观察（方向未知）
10-02 202.5C — Vol 10,830 | 最新价 $0.35 | OI 4234→11734 (ΔOI +7500张) | ΔOI/Volume 69.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7500张（+177.1% vs前日OI），连续性待观察（方向未知）
10-02 195.0C — Vol 14,285 | 最新价 $1.30 | OI 4978→10598 (ΔOI +5620张) | ΔOI/Volume 39.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5620张（+112.9% vs前日OI），连续性待观察（方向未知）
10-02 177.5P — Vol 8,902 | 最新价 $0.87 | OI 4556→8666 (ΔOI +4110张) | ΔOI/Volume 46.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4110张（+90.2% vs前日OI），连续性待观察（方向未知）
10-02 187.5C — Vol 4,853 | 最新价 $3.94 | OI 1280→3345 (ΔOI +2065张) | ΔOI/Volume 42.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2065张（+161.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 27,876 张（Put 4,110 / Call 23,766），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +28.2k / P +8.3k ｜ Activity HIGH ｜ 3D
10-09  C +3.8k / P +2.0k ｜ Activity HIGH ｜ 10D
10-16  C +3.9k / P +0.3k ｜ Activity MEDIUM △ ｜ 17D
10-23  C +0.6k / P +0.7k ｜ Activity MEDIUM △ ｜ 24D

📆 10-02 Forward Structure
存量OI: C 128.6k / P 79.3k，今日变化ΔOI: C +28.2k / P +8.3k，平值价格ATM: C $3.26 / P $4.25 ｜ ATM IV 52.2%，净 delta 敞口 269k shares
Top ΔOI: C 200 +8,581 ｜ C 202 +7,500 ｜ C 195 +5,620
仓位参考: Max Pain 182 ｜ Call Wall 200（+7.3%）（OI 25.6k） ｜ Put Wall 177.5（-4.8%）（OI 8.7k）
量化解读： 存量 Call 重｜ATM IV 52.2%｜历史 Rank 56%（近端代理）｜IV/RV 1.66×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 269,050 股

📆 10-09 Forward Structure
存量OI: C 28.7k / P 40.3k，今日变化ΔOI: C +3.8k / P +2.0k，平值价格ATM: C $5.45 / P $6.27 ｜ ATM IV 46.8%，净 delta 敞口 31k shares
Top ΔOI: P 185 +1,333 ｜ C 187 +1,173 ｜ C 200 +340
仓位参考: Max Pain 185 ｜ Call Wall 200（+7.3%，弱）（OI 3.7k） ｜ Put Wall 190（+2.0%，弱）（OI 4.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 46.8%｜历史 Rank 56%（近端代理）｜IV/RV 1.49×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 31,123 股

10-16（MEDIUM △）Top ΔOI: 205C +1,713 ｜ 200C +798
10-16（MEDIUM △）仓位参考: Max Pain 165 ｜ Call Wall 170（-8.8%，弱）（OI 14.7k） ｜ Put Wall 170（-8.8%，弱）（OI 14.8k）

10-23（MEDIUM △）Top ΔOI: 165P +334 ｜ 190C +232
10-23（MEDIUM △）仓位参考: Max Pain 180 ｜ Call Wall 180（-3.4%）（OI 4.6k） ｜ Put Wall 175（-6.1%）（OI 1.5k）

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 52.2% vs 10-09 46.8%（差 +5.4pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/PLTR_morning.json