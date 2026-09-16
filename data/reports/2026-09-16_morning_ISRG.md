# 期权晨报 2026-09-16（快照 11:22 ET）

📊 市场环境

SPY $760.53 ｜ QQQ $710.93
VIX 16.68 ↓3.0%（5D +1.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75　⏰ 今日
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　⏰ 今日
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　⏰ 今日
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **近现价集中开仓**: 09-18 367P ΔOI +77（距现价 -4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 377.16 → 今开 378.02（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 387.29 ｜ 低 377.16

Options: P/C成交量 1.42 | OI比 0.91 | ATM IV 40.8% | Skew 3.3pp | Term 0.88 | ExpMove ±3.4%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价中性（Skew 3.3pp）｜当日成交偏 Put（P/C量 1.42）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.42×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.91×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（2D）±3.4% ｜ 09-25（9D）±5.1% ｜ 10-02（16D）±9.8% ｜ 10-09（23D）±8.9%
   ⇒ IV–VIX Spread: +24.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 2,176,409 | GEX Change vs 上次快照 2,898,074 | Flip: Primary Flip: 378.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 287 / LOW 216 / INVALID 431
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 378.89（全链重定价，覆盖 90%）
Put Wall 350（弱结构｜现价高于该位 10.3%） | Call Wall 400（弱结构｜现价低于该位 3.5%）
最近结构参考: Flip 379（现价高于该位 1.9%）
量化视角： 正 Gamma（218万，无历史分位）｜由负转正（+290万）｜现价位于 Flip 上方 1.86%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 350（Put Wall，弱结构） / 372（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 379（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 367.5P — Vol 80 | 最新价 $2.00 | OI 89→166 (ΔOI +77张) | ΔOI/Volume 96.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增77张（+86.5% vs前日OI），连续性待观察（方向未知）
09-18 382.5C — Vol 111 | 最新价 $3.34 | OI 23→92 (ΔOI +69张) | ΔOI/Volume 62.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增69张（+300.0% vs前日OI），连续性待观察（方向未知）
09-18 387.5C — Vol 66 | 最新价 $2.10 | OI 72→138 (ΔOI +66张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增66张（+91.7% vs前日OI），连续性待观察（方向未知）
09-18 362.5P — Vol 51 | 最新价 $1.13 | OI 41→91 (ΔOI +50张) | ΔOI/Volume 98.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增50张（+122.0% vs前日OI），连续性待观察（方向未知）
09-18 365.0P — Vol 102 | 最新价 $1.52 | OI 448→487 (ΔOI +39张) | ΔOI/Volume 38.2% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增39张（+8.7% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 301 张（Put 166 / Call 135），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0.1k / P +6 ｜ Activity MEDIUM △ ｜ 2D
09-25  C +4 / P -7 ｜ Activity LOW ｜ 9D
10-02  C +57 / P +2 ｜ Activity HIGH ｜ 16D
10-09  C +3 / P -1 ｜ Activity MEDIUM △ ｜ 23D

📆 09-18 Forward Structure
存量OI: C 16.5k / P 15.0k，今日变化ΔOI: C +0.1k / P +6，平值价格ATM: C $2.35 / P $10.65 ｜ ATM IV 40.8%，净 delta 敞口 2k shares
Top ΔOI: P 367 +77 ｜ C 382 +69 ｜ C 387 +66
仓位参考: Max Pain 372 ｜ Call Wall 400（+3.6%，弱）（OI 1.1k） ｜ Put Wall 350（-9.3%，弱）（OI 2.4k）
量化解读： 存量两侧均衡｜ATM IV 40.8%｜历史 Rank 48%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,027 股

09-25（Activity LOW）仓位参考: Max Pain 370 ｜ Call Wall 405（+4.9%，弱）（OI 0.2k） ｜ Put Wall 360（-6.7%，弱）（OI 0.2k）

📆 10-02 Forward Structure
存量OI: C 0.5k / P 2.8k，今日变化ΔOI: C +57 / P +2，平值价格ATM: C $8.60 / P $29.06 ｜ ATM IV 33.7%，净 delta 敞口 503 shares
Top ΔOI: C 415 +33 ｜ C 405 +27 ｜ P 357 +5
仓位参考: Max Pain 365 ｜ Call Wall 405（+4.9%）（OI 80）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 33.7%｜历史 Rank 48%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 503 股

10-09（MEDIUM △）Top ΔOI: 350P -1
10-09（MEDIUM △）仓位参考: Max Pain 350 ｜ Call Wall 380（-1.5%）（OI 0.1k） ｜ Put Wall 350（-9.3%，弱）（OI 15）

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 40.8% vs 09-25 32.8%（差 +8.0pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/ISRG_morning.json