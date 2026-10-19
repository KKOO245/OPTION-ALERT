# 期权晨报 2026-10-19（快照 10:20 ET）

📊 市场环境

SPY $766.80 ｜ QQQ $718.36
VIX 18.46 ↓7.7%（5D +21.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 23.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🟡 **近现价集中开仓**: 10-21 54C ΔOI +4,231（距现价 +4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-21 54C ΔOI +4,231 占该期限总 OI 11.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 51.51 → 今开 51.91（+0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 51.94 ｜ 低 51.53

Options: P/C成交量 0.59 | OI比 0.78 | ATM IV 32.7% | Skew 5.4pp | Term 1.05 | ExpMove ±2.1%（近端） | Rank 49%
量化视角： IV 中性（Rank 49%）｜期限结构正常（Term 1.05）｜保护溢价中性（Skew 5.4pp）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.59×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-21（2D）±2.1% ｜ 10-23（4D）±3.1% ｜ 10-26（7D）±3.3% ｜ 10-28（9D）±4.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 36,528,302 | GEX Change vs 上次快照 7,826,500 | Flip: Primary Flip: 50.71（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 678 / LOW 152 / INVALID 418
结构观察区: Primary Flip 50.71（全链重定价，覆盖 98%）
Put Wall 50（弱结构｜现价高于该位 3.2%）
最近结构参考: Flip 51（现价高于该位 1.8%）
量化视角： 正 Gamma（3653万，无历史分位）｜正 Gamma 增强（+783万）｜现价位于 Flip 上方 1.78%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构） / 52（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 51（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 56.0C — Vol 7,526 | 最新价 $0.80 | OI 3214→9200 (ΔOI +5986张) | ΔOI/Volume 79.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5986张（+186.2% vs前日OI），连续性待观察（方向未知）
10-21 54.0C — Vol 4,548 | 最新价 $0.07 | OI 718→4949 (ΔOI +4231张) | ΔOI/Volume 93.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4231张（+589.3% vs前日OI），连续性待观察（方向未知）
10-21 54.5C — Vol 3,051 | 最新价 $0.06 | OI 401→3118 (ΔOI +2717张) | ΔOI/Volume 89.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2717张（+677.6% vs前日OI），连续性待观察（方向未知）
11-06 40.0P — Vol 2,525 | 最新价 $0.04 | OI 2507→4746 (ΔOI +2239张) | ΔOI/Volume 88.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2239张（+89.3% vs前日OI），连续性待观察（方向未知）
10-21 49.5P — Vol 2,846 | 最新价 $0.18 | OI 324→2428 (ΔOI +2104张) | ΔOI/Volume 73.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2104张（+649.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 17,277 张（Put 4,343 / Call 12,934），跨 3 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 17.7k / P 13.7k，今日成交量: C 6.1k / P 3.6k，平值价格ATM: C $0.26 / P $0.12 ｜ ATM IV 32.7%，预期波动 ±0.7%，Max Pain 52
Top ΔOI: C 53 +1,529 ｜ P 50 +1,348 ｜ C 52 +1,223

📆 Forward Expiration Structure

10-21  C +12.7k / P +5.3k ｜ Activity HIGH ｜ 2D
10-23  C +2.8k / P +2.1k ｜ Activity HIGH ｜ 4D
10-26  C +0.1k / P +0.6k ｜ Activity HIGH ｜ 7D
10-28  C +0.3k / P +0.1k ｜ Activity MEDIUM △ ｜ 9D

📆 10-21 Forward Structure
存量OI: C 24.2k / P 13.8k，今日变化ΔOI: C +12.7k / P +5.3k，平值价格ATM: C $0.60 / P $0.47 ｜ ATM IV 32.6%，净 delta 敞口 59k shares
Top ΔOI: C 54 +4,231 ｜ C 54 +2,717 ｜ P 49 +2,104
仓位参考: Max Pain 52 ｜ Call Wall 54（+4.6%）（OI 4.9k） ｜ Put Wall 48（-7.0%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 32.6%｜历史 Rank 49%（近端代理）｜IV/RV 0.88×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 59,416 股

📆 10-23 Forward Structure
存量OI: C 64.7k / P 50.3k，今日变化ΔOI: C +2.8k / P +2.1k，平值价格ATM: C $0.91 / P $0.67 ｜ ATM IV 33.2%，净 delta 敞口 27k shares
Top ΔOI: C 53 +1,016 ｜ P 48 +431 ｜ P 48 +426
仓位参考: Max Pain 54 ｜ Call Wall 55（+6.6%，弱）（OI 5.3k） ｜ Put Wall 50（-3.1%，弱）（OI 4.6k）
量化解读： 存量 Call 重｜ATM IV 33.2%｜历史 Rank 49%（近端代理）｜IV/RV 0.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 27,278 股

📆 10-26 Forward Structure
存量OI: C 3.3k / P 3.1k，今日变化ΔOI: C +0.1k / P +0.6k，平值价格ATM: C $0.96 / P $0.76 ｜ ATM IV 29.2%，净 delta 敞口 -6k shares
Top ΔOI: P 50 +295 ｜ P 48 +151
仓位参考: Max Pain 50 ｜ Call Wall 50.5（-2.2%）（OI 1.4k） ｜ Put Wall 50（-3.1%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 29.2%｜历史 Rank 49%（近端代理）｜IV/RV 0.78×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 5,836 股

10-28（MEDIUM △）Top ΔOI: 51P +94 ｜ 53C +90
10-28（MEDIUM △）仓位参考: Max Pain 52 ｜ Call Wall 55（+6.6%，弱）（OI 0.3k） ｜ Put Wall 48（-7.0%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/SLV_morning.json