# 期权晨报 2026-09-15（快照 11:20 ET）

📊 市场环境

SPY $756.82 ｜ QQQ $705.54
VIX 17.68 ↑3.4%（5D +12.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **近现价集中开仓**: 09-18 385C ΔOI +90（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 377.94 → 今开 374.16（-1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 375.38 ｜ 低 368.85

Options: P/C成交量 1.60 | OI比 0.92 | ATM IV 44.8% | Skew 10.3pp | Term 0.78 | ExpMove ±3.8%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价显著（Skew 10.3pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.60×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（3D）±3.8% ｜ 09-25（10D）±5.2% ｜ 10-02（17D）±5.6% ｜ 10-09（24D）±9.9%
   ⇒ IV–VIX Spread: +27.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,504,450 | GEX Change vs 上次快照 -2,081,843 | Flip: Primary Flip: 378.82（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 307 / LOW 196 / INVALID 431
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 378.82（全链重定价，覆盖 91%）
Put Wall 350（弱结构｜现价高于该位 6.0%） | Call Wall 400（弱结构｜现价低于该位 7.3%）
最近结构参考: Flip 379（现价低于该位 2.1%）
量化视角： 负 Gamma（250万，无历史分位）｜负 Gamma 加深（208万）｜现价位于 Flip 下方 2.10%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 350（Put Wall，弱结构）；上方 372（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 379（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 355.0P — Vol 343 | 最新价 $6.05 | OI 215→554 (ΔOI +339张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增339张（+157.7% vs前日OI），连续性待观察（方向未知）
09-18 385.0C — Vol 158 | 最新价 $3.30 | OI 207→297 (ΔOI +90张) | ΔOI/Volume 57.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增90张（+43.5% vs前日OI），连续性待观察（方向未知）
09-18 392.5C — Vol 82 | 最新价 $1.50 | OI 20→101 (ΔOI +81张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增81张（+405.0% vs前日OI），连续性待观察（方向未知）
09-18 585.0C — Vol 60 | 最新价 $0.06 | OI 0→60 (ΔOI +60张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增60张（前日OI缺失），值得跟踪（方向未知）
09-18 570.0C — Vol 60 | 最新价 $0.07 | OI 62→122 (ΔOI +60张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增60张（+96.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 630 张（Put 339 / Call 291），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0.4k / P -1.3k ｜ Activity HIGH ｜ 3D
09-25  C +84 / P +27 ｜ Activity HIGH ｜ 10D
10-02  C +24 / P -7 ｜ Activity MEDIUM △ ｜ 17D
10-09  C +20 / P +1 ｜ Activity MEDIUM △ ｜ 24D

📆 09-18 Forward Structure
存量OI: C 16.4k / P 15.0k，今日变化ΔOI: C +0.4k / P -1.3k，平值价格ATM: C $11.20 / P $2.86 ｜ ATM IV 44.8%，净 delta 敞口 -4k shares
Top ΔOI: C 385 +90 ｜ C 392 +81
仓位参考: Max Pain 372 ｜ Call Wall 400（+7.9%，弱）（OI 1.1k） ｜ Put Wall 350（-5.6%，弱）（OI 2.4k）
量化解读： 存量两侧均衡｜ATM IV 44.8%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,842 股

📆 09-25 Forward Structure
存量OI: C 1.5k / P 0.8k，今日变化ΔOI: C +84 / P +27，平值价格ATM: C $12.12 / P $7.00 ｜ ATM IV 35.6%，净 delta 敞口 788 shares
Top ΔOI: C 400 +30 ｜ C 380 +13 ｜ P 355 -11
仓位参考: Max Pain 370 ｜ Call Wall 405（+9.2%，弱）（OI 0.2k） ｜ Put Wall 360（-2.9%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 35.6%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 788 股

10-02（MEDIUM △）Top ΔOI: 377C +5 ｜ 350P +4
10-02（MEDIUM △）仓位参考: Max Pain 365 ｜ Call Wall 405（+9.2%，弱）（OI 53） ｜ Put Wall 335（-9.7%）（OI 2.4k）

10-09（MEDIUM △）Top ΔOI: 370C +8 ｜ 375C +3
10-09（MEDIUM △）仓位参考: Max Pain 350 ｜ Call Wall 380（+2.5%）（OI 0.1k） ｜ Put Wall 345（-7.0%，弱）（OI 16）

📅 事件差分（观察，非因果）: 09-18（3D）ATM IV 44.8% vs 09-25 35.6%（差 +9.2pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=22 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=22）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/ISRG_morning.json