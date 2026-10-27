# 期权晚报 2026-10-26（快照 21:54 ET）

📊 市场环境

SPY $765.37 ｜ QQQ $712.20
VIX 18.39 ↓5.5%（5D -0.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：无更新，来源自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 待公布 ｜ 前值 0
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 274.85 → 收盘 276.99（+0.8%） ｜ 今日高 278.77 ｜ 低 276.00 ｜ 昨收 275.75 → 收盘 276.99（+0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.10 | OI比 0.59 | ATM IV 16.7% | Skew 1.2pp | Term 1.16 | ExpMove ±0.7%（近端） | Rank — (历史不足)
量化视角： 期限结构正常偏陡（Term 1.16）｜保护溢价薄（Skew 1.2pp）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.10×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-27（1D）±0.7% ｜ 10-28（2D）±1.4% ｜ 10-29（3D）±1.7% ｜ 10-30（4D）±1.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -488,625,381 | GEX Change vs 上次快照 64,983,362 | Flip: Primary Flip: 280.94（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1232 / LOW 151 / INVALID 1177
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 280.94（全链重定价，覆盖 99%）
Put Wall 260（弱结构｜现价高于该位 6.5%） | Call Wall 290（弱结构｜现价低于该位 4.5%）
最近结构参考: Flip 281（现价低于该位 1.4%）
量化视角： 负 Gamma（4.89亿，无历史分位）｜负 Gamma 缓解（+6498万）｜现价位于 Flip 下方 1.40%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 260（Put Wall，弱结构） / 275（MaxPain，仅结算参考）；上方 290（Call Wall，弱结构）。
• Gamma 区域：切换参考 281（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 261.0P — Vol 483 | 最新价 $1.56 | OI 50763→86449 (ΔOI +35686张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增35686张（+70.3% vs前日OI），连续性待观察（方向未知）
11-20 260.0P — Vol 8,215 | 最新价 $1.43 | OI 99553→132495 (ΔOI +32942张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增32942张（+33.1% vs前日OI），连续性待观察（方向未知）
11-20 262.0P — Vol 48,406 | 最新价 $1.69 | OI 49982→77607 (ΔOI +27625张) | ΔOI/Volume 57.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27625张（+55.3% vs前日OI），连续性待观察（方向未知）
10-27 283.0C — Vol 1,997 | 最新价 $0.02 | OI 936→21752 (ΔOI +20816张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20816张（+2223.9% vs前日OI），连续性待观察（方向未知）
11-06 262.0P — Vol 89 | 最新价 $0.66 | OI 10824→24206 (ΔOI +13382张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13382张（+123.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 130,451 张（Put 109,635 / Call 20,816），跨 3 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-27  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-28  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-29  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 4D

📆 10-27 Forward Structure
存量OI: C 41.9k / P 24.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.87 / P $1.09 ｜ ATM IV 16.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 275 ｜ Call Wall 283（+2.2%）（OI 21.8k） ｜ Put Wall 275（-0.7%，弱）（OI 2.5k）
量化解读： 存量 Call 重｜ATM IV 16.7%｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-28（Activity LOW）仓位参考: Max Pain 275 ｜ Call Wall 275（-0.7%）（OI 3.0k） ｜ Put Wall 275（-0.7%）（OI 6.3k）

10-29（Activity LOW）仓位参考: Max Pain 275 ｜ Call Wall 280（+1.1%，弱）（OI 15.3k） ｜ Put Wall 274（-1.1%）（OI 4.4k）

10-30（Activity LOW）仓位参考: Max Pain 278 ｜ Call Wall 278（+0.4%）（OI 28.4k） ｜ Put Wall 260（-6.1%）（OI 86.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/IWM_evening.json