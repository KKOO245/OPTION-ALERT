# 期权晨报 2026-11-23（快照 10:20 ET）

📊 市场环境

SPY $722.55 ｜ QQQ $657.00
VIX 27.37 ↓23.7%（5D +19.5%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 19.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.4 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🟡 **近现价集中开仓**: 11-24 635P ΔOI +6,745（距现价 -2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 608.45 → 今开 655.98（+7.8%） | 较昨收变动（含盘初走势） ｜ 今日高 656.25 ｜ 低 641.95

Options: P/C成交量 1.18 | OI比 1.05 | ATM IV 64.5% | Skew 7.6pp | Term 0.47 | ExpMove ±2.5%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.47，近月 IV 高于远月）｜保护溢价显著（Skew 7.6pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.18）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.18×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.05×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 46% ｜ P/C OI(近端) 7%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 46%）｜近端持仓极端 Call 重（P/C OI 分位 7%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-24（1D）±2.5% ｜ 11-25（2D）±3.0% ｜ 11-27（4D）±3.4% ｜ 11-30（7D）±3.9%
   ⇒ IV–VIX Spread: +37.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -73,082,991 | GEX Change vs 上次快照 400,417,085 | Flip: Primary Flip: 654.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 3613 / LOW 381 / INVALID 1688
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 654.93（全链重定价，覆盖 99%）
最近结构参考: Flip 655（现价低于该位 0.6%）
量化视角： 负 Gamma（7308万，历史分位 46%，中性区）｜负 Gamma 缓解（+4.00亿）｜现价位于 Flip 下方 0.64%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 630（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 655（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 680.0C — Vol 80,475 | 最新价 $3.47 | OI 47309→94371 (ΔOI +47062张) | ΔOI/Volume 58.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增47062张（+99.5% vs前日OI），连续性待观察（方向未知）
11-23 590.0P — Vol 31,011 | 最新价 $3.21 | OI 1189→21953 (ΔOI +20764张) | ΔOI/Volume 67.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20764张（+1746.3% vs前日OI），连续性待观察（方向未知）
11-30 580.0P — Vol 29,422 | 最新价 $7.95 | OI 8391→28364 (ΔOI +19973张) | ΔOI/Volume 67.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19973张（+238.0% vs前日OI），连续性待观察（方向未知）
11-30 650.0C — Vol 22,045 | 最新价 $3.47 | OI 698→13877 (ΔOI +13179张) | ΔOI/Volume 59.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13179张（+1888.1% vs前日OI），连续性待观察（方向未知）
12-18 580.0P — Vol 26,227 | 最新价 $16.03 | OI 26279→38990 (ΔOI +12711张) | ΔOI/Volume 48.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12711张（+48.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 113,689 张（Put 53,448 / Call 60,241），跨 3 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 173.6k / P 181.9k，今日成交量: C 395.5k / P 466.9k，平值价格ATM: C $4.42 / P $4.66 ｜ ATM IV 64.5%，预期波动 ±1.4%，Max Pain 630
Top ΔOI: P 590 +20,764 ｜ P 605 +6,422 ｜ C 650 +5,716

📆 Forward Expiration Structure

11-24  C +29.4k / P +36.2k ｜ Activity HIGH ｜ 1D
11-25  C +37.0k / P +19.3k ｜ Activity HIGH ｜ 2D
11-27  C +39.5k / P +34.8k ｜ Activity HIGH ｜ 4D
11-30  C +42.8k / P +24.1k ｜ Activity MEDIUM △ ｜ 7D

📆 11-24 Forward Structure
存量OI: C 70.0k / P 113.2k，今日变化ΔOI: C +29.4k / P +36.2k，平值价格ATM: C $7.97 / P $8.45 ｜ ATM IV 53.1%，净 delta 敞口 1.4M shares
Top ΔOI: P 635 +6,745 ｜ P 610 +6,276 ｜ P 648 +4,702
仓位参考: Max Pain 645 ｜ Call Wall 645（-0.9%，弱）（OI 3.2k） ｜ Put Wall 635（-2.4%，弱）（OI 7.1k）
量化解读： 存量 Put 重｜ATM IV 53.1%｜历史 Rank 100%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,410,393 股

📆 11-25 Forward Structure
存量OI: C 92.6k / P 54.4k，今日变化ΔOI: C +37.0k / P +19.3k，平值价格ATM: C $9.38 / P $10.38 ｜ ATM IV 48.6%，净 delta 敞口 2.1M shares
Top ΔOI: C 650 +6,625 ｜ C 660 +2,967 ｜ P 550 +2,888
仓位参考: Max Pain 638 ｜ Call Wall 650（-0.1%，弱）（OI 7.1k） ｜ Put Wall 635（-2.4%，弱）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 48.6%｜历史 Rank 100%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,130,943 股

📆 11-27 Forward Structure
存量OI: C 234.7k / P 176.3k，今日变化ΔOI: C +39.5k / P +34.8k，平值价格ATM: C $10.98 / P $11.20 ｜ ATM IV 39.9%，净 delta 敞口 3.3M shares
Top ΔOI: C 650 +5,710 ｜ C 640 +5,465 ｜ P 605 +4,951
仓位参考: Max Pain 650 ｜ Call Wall 665（+2.2%，弱）（OI 10.0k） ｜ Put Wall 640（-1.7%，弱）（OI 12.5k）
量化解读： 存量 Call 重｜ATM IV 39.9%｜历史 Rank 100%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,284,331 股

11-30（MEDIUM △）Top ΔOI: 580P +19,973 ｜ 650C +13,179
11-30（MEDIUM △）仓位参考: Max Pain 675 ｜ Call Wall 650（-0.1%，弱）（OI 13.9k） ｜ Put Wall 650（-0.1%，弱）（OI 19.8k）

📅 事件差分（观察，非因果）: 11-25（2D）ATM IV 48.6% vs 11-27 39.9%（差 +8.8pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/QQQ_morning.json