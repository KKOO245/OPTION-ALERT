# 期权晨报 2026-11-16（快照 10:20 ET）

📊 市场环境

SPY $740.36 ｜ QQQ $661.75
VIX 21.57 ↑11.8%（5D +8.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.8
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **事件差分**: 11-20（4D）ATM IV 90.6% vs 11-27 74.4%（差 +16.2pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 127.64 → 今开 119.31（-6.5%） | 较昨收变动（含盘初走势） ｜ 今日高 122.98 ｜ 低 118.40

Options: P/C成交量 0.34 | OI比 0.46 | ATM IV 90.6% | Skew 4.3pp | Term 0.82 | ExpMove ±7.8%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价中性（Skew 4.3pp）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（4D）±7.8% ｜ 11-27（11D）±8.8% ｜ 12-04（18D）±5.8% ｜ 12-11（25D）±16.0%
   ⇒ IV–VIX Spread: +69.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,270,929 | GEX Change vs 上次快照 1,962,746 | Flip: Primary Flip: 121.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 336 / LOW 189 / INVALID 383
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 121.53（全链重定价，覆盖 100%）
Put Wall 110（现价高于该位 9.6%）
最近结构参考: Flip 122（现价低于该位 0.8%）
量化视角： 负 Gamma（127万，无历史分位）｜负 Gamma 缓解（+196万）｜现价位于 Flip 下方 0.77%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 110（Put Wall）；上方 134（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 122（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 131.0C — Vol 7,263 | 最新价 $3.68 | OI 41→7135 (ΔOI +7094张) | ΔOI/Volume 97.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7094张（+17302.4% vs前日OI），连续性待观察（方向未知）
11-20 136.0C — Vol 7,402 | 最新价 $1.90 | OI 548→7633 (ΔOI +7085张) | ΔOI/Volume 95.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7085张（+1292.9% vs前日OI），连续性待观察（方向未知）
11-20 133.0C — Vol 3,466 | 最新价 $2.75 | OI 44→3423 (ΔOI +3379张) | ΔOI/Volume 97.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3379张（+7679.6% vs前日OI），连续性待观察（方向未知）
11-20 138.0C — Vol 3,229 | 最新价 $1.45 | OI 173→3171 (ΔOI +2998张) | ΔOI/Volume 92.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2998张（+1733.0% vs前日OI），连续性待观察（方向未知）
11-20 137.0C — Vol 3,159 | 最新价 $1.84 | OI 370→3358 (ΔOI +2988张) | ΔOI/Volume 94.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2988张（+807.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 23,544 张（Put 0 / Call 23,544），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +29.1k / P +2.4k ｜ Activity HIGH ｜ 4D
11-27  C +0.7k / P +0.9k ｜ Activity HIGH ｜ 11D
12-04  C +0.6k / P +0.9k ｜ Activity MEDIUM △ ｜ 18D
12-11  C +0.2k / P +0.2k ｜ Activity HIGH ｜ 25D

📆 11-20 Forward Structure
存量OI: C 133.7k / P 61.4k，今日变化ΔOI: C +29.1k / P +2.4k，平值价格ATM: C $4.48 / P $4.95 ｜ ATM IV 90.6%，净 delta 敞口 259k shares
Top ΔOI: C 131 +7,094 ｜ C 136 +7,085 ｜ C 133 +3,379
仓位参考: Max Pain 134 ｜ Call Wall 131（+8.6%，弱）（OI 7.1k） ｜ Put Wall 120（-0.5%，弱）（OI 6.6k）
量化解读： 存量 Call 重｜ATM IV 90.6%｜历史 Rank 80%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 259,061 股

📆 11-27 Forward Structure
存量OI: C 7.8k / P 9.3k，今日变化ΔOI: C +0.7k / P +0.9k，平值价格ATM: C $7.20 / P $3.40 ｜ ATM IV 74.4%，净 delta 敞口 -17k shares
Top ΔOI: P 110 +111
仓位参考: Max Pain 138 ｜ Call Wall 130（+7.8%，弱）（OI 0.3k） ｜ Put Wall 120（-0.5%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜ATM IV 74.4%｜历史 Rank 80%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 负 17,130 股

12-04（MEDIUM △）Top ΔOI: 135P +595 ｜ 110P +257
12-04（MEDIUM △）仓位参考: Max Pain 140 ｜ Put Wall 125（+3.7%，弱）（OI 0.6k）

📆 12-11 Forward Structure
存量OI: C 2.1k / P 2.7k，今日变化ΔOI: C +0.2k / P +0.2k，平值价格ATM: C $10.60 / P $8.70 ｜ ATM IV 74.9%，净 delta 敞口 -2k shares
Top ΔOI: C 130 +74 ｜ P 125 +47
仓位参考: Max Pain 135 ｜ Call Wall 130（+7.8%，弱）（OI 0.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 74.9%｜历史 Rank 80%（近端代理）｜IV/RV 1.10×（近似）｜净 delta 敞口 负 2,071 股

📅 事件差分（观察，非因果）: 11-20（4D）ATM IV 90.6% vs 11-27 74.4%（差 +16.2pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/COIN_morning.json