# 期权晨报 2026-09-18（快照 10:41 ET）

📊 市场环境

SPY $762.74 ｜ QQQ $721.45
VIX 15.50 ↑0.4%（5D -2.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-21 375C ΔOI +1,732（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 366.20 → 今开 369.28（+0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 370.90 ｜ 低 360.75

Options: P/C成交量 0.75 | OI比 0.81 | ATM IV 54.7% | Skew -4.6pp | Term 0.75 | ExpMove ±2.3%（近端） | Rank 57%
量化视角： IV 中性（Rank 57%）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.75×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-21（3D）±2.3% ｜ 09-23（5D）±3.5% ｜ 09-25（7D）±4.4% ｜ 09-28（10D）±4.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 65,217,954 | GEX Change vs 上次快照 -60,208,068 | Flip: Primary Flip: 357.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1113 / LOW 150 / INVALID 737
结构观察区: Primary Flip 357.44（全链重定价，覆盖 98%）
最近结构参考: Flip 357（现价高于该位 1.4%）
量化视角： 正 Gamma（6522万，无历史分位）｜正 Gamma 减弱（6021万）｜现价位于 Flip 上方 1.43%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 360（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 357（全链重定价，覆盖 98%）。
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
存量OI: C 629.1k / P 510.6k，今日成交量: C 473.7k / P 357.0k，平值价格ATM: C $2.68 / P $1.58 ｜ ATM IV 54.7%，预期波动 ±1.2%，Max Pain 360
Top ΔOI: P 360 +12,526 ｜ C 380 +7,388 ｜ C 375 +6,003

📆 Forward Expiration Structure

09-21  C +9.1k / P +9.1k ｜ Activity HIGH ｜ 3D
09-23  C +3.8k / P +3.1k ｜ Activity HIGH ｜ 5D
09-25  C +12.4k / P +33.8k ｜ Activity HIGH ｜ 7D
09-28  C +2.1k / P +1.1k ｜ Activity HIGH ｜ 10D

📆 09-21 Forward Structure
存量OI: C 33.1k / P 29.9k，今日变化ΔOI: C +9.1k / P +9.1k，平值价格ATM: C $4.74 / P $3.70 ｜ ATM IV 30.8%，净 delta 敞口 -57k shares
Top ΔOI: C 375 +1,732
仓位参考: Max Pain 365 ｜ Call Wall 370（+2.1%，弱）（OI 3.3k） ｜ Put Wall 350（-3.5%，弱）（OI 2.2k）
量化解读： 存量两侧均衡｜ATM IV 30.8%｜历史 Rank 57%（近端代理）｜IV/RV 0.68×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 56,581 股

📆 09-23 Forward Structure
存量OI: C 16.4k / P 13.0k，今日变化ΔOI: C +3.8k / P +3.1k，平值价格ATM: C $6.95 / P $5.80 ｜ ATM IV 36.7%，净 delta 敞口 -73k shares
Top ΔOI: P 365 +857 ｜ P 370 +734 ｜ C 367 +470
仓位参考: Max Pain 365 ｜ Call Wall 380（+4.8%，弱）（OI 1.2k） ｜ Put Wall 330（-9.0%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 36.7%｜历史 Rank 57%（近端代理）｜IV/RV 0.82×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 73,128 股

📆 09-25 Forward Structure
存量OI: C 95.4k / P 111.1k，今日变化ΔOI: C +12.4k / P +33.8k，平值价格ATM: C $8.55 / P $7.33 ｜ ATM IV 38.5%，净 delta 敞口 -47k shares
仓位参考: Max Pain 360 ｜ Call Wall 385（+6.2%，弱）（OI 6.9k） ｜ Put Wall 350（-3.5%，弱）（OI 4.2k）
量化解读： 存量两侧均衡｜ATM IV 38.5%｜历史 Rank 57%（近端代理）｜IV/RV 0.85×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 47,372 股

📆 09-28 Forward Structure
存量OI: C 6.2k / P 3.4k，今日变化ΔOI: C +2.1k / P +1.1k，平值价格ATM: C $9.40 / P $8.27 ｜ ATM IV 36.3%，净 delta 敞口 -6k shares
Top ΔOI: C 390 +308
仓位参考: Max Pain 360 ｜ Call Wall 375（+3.4%，弱）（OI 0.5k） ｜ Put Wall 355（-2.1%）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 36.3%｜历史 Rank 57%（近端代理）｜IV/RV 0.81×（近似）｜净 delta 敞口 负 6,102 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/TSLA_morning.json