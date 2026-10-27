# 期权晨报 2026-10-26（快照 09:08 ET）

📊 市场环境

SPY $765.37 ｜ QQQ $712.20
VIX 19.22 ↓1.2%（5D +4.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-26

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 待公布 ｜ 前值 0
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-30 82C ΔOI +18,611（距现价 +0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-30 82C ΔOI +18,611 占该期限总 OI 11.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 80.20 → 今开 81.16（+1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 81.61 ｜ 低 78.92

Options: P/C成交量 0.28 | OI比 0.63 | ATM IV 28.5% | Skew 2.9pp | Term 1.44 | ExpMove ±3.6%（近端） | Rank 7%
量化视角： IV 历史低位（Rank 7%，期权偏便宜）｜期限结构正常偏陡（Term 1.44）｜保护溢价中性（Skew 2.9pp）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.28×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-28（2D）±3.6% ｜ 10-30（4D）±4.5% ｜ 11-02（7D）±5.4% ｜ 11-04（9D）±6.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 27,869,756 | GEX Change vs 上次快照 49,988,273 | Flip: Primary Flip: 79.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 549 / LOW 127 / INVALID 498
结构观察区: Primary Flip 79.44（全链重定价，覆盖 99%）
Put Wall 80（弱结构｜现价高于该位 1.7%） | Call Wall 85（弱结构｜现价低于该位 4.3%）
最近结构参考: Put Wall 80（现价高于该位 1.7%）
量化视角： 正 Gamma（2787万，无历史分位）｜由负转正（+4999万）｜现价位于 Flip 上方 2.41%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（Put Wall，弱结构）；上方 83（MaxPain，仅结算参考） / 85（Call Wall，弱结构）。
• Gamma 区域：切换参考 79（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 82.0C — Vol 18,821 | 最新价 $1.16 | OI 502→19113 (ΔOI +18611张) | ΔOI/Volume 98.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18611张（+3707.4% vs前日OI），连续性待观察（方向未知）
10-30 85.0C — Vol 19,428 | 最新价 $0.38 | OI 11174→27547 (ΔOI +16373张) | ΔOI/Volume 84.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16373张（+146.5% vs前日OI），连续性待观察（方向未知）
10-30 83.0C — Vol 9,246 | 最新价 $0.79 | OI 58→9138 (ΔOI +9080张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9080张（+15655.2% vs前日OI），连续性待观察（方向未知）
10-30 81.0C — Vol 9,256 | 最新价 $1.57 | OI 73→9151 (ΔOI +9078张) | ΔOI/Volume 98.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9078张（+12435.6% vs前日OI），连续性待观察（方向未知）
10-30 76.0P — Vol 4,052 | 最新价 $0.52 | OI 35→4059 (ΔOI +4024张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4024张（+11497.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 57,166 张（Put 4,024 / Call 53,142），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 7.0k / P 4.4k，今日成交量: C 2.7k / P 0.8k，平值价格ATM: C $0.48 / P $1.31 ｜ ATM IV 28.5%，预期波动 ±2.2%，Max Pain 83
Top ΔOI: C 83 +882 ｜ C 86 +509 ｜ C 82 +249

📆 Forward Expiration Structure

10-28  C +0.9k / P +1.0k ｜ Activity HIGH ｜ 2D
10-30  C +56.0k / P +4.8k ｜ Activity HIGH ｜ 4D
11-02  C +0.6k / P +0.5k ｜ Activity HIGH ｜ 7D
11-04  C +0.5k / P +40 ｜ Activity HIGH ｜ 9D

📆 10-28 Forward Structure
存量OI: C 1.9k / P 5.4k，今日变化ΔOI: C +0.9k / P +1.0k，平值价格ATM: C $1.18 / P $1.73 ｜ ATM IV 40.2%，净 delta 敞口 -8k shares
Top ΔOI: P 75 +701 ｜ C 88 +204
仓位参考: Max Pain 85 ｜ Call Wall 86（+5.7%，弱）（OI 0.2k） ｜ Put Wall 84（+3.2%，弱）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 40.2%｜历史 Rank 7%（近端代理）｜IV/RV 1.08×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 8,499 股

📆 10-30 Forward Structure
存量OI: C 130.8k / P 33.3k，今日变化ΔOI: C +56.0k / P +4.8k，平值价格ATM: C $1.57 / P $2.12 ｜ ATM IV 41.3%，净 delta 敞口 1.6M shares
Top ΔOI: C 82 +18,611 ｜ C 85 +16,373 ｜ C 83 +9,080
仓位参考: Max Pain 81 ｜ Call Wall 85（+4.5%，弱）（OI 27.5k） ｜ Put Wall 79（-2.9%，弱）（OI 3.4k）
量化解读： 存量 Call 重｜ATM IV 41.3%｜历史 Rank 7%（近端代理）｜IV/RV 1.11×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,608,315 股

📆 11-02 Forward Structure
存量OI: C 0.9k / P 0.8k，今日变化ΔOI: C +0.6k / P +0.5k，平值价格ATM: C $1.94 / P $2.48 ｜ ATM IV 38.9%，净 delta 敞口 -15k shares
Top ΔOI: C 86 +525 ｜ P 81 +251 ｜ P 80 +156
仓位参考: Max Pain 86 ｜ Call Wall 86（+5.7%）（OI 0.5k） ｜ Put Wall 81（-0.4%）（OI 0.3k）
量化解读： 存量两侧均衡｜ATM IV 38.9%｜历史 Rank 7%（近端代理）｜IV/RV 1.05×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 14,593 股

📆 11-04 Forward Structure
存量OI: C 0.6k / P 59，今日变化ΔOI: C +0.5k / P +40，平值价格ATM: C $3.00 / P $2.30 ｜ ATM IV 48.6%，净 delta 敞口 15k shares
Top ΔOI: C 83 +233 ｜ C 84 +232 ｜ C 82 +29
仓位参考: Max Pain 81 ｜ Call Wall 83（+2.0%，弱）（OI 0.2k） ｜ Put Wall 80（-1.7%，弱）（OI 17）
量化解读： 存量 Call 重｜ATM IV 48.6%｜历史 Rank 7%（近端代理）｜IV/RV 1.31×（近似）｜净 delta 敞口 正 15,469 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/GDX_morning.json