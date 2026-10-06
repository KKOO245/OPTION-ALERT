# 期权晨报 2026-10-05（快照 10:20 ET）

📊 市场环境

SPY $774.83 ｜ QQQ $nan
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
🟡 **近现价集中开仓**: 10-09 140C ΔOI +687（距现价 +2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NOW  昨收 134.38 → 今开 135.22（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 137.90 ｜ 低 134.15

Options: P/C成交量 0.34 | OI比 0.79 | ATM IV 54.7% | Skew 0.4pp | Term 1.07 | ExpMove ±4.7%（近端） | Rank 27%
量化视角： IV 中性（Rank 27%）｜期限结构正常（Term 1.07）｜保护溢价薄（Skew 0.4pp）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（4D）±4.7% ｜ 10-16（11D）±7.1% ｜ 10-23（18D）±9.7% ｜ 10-30（25D）±12.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,961,006 | GEX Change vs 上次快照 2,368,344 | Flip: Primary Flip: 132.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 519 / LOW 26 / INVALID 145
结构观察区: Primary Flip 132.56（全链重定价，覆盖 100%）
最近结构参考: Flip 133（现价高于该位 2.6%）
量化视角： 正 Gamma（696万，无历史分位）｜正 Gamma 增强（+237万）｜现价位于 Flip 上方 2.63%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 133（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 140.0C — Vol 1,436 | 最新价 $1.38 | OI 1981→2668 (ΔOI +687张) | ΔOI/Volume 47.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增687张（+34.7% vs前日OI），连续性待观察（方向未知）
10-09 129.0P — Vol 881 | 最新价 $1.28 | OI 150→817 (ΔOI +667张) | ΔOI/Volume 75.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增667张（+444.7% vs前日OI），连续性待观察（方向未知）
10-16 155.0C — Vol 2,031 | 最新价 $0.42 | OI 3475→4066 (ΔOI +591张) | ΔOI/Volume 29.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增591张（+17.0% vs前日OI），连续性待观察（方向未知）
10-09 130.0P — Vol 1,278 | 最新价 $1.55 | OI 467→1038 (ΔOI +571张) | ΔOI/Volume 44.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增571张（+122.3% vs前日OI），连续性待观察（方向未知）
10-09 150.0C — Vol 1,833 | 最新价 $0.20 | OI 4283→4776 (ΔOI +493张) | ΔOI/Volume 26.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增493张（+11.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,009 张（Put 1,238 / Call 1,771），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +3.9k / P +3.9k ｜ Activity HIGH ｜ 4D
10-16  C +1.2k / P +1.2k ｜ Activity HIGH ｜ 11D
10-23  C -32 / P +1.0k ｜ Activity MEDIUM △ ｜ 18D
10-30  C +0.4k / P +0.9k ｜ Activity MEDIUM △ ｜ 25D

📆 10-09 Forward Structure
存量OI: C 19.9k / P 15.7k，今日变化ΔOI: C +3.9k / P +3.9k，平值价格ATM: C $3.10 / P $3.25 ｜ ATM IV 54.7%，净 delta 敞口 34k shares
Top ΔOI: C 140 +687 ｜ P 129 +667 ｜ P 130 +571
仓位参考: Max Pain 135 ｜ Call Wall 140（+2.9%，弱）（OI 2.7k） ｜ Put Wall 130（-4.4%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 54.7%｜历史 Rank 27%（近端代理）｜IV/RV 1.42×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 34,037 股

📆 10-16 Forward Structure
存量OI: C 77.8k / P 63.2k，今日变化ΔOI: C +1.2k / P +1.2k，平值价格ATM: C $5.10 / P $4.50 ｜ ATM IV 49.9%，净 delta 敞口 886 shares
仓位参考: Max Pain 130 ｜ Call Wall 140（+2.9%，弱）（OI 5.9k） ｜ Put Wall 125（-8.1%，弱）（OI 5.6k）
量化解读： 存量 Call 重｜ATM IV 49.9%｜历史 Rank 27%（近端代理）｜IV/RV 1.30×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 886 股

10-23（MEDIUM △）Top ΔOI: 134C -306
10-23（MEDIUM △）仓位参考: Max Pain 134 ｜ Call Wall 140（+2.9%，弱）（OI 0.9k） ｜ Put Wall 125（-8.1%，弱）（OI 2.0k）

10-30（MEDIUM △）Top ΔOI: 130P +262 ｜ 140P +107
10-30（MEDIUM △）仓位参考: Max Pain 134 ｜ Call Wall 140（+2.9%，弱）（OI 0.6k） ｜ Put Wall 123（-9.6%，弱）（OI 0.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/NOW_morning.json