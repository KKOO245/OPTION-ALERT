# 期权晨报 2026-10-16（快照 10:20 ET）

📊 市场环境

SPY $762.90 ｜ QQQ $709.80
VIX 15.93 ↓3.2%（5D +7.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 17.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-19 278C ΔOI +2,218（距现价 +1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 275.08 → 今开 275.52（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 275.91 ｜ 低 274.41

Options: P/C成交量 1.15 | OI比 1.37 | ATM IV 20.9% | Skew -0.8pp | Term 0.87 | ExpMove ±0.8%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.87，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.15）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.15×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.37×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-19（3D）±0.8% ｜ 10-20（4D）±1.1% ｜ 10-21（5D）±1.3% ｜ 10-22（6D）±1.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,367,022,328 | GEX Change vs 上次快照 306,186,018 | Flip: Primary Flip: 280.85（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 1233 / LOW 241 / INVALID 1364
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 280.85（全链重定价，覆盖 90%）
Put Wall 270（弱结构｜现价高于该位 1.8%） | Call Wall 285（弱结构｜现价低于该位 3.5%）
最近结构参考: Put Wall 270（现价高于该位 1.8%）
量化视角： 负 Gamma（13.67亿，无历史分位）｜负 Gamma 缓解（+3.06亿）｜现价位于 Flip 下方 2.12%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构）；上方 279（MaxPain，仅结算参考） / 285（Call Wall，弱结构）。
• Gamma 区域：切换参考 281（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 262.0P — Vol 42,492 | 最新价 $2.21 | OI 26083→53281 (ΔOI +27198张) | ΔOI/Volume 64.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27198张（+104.3% vs前日OI），连续性待观察（方向未知）
11-20 260.0P — Vol 75,656 | 最新价 $1.88 | OI 67300→87132 (ΔOI +19832张) | ΔOI/Volume 26.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19832张（+29.5% vs前日OI），连续性待观察（方向未知）
10-16 278.0C — Vol 25,381 | 最新价 $0.27 | OI 10556→25198 (ΔOI +14642张) | ΔOI/Volume 57.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14642张（+138.7% vs前日OI），连续性待观察（方向未知）
10-16 275.0C — Vol 51,006 | 最新价 $1.16 | OI 10180→24375 (ΔOI +14195张) | ΔOI/Volume 27.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14195张（+139.4% vs前日OI），连续性待观察（方向未知）
10-30 258.0P — Vol 14,754 | 最新价 $0.46 | OI 1375→15466 (ΔOI +14091张) | ΔOI/Volume 95.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14091张（+1024.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 89,958 张（Put 61,121 / Call 28,837），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $10M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 707.3k / P 969.7k，今日成交量: C 71.3k / P 82.1k，平值价格ATM: C $0.62 / P $0.62 ｜ ATM IV 20.9%，预期波动 ±0.5%，Max Pain 279
Top ΔOI: P 282 -19,635 ｜ C 278 +14,642 ｜ C 275 +14,195

📆 Forward Expiration Structure

10-19  C +9.0k / P +4.7k ｜ Activity HIGH ｜ 3D
10-20  C +2.0k / P +1.4k ｜ Activity HIGH ｜ 4D
10-21  C +1.9k / P +0.8k ｜ Activity HIGH ｜ 5D
10-22  C +0.7k / P +1.5k ｜ Activity HIGH ｜ 6D

📆 10-19 Forward Structure
存量OI: C 24.9k / P 22.2k，今日变化ΔOI: C +9.0k / P +4.7k，平值价格ATM: C $1.19 / P $1.13 ｜ ATM IV 11.2%，净 delta 敞口 116k shares
Top ΔOI: C 278 +2,218 ｜ C 281 +1,649 ｜ C 279 +1,600
仓位参考: Max Pain 275 ｜ Call Wall 278（+1.1%）（OI 3.9k） ｜ Put Wall 272（-1.1%，弱）（OI 2.3k）
量化解读： 存量两侧均衡｜ATM IV 11.2%｜期限正常（远月高于近端）｜净 delta 敞口 正 116,248 股

📆 10-20 Forward Structure
存量OI: C 11.3k / P 14.0k，今日变化ΔOI: C +2.0k / P +1.4k，平值价格ATM: C $1.58 / P $1.40 ｜ ATM IV 12.5%，净 delta 敞口 47k shares
Top ΔOI: C 276 +339 ｜ C 279 +262 ｜ P 267 +245
仓位参考: Max Pain 275 ｜ Call Wall 277（+0.8%，弱）（OI 1.6k） ｜ Put Wall 269（-2.1%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 12.5%｜期限正常（远月高于近端）｜净 delta 敞口 正 47,016 股

📆 10-21 Forward Structure
存量OI: C 8.2k / P 10.0k，今日变化ΔOI: C +1.9k / P +0.8k，平值价格ATM: C $1.77 / P $1.71 ｜ ATM IV 13.4%，净 delta 敞口 36k shares
Top ΔOI: C 285 +452 ｜ C 284 +439 ｜ C 279 +287
仓位参考: Max Pain 276 ｜ Call Wall 285（+3.7%，弱）（OI 1.4k） ｜ Put Wall 260（-5.4%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 13.4%｜期限正常（远月高于近端）｜净 delta 敞口 正 36,008 股

📆 10-22 Forward Structure
存量OI: C 6.5k / P 14.6k，今日变化ΔOI: C +0.7k / P +1.5k，平值价格ATM: C $2.12 / P $1.98 ｜ ATM IV 14.2%，净 delta 敞口 -1k shares
Top ΔOI: P 275 +367 ｜ P 271 +354 ｜ C 278 +339
仓位参考: Max Pain 275 ｜ Call Wall 283（+2.9%，弱）（OI 1.0k） ｜ Put Wall 265（-3.6%，弱）（OI 1.7k）
量化解读： 存量 Put 重｜ATM IV 14.2%｜净 delta 敞口 负 1,225 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/IWM_morning.json