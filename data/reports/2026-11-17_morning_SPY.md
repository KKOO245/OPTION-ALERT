# 期权晨报 2026-11-17（快照 10:20 ET）

📊 市场环境

SPY $734.92 ｜ QQQ $656.95
VIX 22.73 ↓0.8%（5D +16.8%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.8　✅ 今日已公布
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🟡 **近现价集中开仓**: 11-18 718P ΔOI +15,185（距现价 -2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 739.95 → 今开 738.39（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 739.76 ｜ 低 736.07

Options: P/C成交量 1.01 | OI比 1.10 | ATM IV 31.2% | Skew 2.8pp | Term 0.58 | ExpMove ±1.3%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.58，近月 IV 高于远月）｜保护溢价中性（Skew 2.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.01×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.10×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 21% ｜ P/C OI(近端) 4%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 21%）｜近端持仓极端 Call 重（P/C OI 分位 4%，历史极低区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-18（1D）±1.3% ｜ 11-19（2D）±1.6% ｜ 11-20（3D）±1.9% ｜ 11-23（6D）±2.1%
   ⇒ IV–VIX Spread: +8.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,641,179,362 | GEX Change vs 上次快照 -60,883,130 | Flip: Primary Flip: 753.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 3018 / LOW 328 / INVALID 1420
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 753.50（全链重定价，覆盖 95%）
最近结构参考: Flip 754（现价低于该位 2.1%）
量化视角： 负 Gamma（16.41亿，历史分位偏负区，比 79% 的交易日更负）｜负 Gamma 加深（6088万）｜现价位于 Flip 下方 2.07%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 744（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 754（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 725.0P — Vol 56,881 | 最新价 $4.99 | OI 2625→58633 (ΔOI +56008张) | ΔOI/Volume 98.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增56008张（+2133.6% vs前日OI），连续性待观察（方向未知）
11-27 710.0P — Vol 66,572 | 最新价 $2.68 | OI 4482→58603 (ΔOI +54121张) | ΔOI/Volume 81.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增54121张（+1207.5% vs前日OI），连续性待观察（方向未知）
12-18 800.0C — Vol 30,996 | 最新价 $0.33 | OI 124065→151388 (ΔOI +27323张) | ΔOI/Volume 88.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27323张（+22.0% vs前日OI），连续性待观察（方向未知）
12-18 775.0C — Vol 31,985 | 最新价 $2.55 | OI 101506→121584 (ΔOI +20078张) | ΔOI/Volume 62.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20078张（+19.8% vs前日OI），连续性待观察（方向未知）
11-18 718.0P — Vol 22,394 | 最新价 $0.54 | OI 267→15452 (ΔOI +15185张) | ΔOI/Volume 67.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15185张（+5687.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 172,715 张（Put 125,314 / Call 47,401），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $42M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 158.8k / P 175.4k，今日成交量: C 420.0k / P 425.8k，平值价格ATM: C $2.33 / P $2.67 ｜ ATM IV 31.2%，预期波动 ±0.7%，Max Pain 744
Top ΔOI: P 713 +9,326 ｜ C 750 +7,862 ｜ P 640 +6,175

📆 Forward Expiration Structure

11-18  C +33.1k / P +38.3k ｜ Activity HIGH ｜ 1D
11-19  C +20.7k / P +18.0k ｜ Activity HIGH ｜ 2D
11-20  C +51.5k / P +26.4k ｜ Activity HIGH ｜ 3D
11-23  C +25.1k / P +20.4k ｜ Activity HIGH ｜ 6D

📆 11-18 Forward Structure
存量OI: C 111.8k / P 133.7k，今日变化ΔOI: C +33.1k / P +38.3k，平值价格ATM: C $4.68 / P $4.85 ｜ ATM IV 27.3%，净 delta 敞口 103k shares
Top ΔOI: P 718 +15,185 ｜ P 731 -6,533 ｜ P 730 +5,065
仓位参考: Max Pain 748 ｜ Call Wall 760（+3.0%，弱）（OI 5.9k） ｜ Put Wall 718（-2.7%，弱）（OI 15.5k）
量化解读： 存量 Put 重｜ATM IV 27.3%｜历史 Rank 97%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 103,493 股

📆 11-19 Forward Structure
存量OI: C 59.5k / P 86.1k，今日变化ΔOI: C +20.7k / P +18.0k，平值价格ATM: C $5.94 / P $5.88 ｜ ATM IV 25.7%，净 delta 敞口 35k shares
Top ΔOI: C 764 +1,801 ｜ C 750 +1,402 ｜ P 665 +1,372
仓位参考: Max Pain 750 ｜ Call Wall 750（+1.6%，弱）（OI 2.5k） ｜ Put Wall 750（+1.6%，弱）（OI 2.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 25.7%｜历史 Rank 97%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 34,893 股

📆 11-20 Forward Structure
存量OI: C 906.4k / P 2963.6k，今日变化ΔOI: C +51.5k / P +26.4k，平值价格ATM: C $7.15 / P $6.82 ｜ ATM IV 24.9%，净 delta 敞口 1.5M shares
Top ΔOI: P 770 -9,183 ｜ P 740 +7,474 ｜ P 710 +7,052
仓位参考: Max Pain 755 ｜ Put Wall 725（-1.7%，弱）（OI 71.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 24.9%｜历史 Rank 97%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,518,372 股

📆 11-23 Forward Structure
存量OI: C 45.9k / P 47.6k，今日变化ΔOI: C +25.1k / P +20.4k，平值价格ATM: C $8.12 / P $7.63 ｜ ATM IV 20.6%，净 delta 敞口 -199k shares
Top ΔOI: P 736 +2,807 ｜ P 728 +2,551 ｜ P 719 +2,496
仓位参考: Max Pain 750 ｜ Call Wall 752（+1.9%，弱）（OI 1.7k） ｜ Put Wall 736（-0.3%，弱）（OI 3.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 20.6%｜历史 Rank 97%（近端代理）｜IV/RV 0.91×（近似）｜净 delta 敞口 负 198,584 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/SPY_morning.json