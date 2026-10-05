# 期权晨报 2026-10-05（快照 10:20 ET）

📊 市场环境

SPY $771.25 ｜ QQQ $753.41
VIX 15.75 ↑2.9%（5D -2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 43.0（fear）
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
🟡 **近现价集中开仓**: 10-16 154P ΔOI -942（距现价 -0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 154.43 → 今开 155.56（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 155.90 ｜ 低 153.81

Options: P/C成交量 0.07 | OI比 3.34 | ATM IV 34.8% | Skew 2.3pp | Term 0.91 | ExpMove ±3.4%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构正常（Term 0.91）｜保护溢价中性（Skew 2.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.07×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 3.34×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-09（4D）±3.4% ｜ 10-16（11D）±4.4% ｜ 10-23（18D）±5.2% ｜ 10-30（25D）±6.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -38,491,476 | GEX Change vs 上次快照 3,001,112 | Flip: Primary Flip: 166.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 334 / LOW 60 / INVALID 340
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 166.52（全链重定价，覆盖 97%）
Put Wall 150（现价高于该位 3.5%）
最近结构参考: Put Wall 150（现价高于该位 3.5%）
量化视角： 负 Gamma（3849万，无历史分位）｜负 Gamma 缓解（+300万）｜现价位于 Flip 下方 6.78%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall） / 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 167（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 140.0P — Vol 1,890 | 最新价 $0.95 | OI 6382→7996 (ΔOI +1614张) | ΔOI/Volume 85.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1614张（+25.3% vs前日OI），连续性待观察（方向未知）
10-30 150.0P — Vol 1,505 | 最新价 $3.27 | OI 5514→7015 (ΔOI +1501张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1501张（+27.2% vs前日OI），连续性待观察（方向未知）
10-09 145.0C — Vol 1,000 | 最新价 $9.72 | OI 16→1016 (ΔOI +1000张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1000张（+6250.0% vs前日OI），连续性待观察（方向未知）
10-16 155.0C — Vol 283 | 最新价 $3.30 | OI 988→1243 (ΔOI +255张) | ΔOI/Volume 90.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增255张（+25.8% vs前日OI），连续性待观察（方向未知）
10-16 140.0P — Vol 139 | 最新价 $0.26 | OI 5926→6051 (ΔOI +125张) | ΔOI/Volume 89.9% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增125张（+2.1% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,495 张（Put 3,240 / Call 1,255），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +1.4k / P +66 ｜ Activity HIGH ｜ 4D
10-16  C +0.3k / P -1.0k ｜ Activity HIGH ｜ 11D
10-23  C +51 / P +0.1k ｜ Activity MEDIUM △ ｜ 18D
10-30  C +0.1k / P +3.2k ｜ Activity HIGH ｜ 25D

📆 10-09 Forward Structure
存量OI: C 3.1k / P 10.5k，今日变化ΔOI: C +1.4k / P +66，平值价格ATM: C $2.39 / P $2.81 ｜ ATM IV 34.8%，净 delta 敞口 112k shares
Top ΔOI: C 145 +1,000 ｜ P 155 -274 ｜ P 160 +82
仓位参考: Max Pain 155 ｜ Call Wall 162（+4.4%，弱）（OI 0.3k） ｜ Put Wall 148（-4.7%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 34.8%｜历史 Rank 60%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 112,061 股

📆 10-16 Forward Structure
存量OI: C 39.1k / P 79.4k，今日变化ΔOI: C +0.3k / P -1.0k，平值价格ATM: C $3.27 / P $3.50 ｜ ATM IV 32.5%，净 delta 敞口 71k shares
Top ΔOI: P 154 -942 ｜ C 155 +255 ｜ P 144 -216
仓位参考: Max Pain 161 ｜ Call Wall 165（+6.3%，弱）（OI 3.0k） ｜ Put Wall 150（-3.4%）（OI 22.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 32.5%｜历史 Rank 60%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 70,836 股

10-23（MEDIUM △）Top ΔOI: 144P +75 ｜ 148P +33
10-23（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 154（-0.8%，弱）（OI 81） ｜ Put Wall 153（-1.4%，弱）（OI 0.4k）

📆 10-30 Forward Structure
存量OI: C 1.9k / P 17.2k，今日变化ΔOI: C +0.1k / P +3.2k，平值价格ATM: C $5.20 / P $4.57 ｜ ATM IV 31.4%，净 delta 敞口 -62k shares
Top ΔOI: P 140 +1,614 ｜ P 150 +1,501 ｜ C 159 +72
仓位参考: Max Pain 159 ｜ Call Wall 159（+2.4%，弱）（OI 0.4k） ｜ Put Wall 150（-3.4%，弱）（OI 7.0k）
量化解读： 存量 Put 重｜ATM IV 31.4%｜历史 Rank 60%（近端代理）｜IV/RV 1.29×（近似）｜净 delta 敞口 负 61,757 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/XBI_morning.json