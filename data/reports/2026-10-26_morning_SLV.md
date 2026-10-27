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
🟡 **近现价集中开仓**: 10-28 50C ΔOI +1,516（距现价 +2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-04 51C ΔOI +2,920 占该期限总 OI 35.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 48.72 → 今开 48.60（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 48.98 ｜ 低 47.87

Options: P/C成交量 0.75 | OI比 0.78 | ATM IV 27.6% | Skew 2.4pp | Term 1.38 | ExpMove ±3.6%（近端） | Rank 29%
量化视角： IV 中性（Rank 29%）｜期限结构正常偏陡（Term 1.38）｜保护溢价中性（Skew 2.4pp）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.75×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-28（2D）±3.6% ｜ 10-30（4D）±4.4% ｜ 11-02（7D）±4.8% ｜ 11-04（9D）±5.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -5,696,507 | GEX Change vs 上次快照 5,919,278 | Flip: Primary Flip: 48.99（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 740 / LOW 85 / INVALID 399
结构观察区: Primary Flip 48.99（全链重定价，覆盖 99%）
Put Wall 50（弱结构｜现价低于该位 2.4%）
最近结构参考: Flip 49（现价低于该位 0.3%）
量化视角： 负 Gamma（570万，无历史分位）｜负 Gamma 缓解（+592万）｜现价位于 Flip 下方 0.34%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 50（Put Wall，弱结构） / 49（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 49（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 48.0P — Vol 4,815 | 最新价 $1.70 | OI 16222→19623 (ΔOI +3401张) | ΔOI/Volume 70.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3401张（+21.0% vs前日OI），连续性待观察（方向未知）
11-04 51.5C — Vol 2,921 | 最新价 $0.42 | OI 0→2920 (ΔOI +2920张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2920张（前日OI缺失），连续性待观察（方向未知）
11-20 47.0P — Vol 3,563 | 最新价 $1.31 | OI 2402→5175 (ΔOI +2773张) | ΔOI/Volume 77.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2773张（+115.5% vs前日OI），连续性待观察（方向未知）
11-20 58.0C — Vol 3,456 | 最新价 $0.21 | OI 4289→7059 (ΔOI +2770张) | ΔOI/Volume 80.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2770张（+64.6% vs前日OI），连续性待观察（方向未知）
11-13 55.0C — Vol 3,180 | 最新价 $0.28 | OI 1401→4116 (ΔOI +2715张) | ΔOI/Volume 85.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2715张（+193.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,579 张（Put 6,174 / Call 8,405），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 19.6k / P 15.2k，今日成交量: C 15.4k / P 11.5k，平值价格ATM: C $0.34 / P $0.67 ｜ ATM IV 27.6%，预期波动 ±2.1%，Max Pain 49
Top ΔOI: P 46 +2,421 ｜ C 50 +1,806 ｜ C 50 +1,650

📆 Forward Expiration Structure

10-28  C +7.3k / P +5.1k ｜ Activity HIGH ｜ 2D
10-30  C +3.7k / P +4.5k ｜ Activity HIGH ｜ 4D
11-02  C +0.6k / P +0.6k ｜ Activity HIGH ｜ 7D
11-04  C +3.7k / P +0.3k ｜ Activity HIGH ｜ 9D

📆 10-28 Forward Structure
存量OI: C 16.2k / P 13.3k，今日变化ΔOI: C +7.3k / P +5.1k，平值价格ATM: C $0.72 / P $1.02 ｜ ATM IV 38.2%，净 delta 敞口 18k shares
Top ΔOI: P 45 +2,249 ｜ C 50 +1,516
仓位参考: Max Pain 50 ｜ Call Wall 50（+2.4%）（OI 3.9k） ｜ Put Wall 45.5（-6.8%，弱）（OI 2.5k）
量化解读： 存量 Call 重｜ATM IV 38.2%｜历史 Rank 29%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 正 18,130 股

📆 10-30 Forward Structure
存量OI: C 82.1k / P 33.7k，今日变化ΔOI: C +3.7k / P +4.5k，平值价格ATM: C $0.95 / P $1.19 ｜ ATM IV 39.8%，净 delta 敞口 45k shares
Top ΔOI: P 44 +2,031 ｜ P 45 +1,303
仓位参考: Max Pain 52 ｜ Call Wall 50（+2.4%，弱）（OI 1.9k） ｜ Put Wall 45（-7.8%，弱）（OI 4.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 39.8%｜历史 Rank 29%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 45,240 股

📆 11-02 Forward Structure
存量OI: C 1.9k / P 1.5k，今日变化ΔOI: C +0.6k / P +0.6k，平值价格ATM: C $1.05 / P $1.32 ｜ ATM IV 36.5%，净 delta 敞口 -20k shares
Top ΔOI: P 53 +143 ｜ P 48 +109 ｜ C 52 +107
仓位参考: Max Pain 50 ｜ Call Wall 50.5（+3.4%）（OI 0.4k） ｜ Put Wall 53（+8.6%）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 36.5%｜历史 Rank 29%（近端代理）｜IV/RV 0.99×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 19,848 股

📆 11-04 Forward Structure
存量OI: C 7.4k / P 0.8k，今日变化ΔOI: C +3.7k / P +0.3k，平值价格ATM: C $1.31 / P $1.56 ｜ ATM IV 39.0%，净 delta 敞口 76k shares
Top ΔOI: C 51 +2,920 ｜ C 50 -540 ｜ C 53 +464
仓位参考: Max Pain 48 ｜ Call Wall 51.5（+5.5%）（OI 2.9k） ｜ Put Wall 53（+8.6%，弱）（OI 78）
量化解读： 存量 Call 重｜ATM IV 39.0%｜历史 Rank 29%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 正 75,967 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/SLV_morning.json