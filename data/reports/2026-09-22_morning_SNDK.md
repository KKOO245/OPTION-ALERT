# 期权晨报 2026-09-22（快照 10:20 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $nan
VIX 14.54 ↓2.2%（5D -15.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,766.64 → 今开 1,758.55（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 1909.48 ｜ 低 1758.14

Options: P/C成交量 0.43 | OI比 1.24 | ATM IV 91.2% | Skew -7.8pp | Term 0.86 | ExpMove ±6.9%（近端） | Rank 43%
量化视角： IV 中性（Rank 43%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -7.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.24×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（3D）±6.9% ｜ 10-02（10D）±11.4% ｜ 10-09（17D）±14.0% ｜ 10-16（24D）±16.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 11,015,932 | GEX Change vs 上次快照 4,387,241 | Flip: Primary Flip: 1681.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1965 / LOW 360 / INVALID 819
结构观察区: Primary Flip 1681.52（全链重定价，覆盖 100%）
Call Wall 2,000（弱结构｜现价低于该位 4.9%）
最近结构参考: Call Wall 2000（现价低于该位 4.9%）
量化视角： 正 Gamma（1102万，无历史分位）｜正 Gamma 增强（+439万）｜现价位于 Flip 上方 13.08%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,700（MaxPain，仅结算参考）；上方 2,000（Call Wall，弱结构）。
• Gamma 区域：切换参考 1682（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 2000.0C — Vol 8,347 | 最新价 $6.40 | OI 1216→3675 (ΔOI +2459张) | ΔOI/Volume 29.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2459张（+202.2% vs前日OI），连续性待观察（方向未知）
09-25 1700.0P — Vol 3,206 | 最新价 $27.00 | OI 1049→2037 (ΔOI +988张) | ΔOI/Volume 30.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增988张（+94.2% vs前日OI），连续性待观察（方向未知）
09-25 1800.0C — Vol 7,294 | 最新价 $40.90 | OI 1767→2631 (ΔOI +864张) | ΔOI/Volume 11.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增864张（+48.9% vs前日OI），连续性待观察（方向未知）
09-25 2050.0C — Vol 889 | 最新价 $4.10 | OI 246→823 (ΔOI +577张) | ΔOI/Volume 64.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增577张（+234.6% vs前日OI），连续性待观察（方向未知）
09-25 2010.0C — Vol 785 | 最新价 $6.04 | OI 369→909 (ΔOI +540张) | ΔOI/Volume 68.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增540张（+146.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,428 张（Put 988 / Call 4,440），跨 1 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +10.2k / P +9.8k ｜ Activity HIGH ｜ 3D
10-02  C +2.2k / P +2.0k ｜ Activity HIGH ｜ 10D
10-09  C +0.7k / P +1.1k ｜ Activity HIGH ｜ 17D
10-16  C +1.9k / P +1.7k ｜ Activity HIGH ｜ 24D

📆 09-25 Forward Structure
存量OI: C 39.4k / P 48.9k，今日变化ΔOI: C +10.2k / P +9.8k，平值价格ATM: C $63.50 / P $67.70 ｜ ATM IV 91.2%，净 delta 敞口 307k shares
Top ΔOI: C 2000 +2,459 ｜ P 1700 +988 ｜ C 1800 +864
仓位参考: Max Pain 1,700 ｜ Call Wall 2000（+5.2%，弱）（OI 3.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 91.2%｜历史 Rank 43%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 306,548 股

📆 10-02 Forward Structure
存量OI: C 19.7k / P 14.8k，今日变化ΔOI: C +2.2k / P +2.0k，平值价格ATM: C $104.40 / P $111.54 ｜ ATM IV 85.7%，净 delta 敞口 63k shares
Top ΔOI: C 2250 +382 ｜ C 2000 +313
仓位参考: Max Pain 1,600 ｜ Call Wall 2000（+5.2%，弱）（OI 1.0k） ｜ Put Wall 1800（-5.3%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 85.7%｜历史 Rank 43%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 62,976 股

📆 10-09 Forward Structure
存量OI: C 6.6k / P 5.8k，今日变化ΔOI: C +0.7k / P +1.1k，平值价格ATM: C $133.71 / P $132.00 ｜ ATM IV 81.5%，净 delta 敞口 26k shares
Top ΔOI: P 1430 +104 ｜ C 1770 +85
仓位参考: Max Pain 1,500
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 81.5%｜历史 Rank 43%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 26,344 股

📆 10-16 Forward Structure
存量OI: C 32.5k / P 41.5k，今日变化ΔOI: C +1.9k / P +1.7k，平值价格ATM: C $154.27 / P $154.00 ｜ ATM IV 79.4%，净 delta 敞口 40k shares
Top ΔOI: C 2000 +527 ｜ C 2100 +308 ｜ P 1160 -255
仓位参考: Max Pain 1,610 ｜ Call Wall 2000（+5.2%，弱）（OI 2.1k） ｜ Put Wall 1800（-5.3%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 79.4%｜历史 Rank 43%（近端代理）｜IV/RV 1.16×（近似）｜净 delta 敞口 正 39,578 股

📅 事件差分（观察，非因果）: 09-25（3D）ATM IV 91.2% vs 10-02 85.7%（差 +5.5pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/SNDK_morning.json