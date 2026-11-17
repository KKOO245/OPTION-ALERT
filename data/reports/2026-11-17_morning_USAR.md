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
🔴 **事件差分**: 11-20（3D）ATM IV 122.8% vs 11-27 105.8%（差 +17.0pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 7.13 → 今开 7.14（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 7.14 ｜ 低 6.77

Options: P/C成交量 0.44 | OI比 0.54 | ATM IV 122.8% | Skew 8.7pp | Term 0.86 | ExpMove ±9.4%（近端） | Rank 62%
量化视角： IV 中性（Rank 62%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价显著（Skew 8.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（3D）±9.4% ｜ 11-27（10D）±13.5% ｜ 12-04（17D）±18.6% ｜ 12-11（24D）±22.2%
   ⇒ IV–VIX Spread: +100.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 457,982 | GEX Change vs 上次快照 1,498,487 | Flip: Primary Flip: 6.66（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 157 / LOW 98 / INVALID 177
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 6.66（全链重定价，覆盖 100%）
最近结构参考: Flip 7（现价高于该位 3.5%）
量化视角： 正 Gamma（46万，无历史分位）｜由负转正（+150万）｜现价位于 Flip 上方 3.53%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 7（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 8.5C — Vol 2,587 | 最新价 $0.05 | OI 2680→4587 (ΔOI +1907张) | ΔOI/Volume 73.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1907张（+71.2% vs前日OI），连续性待观察（方向未知）
11-27 8.5C — Vol 3,143 | 最新价 $0.13 | OI 1137→2656 (ΔOI +1519张) | ΔOI/Volume 48.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1519张（+133.6% vs前日OI），连续性待观察（方向未知）
12-18 7.0C — Vol 903 | 最新价 $1.03 | OI 45→897 (ΔOI +852张) | ΔOI/Volume 94.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增852张（+1893.3% vs前日OI），连续性待观察（方向未知）
11-27 8.0C — Vol 2,245 | 最新价 $0.23 | OI 2700→3376 (ΔOI +676张) | ΔOI/Volume 30.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增676张（+25.0% vs前日OI），连续性待观察（方向未知）
11-20 7.5C — Vol 644 | 最新价 $0.21 | OI 118→610 (ΔOI +492张) | ΔOI/Volume 76.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增492张（+416.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,446 张（Put 0 / Call 5,446），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +3.2k / P -1.4k ｜ Activity MEDIUM △ ｜ 3D
11-27  C +3.2k / P -91 ｜ Activity HIGH ｜ 10D
12-04  C +72 / P -76 ｜ Activity LOW ｜ 17D
12-11  C +13 / P +47 ｜ Activity MEDIUM △ ｜ 24D

📆 11-20 Forward Structure
存量OI: C 55.6k / P 30.0k，今日变化ΔOI: C +3.2k / P -1.4k，平值价格ATM: C $0.28 / P $0.37 ｜ ATM IV 122.8%，净 delta 敞口 193k shares
Top ΔOI: P 13 -754 ｜ P 12 -652
仓位参考: Max Pain 10 ｜ Put Wall 7（+1.5%，弱）（OI 3.2k）
量化解读： 存量 Call 重｜ATM IV 122.8%｜历史 Rank 62%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 192,516 股

📆 11-27 Forward Structure
存量OI: C 16.7k / P 3.2k，今日变化ΔOI: C +3.2k / P -91，平值价格ATM: C $0.43 / P $0.50 ｜ ATM IV 105.8%，净 delta 敞口 70k shares
Top ΔOI: C 7 +488
仓位参考: Max Pain 8 ｜ Put Wall 7（+1.5%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 105.8%｜历史 Rank 62%（近端代理）｜IV/RV 0.93×（近似）｜净 delta 敞口 正 69,655 股

12-04（Activity LOW）仓位参考: Max Pain 9 ｜ Put Wall 7（+1.5%，弱）（OI 0.1k）

12-11（MEDIUM △）Top ΔOI: 7P +27
12-11（MEDIUM △）仓位参考: Max Pain 10 ｜ Call Wall 7.5（+8.8%，弱）（OI 97） ｜ Put Wall 7.5（+8.8%，弱）（OI 0.1k）

📅 事件差分（观察，非因果）: 11-20（3D）ATM IV 122.8% vs 11-27 105.8%（差 +17.0pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/USAR_morning.json