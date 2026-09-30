# 期权晨报 2026-09-29（快照 10:20 ET）

📊 市场环境

SPY $764.20 ｜ QQQ $nan
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
🟡 **事件差分**: 10-02 ATM IV 84.1% vs 10-09 70.2%（差 +13.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-09 1800P ΔOI +709（距现价 +4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,712.89 → 今开 1,744.41（+1.8%） | 较昨收变动（含盘初走势） ｜ 今日高 1749.78 ｜ 低 1693.00

Options: P/C成交量 0.45 | OI比 0.97 | ATM IV 84.1% | Skew -3.5pp | Term 0.84 | ExpMove ±6.4%（近端） | Rank 38%
量化视角： IV 中性（Rank 38%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.97×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（3D）±6.4% ｜ 10-09（10D）±9.6% ｜ 10-16（17D）±11.1% ｜ 10-23（24D）±13.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,353,888 | GEX Change vs 上次快照 1,372,881 | Flip: Primary Flip: 1707.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1703 / LOW 407 / INVALID 1156
结构观察区: Primary Flip 1707.87（全链重定价，覆盖 99%）
Put Wall 1,600（弱结构｜现价高于该位 7.9%）
最近结构参考: Flip 1708（现价高于该位 1.1%）
量化视角： 正 Gamma（135万，无历史分位）｜由负转正（+137万）｜现价位于 Flip 上方 1.08%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,600（Put Wall，弱结构） / 1,700（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1708（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 2000.0C — Vol 7,297 | 最新价 $3.80 | OI 4068→5260 (ΔOI +1192张) | ΔOI/Volume 16.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1192张（+29.3% vs前日OI），连续性待观察（方向未知）
10-02 1600.0P — Vol 2,847 | 最新价 $14.40 | OI 979→1969 (ΔOI +990张) | ΔOI/Volume 34.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增990张（+101.1% vs前日OI），连续性待观察（方向未知）
10-09 1800.0P — Vol 847 | 最新价 $135.55 | OI 148→857 (ΔOI +709张) | ΔOI/Volume 83.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增709张（+479.1% vs前日OI），连续性待观察（方向未知）
10-02 1620.0P — Vol 1,033 | 最新价 $18.80 | OI 150→784 (ΔOI +634张) | ΔOI/Volume 61.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增634张（+422.7% vs前日OI），连续性待观察（方向未知）
10-02 1500.0P — Vol 1,128 | 最新价 $2.70 | OI 1038→1451 (ΔOI +413张) | ΔOI/Volume 36.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增413张（+39.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,938 张（Put 2,746 / Call 1,192），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $12M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +7.4k / P +6.8k ｜ Activity HIGH ｜ 3D
10-09  C +1.6k / P +2.3k ｜ Activity HIGH ｜ 10D
10-16  C +1.2k / P +1.6k ｜ Activity MEDIUM △ ｜ 17D
10-23  C +0.4k / P +0.4k ｜ Activity MEDIUM △ ｜ 24D

📆 10-02 Forward Structure
存量OI: C 38.7k / P 37.5k，今日变化ΔOI: C +7.4k / P +6.8k，平值价格ATM: C $58.10 / P $53.00 ｜ ATM IV 84.1%，净 delta 敞口 132k shares
Top ΔOI: C 2000 +1,192 ｜ P 1600 +990 ｜ P 1620 +634
仓位参考: Max Pain 1,700 ｜ Call Wall 1600（-7.3%，弱）（OI 1.8k） ｜ Put Wall 1600（-7.3%，弱）（OI 2.0k）
量化解读： 存量两侧均衡｜ATM IV 84.1%｜历史 Rank 38%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 131,866 股

📆 10-09 Forward Structure
存量OI: C 11.5k / P 10.7k，今日变化ΔOI: C +1.6k / P +2.3k，平值价格ATM: C $83.00 / P $81.96 ｜ ATM IV 70.2%，净 delta 敞口 -26k shares
Top ΔOI: P 1800 +709 ｜ C 2000 +194 ｜ C 1875 +140
仓位参考: Max Pain 1,640 ｜ Put Wall 1800（+4.3%）（OI 0.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 70.2%｜历史 Rank 38%（近端代理）｜IV/RV 0.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 26,276 股

10-16（MEDIUM △）Top ΔOI: 2100C -322 ｜ 1380P +207
10-16（MEDIUM △）仓位参考: Max Pain 1,650 ｜ Call Wall 1800（+4.3%，弱）（OI 1.2k） ｜ Put Wall 1600（-7.3%，弱）（OI 1.6k）

10-23（MEDIUM △）Top ΔOI: 1700P +77 ｜ 1845C +41
10-23（MEDIUM △）仓位参考: Max Pain 1,745 ｜ Call Wall 1840（+6.6%，弱）（OI 0.2k） ｜ Put Wall 1650（-4.4%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 84.1% vs 10-09 70.2%（差 +13.9pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/SNDK_morning.json