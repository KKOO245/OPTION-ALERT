# 期权晨报 2026-09-14（快照 10:20 ET）

📊 市场环境

SPY $761.06 ｜ QQQ $709.18
VIX 17.27 ↑9.0%（5D +12.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.1（fear）
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
🟡 **近现价集中开仓**: 09-25 16C ΔOI +478（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 15.56 → 今开 15.28（-1.8%） | 较昨收变动（含盘初走势） ｜ 今日高 15.79 ｜ 低 15.25

Options: P/C成交量 1.02 | OI比 0.54 | ATM IV 67.5% | Skew -2.9pp | Term 1.11 | ExpMove ±7.4%（近端） | Rank 2%
量化视角： IV 历史低位（Rank 2%，期权偏便宜）｜期限结构正常（Term 1.11）｜Put 保护异常便宜（Skew -2.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.02×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（4D）±7.4% ｜ 09-25（11D）±12.0% ｜ 10-02（18D）±14.3% ｜ 10-09（25D）±18.4%
   ⇒ IV–VIX Spread: +50.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,410,169 | GEX Change vs 上次快照 -2,209,119 | Flip: Primary Flip: 16.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 265 / LOW 68 / INVALID 135
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 16.56（全链重定价，覆盖 100%）
Put Wall 15（弱结构｜现价高于该位 3.2%）
最近结构参考: Put Wall 15（现价高于该位 3.2%）
量化视角： 负 Gamma（641万，无历史分位）｜负 Gamma 加深（221万）｜现价位于 Flip 下方 6.53%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 19（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 17（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 21.0C — Vol 4,102 | 最新价 $0.24 | OI 1538→5011 (ΔOI +3473张) | ΔOI/Volume 84.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3473张（+225.8% vs前日OI），连续性待观察（方向未知）
09-18 16.5P — Vol 1,712 | 最新价 $1.19 | OI 723→2176 (ΔOI +1453张) | ΔOI/Volume 84.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1453张（+201.0% vs前日OI），连续性待观察（方向未知）
09-25 16.5C — Vol 1,127 | 最新价 $0.56 | OI 55→1086 (ΔOI +1031张) | ΔOI/Volume 91.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1031张（+1874.5% vs前日OI），连续性待观察（方向未知）
10-16 15.0P — Vol 2,807 | 最新价 $1.10 | OI 3560→4511 (ΔOI +951张) | ΔOI/Volume 33.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增951张（+26.7% vs前日OI），连续性待观察（方向未知）
09-18 18.0C — Vol 2,053 | 最新价 $0.08 | OI 6340→7106 (ΔOI +766张) | ΔOI/Volume 37.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增766张（+12.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,674 张（Put 2,404 / Call 5,270），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +2.1k / P +2.7k ｜ Activity HIGH ｜ 4D
09-25  C +2.1k / P +0.7k ｜ Activity HIGH ｜ 11D
10-02  C +0.2k / P +0.4k ｜ Activity HIGH ｜ 18D
10-09  C +0.1k / P +0.5k ｜ Activity HIGH ｜ 25D

📆 09-18 Forward Structure
存量OI: C 122.8k / P 66.8k，今日变化ΔOI: C +2.1k / P +2.7k，平值价格ATM: C $0.57 / P $0.58 ｜ ATM IV 67.5%，净 delta 敞口 -67k shares
Top ΔOI: P 16 +1,453 ｜ P 17 +667
仓位参考: Max Pain 19 ｜ Put Wall 15（-3.1%，弱）（OI 9.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 67.5%｜历史 Rank 2%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 67,350 股

📆 09-25 Forward Structure
存量OI: C 11.5k / P 4.5k，今日变化ΔOI: C +2.1k / P +0.7k，平值价格ATM: C $1.00 / P $0.86 ｜ ATM IV 73.5%，净 delta 敞口 47k shares
Top ΔOI: C 16 +1,031 ｜ C 16 +478
仓位参考: Max Pain 16 ｜ Put Wall 15（-3.1%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 73.5%｜历史 Rank 2%（近端代理）｜净 delta 敞口 正 47,495 股

📆 10-02 Forward Structure
存量OI: C 7.8k / P 3.2k，今日变化ΔOI: C +0.2k / P +0.4k，平值价格ATM: C $1.19 / P $1.02 ｜ ATM IV 74.6%，净 delta 敞口 -10k shares
Top ΔOI: P 14 +137 ｜ P 16 +117
仓位参考: Max Pain 18 ｜ Put Wall 16（+3.4%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 74.6%｜历史 Rank 2%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 9,971 股

📆 10-09 Forward Structure
存量OI: C 4.1k / P 2.7k，今日变化ΔOI: C +0.1k / P +0.5k，平值价格ATM: C $1.60 / P $1.25 ｜ ATM IV 74.2%，净 delta 敞口 -23k shares
Top ΔOI: P 17 +274 ｜ P 14 +45 ｜ P 15 +38
仓位参考: Max Pain 18 ｜ Put Wall 16（+3.4%）（OI 1.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 74.2%｜历史 Rank 2%（近端代理）｜净 delta 敞口 负 22,878 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=16 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=16）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/USAR_morning.json