# 期权晨报 2026-10-07（快照 10:20 ET）

📊 市场环境

SPY $774.54 ｜ QQQ $754.53
VIX 15.79 ↑5.2%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　⏰ 今日
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-08 755P ΔOI +18,346（距现价 +0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-08 755P ΔOI +18,346 占该期限总 OI 10.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 759.66 → 今开 753.87（-0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 754.82 ｜ 低 751.76

Options: P/C成交量 1.25 | OI比 2.15 | ATM IV 20.8% | Skew 2.5pp | Term 0.92 | ExpMove ±0.8%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构正常（Term 0.92）｜保护溢价中性（Skew 2.5pp）｜当日成交偏 Put（P/C量 1.25）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.25×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.15×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 42% ｜ P/C OI(近端) 83%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 42%）｜近端持仓结构中性（P/C OI 分位 83%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-08（1D）±0.8% ｜ 10-09（2D）±1.1% ｜ 10-12（5D）±1.3% ｜ 10-13（6D）±1.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -139,911,709 | GEX Change vs 上次快照 -836,167,171 | Flip: Primary Flip: 755.39（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 3220 / LOW 260 / INVALID 1622
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 755.39（全链重定价，覆盖 98%）
Call Wall 760（现价低于该位 0.9%）
最近结构参考: Flip 755（现价低于该位 0.3%）
量化视角： 负 Gamma（1.40亿，历史分位 42%，中性区）｜由正转负（8.36亿）｜现价位于 Flip 下方 0.27%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 758（MaxPain，仅结算参考） / 760（Call Wall）。
• Gamma 区域：切换参考 755（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 700.0P — Vol 56,803 | 最新价 $1.82 | OI 38615→88124 (ΔOI +49509张) | ΔOI/Volume 87.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增49509张（+128.2% vs前日OI），连续性待观察（方向未知）
10-09 754.0P — Vol 23,402 | 最新价 $1.96 | OI 3376→23095 (ΔOI +19719张) | ΔOI/Volume 84.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19719张（+584.1% vs前日OI），连续性待观察（方向未知）
10-08 755.0P — Vol 28,934 | 最新价 $1.54 | OI 963→19309 (ΔOI +18346张) | ΔOI/Volume 63.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18346张（+1905.1% vs前日OI），连续性待观察（方向未知）
10-16 770.0C — Vol 18,024 | 最新价 $4.21 | OI 33651→45936 (ΔOI +12285张) | ΔOI/Volume 68.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12285张（+36.5% vs前日OI），连续性待观察（方向未知）
10-07 750.0P — Vol 20,815 | 最新价 $0.18 | OI 3557→15323 (ΔOI +11766张) | ΔOI/Volume 56.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11766张（+330.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 111,625 张（Put 99,340 / Call 12,285），跨 5 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $16M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 109.9k / P 236.1k，今日成交量: C 364.6k / P 454.3k，平值价格ATM: C $1.79 / P $1.60 ｜ ATM IV 20.8%，预期波动 ±0.4%，Max Pain 758
Top ΔOI: P 750 +11,766 ｜ P 755 +8,336 ｜ P 760 +6,767

📆 Forward Expiration Structure

10-08  C +11.0k / P +44.8k ｜ Activity HIGH ｜ 1D
10-09  C +15.5k / P +47.0k ｜ Activity HIGH ｜ 2D
10-12  C +9.6k / P +13.6k ｜ Activity HIGH ｜ 5D
10-13  C +5.1k / P +25.3k ｜ Activity HIGH ｜ 6D

📆 10-08 Forward Structure
存量OI: C 37.5k / P 130.6k，今日变化ΔOI: C +11.0k / P +44.8k，平值价格ATM: C $3.24 / P $3.00 ｜ ATM IV 17.6%，净 delta 敞口 -2.2M shares
Top ΔOI: P 755 +18,346 ｜ P 760 +3,877 ｜ P 758 +1,755
仓位参考: Max Pain 756 ｜ Call Wall 770（+2.2%，弱）（OI 2.2k） ｜ Put Wall 755（+0.2%，弱）（OI 19.3k）
量化解读： 存量 Put 重｜ATM IV 17.6%｜历史 Rank 64%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 2,192,687 股

📆 10-09 Forward Structure
存量OI: C 186.6k / P 355.3k，今日变化ΔOI: C +15.5k / P +47.0k，平值价格ATM: C $4.32 / P $3.78 ｜ ATM IV 17.0%，净 delta 敞口 -2.3M shares
Top ΔOI: P 754 +19,719 ｜ C 765 +4,392 ｜ P 760 +2,908
仓位参考: Max Pain 750 ｜ Call Wall 754（+0.1%）（OI 21.1k） ｜ Put Wall 754（+0.1%，弱）（OI 23.1k）
量化解读： 存量 Put 重｜ATM IV 17.0%｜历史 Rank 64%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 2,349,841 股

📆 10-12 Forward Structure
存量OI: C 26.2k / P 94.1k，今日变化ΔOI: C +9.6k / P +13.6k，平值价格ATM: C $5.33 / P $4.66 ｜ ATM IV 14.0%，净 delta 敞口 -214k shares
Top ΔOI: C 780 +4,828 ｜ P 742 +3,883 ｜ P 731 +1,979
仓位参考: Max Pain 752 ｜ Call Wall 770（+2.2%，弱）（OI 1.3k） ｜ Put Wall 738（-2.0%）（OI 12.6k）
量化解读： 存量 Put 重｜ATM IV 14.0%｜历史 Rank 64%（近端代理）｜IV/RV 1.03×（近似）｜净 delta 敞口 负 213,997 股

📆 10-13 Forward Structure
存量OI: C 14.4k / P 69.0k，今日变化ΔOI: C +5.1k / P +25.3k，平值价格ATM: C $6.05 / P $5.37 ｜ ATM IV 14.6%，净 delta 敞口 -598k shares
Top ΔOI: P 750 +10,519 ｜ P 692 +4,573 ｜ P 727 +1,487
仓位参考: Max Pain 752 ｜ Call Wall 750（-0.4%，弱）（OI 1.0k） ｜ Put Wall 740（-1.8%，弱）（OI 10.9k）
量化解读： 存量 Put 重｜ATM IV 14.6%｜历史 Rank 64%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 负 597,837 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/QQQ_morning.json