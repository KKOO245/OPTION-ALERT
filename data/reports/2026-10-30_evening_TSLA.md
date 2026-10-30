# 期权晚报 2026-10-30（快照 16:40 ET）

📊 市场环境

SPY $755.72 ｜ QQQ $690.49
VIX 19.42 ↑12.9%（5D -0.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-02 402C ΔOI +1,003（距现价 +0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 393.04 → 收盘 399.81（+1.7%） ｜ 今日高 404.19 ｜ 低 387.52 ｜ 昨收 403.30 → 收盘 399.81（-0.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.01 | OI比 1.22 | ATM IV 26.8% | Skew -4.9pp | Term 1.54 | ExpMove ±2.4%（近端） | Rank 2%
量化视角： IV 历史低位（Rank 2%，期权偏便宜）｜期限结构正常偏陡（Term 1.54）｜Put 保护异常便宜（Skew -4.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.01×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.22×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-02（3D）±2.4% ｜ 11-04（5D）±4.3% ｜ 11-06（7D）±5.3% ｜ 11-09（10D）±5.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 93,611,162 | GEX Change vs 上次快照 4,262,777 | Flip: Primary Flip: 374.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 1239 / LOW 109 / INVALID 998
结构观察区: Primary Flip 374.41（全链重定价，覆盖 84%）
Call Wall 420（弱结构｜现价低于该位 4.8%）
最近结构参考: Call Wall 420（现价低于该位 4.8%）
量化视角： 正 Gamma（9361万，无历史分位）｜正 Gamma 增强（+426万）｜现价位于 Flip 上方 6.78%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 388（MaxPain，仅结算参考）；上方 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 374（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-02  C +10.8k / P +5.8k ｜ Activity HIGH ｜ 3D
11-04  C +2.8k / P +3.0k ｜ Activity HIGH ｜ 5D
11-06  C +21.5k / P +22.3k ｜ Activity HIGH ｜ 7D
11-09  C +1.4k / P +1.4k ｜ Activity HIGH ｜ 10D

📆 11-02 Forward Structure
存量OI: C 60.4k / P 27.5k，今日变化ΔOI: C +10.8k / P +5.8k，平值价格ATM: C $4.70 / P $4.77 ｜ ATM IV 32.6%，净 delta 敞口 9k shares
Top ΔOI: C 455 +4,955 ｜ C 402 +1,003
仓位参考: Max Pain 395 ｜ Call Wall 410（+2.5%，弱）（OI 3.3k） ｜ Put Wall 400（+0.0%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 32.6%｜历史 Rank 2%（近端代理）｜IV/RV 0.98×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 8,509 股

📆 11-04 Forward Structure
存量OI: C 13.9k / P 12.9k，今日变化ΔOI: C +2.8k / P +3.0k，平值价格ATM: C $8.65 / P $8.70 ｜ ATM IV 46.8%，净 delta 敞口 -41k shares
Top ΔOI: P 402 +1,038 ｜ P 370 +552
仓位参考: Max Pain 400 ｜ Call Wall 410（+2.5%，弱）（OI 1.6k） ｜ Put Wall 400（+0.0%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 46.8%｜历史 Rank 2%（近端代理）｜IV/RV 1.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 40,927 股

📆 11-06 Forward Structure
存量OI: C 82.7k / P 103.5k，今日变化ΔOI: C +21.5k / P +22.3k，平值价格ATM: C $10.60 / P $10.44 ｜ ATM IV 47.1%，净 delta 敞口 240k shares
Top ΔOI: C 425 +4,576 ｜ C 412 +4,159
仓位参考: Max Pain 390 ｜ Call Wall 425（+6.3%，弱）（OI 7.2k） ｜ Put Wall 400（+0.0%，弱）（OI 4.3k）
量化解读： 存量 Put 重｜ATM IV 47.1%｜历史 Rank 2%（近端代理）｜IV/RV 1.42×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 240,443 股

📆 11-09 Forward Structure
存量OI: C 3.0k / P 4.1k，今日变化ΔOI: C +1.4k / P +1.4k，平值价格ATM: C $11.45 / P $11.95 ｜ ATM IV 43.0%，净 delta 敞口 178 shares
Top ΔOI: C 420 +693 ｜ P 380 +595 ｜ P 405 +240
仓位参考: Max Pain 400 ｜ Call Wall 420（+5.0%）（OI 0.8k） ｜ Put Wall 380（-5.0%）（OI 1.0k）
量化解读： 存量 Put 重｜ATM IV 43.0%｜历史 Rank 2%（近端代理）｜IV/RV 1.29×（近似）｜净 delta 敞口 正 178 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/TSLA_evening.json