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
🟡 **近现价集中开仓**: 12-04 85C ΔOI +2,936（距现价 -0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 79.92 → 收盘 85.36（+6.8%） ｜ 今日高 85.44 ｜ 低 77.10 ｜ 昨收 73.61 → 收盘 85.36（+16.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.73 | OI比 0.35 | ATM IV 113.5% | Skew 5.7pp | Term 0.98 | ExpMove ±14.3%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构正常（Term 0.98）｜保护溢价中性（Skew 5.7pp）｜存量 Call 偏重（OI比 0.35）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.35×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 12-04（7D）±14.3% ｜ 12-11（14D）±16.0% ｜ 12-18（21D）±22.0% ｜ 12-24（27D）±24.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,292,282 | GEX Change vs 上次快照 -6,834,064 | Flip: Primary Flip: 93.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 1070 / LOW 731 / INVALID 4231
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 93.33（全链重定价，覆盖 86%）
最近结构参考: Flip 93（现价低于该位 8.5%）
量化视角： 负 Gamma（1029万，无历史分位）｜负 Gamma 加深（683万）｜现价位于 Flip 下方 8.54%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 93（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

12-04  C +16.2k / P +6.8k ｜ Activity HIGH ｜ 7D
12-11  C +6.0k / P -0.3k ｜ Activity HIGH ｜ 14D
12-18  C +2.6k / P -13.7k ｜ Activity HIGH ｜ 21D
12-24  C +2.2k / P +0.4k ｜ Activity HIGH ｜ 27D

📆 12-04 Forward Structure
存量OI: C 147.7k / P 71.5k，今日变化ΔOI: C +16.2k / P +6.8k，平值价格ATM: C $6.55 / P $5.70 ｜ ATM IV 124.1%，净 delta 敞口 1.4M shares
Top ΔOI: C 85 +2,936 ｜ C 75 +2,910 ｜ P 73 +2,122
仓位参考: Max Pain 90 ｜ Call Wall 85（-0.4%，弱）（OI 5.6k） ｜ Put Wall 87.5（+2.5%，弱）（OI 3.6k）
量化解读： 存量 Call 重｜ATM IV 124.1%｜历史 Rank 69%（近端代理）｜IV/RV 0.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,383,617 股

📆 12-11 Forward Structure
存量OI: C 67.0k / P 43.7k，今日变化ΔOI: C +6.0k / P -0.3k，平值价格ATM: C $5.84 / P $7.80 ｜ ATM IV 119.8%，净 delta 敞口 477k shares
Top ΔOI: C 70 +1,729 ｜ C 85 +1,187 ｜ C 113 +727
仓位参考: Max Pain 97 ｜ Call Wall 80（-6.3%，弱）（OI 2.8k） ｜ Put Wall 80（-6.3%）（OI 10.4k）
量化解读： 存量 Call 重｜ATM IV 119.8%｜历史 Rank 69%（近端代理）｜IV/RV 0.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 476,918 股

📆 12-18 Forward Structure
存量OI: C 574.5k / P 503.1k，今日变化ΔOI: C +2.6k / P -13.7k，平值价格ATM: C $9.60 / P $9.20 ｜ ATM IV 115.6%，净 delta 敞口 1.8M shares
Top ΔOI: P 60 +5,411 ｜ P 150 -4,975 ｜ P 70 -4,364
仓位参考: Max Pain 108 ｜ Call Wall 90（+5.4%，弱）（OI 5.1k） ｜ Put Wall 87.5（+2.5%，弱）（OI 23.5k）
量化解读： 存量两侧均衡｜ATM IV 115.6%｜历史 Rank 69%（近端代理）｜IV/RV 0.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,806,036 股

📆 12-24 Forward Structure
存量OI: C 31.8k / P 27.5k，今日变化ΔOI: C +2.2k / P +0.4k，平值价格ATM: C $10.60 / P $10.20 ｜ ATM IV 111.0%，净 delta 敞口 101k shares
Top ΔOI: C 122 +868 ｜ P 60 +306
仓位参考: Max Pain 111 ｜ Put Wall 87.5（+2.5%，弱）（OI 1.8k）
量化解读： 存量两侧均衡｜ATM IV 111.0%｜历史 Rank 69%（近端代理）｜IV/RV 0.14×（近似）｜净 delta 敞口 正 100,865 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/SNDK_evening.json