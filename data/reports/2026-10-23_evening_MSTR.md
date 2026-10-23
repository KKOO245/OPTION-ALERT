# 期权晚报 2026-10-23（快照 16:40 ET）

📊 市场环境

SPY $759.97 ｜ QQQ $704.40
VIX 19.45 ↑2.2%（5D -2.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 21.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 150C ΔOI +8,484（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 144.38 → 收盘 146.01（+1.1%） ｜ 今日高 152.21 ｜ 低 144.21 ｜ 昨收 145.80 → 收盘 146.01（+0.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.52 | OI比 0.83 | ATM IV 73.6% | Skew 13.1pp | Term 0.99 | ExpMove ±8.4%（近端） | Rank 35%
量化视角： IV 中性（Rank 35%）｜期限结构正常（Term 0.99）｜保护溢价显著（Skew 13.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（7D）±8.4% ｜ 11-06（14D）±11.7% ｜ 11-13（21D）±13.9% ｜ 11-20（28D）±17.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 71,349,989 | GEX Change vs 上次快照 1,183,289 | Flip: Primary Flip: 131.58（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 80%（带内） ｜ IV 有效性: VALID 555 / LOW 92 / INVALID 297
结构观察区: Primary Flip 131.58（全链重定价，覆盖 80%）
Call Wall 155（弱结构｜现价低于该位 5.8%）
最近结构参考: Call Wall 155（现价低于该位 5.8%）
量化视角： 正 Gamma（7135万，无历史分位）｜正 Gamma 增强（+118万）｜现价位于 Flip 上方 10.97%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 141（MaxPain，仅结算参考）；上方 155（Call Wall，弱结构）。
• Gamma 区域：切换参考 132（全链重定价，覆盖 80%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +26.0k / P +10.0k ｜ Activity HIGH ｜ 7D
11-06  C +1.3k / P +3.8k ｜ Activity HIGH ｜ 14D
11-13  C +0.5k / P +3.7k ｜ Activity HIGH ｜ 21D
11-20  C +1.6k / P +4.1k ｜ Activity HIGH ｜ 28D

📆 10-30 Forward Structure
存量OI: C 81.2k / P 106.0k，今日变化ΔOI: C +26.0k / P +10.0k，平值价格ATM: C $6.25 / P $6.09 ｜ ATM IV 76.3%，净 delta 敞口 663k shares
Top ΔOI: C 150 +8,484 ｜ C 152 +5,013 ｜ C 157 +4,665
仓位参考: Max Pain 150 ｜ Call Wall 150（+2.7%）（OI 10.8k） ｜ Put Wall 155（+6.2%，弱）（OI 4.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 76.3%｜历史 Rank 35%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 663,364 股

📆 11-06 Forward Structure
存量OI: C 18.0k / P 41.3k，今日变化ΔOI: C +1.3k / P +3.8k，平值价格ATM: C $9.08 / P $8.05 ｜ ATM IV 75.0%，净 delta 敞口 -5k shares
仓位参考: Max Pain 160 ｜ Call Wall 160（+9.6%）（OI 2.2k） ｜ Put Wall 160（+9.6%，弱）（OI 3.7k）
量化解读： 存量 Put 重｜ATM IV 75.0%｜历史 Rank 35%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 4,762 股

📆 11-13 Forward Structure
存量OI: C 14.5k / P 34.9k，今日变化ΔOI: C +0.5k / P +3.7k，平值价格ATM: C $10.55 / P $9.80 ｜ ATM IV 72.5%，净 delta 敞口 -47k shares
仓位参考: Max Pain 160 ｜ Call Wall 144（-1.4%，弱）（OI 0.8k） ｜ Put Wall 160（+9.6%，弱）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 72.5%｜历史 Rank 35%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 负 47,238 股

📆 11-20 Forward Structure
存量OI: C 142.5k / P 103.0k，今日变化ΔOI: C +1.6k / P +4.1k，平值价格ATM: C $13.72 / P $11.40 ｜ ATM IV 72.8%，净 delta 敞口 -42k shares
仓位参考: Max Pain 135 ｜ Call Wall 135（-7.5%）（OI 42.3k） ｜ Put Wall 160（+9.6%，弱）（OI 4.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 72.8%｜历史 Rank 35%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 负 41,973 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/MSTR_evening.json