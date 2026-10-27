# 期权晨报 2026-10-26（快照 09:08 ET）

📊 市场环境

SPY $765.37 ｜ QQQ $712.20
VIX 19.22 ↓1.2%（5D +4.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-26

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 待公布 ｜ 前值 0
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🟡 **近现价集中开仓**: 10-27 283C ΔOI +20,816（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-27 283C ΔOI +20,816 占该期限总 OI 31.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 275.75 → 今开 274.85（-0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 276.24 ｜ 低 273.35

Options: P/C成交量 0.92 | OI比 0.74 | ATM IV 32.9% | Skew 2.2pp | Term 0.62 | ExpMove ±1.4%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.62，近月 IV 高于远月）｜保护溢价中性（Skew 2.2pp）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.92×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-27（1D）±1.4% ｜ 10-28（2D）±1.9% ｜ 10-29（3D）±2.2% ｜ 10-30（4D）±2.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -553,608,743 | GEX Change vs 上次快照 -29,693,023 | Flip: Primary Flip: 280.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1204 / LOW 250 / INVALID 1274
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 280.69（全链重定价，覆盖 98%）
Put Wall 260（弱结构｜现价高于该位 6.1%） | Call Wall 290（弱结构｜现价低于该位 4.9%）
最近结构参考: Flip 281（现价低于该位 1.7%）
量化视角： 负 Gamma（5.54亿，无历史分位）｜负 Gamma 加深（2969万）｜现价位于 Flip 下方 1.73%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 260（Put Wall，弱结构） / 275（MaxPain，仅结算参考）；上方 290（Call Wall，弱结构）。
• Gamma 区域：切换参考 281（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 261.0P — Vol 72,383 | 最新价 $2.07 | OI 50763→86449 (ΔOI +35686张) | ΔOI/Volume 49.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增35686张（+70.3% vs前日OI），连续性待观察（方向未知）
11-20 260.0P — Vol 76,696 | 最新价 $1.90 | OI 99553→132495 (ΔOI +32942张) | ΔOI/Volume 43.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增32942张（+33.1% vs前日OI），连续性待观察（方向未知）
10-26 282.0C — Vol 34,609 | 最新价 $0.07 | OI 1768→30624 (ΔOI +28856张) | ΔOI/Volume 83.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增28856张（+1632.1% vs前日OI），连续性待观察（方向未知）
11-20 262.0P — Vol 62,630 | 最新价 $2.21 | OI 49982→77607 (ΔOI +27625张) | ΔOI/Volume 44.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27625张（+55.3% vs前日OI），连续性待观察（方向未知）
10-27 283.0C — Vol 21,593 | 最新价 $0.10 | OI 936→21752 (ΔOI +20816张) | ΔOI/Volume 96.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20816张（+2223.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 145,925 张（Put 96,253 / Call 49,672），跨 3 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 85.7k / P 63.5k，今日成交量: C 78.5k / P 72.5k，平值价格ATM: C $1.04 / P $1.09 ｜ ATM IV 32.9%，预期波动 ±0.8%，Max Pain 275
Top ΔOI: C 282 +28,856 ｜ C 280 +8,457 ｜ P 275 +3,249

📆 Forward Expiration Structure

10-27  C +21.5k / P +4.6k ｜ Activity HIGH ｜ 1D
10-28  C +1.9k / P +9.0k ｜ Activity HIGH ｜ 2D
10-29  C +2.4k / P +5.7k ｜ Activity HIGH ｜ 3D
10-30  C +11.5k / P +6.2k ｜ Activity HIGH ｜ 4D

📆 10-27 Forward Structure
存量OI: C 41.9k / P 24.9k，今日变化ΔOI: C +21.5k / P +4.6k，平值价格ATM: C $1.82 / P $1.92 ｜ ATM IV 23.3%，净 delta 敞口 -44k shares
Top ΔOI: C 283 +20,816 ｜ P 275 +1,639 ｜ P 268 +889
仓位参考: Max Pain 275 ｜ Call Wall 283（+2.6%）（OI 21.8k） ｜ Put Wall 275（-0.3%，弱）（OI 2.5k）
量化解读： 存量 Call 重｜ATM IV 23.3%｜期限正常（远月高于近端）｜净 delta 敞口 负 43,800 股

📆 10-28 Forward Structure
存量OI: C 12.6k / P 29.7k，今日变化ΔOI: C +1.9k / P +9.0k，平值价格ATM: C $2.59 / P $2.54 ｜ ATM IV 26.9%，净 delta 敞口 -223k shares
Top ΔOI: P 275 +5,072 ｜ P 263 +1,124 ｜ P 270 +879
仓位参考: Max Pain 275 ｜ Call Wall 275（-0.3%）（OI 3.0k） ｜ Put Wall 275（-0.3%）（OI 6.3k）
量化解读： 存量 Put 重｜ATM IV 26.9%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 222,666 股

📆 10-29 Forward Structure
存量OI: C 46.3k / P 17.1k，今日变化ΔOI: C +2.4k / P +5.7k，平值价格ATM: C $2.91 / P $3.05 ｜ ATM IV 27.0%，净 delta 敞口 -140k shares
Top ΔOI: P 274 +4,033 ｜ C 291 +661 ｜ P 273 +336
仓位参考: Max Pain 275 ｜ Call Wall 280（+1.5%，弱）（OI 15.3k） ｜ Put Wall 274（-0.7%）（OI 4.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 27.0%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 140,199 股

📆 10-30 Forward Structure
存量OI: C 210.9k / P 494.8k，今日变化ΔOI: C +11.5k / P +6.2k，平值价格ATM: C $3.34 / P $3.33 ｜ ATM IV 26.0%，净 delta 敞口 -219k shares
Top ΔOI: P 275 +8,995 ｜ P 258 -6,799 ｜ P 253 -5,870
仓位参考: Max Pain 278 ｜ Call Wall 278（+0.8%）（OI 28.4k） ｜ Put Wall 260（-5.7%）（OI 86.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 26.0%｜净 delta 敞口 负 218,615 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/IWM_morning.json