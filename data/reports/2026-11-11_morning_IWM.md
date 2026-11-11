# 期权晨报 2026-11-11（快照 10:20 ET）

📊 市场环境

SPY $759.90 ｜ QQQ $690.38
VIX 18.31 ↓5.9%（5D +10.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-12 287C ΔOI +24,261（距现价 +1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-12 287C ΔOI +24,261 占该期限总 OI 36.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 280.58 → 今开 282.99（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 283.08 ｜ 低 281.48

Options: P/C成交量 0.88 | OI比 0.48 | ATM IV 23.1% | Skew 1.5pp | Term 0.81 | ExpMove ±0.9%（近端） | Rank 42%
量化视角： IV 中性（Rank 42%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价薄（Skew 1.5pp）｜存量 Call 偏重（OI比 0.48）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.88×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.48×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-12（1D）±0.9% ｜ 11-13（2D）±1.2% ｜ 11-16（5D）±1.4% ｜ 11-17（6D）±1.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -162,826,640 | GEX Change vs 上次快照 288,938,651 | Flip: Primary Flip: 283.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1485 / LOW 198 / INVALID 1043
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 283.03（全链重定价，覆盖 98%）
Put Wall 270（弱结构｜现价高于该位 4.5%） | Call Wall 290（弱结构｜现价低于该位 2.7%）
最近结构参考: Flip 283（现价低于该位 0.3%）
量化视角： 负 Gamma（1.63亿，无历史分位）｜负 Gamma 缓解（+2.89亿）｜现价位于 Flip 下方 0.35%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构） / 280（MaxPain，仅结算参考）；上方 290（Call Wall，弱结构）。
• Gamma 区域：切换参考 283（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 275.0P — Vol 30,678 | 最新价 $2.27 | OI 1044→31348 (ΔOI +30304张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30304张（+2902.7% vs前日OI），连续性待观察（方向未知）
11-12 287.0C — Vol 25,415 | 最新价 $0.10 | OI 1089→25350 (ΔOI +24261张) | ΔOI/Volume 95.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24261张（+2227.8% vs前日OI），连续性待观察（方向未知）
11-20 262.0P — Vol 20,075 | 最新价 $0.34 | OI 44603→63571 (ΔOI +18968张) | ΔOI/Volume 94.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18968张（+42.5% vs前日OI），连续性待观察（方向未知）
11-20 273.0P — Vol 22,120 | 最新价 $1.24 | OI 6339→24642 (ΔOI +18303张) | ΔOI/Volume 82.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18303张（+288.7% vs前日OI），连续性待观察（方向未知）
11-20 294.0C — Vol 5,732 | 最新价 $0.18 | OI 23074→26329 (ΔOI +3255张) | ΔOI/Volume 56.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3255张（+14.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 95,091 张（Put 67,575 / Call 27,516），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $9M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 84.5k / P 40.6k，今日成交量: C 66.9k / P 58.6k，平值价格ATM: C $0.66 / P $0.76 ｜ ATM IV 23.1%，预期波动 ±0.5%，Max Pain 280
Top ΔOI: C 281 +2,993 ｜ C 280 +2,328 ｜ C 282 +1,924

📆 Forward Expiration Structure

11-12  C +26.2k / P +2.3k ｜ Activity HIGH ｜ 1D
11-13  C +6.2k / P +5.9k ｜ Activity HIGH ｜ 2D
11-16  C +5.4k / P +3.9k ｜ Activity HIGH ｜ 5D
11-17  C +1.7k / P +2.5k ｜ Activity HIGH ｜ 6D

📆 11-12 Forward Structure
存量OI: C 48.8k / P 17.8k，今日变化ΔOI: C +26.2k / P +2.3k，平值价格ATM: C $1.24 / P $1.31 ｜ ATM IV 19.3%，净 delta 敞口 217k shares
Top ΔOI: C 287 +24,261 ｜ C 277 +491 ｜ P 274 +434
仓位参考: Max Pain 278 ｜ Call Wall 287（+1.8%）（OI 25.4k） ｜ Put Wall 265（-6.0%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 19.3%｜历史 Rank 42%（近端代理）｜IV/RV 0.80×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 216,996 股

📆 11-13 Forward Structure
存量OI: C 111.7k / P 183.2k，今日变化ΔOI: C +6.2k / P +5.9k，平值价格ATM: C $1.75 / P $1.60 ｜ ATM IV 19.4%，净 delta 敞口 76k shares
Top ΔOI: P 278 +2,187 ｜ C 285 +1,635 ｜ P 280 +923
仓位参考: Max Pain 279 ｜ Call Wall 302（+7.1%，弱）（OI 13.7k） ｜ Put Wall 272（-3.6%，弱）（OI 13.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 19.4%｜历史 Rank 42%（近端代理）｜IV/RV 0.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 75,593 股

📆 11-16 Forward Structure
存量OI: C 13.7k / P 18.9k，今日变化ΔOI: C +5.4k / P +3.9k，平值价格ATM: C $2.28 / P $1.80 ｜ ATM IV 15.7%，净 delta 敞口 159k shares
Top ΔOI: C 285 +1,666 ｜ C 282 +1,446 ｜ P 277 +892
仓位参考: Max Pain 279 ｜ Call Wall 285（+1.0%，弱）（OI 2.3k） ｜ Put Wall 270（-4.3%）（OI 3.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 15.7%｜历史 Rank 42%（近端代理）｜IV/RV 0.65×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 158,768 股

📆 11-17 Forward Structure
存量OI: C 6.4k / P 10.4k，今日变化ΔOI: C +1.7k / P +2.5k，平值价格ATM: C $2.87 / P $2.27 ｜ ATM IV 16.5%，净 delta 敞口 26k shares
Top ΔOI: P 275 +398 ｜ P 276 +392 ｜ P 277 +358
仓位参考: Max Pain 278 ｜ Call Wall 289（+2.5%，弱）（OI 0.6k） ｜ Put Wall 260（-7.8%）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 16.5%｜历史 Rank 42%（近端代理）｜IV/RV 0.69×（近似）｜净 delta 敞口 正 25,619 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/IWM_morning.json