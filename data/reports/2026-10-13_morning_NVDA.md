# 期权晨报 2026-10-13（快照 10:20 ET）

📊 市场环境

SPY $777.22 ｜ QQQ $743.44
VIX 15.31 ↑0.7%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 46.0（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.95 ｜ 实际 3.99 ｜ 前值 3.93　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-14 225C ΔOI +10,584（距现价 -0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-14 242C ΔOI +34,141 占该期限总 OI 14.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 226.32 → 今开 224.27（-0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 226.60 ｜ 低 223.06

Options: P/C成交量 0.92 | OI比 0.90 | ATM IV 38.2% | Skew 2.3pp | Term 0.82 | ExpMove ±1.8%（近端） | Rank 33%
量化视角： IV 中性（Rank 33%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价中性（Skew 2.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.92×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-14（1D）±1.8% ｜ 10-16（3D）±2.8% ｜ 10-19（6D）±3.2% ｜ 10-21（8D）±3.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 306,167,534 | GEX Change vs 上次快照 28,049,012 | Flip: Primary Flip: 217.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 668 / LOW 180 / INVALID 690
结构观察区: Primary Flip 217.38（全链重定价，覆盖 98%）
Call Wall 240（弱结构｜现价低于该位 5.8%）
最近结构参考: Flip 217（现价高于该位 4.0%）
量化视角： 正 Gamma（3.06亿，无历史分位）｜正 Gamma 增强（+2805万）｜现价位于 Flip 上方 3.96%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 225（MaxPain，仅结算参考）；上方 240（Call Wall，弱结构）。
• Gamma 区域：切换参考 217（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-14 242.5C — Vol 139,205 | 最新价 $0.02 | OI 1882→36023 (ΔOI +34141张) | ΔOI/Volume 24.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增34141张（+1814.1% vs前日OI），连续性待观察（方向未知）
10-14 225.0C — Vol 21,356 | 最新价 $3.12 | OI 369→10953 (ΔOI +10584张) | ΔOI/Volume 49.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10584张（+2868.3% vs前日OI），连续性待观察（方向未知）
10-14 202.5P — Vol 15,008 | 最新价 $0.08 | OI 720→9334 (ΔOI +8614张) | ΔOI/Volume 57.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8614张（+1196.4% vs前日OI），连续性待观察（方向未知）
10-14 232.5C — Vol 20,238 | 最新价 $0.42 | OI 2799→9470 (ΔOI +6671张) | ΔOI/Volume 33.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6671张（+238.3% vs前日OI），连续性待观察（方向未知）
10-16 232.5C — Vol 24,892 | 最新价 $1.08 | OI 39819→46403 (ΔOI +6584张) | ΔOI/Volume 26.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6584张（+16.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 66,594 张（Put 8,614 / Call 57,980），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-14  C +74.8k / P +72.7k ｜ Activity HIGH ｜ 1D
10-16  C +21.1k / P +12.2k ｜ Activity HIGH ｜ 3D
10-19  C +6.9k / P +8.8k ｜ Activity HIGH ｜ 6D
10-21  C +3.2k / P +4.1k ｜ Activity HIGH ｜ 8D

📆 10-14 Forward Structure
存量OI: C 122.8k / P 110.2k，今日变化ΔOI: C +74.8k / P +72.7k，平值价格ATM: C $2.49 / P $1.61 ｜ ATM IV 38.2%，净 delta 敞口 719k shares
Top ΔOI: C 242 +34,141 ｜ C 225 +10,584
仓位参考: Max Pain 225 ｜ Call Wall 242.5（+7.3%）（OI 36.0k） ｜ Put Wall 225（-0.4%，弱）（OI 8.1k）
量化解读： 存量两侧均衡｜ATM IV 38.2%｜历史 Rank 33%（近端代理）｜IV/RV 1.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 719,376 股

📆 10-16 Forward Structure
存量OI: C 1043.2k / P 816.7k，今日变化ΔOI: C +21.1k / P +12.2k，平值价格ATM: C $3.70 / P $2.64 ｜ ATM IV 36.9%，净 delta 敞口 514k shares
Top ΔOI: C 232 +6,584 ｜ P 220 +4,674
仓位参考: Max Pain 220 ｜ Call Wall 220（-2.7%，弱）（OI 99.2k） ｜ Put Wall 220（-2.7%，弱）（OI 64.6k）
量化解读： 存量 Call 重｜ATM IV 36.9%｜历史 Rank 33%（近端代理）｜IV/RV 1.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 513,621 股

📆 10-19 Forward Structure
存量OI: C 37.3k / P 14.9k，今日变化ΔOI: C +6.9k / P +8.8k，平值价格ATM: C $4.10 / P $3.09 ｜ ATM IV 30.2%，净 delta 敞口 -165k shares
Top ΔOI: P 230 +3,619 ｜ C 240 +1,279 ｜ C 230 +840
仓位参考: Max Pain 230 ｜ Call Wall 247.5（+9.5%，弱）（OI 8.9k） ｜ Put Wall 230（+1.8%）（OI 4.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 30.2%｜历史 Rank 33%（近端代理）｜IV/RV 1.51×（近似）｜净 delta 敞口 负 164,957 股

📆 10-21 Forward Structure
存量OI: C 9.9k / P 6.5k，今日变化ΔOI: C +3.2k / P +4.1k，平值价格ATM: C $4.85 / P $3.70 ｜ ATM IV 31.6%，净 delta 敞口 -32k shares
Top ΔOI: P 225 +1,551 ｜ C 235 +950 ｜ P 205 +855
仓位参考: Max Pain 230 ｜ Call Wall 240（+6.2%）（OI 3.7k） ｜ Put Wall 225（-0.4%）（OI 1.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 31.6%｜历史 Rank 33%（近端代理）｜IV/RV 1.58×（近似）｜净 delta 敞口 负 31,892 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/NVDA_morning.json