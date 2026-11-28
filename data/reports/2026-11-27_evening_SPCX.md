# 期权晚报 2026-11-27（快照 21:00 ET）

📊 市场环境

SPY $728.32 ｜ QQQ $650.99
VIX 23.81 ↓11.2%（5D -33.7%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 131.20 → 收盘 133.59（+1.8%） ｜ 今日高 134.44 ｜ 低 129.10 ｜ 昨收 127.44 → 收盘 133.59（+4.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.50 | OI比 1.13 | ATM IV 46.0% | Skew 5.3pp | Term 1.23 | ExpMove ±3.4%（近端） | Rank 13%
量化视角： IV 历史低位（Rank 13%，期权偏便宜）｜期限结构正常偏陡（Term 1.23）｜保护溢价中性（Skew 5.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.13×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-30（3D）±3.4% ｜ 12-02（5D）±5.4% ｜ 12-04（7D）±7.1% ｜ 12-07（10D）±13.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 16,266,561 | GEX Change vs 上次快照 -14,518,038 | Flip: Primary Flip: 130.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 756 / LOW 139 / INVALID 823
结构观察区: Primary Flip 130.52（全链重定价，覆盖 100%）
最近结构参考: Flip 131（现价高于该位 2.4%）
量化视角： 正 Gamma（1627万，无历史分位）｜正 Gamma 减弱（1452万）｜现价位于 Flip 上方 2.35%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 125（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 131（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-30  C +0 / P +0 ｜ Activity LOW ｜ 3D
12-02  C +0 / P +0 ｜ Activity LOW ｜ 5D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 7D
12-07  C +0 / P +0 ｜ Activity LOW ｜ 10D

📆 11-30 Forward Structure
存量OI: C 38.1k / P 43.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.05 / P $2.55 ｜ ATM IV 46.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 125 ｜ Call Wall 140（+4.8%）（OI 6.6k）
量化解读： 存量两侧均衡｜ATM IV 46.1%｜历史 Rank 13%（近端代理）｜IV/RV 0.74×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

12-02（Activity LOW）仓位参考: Max Pain 125 ｜ Call Wall 135（+1.1%，弱）（OI 1.8k） ｜ Put Wall 125（-6.4%，弱）（OI 0.4k）

12-04（Activity LOW）仓位参考: Max Pain 135 ｜ Call Wall 137（+2.6%，弱）（OI 10.5k） ｜ Put Wall 140（+4.8%，弱）（OI 11.7k）

12-07（Activity LOW）仓位参考: Max Pain 125 ｜ Call Wall 140（+4.8%）（OI 0.7k） ｜ Put Wall 130（-2.7%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/SPCX_evening.json