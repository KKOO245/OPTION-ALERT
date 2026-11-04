# 期权晨报 2026-11-04（快照 10:20 ET）

📊 市场环境

SPY $767.05 ｜ QQQ $697.27
VIX 17.01 ↓18.3%（5D +0.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-04

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 54.5 ｜ 前值 54.9　✅ 今日已公布
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **事件差分**: 11-06 ATM IV 85.4% vs 11-13 70.8%（差 +14.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 145.45 → 今开 141.98（-2.4%） | 较昨收变动（含盘初走势） ｜ 今日高 152.54 ｜ 低 141.88

Options: P/C成交量 0.44 | OI比 0.75 | ATM IV 85.4% | Skew 1.7pp | Term 0.78 | ExpMove ±5.9%（近端） | Rank 73%
量化视角： IV 中性（Rank 73%）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价薄（Skew 1.7pp）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±5.9% ｜ 11-13（9D）±10.8% ｜ 11-20（16D）±12.1% ｜ 11-27（23D）±14.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 23,883,083 | GEX Change vs 上次快照 3,524,248 | Flip: Primary Flip: 134.58（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 428 / LOW 158 / INVALID 264
结构观察区: Primary Flip 134.58（全链重定价，覆盖 100%）
最近结构参考: Flip 135（现价高于该位 10.6%）
量化视角： 正 Gamma（2388万，无历史分位）｜正 Gamma 增强（+352万）｜现价位于 Flip 上方 10.57%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 141（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 135（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 130.0P — Vol 3,467 | 最新价 $0.80 | OI 2151→4125 (ΔOI +1974张) | ΔOI/Volume 56.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1974张（+91.8% vs前日OI），连续性待观察（方向未知）
11-20 120.0P — Vol 4,028 | 最新价 $1.45 | OI 2778→4614 (ΔOI +1836张) | ΔOI/Volume 45.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1836张（+66.1% vs前日OI），连续性待观察（方向未知）
11-20 90.0P — Vol 2,111 | 最新价 $0.20 | OI 1273→2923 (ΔOI +1650张) | ΔOI/Volume 78.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1650张（+129.6% vs前日OI），连续性待观察（方向未知）
11-06 135.0P — Vol 2,942 | 最新价 $1.50 | OI 1624→2729 (ΔOI +1105张) | ΔOI/Volume 37.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1105张（+68.0% vs前日OI），连续性待观察（方向未知）
11-06 160.0C — Vol 2,669 | 最新价 $0.95 | OI 1595→2414 (ΔOI +819张) | ΔOI/Volume 30.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增819张（+51.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,384 张（Put 6,565 / Call 819），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +4.8k / P +5.5k ｜ Activity HIGH ｜ 2D
11-13  C +1.8k / P +1.1k ｜ Activity MEDIUM △ ｜ 9D
11-20  C +0.5k / P +4.4k ｜ Activity HIGH ｜ 16D
11-27  C +5 / P +0.2k ｜ Activity MEDIUM △ ｜ 23D

📆 11-06 Forward Structure
存量OI: C 72.7k / P 54.2k，今日变化ΔOI: C +4.8k / P +5.5k，平值价格ATM: C $3.98 / P $4.85 ｜ ATM IV 85.4%，净 delta 敞口 24k shares
Top ΔOI: P 135 +1,105 ｜ C 160 +819
仓位参考: Max Pain 141 ｜ Call Wall 148（-0.5%，弱）（OI 8.6k） ｜ Put Wall 135（-9.3%，弱）（OI 2.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 85.4%｜历史 Rank 73%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 24,233 股

11-13（MEDIUM △）Top ΔOI: 170C +448 ｜ 145C +199
11-13（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 150（+0.8%，弱）（OI 0.6k） ｜ Put Wall 155（+4.2%，弱）（OI 2.1k）

📆 11-20 Forward Structure
存量OI: C 73.1k / P 57.3k，今日变化ΔOI: C +0.5k / P +4.4k，平值价格ATM: C $8.35 / P $9.70 ｜ ATM IV 70.0%，净 delta 敞口 20k shares
Top ΔOI: P 120 +1,836
仓位参考: Max Pain 170 ｜ Put Wall 140（-5.9%，弱）（OI 3.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 70.0%｜历史 Rank 73%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 19,645 股

11-27（MEDIUM △）Top ΔOI: 145C -51
11-27（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 155（+4.2%，弱）（OI 0.2k） ｜ Put Wall 140（-5.9%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 85.4% vs 11-13 70.8%（差 +14.6pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/COIN_morning.json