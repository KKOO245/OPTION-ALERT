# 期权晨报 2026-09-21（快照 10:20 ET）

📊 市场环境

SPY $767.46 ｜ QQQ $734.29
VIX 14.85 ↑0.3%（5D -13.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 32.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-23 220C ΔOI +2,643（距现价 -1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 222.27 → 今开 222.93（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 224.93 ｜ 低 221.56

Options: P/C成交量 0.54 | OI比 0.93 | ATM IV 37.5% | Skew 3.5pp | Term 0.82 | ExpMove ±2.0%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价中性（Skew 3.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.93×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-23（2D）±2.0% ｜ 09-25（4D）±2.8% ｜ 09-28（7D）±3.2% ｜ 09-30（9D）±3.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 493,713,899 | GEX Change vs 上次快照 175,948,829 | Flip: Primary Flip: 211.99（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 729 / LOW 193 / INVALID 548
结构观察区: Primary Flip 211.99（全链重定价，覆盖 99%）
Call Wall 230（弱结构｜现价低于该位 2.9%）
最近结构参考: Call Wall 230（现价低于该位 2.9%）
量化视角： 正 Gamma（4.94亿，无历史分位）｜正 Gamma 增强（+1.76亿）｜现价位于 Flip 上方 5.37%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 218（MaxPain，仅结算参考）；上方 230（Call Wall，弱结构）。
• Gamma 区域：切换参考 212（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 222.5C — Vol 57,954 | 最新价 $3.25 | OI 22326→65673 (ΔOI +43347张) | ΔOI/Volume 74.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增43347张（+194.2% vs前日OI），连续性待观察（方向未知）
09-25 230.0C — Vol 57,529 | 最新价 $0.88 | OI 26515→62908 (ΔOI +36393张) | ΔOI/Volume 63.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增36393张（+137.2% vs前日OI），连续性待观察（方向未知）
09-25 105.0P — Vol 26,811 | 最新价 $0.01 | OI 20669→47479 (ΔOI +26810张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26810张（+129.7% vs前日OI），连续性待观察（方向未知）
09-25 227.5C — Vol 21,915 | 最新价 $1.40 | OI 14641→29790 (ΔOI +15149张) | ΔOI/Volume 69.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15149张（+103.5% vs前日OI），连续性待观察（方向未知）
09-25 165.0P — Vol 10,419 | 最新价 $0.03 | OI 1793→11720 (ΔOI +9927张) | ΔOI/Volume 95.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9927张（+553.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 131,626 张（Put 36,737 / Call 94,889），跨 1 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 75.9k / P 70.5k，今日成交量: C 195.1k / P 105.0k，平值价格ATM: C $1.05 / P $0.77 ｜ ATM IV 37.5%，预期波动 ±0.8%，Max Pain 218
Top ΔOI: C 222 +7,978 ｜ C 225 +4,038 ｜ P 215 +3,516

📆 Forward Expiration Structure

09-23  C +12.1k / P +14.9k ｜ Activity HIGH ｜ 2D
09-25  C +121.5k / P +79.2k ｜ Activity HIGH ｜ 4D
09-28  C +5.9k / P +2.0k ｜ Activity HIGH ｜ 7D
09-30  C +1.9k / P +2.6k ｜ Activity HIGH ｜ 9D

📆 09-23 Forward Structure
存量OI: C 50.5k / P 32.6k，今日变化ΔOI: C +12.1k / P +14.9k，平值价格ATM: C $2.42 / P $2.07 ｜ ATM IV 32.2%，净 delta 敞口 304k shares
Top ΔOI: C 220 +2,643 ｜ C 227 +2,378
仓位参考: Max Pain 218 ｜ Call Wall 225（+0.7%，弱）（OI 11.2k） ｜ Put Wall 205（-8.2%，弱）（OI 4.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 32.2%｜历史 Rank 26%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 304,091 股

📆 09-25 Forward Structure
存量OI: C 408.9k / P 303.5k，今日变化ΔOI: C +121.5k / P +79.2k，平值价格ATM: C $3.29 / P $2.87 ｜ ATM IV 31.8%，净 delta 敞口 3.5M shares
Top ΔOI: C 222 +43,347 ｜ C 230 +36,393
仓位参考: Max Pain 220 ｜ Call Wall 222.5（-0.4%，弱）（OI 65.7k） ｜ Put Wall 210（-6.0%，弱）（OI 30.5k）
量化解读： 存量 Call 重｜ATM IV 31.8%｜历史 Rank 26%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,503,520 股

📆 09-28 Forward Structure
存量OI: C 22.3k / P 14.6k，今日变化ΔOI: C +5.9k / P +2.0k，平值价格ATM: C $3.75 / P $3.36 ｜ ATM IV 27.9%，净 delta 敞口 183k shares
Top ΔOI: C 225 +2,192 ｜ C 230 +1,255 ｜ C 220 +839
仓位参考: Max Pain 215 ｜ Call Wall 225（+0.7%）（OI 6.5k） ｜ Put Wall 205（-8.2%，弱）（OI 2.6k）
量化解读： 存量 Call 重｜ATM IV 27.9%｜历史 Rank 26%（近端代理）｜IV/RV 0.86×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 182,535 股

📆 09-30 Forward Structure
存量OI: C 8.6k / P 10.7k，今日变化ΔOI: C +1.9k / P +2.6k，平值价格ATM: C $4.50 / P $4.00 ｜ ATM IV 29.9%，净 delta 敞口 17k shares
Top ΔOI: P 212 +1,513 ｜ C 217 -395 ｜ C 220 +381
仓位参考: Max Pain 215 ｜ Call Wall 220（-1.5%，弱）（OI 1.6k） ｜ Put Wall 212.5（-4.9%，弱）（OI 3.3k）
量化解读： 存量 Put 重｜ATM IV 29.9%｜历史 Rank 26%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 正 16,530 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/NVDA_morning.json