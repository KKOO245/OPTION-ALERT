# 期权晨报 2026-11-17（快照 10:20 ET）

📊 市场环境

SPY $737.42 ｜ QQQ $nan
VIX 22.73 ↓0.8%（5D +16.8%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.8　✅ 今日已公布
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **事件差分**: 11-20（3D）ATM IV 142.7% vs 11-27 107.8%（差 +34.9pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-20 790P ΔOI +613（距现价 -1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 809.11 → 今开 809.83（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 821.46 ｜ 低 781.19

Options: P/C成交量 0.70 | OI比 0.64 | ATM IV 142.7% | Skew 9.6pp | Term 0.69 | ExpMove ±10.8%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价显著（Skew 9.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.70×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（3D）±10.8% ｜ 11-27（10D）±14.3% ｜ 12-04（17D）±17.2% ｜ 12-11（24D）±21.4%
   ⇒ IV–VIX Spread: +120.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,774,869 | GEX Change vs 上次快照 -315,098 | Flip: Primary Flip: 867.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 2031 / LOW 536 / INVALID 929
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 867.02（全链重定价，覆盖 100%）
最近结构参考: Flip 867（现价低于该位 7.5%）
量化视角： 负 Gamma（377万，无历史分位）｜负 Gamma 加深（32万）｜现价位于 Flip 下方 7.47%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 960（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 867（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 600.0P — Vol 4,741 | 最新价 $20.30 | OI 2754→6007 (ΔOI +3253张) | ΔOI/Volume 68.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3253张（+118.1% vs前日OI），连续性待观察（方向未知）
11-20 1060.0C — Vol 1,637 | 最新价 $1.45 | OI 1017→2368 (ΔOI +1351张) | ΔOI/Volume 82.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1351张（+132.8% vs前日OI），连续性待观察（方向未知）
11-27 800.0P — Vol 1,134 | 最新价 $55.28 | OI 291→1090 (ΔOI +799张) | ΔOI/Volume 70.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增799张（+274.6% vs前日OI），连续性待观察（方向未知）
12-18 500.0P — Vol 1,233 | 最新价 $7.50 | OI 1926→2685 (ΔOI +759张) | ΔOI/Volume 61.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增759张（+39.4% vs前日OI），连续性待观察（方向未知）
11-20 790.0P — Vol 966 | 最新价 $38.00 | OI 439→1052 (ΔOI +613张) | ΔOI/Volume 63.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增613张（+139.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,775 张（Put 5,424 / Call 1,351），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $14M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +7.0k / P -0.4k ｜ Activity HIGH ｜ 3D
11-27  C +2.5k / P +2.3k ｜ Activity HIGH ｜ 10D
12-04  C +0.6k / P +0.3k ｜ Activity MEDIUM △ ｜ 17D
12-11  C +0.2k / P +0.2k ｜ Activity LOW ｜ 24D

📆 11-20 Forward Structure
存量OI: C 94.3k / P 60.0k，今日变化ΔOI: C +7.0k / P -0.4k，平值价格ATM: C $43.98 / P $42.43 ｜ ATM IV 142.7%，净 delta 敞口 590k shares
Top ΔOI: C 1060 +1,351 ｜ P 790 +613
仓位参考: Max Pain 960 ｜ Call Wall 800（-0.3%，弱）（OI 1.5k） ｜ Put Wall 870（+8.4%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 142.7%｜历史 Rank 90%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 589,584 股

📆 11-27 Forward Structure
存量OI: C 22.1k / P 12.9k，今日变化ΔOI: C +2.5k / P +2.3k，平值价格ATM: C $59.00 / P $55.52 ｜ ATM IV 107.8%，净 delta 敞口 -3k shares
Top ΔOI: P 800 +799 ｜ C 850 +458 ｜ C 1000 +219
仓位参考: Max Pain 990 ｜ Call Wall 850（+5.9%，弱）（OI 0.5k） ｜ Put Wall 800（-0.3%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 107.8%｜历史 Rank 90%（近端代理）｜IV/RV 0.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,289 股

12-04（MEDIUM △）Top ΔOI: 880C +119 ｜ 1000C +83
12-04（MEDIUM △）仓位参考: Max Pain 950 ｜ Call Wall 880（+9.7%，弱）（OI 0.2k） ｜ Put Wall 820（+2.2%，弱）（OI 0.4k）

12-11（Activity LOW）仓位参考: Max Pain 920 ｜ Call Wall 840（+4.7%，弱）（OI 63） ｜ Put Wall 830（+3.5%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 11-20（3D）ATM IV 142.7% vs 11-27 107.8%（差 +34.9pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/SNDK_morning.json