# 期权晨报 2026-10-19（快照 10:20 ET）

📊 市场环境

SPY $766.48 ｜ QQQ $718.36
VIX 18.46 ↓7.7%（5D +21.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 23.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🟡 **近现价集中开仓**: 10-21 83P ΔOI +581（距现价 -4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-23 93C ΔOI +18,371 占该期限总 OI 14.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 87.71 → 今开 87.14（-0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 87.73 ｜ 低 86.47

Options: P/C成交量 0.59 | OI比 0.43 | ATM IV 43.2% | Skew -4.7pp | Term 0.94 | ExpMove ±3.4%（近端） | Rank 66%
量化视角： IV 中性（Rank 66%）｜期限结构正常（Term 0.94）｜Put 保护异常便宜（Skew -4.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.43）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.59×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.43×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-21（2D）±3.4% ｜ 10-23（4D）±4.2% ｜ 10-26（7D）±4.6% ｜ 10-28（9D）±5.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 26,750,031 | GEX Change vs 上次快照 19,748,273 | Flip: Primary Flip: 84.81（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 600 / LOW 135 / INVALID 467
结构观察区: Primary Flip 84.81（全链重定价，覆盖 97%）
最近结构参考: Flip 85（现价高于该位 2.2%）
量化视角： 正 Gamma（2675万，无历史分位）｜正 Gamma 增强（+1975万）｜现价位于 Flip 上方 2.18%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 87（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 85（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 93.0C — Vol 18,431 | 最新价 $0.37 | OI 259→18630 (ΔOI +18371张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18371张（+7093.1% vs前日OI），连续性待观察（方向未知）
10-23 90.0C — Vol 10,660 | 最新价 $0.98 | OI 1249→11421 (ΔOI +10172张) | ΔOI/Volume 95.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10172张（+814.4% vs前日OI），连续性待观察（方向未知）
10-23 92.0C — Vol 10,240 | 最新价 $0.52 | OI 915→10979 (ΔOI +10064张) | ΔOI/Volume 98.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10064张（+1099.9% vs前日OI），连续性待观察（方向未知）
10-23 89.0C — Vol 10,107 | 最新价 $1.27 | OI 312→10198 (ΔOI +9886张) | ΔOI/Volume 97.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9886张（+3168.6% vs前日OI），连续性待观察（方向未知）
10-23 90.5C — Vol 8,345 | 最新价 $0.66 | OI 684→8285 (ΔOI +7601张) | ΔOI/Volume 91.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7601张（+1111.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 56,094 张（Put 0 / Call 56,094），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 4.3k / P 1.9k，今日成交量: C 0.9k / P 0.5k，平值价格ATM: C $0.27 / P $0.60 ｜ ATM IV 43.2%，预期波动 ±1.0%，Max Pain 87
Top ΔOI: C 91 +504 ｜ P 84 +371 ｜ C 90 +353

📆 Forward Expiration Structure

10-21  C +0.3k / P +1.4k ｜ Activity HIGH ｜ 2D
10-23  C +58.4k / P +7.6k ｜ Activity HIGH ｜ 4D
10-26  C +76 / P +0.2k ｜ Activity MEDIUM △ ｜ 7D
10-28  C -11 / P +1.3k ｜ Activity HIGH ｜ 9D

📆 10-21 Forward Structure
存量OI: C 3.5k / P 5.4k，今日变化ΔOI: C +0.3k / P +1.4k，平值价格ATM: C $1.72 / P $1.23 ｜ ATM IV 48.2%，净 delta 敞口 -34k shares
Top ΔOI: P 83 +581 ｜ P 85 +298
仓位参考: Max Pain 87 ｜ Put Wall 83（-4.2%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜ATM IV 48.2%｜历史 Rank 66%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 33,832 股

📆 10-23 Forward Structure
存量OI: C 91.9k / P 32.0k，今日变化ΔOI: C +58.4k / P +7.6k，平值价格ATM: C $2.13 / P $1.48 ｜ ATM IV 42.7%，净 delta 敞口 912k shares
Top ΔOI: C 93 +18,371 ｜ C 90 +10,172 ｜ C 92 +10,064
仓位参考: Max Pain 86 ｜ Call Wall 90（+3.9%，弱）（OI 11.4k） ｜ Put Wall 85（-1.9%，弱）（OI 5.3k）
量化解读： 存量 Call 重｜ATM IV 42.7%｜历史 Rank 66%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 911,853 股

10-26（MEDIUM △）Top ΔOI: 84P +52 ｜ 87C +52
10-26（MEDIUM △）仓位参考: Max Pain 86 ｜ Call Wall 92（+6.2%，弱）（OI 0.4k）

📆 10-28 Forward Structure
存量OI: C 97 / P 1.8k，今日变化ΔOI: C -11 / P +1.3k，平值价格ATM: C $2.58 / P $2.19 ｜ ATM IV 40.9%，净 delta 敞口 -38k shares
Top ΔOI: P 84 +996 ｜ P 82 +225 ｜ P 81 +62
仓位参考: Max Pain 87 ｜ Call Wall 84（-3.1%）（OI 26） ｜ Put Wall 84（-3.1%）（OI 1.0k）
量化解读： 存量 Put 重｜ATM IV 40.9%｜历史 Rank 66%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 负 38,016 股

📅 事件差分（观察，非因果）: 10-21（2D）ATM IV 48.2% vs 10-23 42.7%（差 +5.6pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/GDX_morning.json