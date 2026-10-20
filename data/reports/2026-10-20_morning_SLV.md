# 期权晨报 2026-10-20（快照 10:20 ET）

📊 市场环境

SPY $769.53 ｜ QQQ $717.63
VIX 18.12 ↓1.7%（5D +18.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-21 52C ΔOI +1,802（距现价 +0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 51.54 → 今开 51.70（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 52.28 ｜ 低 51.55

Options: P/C成交量 0.22 | OI比 0.54 | ATM IV 33.7% | Skew 3.0pp | Term 1.00 | ExpMove ±1.6%（近端） | Rank 52%
量化视角： IV 中性（Rank 52%）｜期限结构正常（Term 1.00）｜保护溢价中性（Skew 3.0pp）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.22×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-21（1D）±1.6% ｜ 10-23（3D）±2.5% ｜ 10-26（6D）±3.1% ｜ 10-28（8D）±3.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 45,619,902 | GEX Change vs 上次快照 22,322,161 | Flip: Primary Flip: 50.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 759 / LOW 120 / INVALID 377
结构观察区: Primary Flip 50.77（全链重定价，覆盖 98%）
Put Wall 50（弱结构｜现价高于该位 3.9%）
最近结构参考: Flip 51（现价高于该位 2.3%）
量化视角： 正 Gamma（4562万，无历史分位）｜正 Gamma 增强（+2232万）｜现价位于 Flip 上方 2.32%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构） / 51（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 51（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 55.0C — Vol 9,932 | 最新价 $0.88 | OI 17721→20565 (ΔOI +2844张) | ΔOI/Volume 28.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2844张（+16.1% vs前日OI），连续性待观察（方向未知）
10-21 52.0C — Vol 3,812 | 最新价 $0.29 | OI 629→2431 (ΔOI +1802张) | ΔOI/Volume 47.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1802张（+286.5% vs前日OI），连续性待观察（方向未知）
10-30 64.0C — Vol 1,566 | 最新价 $0.02 | OI 665→2288 (ΔOI +1623张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1623张（+244.1% vs前日OI），连续性待观察（方向未知）
11-20 110.0C — Vol 1,717 | 最新价 $0.01 | OI 15270→16653 (ΔOI +1383张) | ΔOI/Volume 80.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1383张（+9.1% vs前日OI），连续性待观察（方向未知）
11-20 50.0P — Vol 1,430 | 最新价 $1.29 | OI 16632→17510 (ΔOI +878张) | ΔOI/Volume 61.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增878张（+5.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,530 张（Put 878 / Call 7,652），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-21  C +5.4k / P +2.1k ｜ Activity HIGH ｜ 1D
10-23  C +3.0k / P -3.8k ｜ Activity MEDIUM △ ｜ 3D
10-26  C +0.9k / P +0.3k ｜ Activity HIGH ｜ 6D
10-28  C +0.4k / P +0.5k ｜ Activity MEDIUM △ ｜ 8D

📆 10-21 Forward Structure
存量OI: C 29.7k / P 16.0k，今日变化ΔOI: C +5.4k / P +2.1k，平值价格ATM: C $0.34 / P $0.51 ｜ ATM IV 33.7%，净 delta 敞口 214k shares
Top ΔOI: C 52 +1,802 ｜ P 51 +758 ｜ C 52 +716
仓位参考: Max Pain 51 ｜ Call Wall 54（+4.0%）（OI 5.3k） ｜ Put Wall 48（-7.6%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 33.7%｜历史 Rank 52%（近端代理）｜IV/RV 0.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 213,578 股

10-23（MEDIUM △）Top ΔOI: 58P -2,186 ｜ 57P -1,650
10-23（MEDIUM △）仓位参考: Max Pain 53 ｜ Call Wall 57（+9.7%，弱）（OI 7.0k） ｜ Put Wall 50（-3.7%，弱）（OI 4.5k）

📆 10-26 Forward Structure
存量OI: C 4.2k / P 3.4k，今日变化ΔOI: C +0.9k / P +0.3k，平值价格ATM: C $0.73 / P $0.88 ｜ ATM IV 28.2%，净 delta 敞口 11k shares
Top ΔOI: C 53 +339 ｜ C 52 +128 ｜ C 54 +79
仓位参考: Max Pain 50 ｜ Call Wall 50.5（-2.8%）（OI 1.5k） ｜ Put Wall 48（-7.6%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 28.2%｜历史 Rank 52%（近端代理）｜IV/RV 0.77×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 10,693 股

10-28（MEDIUM △）Top ΔOI: 51P +135 ｜ 52C +77
10-28（MEDIUM △）仓位参考: Max Pain 52 ｜ Call Wall 55（+5.9%，弱）（OI 0.3k） ｜ Put Wall 48（-7.6%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/SLV_morning.json