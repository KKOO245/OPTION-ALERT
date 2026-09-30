# 期权晨报 2026-09-30（快照 10:20 ET）

📊 市场环境

SPY $763.55 ｜ QQQ $739.77
VIX 15.68 ↓2.2%（5D +3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 157C ΔOI +5,547（距现价 +4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 149.24 → 今开 148.63（-0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 152.08 ｜ 低 147.75

Options: P/C成交量 0.37 | OI比 1.00 | ATM IV 51.2% | Skew 1.1pp | Term 0.87 | ExpMove ±3.2%（近端） | Rank 24%
量化视角： IV 历史低位（Rank 24%，期权偏便宜）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价薄（Skew 1.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.00×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（2D）±3.2% ｜ 10-09（9D）±5.7% ｜ 10-16（16D）±7.5% ｜ 10-23（23D）±8.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 50,503,059 | GEX Change vs 上次快照 23,320,126 | Flip: Primary Flip: 147.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 522 / LOW 83 / INVALID 317
结构观察区: Primary Flip 147.35（全链重定价，覆盖 100%）
Call Wall 160（弱结构｜现价低于该位 6.2%）
最近结构参考: Flip 147（现价高于该位 1.9%）
量化视角： 正 Gamma（5050万，无历史分位）｜正 Gamma 增强（+2332万）｜现价位于 Flip 上方 1.90%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 149（MaxPain，仅结算参考）；上方 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 147（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 162.5C — Vol 12,340 | 最新价 $1.69 | OI 676→10778 (ΔOI +10102张) | ΔOI/Volume 81.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10102张（+1494.4% vs前日OI），连续性待观察（方向未知）
10-16 160.0C — Vol 15,688 | 最新价 $2.18 | OI 35237→42179 (ΔOI +6942张) | ΔOI/Volume 44.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6942张（+19.7% vs前日OI），连续性待观察（方向未知）
10-02 157.5C — Vol 15,293 | 最新价 $0.48 | OI 9206→14753 (ΔOI +5547张) | ΔOI/Volume 36.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5547张（+60.2% vs前日OI），连续性待观察（方向未知）
10-02 152.5C — Vol 29,537 | 最新价 $1.47 | OI 10655→13776 (ΔOI +3121张) | ΔOI/Volume 10.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3121张（+29.3% vs前日OI），连续性待观察（方向未知）
10-02 160.0C — Vol 19,600 | 最新价 $0.27 | OI 21773→24891 (ΔOI +3118张) | ΔOI/Volume 15.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3118张（+14.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 28,830 张（Put 0 / Call 28,830），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +18.2k / P +11.0k ｜ Activity HIGH ｜ 2D
10-09  C +11.9k / P +7.3k ｜ Activity MEDIUM △ ｜ 9D
10-16  C +8.9k / P -0.5k ｜ Activity HIGH ｜ 16D
10-23  C +2.1k / P +2.4k ｜ Activity MEDIUM △ ｜ 23D

📆 10-02 Forward Structure
存量OI: C 199.1k / P 199.5k，今日变化ΔOI: C +18.2k / P +11.0k，平值价格ATM: C $2.66 / P $2.20 ｜ ATM IV 51.2%，净 delta 敞口 249k shares
Top ΔOI: C 157 +5,547 ｜ C 152 +3,121 ｜ C 160 +3,118
仓位参考: Max Pain 149 ｜ Call Wall 160（+6.6%，弱）（OI 24.9k） ｜ Put Wall 140（-6.8%，弱）（OI 19.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 51.2%｜历史 Rank 24%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 249,066 股

10-09（MEDIUM △）Top ΔOI: 170C +2,814 ｜ 150C +1,313
10-09（MEDIUM △）仓位参考: Max Pain 148 ｜ Call Wall 155（+3.2%，弱）（OI 5.8k） ｜ Put Wall 140（-6.8%，弱）（OI 3.8k）

📆 10-16 Forward Structure
存量OI: C 334.3k / P 340.2k，今日变化ΔOI: C +8.9k / P -0.5k，平值价格ATM: C $5.90 / P $5.35 ｜ ATM IV 43.8%，净 delta 敞口 394k shares
Top ΔOI: C 172 -10,103 ｜ C 162 +10,102 ｜ C 160 +6,942
仓位参考: Max Pain 143 ｜ Call Wall 160（+6.6%）（OI 42.2k） ｜ Put Wall 150（-0.1%，弱）（OI 19.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 43.8%｜历史 Rank 24%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 394,369 股

10-23（MEDIUM △）Top ΔOI: 140P +1,536 ｜ 155C +612
10-23（MEDIUM △）仓位参考: Max Pain 148 ｜ Call Wall 150（-0.1%，弱）（OI 3.4k） ｜ Put Wall 140（-6.8%）（OI 3.6k）

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 51.2% vs 10-09 44.6%（差 +6.6pp）——覆盖 PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/SPCX_morning.json