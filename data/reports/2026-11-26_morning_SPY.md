# 期权晨报 2026-11-26（快照 10:20 ET）

📊 市场环境

SPY $720.30 ｜ QQQ $633.93
VIX 26.96 ↓4.7%（5D -5.2%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-26

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 716.70 → 今开 703.20（-1.9%） | 较昨收变动（含盘初走势） ｜ 今日高 718.43 ｜ 低 695.45

Options: P/C成交量 1.06 | OI比 0.78 | ATM IV 23.1% | Skew 4.6pp | Term 0.88 | ExpMove ±0.0%（近端） | Rank 89%
量化视角： IV 历史高位（Rank 89%，期权偏贵）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价中性（Skew 4.6pp）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.06×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 39% ｜ P/C OI(近端) 0%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 39%）｜近端持仓极端 Call 重（P/C OI 分位 0%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-27（1D）±0.0% ｜ 11-30（4D）±2.0% ｜ 12-01（5D）±2.4% ｜ 12-02（6D）±2.6%
   ⇒ IV–VIX Spread: -3.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -770,103,286 | GEX Change vs 上次快照 166,593,716 | Flip: Primary Flip: 732.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 3098 / LOW 388 / INVALID 1790
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 732.88（全链重定价，覆盖 97%）
Put Wall 700（弱结构｜现价高于该位 2.9%）
最近结构参考: Flip 733（现价低于该位 1.7%）
量化视角： 负 Gamma（7.70亿，历史分位 39%，中性区）｜负 Gamma 缓解（+1.67亿）｜现价位于 Flip 下方 1.72%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 721（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 733（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +0 / P +0 ｜ Activity LOW ｜ 1D
11-30  C +0 / P +0 ｜ Activity LOW ｜ 4D
12-01  C +0 / P +0 ｜ Activity LOW ｜ 5D
12-02  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 11-27 Forward Structure
存量OI: C 477.7k / P 372.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 23.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 721 ｜ Call Wall 735（+2.0%，弱）（OI 26.4k） ｜ Put Wall 700（-2.8%，弱）（OI 35.1k）
量化解读： 存量 Call 重｜ATM IV 23.2%｜历史 Rank 89%（近端代理）｜IV/RV 0.74×（近似）｜净 delta 敞口 正 0 股

11-30（Activity LOW）仓位参考: Max Pain 730 ｜ Call Wall 740（+2.7%，弱）（OI 11.2k） ｜ Put Wall 700（-2.8%，弱）（OI 30.3k）

12-01（Activity LOW）仓位参考: Max Pain 720 ｜ Call Wall 725（+0.7%，弱）（OI 1.4k） ｜ Put Wall 703（-2.4%，弱）（OI 4.0k）

12-02（Activity LOW）仓位参考: Max Pain 715 ｜ Call Wall 717（-0.5%，弱）（OI 1.5k） ｜ Put Wall 700（-2.8%，弱）（OI 9.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-26/SPY_morning.json