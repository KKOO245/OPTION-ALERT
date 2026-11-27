# 期权晨报 2026-11-27（快照 10:20 ET）

📊 市场环境

SPY $722.09 ｜ QQQ $641.70
VIX 27.52 ↑2.7%（5D -23.3%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 22.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 8.85 → 今开 9.53（+7.6%） | 较昨收变动（含盘初走势） ｜ 今日高 9.60 ｜ 低 9.03

Options: P/C成交量 0.40 | OI比 0.15 | ATM IV 110.2% | Skew 17.0pp | Term 0.89 | ExpMove ±15.9%（近端） | Rank 59%
量化视角： IV 中性（Rank 59%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜保护溢价显著（Skew 17.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.15）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.40×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.15×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 12-04（7D）±15.9% ｜ 12-11（14D）±23.4% ｜ 12-18（21D）±0.0% ｜ 12-24（27D）±3.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -64,718 | GEX Change vs 上次快照 4,303 | Flip: Primary Flip: 10.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 102 / LOW 61 / INVALID 217
结构观察区: Primary Flip 10.07（全链重定价，覆盖 100%）
Put Wall 10（弱结构｜现价低于该位 6.7%）
最近结构参考: Put Wall 10（现价低于该位 6.7%）
量化视角： 负 Gamma（6万，无历史分位）｜负 Gamma 缓解（+0万）｜现价位于 Flip 下方 7.35%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（Put Wall，弱结构） / 12（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 10（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
🎯 今日到期（0DTE）
存量OI: C 5.1k / P 0.8k，今日成交量: C 0.3k / P 0.1k，平值价格ATM: C $0.72 / P $0.25 ｜ ATM IV 110.2%，预期波动 ±10.5%，Max Pain 12

📆 Forward Expiration Structure

12-04  C +0 / P +0 ｜ Activity LOW ｜ 7D
12-11  C +0 / P +0 ｜ Activity LOW ｜ 14D
12-18  C +0 / P +0 ｜ Activity LOW ｜ 21D
12-24  C +0 / P +0 ｜ Activity LOW ｜ 27D

📆 12-04 Forward Structure
存量OI: C 0.8k / P 0.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.05 / P $0.43 ｜ ATM IV 108.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 11 ｜ Put Wall 9.5（+1.8%）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 108.8%｜历史 Rank 59%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

12-11（Activity LOW）仓位参考: Max Pain 11 ｜ Call Wall 10（+7.2%，弱）（OI 34） ｜ Put Wall 9（-3.5%，弱）（OI 8）

12-18（Activity LOW）仓位参考: Max Pain 11 ｜ Call Wall 10（+7.2%，弱）（OI 65） ｜ Put Wall 9（-3.5%，弱）（OI 0.2k）

12-24（Activity LOW）仓位参考: Max Pain 12

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/NNE_morning.json