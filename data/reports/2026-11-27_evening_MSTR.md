# 期权晚报 2026-11-27（快照 16:40 ET）

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

🔍 重点速览
🟡 **近现价集中开仓**: 12-04 82C ΔOI +12,892（距现价 +0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 76.3）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 84.57 → 收盘 81.62（-3.5%） ｜ 今日高 84.67 ｜ 低 78.84 ｜ 昨收 79.96 → 收盘 81.62（+2.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.66 | OI比 0.62 | ATM IV 92.8% | Skew -22.5pp | Term 1.05 | ExpMove ±11.8%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构正常（Term 1.05）｜Put 保护异常便宜（Skew -22.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 12-04（7D）±11.8% ｜ 12-11（14D）±16.5% ｜ 12-18（21D）±19.5% ｜ 12-24（27D）±20.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 11,282,685 | GEX Change vs 上次快照 -7,752,383 | Flip: Candidates 76.25 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 76%（带内） ｜ IV 有效性: VALID 513 / LOW 130 / INVALID 485
结构观察区: ≈76（全链重定价，覆盖 76%，CONDITIONAL）
Call Wall 85（弱结构｜现价低于该位 4.0%）
最近结构参考: Call Wall 85（现价低于该位 4.0%）
量化视角： 正 Gamma（1128万，无历史分位）｜正 Gamma 减弱（775万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 84（MaxPain，仅结算参考） / 85（Call Wall，弱结构）。
• Gamma 区域：切换参考 76（全链重定价，覆盖 76%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

12-04  C +79.6k / P +45.6k ｜ Activity HIGH ｜ 7D
12-11  C +4.5k / P +8.3k ｜ Activity HIGH ｜ 14D
12-18  C +12.3k / P +8.7k ｜ Activity HIGH ｜ 21D
12-24  C +0.5k / P +2.1k ｜ Activity HIGH ｜ 27D

📆 12-04 Forward Structure
存量OI: C 140.0k / P 124.4k，今日变化ΔOI: C +79.6k / P +45.6k，平值价格ATM: C $4.65 / P $4.95 ｜ ATM IV 105.6%，净 delta 敞口 2.9M shares
Top ΔOI: P 40 +17,511 ｜ C 82 +12,892 ｜ C 87 +12,490
仓位参考: Max Pain 82 ｜ Call Wall 87（+6.6%，弱）（OI 13.2k） ｜ Put Wall 80（-2.0%，弱）（OI 8.4k）
量化解读： 存量两侧均衡｜ATM IV 105.6%｜历史 Rank 69%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,901,292 股

📆 12-11 Forward Structure
存量OI: C 17.9k / P 47.9k，今日变化ΔOI: C +4.5k / P +8.3k，平值价格ATM: C $6.55 / P $6.90 ｜ ATM IV 102.8%，净 delta 敞口 143k shares
Top ΔOI: P 65 +2,414 ｜ P 60 +1,771 ｜ P 70 +1,343
仓位参考: Max Pain 90 ｜ Call Wall 80（-2.0%，弱）（OI 0.6k） ｜ Put Wall 80（-2.0%，弱）（OI 3.6k）
量化解读： 存量 Put 重｜ATM IV 102.8%｜历史 Rank 69%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 143,437 股

📆 12-18 Forward Structure
存量OI: C 259.4k / P 179.5k，今日变化ΔOI: C +12.3k / P +8.7k，平值价格ATM: C $7.65 / P $8.30 ｜ ATM IV 98.4%，净 delta 敞口 492k shares
Top ΔOI: P 30 +5,296 ｜ C 100 +4,077 ｜ C 90 +2,713
仓位参考: Max Pain 105 ｜ Call Wall 85（+4.1%，弱）（OI 9.6k） ｜ Put Wall 80（-2.0%，弱）（OI 9.1k）
量化解读： 存量 Call 重｜ATM IV 98.4%｜历史 Rank 69%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 491,540 股

📆 12-24 Forward Structure
存量OI: C 8.4k / P 13.3k，今日变化ΔOI: C +0.5k / P +2.1k，平值价格ATM: C $9.17 / P $7.60 ｜ ATM IV 97.4%，净 delta 敞口 23k shares
Top ΔOI: P 55 +689
仓位参考: Max Pain 110 ｜ Call Wall 85（+4.1%，弱）（OI 0.4k） ｜ Put Wall 80（-2.0%，弱）（OI 1.1k）
量化解读： 存量 Put 重｜ATM IV 97.4%｜历史 Rank 69%（近端代理）｜IV/RV 1.22×（近似）｜净 delta 敞口 正 23,403 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/MSTR_evening.json