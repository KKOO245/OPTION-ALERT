# 期权晨报 2026-09-18（快照 10:41 ET）

📊 市场环境

SPY $762.85 ｜ QQQ $nan
VIX 15.50 ↑0.4%（5D -2.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-21 225C ΔOI +4,031（距现价 +2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-23 225C ΔOI +8,539 占该期限总 OI 15.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 219.34 → 今开 219.36（+0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 220.89 ｜ 低 218.04

Options: P/C成交量 0.52 | OI比 0.90 | ATM IV 36.6% | Skew 0.4pp | Term 0.83 | ExpMove ±1.6%（近端） | Rank 23%
量化视角： IV 历史低位（Rank 23%，期权偏便宜）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价薄（Skew 0.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-21（3D）±1.6% ｜ 09-23（5D）±2.5% ｜ 09-25（7D）±3.1% ｜ 09-28（10D）±3.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 696,954,201 | GEX Change vs 上次快照 138,785,811 | Flip: Primary Flip: 211.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 700 / LOW 220 / INVALID 500
结构观察区: Primary Flip 211.00（全链重定价，覆盖 91%）
Put Wall 200（现价高于该位 10.2%） | Call Wall 220（弱结构｜现价高于该位 0.2%）
最近结构参考: Call Wall 220（现价高于该位 0.2%）
量化视角： 正 Gamma（6.97亿，无历史分位）｜正 Gamma 增强（+1.39亿）｜现价位于 Flip 上方 4.43%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall） / 205（MaxPain，仅结算参考） / 220（Call Wall，弱结构）。
• Gamma 区域：切换参考 211（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 105.0P — Vol 19,324（Yahoo补） | 最新价 $0.01 | OI 1744→20669 (ΔOI +18925张) | ΔOI/Volume 97.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18925张（+1085.2% vs前日OI），连续性待观察（方向未知）
09-25 222.5C — Vol 585 | 最新价 $2.14 | OI 3754→22326 (ΔOI +18572张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18572张（+494.7% vs前日OI），连续性待观察（方向未知）
10-16 235.0C — Vol 739 | 最新价 $2.26 | OI 37328→51173 (ΔOI +13845张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13845张（+37.1% vs前日OI），连续性待观察（方向未知）
09-25 197.5P — Vol 11 | 最新价 $0.17 | OI 3622→15368 (ΔOI +11746张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11746张（+324.3% vs前日OI），连续性待观察（方向未知）
09-25 227.5C — Vol 389 | 最新价 $0.88 | OI 3242→14641 (ΔOI +11399张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11399张（+351.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 74,487 张（Put 30,671 / Call 43,816），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 1338.5k / P 1207.4k，今日成交量: C 301.9k / P 155.9k，平值价格ATM: C $0.82 / P $0.86 ｜ ATM IV 36.6%，预期波动 ±0.8%，Max Pain 205
Top ΔOI: C 215 -12,497 ｜ C 220 -10,545 ｜ P 195 +10,542

📆 Forward Expiration Structure

09-21  C +12.6k / P +5.2k ｜ Activity HIGH ｜ 3D
09-23  C +13.6k / P +5.6k ｜ Activity HIGH ｜ 5D
09-25  C +42.8k / P +52.3k ｜ Activity HIGH ｜ 7D
09-28  C +2.6k / P +2.0k ｜ Activity HIGH ｜ 10D

📆 09-21 Forward Structure
存量OI: C 53.0k / P 47.4k，今日变化ΔOI: C +12.6k / P +5.2k，平值价格ATM: C $1.75 / P $1.74 ｜ ATM IV 21.0%，净 delta 敞口 126k shares
Top ΔOI: C 225 +4,031 ｜ C 220 +2,571 ｜ P 217 +1,852
仓位参考: Max Pain 215 ｜ Call Wall 225（+2.1%，弱）（OI 7.1k） ｜ Put Wall 200（-9.2%，弱）（OI 8.2k）
量化解读： 存量两侧均衡｜ATM IV 21.0%｜历史 Rank 23%（近端代理）｜IV/RV 0.56×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 125,500 股

📆 09-23 Forward Structure
存量OI: C 38.4k / P 17.7k，今日变化ΔOI: C +13.6k / P +5.6k，平值价格ATM: C $2.75 / P $2.70 ｜ ATM IV 25.9%，净 delta 敞口 230k shares
Top ΔOI: C 225 +8,539 ｜ C 227 +1,824 ｜ P 205 +1,788
仓位参考: Max Pain 215 ｜ Call Wall 225（+2.1%，弱）（OI 10.7k） ｜ Put Wall 205（-7.0%，弱）（OI 3.3k）
量化解读： 存量 Call 重｜ATM IV 25.9%｜历史 Rank 23%（近端代理）｜IV/RV 0.69×（近似）｜净 delta 敞口 正 229,817 股

📆 09-25 Forward Structure
存量OI: C 287.3k / P 224.3k，今日变化ΔOI: C +42.8k / P +52.3k，平值价格ATM: C $3.55 / P $3.35 ｜ ATM IV 27.7%，净 delta 敞口 205k shares
Top ΔOI: C 222 +18,572 ｜ C 220 -16,846
仓位参考: Max Pain 218 ｜ Call Wall 225（+2.1%，弱）（OI 31.1k） ｜ Put Wall 210（-4.7%，弱）（OI 27.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 27.7%｜历史 Rank 23%（近端代理）｜IV/RV 0.74×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 204,670 股

📆 09-28 Forward Structure
存量OI: C 16.5k / P 12.6k，今日变化ΔOI: C +2.6k / P +2.0k，平值价格ATM: C $4.05 / P $3.75 ｜ ATM IV 26.5%，净 delta 敞口 34k shares
Top ΔOI: C 225 +775 ｜ C 222 +765 ｜ C 230 +427
仓位参考: Max Pain 215 ｜ Call Wall 225（+2.1%）（OI 4.3k） ｜ Put Wall 205（-7.0%，弱）（OI 2.6k）
量化解读： 存量 Call 重｜ATM IV 26.5%｜历史 Rank 23%（近端代理）｜IV/RV 0.71×（近似）｜净 delta 敞口 正 33,573 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/NVDA_morning.json