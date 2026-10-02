# 期权晚报 2026-10-02（快照 16:40 ET）

📊 市场环境

SPY $769.64 ｜ QQQ $749.58
VIX 15.31 ↓6.6%（5D +3.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-05 736P ΔOI +18,082（距现价 -1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-08 675P ΔOI +5,959 占该期限总 OI 10.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 751.31 → 收盘 749.58（-0.2%） ｜ 今日高 754.53 ｜ 低 747.53 ｜ 昨收 742.03 → 收盘 749.58（+1.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.90 | OI比 2.06 | ATM IV 11.6% | Skew 3.5pp | Term 1.61 | ExpMove ±0.8%（近端） | Rank 14%
量化视角： IV 历史低位（Rank 14%，期权偏便宜）｜期限结构正常偏陡（Term 1.61）｜保护溢价中性（Skew 3.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.90×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.06×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 90% ｜ P/C OI(近端) 80%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 90%）｜近端持仓结构中性（P/C OI 分位 80%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-05（3D）±0.8% ｜ 10-06（4D）±1.1% ｜ 10-07（5D）±1.3% ｜ 10-08（6D）±1.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 518,267,773 | GEX Change vs 上次快照 -53,398,487 | Flip: Primary Flip: 742.76（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 2768 / LOW 293 / INVALID 1823
结构观察区: Primary Flip 742.76（全链重定价，覆盖 89%）
Call Wall 760（现价低于该位 1.4%）
最近结构参考: Flip 743（现价高于该位 0.9%）
量化视角： 正 Gamma（5.18亿，历史分位偏正区，比 90% 的交易日更正）｜正 Gamma 减弱（5340万）｜现价位于 Flip 上方 0.92%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 738（MaxPain，仅结算参考）；上方 760（Call Wall）。
• Gamma 区域：切换参考 743（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-05  C +26.9k / P +55.0k ｜ Activity HIGH ｜ 3D
10-06  C +5.1k / P +17.8k ｜ Activity HIGH ｜ 4D
10-07  C +8.6k / P +12.1k ｜ Activity HIGH ｜ 5D
10-08  C +5.9k / P +26.8k ｜ Activity HIGH ｜ 6D

📆 10-05 Forward Structure
存量OI: C 71.0k / P 174.5k，今日变化ΔOI: C +26.9k / P +55.0k，平值价格ATM: C $2.83 / P $2.87 ｜ ATM IV 10.4%，净 delta 敞口 662k shares
Top ΔOI: P 736 +18,082 ｜ P 735 +10,960 ｜ C 755 +6,007
仓位参考: Max Pain 740 ｜ Call Wall 755（+0.7%，弱）（OI 13.8k） ｜ Put Wall 736（-1.8%）（OI 25.6k）
量化解读： 存量 Put 重｜ATM IV 10.4%｜历史 Rank 14%（近端代理）｜IV/RV 0.71×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 661,690 股

📆 10-06 Forward Structure
存量OI: C 23.3k / P 59.6k，今日变化ΔOI: C +5.1k / P +17.8k，平值价格ATM: C $4.03 / P $3.97 ｜ ATM IV 12.7%，净 delta 敞口 130k shares
Top ΔOI: P 715 +3,482 ｜ P 736 +1,554 ｜ C 757 +1,267
仓位参考: Max Pain 739 ｜ Call Wall 770（+2.7%）（OI 2.6k） ｜ Put Wall 736（-1.8%，弱）（OI 5.5k）
量化解读： 存量 Put 重｜ATM IV 12.7%｜历史 Rank 14%（近端代理）｜IV/RV 0.86×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 130,236 股

📆 10-07 Forward Structure
存量OI: C 28.0k / P 58.7k，今日变化ΔOI: C +8.6k / P +12.1k，平值价格ATM: C $5.03 / P $4.84 ｜ ATM IV 14.0%，净 delta 敞口 172k shares
Top ΔOI: C 763 +2,895 ｜ P 717 +1,254 ｜ C 770 +1,117
仓位参考: Max Pain 740 ｜ Call Wall 763（+1.8%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 14.0%｜历史 Rank 14%（近端代理）｜IV/RV 0.95×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 172,410 股

📆 10-08 Forward Structure
存量OI: C 15.8k / P 43.2k，今日变化ΔOI: C +5.9k / P +26.8k，平值价格ATM: C $5.87 / P $5.52 ｜ ATM IV 14.7%，净 delta 敞口 90k shares
Top ΔOI: P 675 +5,959
仓位参考: Max Pain 740 ｜ Call Wall 740（-1.3%，弱）（OI 1.5k） ｜ Put Wall 770（+2.7%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 14.7%｜历史 Rank 14%（近端代理）｜IV/RV 1.00×（近似）｜净 delta 敞口 正 89,569 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/QQQ_evening.json