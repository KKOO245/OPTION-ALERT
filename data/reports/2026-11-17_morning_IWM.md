# 期权晨报 2026-11-17（快照 10:20 ET）

📊 市场环境

SPY $737.44 ｜ QQQ $658.84
VIX 22.73 ↓0.8%（5D +16.8%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.3（fear）
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
🟡 **近现价集中开仓**: 11-18 275P ΔOI -1,217（距现价 +1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-23 270P ΔOI +12,177 占该期限总 OI 35.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 272.94 → 今开 272.03（-0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 273.04 ｜ 低 270.98

Options: P/C成交量 0.54 | OI比 1.09 | ATM IV 30.0% | Skew 2.9pp | Term 0.71 | ExpMove ±1.2%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜保护溢价中性（Skew 2.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.09×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-18（1D）±1.2% ｜ 11-19（2D）±1.6% ｜ 11-20（3D）±2.0% ｜ 11-23（6D）±2.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,610,110,178 | GEX Change vs 上次快照 -71,455,870 | Flip: Primary Flip: 282.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1219 / LOW 234 / INVALID 1095
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 282.63（全链重定价，覆盖 97%）
Put Wall 270（弱结构｜现价高于该位 0.8%）
最近结构参考: Put Wall 270（现价高于该位 0.8%）
量化视角： 负 Gamma（16.10亿，无历史分位）｜负 Gamma 加深（7146万）｜现价位于 Flip 下方 3.71%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构）；上方 275（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 283（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 259.0P — Vol 42,186 | 最新价 $2.90 | OI 5323→32355 (ΔOI +27032张) | ΔOI/Volume 64.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27032张（+507.8% vs前日OI），连续性待观察（方向未知）
11-20 264.0P — Vol 21,782 | 最新价 $0.65 | OI 51089→67655 (ΔOI +16566张) | ΔOI/Volume 76.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16566张（+32.4% vs前日OI），连续性待观察（方向未知）
12-18 261.0P — Vol 40,890 | 最新价 $3.30 | OI 2334→15484 (ΔOI +13150张) | ΔOI/Volume 32.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13150张（+563.4% vs前日OI），连续性待观察（方向未知）
11-23 270.0P — Vol 15,336 | 最新价 $2.19 | OI 211→12388 (ΔOI +12177张) | ΔOI/Volume 79.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12177张（+5771.1% vs前日OI），连续性待观察（方向未知）
11-27 255.0P — Vol 9,971 | 最新价 $0.55 | OI 1060→10584 (ΔOI +9524张) | ΔOI/Volume 95.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9524张（+898.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 78,449 张（Put 78,449 / Call 0），跨 4 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $15M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 23.1k / P 25.2k，今日成交量: C 94.0k / P 50.5k，平值价格ATM: C $1.06 / P $0.71 ｜ ATM IV 30.0%，预期波动 ±0.7%，Max Pain 275
Top ΔOI: C 277 +2,150 ｜ C 275 +1,669 ｜ P 267 +1,265

📆 Forward Expiration Structure

11-18  C +5.3k / P +2.7k ｜ Activity HIGH ｜ 1D
11-19  C +1.3k / P +2.5k ｜ Activity HIGH ｜ 2D
11-20  C +6.7k / P -37.0k ｜ Activity HIGH ｜ 3D
11-23  C +7.0k / P +15.5k ｜ Activity HIGH ｜ 6D

📆 11-18 Forward Structure
存量OI: C 21.5k / P 20.7k，今日变化ΔOI: C +5.3k / P +2.7k，平值价格ATM: C $1.86 / P $1.50 ｜ ATM IV 26.2%，净 delta 敞口 154k shares
Top ΔOI: P 275 -1,217 ｜ P 267 +1,212 ｜ C 275 +1,126
仓位参考: Max Pain 276 ｜ Call Wall 278（+2.1%，弱）（OI 2.2k） ｜ Put Wall 275（+1.0%）（OI 3.2k）
量化解读： 存量两侧均衡｜ATM IV 26.2%｜历史 Rank 68%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 153,872 股

📆 11-19 Forward Structure
存量OI: C 15.1k / P 27.0k，今日变化ΔOI: C +1.3k / P +2.5k，平值价格ATM: C $2.44 / P $1.88 ｜ ATM IV 25.6%，净 delta 敞口 -23k shares
Top ΔOI: P 270 +553 ｜ P 271 +458 ｜ P 267 +358
仓位参考: Max Pain 278 ｜ Call Wall 287（+5.5%）（OI 3.4k） ｜ Put Wall 272（-0.1%，弱）（OI 3.9k）
量化解读： 存量 Put 重｜ATM IV 25.6%｜历史 Rank 68%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 23,021 股

📆 11-20 Forward Structure
存量OI: C 569.1k / P 1501.0k，今日变化ΔOI: C +6.7k / P -37.0k，平值价格ATM: C $2.91 / P $2.49 ｜ ATM IV 25.9%，净 delta 敞口 2.7M shares
Top ΔOI: P 268 -26,781 ｜ P 264 +16,566 ｜ P 290 -12,597
仓位参考: Max Pain 279 ｜ Call Wall 285（+4.7%，弱）（OI 51.5k） ｜ Put Wall 265（-2.6%，弱）（OI 138.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 25.9%｜历史 Rank 68%（近端代理）｜IV/RV 1.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,657,572 股

📆 11-23 Forward Structure
存量OI: C 12.7k / P 21.7k，今日变化ΔOI: C +7.0k / P +15.5k，平值价格ATM: C $3.15 / P $2.90 ｜ ATM IV 21.6%，净 delta 敞口 -441k shares
Top ΔOI: P 270 +12,177 ｜ C 278 +1,090 ｜ C 282 +1,085
仓位参考: Max Pain 277 ｜ Call Wall 282（+3.6%，弱）（OI 1.5k） ｜ Put Wall 270（-0.8%）（OI 12.4k）
量化解读： 存量 Put 重｜ATM IV 21.6%｜历史 Rank 68%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 负 440,709 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/IWM_morning.json