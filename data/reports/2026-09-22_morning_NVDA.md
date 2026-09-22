# 期权晨报 2026-09-22（快照 10:20 ET）

📊 市场环境

SPY $774.05 ｜ QQQ $745.56
VIX 14.54 ↓2.2%（5D -15.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 37.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-23 230C ΔOI +47,481（距现价 +1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-23 230C ΔOI +47,481 占该期限总 OI 20.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 227.38 → 今开 226.91（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 229.60 ｜ 低 226.50

Options: P/C成交量 0.32 | OI比 0.74 | ATM IV 32.5% | Skew 1.1pp | Term 0.95 | ExpMove ±1.5%（近端） | Rank 12%
量化视角： IV 历史低位（Rank 12%，期权偏便宜）｜期限结构正常（Term 0.95）｜保护溢价薄（Skew 1.1pp）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.32×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-23（1D）±1.5% ｜ 09-25（3D）±2.4% ｜ 09-28（6D）±2.8% ｜ 09-30（8D）±3.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 700,040,148 | GEX Change vs 上次快照 174,767,803 | Flip: Primary Flip: 213.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 740 / LOW 195 / INVALID 441
结构观察区: Primary Flip 213.34（全链重定价，覆盖 100%）
Call Wall 230（现价低于该位 1.0%）
最近结构参考: Call Wall 230（现价低于该位 1.0%）
量化视角： 正 Gamma（7.00亿，无历史分位）｜正 Gamma 增强（+1.75亿）｜现价位于 Flip 上方 6.68%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 222（MaxPain，仅结算参考）；上方 230（Call Wall）。
• Gamma 区域：切换参考 213（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-23 230.0C — Vol 110,955 | 最新价 $1.14 | OI 10095→57576 (ΔOI +47481张) | ΔOI/Volume 42.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增47481张（+470.3% vs前日OI），连续性待观察（方向未知）
09-25 235.0C — Vol 46,117 | 最新价 $0.73 | OI 12792→36692 (ΔOI +23900张) | ΔOI/Volume 51.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23900张（+186.8% vs前日OI），连续性待观察（方向未知）
09-23 140.0P — Vol 22,759 | 最新价 $0.01 | OI 7→22700 (ΔOI +22693张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22693张（+324185.7% vs前日OI），连续性待观察（方向未知）
09-25 230.0C — Vol 116,399 | 最新价 $2.04 | OI 62908→78834 (ΔOI +15926张) | ΔOI/Volume 13.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15926张（+25.3% vs前日OI），连续性待观察（方向未知）
09-25 237.5C — Vol 23,175 | 最新价 $0.43 | OI 4547→17931 (ΔOI +13384张) | ΔOI/Volume 57.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13384张（+294.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 123,384 张（Put 22,693 / Call 100,691），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-23  C +80.4k / P +64.1k ｜ Activity HIGH ｜ 1D
09-25  C +69.1k / P +23.5k ｜ Activity HIGH ｜ 3D
09-28  C +16.6k / P +7.7k ｜ Activity HIGH ｜ 6D
09-30  C +6.3k / P +1.7k ｜ Activity HIGH ｜ 8D

📆 09-23 Forward Structure
存量OI: C 130.9k / P 96.6k，今日变化ΔOI: C +80.4k / P +64.1k，平值价格ATM: C $1.63 / P $1.84 ｜ ATM IV 32.5%，净 delta 敞口 1.2M shares
Top ΔOI: C 230 +47,481 ｜ C 235 +11,749
仓位参考: Max Pain 222 ｜ Call Wall 230（+1.1%）（OI 57.6k） ｜ Put Wall 205（-9.9%，弱）（OI 6.0k）
量化解读： 存量 Call 重｜ATM IV 32.5%｜历史 Rank 12%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,207,545 股

📆 09-25 Forward Structure
存量OI: C 478.0k / P 327.0k，今日变化ΔOI: C +69.1k / P +23.5k，平值价格ATM: C $2.72 / P $2.82 ｜ ATM IV 32.2%，净 delta 敞口 222k shares
Top ΔOI: C 235 +23,900 ｜ C 230 +15,926 ｜ C 237 +13,384
仓位参考: Max Pain 220 ｜ Call Wall 230（+1.1%，弱）（OI 78.8k） ｜ Put Wall 210（-7.7%，弱）（OI 19.9k）
量化解读： 存量 Call 重｜ATM IV 32.2%｜历史 Rank 12%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 222,137 股

📆 09-28 Forward Structure
存量OI: C 38.9k / P 22.3k，今日变化ΔOI: C +16.6k / P +7.7k，平值价格ATM: C $3.20 / P $3.26 ｜ ATM IV 27.0%，净 delta 敞口 278k shares
Top ΔOI: C 235 +8,637 ｜ C 230 +3,798 ｜ P 225 +1,564
仓位参考: Max Pain 220 ｜ Call Wall 235（+3.3%，弱）（OI 10.1k） ｜ Put Wall 210（-7.7%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 27.0%｜历史 Rank 12%（近端代理）｜IV/RV 0.89×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 278,469 股

📆 09-30 Forward Structure
存量OI: C 15.0k / P 12.4k，今日变化ΔOI: C +6.3k / P +1.7k，平值价格ATM: C $4.05 / P $4.00 ｜ ATM IV 29.7%，净 delta 敞口 117k shares
Top ΔOI: C 240 +2,550 ｜ C 237 +539 ｜ C 225 +465
仓位参考: Max Pain 218 ｜ Call Wall 240（+5.5%）（OI 3.0k） ｜ Put Wall 212.5（-6.6%，弱）（OI 3.4k）
量化解读： 存量 Call 重｜ATM IV 29.7%｜历史 Rank 12%（近端代理）｜IV/RV 0.98×（近似）｜净 delta 敞口 正 116,864 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/NVDA_morning.json