# 期权晨报 2026-09-22（快照 10:20 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $nan
VIX 14.54 ↓2.2%（5D -15.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-23 390C ΔOI +3,131（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 375.30 → 今开 379.07（+1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 379.25 ｜ 低 372.88

Options: P/C成交量 0.64 | OI比 0.74 | ATM IV 46.0% | Skew -2.3pp | Term 0.98 | ExpMove ±2.2%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构正常（Term 0.98）｜Put 保护异常便宜（Skew -2.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-23（1D）±2.2% ｜ 09-25（3D）±3.4% ｜ 09-28（6D）±3.9% ｜ 09-30（8D）±4.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 115,955,203 | GEX Change vs 上次快照 -35,521 | Flip: Primary Flip: 357.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1199 / LOW 76 / INVALID 561
结构观察区: Primary Flip 357.34（全链重定价，覆盖 100%）
Call Wall 400（弱结构｜现价低于该位 6.1%）
最近结构参考: Flip 357（现价高于该位 5.1%）
量化视角： 正 Gamma（1.16亿，无历史分位）｜正 Gamma 减弱（4万）｜现价位于 Flip 上方 5.11%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 370（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 357（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 400.0C — Vol 27,828 | 最新价 $0.81 | OI 8008→14787 (ΔOI +6779张) | ΔOI/Volume 24.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6779张（+84.7% vs前日OI），连续性待观察（方向未知）
09-25 230.0P — Vol 5,136 | 最新价 $0.02 | OI 652→5457 (ΔOI +4805张) | ΔOI/Volume 93.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4805张（+737.0% vs前日OI），连续性待观察（方向未知）
09-25 395.0C — Vol 9,463 | 最新价 $1.31 | OI 3266→7469 (ΔOI +4203张) | ΔOI/Volume 44.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4203张（+128.7% vs前日OI），连续性待观察（方向未知）
09-23 400.0C — Vol 14,544 | 最新价 $0.22 | OI 1716→5888 (ΔOI +4172张) | ΔOI/Volume 28.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4172张（+243.1% vs前日OI），连续性待观察（方向未知）
09-25 310.0P — Vol 4,282 | 最新价 $0.06 | OI 1096→4702 (ΔOI +3606张) | ΔOI/Volume 84.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3606张（+329.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 23,565 张（Put 8,411 / Call 15,154），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-23  C +28.5k / P +18.7k ｜ Activity HIGH ｜ 1D
09-25  C +33.7k / P +23.6k ｜ Activity HIGH ｜ 3D
09-28  C +5.8k / P +3.2k ｜ Activity HIGH ｜ 6D
09-30  C +2.0k / P +1.8k ｜ Activity HIGH ｜ 8D

📆 09-23 Forward Structure
存量OI: C 54.6k / P 40.5k，今日变化ΔOI: C +28.5k / P +18.7k，平值价格ATM: C $5.04 / P $3.25 ｜ ATM IV 46.0%，净 delta 敞口 69k shares
Top ΔOI: C 400 +4,172 ｜ C 410 +3,589 ｜ C 390 +3,131
仓位参考: Max Pain 370 ｜ Call Wall 400（+6.5%，弱）（OI 5.9k） ｜ Put Wall 370（-1.5%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 46.0%｜历史 Rank 26%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 69,357 股

📆 09-25 Forward Structure
存量OI: C 188.9k / P 222.0k，今日变化ΔOI: C +33.7k / P +23.6k，平值价格ATM: C $7.32 / P $5.45 ｜ ATM IV 44.7%，净 delta 敞口 -97k shares
Top ΔOI: C 400 +6,779 ｜ C 395 +4,203
仓位参考: Max Pain 362 ｜ Call Wall 367.5（-2.2%，弱）（OI 16.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 44.7%｜历史 Rank 26%（近端代理）｜IV/RV 1.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 96,619 股

📆 09-28 Forward Structure
存量OI: C 15.4k / P 7.7k，今日变化ΔOI: C +5.8k / P +3.2k，平值价格ATM: C $8.30 / P $6.36 ｜ ATM IV 37.1%，净 delta 敞口 18k shares
Top ΔOI: C 410 +1,061 ｜ P 375 +776
仓位参考: Max Pain 368 ｜ Call Wall 410（+9.2%，弱）（OI 1.4k） ｜ Put Wall 375（-0.2%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 37.1%｜历史 Rank 26%（近端代理）｜IV/RV 0.86×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 17,607 股

📆 09-30 Forward Structure
存量OI: C 8.5k / P 5.2k，今日变化ΔOI: C +2.0k / P +1.8k，平值价格ATM: C $10.00 / P $7.90 ｜ ATM IV 39.5%，净 delta 敞口 -19k shares
Top ΔOI: P 370 +508 ｜ C 395 +322 ｜ C 390 +282
仓位参考: Max Pain 368 ｜ Call Wall 400（+6.5%，弱）（OI 0.8k） ｜ Put Wall 370（-1.5%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 39.5%｜历史 Rank 26%（近端代理）｜IV/RV 0.91×（近似）｜净 delta 敞口 负 19,464 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/TSLA_morning.json