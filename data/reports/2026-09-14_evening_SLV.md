# 期权晚报 2026-09-14（快照 16:48 ET）

📊 市场环境

SPY $760.88 ｜ QQQ $709.18
VIX 17.10 ↑8.0%（5D +11.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.9 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: -2.2%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 56.84 → 收盘 56.84（+0.0%） ｜ 今日高 57.68 ｜ 低 56.65 ｜ 昨收 58.12 → 收盘 56.84（-2.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.52 | OI比 0.57 | ATM IV 30.2% | Skew -16.6pp | Term 1.41 | ExpMove ±2.8%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构正常偏陡（Term 1.41）｜Put 保护异常便宜（Skew -16.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.57）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.57×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-16（2D）±2.8% ｜ 09-18（4D）±4.1% ｜ 09-21（7D）±4.5% ｜ 09-23（9D）±5.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 13,565,145 | GEX Change vs 上次快照 1,523,315 | Flip: Primary Flip: 56.32（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 860 / LOW 198 / INVALID 616
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 56.32（全链重定价，覆盖 99%）
最近结构参考: Flip 56（现价高于该位 0.9%）
量化视角： 正 Gamma（1357万，无历史分位）｜正 Gamma 增强（+152万）｜现价位于 Flip 上方 0.92%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 59（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 56（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 64.0C — Vol 12,399 | 最新价 $0.94 | OI 44281→56350 (ΔOI +12069张) | ΔOI/Volume 97.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12069张（+27.3% vs前日OI），连续性待观察（方向未知）
09-16 70.0C — Vol 380 | 最新价 $0.01 | OI 228→5367 (ΔOI +5139张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5139张（+2253.9% vs前日OI），连续性待观察（方向未知）
09-16 56.0P — Vol 1,161 | 最新价 $0.43 | OI 363→3785 (ΔOI +3422张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3422张（+942.7% vs前日OI），连续性待观察（方向未知）
09-16 55.0P — Vol 1,529 | 最新价 $0.18 | OI 269→3563 (ΔOI +3294张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3294张（+1224.5% vs前日OI），连续性待观察（方向未知）
09-18 62.0C — Vol 1,313 | 最新价 $0.14 | OI 15092→18046 (ΔOI +2954张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增2954张（+19.6% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 26,878 张（Put 6,716 / Call 20,162），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-16  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-21  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-23  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 09-16 Forward Structure
存量OI: C 14.5k / P 17.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.74 / P $0.85 ｜ ATM IV 48.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 59 ｜ Put Wall 58（+2.0%，弱）（OI 5.0k）
量化解读： 存量 Put 重｜ATM IV 48.0%｜历史 Rank 40%（近端代理）｜IV/RV 1.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-18（Activity LOW）仓位参考: Max Pain 60 ｜ Call Wall 60（+5.6%，弱）（OI 41.7k） ｜ Put Wall 55（-3.2%，弱）（OI 21.2k）

09-21（Activity LOW）仓位参考: Max Pain 58 ｜ Call Wall 58（+2.0%，弱）（OI 0.5k） ｜ Put Wall 59（+3.8%，弱）（OI 0.3k）

09-23（Activity LOW）仓位参考: Max Pain 60 ｜ Call Wall 58（+2.0%，弱）（OI 0.2k） ｜ Put Wall 58（+2.0%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/SLV_evening.json