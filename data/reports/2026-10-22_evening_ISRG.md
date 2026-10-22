# 期权晚报 2026-10-22（快照 16:40 ET）

📊 市场环境

SPY $763.96 ｜ QQQ $704.47
VIX 19.03 ↑14.1%（5D +15.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 19.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 440C ΔOI +200（距现价 -0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 430.67 → 收盘 443.85（+3.1%） ｜ 今日高 444.15 ｜ 低 427.47 ｜ 昨收 428.12 → 收盘 443.85（+3.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.47 | OI比 0.98 | ATM IV 42.5% | Skew 14.4pp | Term 0.82 | ExpMove ±1.7%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价显著（Skew 14.4pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（1D）±1.7% ｜ 10-30（8D）±2.0% ｜ 11-06（15D）±2.9% ｜ 11-13（22D）±3.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,626,789 | GEX Change vs 上次快照 1,961,918 | Flip: Primary Flip: 425.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 83%（带内） ｜ IV 有效性: VALID 265 / LOW 220 / INVALID 481
结构观察区: Primary Flip 425.25（全链重定价，覆盖 83%）
Call Wall 475（弱结构｜现价低于该位 6.6%）
最近结构参考: Flip 425（现价高于该位 4.4%）
量化视角： 正 Gamma（563万，无历史分位）｜正 Gamma 增强（+196万）｜现价位于 Flip 上方 4.38%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 425（MaxPain，仅结算参考）；上方 475（Call Wall，弱结构）。
• Gamma 区域：切换参考 425（全链重定价，覆盖 83%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +0.1k / P -0.1k ｜ Activity MEDIUM △ ｜ 1D
10-30  C +0.1k / P +0.1k ｜ Activity HIGH ｜ 8D
11-06  C +0.3k / P +48 ｜ Activity MEDIUM △ ｜ 15D
11-13  C +0.2k / P +0.1k ｜ Activity HIGH ｜ 22D

📆 10-23 Forward Structure
存量OI: C 8.7k / P 8.5k，今日变化ΔOI: C +0.1k / P -0.1k，平值价格ATM: C $2.62 / P $5.00 ｜ ATM IV 42.5%，净 delta 敞口 23k shares
Top ΔOI: C 440 +200 ｜ C 460 +142 ｜ C 455 +126
仓位参考: Max Pain 425 ｜ Call Wall 475（+7.0%）（OI 1.2k） ｜ Put Wall 400（-9.9%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 42.5%｜历史 Rank 64%（近端代理）｜IV/RV 1.70×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 22,529 股

📆 10-30 Forward Structure
存量OI: C 1.9k / P 1.4k，今日变化ΔOI: C +0.1k / P +0.1k，平值价格ATM: C $9.00 / P $0.00 ｜ ATM IV 37.9%，净 delta 敞口 7k shares
Top ΔOI: C 470 -86 ｜ C 440 +54 ｜ C 450 +48
仓位参考: Max Pain 410 ｜ Call Wall 450（+1.4%，弱）（OI 0.2k） ｜ Put Wall 410（-7.6%，弱）（OI 93）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 37.9%｜历史 Rank 64%（近端代理）｜IV/RV 1.52×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 6,984 股

11-06（MEDIUM △）Top ΔOI: 430C +121 ｜ 440C +108
11-06（MEDIUM △）仓位参考: Max Pain 425 ｜ Call Wall 430（-3.1%，弱）（OI 0.1k） ｜ Put Wall 400（-9.9%，弱）（OI 77）

📆 11-13 Forward Structure
存量OI: C 0.5k / P 0.7k，今日变化ΔOI: C +0.2k / P +0.1k，平值价格ATM: C $13.60 / P $0.00 ｜ ATM IV 33.9%，净 delta 敞口 10k shares
Top ΔOI: C 435 +86 ｜ C 440 +53 ｜ C 430 +52
仓位参考: Max Pain 425 ｜ Call Wall 435（-2.0%）（OI 0.1k） ｜ Put Wall 420（-5.4%，弱）（OI 76）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 33.9%｜历史 Rank 64%（近端代理）｜IV/RV 1.36×（近似）｜净 delta 敞口 正 10,223 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/ISRG_evening.json