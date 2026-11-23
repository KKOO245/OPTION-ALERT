# 期权晚报 2026-11-23（快照 16:40 ET）

📊 市场环境

SPY $722.29 ｜ QQQ $651.03
VIX 26.62 ↓25.8%（5D +16.2%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.0（extreme fear）
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
🟡 **近现价集中开仓**: 11-24 635P ΔOI +6,745（距现价 -2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 655.98 → 收盘 651.03（-0.8%） ｜ 今日高 657.50 ｜ 低 641.95 ｜ 昨收 608.45 → 收盘 651.03（+7.0%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-30，窗口结束前不做对错判定）

Options: P/C成交量 1.24 | OI比 1.05 | ATM IV 51.0% | Skew -1.1pp | Term 0.61 | ExpMove ±1.9%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.1pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.24）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.24×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.05×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 48% ｜ P/C OI(近端) 7%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 48%）｜近端持仓极端 Call 重（P/C OI 分位 7%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-24（1D）±1.9% ｜ 11-25（2D）±2.6% ｜ 11-27（4D）±3.1% ｜ 11-30（7D）±3.7%
   ⇒ IV–VIX Spread: +24.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -48,323,282 | GEX Change vs 上次快照 24,759,709 | Flip: Primary Flip: 653.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 3289 / LOW 475 / INVALID 1918
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 653.92（全链重定价，覆盖 95%）
最近结构参考: Flip 654（现价低于该位 0.4%）
量化视角： 负 Gamma（4832万，历史分位 48%，中性区）｜负 Gamma 缓解（+2476万）｜现价位于 Flip 下方 0.44%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 630（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 654（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 680.0C — Vol 21,728 | 最新价 $9.01 | OI 47309→94371 (ΔOI +47062张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增47062张（+99.5% vs前日OI），连续性待观察（方向未知）
11-30 580.0P — Vol 1,802 | 最新价 $0.80 | OI 8391→28364 (ΔOI +19973张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19973张（+238.0% vs前日OI），连续性待观察（方向未知）
11-30 650.0C — Vol 6,878 | 最新价 $12.76 | OI 698→13877 (ΔOI +13179张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13179张（+1888.1% vs前日OI），连续性待观察（方向未知）
12-18 580.0P — Vol 36,415 | 最新价 $5.55 | OI 26279→38990 (ΔOI +12711张) | ΔOI/Volume 34.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12711张（+48.4% vs前日OI），连续性待观察（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 92,925 张（Put 32,684 / Call 60,241），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-24  C +29.4k / P +36.2k ｜ Activity HIGH ｜ 1D
11-25  C +37.0k / P +19.3k ｜ Activity HIGH ｜ 2D
11-27  C +39.5k / P +34.8k ｜ Activity HIGH ｜ 4D
11-30  C +42.8k / P +24.1k ｜ Activity HIGH ｜ 7D

📆 11-24 Forward Structure
存量OI: C 70.0k / P 113.2k，今日变化ΔOI: C +29.4k / P +36.2k，平值价格ATM: C $5.98 / P $6.39 ｜ ATM IV 45.2%，净 delta 敞口 1.6M shares
Top ΔOI: P 635 +6,745 ｜ P 610 +6,276 ｜ P 648 +4,702
仓位参考: Max Pain 645 ｜ Call Wall 645（-0.9%，弱）（OI 3.2k） ｜ Put Wall 635（-2.5%，弱）（OI 7.1k）
量化解读： 存量 Put 重｜ATM IV 45.2%｜历史 Rank 98%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,600,348 股

📆 11-25 Forward Structure
存量OI: C 92.6k / P 54.4k，今日变化ΔOI: C +37.0k / P +19.3k，平值价格ATM: C $8.47 / P $8.60 ｜ ATM IV 44.5%，净 delta 敞口 2.2M shares
Top ΔOI: C 650 +6,625 ｜ C 660 +2,967
仓位参考: Max Pain 638 ｜ Call Wall 650（-0.2%，弱）（OI 7.1k） ｜ Put Wall 635（-2.5%，弱）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 44.5%｜历史 Rank 98%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,190,848 股

📆 11-27 Forward Structure
存量OI: C 234.7k / P 176.3k，今日变化ΔOI: C +39.5k / P +34.8k，平值价格ATM: C $10.16 / P $9.79 ｜ ATM IV 37.4%，净 delta 敞口 3.4M shares
Top ΔOI: C 650 +5,710 ｜ C 640 +5,465 ｜ P 605 +4,951
仓位参考: Max Pain 650 ｜ Call Wall 665（+2.1%，弱）（OI 10.0k） ｜ Put Wall 640（-1.7%，弱）（OI 12.5k）
量化解读： 存量 Call 重｜ATM IV 37.4%｜历史 Rank 98%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,378,001 股

📆 11-30 Forward Structure
存量OI: C 298.4k / P 306.2k，今日变化ΔOI: C +42.8k / P +24.1k，平值价格ATM: C $12.19 / P $11.85 ｜ ATM IV 33.3%，净 delta 敞口 3.6M shares
Top ΔOI: P 580 +19,973 ｜ C 650 +13,179 ｜ C 630 +6,770
仓位参考: Max Pain 675 ｜ Call Wall 650（-0.2%，弱）（OI 13.9k） ｜ Put Wall 650（-0.2%，弱）（OI 19.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 33.3%｜历史 Rank 98%（近端代理）｜IV/RV 0.80×（近似）｜净 delta 敞口 正 3,578,549 股

📅 事件差分（观察，非因果）: 11-25（2D）ATM IV 44.5% vs 11-27 37.4%（差 +7.2pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/QQQ_evening.json