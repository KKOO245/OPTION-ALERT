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
🟡 **近现价集中开仓**: 10-26 283C ΔOI +10,088（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-26 283C ΔOI +10,088 占该期限总 OI 11.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 274.85 → 收盘 275.75（+0.3%） ｜ 今日高 276.24 ｜ 低 273.35 ｜ 昨收 276.67 → 收盘 275.75（-0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.38 | OI比 1.37 | ATM IV 16.0% | Skew 6.5pp | Term 1.28 | ExpMove ±1.0%（近端） | Rank — (历史不足)
量化视角： 期限结构正常偏陡（Term 1.28）｜保护溢价显著（Skew 6.5pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.38）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.38×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.37×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-26（3D）±1.0% ｜ 10-27（4D）±1.4% ｜ 10-28（5D）±1.9% ｜ 10-29（6D）±2.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -545,818,824 | GEX Change vs 上次快照 87,352,833 | Flip: Primary Flip: 282.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 1199 / LOW 208 / INVALID 1293
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 282.25（全链重定价，覆盖 94%）
Put Wall 270（弱结构｜现价高于该位 2.1%） | Call Wall 280（弱结构｜现价低于该位 1.5%）
最近结构参考: Call Wall 280（现价低于该位 1.5%）
量化视角： 负 Gamma（5.46亿，无历史分位）｜负 Gamma 缓解（+8735万）｜现价位于 Flip 下方 2.30%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构）；上方 277（MaxPain，仅结算参考） / 280（Call Wall，弱结构）。
• Gamma 区域：切换参考 282（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-26  C +16.3k / P +13.6k ｜ Activity HIGH ｜ 3D
10-27  C +1.7k / P +3.4k ｜ Activity HIGH ｜ 4D
10-28  C +1.4k / P +4.8k ｜ Activity HIGH ｜ 5D
10-29  C +2.0k / P +4.9k ｜ Activity HIGH ｜ 6D

📆 10-26 Forward Structure
存量OI: C 43.1k / P 44.2k，今日变化ΔOI: C +16.3k / P +13.6k，平值价格ATM: C $1.33 / P $1.37 ｜ ATM IV 13.6%，净 delta 敞口 187k shares
Top ΔOI: C 283 +10,088 ｜ P 270 +2,014 ｜ P 263 +1,538
仓位参考: Max Pain 274 ｜ Call Wall 283（+2.6%）（OI 15.3k） ｜ Put Wall 269（-2.4%）（OI 5.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 13.6%｜期限正常（远月高于近端）｜净 delta 敞口 正 187,447 股

📆 10-27 Forward Structure
存量OI: C 20.4k / P 20.3k，今日变化ΔOI: C +1.7k / P +3.4k，平值价格ATM: C $1.82 / P $1.92 ｜ ATM IV 15.7%，净 delta 敞口 -26k shares
Top ΔOI: P 272 +1,585 ｜ C 280 +425 ｜ P 273 +399
仓位参考: Max Pain 274 ｜ Call Wall 284（+3.0%）（OI 4.3k） ｜ Put Wall 272（-1.4%，弱）（OI 2.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 15.7%｜期限正常（远月高于近端）｜净 delta 敞口 负 26,062 股

📆 10-28 Forward Structure
存量OI: C 10.6k / P 20.7k，今日变化ΔOI: C +1.4k / P +4.8k，平值价格ATM: C $2.59 / P $2.54 ｜ ATM IV 19.9%，净 delta 敞口 -24k shares
Top ΔOI: P 270 +1,015 ｜ P 260 +973 ｜ P 265 +653
仓位参考: Max Pain 275 ｜ Call Wall 275（-0.3%）（OI 2.8k） ｜ Put Wall 260（-5.7%，弱）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 19.9%｜期限正常（远月高于近端）｜净 delta 敞口 负 24,121 股

📆 10-29 Forward Structure
存量OI: C 44.0k / P 11.4k，今日变化ΔOI: C +2.0k / P +4.9k，平值价格ATM: C $2.91 / P $3.05 ｜ ATM IV 21.0%，净 delta 敞口 -73k shares
Top ΔOI: P 270 +699 ｜ C 282 +646 ｜ P 273 +613
仓位参考: Max Pain 276 ｜ Call Wall 280（+1.5%，弱）（OI 15.3k） ｜ Put Wall 267（-3.2%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 21.0%｜净 delta 敞口 负 73,188 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/IWM_evening.json