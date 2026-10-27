# 期权晨报 2026-10-27（快照 10:20 ET）

📊 市场环境

SPY $769.58 ｜ QQQ $721.25
VIX 18.02 ↓2.0%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 1.8 ｜ 前值 0.1　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🔴 **事件差分**: 10-30（3D）ATM IV 115.5% vs 11-06 99.3%（差 +16.2pp），覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-30 160C ΔOI +2,312（距现价 -4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 153.27 → 今开 159.23（+3.9%） | 较昨收变动（含盘初走势） ｜ 今日高 170.93 ｜ 低 158.31

Options: P/C成交量 0.52 | OI比 0.54 | ATM IV 115.5% | Skew 2.7pp | Term 0.83 | ExpMove ±8.9%（近端） | Rank 67%
量化视角： IV 中性（Rank 67%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价中性（Skew 2.7pp）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（3D）±8.9% ｜ 11-06（10D）±13.2% ｜ 11-13（17D）±18.4% ｜ 11-20（24D）±21.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -40,285 | GEX Change vs 上次快照 11,033,287 | Flip: Primary Flip: 167.74（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 590 / LOW 38 / INVALID 226
结构观察区: Primary Flip 167.74（全链重定价，覆盖 100%）
最近结构参考: Flip 168（现价低于该位 0.0%）
量化视角： 负 Gamma（4万，无历史分位）｜负 Gamma 缓解（+1103万）｜现价位于 Flip 下方 0.04%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 172（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 168（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 160.0C — Vol 10,651 | 最新价 $4.30 | OI 1139→3451 (ΔOI +2312张) | ΔOI/Volume 21.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2312张（+203.0% vs前日OI），连续性待观察（方向未知）
10-30 180.0C — Vol 8,179 | 最新价 $0.68 | OI 2986→4271 (ΔOI +1285张) | ΔOI/Volume 15.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1285张（+43.0% vs前日OI），连续性待观察（方向未知）
10-30 185.0C — Vol 3,567 | 最新价 $0.43 | OI 1790→2693 (ΔOI +903张) | ΔOI/Volume 25.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增903张（+50.5% vs前日OI），连续性待观察（方向未知）
11-13 195.0C — Vol 1,054 | 最新价 $3.60 | OI 186→1088 (ΔOI +902张) | ΔOI/Volume 85.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增902张（+484.9% vs前日OI），连续性待观察（方向未知）
11-06 170.0C — Vol 1,608 | 最新价 $4.50 | OI 579→1468 (ΔOI +889张) | ΔOI/Volume 55.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增889张（+153.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,291 张（Put 0 / Call 6,291），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +12.2k / P +1.2k ｜ Activity HIGH ｜ 3D
11-06  C +4.7k / P +2.1k ｜ Activity HIGH ｜ 10D
11-13  C +2.1k / P +0.3k ｜ Activity MEDIUM △ ｜ 17D
11-20  C +0.7k / P +0.2k ｜ Activity HIGH ｜ 24D

📆 10-30 Forward Structure
存量OI: C 90.3k / P 48.6k，今日变化ΔOI: C +12.2k / P +1.2k，平值价格ATM: C $7.55 / P $7.40 ｜ ATM IV 115.5%，净 delta 敞口 871k shares
Top ΔOI: C 160 +2,312 ｜ P 230 -1,535 ｜ C 180 +1,285
仓位参考: Max Pain 172 ｜ Call Wall 180（+7.4%，弱）（OI 4.3k） ｜ Put Wall 160（-4.6%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 115.5%｜历史 Rank 67%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 871,387 股

📆 11-06 Forward Structure
存量OI: C 40.9k / P 25.6k，今日变化ΔOI: C +4.7k / P +2.1k，平值价格ATM: C $10.55 / P $11.50 ｜ ATM IV 99.3%，净 delta 敞口 211k shares
Top ΔOI: C 170 +889 ｜ P 140 +575 ｜ C 165 +419
仓位参考: Max Pain 200 ｜ Put Wall 170（+1.4%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 99.3%｜历史 Rank 67%（近端代理）｜IV/RV 1.30×（近似）｜净 delta 敞口 正 210,910 股

11-13（MEDIUM △）Top ΔOI: 195C +902 ｜ 200C +271
11-13（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 175（+4.4%，弱）（OI 1.2k） ｜ Put Wall 165（-1.6%，弱）（OI 1.4k）

📆 11-20 Forward Structure
存量OI: C 91.3k / P 104.3k，今日变化ΔOI: C +0.7k / P +0.2k，平值价格ATM: C $17.78 / P $17.40 ｜ ATM IV 102.3%，净 delta 敞口 69k shares
Top ΔOI: C 260 -569 ｜ P 150 -529 ｜ C 250 +524
仓位参考: Max Pain 195 ｜ Call Wall 180（+7.4%，弱）（OI 5.4k） ｜ Put Wall 180（+7.4%，弱）（OI 3.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 102.3%｜历史 Rank 67%（近端代理）｜IV/RV 1.34×（近似）｜净 delta 敞口 正 68,986 股

📅 事件差分（观察，非因果）: 10-30（3D）ATM IV 115.5% vs 11-06 99.3%（差 +16.2pp）——覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/NBIS_morning.json