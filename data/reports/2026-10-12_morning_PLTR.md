# 期权晨报 2026-10-12（快照 10:20 ET）

📊 市场环境

SPY $778.00 ｜ QQQ $745.76
VIX 15.29 ↑3.0%（5D -1.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 46.0（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.96 ｜ 实际 待公布 ｜ 前值 3.98
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.7 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 10-16 215C ΔOI +12,652（距现价 +3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-23 125P ΔOI +11,134 占该期限总 OI 13.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 209.05 → 今开 208.90（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 212.94 ｜ 低 206.56

Options: P/C成交量 0.53 | OI比 1.09 | ATM IV 46.6% | Skew 2.5pp | Term 1.20 | ExpMove ±4.1%（近端） | Rank 35%
量化视角： IV 中性（Rank 35%）｜期限结构正常偏陡（Term 1.20）｜保护溢价中性（Skew 2.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.09×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（4D）±4.1% ｜ 10-23（11D）±6.0% ｜ 10-30（18D）±7.7% ｜ 11-06（25D）±12.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 85,933,233 | GEX Change vs 上次快照 38,853,841 | Flip: Primary Flip: 184.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 631 / LOW 47 / INVALID 120
结构观察区: Primary Flip 184.92（全链重定价，覆盖 100%）
Call Wall 200（弱结构｜现价高于该位 4.0%）
最近结构参考: Call Wall 200（现价高于该位 4.0%）
量化视角： 正 Gamma（8593万，无历史分位）｜正 Gamma 增强（+3885万）｜现价位于 Flip 上方 12.52%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 175（MaxPain，仅结算参考） / 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 185（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 215.0C — Vol 30,931 | 最新价 $2.53 | OI 3990→16642 (ΔOI +12652张) | ΔOI/Volume 40.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12652张（+317.1% vs前日OI），连续性待观察（方向未知）
10-16 207.5C — Vol 21,080 | 最新价 $5.60 | OI 2314→14493 (ΔOI +12179张) | ΔOI/Volume 57.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12179张（+526.3% vs前日OI），连续性待观察（方向未知）
10-23 125.0P — Vol 11,325 | 最新价 $0.07 | OI 355→11489 (ΔOI +11134张) | ΔOI/Volume 98.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11134张（+3136.3% vs前日OI），连续性待观察（方向未知）
10-16 212.5C — Vol 20,123 | 最新价 $3.38 | OI 1682→10557 (ΔOI +8875张) | ΔOI/Volume 44.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8875张（+527.6% vs前日OI），连续性待观察（方向未知）
10-16 220.0C — Vol 17,695 | 最新价 $1.38 | OI 6392→14174 (ΔOI +7782张) | ΔOI/Volume 44.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7782张（+121.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 52,622 张（Put 11,134 / Call 41,488），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +57.8k / P +34.9k ｜ Activity HIGH ｜ 4D
10-23  C +4.7k / P +22.0k ｜ Activity HIGH ｜ 11D
10-30  C +6.0k / P +10.4k ｜ Activity HIGH ｜ 18D
11-06  C +3.2k / P +1.0k ｜ Activity HIGH ｜ 25D

📆 10-16 Forward Structure
存量OI: C 226.8k / P 247.0k，今日变化ΔOI: C +57.8k / P +34.9k，平值价格ATM: C $4.65 / P $3.80 ｜ ATM IV 46.6%，净 delta 敞口 1.6M shares
Top ΔOI: C 215 +12,652 ｜ C 207 +12,179 ｜ C 212 +8,875
仓位参考: Max Pain 175 ｜ Call Wall 215（+3.3%，弱）（OI 16.6k） ｜ Put Wall 190（-8.7%，弱）（OI 9.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 46.6%｜历史 Rank 35%（近端代理）｜IV/RV 1.80×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,643,491 股

📆 10-23 Forward Structure
存量OI: C 34.6k / P 49.6k，今日变化ΔOI: C +4.7k / P +22.0k，平值价格ATM: C $6.70 / P $5.85 ｜ ATM IV 42.9%，净 delta 敞口 -20k shares
Top ΔOI: P 125 +11,134
仓位参考: Max Pain 188 ｜ Call Wall 200（-3.9%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 42.9%｜历史 Rank 35%（近端代理）｜IV/RV 1.65×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 20,476 股

📆 10-30 Forward Structure
存量OI: C 35.8k / P 32.7k，今日变化ΔOI: C +6.0k / P +10.4k，平值价格ATM: C $8.67 / P $7.42 ｜ ATM IV 43.1%，净 delta 敞口 -9k shares
Top ΔOI: P 202 +3,157 ｜ C 205 +1,208 ｜ P 200 +1,154
仓位参考: Max Pain 192 ｜ Call Wall 205（-1.5%，弱）（OI 2.9k） ｜ Put Wall 202.5（-2.7%，弱）（OI 3.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 43.1%｜历史 Rank 35%（近端代理）｜IV/RV 1.66×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 9,285 股

📆 11-06 Forward Structure
存量OI: C 14.3k / P 13.4k，今日变化ΔOI: C +3.2k / P +1.0k，平值价格ATM: C $13.25 / P $11.80 ｜ ATM IV 58.0%，净 delta 敞口 90k shares
Top ΔOI: C 220 +493 ｜ C 225 +479 ｜ C 240 +327
仓位参考: Max Pain 190 ｜ Call Wall 220（+5.7%，弱）（OI 1.4k） ｜ Put Wall 190（-8.7%）（OI 2.9k）
量化解读： 存量两侧均衡｜ATM IV 58.0%｜历史 Rank 35%（近端代理）｜IV/RV 2.23×（近似）｜净 delta 敞口 正 89,935 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/PLTR_morning.json