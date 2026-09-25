# 期权晚报 2026-09-25（快照 16:40 ET）

📊 市场环境

SPY $771.35 ｜ QQQ $744.50
VIX 14.87 ↓5.1%（5D +0.4%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 0 ｜ 前值 0.9　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 17.15 → 收盘 16.99（-0.9%） ｜ 今日高 17.42 ｜ 低 16.77 ｜ 昨收 17.02 → 收盘 16.99（-0.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.39 | OI比 0.51 | ATM IV 114.4% | Skew 16.4pp | Term 0.61 | ExpMove ±8.7%（近端） | Rank 59%
量化视角： IV 中性（Rank 59%）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜保护溢价显著（Skew 16.4pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.51）+ 当日成交偏 Put（P/C量 1.39）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.39×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±8.7% ｜ 10-09（14D）±10.8% ｜ 10-16（21D）±14.4% ｜ 10-23（28D）±18.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,822,770 | GEX Change vs 上次快照 638,201 | Flip: Primary Flip: 14.73（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 168 / LOW 90 / INVALID 198
结构观察区: Primary Flip 14.73（全链重定价，覆盖 84%）
Put Wall 17（弱结构｜现价低于该位 0.1%）
最近结构参考: Put Wall 17（现价低于该位 0.1%）
量化视角： 正 Gamma（182万，无历史分位）｜正 Gamma 增强（+64万）｜现价位于 Flip 上方 15.35%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 17（Put Wall，弱结构） / 17（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 15（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 7D
10-09  C +86 / P +0.2k ｜ Activity MEDIUM △ ｜ 14D
10-16  C +0.1k / P -77 ｜ Activity LOW ｜ 21D
10-23  C +7 / P +0.1k ｜ Activity MEDIUM △ ｜ 28D

📆 10-02 Forward Structure
存量OI: C 4.2k / P 1.5k，今日变化ΔOI: C +0.2k / P +0.3k，平值价格ATM: C $0.79 / P $0.68 ｜ ATM IV 68.0%，净 delta 敞口 -5k shares
Top ΔOI: C 18 +127 ｜ P 17 +102 ｜ P 15 +68
仓位参考: Max Pain 18 ｜ Call Wall 18（+5.9%，弱）（OI 0.5k） ｜ Put Wall 16（-5.8%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 68.0%｜历史 Rank 59%（近端代理）｜IV/RV 0.93×（近似）｜净 delta 敞口 负 5,049 股

10-09（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 16（-5.8%，弱）（OI 0.1k）

10-16（Activity LOW）仓位参考: Max Pain 20 ｜ Put Wall 17（+0.1%，弱）（OI 0.7k）

10-23（MEDIUM △）Top ΔOI: 17P +35 ｜ 18P +18
10-23（MEDIUM △）仓位参考: Max Pain 18 ｜ Call Wall 18（+5.9%，弱）（OI 75） ｜ Put Wall 15.5（-8.8%）（OI 95）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/NNE_evening.json