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

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 160C ΔOI +512（距现价 +0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 162.75 → 收盘 158.61（-2.5%） ｜ 今日高 162.75 ｜ 低 156.78 ｜ 昨收 161.61 → 收盘 158.61（-1.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.20 | OI比 0.75 | ATM IV 58.4% | Skew -21.0pp | Term 1.10 | ExpMove ±7.1%（近端） | Rank 11%
量化视角： IV 历史低位（Rank 11%，期权偏便宜）｜期限结构正常（Term 1.10）｜Put 保护异常便宜（Skew -21.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.20×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±7.1% ｜ 10-09（14D）±9.9% ｜ 10-16（21D）±12.3% ｜ 10-23（28D）±14.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 49,489,495 | GEX Change vs 上次快照 -25,143,768 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 74%（带内） ｜ IV 有效性: VALID 760 / LOW 67 / INVALID 317
结构观察区: NO_CROSS
量化视角： 正 Gamma（4949万，无历史分位）｜正 Gamma 减弱（2514万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 142（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +34.8k / P +12.0k ｜ Activity HIGH ｜ 7D
10-09  C +1.3k / P +3.2k ｜ Activity HIGH ｜ 14D
10-16  C +3.7k / P +0.6k ｜ Activity MEDIUM △ ｜ 21D
10-23  C +0.8k / P +2.0k ｜ Activity HIGH ｜ 28D

📆 10-02 Forward Structure
存量OI: C 98.8k / P 119.1k，今日变化ΔOI: C +34.8k / P +12.0k，平值价格ATM: C $6.30 / P $5.00 ｜ ATM IV 64.1%，净 delta 敞口 638k shares
Top ΔOI: C 167 +14,241 ｜ C 175 +9,263
仓位参考: Max Pain 155 ｜ Call Wall 167.5（+5.6%，弱）（OI 15.0k） ｜ Put Wall 150（-5.4%，弱）（OI 11.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 64.1%｜历史 Rank 11%（近端代理）｜IV/RV 0.65×（近似）｜净 delta 敞口 正 638,438 股

📆 10-09 Forward Structure
存量OI: C 31.4k / P 47.6k，今日变化ΔOI: C +1.3k / P +3.2k，平值价格ATM: C $8.60 / P $7.15 ｜ ATM IV 63.5%，净 delta 敞口 12k shares
Top ΔOI: C 160 +512
仓位参考: Max Pain 144 ｜ Call Wall 160（+0.9%，弱）（OI 5.6k） ｜ Put Wall 155（-2.3%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜ATM IV 63.5%｜历史 Rank 11%（近端代理）｜IV/RV 0.65×（近似）｜净 delta 敞口 正 12,133 股

10-16（MEDIUM △）Top ΔOI: 95C +2,059 ｜ 200C +607
10-16（MEDIUM △）仓位参考: Max Pain 120 ｜ Call Wall 155（-2.3%，弱）（OI 10.4k） ｜ Put Wall 160（+0.9%，弱）（OI 4.1k）

📆 10-23 Forward Structure
存量OI: C 13.4k / P 17.6k，今日变化ΔOI: C +0.8k / P +2.0k，平值价格ATM: C $12.30 / P $10.25 ｜ ATM IV 64.2%，净 delta 敞口 -36k shares
Top ΔOI: P 160 +306 ｜ P 165 +247
仓位参考: Max Pain 155 ｜ Call Wall 170（+7.2%，弱）（OI 1.0k） ｜ Put Wall 155（-2.3%，弱）（OI 1.5k）
量化解读： 存量 Put 重｜ATM IV 64.2%｜历史 Rank 11%（近端代理）｜IV/RV 0.65×（近似）｜净 delta 敞口 负 36,127 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/MSTR_evening.json