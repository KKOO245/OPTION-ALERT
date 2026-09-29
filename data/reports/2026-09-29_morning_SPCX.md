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
🟡 **近现价集中开仓**: 10-02 140P ΔOI +5,557（距现价 -3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 145.47 → 今开 146.68（+0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 147.48 ｜ 低 145.47

Options: P/C成交量 0.35 | OI比 1.04 | ATM IV 51.6% | Skew 0.6pp | Term 0.87 | ExpMove ±3.9%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价薄（Skew 0.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.35×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.04×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（3D）±3.9% ｜ 10-09（10D）±6.2% ｜ 10-16（17D）±7.7% ｜ 10-23（24D）±9.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -18,988,863 | GEX Change vs 上次快照 4,005,603 | Flip: Primary Flip: 147.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 549 / LOW 77 / INVALID 296
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 147.02（全链重定价，覆盖 100%）
Call Wall 160（弱结构｜现价低于该位 9.0%）
最近结构参考: Flip 147（现价低于该位 1.0%）
量化视角： 负 Gamma（1899万，无历史分位）｜负 Gamma 缓解（+401万）｜现价位于 Flip 下方 0.98%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 148（MaxPain，仅结算参考） / 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 147（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 160.0C — Vol 32,355 | 最新价 $0.22 | OI 10102→21773 (ΔOI +11671张) | ΔOI/Volume 36.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11671张（+115.5% vs前日OI），连续性待观察（方向未知）
10-02 162.5C — Vol 16,084 | 最新价 $0.15 | OI 3092→14327 (ΔOI +11235张) | ΔOI/Volume 69.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11235张（+363.4% vs前日OI），连续性待观察（方向未知）
10-02 140.0P — Vol 12,770 | 最新价 $1.13 | OI 13443→19000 (ΔOI +5557张) | ΔOI/Volume 43.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5557张（+41.3% vs前日OI），连续性待观察（方向未知）
10-02 155.0C — Vol 27,073 | 最新价 $0.56 | OI 13924→18976 (ΔOI +5052张) | ΔOI/Volume 18.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5052张（+36.3% vs前日OI），连续性待观察（方向未知）
10-09 180.0C — Vol 4,299 | 最新价 $0.11 | OI 12108→15824 (ΔOI +3716张) | ΔOI/Volume 86.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3716张（+30.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 37,231 张（Put 5,557 / Call 31,674），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +44.1k / P +27.0k ｜ Activity HIGH ｜ 3D
10-09  C +15.1k / P +3.0k ｜ Activity HIGH ｜ 10D
10-16  C +0.5k / P +2.9k ｜ Activity MEDIUM △ ｜ 17D
10-23  C +1.8k / P +2.0k ｜ Activity MEDIUM △ ｜ 24D

📆 10-02 Forward Structure
存量OI: C 180.9k / P 188.6k，今日变化ΔOI: C +44.1k / P +27.0k，平值价格ATM: C $2.79 / P $2.92 ｜ ATM IV 51.6%，净 delta 敞口 95k shares
Top ΔOI: C 160 +11,671 ｜ C 162 +11,235 ｜ P 140 +5,557
仓位参考: Max Pain 148 ｜ Call Wall 160（+9.9%，弱）（OI 21.8k） ｜ Put Wall 140（-3.8%，弱）（OI 19.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 51.6%｜历史 Rank 26%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 94,614 股

📆 10-09 Forward Structure
存量OI: C 65.0k / P 42.5k，今日变化ΔOI: C +15.1k / P +3.0k，平值价格ATM: C $4.50 / P $4.60 ｜ ATM IV 45.8%，净 delta 敞口 130k shares
仓位参考: Max Pain 148 ｜ Call Wall 155（+6.5%，弱）（OI 5.1k） ｜ Put Wall 135（-7.3%）（OI 5.4k）
量化解读： 存量 Call 重｜ATM IV 45.8%｜历史 Rank 26%（近端代理）｜IV/RV 1.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 129,933 股

10-16（MEDIUM △）Top ΔOI: 155C +933
10-16（MEDIUM △）仓位参考: Max Pain 142 ｜ Call Wall 160（+9.9%，弱）（OI 35.2k） ｜ Put Wall 135（-7.3%，弱）（OI 30.6k）

10-23（MEDIUM △）Top ΔOI: 145P +659 ｜ 160P +399
10-23（MEDIUM △）仓位参考: Max Pain 149 ｜ Call Wall 150（+3.0%）（OI 3.3k） ｜ Put Wall 135（-7.3%，弱）（OI 2.2k）

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 51.6% vs 10-09 45.8%（差 +5.9pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/SPCX_morning.json