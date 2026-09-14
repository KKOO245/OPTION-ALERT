# 期权晨报 2026-09-14（快照 10:20 ET）

📊 市场环境

SPY $760.44 ｜ QQQ $706.06
VIX 17.27 ↑9.0%（5D +12.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.9 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **单日价格波动**: -5.7%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,633.35 → 今开 1,521.53（-6.8%） | 较昨收变动（含盘初走势） ｜ 今日高 1565.92 ｜ 低 1505.00

Options: P/C成交量 0.72 | OI比 1.18 | ATM IV 77.8% | Skew -0.5pp | Term 0.91 | ExpMove ±6.8%（近端） | Rank 31%
量化视角： IV 中性（Rank 31%）｜期限结构正常（Term 0.91）｜Put 保护异常便宜（Skew -0.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.72×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.18×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（4D）±6.8% ｜ 09-25（11D）±10.1% ｜ 10-02（18D）±12.8% ｜ 10-09（25D）±15.0%
   ⇒ IV–VIX Spread: +60.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,911,293 | GEX Change vs 上次快照 -2,859,519 | Flip: Primary Flip: 1630.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1995 / LOW 457 / INVALID 924
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1630.63（全链重定价，覆盖 100%）
Put Wall 1,500（弱结构｜现价高于该位 2.7%）
最近结构参考: Put Wall 1500（现价高于该位 2.7%）
量化视角： 负 Gamma（591万，无历史分位）｜负 Gamma 加深（286万）｜现价位于 Flip 下方 5.56%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,500（Put Wall，弱结构） / 1,500（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1631（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 1800.0C — Vol 4,444 | 最新价 $10.80 | OI 2086→3050 (ΔOI +964张) | ΔOI/Volume 21.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增964张（+46.2% vs前日OI），连续性待观察（方向未知）
09-18 1750.0C — Vol 2,687 | 最新价 $17.70 | OI 905→1729 (ΔOI +824张) | ΔOI/Volume 30.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增824张（+91.0% vs前日OI），连续性待观察（方向未知）
09-18 1450.0P — Vol 1,783 | 最新价 $5.10 | OI 2915→3614 (ΔOI +699张) | ΔOI/Volume 39.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增699张（+24.0% vs前日OI），连续性待观察（方向未知）
09-18 1000.0P — Vol 868 | 最新价 $0.15 | OI 2801→3438 (ΔOI +637张) | ΔOI/Volume 73.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增637张（+22.7% vs前日OI），连续性待观察（方向未知）
09-25 1800.0C — Vol 915 | 最新价 $28.00 | OI 362→953 (ΔOI +591张) | ΔOI/Volume 64.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增591张（+163.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,715 张（Put 1,336 / Call 2,379），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +6.6k / P +6.0k ｜ Activity HIGH ｜ 4D
09-25  C +1.8k / P +1.7k ｜ Activity HIGH ｜ 11D
10-02  C +0.6k / P +1.1k ｜ Activity HIGH ｜ 18D
10-09  C +0.3k / P +0.7k ｜ Activity HIGH ｜ 25D

📆 09-18 Forward Structure
存量OI: C 76.4k / P 90.0k，今日变化ΔOI: C +6.6k / P +6.0k，平值价格ATM: C $56.30 / P $48.00 ｜ ATM IV 77.8%，净 delta 敞口 -120k shares
Top ΔOI: C 1800 +964 ｜ C 1750 +824 ｜ P 1450 +699
仓位参考: Max Pain 1,500 ｜ Put Wall 1450（-5.8%，弱）（OI 3.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 77.8%｜历史 Rank 31%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 120,262 股

📆 09-25 Forward Structure
存量OI: C 10.3k / P 17.6k，今日变化ΔOI: C +1.8k / P +1.7k，平值价格ATM: C $80.85 / P $75.20 ｜ ATM IV 71.3%，净 delta 敞口 -28k shares
Top ΔOI: C 1800 +591 ｜ P 1500 +458 ｜ C 1900 +122
仓位参考: Max Pain 1,605
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 71.3%｜历史 Rank 31%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 28,320 股

📆 10-02 Forward Structure
存量OI: C 7.4k / P 9.2k，今日变化ΔOI: C +0.6k / P +1.1k，平值价格ATM: C $103.97 / P $93.90 ｜ ATM IV 71.8%，净 delta 敞口 -34k shares
Top ΔOI: P 1540 +199 ｜ P 1400 +107 ｜ C 1700 -93
仓位参考: Max Pain 1,600 ｜ Call Wall 1600（+3.9%，弱）（OI 0.3k） ｜ Put Wall 1500（-2.6%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 71.8%｜历史 Rank 31%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 34,376 股

📆 10-09 Forward Structure
存量OI: C 2.5k / P 3.6k，今日变化ΔOI: C +0.3k / P +0.7k，平值价格ATM: C $117.00 / P $113.74 ｜ ATM IV 70.9%，净 delta 敞口 -22k shares
Top ΔOI: P 1540 +188 ｜ P 1640 +96 ｜ P 1440 +88
仓位参考: Max Pain 1,640 ｜ Put Wall 1500（-2.6%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜ATM IV 70.9%｜历史 Rank 31%（近端代理）｜净 delta 敞口 负 21,818 股

📅 事件差分（观察，非因果）: 09-18（4D）ATM IV 77.8% vs 09-25 71.3%（差 +6.5pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=16 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=16）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/SNDK_morning.json