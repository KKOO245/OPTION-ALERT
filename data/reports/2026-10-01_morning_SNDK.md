# 期权晨报 2026-10-01（快照 10:20 ET）

📊 市场环境

SPY $760.23 ｜ QQQ $737.52
VIX 17.57 ↑7.5%（5D +12.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-01

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 54.5 ｜ 前值 54.6　✅ 今日已公布
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 10-02（1D）ATM IV 83.1% vs 10-09 64.8%（差 +18.3pp），覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-02 1740C ΔOI +1,349（距现价 +0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,739.89 → 今开 1,736.19（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 1764.77 ｜ 低 1721.00

Options: P/C成交量 0.38 | OI比 0.80 | ATM IV 83.1% | Skew -5.5pp | Term 0.88 | ExpMove ±3.9%（近端） | Rank 39%
量化视角： IV 中性（Rank 39%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（1D）±3.9% ｜ 10-09（8D）±7.7% ｜ 10-16（15D）±11.3% ｜ 10-23（22D）±15.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,493,793 | GEX Change vs 上次快照 1,144,287 | Flip: Primary Flip: 1704.71（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1794 / LOW 507 / INVALID 977
结构观察区: Primary Flip 1704.71（全链重定价，覆盖 100%）
最近结构参考: Flip 1705（现价高于该位 1.8%）
量化视角： 正 Gamma（449万，无历史分位）｜正 Gamma 增强（+114万）｜现价位于 Flip 上方 1.77%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,700（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1705（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 1740.0C — Vol 3,958 | 最新价 $47.10 | OI 248→1597 (ΔOI +1349张) | ΔOI/Volume 34.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1349张（+544.0% vs前日OI），连续性待观察（方向未知）
10-02 2000.0C — Vol 5,299 | 最新价 $2.65 | OI 7002→8017 (ΔOI +1015张) | ΔOI/Volume 19.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1015张（+14.5% vs前日OI），连续性待观察（方向未知）
10-02 1900.0C — Vol 5,013 | 最新价 $7.40 | OI 2566→3406 (ΔOI +840张) | ΔOI/Volume 16.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增840张（+32.7% vs前日OI），连续性待观察（方向未知）
10-09 1370.0P — Vol 473 | 最新价 $1.85 | OI 60→525 (ΔOI +465张) | ΔOI/Volume 98.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增465张（+775.0% vs前日OI），连续性待观察（方向未知）
10-02 1950.0C — Vol 1,367 | 最新价 $4.30 | OI 1344→1807 (ΔOI +463张) | ΔOI/Volume 33.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增463张（+34.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,132 张（Put 465 / Call 3,667），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +7.0k / P +1.6k ｜ Activity HIGH ｜ 1D
10-09  C +1.8k / P +2.9k ｜ Activity HIGH ｜ 8D
10-16  C +0.5k / P +0.5k ｜ Activity HIGH ｜ 15D
10-23  C +0.4k / P +0.5k ｜ Activity MEDIUM △ ｜ 22D

📆 10-02 Forward Structure
存量OI: C 51.8k / P 41.7k，今日变化ΔOI: C +7.0k / P +1.6k，平值价格ATM: C $38.05 / P $29.40 ｜ ATM IV 83.1%，净 delta 敞口 109k shares
Top ΔOI: C 1740 +1,349 ｜ C 1900 +840
仓位参考: Max Pain 1,700 ｜ Call Wall 1900（+9.5%，弱）（OI 3.4k） ｜ Put Wall 1600（-7.8%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 83.1%｜历史 Rank 39%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 109,469 股

📆 10-09 Forward Structure
存量OI: C 14.4k / P 14.5k，今日变化ΔOI: C +1.8k / P +2.9k，平值价格ATM: C $78.83 / P $54.70 ｜ ATM IV 64.8%，净 delta 敞口 9k shares
Top ΔOI: P 1370 +465
仓位参考: Max Pain 1,655 ｜ Call Wall 1900（+9.5%，弱）（OI 0.5k） ｜ Put Wall 1800（+3.8%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 64.8%｜历史 Rank 39%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 正 9,496 股

📆 10-16 Forward Structure
存量OI: C 38.6k / P 48.9k，今日变化ΔOI: C +0.5k / P +0.5k，平值价格ATM: C $110.10 / P $86.50 ｜ ATM IV 65.3%，净 delta 敞口 -9k shares
Top ΔOI: P 1780 +238 ｜ P 1600 -216
仓位参考: Max Pain 1,660 ｜ Call Wall 1900（+9.5%，弱）（OI 1.2k） ｜ Put Wall 1600（-7.8%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 65.3%｜历史 Rank 39%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 负 8,811 股

10-23（MEDIUM △）Top ΔOI: 1650P +101 ｜ 1645P +76
10-23（MEDIUM △）仓位参考: Max Pain 1,745 ｜ Call Wall 1840（+6.1%，弱）（OI 0.2k） ｜ Put Wall 1650（-4.9%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 83.1% vs 10-09 64.8%（差 +18.3pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/SNDK_morning.json