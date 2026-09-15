# 期权晨报 2026-09-15（快照 11:20 ET）

📊 市场环境

SPY $758.10 ｜ QQQ $704.54
VIX 17.68 ↑3.4%（5D +12.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 173.31 → 今开 170.24（-1.8%） | 较昨收变动（含盘初走势） ｜ 今日高 173.17 ｜ 低 169.45

Options: P/C成交量 0.90 | OI比 0.79 | ATM IV 56.6% | Skew 2.1pp | Term 0.85 | ExpMove ±4.3%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价中性（Skew 2.1pp）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.90×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（3D）±4.3% ｜ 09-25（10D）±6.7% ｜ 10-02（17D）±8.3% ｜ 10-09（24D）±9.7%
   ⇒ IV–VIX Spread: +38.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 53,688,347 | GEX Change vs 上次快照 6,819,238 | Flip: Primary Flip: 162.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 611 / LOW 67 / INVALID 142
结构观察区: Primary Flip 162.67（全链重定价，覆盖 100%）
Put Wall 170（弱结构｜现价高于该位 0.5%） | Call Wall 180（弱结构｜现价低于该位 5.1%）
最近结构参考: Put Wall 170（现价高于该位 0.5%）
量化视角： 正 Gamma（5369万，无历史分位）｜正 Gamma 增强（+682万）｜现价位于 Flip 上方 5.03%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Put Wall，弱结构） / 155（MaxPain，仅结算参考）；上方 180（Call Wall，弱结构）。
• Gamma 区域：切换参考 163（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 180.0C — Vol 40,074 | 最新价 $1.64 | OI 20040→30400 (ΔOI +10360张) | ΔOI/Volume 25.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10360张（+51.7% vs前日OI），连续性待观察（方向未知）
09-18 182.5C — Vol 17,973 | 最新价 $1.12 | OI 2583→10891 (ΔOI +8308张) | ΔOI/Volume 46.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8308张（+321.6% vs前日OI），连续性待观察（方向未知）
09-25 100.0P — Vol 3,001 | 最新价 $0.03 | OI 3883→6572 (ΔOI +2689张) | ΔOI/Volume 89.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2689张（+69.2% vs前日OI），连续性待观察（方向未知）
09-18 160.0P — Vol 7,923 | 最新价 $0.51 | OI 11509→14037 (ΔOI +2528张) | ΔOI/Volume 31.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2528张（+22.0% vs前日OI），连续性待观察（方向未知）
09-18 177.5C — Vol 8,505 | 最新价 $2.35 | OI 12530→14651 (ΔOI +2121张) | ΔOI/Volume 24.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2121张（+16.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 26,006 张（Put 5,217 / Call 20,789），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +27.5k / P -1.9k ｜ Activity HIGH ｜ 3D
09-25  C +7.5k / P +7.9k ｜ Activity HIGH ｜ 10D
10-02  C +2.0k / P +0.8k ｜ Activity MEDIUM △ ｜ 17D
10-09  C +1.8k / P +0.9k ｜ Activity HIGH ｜ 24D

📆 09-18 Forward Structure
存量OI: C 351.6k / P 276.5k，今日变化ΔOI: C +27.5k / P -1.9k，平值价格ATM: C $4.44 / P $2.94 ｜ ATM IV 56.6%，净 delta 敞口 352k shares
Top ΔOI: C 180 +10,360 ｜ C 182 +8,308 ｜ P 157 -7,614
仓位参考: Max Pain 155 ｜ Call Wall 180（+5.4%，弱）（OI 30.4k） ｜ Put Wall 160（-6.4%，弱）（OI 14.0k）
量化解读： 存量 Call 重｜ATM IV 56.6%｜历史 Rank 80%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 352,140 股

📆 09-25 Forward Structure
存量OI: C 32.8k / P 40.7k，今日变化ΔOI: C +7.5k / P +7.9k，平值价格ATM: C $6.25 / P $5.15 ｜ ATM IV 49.1%，净 delta 敞口 59k shares
Top ΔOI: C 190 +1,388 ｜ C 180 +1,352
仓位参考: Max Pain 172 ｜ Call Wall 180（+5.4%，弱）（OI 2.9k） ｜ Put Wall 170（-0.5%，弱）（OI 4.1k）
量化解读： 存量 Put 重｜ATM IV 49.1%｜历史 Rank 80%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 59,156 股

10-02（MEDIUM △）Top ΔOI: 190C +498
10-02（MEDIUM △）仓位参考: Max Pain 172 ｜ Call Wall 180（+5.4%，弱）（OI 2.7k） ｜ Put Wall 170（-0.5%）（OI 4.6k）

📆 10-09 Forward Structure
存量OI: C 9.5k / P 11.8k，今日变化ΔOI: C +1.8k / P +0.9k，平值价格ATM: C $9.10 / P $7.50 ｜ ATM IV 47.9%，净 delta 敞口 16k shares
Top ΔOI: C 200 +648
仓位参考: Max Pain 170 ｜ Call Wall 172.5（+1.0%，弱）（OI 0.5k） ｜ Put Wall 170（-0.5%）（OI 2.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 47.9%｜历史 Rank 80%（近端代理）｜净 delta 敞口 正 15,656 股

📅 事件差分（观察，非因果）: 09-18（3D）ATM IV 56.6% vs 09-25 49.1%（差 +7.5pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/PLTR_morning.json