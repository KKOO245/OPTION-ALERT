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
🟡 **近现价集中开仓**: 11-06 150C ΔOI +504（距现价 +4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 146.01 → 今开 144.43（-1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 152.21 ｜ 低 144.21

Options: P/C成交量 0.56 | OI比 0.80 | ATM IV 76.4% | Skew 1.1pp | Term 0.92 | ExpMove ±8.7%（近端） | Rank 43%
量化视角： IV 中性（Rank 43%）｜期限结构正常（Term 0.92）｜保护溢价薄（Skew 1.1pp）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（4D）±8.7% ｜ 11-06（11D）±11.3% ｜ 11-13（18D）±13.7% ｜ 11-20（25D）±16.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 32,799,920 | GEX Change vs 上次快照 26,449,989 | Flip: Primary Flip: 135.57（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 612 / LOW 58 / INVALID 186
结构观察区: Primary Flip 135.57（全链重定价，覆盖 100%）
Call Wall 135（弱结构｜现价高于该位 6.4%）
最近结构参考: Flip 136（现价高于该位 6.0%）
量化视角： 正 Gamma（3280万，无历史分位）｜正 Gamma 增强（+2645万）｜现价位于 Flip 上方 6.00%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（Call Wall，弱结构）；上方 147（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 136（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 152.5C — Vol 34,005 | 最新价 $3.70 | OI 5848→37825 (ΔOI +31977张) | ΔOI/Volume 94.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31977张（+546.8% vs前日OI），连续性待观察（方向未知）
10-30 160.0C — Vol 32,193 | 最新价 $1.80 | OI 6726→34397 (ΔOI +27671张) | ΔOI/Volume 86.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27671张（+411.4% vs前日OI），连续性待观察（方向未知）
10-30 90.0P — Vol 27,810 | 最新价 $0.07 | OI 3885→30745 (ΔOI +26860张) | ΔOI/Volume 96.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26860张（+691.4% vs前日OI），连续性待观察（方向未知）
10-30 162.5C — Vol 24,635 | 最新价 $1.39 | OI 3128→24543 (ΔOI +21415张) | ΔOI/Volume 86.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21415张（+684.6% vs前日OI），连续性待观察（方向未知）
10-30 155.0C — Vol 24,818 | 最新价 $2.90 | OI 5104→25884 (ΔOI +20780张) | ΔOI/Volume 83.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20780张（+407.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 128,703 张（Put 26,860 / Call 101,843），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +128.2k / P +60.7k ｜ Activity HIGH ｜ 4D
11-06  C +2.1k / P +4.5k ｜ Activity HIGH ｜ 11D
11-13  C +3.0k / P +2.8k ｜ Activity HIGH ｜ 18D
11-20  C +2.3k / P +3.0k ｜ Activity HIGH ｜ 25D

📆 10-30 Forward Structure
存量OI: C 209.4k / P 166.7k，今日变化ΔOI: C +128.2k / P +60.7k，平值价格ATM: C $7.35 / P $5.15 ｜ ATM IV 76.4%，净 delta 敞口 3.7M shares
Top ΔOI: C 152 +31,977 ｜ C 160 +27,671 ｜ P 90 +26,860
仓位参考: Max Pain 147 ｜ Call Wall 152.5（+6.1%，弱）（OI 37.8k）
量化解读： 存量 Call 重｜ATM IV 76.4%｜历史 Rank 43%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,669,365 股

📆 11-06 Forward Structure
存量OI: C 20.1k / P 45.8k，今日变化ΔOI: C +2.1k / P +4.5k，平值价格ATM: C $9.02 / P $7.27 ｜ ATM IV 75.2%，净 delta 敞口 17k shares
Top ΔOI: C 150 +504
仓位参考: Max Pain 158 ｜ Call Wall 150（+4.4%，弱）（OI 1.3k） ｜ Put Wall 155（+7.9%，弱）（OI 3.6k）
量化解读： 存量 Put 重｜ATM IV 75.2%｜历史 Rank 43%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 17,093 股

📆 11-13 Forward Structure
存量OI: C 17.6k / P 37.8k，今日变化ΔOI: C +3.0k / P +2.8k，平值价格ATM: C $11.95 / P $7.80 ｜ ATM IV 73.6%，净 delta 敞口 -27k shares
Top ΔOI: C 210 +2,349
仓位参考: Max Pain 160 ｜ Call Wall 144（+0.2%，弱）（OI 0.8k） ｜ Put Wall 155（+7.9%，弱）（OI 2.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 73.6%｜历史 Rank 43%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 26,805 股

📆 11-20 Forward Structure
存量OI: C 144.8k / P 106.0k，今日变化ΔOI: C +2.3k / P +3.0k，平值价格ATM: C $13.20 / P $10.30 ｜ ATM IV 73.0%，净 delta 敞口 -57k shares
Top ΔOI: C 200 +809 ｜ C 152 +302 ｜ P 149 +275
仓位参考: Max Pain 135 ｜ Call Wall 135（-6.1%）（OI 42.3k） ｜ Put Wall 130（-9.5%，弱）（OI 4.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 73.0%｜历史 Rank 43%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 负 57,055 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/MSTR_morning.json