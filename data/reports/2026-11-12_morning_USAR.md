# 期权晨报 2026-11-12（快照 10:20 ET）

📊 市场环境

SPY $756.94 ｜ QQQ $685.56
VIX 18.45 ↑5.5%（5D -34.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **事件差分**: 11-13（1D）ATM IV 125.8% vs 11-20 105.0%（差 +20.8pp），覆盖 成屋销售、PPI 生产者物价 MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-13 8P ΔOI +624（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 8.27 → 今开 7.90（-4.4%） | 较昨收变动（含盘初走势） ｜ 今日高 8.19 ｜ 低 7.69

Options: P/C成交量 0.51 | OI比 0.25 | ATM IV 125.8% | Skew -4.6pp | Term 0.80 | ExpMove ±6.3%（近端） | Rank 65%
量化视角： IV 中性（Rank 65%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.25）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.25×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±6.3% ｜ 11-20（8D）±12.8% ｜ 11-27（15D）±17.6% ｜ 12-04（22D）±15.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 72,815 | GEX Change vs 上次快照 -1,983,416 | Flip: Primary Flip: 7.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 231 / LOW 94 / INVALID 99
结构观察区: Primary Flip 7.87（全链重定价，覆盖 100%）
最近结构参考: Flip 8（现价高于该位 0.2%）
量化视角： 正 Gamma（7万，无历史分位）｜正 Gamma 减弱（198万）｜现价位于 Flip 上方 0.20%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 8（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 8（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 8.0C — Vol 2,343 | 最新价 $0.90 | OI 357→1277 (ΔOI +920张) | ΔOI/Volume 39.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增920张（+257.7% vs前日OI），连续性待观察（方向未知）
11-20 8.5C — Vol 947 | 最新价 $0.41 | OI 196→937 (ΔOI +741张) | ΔOI/Volume 78.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增741张（+378.1% vs前日OI），连续性待观察（方向未知）
11-13 8.0P — Vol 1,176 | 最新价 $0.16 | OI 708→1332 (ΔOI +624张) | ΔOI/Volume 53.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增624张（+88.1% vs前日OI），连续性待观察（方向未知）
11-20 8.5P — Vol 399 | 最新价 $0.56 | OI 90→391 (ΔOI +301张) | ΔOI/Volume 75.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增301张（+334.4% vs前日OI），连续性待观察（方向未知）
11-20 10.5C — Vol 399 | 最新价 $0.07 | OI 1381→1622 (ΔOI +241张) | ΔOI/Volume 60.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增241张（+17.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,827 张（Put 925 / Call 1,902），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +0.2k / P +0.4k ｜ Activity MEDIUM △ ｜ 1D
11-20  C +1.0k / P -3 ｜ Activity MEDIUM △ ｜ 8D
11-27  C +1.0k / P +79 ｜ Activity HIGH ｜ 15D
12-04  C +91 / P +3 ｜ Activity MEDIUM △ ｜ 22D

📆 11-13 Forward Structure
存量OI: C 28.0k / P 7.1k，今日变化ΔOI: C +0.2k / P +0.4k，平值价格ATM: C $0.20 / P $0.30 ｜ ATM IV 125.8%，净 delta 敞口 -35k shares
Top ΔOI: P 8 +624
仓位参考: Max Pain 8 ｜ Call Wall 8（+1.5%，弱）（OI 1.8k） ｜ Put Wall 8（+1.5%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 125.8%｜历史 Rank 65%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 35,329 股

11-20（MEDIUM △）Top ΔOI: 8C +741 ｜ 8P +301
11-20（MEDIUM △）仓位参考: Max Pain 10 ｜ Call Wall 8（+1.5%，弱）（OI 1.7k） ｜ Put Wall 8（+1.5%，弱）（OI 7.2k）

📆 11-27 Forward Structure
存量OI: C 11.6k / P 3.2k，今日变化ΔOI: C +1.0k / P +79，平值价格ATM: C $0.90 / P $0.49 ｜ ATM IV 96.5%，净 delta 敞口 47k shares
Top ΔOI: C 8 +920
仓位参考: Max Pain 8 ｜ Call Wall 8（+1.5%，弱）（OI 1.3k） ｜ Put Wall 8（+1.5%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 96.5%｜历史 Rank 65%（近端代理）｜IV/RV 0.91×（近似）｜净 delta 敞口 正 46,547 股

12-04（MEDIUM △）仓位参考: Max Pain 10 ｜ Call Wall 8（+1.5%，弱）（OI 0.1k） ｜ Put Wall 8.5（+7.8%）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 125.8% vs 11-20 105.0%（差 +20.8pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/USAR_morning.json