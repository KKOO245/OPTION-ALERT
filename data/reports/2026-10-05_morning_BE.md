# 期权晨报 2026-10-05（快照 10:20 ET）

📊 市场环境

SPY $771.25 ｜ QQQ $753.44
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
🟡 **近现价集中开仓**: 10-09 280P ΔOI +945（距现价 -2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 289.15 → 今开 289.99（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 291.06 ｜ 低 282.34

Options: P/C成交量 1.01 | OI比 1.13 | ATM IV 71.9% | Skew -1.1pp | Term 1.15 | ExpMove ±6.3%（近端） | Rank 29%
量化视角： IV 中性（Rank 29%）｜期限结构正常偏陡（Term 1.15）｜Put 保护异常便宜（Skew -1.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.01×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.13×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（4D）±6.3% ｜ 10-16（11D）±9.6% ｜ 10-23（18D）±12.3% ｜ 10-30（25D）±16.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 7,078,047 | GEX Change vs 上次快照 -1,954,494 | Flip: Primary Flip: 270.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 527 / LOW 70 / INVALID 231
结构观察区: Primary Flip 270.34（全链重定价，覆盖 99%）
Call Wall 280（弱结构｜现价高于该位 2.1%）
最近结构参考: Call Wall 280（现价高于该位 2.1%）
量化视角： 正 Gamma（708万，无历史分位）｜正 Gamma 减弱（195万）｜现价位于 Flip 上方 5.77%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 280（MaxPain，仅结算参考） / 280（Call Wall，弱结构）。
• Gamma 区域：切换参考 270（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 280.0P — Vol 1,716 | 最新价 $6.05 | OI 448→1393 (ΔOI +945张) | ΔOI/Volume 55.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增945张（+210.9% vs前日OI），连续性待观察（方向未知）
10-09 300.0C — Vol 3,370 | 最新价 $5.90 | OI 1567→2352 (ΔOI +785张) | ΔOI/Volume 23.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增785张（+50.1% vs前日OI），连续性待观察（方向未知）
10-09 245.0C — Vol 809 | 最新价 $47.23 | OI 89→846 (ΔOI +757张) | ΔOI/Volume 93.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增757张（+850.6% vs前日OI），连续性待观察（方向未知）
10-09 275.0P — Vol 1,193 | 最新价 $4.20 | OI 548→1220 (ΔOI +672张) | ΔOI/Volume 56.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增672张（+122.6% vs前日OI），连续性待观察（方向未知）
10-09 290.0P — Vol 1,800 | 最新价 $10.45 | OI 642→1190 (ΔOI +548张) | ΔOI/Volume 30.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增548张（+85.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,707 张（Put 2,165 / Call 1,542），跨 1 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +6.3k / P +5.7k ｜ Activity HIGH ｜ 4D
10-16  C -0.5k / P +0.2k ｜ Activity MEDIUM △ ｜ 11D
10-23  C +0.6k / P -0.3k ｜ Activity MEDIUM △ ｜ 18D
10-30  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 25D

📆 10-09 Forward Structure
存量OI: C 24.0k / P 27.1k，今日变化ΔOI: C +6.3k / P +5.7k，平值价格ATM: C $9.42 / P $8.50 ｜ ATM IV 71.9%，净 delta 敞口 -39k shares
Top ΔOI: P 280 +945 ｜ C 300 +785 ｜ C 245 +757
仓位参考: Max Pain 280 ｜ Call Wall 300（+4.9%）（OI 2.4k） ｜ Put Wall 280（-2.1%，弱）（OI 1.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 71.9%｜历史 Rank 29%（近端代理）｜IV/RV 0.91×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 39,062 股

10-16（MEDIUM △）Top ΔOI: 270C -764 ｜ 300C -450
10-16（MEDIUM △）仓位参考: Max Pain 265 ｜ Call Wall 270（-5.6%，弱）（OI 7.6k） ｜ Put Wall 260（-9.1%，弱）（OI 3.9k）

10-23（MEDIUM △）Top ΔOI: 300C -227 ｜ 280C +187
10-23（MEDIUM △）仓位参考: Max Pain 270 ｜ Call Wall 300（+4.9%，弱）（OI 1.1k） ｜ Put Wall 280（-2.1%，弱）（OI 0.7k）

10-30（MEDIUM △）Top ΔOI: 210P +344
10-30（MEDIUM △）仓位参考: Max Pain 285 ｜ Call Wall 300（+4.9%，弱）（OI 1.2k） ｜ Put Wall 285（-0.3%，弱）（OI 1.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/BE_morning.json