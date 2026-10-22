# 期权晨报 2026-10-22（快照 10:20 ET）

📊 市场环境

SPY $763.51 ｜ QQQ $708.64
VIX 17.91 ↑7.4%（5D +8.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 20.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 283C ΔOI +16,820（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 276.48 → 今开 274.81（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 277.28 ｜ 低 274.74

Options: P/C成交量 0.68 | OI比 1.05 | ATM IV 26.0% | Skew 0.5pp | Term 0.76 | ExpMove ±1.0%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价薄（Skew 0.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.68×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.05×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（1D）±1.0% ｜ 10-26（4D）±1.3% ｜ 10-27（5D）±1.6% ｜ 10-28（6D）±2.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -445,390,528 | GEX Change vs 上次快照 -22,695,691 | Flip: Primary Flip: 279.76（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1274 / LOW 190 / INVALID 1392
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 279.76（全链重定价，覆盖 98%）
Put Wall 270（弱结构｜现价高于该位 2.5%） | Call Wall 280（弱结构｜现价低于该位 1.1%）
最近结构参考: Flip 280（现价低于该位 1.0%）
量化视角： 负 Gamma（4.45亿，无历史分位）｜负 Gamma 加深（2270万）｜现价位于 Flip 下方 1.04%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构） / 275（MaxPain，仅结算参考）；上方 280（Call Wall，弱结构）。
• Gamma 区域：切换参考 280（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 263.0P — Vol 61,347 | 最新价 $1.91 | OI 44064→84475 (ΔOI +40411张) | ΔOI/Volume 65.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增40411张（+91.7% vs前日OI），连续性待观察（方向未知）
11-20 270.0P — Vol 37,473 | 最新价 $3.36 | OI 141536→168381 (ΔOI +26845张) | ΔOI/Volume 71.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26845张（+19.0% vs前日OI），连续性待观察（方向未知）
10-23 283.0C — Vol 19,658 | 最新价 $0.06 | OI 4709→21529 (ΔOI +16820张) | ΔOI/Volume 85.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16820张（+357.2% vs前日OI），连续性待观察（方向未知）
10-23 277.0P — Vol 20,308 | 最新价 $1.79 | OI 12250→23141 (ΔOI +10891张) | ΔOI/Volume 53.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10891张（+88.9% vs前日OI），连续性待观察（方向未知）
11-06 270.0P — Vol 15,979 | 最新价 $2.05 | OI 5656→16546 (ΔOI +10890张) | ΔOI/Volume 68.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10890张（+192.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 105,857 张（Put 89,037 / Call 16,820），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $21M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 44.4k / P 46.4k，今日成交量: C 126.8k / P 85.9k，平值价格ATM: C $0.82 / P $0.76 ｜ ATM IV 26.0%，预期波动 ±0.6%，Max Pain 275
Top ΔOI: C 282 -8,521 ｜ P 271 +5,357 ｜ P 274 +2,930

📆 Forward Expiration Structure

10-23  C +27.3k / P +29.9k ｜ Activity MEDIUM △ ｜ 1D
10-26  C +2.6k / P +10.1k ｜ Activity HIGH ｜ 4D
10-27  C +2.1k / P +3.2k ｜ Activity HIGH ｜ 5D
10-28  C +1.9k / P +7.4k ｜ Activity HIGH ｜ 6D

📆 10-23 Forward Structure
存量OI: C 183.5k / P 219.7k，今日变化ΔOI: C +27.3k / P +29.9k，平值价格ATM: C $1.46 / P $1.37 ｜ ATM IV 21.3%，净 delta 敞口 -629k shares
Top ΔOI: C 283 +16,820 ｜ P 277 +10,891 ｜ P 273 +9,074
仓位参考: Max Pain 277 ｜ Call Wall 283（+2.2%，弱）（OI 21.5k） ｜ Put Wall 277（+0.1%，弱）（OI 23.1k）
量化解读： 存量 Put 重｜ATM IV 21.3%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 628,721 股

📆 10-26 Forward Structure
存量OI: C 26.8k / P 30.7k，今日变化ΔOI: C +2.6k / P +10.1k，平值价格ATM: C $1.88 / P $1.72 ｜ ATM IV 15.7%，净 delta 敞口 -67k shares
Top ΔOI: P 269 +4,555 ｜ P 264 +2,300 ｜ C 285 +970
仓位参考: Max Pain 274 ｜ Call Wall 283（+2.2%，弱）（OI 5.2k） ｜ Put Wall 269（-2.8%）（OI 5.2k）
量化解读： 存量两侧均衡｜ATM IV 15.7%｜期限正常（远月高于近端）｜净 delta 敞口 负 66,758 股

📆 10-27 Forward Structure
存量OI: C 18.6k / P 16.9k，今日变化ΔOI: C +2.1k / P +3.2k，平值价格ATM: C $2.24 / P $2.18 ｜ ATM IV 16.5%，净 delta 敞口 9k shares
Top ΔOI: P 265 +1,184 ｜ C 283 +582 ｜ P 266 +536
仓位参考: Max Pain 274 ｜ Call Wall 284（+2.6%）（OI 4.3k） ｜ Put Wall 262（-5.4%，弱）（OI 1.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 16.5%｜期限正常（远月高于近端）｜净 delta 敞口 正 8,930 股

📆 10-28 Forward Structure
存量OI: C 9.2k / P 15.9k，今日变化ΔOI: C +1.9k / P +7.4k，平值价格ATM: C $3.01 / P $2.70 ｜ ATM IV 19.7%，净 delta 敞口 -141k shares
Top ΔOI: P 272 +1,793 ｜ P 273 +1,653 ｜ P 275 +957
仓位参考: Max Pain 275 ｜ Call Wall 275（-0.7%）（OI 2.6k） ｜ Put Wall 272（-1.8%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 19.7%｜净 delta 敞口 负 141,007 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/IWM_morning.json