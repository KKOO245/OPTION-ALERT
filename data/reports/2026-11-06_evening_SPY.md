# 期权晚报 2026-11-06（快照 21:00 ET）

📊 市场环境

SPY $735.29 ｜ QQQ $656.10
VIX 25.64 ↓9.0%（5D +32.0%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 22.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 165 ｜ 前值 60　✅ 今日已公布
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 4.1 ｜ 前值 4.2　✅ 今日已公布
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 51 ｜ 前值 46.3　✅ 今日已公布

🔍 重点速览
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 734.82 → 收盘 735.29（+0.1%） ｜ 今日高 742.21 ｜ 低 734.58 ｜ 昨收 733.00 → 收盘 735.29（+0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.25 | OI比 1.88 | ATM IV 17.8% | Skew 4.4pp | Term 1.14 | ExpMove ±1.3%（近端） | Rank 77%
量化视角： IV 历史高位（Rank 77%，期权偏贵）｜期限结构正常（Term 1.14）｜保护溢价中性（Skew 4.4pp）｜当日成交偏 Put（P/C量 1.25）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.25×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.88×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 25% ｜ P/C OI(近端) 53%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 25%）｜近端持仓结构中性（P/C OI 分位 53%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-09（3D）±1.3% ｜ 11-10（4D）±1.8% ｜ 11-11（5D）±2.1% ｜ 11-12（6D）±2.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,455,301,697 | GEX Change vs 上次快照 -211,921,944 | Flip: Primary Flip: 761.51（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 2958 / LOW 255 / INVALID 1219
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 761.51（全链重定价，覆盖 98%）
最近结构参考: Flip 762（现价低于该位 3.4%）
量化视角： 负 Gamma（14.55亿，历史分位偏负区，比 75% 的交易日更负）｜负 Gamma 加深（2.12亿）｜现价位于 Flip 下方 3.44%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 747（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 762（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-09  C +0 / P +0 ｜ Activity LOW ｜ 3D
11-10  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-11  C +0 / P +0 ｜ Activity LOW ｜ 5D
11-12  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 11-09 Forward Structure
存量OI: C 111.3k / P 208.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.26 / P $4.25 ｜ ATM IV 17.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 747 ｜ Call Wall 750（+2.0%，弱）（OI 5.1k） ｜ Put Wall 725（-1.4%，弱）（OI 35.8k）
量化解读： 存量 Put 重｜ATM IV 17.8%｜历史 Rank 77%（近端代理）｜IV/RV 0.89×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

11-10（Activity LOW）仓位参考: Max Pain 741 ｜ Call Wall 740（+0.6%，弱）（OI 11.3k） ｜ Put Wall 734（-0.2%）（OI 9.9k）

11-11（Activity LOW）仓位参考: Max Pain 750 ｜ Call Wall 738（+0.4%，弱）（OI 1.8k） ｜ Put Wall 720（-2.1%，弱）（OI 6.8k）

11-12（Activity LOW）仓位参考: Max Pain 750 ｜ Call Wall 750（+2.0%，弱）（OI 2.1k） ｜ Put Wall 715（-2.8%）（OI 4.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/SPY_evening.json