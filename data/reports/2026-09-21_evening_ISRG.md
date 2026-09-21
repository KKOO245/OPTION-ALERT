# 期权晚报 2026-09-21（快照 16:40 ET）

📊 市场环境

SPY $773.50 ｜ QQQ $741.47
VIX 14.87 ↑0.4%（5D -13.0%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 33.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 400C ΔOI +39（距现价 -0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 393.89 → 收盘 401.65（+2.0%） ｜ 今日高 403.48 ｜ 低 391.04 ｜ 昨收 393.33 → 收盘 401.65（+2.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.76 | OI比 0.54 | ATM IV 37.7% | Skew 1.6pp | Term 1.13 | ExpMove ±1.6%（近端） | Rank 33%
量化视角： IV 中性（Rank 33%）｜期限结构正常（Term 1.13）｜保护溢价薄（Skew 1.6pp）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.76×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（4D）±1.6% ｜ 10-02（11D）±4.5% ｜ 10-09（18D）±3.4% ｜ 10-16（25D）±6.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,541,411 | GEX Change vs 上次快照 152,223 | Flip: Primary Flip: 384.48（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 260 / LOW 127 / INVALID 503
结构观察区: Primary Flip 384.48（全链重定价，覆盖 95%）
Call Wall 400（弱结构｜现价高于该位 0.4%）
最近结构参考: Call Wall 400（现价高于该位 0.4%）
量化视角： 正 Gamma（154万，无历史分位）｜正 Gamma 增强（+15万）｜现价位于 Flip 上方 4.47%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 375（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 384（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 410.0C — Vol 46 | 最新价 $6.02 | OI 23→243 (ΔOI +220张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增220张（+956.5% vs前日OI），值得跟踪（方向未知）
10-02 415.0C — Vol 3 | 最新价 $3.25 | OI 48→187 (ΔOI +139张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增139张（+289.6% vs前日OI），值得跟踪（方向未知）
10-16 430.0C — Vol 85 | 最新价 $5.40 | OI 135→243 (ΔOI +108张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增108张（+80.0% vs前日OI），值得跟踪（方向未知）
10-16 420.0C — Vol 51 | 最新价 $7.80 | OI 414→475 (ΔOI +61张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增61张（+14.7% vs前日OI），值得跟踪（方向未知）
09-25 392.5C — Vol 8 | 最新价 $11.60 | OI 8→54 (ΔOI +46张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增46张（+575.0% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 574 张（Put 0 / Call 574），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +0.2k / P +0.1k ｜ Activity HIGH ｜ 4D
10-02  C +0.4k / P +23 ｜ Activity MEDIUM △ ｜ 11D
10-09  C +25 / P +9 ｜ Activity MEDIUM △ ｜ 18D
10-16  C +0.3k / P -9 ｜ Activity MEDIUM △ ｜ 25D

📆 09-25 Forward Structure
存量OI: C 1.9k / P 1.0k，今日变化ΔOI: C +0.2k / P +0.1k，平值价格ATM: C $6.55 / P $0.00 ｜ ATM IV 37.7%，净 delta 敞口 11k shares
Top ΔOI: C 392 +46 ｜ C 395 +42 ｜ C 400 +39
仓位参考: Max Pain 375 ｜ Call Wall 430（+7.1%，弱）（OI 0.3k） ｜ Put Wall 370（-7.9%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 37.7%｜历史 Rank 33%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 10,582 股

10-02（MEDIUM △）Top ΔOI: 410C +220 ｜ 415C +139
10-02（MEDIUM △）仓位参考: Max Pain 365 ｜ Call Wall 410（+2.1%，弱）（OI 0.2k）

10-09（MEDIUM △）Top ΔOI: 390C +18 ｜ 395C +5
10-09（MEDIUM △）仓位参考: Max Pain 380 ｜ Call Wall 380（-5.4%）（OI 0.1k） ｜ Put Wall 385（-4.1%）（OI 0.2k）

10-16（MEDIUM △）Top ΔOI: 430C +108 ｜ 420C +61
10-16（MEDIUM △）仓位参考: Max Pain 385 ｜ Call Wall 400（-0.4%，弱）（OI 0.5k） ｜ Put Wall 380（-5.4%，弱）（OI 0.6k）

📅 事件差分（观察，非因果）: 09-25（4D）ATM IV 37.7% vs 10-02 31.8%（差 +5.9pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/ISRG_evening.json