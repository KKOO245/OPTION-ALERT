# 期权晚报 2026-10-27（快照 16:40 ET）

📊 市场环境

SPY $769.66 ｜ QQQ $721.25
VIX 17.52 ↓4.7%（5D +1.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 1.8 ｜ 前值 0.1　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🟡 **近现价集中开仓**: 10-28 50C ΔOI +2,511（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-02 47P ΔOI +586 占该期限总 OI 11.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 48.50 → 收盘 49.16（+1.4%） ｜ 今日高 49.24 ｜ 低 48.48 ｜ 昨收 48.66 → 收盘 49.16（+1.0%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-03，窗口结束前不做对错判定）

Options: P/C成交量 0.42 | OI比 0.69 | ATM IV 48.6% | Skew 3.9pp | Term 0.76 | ExpMove ±2.0%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价中性（Skew 3.9pp）｜存量 Call 偏重（OI比 0.69）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-28（1D）±2.0% ｜ 10-30（3D）±3.2% ｜ 11-02（6D）±3.7% ｜ 11-04（8D）±4.5%
   ⇒ IV–VIX Spread: +31.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 12,292,925 | GEX Change vs 上次快照 11,989,479 | Flip: Primary Flip: 48.75（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 728 / LOW 108 / INVALID 356
结构观察区: Primary Flip 48.75（全链重定价，覆盖 98%）
Put Wall 50（弱结构｜现价低于该位 1.7%）
最近结构参考: Flip 49（现价高于该位 0.8%）
量化视角： 正 Gamma（1229万，无历史分位）｜正 Gamma 增强（+1199万）｜现价位于 Flip 上方 0.84%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 49（MaxPain，仅结算参考）；上方 50（Put Wall，弱结构）。
• Gamma 区域：切换参考 49（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 48.0P — Vol 1,554 | 最新价 $1.56 | OI 16222→19623 (ΔOI +3401张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3401张（+21.0% vs前日OI），连续性待观察（方向未知）
11-04 51.5C — Vol 52 | 最新价 $0.32 | OI 0→2920 (ΔOI +2920张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增2920张（前日OI缺失），值得跟踪（方向未知）
11-20 47.0P — Vol 142 | 最新价 $1.20 | OI 2402→5175 (ΔOI +2773张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2773张（+115.5% vs前日OI），连续性待观察（方向未知）
11-20 58.0C — Vol 60 | 最新价 $0.18 | OI 4289→7059 (ΔOI +2770张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2770张（+64.6% vs前日OI），连续性待观察（方向未知）
11-13 55.0C — Vol 198 | 最新价 $0.22 | OI 1401→4116 (ΔOI +2715张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2715张（+193.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,579 张（Put 6,174 / Call 8,405），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-28  C +9.2k / P +4.2k ｜ Activity HIGH ｜ 1D
10-30  C +5.8k / P +0.3k ｜ Activity HIGH ｜ 3D
11-02  C +0.8k / P +1.1k ｜ Activity HIGH ｜ 6D
11-04  C +0.9k / P +2.1k ｜ Activity HIGH ｜ 8D

📆 10-28 Forward Structure
存量OI: C 25.5k / P 17.6k，今日变化ΔOI: C +9.2k / P +4.2k，平值价格ATM: C $0.59 / P $0.42 ｜ ATM IV 48.6%，净 delta 敞口 291k shares
Top ΔOI: C 50 +2,511 ｜ C 49 +1,594 ｜ C 49 +1,102
仓位参考: Max Pain 49 ｜ Call Wall 50（+1.7%）（OI 6.4k） ｜ Put Wall 45.5（-7.4%，弱）（OI 2.5k）
量化解读： 存量 Call 重｜ATM IV 48.6%｜历史 Rank 81%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 290,612 股

📆 10-30 Forward Structure
存量OI: C 87.9k / P 34.0k，今日变化ΔOI: C +5.8k / P +0.3k，平值价格ATM: C $0.88 / P $0.68 ｜ ATM IV 43.8%，净 delta 敞口 236k shares
Top ΔOI: C 52 +1,981 ｜ C 50 +1,483 ｜ C 51 +1,457
仓位参考: Max Pain 51 ｜ Call Wall 52.5（+6.8%，弱）（OI 3.5k） ｜ Put Wall 45（-8.5%，弱）（OI 4.2k）
量化解读： 存量 Call 重｜ATM IV 43.8%｜历史 Rank 81%（近端代理）｜IV/RV 1.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 236,317 股

📆 11-02 Forward Structure
存量OI: C 2.8k / P 2.6k，今日变化ΔOI: C +0.8k / P +1.1k，平值价格ATM: C $0.98 / P $0.83 ｜ ATM IV 35.9%，净 delta 敞口 1k shares
Top ΔOI: P 47 +586 ｜ C 49 +166 ｜ C 50 +149
仓位参考: Max Pain 50 ｜ Call Wall 50.5（+2.7%，弱）（OI 0.5k） ｜ Put Wall 47.5（-3.4%）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 35.9%｜历史 Rank 81%（近端代理）｜IV/RV 0.99×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,006 股

📆 11-04 Forward Structure
存量OI: C 8.3k / P 2.9k，今日变化ΔOI: C +0.9k / P +2.1k，平值价格ATM: C $1.21 / P $1.02 ｜ ATM IV 38.5%，净 delta 敞口 1k shares
仓位参考: Max Pain 48 ｜ Call Wall 51.5（+4.8%）（OI 3.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 38.5%｜历史 Rank 81%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 正 1,445 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/SLV_evening.json