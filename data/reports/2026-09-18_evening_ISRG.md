# 期权晚报 2026-09-18（快照 16:40 ET）

📊 市场环境

SPY $761.69 ｜ QQQ $nan
VIX 14.81 ↓4.1%（5D -6.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 29.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔵 **Flip 状态**: CONDITIONAL（Candidates: 376.5）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 381.84 → 收盘 393.33（+3.0%） ｜ 今日高 394.59 ｜ 低 379.50 ｜ 昨收 383.54 → 收盘 393.33（+2.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.21 | OI比 0.92 | ATM IV 49.1% | Skew 17.4pp | Term 0.71 | ExpMove ±3.5%（近端） | Rank 77%
量化视角： IV 历史高位（Rank 77%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜保护溢价显著（Skew 17.4pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.21×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（7D）±3.5% ｜ 10-02（14D）±2.7% ｜ 10-09（21D）±6.3% ｜ 10-16（28D）±7.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,454,094 | GEX Change vs 上次快照 1,360,132 | Flip: Candidates 376.50 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 68%（带内） ｜ IV 有效性: VALID 238 / LOW 150 / INVALID 588
结构观察区: ≈377（全链重定价，覆盖 68%，CONDITIONAL）
Call Wall 400（弱结构｜现价低于该位 1.7%）
最近结构参考: Call Wall 400（现价低于该位 1.7%）
量化视角： 正 Gamma（245万，无历史分位）｜正 Gamma 增强（+136万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 372（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 377（全链重定价，覆盖 68%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +53 / P +0.1k ｜ Activity HIGH ｜ 7D
10-02  C +56 / P +2 ｜ Activity HIGH ｜ 14D
10-09  C +5 / P -2 ｜ Activity LOW ｜ 21D
10-16  C +0.2k / P +54 ｜ Activity MEDIUM △ ｜ 28D

📆 09-25 Forward Structure
存量OI: C 1.7k / P 0.9k，今日变化ΔOI: C +53 / P +0.1k，平值价格ATM: C $7.13 / P $6.80 ｜ ATM IV 31.9%，净 delta 敞口 2k shares
Top ΔOI: P 360 +51 ｜ C 400 +27
仓位参考: Max Pain 370 ｜ Call Wall 430（+9.3%，弱）（OI 0.3k） ｜ Put Wall 360（-8.5%）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 31.9%｜历史 Rank 77%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,998 股

📆 10-02 Forward Structure
存量OI: C 0.6k / P 2.8k，今日变化ΔOI: C +56 / P +2，平值价格ATM: C $10.60 / P $0.00 ｜ ATM IV 31.4%，净 delta 敞口 2k shares
Top ΔOI: C 407 +24 ｜ C 420 +20 ｜ C 380 +4
仓位参考: Max Pain 365 ｜ Call Wall 405（+3.0%，弱）（OI 79）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 31.4%｜历史 Rank 77%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,614 股

10-09（Activity LOW）仓位参考: Max Pain 380 ｜ Call Wall 380（-3.4%）（OI 0.1k） ｜ Put Wall 385（-2.1%）（OI 0.2k）

10-16（MEDIUM △）Top ΔOI: 370C +50 ｜ 400C +37
10-16（MEDIUM △）仓位参考: Max Pain 385 ｜ Call Wall 400（+1.7%，弱）（OI 0.5k） ｜ Put Wall 380（-3.4%，弱）（OI 0.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/ISRG_evening.json