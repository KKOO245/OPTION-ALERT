# 期权晨报 2026-10-28（快照 10:20 ET）

📊 市场环境

SPY $770.28 ｜ QQQ $725.61
VIX 17.36 ↓0.9%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 4　✅ 今日已公布
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🔴 **事件差分**: 10-30（2D）ATM IV 110.4% vs 11-06 95.2%（差 +15.2pp），覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-06 170C ΔOI +895（距现价 -1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 170.47 → 今开 173.65（+1.9%） | 较昨收变动（含盘初走势） ｜ 今日高 175.55 ｜ 低 168.92

Options: P/C成交量 0.84 | OI比 0.54 | ATM IV 110.4% | Skew 3.6pp | Term 0.83 | ExpMove ±7.1%（近端） | Rank 61%
量化视角： IV 中性（Rank 61%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价中性（Skew 3.6pp）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±7.1% ｜ 11-06（9D）±12.0% ｜ 11-13（16D）±18.1% ｜ 11-20（23D）±20.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,411,543 | GEX Change vs 上次快照 1,661,752 | Flip: Primary Flip: 168.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 590 / LOW 57 / INVALID 207
结构观察区: Primary Flip 168.87（全链重定价，覆盖 100%）
最近结构参考: Flip 169（现价高于该位 2.4%）
量化视角： 正 Gamma（341万，无历史分位）｜正 Gamma 增强（+166万）｜现价位于 Flip 上方 2.44%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 175（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 169（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 195.0C — Vol 1,770 | 最新价 $0.74 | OI 1485→2450 (ΔOI +965张) | ΔOI/Volume 54.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增965张（+65.0% vs前日OI），连续性待观察（方向未知）
10-30 200.0C — Vol 4,506 | 最新价 $0.44 | OI 6026→6977 (ΔOI +951张) | ΔOI/Volume 21.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增951张（+15.8% vs前日OI），连续性待观察（方向未知）
11-06 200.0C — Vol 2,283 | 最新价 $2.63 | OI 1534→2483 (ΔOI +949张) | ΔOI/Volume 41.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增949张（+61.9% vs前日OI），连续性待观察（方向未知）
11-06 170.0C — Vol 2,633 | 最新价 $11.50 | OI 1468→2363 (ΔOI +895张) | ΔOI/Volume 34.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增895张（+61.0% vs前日OI），连续性待观察（方向未知）
11-06 220.0P — Vol 871 | 最新价 $49.50 | OI 1820→2684 (ΔOI +864张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增864张（+47.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,624 张（Put 864 / Call 3,760），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +2.5k / P +1.3k ｜ Activity HIGH ｜ 2D
11-06  C +5.0k / P +3.7k ｜ Activity MEDIUM △ ｜ 9D
11-13  C +0.4k / P +0.8k ｜ Activity MEDIUM △ ｜ 16D
11-20  C +0.2k / P +2.0k ｜ Activity MEDIUM △ ｜ 23D

📆 10-30 Forward Structure
存量OI: C 92.8k / P 49.9k，今日变化ΔOI: C +2.5k / P +1.3k，平值价格ATM: C $6.91 / P $5.45 ｜ ATM IV 110.4%，净 delta 敞口 9k shares
Top ΔOI: C 195 +965 ｜ C 187 +689
仓位参考: Max Pain 175 ｜ Call Wall 190（+9.8%，弱）（OI 4.5k） ｜ Put Wall 160（-7.5%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 110.4%｜历史 Rank 61%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 9,420 股

11-06（MEDIUM △）Top ΔOI: 200C +949 ｜ 170C +895
11-06（MEDIUM △）仓位参考: Max Pain 198 ｜ Call Wall 170（-1.7%，弱）（OI 2.4k） ｜ Put Wall 170（-1.7%，弱）（OI 1.8k）

11-13（MEDIUM △）Top ΔOI: 170C +209 ｜ 143P +180
11-13（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 175（+1.2%，弱）（OI 1.1k） ｜ Put Wall 165（-4.6%，弱）（OI 1.4k）

11-20（MEDIUM △）Top ΔOI: 125P +808
11-20（MEDIUM △）仓位参考: Max Pain 195 ｜ Call Wall 180（+4.1%，弱）（OI 5.5k） ｜ Put Wall 180（+4.1%，弱）（OI 3.2k）

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 110.4% vs 11-06 95.2%（差 +15.2pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/NBIS_morning.json