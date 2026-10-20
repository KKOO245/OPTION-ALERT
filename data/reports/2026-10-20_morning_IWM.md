# 期权晨报 2026-10-20（快照 10:20 ET）

📊 市场环境

SPY $768.68 ｜ QQQ $720.22
VIX 18.12 ↓1.7%（5D +18.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 25.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-21 277C ΔOI +9,556（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-21 277C ΔOI +9,556 占该期限总 OI 14.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 271.28 → 今开 271.53（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 274.62 ｜ 低 271.29

Options: P/C成交量 0.63 | OI比 1.34 | ATM IV 23.6% | Skew 1.9pp | Term 0.83 | ExpMove ±0.9%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价薄（Skew 1.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.34×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-21（1D）±0.9% ｜ 10-22（2D）±1.2% ｜ 10-23（3D）±1.5% ｜ 10-26（6D）±1.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -572,279,066 | GEX Change vs 上次快照 294,923,789 | Flip: Primary Flip: 281.24（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1299 / LOW 194 / INVALID 1393
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 281.24（全链重定价，覆盖 99%）
Put Wall 270（弱结构｜现价高于该位 1.4%） | Call Wall 290（弱结构｜现价低于该位 5.6%）
最近结构参考: Put Wall 270（现价高于该位 1.4%）
量化视角： 负 Gamma（5.72亿，无历史分位）｜负 Gamma 缓解（+2.95亿）｜现价位于 Flip 下方 2.65%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构） / 272（MaxPain，仅结算参考）；上方 290（Call Wall，弱结构）。
• Gamma 区域：切换参考 281（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 258.0P — Vol 45,791 | 最新价 $2.32 | OI 32252→62383 (ΔOI +30131张) | ΔOI/Volume 65.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30131张（+93.4% vs前日OI），连续性待观察（方向未知）
10-30 259.0P — Vol 25,479 | 最新价 $0.88 | OI 1436→26458 (ΔOI +25022张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增25022张（+1742.5% vs前日OI），连续性待观察（方向未知）
10-29 280.0C — Vol 15,147 | 最新价 $0.63 | OI 216→15157 (ΔOI +14941张) | ΔOI/Volume 98.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14941张（+6917.1% vs前日OI），连续性待观察（方向未知）
10-29 282.0C — Vol 9,802 | 最新价 $0.38 | OI 86→9867 (ΔOI +9781张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9781张（+11373.3% vs前日OI），连续性待观察（方向未知）
10-29 284.0C — Vol 9,750 | 最新价 $0.23 | OI 96→9783 (ΔOI +9687张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9687张（+10090.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 89,562 张（Put 55,153 / Call 34,409），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 26.9k / P 36.0k，今日成交量: C 145.4k / P 91.3k，平值价格ATM: C $0.56 / P $0.85 ｜ ATM IV 23.6%，预期波动 ±0.5%，Max Pain 272
Top ΔOI: C 274 +2,709 ｜ P 264 +2,694 ｜ C 276 -2,548

📆 Forward Expiration Structure

10-21  C +18.0k / P +10.3k ｜ Activity HIGH ｜ 1D
10-22  C +1.0k / P +6.1k ｜ Activity HIGH ｜ 2D
10-23  C +12.0k / P +28.4k ｜ Activity HIGH ｜ 3D
10-26  C +0.9k / P +3.4k ｜ Activity HIGH ｜ 6D

📆 10-21 Forward Structure
存量OI: C 40.4k / P 28.0k，今日变化ΔOI: C +18.0k / P +10.3k，平值价格ATM: C $1.13 / P $1.43 ｜ ATM IV 19.8%，净 delta 敞口 339k shares
Top ΔOI: C 277 +9,556 ｜ C 275 +6,933 ｜ P 260 +4,758
仓位参考: Max Pain 273 ｜ Call Wall 277（+1.2%，弱）（OI 12.2k） ｜ Put Wall 260（-5.0%）（OI 6.9k）
量化解读： 存量 Call 重｜ATM IV 19.8%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 338,610 股

📆 10-22 Forward Structure
存量OI: C 12.3k / P 23.4k，今日变化ΔOI: C +1.0k / P +6.1k，平值价格ATM: C $1.64 / P $1.76 ｜ ATM IV 19.7%，净 delta 敞口 -18k shares
Top ΔOI: P 267 +4,305
仓位参考: Max Pain 274 ｜ Call Wall 275（+0.4%）（OI 2.8k） ｜ Put Wall 267（-2.5%）（OI 4.8k）
量化解读： 存量 Put 重｜ATM IV 19.7%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 17,856 股

📆 10-23 Forward Structure
存量OI: C 142.9k / P 176.7k，今日变化ΔOI: C +12.0k / P +28.4k，平值价格ATM: C $2.02 / P $2.15 ｜ ATM IV 20.0%，净 delta 敞口 310k shares
Top ΔOI: P 267 +7,480 ｜ C 276 +4,254
仓位参考: Max Pain 276 ｜ Call Wall 281（+2.6%，弱）（OI 11.6k） ｜ Put Wall 267（-2.5%，弱）（OI 17.8k）
量化解读： 存量 Put 重｜ATM IV 20.0%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 310,178 股

📆 10-26 Forward Structure
存量OI: C 16.5k / P 15.5k，今日变化ΔOI: C +0.9k / P +3.4k，平值价格ATM: C $2.44 / P $2.42 ｜ ATM IV 16.8%，净 delta 敞口 62k shares
Top ΔOI: C 278 -2,047 ｜ P 262 +761 ｜ C 273 +721
仓位参考: Max Pain 273 ｜ Call Wall 283（+3.4%）（OI 3.4k） ｜ Put Wall 267（-2.5%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 16.8%｜净 delta 敞口 正 62,287 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/IWM_morning.json