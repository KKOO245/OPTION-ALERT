# 期权晨报 2026-11-11（快照 10:20 ET）

📊 市场环境

SPY $755.79 ｜ QQQ $687.28
VIX 18.31 ↓5.9%（5D +10.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 36.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 172C ΔOI +3,317（距现价 +0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 168.82 → 今开 173.31（+2.7%） | 较昨收变动（含盘初走势） ｜ 今日高 175.41 ｜ 低 170.80

Options: P/C成交量 0.70 | OI比 0.62 | ATM IV 59.6% | Skew 5.1pp | Term 0.84 | ExpMove ±3.8%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价中性（Skew 5.1pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.70×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±3.8% ｜ 11-20（9D）±6.8% ｜ 11-27（16D）±8.4% ｜ 12-04（23D）±9.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 52,434,181 | GEX Change vs 上次快照 13,631,506 | Flip: Primary Flip: 159.78（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 547 / LOW 179 / INVALID 208
结构观察区: Primary Flip 159.78（全链重定价，覆盖 100%）
Call Wall 165（弱结构｜现价高于该位 3.8%）
最近结构参考: Call Wall 165（现价高于该位 3.8%）
量化视角： 正 Gamma（5243万，无历史分位）｜正 Gamma 增强（+1363万）｜现价位于 Flip 上方 7.17%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 162（MaxPain，仅结算参考） / 165（Call Wall，弱结构）。
• Gamma 区域：切换参考 160（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 172.5C — Vol 9,127 | 最新价 $2.04 | OI 8680→11997 (ΔOI +3317张) | ΔOI/Volume 36.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3317张（+38.2% vs前日OI），连续性待观察（方向未知）
11-13 180.0C — Vol 5,569 | 最新价 $0.46 | OI 5744→6903 (ΔOI +1159张) | ΔOI/Volume 20.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1159张（+20.2% vs前日OI），连续性待观察（方向未知）
11-20 167.5C — Vol 1,748 | 最新价 $7.01 | OI 486→1559 (ΔOI +1073张) | ΔOI/Volume 61.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1073张（+220.8% vs前日OI），连续性待观察（方向未知）
11-13 177.5C — Vol 2,794 | 最新价 $0.77 | OI 2084→3155 (ΔOI +1071张) | ΔOI/Volume 38.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1071张（+51.4% vs前日OI），连续性待观察（方向未知）
11-13 175.0C — Vol 3,870 | 最新价 $1.30 | OI 5598→6526 (ΔOI +928张) | ΔOI/Volume 24.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增928张（+16.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,548 张（Put 0 / Call 7,548），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +5.1k / P +0.9k ｜ Activity HIGH ｜ 2D
11-20  C +1.7k / P -0.4k ｜ Activity MEDIUM △ ｜ 9D
11-27  C +0.7k / P +1.1k ｜ Activity HIGH ｜ 16D
12-04  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 23D

📆 11-13 Forward Structure
存量OI: C 138.4k / P 85.8k，今日变化ΔOI: C +5.1k / P +0.9k，平值价格ATM: C $3.95 / P $2.63 ｜ ATM IV 59.6%，净 delta 敞口 147k shares
Top ΔOI: C 172 +3,317 ｜ C 180 +1,159 ｜ C 177 +1,071
仓位参考: Max Pain 162 ｜ Call Wall 165（-3.6%，弱）（OI 13.7k） ｜ Put Wall 155（-9.5%，弱）（OI 4.2k）
量化解读： 存量 Call 重｜ATM IV 59.6%｜历史 Rank 78%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 147,179 股

11-20（MEDIUM △）Top ΔOI: 167C +1,073
11-20（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 180（+5.1%，弱）（OI 10.7k） ｜ Put Wall 185（+8.0%，弱）（OI 9.9k）

📆 11-27 Forward Structure
存量OI: C 17.3k / P 22.0k，今日变化ΔOI: C +0.7k / P +1.1k，平值价格ATM: C $8.20 / P $6.25 ｜ ATM IV 49.4%，净 delta 敞口 23k shares
Top ΔOI: C 180 +388
仓位参考: Max Pain 175 ｜ Call Wall 180（+5.1%，弱）（OI 1.3k） ｜ Put Wall 160（-6.6%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 49.4%｜历史 Rank 78%（近端代理）｜IV/RV 0.90×（近似）｜净 delta 敞口 正 22,601 股

12-04（MEDIUM △）Top ΔOI: 150P +395 ｜ 185C +89
12-04（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 185（+8.0%，弱）（OI 1.1k） ｜ Put Wall 155（-9.5%，弱）（OI 0.8k）

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 59.6% vs 11-20 53.1%（差 +6.5pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/PLTR_morning.json