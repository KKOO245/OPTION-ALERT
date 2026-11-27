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
🟡 **近现价集中开仓**: 12-04 170C ΔOI +7,866（距现价 -1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-04 95P ΔOI +12,070 占该期限总 OI 11.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 157.4）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 169.76 → 收盘 172.17（+1.4%） ｜ 今日高 173.22 ｜ 低 164.80 ｜ 昨收 163.59 → 收盘 172.17（+5.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.25 | OI比 0.61 | ATM IV 52.8% | Skew 7.8pp | Term 1.03 | ExpMove ±6.6%（近端） | Rank 44%
量化视角： IV 中性（Rank 44%）｜期限结构正常（Term 1.03）｜保护溢价显著（Skew 7.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.61）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.25×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.61×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 12-04（7D）±6.6% ｜ 12-11（14D）±8.9% ｜ 12-18（21D）±10.9% ｜ 12-24（27D）±11.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 41,331,704 | GEX Change vs 上次快照 -4,878,270 | Flip: Candidates 157.42 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 78%（带内） ｜ IV 有效性: VALID 397 / LOW 143 / INVALID 418
结构观察区: ≈157（全链重定价，覆盖 78%，CONDITIONAL）
Call Wall 175（弱结构｜现价低于该位 1.6%）
最近结构参考: Call Wall 175（现价低于该位 1.6%）
量化视角： 正 Gamma（4133万，无历史分位）｜正 Gamma 减弱（488万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 152（MaxPain，仅结算参考）；上方 175（Call Wall，弱结构）。
• Gamma 区域：切换参考 157（全链重定价，覆盖 78%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

12-04  C +18.9k / P +21.7k ｜ Activity HIGH ｜ 7D
12-11  C +0.5k / P +1.2k ｜ Activity HIGH ｜ 14D
12-18  C +0.6k / P -0.4k ｜ Activity MEDIUM △ ｜ 21D
12-24  C +0.3k / P +20 ｜ Activity MEDIUM △ ｜ 27D

📆 12-04 Forward Structure
存量OI: C 54.3k / P 48.0k，今日变化ΔOI: C +18.9k / P +21.7k，平值价格ATM: C $5.85 / P $5.55 ｜ ATM IV 57.6%，净 delta 敞口 931k shares
Top ΔOI: C 170 +7,866 ｜ C 175 +7,547
仓位参考: Max Pain 160 ｜ Call Wall 175（+1.6%，弱）（OI 9.4k） ｜ Put Wall 155（-10.0%，弱）（OI 3.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 57.6%｜历史 Rank 44%（近端代理）｜IV/RV 0.85×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 931,045 股

📆 12-11 Forward Structure
存量OI: C 13.9k / P 16.3k，今日变化ΔOI: C +0.5k / P +1.2k，平值价格ATM: C $7.45 / P $7.95 ｜ ATM IV 56.4%，净 delta 敞口 18k shares
Top ΔOI: C 180 -317
仓位参考: Max Pain 160 ｜ Call Wall 175（+1.6%，弱）（OI 1.3k） ｜ Put Wall 160（-7.1%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 56.4%｜历史 Rank 44%（近端代理）｜IV/RV 0.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 17,705 股

12-18（MEDIUM △）Top ΔOI: 190C +938
12-18（MEDIUM △）仓位参考: Max Pain 140 ｜ Call Wall 185（+7.5%，弱）（OI 16.0k） ｜ Put Wall 160（-7.1%，弱）（OI 18.5k）

12-24（MEDIUM △）Top ΔOI: 180C +88 ｜ 185C +42
12-24（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 180（+4.5%，弱）（OI 0.7k） ｜ Put Wall 155（-10.0%，弱）（OI 0.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/PLTR_evening.json