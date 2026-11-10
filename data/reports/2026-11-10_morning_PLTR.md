# 期权晨报 2026-11-10（快照 10:20 ET）

📊 市场环境

SPY $751.28 ｜ QQQ $676.84
VIX 19.85 ↓0.3%（5D -4.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 165P ΔOI +2,335（距现价 -1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 169.20 → 今开 168.20（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 169.34 ｜ 低 165.60

Options: P/C成交量 0.93 | OI比 0.64 | ATM IV 60.7% | Skew 6.2pp | Term 0.83 | ExpMove ±4.6%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价显著（Skew 6.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.93×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（3D）±4.6% ｜ 11-20（10D）±7.4% ｜ 11-27（17D）±8.9% ｜ 12-04（24D）±11.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 37,347,466 | GEX Change vs 上次快照 5,320,121 | Flip: Primary Flip: 159.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 546 / LOW 170 / INVALID 218
结构观察区: Primary Flip 159.03（全链重定价，覆盖 99%）
Call Wall 165（弱结构｜现价高于该位 2.0%）
最近结构参考: Call Wall 165（现价高于该位 2.0%）
量化视角： 正 Gamma（3735万，无历史分位）｜正 Gamma 增强（+532万）｜现价位于 Flip 上方 5.81%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 162（MaxPain，仅结算参考） / 165（Call Wall，弱结构）。
• Gamma 区域：切换参考 159（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 185.0C — Vol 12,331 | 最新价 $0.33 | OI 1676→11775 (ΔOI +10099张) | ΔOI/Volume 81.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10099张（+602.6% vs前日OI），连续性待观察（方向未知）
11-13 182.5C — Vol 12,145 | 最新价 $0.51 | OI 1466→10377 (ΔOI +8911张) | ΔOI/Volume 73.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8911张（+607.8% vs前日OI），连续性待观察（方向未知）
11-13 165.0P — Vol 6,145 | 最新价 $2.55 | OI 1856→4191 (ΔOI +2335张) | ΔOI/Volume 38.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2335张（+125.8% vs前日OI），连续性待观察（方向未知）
11-20 115.0P — Vol 3,082 | 最新价 $0.13 | OI 4581→6653 (ΔOI +2072张) | ΔOI/Volume 67.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2072张（+45.2% vs前日OI），连续性待观察（方向未知）
11-13 150.0P — Vol 4,206 | 最新价 $0.32 | OI 2990→4962 (ΔOI +1972张) | ΔOI/Volume 46.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1972张（+66.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 25,389 张（Put 6,379 / Call 19,010），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +27.4k / P +7.8k ｜ Activity HIGH ｜ 3D
11-20  C -6.8k / P +7.4k ｜ Activity MEDIUM △ ｜ 10D
11-27  C +0.4k / P +0.4k ｜ Activity LOW ｜ 17D
12-04  C +1.0k / P +0.6k ｜ Activity MEDIUM △ ｜ 24D

📆 11-13 Forward Structure
存量OI: C 133.3k / P 84.8k，今日变化ΔOI: C +27.4k / P +7.8k，平值价格ATM: C $4.10 / P $3.60 ｜ ATM IV 60.7%，净 delta 敞口 159k shares
Top ΔOI: C 185 +10,099 ｜ C 182 +8,911 ｜ P 165 +2,335
仓位参考: Max Pain 162 ｜ Call Wall 165（-1.9%，弱）（OI 14.2k） ｜ Put Wall 165（-1.9%，弱）（OI 4.2k）
量化解读： 存量 Call 重｜ATM IV 60.7%｜历史 Rank 81%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 159,444 股

11-20（MEDIUM △）Top ΔOI: 165C -5,555 ｜ 165P -1,766
11-20（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 180（+7.0%，弱）（OI 10.4k） ｜ Put Wall 185（+9.9%，弱）（OI 9.9k）

11-27（Activity LOW）仓位参考: Max Pain 178 ｜ Call Wall 180（+7.0%，弱）（OI 0.9k） ｜ Put Wall 160（-4.9%，弱）（OI 1.3k）

12-04（MEDIUM △）Top ΔOI: 185C +477 ｜ 175P +156
12-04（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 185（+9.9%，弱）（OI 1.0k） ｜ Put Wall 155（-7.9%，弱）（OI 0.8k）

📅 事件差分（观察，非因果）: 11-13（3D）ATM IV 60.7% vs 11-20 55.1%（差 +5.5pp）——覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/PLTR_morning.json