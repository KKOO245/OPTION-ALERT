# 期权晚报 2026-10-19（快照 16:40 ET）

📊 市场环境

SPY $766.48 ｜ QQQ $718.36
VIX 18.44 ↓7.8%（5D +21.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 23.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🟡 **近现价集中开仓**: 10-20 276C ΔOI +4,819（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-20 276C ΔOI +4,819 占该期限总 OI 10.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 271.82 → 收盘 271.28（-0.2%） ｜ 今日高 272.66 ｜ 低 270.72 ｜ 昨收 270.44 → 收盘 271.28（+0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.78 | OI比 1.03 | ATM IV 15.3% | Skew -11.3pp | Term 1.29 | ExpMove ±0.8%（近端） | Rank — (历史不足)
量化视角： 期限结构正常偏陡（Term 1.29）｜Put 保护异常便宜（Skew -11.3pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.78×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.03×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-20（1D）±0.8% ｜ 10-21（2D）±1.1% ｜ 10-22（3D）±1.4% ｜ 10-23（4D）±1.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -825,090,702 | GEX Change vs 上次快照 106,227,456 | Flip: Primary Flip: 282.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 1210 / LOW 243 / INVALID 1433
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 282.38（全链重定价，覆盖 96%）
Put Wall 270（弱结构｜现价高于该位 0.5%） | Call Wall 290（弱结构｜现价低于该位 6.5%）
最近结构参考: Put Wall 270（现价高于该位 0.5%）
量化视角： 负 Gamma（8.25亿，无历史分位）｜负 Gamma 缓解（+1.06亿）｜现价位于 Flip 下方 3.93%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构）；上方 273（MaxPain，仅结算参考） / 290（Call Wall，弱结构）。
• Gamma 区域：切换参考 282（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 260.0P — Vol 3,349 | 最新价 $0.96 | OI 27217→79249 (ΔOI +52032张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增52032张（+191.2% vs前日OI），连续性待观察（方向未知）
10-30 250.0P — Vol 851 | 最新价 $0.33 | OI 1182→47915 (ΔOI +46733张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增46733张（+3953.7% vs前日OI），连续性待观察（方向未知）
11-20 257.0P — Vol 43,373 | 最新价 $2.15 | OI 5650→44947 (ΔOI +39297张) | ΔOI/Volume 90.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增39297张（+695.5% vs前日OI），连续性待观察（方向未知）
11-20 258.0P — Vol 45,791 | 最新价 $2.32 | OI 15911→32252 (ΔOI +16341张) | ΔOI/Volume 35.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16341张（+102.7% vs前日OI），连续性待观察（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 154,403 张（Put 154,403 / Call 0），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $12M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-20  C +10.5k / P +8.6k ｜ Activity HIGH ｜ 1D
10-21  C +14.2k / P +7.7k ｜ Activity HIGH ｜ 2D
10-22  C +4.9k / P +2.6k ｜ Activity HIGH ｜ 3D
10-23  C +13.1k / P +35.6k ｜ Activity HIGH ｜ 4D

📆 10-20 Forward Structure
存量OI: C 21.9k / P 22.6k，今日变化ΔOI: C +10.5k / P +8.6k，平值价格ATM: C $1.16 / P $0.96 ｜ ATM IV 18.9%，净 delta 敞口 2k shares
Top ΔOI: C 276 +4,819 ｜ P 268 +2,000 ｜ C 272 +1,797
仓位参考: Max Pain 273 ｜ Call Wall 276（+1.7%）（OI 5.5k） ｜ Put Wall 270（-0.5%，弱）（OI 2.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 18.9%｜期限正常（远月高于近端）｜净 delta 敞口 正 1,566 股

📆 10-21 Forward Structure
存量OI: C 22.4k / P 17.7k，今日变化ΔOI: C +14.2k / P +7.7k，平值价格ATM: C $1.64 / P $1.43 ｜ ATM IV 19.1%，净 delta 敞口 189k shares
Top ΔOI: C 275 +3,250 ｜ C 277 +2,045 ｜ C 274 +1,873
仓位参考: Max Pain 272 ｜ Call Wall 275（+1.4%，弱）（OI 3.7k） ｜ Put Wall 260（-4.2%）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 19.1%｜净 delta 敞口 正 188,769 股

📆 10-22 Forward Structure
存量OI: C 11.4k / P 17.3k，今日变化ΔOI: C +4.9k / P +2.6k，平值价格ATM: C $2.00 / P $1.82 ｜ ATM IV 19.4%，净 delta 敞口 51k shares
Top ΔOI: C 275 +2,420 ｜ C 274 +878 ｜ P 266 +726
仓位参考: Max Pain 274 ｜ Call Wall 275（+1.4%）（OI 2.8k） ｜ Put Wall 265（-2.3%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 19.4%｜净 delta 敞口 正 51,107 股

📆 10-23 Forward Structure
存量OI: C 130.9k / P 148.3k，今日变化ΔOI: C +13.1k / P +35.6k，平值价格ATM: C $2.38 / P $2.11 ｜ ATM IV 19.9%，净 delta 敞口 -151k shares
Top ΔOI: P 267 +4,792 ｜ C 281 +4,573 ｜ P 260 +3,994
仓位参考: Max Pain 277 ｜ Call Wall 281（+3.6%，弱）（OI 11.6k） ｜ Put Wall 277（+2.1%，弱）（OI 12.2k）
量化解读： 存量两侧均衡｜ATM IV 19.9%｜净 delta 敞口 负 151,258 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/IWM_evening.json