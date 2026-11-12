# 期权晨报 2026-11-12（快照 10:20 ET）

📊 市场环境

SPY $756.94 ｜ QQQ $685.78
VIX 18.45 ↑5.5%（5D -34.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **事件差分**: 11-13（1D）ATM IV 84.9% vs 11-16 68.8%（差 +16.2pp），覆盖 成屋销售、PPI 生产者物价 MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-13 139C ΔOI +4,691（距现价 -3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-16 160C ΔOI +7,041 占该期限总 OI 13.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 139.75 → 今开 137.89（-1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 147.58 ｜ 低 137.75

Options: P/C成交量 0.54 | OI比 0.74 | ATM IV 84.9% | Skew -1.1pp | Term 0.70 | ExpMove ±4.0%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±4.0% ｜ 11-16（4D）±6.1% ｜ 11-18（6D）±7.6% ｜ 11-20（8D）±8.6%
   ⇒ IV–VIX Spread: +66.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 75,315,966 | GEX Change vs 上次快照 56,195,213 | Flip: Primary Flip: 137.75（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 928 / LOW 174 / INVALID 502
结构观察区: Primary Flip 137.75（全链重定价，覆盖 100%）
Put Wall 135（弱结构｜现价高于该位 6.3%）
最近结构参考: Flip 138（现价高于该位 4.2%）
量化视角： 正 Gamma（7532万，无历史分位）｜正 Gamma 增强（+5620万）｜现价位于 Flip 上方 4.18%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（Put Wall，弱结构） / 140（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 138（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 170.0C — Vol 39,785 | 最新价 $0.62 | OI 4399→43359 (ΔOI +38960张) | ΔOI/Volume 97.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增38960张（+885.7% vs前日OI），连续性待观察（方向未知）
11-16 160.0C — Vol 8,400 | 最新价 $0.29 | OI 1613→8654 (ΔOI +7041张) | ΔOI/Volume 83.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7041张（+436.5% vs前日OI），连续性待观察（方向未知）
11-13 139.0C — Vol 17,271 | 最新价 $3.59 | OI 949→5640 (ΔOI +4691张) | ΔOI/Volume 27.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4691张（+494.3% vs前日OI），连续性待观察（方向未知）
11-13 134.0P — Vol 6,475 | 最新价 $1.11 | OI 1500→5164 (ΔOI +3664张) | ΔOI/Volume 56.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3664张（+244.3% vs前日OI），连续性待观察（方向未知）
11-16 155.0C — Vol 5,305 | 最新价 $0.58 | OI 885→3780 (ΔOI +2895张) | ΔOI/Volume 54.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2895张（+327.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 57,251 张（Put 3,664 / Call 53,587），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +19.5k / P +14.4k ｜ Activity HIGH ｜ 1D
11-16  C +25.1k / P +4.0k ｜ Activity HIGH ｜ 4D
11-18  C +3.2k / P +3.0k ｜ Activity HIGH ｜ 6D
11-20  C -15.8k / P +1.1k ｜ Activity MEDIUM △ ｜ 8D

📆 11-13 Forward Structure
存量OI: C 214.2k / P 158.5k，今日变化ΔOI: C +19.5k / P +14.4k，平值价格ATM: C $3.50 / P $2.31 ｜ ATM IV 84.9%，净 delta 敞口 691k shares
Top ΔOI: C 139 +4,691 ｜ P 134 +3,664 ｜ P 143 +2,617
仓位参考: Max Pain 140 ｜ Call Wall 157.5（+9.8%，弱）（OI 26.9k） ｜ Put Wall 135（-5.9%，弱）（OI 8.2k）
量化解读： 存量 Call 重｜ATM IV 84.9%｜历史 Rank 91%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 691,128 股

📆 11-16 Forward Structure
存量OI: C 43.0k / P 8.9k，今日变化ΔOI: C +25.1k / P +4.0k，平值价格ATM: C $4.85 / P $3.90 ｜ ATM IV 68.8%，净 delta 敞口 324k shares
Top ΔOI: C 160 +7,041 ｜ C 155 +2,895 ｜ C 162 +2,822
仓位参考: Max Pain 140 ｜ Call Wall 150（+4.5%，弱）（OI 5.1k） ｜ Put Wall 140（-2.4%）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 68.8%｜历史 Rank 91%（近端代理）｜IV/RV 0.91×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 323,519 股

📆 11-18 Forward Structure
存量OI: C 10.9k / P 15.3k，今日变化ΔOI: C +3.2k / P +3.0k，平值价格ATM: C $5.60 / P $5.30 ｜ ATM IV 72.8%，净 delta 敞口 26k shares
Top ΔOI: P 135 +888 ｜ C 150 +410
仓位参考: Max Pain 140 ｜ Call Wall 145（+1.0%，弱）（OI 1.1k） ｜ Put Wall 135（-5.9%）（OI 9.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 72.8%｜历史 Rank 91%（近端代理）｜IV/RV 0.97×（近似）｜净 delta 敞口 正 25,562 股

11-20（MEDIUM △）Top ΔOI: 160C -16,892 ｜ 115P -2,208
11-20（MEDIUM △）仓位参考: Max Pain 145 ｜ Call Wall 145（+1.0%，弱）（OI 40.8k） ｜ Put Wall 130（-9.4%，弱）（OI 34.5k）

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 84.9% vs 11-16 68.8%（差 +16.2pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/SPCX_morning.json