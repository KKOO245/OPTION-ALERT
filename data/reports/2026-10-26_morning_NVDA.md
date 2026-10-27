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
🟡 **近现价集中开仓**: 10-30 220C ΔOI +30,792（距现价 +3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-28 125P ΔOI +21,376 占该期限总 OI 15.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 210.96 → 今开 210.99（+0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 213.85 ｜ 低 210.18

Options: P/C成交量 0.70 | OI比 0.75 | ATM IV 69.8% | Skew 4.0pp | Term 0.65 | ExpMove ±3.4%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.65，近月 IV 高于远月）｜保护溢价中性（Skew 4.0pp）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.70×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-28（2D）±3.4% ｜ 10-30（4D）±4.1% ｜ 11-02（7D）±4.7% ｜ 11-04（9D）±5.2%
   ⇒ IV–VIX Spread: +50.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 148,340,359 | GEX Change vs 上次快照 154,477,906 | Flip: Primary Flip: 207.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 376 / LOW 466 / INVALID 636
结构观察区: Primary Flip 207.87（全链重定价，覆盖 93%）
Put Wall 200（弱结构｜现价高于该位 6.6%） | Call Wall 230（弱结构｜现价低于该位 7.3%）
最近结构参考: Flip 208（现价高于该位 2.6%）
量化视角： 正 Gamma（1.48亿，无历史分位）｜由负转正（+1.54亿）｜现价位于 Flip 上方 2.59%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构） / 212（MaxPain，仅结算参考）；上方 230（Call Wall，弱结构）。
• Gamma 区域：切换参考 208（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 220.0C — Vol 57,852 | 最新价 $1.19 | OI 17097→47889 (ΔOI +30792张) | ΔOI/Volume 53.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30792张（+180.1% vs前日OI），连续性待观察（方向未知）
10-30 215.0C — Vol 46,517 | 最新价 $2.70 | OI 5429→35356 (ΔOI +29927张) | ΔOI/Volume 64.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29927张（+551.2% vs前日OI），连续性待观察（方向未知）
10-28 125.0P — Vol 21,376 | 最新价 $0.01 | OI 5→21381 (ΔOI +21376张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21376张（+427520.0% vs前日OI），连续性待观察（方向未知）
10-30 217.5C — Vol 35,219 | 最新价 $1.84 | OI 23035→44192 (ΔOI +21157张) | ΔOI/Volume 60.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21157张（+91.8% vs前日OI），连续性待观察（方向未知）
10-30 225.0C — Vol 43,582 | 最新价 $0.45 | OI 32301→50890 (ΔOI +18589张) | ΔOI/Volume 42.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18589张（+57.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 121,841 张（Put 21,376 / Call 100,465），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 88.0k / P 65.9k，今日成交量: C 205.2k / P 142.8k，平值价格ATM: C $2.08 / P $1.46 ｜ ATM IV 69.8%，预期波动 ±1.7%，Max Pain 212
Top ΔOI: C 215 +7,029 ｜ C 220 +4,218 ｜ P 210 +4,116

📆 Forward Expiration Structure

10-28  C +33.0k / P +48.4k ｜ Activity HIGH ｜ 2D
10-30  C +122.1k / P +71.1k ｜ Activity HIGH ｜ 4D
11-02  C +2.5k / P +3.4k ｜ Activity HIGH ｜ 7D
11-04  C +0.7k / P +2.1k ｜ Activity HIGH ｜ 9D

📆 10-28 Forward Structure
存量OI: C 67.4k / P 70.4k，今日变化ΔOI: C +33.0k / P +48.4k，平值价格ATM: C $2.92 / P $4.30 ｜ ATM IV 49.5%，净 delta 敞口 23k shares
Top ΔOI: P 180 +8,391
仓位参考: Max Pain 215 ｜ Call Wall 230（+7.9%，弱）（OI 7.0k）
量化解读： 存量两侧均衡｜ATM IV 49.5%｜历史 Rank 90%（近端代理）｜IV/RV 1.74×（近似）｜净 delta 敞口 正 23,251 股

📆 10-30 Forward Structure
存量OI: C 394.5k / P 282.4k，今日变化ΔOI: C +122.1k / P +71.1k，平值价格ATM: C $3.75 / P $5.05 ｜ ATM IV 46.3%，净 delta 敞口 3.2M shares
Top ΔOI: C 220 +30,792 ｜ C 215 +29,927 ｜ C 217 +21,157
仓位参考: Max Pain 215 ｜ Call Wall 225（+5.5%，弱）（OI 50.9k） ｜ Put Wall 210（-1.5%，弱）（OI 21.3k）
量化解读： 存量 Call 重｜ATM IV 46.3%｜历史 Rank 90%（近端代理）｜IV/RV 1.62×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 3,247,545 股

📆 11-02 Forward Structure
存量OI: C 9.9k / P 6.1k，今日变化ΔOI: C +2.5k / P +3.4k，平值价格ATM: C $4.55 / P $5.54 ｜ ATM IV 43.0%，净 delta 敞口 11k shares
Top ΔOI: P 200 +2,009 ｜ C 215 +428 ｜ C 210 +400
仓位参考: Max Pain 212 ｜ Call Wall 230（+7.9%，弱）（OI 2.0k） ｜ Put Wall 200（-6.2%）（OI 2.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 43.0%｜历史 Rank 90%（近端代理）｜IV/RV 1.51×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 11,245 股

📆 11-04 Forward Structure
存量OI: C 6.1k / P 4.5k，今日变化ΔOI: C +0.7k / P +2.1k，平值价格ATM: C $5.00 / P $6.03 ｜ ATM IV 50.4%，净 delta 敞口 -15k shares
Top ΔOI: P 192 +1,398 ｜ C 212 +198
仓位参考: Max Pain 215 ｜ Call Wall 225（+5.5%）（OI 2.5k） ｜ Put Wall 192.5（-9.7%）（OI 1.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 50.4%｜历史 Rank 90%（近端代理）｜IV/RV 1.77×（近似）｜净 delta 敞口 负 14,710 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/NVDA_morning.json