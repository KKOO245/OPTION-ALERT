# 期权晨报 2026-09-16（快照 11:22 ET）

📊 市场环境

SPY $760.53 ｜ QQQ $710.91
VIX 16.68 ↓3.0%（5D +1.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75　⏰ 今日
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　⏰ 今日
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　⏰ 今日
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **事件差分**: 09-18 ATM IV 50.6% vs 09-21 39.7%（差 +10.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-18 360C ΔOI +3,346（距现价 -1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-21 400C ΔOI +4,142 占该期限总 OI 12.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 356.58 → 今开 357.71（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 365.05 ｜ 低 354.89

Options: P/C成交量 0.63 | OI比 0.71 | ATM IV 66.5% | Skew 3.2pp | Term 0.63 | ExpMove ±3.1%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.63，近月 IV 高于远月）｜保护溢价中性（Skew 3.2pp）｜存量 Call 偏重（OI比 0.71）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.71×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（2D）±3.1% ｜ 09-21（5D）±3.8% ｜ 09-23（7D）±4.7% ｜ 09-25（9D）±5.4%
   ⇒ IV–VIX Spread: +49.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 106,398,246 | GEX Change vs 上次快照 94,736,949 | Flip: Primary Flip: 354.46（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1337 / LOW 142 / INVALID 561
结构观察区: Primary Flip 354.46（全链重定价，覆盖 99%）
Call Wall 400（弱结构｜现价低于该位 8.8%）
最近结构参考: Flip 354（现价高于该位 2.9%）
量化视角： 正 Gamma（1.06亿，无历史分位）｜正 Gamma 增强（+9474万）｜现价位于 Flip 上方 2.91%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 360（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 354（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-16 350.0P — Vol 65,883 | 最新价 $1.28 | OI 2555→6961 (ΔOI +4406张) | ΔOI/Volume 6.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4406张（+172.4% vs前日OI），连续性待观察（方向未知）
09-16 377.5C — Vol 12,922 | 最新价 $0.12 | OI 1431→5664 (ΔOI +4233张) | ΔOI/Volume 32.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4233张（+295.8% vs前日OI），连续性待观察（方向未知）
09-21 400.0C — Vol 5,184 | 最新价 $0.24 | OI 716→4858 (ΔOI +4142张) | ΔOI/Volume 79.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4142张（+578.5% vs前日OI），连续性待观察（方向未知）
09-16 370.0C — Vol 59,871 | 最新价 $0.41 | OI 5226→9130 (ΔOI +3904张) | ΔOI/Volume 6.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3904张（+74.7% vs前日OI），连续性待观察（方向未知）
09-16 360.0C — Vol 91,775 | 最新价 $2.36 | OI 4404→8226 (ΔOI +3822张) | ΔOI/Volume 4.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3822张（+86.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 20,507 张（Put 4,406 / Call 16,101），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 83.7k / P 59.2k，今日成交量: C 395.1k / P 248.0k，平值价格ATM: C $1.84 / P $3.05 ｜ ATM IV 66.5%，预期波动 ±1.3%，Max Pain 360
Top ΔOI: P 350 +4,406 ｜ C 377 +4,233 ｜ C 370 +3,904

📆 Forward Expiration Structure

09-18  C +13.0k / P +5.4k ｜ Activity MEDIUM △ ｜ 2D
09-21  C +9.5k / P +3.8k ｜ Activity HIGH ｜ 5D
09-23  C +2.8k / P +3.8k ｜ Activity HIGH ｜ 7D
09-25  C +6.8k / P +6.9k ｜ Activity HIGH ｜ 9D

📆 09-18 Forward Structure
存量OI: C 588.9k / P 485.5k，今日变化ΔOI: C +13.0k / P +5.4k，平值价格ATM: C $5.24 / P $6.20 ｜ ATM IV 50.6%，净 delta 敞口 606k shares
Top ΔOI: C 360 +3,346 ｜ P 410 -2,128
仓位参考: Max Pain 360 ｜ Call Wall 400（+9.7%，弱）（OI 24.8k） ｜ Put Wall 350（-4.1%，弱）（OI 17.7k）
量化解读： 存量 Call 重｜ATM IV 50.6%｜历史 Rank 80%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 605,781 股

📆 09-21 Forward Structure
存量OI: C 19.6k / P 12.8k，今日变化ΔOI: C +9.5k / P +3.8k，平值价格ATM: C $6.50 / P $7.30 ｜ ATM IV 39.7%，净 delta 敞口 61k shares
Top ΔOI: C 400 +4,142 ｜ C 405 +2,159 ｜ P 347 +897
仓位参考: Max Pain 360 ｜ Call Wall 400（+9.7%）（OI 4.9k） ｜ Put Wall 360（-1.3%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 39.7%｜历史 Rank 80%（近端代理）｜IV/RV 0.82×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 61,410 股

📆 09-23 Forward Structure
存量OI: C 9.3k / P 7.4k，今日变化ΔOI: C +2.8k / P +3.8k，平值价格ATM: C $8.25 / P $8.95 ｜ ATM IV 41.9%，净 delta 敞口 7k shares
Top ΔOI: P 330 +1,403 ｜ P 340 +374
仓位参考: Max Pain 362 ｜ Call Wall 375（+2.8%，弱）（OI 0.9k） ｜ Put Wall 330（-9.5%）（OI 1.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 41.9%｜历史 Rank 80%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 正 7,344 股

📆 09-25 Forward Structure
存量OI: C 75.8k / P 71.0k，今日变化ΔOI: C +6.8k / P +6.9k，平值价格ATM: C $9.65 / P $10.17 ｜ ATM IV 43.0%，净 delta 敞口 54k shares
仓位参考: Max Pain 358 ｜ Call Wall 400（+9.7%，弱）（OI 6.8k） ｜ Put Wall 350（-4.1%，弱）（OI 3.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 43.0%｜历史 Rank 80%（近端代理）｜IV/RV 0.88×（近似）｜净 delta 敞口 正 53,731 股

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 50.6% vs 09-21 39.7%（差 +10.9pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/TSLA_morning.json