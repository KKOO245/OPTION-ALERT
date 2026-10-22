# 期权晨报 2026-10-22（快照 10:20 ET）

📊 市场环境

SPY $766.63 ｜ QQQ $710.98
VIX 17.91 ↑7.4%（5D +8.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 222C ΔOI +6,209（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 221.97 → 今开 217.23（-2.1%） | 较昨收变动（含盘初走势） ｜ 今日高 218.88 ｜ 低 215.38

Options: P/C成交量 0.60 | OI比 0.80 | ATM IV 39.9% | Skew 3.1pp | Term 1.01 | ExpMove ±1.9%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构正常（Term 1.01）｜保护溢价中性（Skew 3.1pp）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（1D）±1.9% ｜ 10-26（4D）±2.6% ｜ 10-28（6D）±3.5% ｜ 10-30（8D）±4.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 115,299,991 | GEX Change vs 上次快照 -241,643,215 | Flip: Primary Flip: 214.62（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 791 / LOW 180 / INVALID 487
结构观察区: Primary Flip 214.62（全链重定价，覆盖 97%）
Call Wall 230（弱结构｜现价低于该位 5.7%）
最近结构参考: Flip 215（现价高于该位 1.1%）
量化视角： 正 Gamma（1.15亿，无历史分位）｜正 Gamma 减弱（2.42亿）｜现价位于 Flip 上方 1.08%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 220（MaxPain，仅结算参考） / 230（Call Wall，弱结构）。
• Gamma 区域：切换参考 215（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 235.0C — Vol 13,178 | 最新价 $0.06 | OI 16267→25261 (ΔOI +8994张) | ΔOI/Volume 68.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8994张（+55.3% vs前日OI），连续性待观察（方向未知）
10-23 222.5C — Vol 64,826 | 最新价 $2.22 | OI 42897→49106 (ΔOI +6209张) | ΔOI/Volume 9.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6209张（+14.5% vs前日OI），连续性待观察（方向未知）
10-30 210.0P — Vol 10,914 | 最新价 $1.11 | OI 10415→16095 (ΔOI +5680张) | ΔOI/Volume 52.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5680张（+54.5% vs前日OI），连续性待观察（方向未知）
10-23 227.5C — Vol 29,319 | 最新价 $0.60 | OI 46726→52364 (ΔOI +5638张) | ΔOI/Volume 19.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5638张（+12.1% vs前日OI），连续性待观察（方向未知）
10-30 197.5P — Vol 6,538 | 最新价 $0.28 | OI 1614→6956 (ΔOI +5342张) | ΔOI/Volume 81.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5342张（+331.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 31,863 张（Put 11,022 / Call 20,841），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +33.4k / P +23.7k ｜ Activity HIGH ｜ 1D
10-26  C +2.8k / P +5.3k ｜ Activity HIGH ｜ 4D
10-28  C +5.4k / P +4.7k ｜ Activity HIGH ｜ 6D
10-30  C +14.5k / P +24.1k ｜ Activity HIGH ｜ 8D

📆 10-23 Forward Structure
存量OI: C 475.1k / P 379.1k，今日变化ΔOI: C +33.4k / P +23.7k，平值价格ATM: C $1.76 / P $2.30 ｜ ATM IV 39.9%，净 delta 敞口 -191k shares
Top ΔOI: C 235 +8,994 ｜ C 222 +6,209 ｜ C 227 +5,638
仓位参考: Max Pain 220 ｜ Call Wall 230（+6.0%，弱）（OI 58.5k） ｜ Put Wall 210（-3.2%，弱）（OI 18.2k）
量化解读： 存量 Call 重｜ATM IV 39.9%｜历史 Rank 40%（近端代理）｜IV/RV 1.65×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 190,886 股

📆 10-26 Forward Structure
存量OI: C 42.5k / P 37.3k，今日变化ΔOI: C +2.8k / P +5.3k，平值价格ATM: C $2.59 / P $3.10 ｜ ATM IV 30.0%，净 delta 敞口 -49k shares
Top ΔOI: C 237 -5,708 ｜ C 225 +1,255
仓位参考: Max Pain 218 ｜ Call Wall 230（+6.0%，弱）（OI 5.6k） ｜ Put Wall 200（-7.8%）（OI 8.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 30.0%｜历史 Rank 40%（近端代理）｜IV/RV 1.24×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 48,559 股

📆 10-28 Forward Structure
存量OI: C 18.9k / P 17.1k，今日变化ΔOI: C +5.4k / P +4.7k，平值价格ATM: C $3.60 / P $4.02 ｜ ATM IV 33.5%，净 delta 敞口 -87k shares
Top ΔOI: P 215 +1,576 ｜ C 232 +985 ｜ C 235 +881
仓位参考: Max Pain 218 ｜ Call Wall 230（+6.0%）（OI 5.5k） ｜ Put Wall 215（-0.9%）（OI 3.4k）
量化解读： 存量两侧均衡｜ATM IV 33.5%｜历史 Rank 40%（近端代理）｜IV/RV 1.38×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 86,861 股

📆 10-30 Forward Structure
存量OI: C 209.3k / P 193.5k，今日变化ΔOI: C +14.5k / P +24.1k，平值价格ATM: C $4.45 / P $4.70 ｜ ATM IV 35.5%，净 delta 敞口 -354k shares
Top ΔOI: P 210 +5,680 ｜ P 197 +5,342
仓位参考: Max Pain 222 ｜ Call Wall 230（+6.0%，弱）（OI 18.7k） ｜ Put Wall 210（-3.2%，弱）（OI 16.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 35.5%｜历史 Rank 40%（近端代理）｜IV/RV 1.47×（近似）｜净 delta 敞口 负 353,522 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/NVDA_morning.json