# 期权晨报 2026-09-18（快照 10:20 ET）

📊 市场环境

SPY $758.97 ｜ QQQ $716.84
VIX 15.53 ↑0.6%（5D -2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-21 375C ΔOI +1,732（距现价 +2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 366.20 → 今开 369.28（+0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 370.90 ｜ 低 360.75

Options: P/C成交量 0.65 | OI比 0.81 | ATM IV 57.7% | Skew -0.9pp | Term 0.71 | ExpMove ±2.4%（近端） | Rank 66%
量化视角： IV 中性（Rank 66%）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-21（3D）±2.4% ｜ 09-23（5D）±3.6% ｜ 09-25（7D）±4.3% ｜ 09-28（10D）±4.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 113,228,109 | GEX Change vs 上次快照 -12,197,913 | Flip: Primary Flip: 356.85（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1230 / LOW 150 / INVALID 620
结构观察区: Primary Flip 356.85（全链重定价，覆盖 100%）
Call Wall 400（弱结构｜现价低于该位 8.6%）
最近结构参考: Flip 357（现价高于该位 2.5%）
量化视角： 正 Gamma（1.13亿，无历史分位）｜正 Gamma 减弱（1220万）｜现价位于 Flip 上方 2.48%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 360（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 357（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 160.0P — Vol 16 | 最新价 $0.01 | OI 381→13593 (ΔOI +13212张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13212张（+3467.7% vs前日OI），连续性待观察（方向未知）
09-18 360.0P — Vol 8,278 | 最新价 $0.35 | OI 12913→25439 (ΔOI +12526张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12526张（+97.0% vs前日OI），连续性待观察（方向未知）
09-25 180.0P — Vol 8,772（Yahoo补） | 最新价 $0.01 | OI 227→8972 (ΔOI +8745张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8745张（+3852.4% vs前日OI），连续性待观察（方向未知）
09-18 380.0C — Vol 8,196 | 最新价 $0.17 | OI 22079→29467 (ΔOI +7388张) | ΔOI/Volume 90.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7388张（+33.5% vs前日OI），连续性待观察（方向未知）
09-18 375.0C — Vol 12,677 | 最新价 $0.57 | OI 14782→20785 (ΔOI +6003张) | ΔOI/Volume 47.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6003张（+40.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 47,874 张（Put 34,483 / Call 13,391），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 629.1k / P 510.6k，今日成交量: C 328.3k / P 211.8k，平值价格ATM: C $1.85 / P $2.77 ｜ ATM IV 57.7%，预期波动 ±1.3%，Max Pain 360
Top ΔOI: P 360 +12,526 ｜ C 380 +7,388 ｜ C 375 +6,003

📆 Forward Expiration Structure

09-21  C +9.1k / P +9.1k ｜ Activity HIGH ｜ 3D
09-23  C +3.8k / P +3.1k ｜ Activity HIGH ｜ 5D
09-25  C +12.4k / P +33.8k ｜ Activity HIGH ｜ 7D
09-28  C +2.1k / P +1.1k ｜ Activity HIGH ｜ 10D

📆 09-21 Forward Structure
存量OI: C 33.1k / P 29.9k，今日变化ΔOI: C +9.1k / P +9.1k，平值价格ATM: C $3.97 / P $4.81 ｜ ATM IV 31.5%，净 delta 敞口 -29k shares
Top ΔOI: C 375 +1,732
仓位参考: Max Pain 365 ｜ Call Wall 400（+9.4%）（OI 5.3k） ｜ Put Wall 350（-4.3%，弱）（OI 2.2k）
量化解读： 存量两侧均衡｜ATM IV 31.5%｜历史 Rank 66%（近端代理）｜IV/RV 0.70×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 28,787 股

📆 09-23 Forward Structure
存量OI: C 16.4k / P 13.0k，今日变化ΔOI: C +3.8k / P +3.1k，平值价格ATM: C $6.43 / P $6.83 ｜ ATM IV 37.1%，净 delta 敞口 -64k shares
Top ΔOI: P 365 +857 ｜ P 370 +734 ｜ C 367 +470
仓位参考: Max Pain 365 ｜ Call Wall 400（+9.4%，弱）（OI 1.5k） ｜ Put Wall 330（-9.8%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 37.1%｜历史 Rank 66%（近端代理）｜IV/RV 0.82×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 63,584 股

📆 09-25 Forward Structure
存量OI: C 95.4k / P 111.1k，今日变化ΔOI: C +12.4k / P +33.8k，平值价格ATM: C $7.60 / P $8.30 ｜ ATM IV 38.5%，净 delta 敞口 -33k shares
仓位参考: Max Pain 360 ｜ Call Wall 400（+9.4%，弱）（OI 8.0k） ｜ Put Wall 350（-4.3%，弱）（OI 4.2k）
量化解读： 存量两侧均衡｜ATM IV 38.5%｜历史 Rank 66%（近端代理）｜IV/RV 0.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 33,340 股

📆 09-28 Forward Structure
存量OI: C 6.2k / P 3.4k，今日变化ΔOI: C +2.1k / P +1.1k，平值价格ATM: C $8.80 / P $8.74 ｜ ATM IV 35.8%，净 delta 敞口 -3k shares
Top ΔOI: C 400 +370 ｜ C 390 +308
仓位参考: Max Pain 360 ｜ Call Wall 400（+9.4%）（OI 0.9k） ｜ Put Wall 355（-2.9%）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 35.8%｜历史 Rank 66%（近端代理）｜IV/RV 0.80×（近似）｜净 delta 敞口 负 3,161 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/TSLA_morning.json