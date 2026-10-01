# 期权晚报 2026-10-01（快照 16:40 ET）

📊 市场环境

SPY $763.99 ｜ QQQ $742.03
VIX 16.39 ↑0.3%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-01

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 54.5 ｜ 前值 54.6　✅ 今日已公布
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 731P ΔOI +10,358（距现价 -4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-06 810C ΔOI +44,167 占该期限总 OI 27.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 764.36 → 收盘 763.99（-0.0%） ｜ 今日高 765.65 ｜ 低 758.79 ｜ 昨收 762.63 → 收盘 763.99（+0.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.14 | OI比 1.23 | ATM IV 13.5% | Skew 0.5pp | Term 1.02 | ExpMove ±0.7%（近端） | Rank 55%
量化视角： IV 中性（Rank 55%）｜期限结构正常（Term 1.02）｜保护溢价薄（Skew 0.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.14×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.23×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 38% ｜ P/C OI(近端) 8%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 38%）｜近端持仓极端 Call 重（P/C OI 分位 8%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-02（1D）±0.7% ｜ 10-05（4D）±0.9% ｜ 10-06（5D）±1.1% ｜ 10-07（6D）±1.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -773,957,502 | GEX Change vs 上次快照 481,614,154 | Flip: Primary Flip: 768.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 2467 / LOW 390 / INVALID 1943
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 768.50（全链重定价，覆盖 95%）
Call Wall 785（现价低于该位 2.7%）
最近结构参考: Flip 769（现价低于该位 0.6%）
量化视角： 负 Gamma（7.74亿，历史分位 38%，中性区）｜负 Gamma 缓解（+4.82亿）｜现价位于 Flip 下方 0.59%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 764（MaxPain，仅结算参考） / 785（Call Wall）。
• Gamma 区域：切换参考 769（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +41.6k / P +64.3k ｜ Activity HIGH ｜ 1D
10-05  C +11.0k / P +12.0k ｜ Activity HIGH ｜ 4D
10-06  C +96.6k / P +7.1k ｜ Activity HIGH ｜ 5D
10-07  C +33.3k / P +13.0k ｜ Activity HIGH ｜ 6D

📆 10-02 Forward Structure
存量OI: C 351.5k / P 550.3k，今日变化ΔOI: C +41.6k / P +64.3k，平值价格ATM: C $3.07 / P $2.16 ｜ ATM IV 16.1%，净 delta 敞口 678k shares
Top ΔOI: P 730 +11,738 ｜ P 731 +10,358 ｜ P 729 +6,093
仓位参考: Max Pain 765 ｜ Call Wall 785（+2.8%）（OI 61.3k） ｜ Put Wall 745（-2.5%，弱）（OI 68.1k）
量化解读： 存量 Put 重｜ATM IV 16.1%｜历史 Rank 55%（近端代理）｜IV/RV 1.64×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 677,643 股

📆 10-05 Forward Structure
存量OI: C 49.1k / P 77.2k，今日变化ΔOI: C +11.0k / P +12.0k，平值价格ATM: C $4.07 / P $3.12 ｜ ATM IV 11.1%，净 delta 敞口 -15k shares
Top ΔOI: P 735 +2,278 ｜ C 795 +1,878 ｜ C 794 +1,856
仓位参考: Max Pain 766 ｜ Call Wall 775（+1.4%，弱）（OI 2.6k） ｜ Put Wall 750（-1.8%，弱）（OI 6.9k）
量化解读： 存量 Put 重｜ATM IV 11.1%｜历史 Rank 55%（近端代理）｜IV/RV 1.13×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 14,945 股

📆 10-06 Forward Structure
存量OI: C 122.3k / P 38.6k，今日变化ΔOI: C +96.6k / P +7.1k，平值价格ATM: C $4.65 / P $3.70 ｜ ATM IV 11.6%，净 delta 敞口 23k shares
Top ΔOI: C 810 +44,167 ｜ C 809 +41,674 ｜ C 825 +2,872
仓位参考: Max Pain 766
量化解读： 存量 Call 重｜ATM IV 11.6%｜历史 Rank 55%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 正 22,519 股

📆 10-07 Forward Structure
存量OI: C 48.8k / P 65.5k，今日变化ΔOI: C +33.3k / P +13.0k，平值价格ATM: C $5.19 / P $4.23 ｜ ATM IV 12.0%，净 delta 敞口 265k shares
Top ΔOI: C 810 +11,654 ｜ P 690 +8,030
仓位参考: Max Pain 766 ｜ Put Wall 760（-0.5%，弱）（OI 14.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 12.0%｜历史 Rank 55%（近端代理）｜IV/RV 1.23×（近似）｜净 delta 敞口 正 264,763 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/SPY_evening.json