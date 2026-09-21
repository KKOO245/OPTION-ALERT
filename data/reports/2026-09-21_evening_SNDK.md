# 期权晚报 2026-09-21（快照 16:40 ET）

📊 市场环境

SPY $773.50 ｜ QQQ $741.47
VIX 14.87 ↑0.4%（5D -13.0%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 33.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 1800C ΔOI +877（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 900C ΔOI +2,050 占该期限总 OI 19.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,826.66 → 收盘 1,766.64（-3.3%） ｜ 今日高 1834.49 ｜ 低 1737.01 ｜ 昨收 1,791.82 → 收盘 1,766.64（-1.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.67 | OI比 1.34 | ATM IV 74.3% | Skew -4.0pp | Term 0.97 | ExpMove ±6.1%（近端） | Rank 29%
量化视角： IV 中性（Rank 29%）｜期限结构正常（Term 0.97）｜Put 保护异常便宜（Skew -4.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.34×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（4D）±6.1% ｜ 10-02（11D）±10.9% ｜ 10-09（18D）±12.9% ｜ 10-16（25D）±15.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,087,093 | GEX Change vs 上次快照 -388,045 | Flip: Primary Flip: 1640.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1997 / LOW 273 / INVALID 874
结构观察区: Primary Flip 1640.61（全链重定价，覆盖 100%）
Call Wall 1,600（弱结构｜现价高于该位 10.4%）
最近结构参考: Flip 1641（现价高于该位 7.7%）
量化视角： 正 Gamma（609万，无历史分位）｜正 Gamma 减弱（39万）｜现价位于 Flip 上方 7.68%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,650（MaxPain，仅结算参考） / 1,600（Call Wall，弱结构）。
• Gamma 区域：切换参考 1641（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 900.0C — Vol 2,050（Yahoo补） | 最新价 $827.95 | OI 0→2050 (ΔOI +2050张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2050张（前日OI缺失），连续性待观察（方向未知）
10-02 2250.0C — Vol 521 | 最新价 $7.00 | OI 35→1354 (ΔOI +1319张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1319张（+3768.6% vs前日OI），连续性待观察（方向未知）
09-25 1000.0P — Vol 102 | 最新价 $0.05 | OI 324→1454 (ΔOI +1130张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1130张（+348.8% vs前日OI），连续性待观察（方向未知）
09-25 1800.0C — Vol 7,294 | 最新价 $40.90 | OI 890→1767 (ΔOI +877张) | ΔOI/Volume 12.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增877张（+98.5% vs前日OI），连续性待观察（方向未知）
09-25 1900.0C — Vol 3,366 | 最新价 $16.25 | OI 484→1340 (ΔOI +856张) | ΔOI/Volume 25.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增856张（+176.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,232 张（Put 1,130 / Call 5,102），跨 3 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +10.0k / P +14.1k ｜ Activity HIGH ｜ 4D
10-02  C +2.8k / P +2.1k ｜ Activity HIGH ｜ 11D
10-09  C +2.4k / P +0.2k ｜ Activity HIGH ｜ 18D
10-16  C +2.2k / P +3.0k ｜ Activity HIGH ｜ 25D

📆 09-25 Forward Structure
存量OI: C 29.3k / P 39.1k，今日变化ΔOI: C +10.0k / P +14.1k，平值价格ATM: C $55.34 / P $53.07 ｜ ATM IV 74.3%，净 delta 敞口 105k shares
Top ΔOI: C 1800 +877 ｜ C 1900 +856
仓位参考: Max Pain 1,650 ｜ Call Wall 1800（+1.9%，弱）（OI 1.8k） ｜ Put Wall 1700（-3.8%，弱）（OI 1.0k）
量化解读： 存量 Put 重｜ATM IV 74.3%｜历史 Rank 29%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 104,704 股

📆 10-02 Forward Structure
存量OI: C 17.4k / P 12.9k，今日变化ΔOI: C +2.8k / P +2.1k，平值价格ATM: C $95.00 / P $97.00 ｜ ATM IV 75.9%，净 delta 敞口 -5k shares
Top ΔOI: C 2250 +1,319 ｜ C 2000 +269 ｜ C 1900 +233
仓位参考: Max Pain 1,600 ｜ Call Wall 1600（-9.4%）（OI 4.4k） ｜ Put Wall 1680（-4.9%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 75.9%｜历史 Rank 29%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 5,242 股

📆 10-09 Forward Structure
存量OI: C 5.9k / P 4.7k，今日变化ΔOI: C +2.4k / P +0.2k，平值价格ATM: C $112.95 / P $114.33 ｜ ATM IV 71.9%，净 delta 敞口 208k shares
Top ΔOI: C 900 +2,050 ｜ C 1650 +47
仓位参考: Max Pain 1,440 ｜ Put Wall 1690（-4.3%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 71.9%｜历史 Rank 29%（近端代理）｜IV/RV 1.01×（近似）｜净 delta 敞口 正 208,145 股

📆 10-16 Forward Structure
存量OI: C 30.6k / P 39.7k，今日变化ΔOI: C +2.2k / P +3.0k，平值价格ATM: C $132.92 / P $134.00 ｜ ATM IV 72.1%，净 delta 敞口 11k shares
Top ΔOI: C 2500 +419 ｜ P 1610 +282
仓位参考: Max Pain 1,600 ｜ Call Wall 1800（+1.9%，弱）（OI 1.0k） ｜ Put Wall 1600（-9.4%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 72.1%｜历史 Rank 29%（近端代理）｜IV/RV 1.01×（近似）｜净 delta 敞口 正 11,378 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/SNDK_evening.json