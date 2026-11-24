# 期权晨报 2026-11-24（快照 10:20 ET）

📊 市场环境

SPY $718.15 ｜ QQQ $638.10
VIX 27.25 ↑2.4%（5D +7.0%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.4（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 108.78 → 今开 107.49（-1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 107.49 ｜ 低 103.46

Options: P/C成交量 0.61 | OI比 0.58 | ATM IV 80.9% | Skew 5.9pp | Term 0.97 | ExpMove ±6.2%（近端） | Rank 62%
量化视角： IV 中性（Rank 62%）｜期限结构正常（Term 0.97）｜保护溢价中性（Skew 5.9pp）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（3D）±6.2% ｜ 12-04（10D）±10.5% ｜ 12-11（17D）±12.6% ｜ 12-18（24D）±14.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,069,751 | GEX Change vs 上次快照 -4,793,541 | Flip: Primary Flip: 103.86（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 382 / LOW 219 / INVALID 387
结构观察区: Primary Flip 103.86（全链重定价，覆盖 99%）
Put Wall 110（弱结构｜现价低于该位 4.0%）
最近结构参考: Flip 104（现价高于该位 1.7%）
量化视角： 正 Gamma（407万，无历史分位）｜正 Gamma 减弱（479万）｜现价位于 Flip 上方 1.70%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 110（Put Wall，弱结构） / 110（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 104（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 80.0P — Vol 2,722 | 最新价 $0.06 | OI 216→2864 (ΔOI +2648张) | ΔOI/Volume 97.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2648张（+1225.9% vs前日OI），连续性待观察（方向未知）
12-18 150.0C — Vol 2,770 | 最新价 $0.50 | OI 2109→4111 (ΔOI +2002张) | ΔOI/Volume 72.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2002张（+94.9% vs前日OI），连续性待观察（方向未知）
12-04 113.0P — Vol 1,595 | 最新价 $7.67 | OI 10→1561 (ΔOI +1551张) | ΔOI/Volume 97.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1551张（+15510.0% vs前日OI），连续性待观察（方向未知）
12-04 97.0P — Vol 1,695 | 最新价 $1.82 | OI 30→1543 (ΔOI +1513张) | ΔOI/Volume 89.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1513张（+5043.3% vs前日OI），连续性待观察（方向未知）
11-27 140.0C — Vol 1,207 | 最新价 $0.03 | OI 733→1840 (ΔOI +1107张) | ΔOI/Volume 91.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1107张（+151.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,821 张（Put 5,712 / Call 3,109），跨 3 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +5.9k / P +4.1k ｜ Activity MEDIUM △ ｜ 3D
12-04  C +2.6k / P +5.1k ｜ Activity HIGH ｜ 10D
12-11  C +0.7k / P +2.1k ｜ Activity HIGH ｜ 17D
12-18  C +5.4k / P +1.3k ｜ Activity MEDIUM △ ｜ 24D

📆 11-27 Forward Structure
存量OI: C 63.0k / P 36.4k，今日变化ΔOI: C +5.9k / P +4.1k，平值价格ATM: C $3.00 / P $3.53 ｜ ATM IV 80.9%，净 delta 敞口 36k shares
仓位参考: Max Pain 110 ｜ Call Wall 114（+7.9%，弱）（OI 7.2k） ｜ Put Wall 100（-5.3%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 80.9%｜历史 Rank 62%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 36,425 股

📆 12-04 Forward Structure
存量OI: C 13.1k / P 18.8k，今日变化ΔOI: C +2.6k / P +5.1k，平值价格ATM: C $5.80 / P $5.30 ｜ ATM IV 77.9%，净 delta 敞口 -118k shares
Top ΔOI: P 113 +1,551 ｜ P 97 +1,513 ｜ C 122 +679
仓位参考: Max Pain 125 ｜ Put Wall 113（+7.0%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜ATM IV 77.9%｜历史 Rank 62%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 117,937 股

📆 12-11 Forward Structure
存量OI: C 4.3k / P 7.1k，今日变化ΔOI: C +0.7k / P +2.1k，平值价格ATM: C $7.00 / P $6.29 ｜ ATM IV 77.4%，净 delta 敞口 -6k shares
仓位参考: Max Pain 125 ｜ Call Wall 110（+4.1%，弱）（OI 0.3k） ｜ Put Wall 100（-5.3%，弱）（OI 0.7k）
量化解读： 存量 Put 重｜ATM IV 77.4%｜历史 Rank 62%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 5,925 股

12-18（MEDIUM △）Top ΔOI: 150C +2,002 ｜ 140C +863
12-18（MEDIUM △）仓位参考: Max Pain 130 ｜ Put Wall 110（+4.1%）（OI 7.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/COIN_morning.json