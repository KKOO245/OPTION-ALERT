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


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 77.12 → 收盘 79.18（+2.7%） ｜ 今日高 79.23 ｜ 低 76.52 ｜ 昨收 73.89 → 收盘 79.18（+7.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.15 | OI比 0.62 | ATM IV 41.8% | Skew 4.7pp | Term 1.18 | ExpMove ±4.4%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构正常偏陡（Term 1.18）｜保护溢价中性（Skew 4.7pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.15×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-30（3D）±4.4% ｜ 12-02（5D）±2.0% ｜ 12-04（7D）±5.9% ｜ 12-07（10D）±6.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,074,414 | GEX Change vs 上次快照 -15,355,280 | Flip: Primary Flip: 76.99（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 486 / LOW 145 / INVALID 515
结构观察区: Primary Flip 76.99（全链重定价，覆盖 99%）
Put Wall 75（弱结构｜现价高于该位 5.6%）
最近结构参考: Flip 77（现价高于该位 2.8%）
量化视角： 正 Gamma（1407万，无历史分位）｜正 Gamma 减弱（1536万）｜现价位于 Flip 上方 2.84%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 75（Put Wall，弱结构） / 71（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 77（全链重定价，覆盖 99%）。
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
存量OI: C 4.5k / P 2.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.03 / P $2.48 ｜ ATM IV 41.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 71 ｜ Call Wall 80（+1.0%）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 41.8%｜历史 Rank 60%（近端代理）｜IV/RV 0.67×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

12-02（Activity LOW）仓位参考: Max Pain 73 ｜ Call Wall 75（-5.3%）（OI 0.3k）

12-04（Activity LOW）仓位参考: Max Pain 76 ｜ Call Wall 76（-4.0%，弱）（OI 20.6k） ｜ Put Wall 75（-5.3%，弱）（OI 1.4k）

12-07（Activity LOW）仓位参考: Max Pain 72 ｜ Call Wall 77（-2.8%）（OI 0.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/GDX_evening.json