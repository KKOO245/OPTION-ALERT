# 期权晚报 2026-10-05（快照 16:51 ET）

📊 市场环境

SPY $774.83 ｜ QQQ $756.20
VIX 15.52 ↑1.4%（5D -3.4%） ｜ Vol Regime: NORMAL
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
🔵 **期限 OI 集中**: 10-09 370P ΔOI +358 占该期限总 OI 12.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 389.76 → 收盘 406.48（+4.3%） ｜ 今日高 407.63 ｜ 低 389.56 ｜ 昨收 391.95 → 收盘 406.48（+3.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.28 | OI比 0.80 | ATM IV 36.4% | Skew 1.1pp | Term 1.22 | ExpMove ±3.0%（近端） | Rank 27%
量化视角： IV 中性（Rank 27%）｜期限结构正常偏陡（Term 1.22）｜保护溢价薄（Skew 1.1pp）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.28×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（4D）±3.0% ｜ 10-16（11D）±5.2% ｜ 10-23（18D）±6.6% ｜ 10-30（25D）±9.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,642,527 | GEX Change vs 上次快照 917,732 | Flip: Primary Flip: 393.48（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 271 / LOW 135 / INVALID 430
结构观察区: Primary Flip 393.48（全链重定价，覆盖 94%）
Call Wall 400（弱结构｜现价高于该位 1.6%）
最近结构参考: Call Wall 400（现价高于该位 1.6%）
量化视角： 正 Gamma（164万，无历史分位）｜正 Gamma 增强（+92万）｜现价位于 Flip 上方 3.30%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 390（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 393（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 370.0P — Vol 2 | 最新价 $0.20 | OI 17→375 (ΔOI +358张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增358张（+2105.9% vs前日OI），值得跟踪（方向未知）
10-09 390.0P — Vol 16 | 最新价 $1.46 | OI 24→166 (ΔOI +142张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增142张（+591.7% vs前日OI），值得跟踪（方向未知）
10-09 375.0P — Vol 17 | 最新价 $0.30 | OI 34→111 (ΔOI +77张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增77张（+226.5% vs前日OI），值得跟踪（方向未知）
10-09 380.0P — Vol 13 | 最新价 $0.40 | OI 22→86 (ΔOI +64张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增64张（+290.9% vs前日OI），值得跟踪（方向未知）
11-06 455.0C — Vol 43（Yahoo补） | 最新价 $4.40 | OI 1→44 (ΔOI +43张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增43张（+4300.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 684 张（Put 641 / Call 43），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +0.2k / P +0.7k ｜ Activity HIGH ｜ 4D
10-16  C -53 / P +75 ｜ Activity MEDIUM △ ｜ 11D
10-23  C +29 / P +33 ｜ Activity MEDIUM △ ｜ 18D
10-30  C +0 / P +34 ｜ Activity MEDIUM △ ｜ 25D

📆 10-09 Forward Structure
存量OI: C 1.5k / P 1.2k，今日变化ΔOI: C +0.2k / P +0.7k，平值价格ATM: C $5.90 / P $6.23 ｜ ATM IV 36.4%，净 delta 敞口 4k shares
Top ΔOI: P 370 +358 ｜ P 390 +142 ｜ P 375 +77
仓位参考: Max Pain 390 ｜ Call Wall 420（+3.3%，弱）（OI 0.2k） ｜ Put Wall 370（-9.0%）（OI 0.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 36.4%｜历史 Rank 27%（近端代理）｜IV/RV 1.60×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 4,177 股

10-16（MEDIUM △）Top ΔOI: 370P +35 ｜ 377P +34
10-16（MEDIUM △）仓位参考: Max Pain 390 ｜ Call Wall 400（-1.6%，弱）（OI 0.9k） ｜ Put Wall 380（-6.5%，弱）（OI 0.6k）

10-23（MEDIUM △）Top ΔOI: 385P +16 ｜ 390P +13
10-23（MEDIUM △）仓位参考: Max Pain 415 ｜ Call Wall 425（+4.6%）（OI 0.5k） ｜ Put Wall 415（+2.1%）（OI 0.4k）

10-30（MEDIUM △）Top ΔOI: 400P +7
10-30（MEDIUM △）仓位参考: Max Pain 380 ｜ Call Wall 375（-7.7%，弱）（OI 59） ｜ Put Wall 375（-7.7%，弱）（OI 49）

📅 事件差分（观察，非因果）: 10-09（4D）ATM IV 36.4% vs 10-16 30.3%（差 +6.1pp）——覆盖 ISM 非制造业 PMI、美联储议息会议 Minutes 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/ISRG_evening.json