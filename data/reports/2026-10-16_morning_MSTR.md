# 期权晨报 2026-10-16（快照 10:20 ET）

📊 市场环境

SPY $771.51 ｜ QQQ $721.45
VIX 15.93 ↓3.2%（5D +7.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔵 **期限 OI 集中**: 11-13 80P ΔOI +3,899 占该期限总 OI 14.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 151.29 → 今开 146.14（-3.4%） | 较昨收变动（含盘初走势） ｜ 今日高 146.83 ｜ 低 143.04

Options: P/C成交量 0.53 | OI比 0.76 | ATM IV 96.9% | Skew -1.4pp | Term 0.70 | ExpMove ±7.2%（近端） | Rank 77%
量化视角： IV 历史高位（Rank 77%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.76）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（7D）±7.2% ｜ 10-30（14D）±10.7% ｜ 11-06（21D）±13.8% ｜ 11-13（28D）±15.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 10,409,756 | GEX Change vs 上次快照 -43,762,507 | Flip: Primary Flip: 142.98（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 555 / LOW 113 / INVALID 216
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 142.98（全链重定价，覆盖 95%）
Call Wall 135（弱结构｜现价高于该位 7.3%）
最近结构参考: Flip 143（现价高于该位 1.3%）
量化视角： 正 Gamma（1041万，无历史分位）｜正 Gamma 减弱（4376万）｜现价位于 Flip 上方 1.28%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（MaxPain，仅结算参考） / 135（Call Wall，弱结构）。
• Gamma 区域：切换参考 143（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 152.5C — Vol 11,117 | 最新价 $5.85 | OI 677→10556 (ΔOI +9879张) | ΔOI/Volume 88.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9879张（+1459.2% vs前日OI），连续性待观察（方向未知）
10-23 155.0C — Vol 11,825 | 最新价 $4.75 | OI 1881→11131 (ΔOI +9250张) | ΔOI/Volume 78.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9250张（+491.8% vs前日OI），连续性待观察（方向未知）
10-23 160.0C — Vol 12,428 | 最新价 $3.16 | OI 3022→12018 (ΔOI +8996张) | ΔOI/Volume 72.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8996张（+297.7% vs前日OI），连续性待观察（方向未知）
10-23 162.5C — Vol 7,411 | 最新价 $2.63 | OI 2217→7302 (ΔOI +5085张) | ΔOI/Volume 68.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5085张（+229.4% vs前日OI），连续性待观察（方向未知）
10-23 157.5C — Vol 7,709 | 最新价 $3.90 | OI 2059→6366 (ΔOI +4307张) | ΔOI/Volume 55.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4307张（+209.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 37,517 张（Put 0 / Call 37,517），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 295.2k / P 223.4k，今日成交量: C 38.5k / P 20.3k，平值价格ATM: C $1.62 / P $1.43 ｜ ATM IV 96.9%，预期波动 ±2.1%，Max Pain 140
Top ΔOI: C 157 -18,957 ｜ C 162 -10,368 ｜ C 165 -8,044

📆 Forward Expiration Structure

10-23  C +44.5k / P +15.0k ｜ Activity HIGH ｜ 7D
10-30  C +5.1k / P +5.2k ｜ Activity MEDIUM △ ｜ 14D
11-06  C +0.7k / P +2.7k ｜ Activity MEDIUM △ ｜ 21D
11-13  C +0.8k / P +6.3k ｜ Activity HIGH ｜ 28D

📆 10-23 Forward Structure
存量OI: C 95.0k / P 123.5k，今日变化ΔOI: C +44.5k / P +15.0k，平值价格ATM: C $5.10 / P $5.25 ｜ ATM IV 63.6%，净 delta 敞口 845k shares
Top ΔOI: C 152 +9,879 ｜ C 155 +9,250 ｜ C 160 +8,996
仓位参考: Max Pain 152 ｜ Call Wall 155（+7.0%，弱）（OI 11.1k） ｜ Put Wall 150（+3.6%，弱）（OI 5.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 63.6%｜历史 Rank 77%（近端代理）｜IV/RV 1.36×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 845,037 股

10-30（MEDIUM △）Top ΔOI: 190C +1,708
10-30（MEDIUM △）仓位参考: Max Pain 158 ｜ Call Wall 155（+7.0%，弱）（OI 1.5k） ｜ Put Wall 155（+7.0%，弱）（OI 3.8k）

11-06（MEDIUM △）Top ΔOI: 115P +552
11-06（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 155（+7.0%，弱）（OI 0.7k） ｜ Put Wall 155（+7.0%，弱）（OI 3.0k）

📆 11-13 Forward Structure
存量OI: C 9.7k / P 17.2k，今日变化ΔOI: C +0.8k / P +6.3k，平值价格ATM: C $11.55 / P $10.89 ｜ ATM IV 68.0%，净 delta 敞口 -51k shares
Top ΔOI: P 80 +3,899 ｜ P 110 +408
仓位参考: Max Pain 165 ｜ Put Wall 155（+7.0%，弱）（OI 1.7k）
量化解读： 存量 Put 重｜ATM IV 68.0%｜历史 Rank 77%（近端代理）｜IV/RV 1.45×（近似）｜净 delta 敞口 负 51,471 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/MSTR_morning.json