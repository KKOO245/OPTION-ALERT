# 期权晨报 2026-09-15（快照 10:20 ET）

📊 市场环境

SPY $759.03 ｜ QQQ $706.15
VIX 17.08 ↓0.1%（5D +8.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.6（fear）
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
🟡 **近现价集中开仓**: 09-25 52C ΔOI +101（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 50.68 → 今开 50.47（-0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 51.18 ｜ 低 49.74

Options: P/C成交量 1.12 | OI比 0.79 | ATM IV 70.2% | Skew -5.9pp | Term 0.89 | ExpMove ±6.0%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.12×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（3D）±6.0% ｜ 09-25（10D）±9.1% ｜ 10-02（17D）±12.3% ｜ 10-09（24D）±12.9%
   ⇒ IV–VIX Spread: +53.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,494,033 | GEX Change vs 上次快照 -1,098,108 | Flip: Primary Flip: 54.10（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 277 / LOW 41 / INVALID 100
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 54.10（全链重定价，覆盖 100%）
Put Wall 55（弱结构｜现价低于该位 8.9%）
最近结构参考: Flip 54（现价低于该位 7.4%）
量化视角： 负 Gamma（549万，无历史分位）｜负 Gamma 加深（110万）｜现价位于 Flip 下方 7.39%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 55（Put Wall，弱结构） / 55（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 54（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 55.0P — Vol 3,715 | 最新价 $6.20 | OI 789→4060 (ΔOI +3271张) | ΔOI/Volume 88.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3271张（+414.6% vs前日OI），连续性待观察（方向未知）
10-16 60.0C — Vol 606 | 最新价 $1.23 | OI 1865→2300 (ΔOI +435张) | ΔOI/Volume 71.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增435张（+23.3% vs前日OI），连续性待观察（方向未知）
09-18 53.0C — Vol 568 | 最新价 $0.73 | OI 363→744 (ΔOI +381张) | ΔOI/Volume 67.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增381张（+105.0% vs前日OI），连续性待观察（方向未知）
09-18 55.0C — Vol 976 | 最新价 $0.31 | OI 4803→5173 (ΔOI +370张) | ΔOI/Volume 37.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增370张（+7.7% vs前日OI），连续性待观察（方向未知）
09-18 54.0C — Vol 593 | 最新价 $0.49 | OI 1417→1761 (ΔOI +344张) | ΔOI/Volume 58.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增344张（+24.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,801 张（Put 3,271 / Call 1,530），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +1.4k / P -1.0k ｜ Activity HIGH ｜ 3D
09-25  C +0.6k / P +0.4k ｜ Activity HIGH ｜ 10D
10-02  C +0.2k / P +53 ｜ Activity HIGH ｜ 17D
10-09  C +17 / P +67 ｜ Activity MEDIUM △ ｜ 24D

📆 09-18 Forward Structure
存量OI: C 54.0k / P 42.9k，今日变化ΔOI: C +1.4k / P -1.0k，平值价格ATM: C $1.95 / P $1.07 ｜ ATM IV 70.2%，净 delta 敞口 160k shares
Top ΔOI: P 55 -1,133 ｜ C 53 +381 ｜ C 55 +370
仓位参考: Max Pain 55 ｜ Call Wall 55（+9.8%，弱）（OI 5.2k） ｜ Put Wall 55（+9.8%，弱）（OI 7.7k）
量化解读： 存量 Call 重｜ATM IV 70.2%｜历史 Rank 54%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 159,897 股

📆 09-25 Forward Structure
存量OI: C 5.5k / P 5.5k，今日变化ΔOI: C +0.6k / P +0.4k，平值价格ATM: C $2.75 / P $1.80 ｜ ATM IV 61.5%，净 delta 敞口 -7k shares
Top ΔOI: P 54 +205 ｜ C 52 +101
仓位参考: Max Pain 54 ｜ Call Wall 55（+9.8%，弱）（OI 0.4k） ｜ Put Wall 55（+9.8%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜ATM IV 61.5%｜历史 Rank 54%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 7,320 股

📆 10-02 Forward Structure
存量OI: C 2.9k / P 3.2k，今日变化ΔOI: C +0.2k / P +53，平值价格ATM: C $3.73 / P $2.45 ｜ ATM IV 58.9%，净 delta 敞口 3k shares
仓位参考: Max Pain 58 ｜ Call Wall 55（+9.8%，弱）（OI 0.2k） ｜ Put Wall 50（-0.2%）（OI 1.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 58.9%｜历史 Rank 54%（近端代理）｜净 delta 敞口 正 3,117 股

10-09（MEDIUM △）Top ΔOI: 48P +22 ｜ 55P +10
10-09（MEDIUM △）仓位参考: Max Pain 52 ｜ Call Wall 55（+9.8%）（OI 1.0k） ｜ Put Wall 47（-6.2%）（OI 1.0k）

📅 事件差分（观察，非因果）: 09-18（3D）ATM IV 70.2% vs 09-25 61.5%（差 +8.6pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=22 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=22）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/MP_morning.json