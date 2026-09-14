# 期权晨报 2026-09-14（快照 10:20 ET）

📊 市场环境

SPY $761.06 ｜ QQQ $709.18
VIX 17.27 ↑9.0%（5D +12.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.9 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **近现价集中开仓**: 09-16 370C ΔOI +1,447（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 365.44 → 今开 359.95（-1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 367.73 ｜ 低 358.52

Options: P/C成交量 0.63 | OI比 0.76 | ATM IV 54.4% | Skew -2.6pp | Term 0.74 | ExpMove ±3.0%（近端） | Rank 56%
量化视角： IV 中性（Rank 56%）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.76）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-16（2D）±3.0% ｜ 09-18（4D）±3.9% ｜ 09-21（7D）±4.4% ｜ 09-23（9D）±5.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 31,167,778 | GEX Change vs 上次快照 -29,856,720 | Flip: Primary Flip: 356.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1306 / LOW 126 / INVALID 594
结构观察区: Primary Flip 356.18（全链重定价，覆盖 98%）
最近结构参考: Flip 356（现价高于该位 1.2%）
量化视角： 正 Gamma（3117万，无历史分位）｜正 Gamma 减弱（2986万）｜现价位于 Flip 上方 1.16%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 365（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 356（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 145.0P — Vol 23,742 | 最新价 $0.01 | OI 2547→24672 (ΔOI +22125张) | ΔOI/Volume 93.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22125张（+868.7% vs前日OI），连续性待观察（方向未知）
09-18 220.0P — Vol 18,376 | 最新价 $0.03 | OI 3723→21074 (ΔOI +17351张) | ΔOI/Volume 94.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17351张（+466.1% vs前日OI），连续性待观察（方向未知）
10-02 200.0P — Vol 10,679 | 最新价 $0.10 | OI 215→10104 (ΔOI +9889张) | ΔOI/Volume 92.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9889张（+4599.5% vs前日OI），连续性待观察（方向未知）
09-18 367.5C — Vol 11,923 | 最新价 $6.77 | OI 2059→8291 (ΔOI +6232张) | ΔOI/Volume 52.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6232张（+302.7% vs前日OI），连续性待观察（方向未知）
09-18 370.0C — Vol 19,675 | 最新价 $5.72 | OI 13153→19371 (ΔOI +6218张) | ΔOI/Volume 31.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6218张（+47.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 61,815 张（Put 49,365 / Call 12,450），跨 2 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 63.5k / P 48.4k，今日成交量: C 198.5k / P 125.3k，平值价格ATM: C $2.17 / P $2.08 ｜ ATM IV 54.4%，预期波动 ±1.2%，Max Pain 365
Top ΔOI: P 360 +4,036 ｜ C 370 +2,854 ｜ C 367 +2,469

📆 Forward Expiration Structure

09-16  C +9.2k / P +5.6k ｜ Activity HIGH ｜ 2D
09-18  C +38.4k / P +67.3k ｜ Activity MEDIUM △ ｜ 4D
09-21  C +1.8k / P +1.3k ｜ Activity HIGH ｜ 7D
09-23  C +1.1k / P +0.7k ｜ Activity HIGH ｜ 9D

📆 09-16 Forward Structure
存量OI: C 25.9k / P 16.3k，今日变化ΔOI: C +9.2k / P +5.6k，平值价格ATM: C $5.45 / P $5.27 ｜ ATM IV 47.2%，净 delta 敞口 62k shares
Top ΔOI: C 370 +1,447 ｜ C 365 +1,134
仓位参考: Max Pain 362 ｜ Call Wall 370（+2.7%，弱）（OI 3.3k）
量化解读： 存量 Call 重｜ATM IV 47.2%｜历史 Rank 56%（近端代理）｜IV/RV 0.93×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 62,001 股

09-18（MEDIUM △）Top ΔOI: 367C +6,232
09-18（MEDIUM △）仓位参考: Max Pain 360

📆 09-21 Forward Structure
存量OI: C 5.9k / P 5.0k，今日变化ΔOI: C +1.8k / P +1.3k，平值价格ATM: C $8.23 / P $7.75 ｜ ATM IV 39.2%，净 delta 敞口 1k shares
Top ΔOI: C 385 +205
仓位参考: Max Pain 365 ｜ Call Wall 380（+5.5%，弱）（OI 0.8k） ｜ Put Wall 345（-4.3%）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 39.2%｜历史 Rank 56%（近端代理）｜IV/RV 0.78×（近似）｜净 delta 敞口 正 1,419 股

📆 09-23 Forward Structure
存量OI: C 4.5k / P 2.5k，今日变化ΔOI: C +1.1k / P +0.7k，平值价格ATM: C $9.50 / P $8.85 ｜ ATM IV 40.2%，净 delta 敞口 5k shares
Top ΔOI: C 390 +393
仓位参考: Max Pain 368 ｜ Call Wall 390（+8.2%，弱）（OI 0.6k） ｜ Put Wall 382.5（+6.2%）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 40.2%｜历史 Rank 56%（近端代理）｜IV/RV 0.80×（近似）｜净 delta 敞口 正 4,811 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/TSLA_morning.json