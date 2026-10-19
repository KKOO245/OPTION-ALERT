# 期权晨报 2026-10-19（快照 10:20 ET）

📊 市场环境

SPY $766.80 ｜ QQQ $718.36
VIX 18.46 ↓7.7%（5D +21.4%） ｜ Vol Regime: NORMAL
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
🟡 **近现价集中开仓**: 10-20 276C ΔOI +4,819（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-20 276C ΔOI +4,819 占该期限总 OI 10.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 270.44 → 今开 271.82（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 272.60 ｜ 低 270.72

Options: P/C成交量 2.72 | OI比 1.03 | ATM IV 23.8% | Skew 3.1pp | Term 0.82 | ExpMove ±1.0%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价中性（Skew 3.1pp）｜当日成交偏 Put（P/C量 2.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.72×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.03×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-20（1D）±1.0% ｜ 10-21（2D）±1.3% ｜ 10-22（3D）±1.6% ｜ 10-23（4D）±1.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -931,318,159 | GEX Change vs 上次快照 -134,673,669 | Flip: Primary Flip: 281.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1253 / LOW 235 / INVALID 1398
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 281.89（全链重定价，覆盖 98%）
Put Wall 270（弱结构｜现价高于该位 0.3%） | Call Wall 290（弱结构｜现价低于该位 6.6%）
最近结构参考: Put Wall 270（现价高于该位 0.3%）
量化视角： 负 Gamma（9.31亿，无历史分位）｜负 Gamma 加深（1.35亿）｜现价位于 Flip 下方 3.93%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构）；上方 273（MaxPain，仅结算参考） / 290（Call Wall，弱结构）。
• Gamma 区域：切换参考 282（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 260.0P — Vol 58,247 | 最新价 $1.43 | OI 27217→79249 (ΔOI +52032张) | ΔOI/Volume 89.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增52032张（+191.2% vs前日OI），连续性待观察（方向未知）
10-30 250.0P — Vol 49,718 | 最新价 $0.62 | OI 1182→47915 (ΔOI +46733张) | ΔOI/Volume 94.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增46733张（+3953.7% vs前日OI），连续性待观察（方向未知）
11-20 257.0P — Vol 45,152 | 最新价 $2.55 | OI 5650→44947 (ΔOI +39297张) | ΔOI/Volume 87.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增39297张（+695.5% vs前日OI），连续性待观察（方向未知）
11-20 258.0P — Vol 82,320 | 最新价 $2.75 | OI 15911→32252 (ΔOI +16341张) | ΔOI/Volume 19.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16341张（+102.7% vs前日OI），连续性待观察（方向未知）
10-19 272.0P — Vol 45,629 | 最新价 $2.25 | OI 2260→16759 (ΔOI +14499张) | ΔOI/Volume 31.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14499张（+641.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 168,902 张（Put 168,902 / Call 0），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $25M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 73.2k / P 75.6k，今日成交量: C 46.0k / P 125.4k，平值价格ATM: C $0.68 / P $0.69 ｜ ATM IV 23.8%，预期波动 ±0.5%，Max Pain 273
Top ΔOI: P 272 +14,499 ｜ P 270 +13,029 ｜ C 276 +12,558

📆 Forward Expiration Structure

10-20  C +10.5k / P +8.6k ｜ Activity HIGH ｜ 1D
10-21  C +14.2k / P +7.7k ｜ Activity HIGH ｜ 2D
10-22  C +4.9k / P +2.6k ｜ Activity HIGH ｜ 3D
10-23  C +13.1k / P +35.6k ｜ Activity HIGH ｜ 4D

📆 10-20 Forward Structure
存量OI: C 21.9k / P 22.6k，今日变化ΔOI: C +10.5k / P +8.6k，平值价格ATM: C $1.29 / P $1.30 ｜ ATM IV 20.5%，净 delta 敞口 -26k shares
Top ΔOI: C 276 +4,819 ｜ P 268 +2,000 ｜ C 272 +1,797
仓位参考: Max Pain 273 ｜ Call Wall 276（+1.9%）（OI 5.5k） ｜ Put Wall 270（-0.3%，弱）（OI 2.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 20.5%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 25,983 股

📆 10-21 Forward Structure
存量OI: C 22.4k / P 17.7k，今日变化ΔOI: C +14.2k / P +7.7k，平值价格ATM: C $1.64 / P $1.77 ｜ ATM IV 19.9%，净 delta 敞口 170k shares
Top ΔOI: C 275 +3,250 ｜ C 277 +2,045 ｜ C 274 +1,873
仓位参考: Max Pain 272 ｜ Call Wall 275（+1.6%，弱）（OI 3.7k） ｜ Put Wall 260（-4.0%）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 19.9%｜净 delta 敞口 正 169,611 股

📆 10-22 Forward Structure
存量OI: C 11.4k / P 17.3k，今日变化ΔOI: C +4.9k / P +2.6k，平值价格ATM: C $2.20 / P $2.04 ｜ ATM IV 20.0%，净 delta 敞口 47k shares
Top ΔOI: C 275 +2,420 ｜ C 274 +878 ｜ P 266 +726
仓位参考: Max Pain 274 ｜ Call Wall 275（+1.6%）（OI 2.8k） ｜ Put Wall 265（-2.1%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 20.0%｜净 delta 敞口 正 47,060 股

📆 10-23 Forward Structure
存量OI: C 130.9k / P 148.3k，今日变化ΔOI: C +13.1k / P +35.6k，平值价格ATM: C $2.39 / P $2.37 ｜ ATM IV 20.3%，净 delta 敞口 -216k shares
Top ΔOI: P 267 +4,792 ｜ C 281 +4,573 ｜ P 260 +3,994
仓位参考: Max Pain 277 ｜ Call Wall 281（+3.8%，弱）（OI 11.6k） ｜ Put Wall 277（+2.3%，弱）（OI 12.2k）
量化解读： 存量两侧均衡｜ATM IV 20.3%｜净 delta 敞口 负 216,348 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/IWM_morning.json