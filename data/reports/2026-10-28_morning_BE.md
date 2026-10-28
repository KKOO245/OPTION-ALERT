# 期权晨报 2026-10-28（快照 10:20 ET）

📊 市场环境

SPY $770.58 ｜ QQQ $721.71
VIX 17.36 ↓0.9%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　⏰ 今日
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4　⏰ 今日
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　⏰ 今日
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🔴 **事件差分**: 10-30（2D）ATM IV 107.7% vs 11-06 87.3%（差 +20.4pp），覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-30 222C ΔOI +1,660（距现价 -0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 218.50 → 今开 225.97（+3.4%） | 较昨收变动（含盘初走势） ｜ 今日高 227.55 ｜ 低 217.90

Options: P/C成交量 0.59 | OI比 0.74 | ATM IV 107.7% | Skew 1.7pp | Term 0.75 | ExpMove ±6.9%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜保护溢价薄（Skew 1.7pp）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.59×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±6.9% ｜ 11-06（9D）±11.7% ｜ 11-13（16D）±14.3% ｜ 11-20（23D）±16.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,928,999 | GEX Change vs 上次快照 -629,978 | Flip: Primary Flip: 215.26（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 583 / LOW 111 / INVALID 244
结构观察区: Primary Flip 215.26（全链重定价，覆盖 98%）
最近结构参考: Flip 215（现价高于该位 3.8%）
量化视角： 正 Gamma（393万，无历史分位）｜正 Gamma 减弱（63万）｜现价位于 Flip 上方 3.75%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 212（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 215（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 222.5C — Vol 3,974 | 最新价 $6.10 | OI 484→2144 (ΔOI +1660张) | ΔOI/Volume 41.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1660张（+343.0% vs前日OI），连续性待观察（方向未知）
10-30 250.0C — Vol 3,151 | 最新价 $0.71 | OI 1807→2917 (ΔOI +1110张) | ΔOI/Volume 35.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1110张（+61.4% vs前日OI），连续性待观察（方向未知）
10-30 210.0P — Vol 2,690 | 最新价 $4.00 | OI 1254→2316 (ΔOI +1062张) | ΔOI/Volume 39.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1062张（+84.7% vs前日OI），连续性待观察（方向未知）
11-20 350.0C — Vol 1,307 | 最新价 $0.49 | OI 2593→3444 (ΔOI +851张) | ΔOI/Volume 65.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增851张（+32.8% vs前日OI），连续性待观察（方向未知）
10-30 240.0C — Vol 4,932 | 最新价 $1.65 | OI 3468→4143 (ΔOI +675张) | ΔOI/Volume 13.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增675张（+19.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,358 张（Put 1,062 / Call 4,296），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +2.9k / P +2.2k ｜ Activity HIGH ｜ 2D
11-06  C +2.5k / P +2.6k ｜ Activity MEDIUM △ ｜ 9D
11-13  C +0.7k / P +0.3k ｜ Activity MEDIUM △ ｜ 16D
11-20  C +2.4k / P +0.9k ｜ Activity MEDIUM △ ｜ 23D

📆 10-30 Forward Structure
存量OI: C 65.6k / P 48.4k，今日变化ΔOI: C +2.9k / P +2.2k，平值价格ATM: C $8.65 / P $6.80 ｜ ATM IV 107.7%，净 delta 敞口 -135k shares
Top ΔOI: C 222 +1,660 ｜ C 250 +1,110 ｜ P 210 +1,062
仓位参考: Max Pain 212 ｜ Call Wall 240（+7.5%，弱）（OI 4.1k） ｜ Put Wall 210（-6.0%，弱）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 107.7%｜历史 Rank 68%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 135,475 股

11-06（MEDIUM △）Top ΔOI: 220P +417 ｜ 240C +413
11-06（MEDIUM △）仓位参考: Max Pain 230 ｜ Call Wall 225（+0.7%，弱）（OI 1.4k） ｜ Put Wall 235（+5.2%，弱）（OI 2.0k）

11-13（MEDIUM △）Top ΔOI: 250C +111
11-13（MEDIUM △）仓位参考: Max Pain 242 ｜ Call Wall 240（+7.5%，弱）（OI 0.5k） ｜ Put Wall 240（+7.5%，弱）（OI 0.5k）

11-20（MEDIUM △）Top ΔOI: 180P +330 ｜ 217P +220
11-20（MEDIUM △）仓位参考: Max Pain 230 ｜ Call Wall 240（+7.5%，弱）（OI 2.7k） ｜ Put Wall 220（-1.5%，弱）（OI 3.7k）

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 107.7% vs 11-06 87.3%（差 +20.4pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/BE_morning.json