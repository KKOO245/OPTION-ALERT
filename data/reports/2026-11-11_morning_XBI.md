# 期权晨报 2026-11-11（快照 10:20 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $nan
VIX 18.31 ↓5.9%（5D +10.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **事件差分**: 11-13 ATM IV 50.9% vs 11-20 37.7%（差 +13.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-20 150P ΔOI +964（距现价 -3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 155.06 → 今开 155.85（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 156.39 ｜ 低 154.73

Options: P/C成交量 14.67 | OI比 1.21 | ATM IV 50.9% | Skew 9.1pp | Term 0.69 | ExpMove ±2.7%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价显著（Skew 9.1pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 14.67）——观察点，非方向信号
   ⇒ Put/Call Volume: 14.67×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.21×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±2.7% ｜ 11-20（9D）±4.5% ｜ 11-27（16D）±6.0% ｜ 12-04（23D）±7.8%
   ⇒ IV–VIX Spread: +32.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 9,426,125 | GEX Change vs 上次快照 1,028,038 | Flip: Primary Flip: 152.73（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 471 / LOW 139 / INVALID 312
结构观察区: Primary Flip 152.73（全链重定价，覆盖 97%）
最近结构参考: Flip 153（现价高于该位 1.7%）
量化视角： 正 Gamma（943万，无历史分位）｜正 Gamma 增强（+103万）｜现价位于 Flip 上方 1.72%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 153（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 150.0P — Vol 1,018 | 最新价 $1.74 | OI 3487→4451 (ΔOI +964张) | ΔOI/Volume 94.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增964张（+27.6% vs前日OI），连续性待观察（方向未知）
11-20 155.0C — Vol 1,019 | 最新价 $3.54 | OI 906→1804 (ΔOI +898张) | ΔOI/Volume 88.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增898张（+99.1% vs前日OI），连续性待观察（方向未知）
11-20 141.0P — Vol 720 | 最新价 $0.44 | OI 863→1357 (ΔOI +494张) | ΔOI/Volume 68.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增494张（+57.2% vs前日OI），连续性待观察（方向未知）
11-20 142.0P — Vol 338 | 最新价 $0.41 | OI 644→854 (ΔOI +210张) | ΔOI/Volume 62.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增210张（+32.6% vs前日OI），连续性待观察（方向未知）
11-13 151.0C — Vol 193 | 最新价 $4.55 | OI 100→242 (ΔOI +142张) | ΔOI/Volume 73.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增142张（+142.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,708 张（Put 1,668 / Call 1,040），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +0.3k / P -0.3k ｜ Activity MEDIUM △ ｜ 2D
11-20  C +0.8k / P +1.8k ｜ Activity HIGH ｜ 9D
11-27  C +14 / P +20 ｜ Activity LOW ｜ 16D
12-04  C +1 / P +2 ｜ Activity LOW ｜ 23D

📆 11-13 Forward Structure
存量OI: C 6.1k / P 7.4k，今日变化ΔOI: C +0.3k / P -0.3k，平值价格ATM: C $2.12 / P $2.11 ｜ ATM IV 50.9%，净 delta 敞口 20k shares
Top ΔOI: P 147 -363 ｜ C 151 +142 ｜ C 160 +115
仓位参考: Max Pain 150 ｜ Call Wall 160（+3.0%，弱）（OI 1.2k） ｜ Put Wall 147（-5.4%，弱）（OI 1.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 50.9%｜历史 Rank 97%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 19,613 股

📆 11-20 Forward Structure
存量OI: C 24.8k / P 56.9k，今日变化ΔOI: C +0.8k / P +1.8k，平值价格ATM: C $3.54 / P $3.52 ｜ ATM IV 37.7%，净 delta 敞口 8k shares
Top ΔOI: P 150 +964 ｜ C 155 +898 ｜ P 141 +494
仓位参考: Max Pain 154 ｜ Call Wall 165（+6.2%）（OI 5.5k） ｜ Put Wall 147（-5.4%，弱）（OI 5.6k）
量化解读： 存量 Put 重｜ATM IV 37.7%｜历史 Rank 97%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 7,652 股

11-27（Activity LOW）仓位参考: Max Pain 158 ｜ Call Wall 152.5（-1.8%，弱）（OI 0.1k） ｜ Put Wall 156（+0.4%）（OI 0.2k）

12-04（Activity LOW）仓位参考: Max Pain 162 ｜ Call Wall 162（+4.3%，弱）（OI 44） ｜ Put Wall 159（+2.3%，弱）（OI 80）

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 50.9% vs 11-20 37.7%（差 +13.2pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/XBI_morning.json