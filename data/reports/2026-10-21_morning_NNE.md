# 期权晨报 2026-10-21（快照 10:20 ET）

📊 市场环境

SPY $772.65 ｜ QQQ $726.26
VIX 17.20 ↓0.6%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 13C ΔOI +139（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 12.96 → 今开 13.48（+4.0%） | 较昨收变动（含盘初走势） ｜ 今日高 13.50 ｜ 低 13.04

Options: P/C成交量 0.26 | OI比 0.23 | ATM IV 84.9% | Skew 3.9pp | Term 0.86 | ExpMove ±7.1%（近端） | Rank 18%
量化视角： IV 历史低位（Rank 18%，期权偏便宜）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价中性（Skew 3.9pp）｜存量 Call 偏重（OI比 0.23）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.26×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.23×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（2D）±7.1% ｜ 10-30（9D）±9.9% ｜ 11-06（16D）±14.1% ｜ 11-13（23D）±17.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 929,515 | GEX Change vs 上次快照 287,281 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 173 / LOW 88 / INVALID 141
结构观察区: NO_CROSS
Put Wall 14（现价低于该位 6.0%）
最近结构参考: Put Wall 14（现价低于该位 6.0%）
量化视角： 正 Gamma（93万，无历史分位）｜正 Gamma 增强（+29万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（Put Wall） / 14（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 13.5C — Vol 168 | 最新价 $0.17 | OI 498→637 (ΔOI +139张) | ΔOI/Volume 82.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增139张（+27.9% vs前日OI），连续性待观察（方向未知）
10-23 14.0C — Vol 110 | 最新价 $0.10 | OI 426→525 (ΔOI +99张) | ΔOI/Volume 90.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增99张（+23.2% vs前日OI），连续性待观察（方向未知）
11-20 19.0C — Vol 80 | 最新价 $0.10 | OI 666→746 (ΔOI +80张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增80张（+12.0% vs前日OI），连续性待观察（方向未知）
11-13 16.0C — Vol 50 | 最新价 $0.20 | OI 11→61 (ΔOI +50张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增50张（+454.6% vs前日OI），连续性待观察（方向未知）
11-20 10.0P — Vol 40 | 最新价 $0.19 | OI 26→60 (ΔOI +34张) | ΔOI/Volume 85.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增34张（+130.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 402 张（Put 34 / Call 368），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +0.3k / P -0.2k ｜ Activity MEDIUM △ ｜ 2D
10-30  C +77 / P +10 ｜ Activity MEDIUM △ ｜ 9D
11-06  C +12 / P -2 ｜ Activity MEDIUM △ ｜ 16D
11-13  C +50 / P -27 ｜ Activity HIGH ｜ 23D

📆 10-23 Forward Structure
存量OI: C 6.8k / P 1.6k，今日变化ΔOI: C +0.3k / P -0.2k，平值价格ATM: C $0.40 / P $0.53 ｜ ATM IV 84.9%，净 delta 敞口 25k shares
Top ΔOI: C 13 +139 ｜ C 14 +99
仓位参考: Max Pain 14 ｜ Put Wall 14（+6.4%）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 84.9%｜历史 Rank 18%（近端代理）｜IV/RV 1.48×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 24,790 股

10-30（MEDIUM △）Top ΔOI: 14C +21 ｜ 12P +14
10-30（MEDIUM △）仓位参考: Max Pain 14 ｜ Put Wall 14（+6.4%）（OI 0.4k）

11-06（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 13（-1.2%，弱）（OI 77）

📆 11-13 Forward Structure
存量OI: C 0.7k / P 0.4k，今日变化ΔOI: C +50 / P -27，平值价格ATM: C $1.28 / P $1.00 ｜ ATM IV 75.6%，净 delta 敞口 2k shares
Top ΔOI: P 12 -41 ｜ P 12 +5
仓位参考: Max Pain 14 ｜ Call Wall 13.5（+2.6%，弱）（OI 50） ｜ Put Wall 13（-1.2%，弱）（OI 71）
量化解读： 存量 Call 重｜ATM IV 75.6%｜历史 Rank 18%（近端代理）｜IV/RV 1.32×（近似）｜净 delta 敞口 正 1,711 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/NNE_morning.json