# 期权晨报 2026-10-05（快照 10:20 ET）

📊 市场环境

SPY $774.78 ｜ QQQ $756.20
VIX 15.75 ↑2.9%（5D -2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 43.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 10-05 10:00　【高】ISM 非制造业 PMI　预测 55 ｜ 实际 54.9 ｜ 前值 55.4　✅ 今日已公布
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 570P ΔOI +501（距现价 -2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 588.90 → 今开 586.76（-0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 588.00 ｜ 低 582.08

Options: P/C成交量 2.20 | OI比 1.23 | ATM IV 32.7% | Skew -0.3pp | Term 1.18 | ExpMove ±3.0%（近端） | Rank 47%
量化视角： IV 中性（Rank 47%）｜期限结构正常偏陡（Term 1.18）｜Put 保护异常便宜（Skew -0.3pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 2.20）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.20×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.23×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-09（4D）±3.0% ｜ 10-16（11D）±9.1% ｜ 10-23（18D）±4.8% ｜ 10-30（25D）±8.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,770,395 | GEX Change vs 上次快照 -1,943,487 | Flip: Primary Flip: 570.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 512 / LOW 231 / INVALID 757
结构观察区: Primary Flip 570.02（全链重定价，覆盖 95%）
Call Wall 600（现价低于该位 2.8%）
最近结构参考: Flip 570（现价高于该位 2.3%）
量化视角： 正 Gamma（577万，无历史分位）｜正 Gamma 减弱（194万）｜现价位于 Flip 上方 2.31%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 550（MaxPain，仅结算参考）；上方 600（Call Wall）。
• Gamma 区域：切换参考 570（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 425.0P — Vol 10,004 | 最新价 $0.12 | OI 1678→11678 (ΔOI +10000张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10000张（+596.0% vs前日OI），连续性待观察（方向未知）
10-16 505.0P — Vol 2,134 | 最新价 $0.62 | OI 886→2653 (ΔOI +1767张) | ΔOI/Volume 82.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1767张（+199.4% vs前日OI），连续性待观察（方向未知）
10-16 460.0P — Vol 1,023 | 最新价 $0.30 | OI 1513→2249 (ΔOI +736张) | ΔOI/Volume 72.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增736张（+48.6% vs前日OI），连续性待观察（方向未知）
10-09 570.0P — Vol 544 | 最新价 $2.55 | OI 12→513 (ΔOI +501张) | ΔOI/Volume 92.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增501张（+4175.0% vs前日OI），连续性待观察（方向未知）
10-09 550.0P — Vol 642 | 最新价 $0.78 | OI 565→946 (ΔOI +381张) | ΔOI/Volume 59.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增381张（+67.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 13,385 张（Put 13,385 / Call 0），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +0.6k / P +1.8k ｜ Activity HIGH ｜ 4D
10-16  C -0.5k / P +12.7k ｜ Activity MEDIUM △ ｜ 11D
10-23  C +91 / P +0.5k ｜ Activity MEDIUM △ ｜ 18D
10-30  C +0.5k / P +0.3k ｜ Activity MEDIUM △ ｜ 25D

📆 10-09 Forward Structure
存量OI: C 5.3k / P 6.6k，今日变化ΔOI: C +0.6k / P +1.8k，平值价格ATM: C $10.00 / P $7.25 ｜ ATM IV 32.7%，净 delta 敞口 -35k shares
Top ΔOI: P 570 +501 ｜ P 550 +381 ｜ C 610 +173
仓位参考: Max Pain 550 ｜ Put Wall 550（-5.7%）（OI 0.9k）
量化解读： 存量 Put 重｜ATM IV 32.7%｜历史 Rank 47%（近端代理）｜IV/RV 0.93×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 34,723 股

10-16（MEDIUM △）Top ΔOI: 425P +10,000 ｜ 505P +1,767
10-16（MEDIUM △）仓位参考: Max Pain 530 ｜ Call Wall 600（+2.9%）（OI 9.1k）

10-23（MEDIUM △）Top ΔOI: 570P +53
10-23（MEDIUM △）仓位参考: Max Pain 540 ｜ Call Wall 570（-2.3%，弱）（OI 89）

10-30（MEDIUM △）Top ΔOI: 550P +143 ｜ 650C +119
10-30（MEDIUM △）仓位参考: Max Pain 555 ｜ Put Wall 550（-5.7%，弱）（OI 3.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/SOXX_morning.json