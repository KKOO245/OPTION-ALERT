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
🟡 **近现价集中开仓**: 10-02 755C ΔOI +10,517（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-07 675P ΔOI +11,736 占该期限总 OI 17.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 742.51 → 收盘 742.03（-0.1%） ｜ 今日高 744.67 ｜ 低 736.27 ｜ 昨收 739.77 → 收盘 742.03（+0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.86 | OI比 1.12 | ATM IV 15.9% | Skew 0.4pp | Term 1.24 | ExpMove ±0.9%（近端） | Rank 35%
量化视角： IV 中性（Rank 35%）｜期限结构正常偏陡（Term 1.24）｜保护溢价薄（Skew 0.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.86×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.12×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 55% ｜ P/C OI(近端) 11%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 55%）｜近端持仓结构中性（P/C OI 分位 11%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-02（1D）±0.9% ｜ 10-05（4D）±1.3% ｜ 10-06（5D）±1.6% ｜ 10-07（6D）±1.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 28,421,528 | GEX Change vs 上次快照 164,477,409 | Flip: Primary Flip: 741.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2776 / LOW 335 / INVALID 1853
结构观察区: Primary Flip 741.68（全链重定价，覆盖 94%）
Call Wall 760（现价低于该位 2.4%）
最近结构参考: Flip 742（现价高于该位 0.0%）
量化视角： 正 Gamma（2842万，历史分位 55%，中性区）｜由负转正（+1.64亿）｜现价位于 Flip 上方 0.05%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 740（MaxPain，仅结算参考）；上方 760（Call Wall）。
• Gamma 区域：切换参考 742（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +15.6k / P +21.8k ｜ Activity MEDIUM △ ｜ 1D
10-05  C +13.9k / P +30.7k ｜ Activity HIGH ｜ 4D
10-06  C +2.3k / P +7.6k ｜ Activity HIGH ｜ 5D
10-07  C +3.6k / P +29.4k ｜ Activity HIGH ｜ 6D

📆 10-02 Forward Structure
存量OI: C 257.6k / P 483.6k，今日变化ΔOI: C +15.6k / P +21.8k，平值价格ATM: C $4.11 / P $2.91 ｜ ATM IV 22.0%，净 delta 敞口 -1.2M shares
Top ΔOI: P 690 -17,505 ｜ C 755 +10,517 ｜ P 736 +7,424
仓位参考: Max Pain 735 ｜ Call Wall 725（-2.3%）（OI 35.1k） ｜ Put Wall 730（-1.6%，弱）（OI 48.9k）
量化解读： 存量 Put 重｜ATM IV 22.0%｜历史 Rank 35%（近端代理）｜IV/RV 1.50×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,224,479 股

📆 10-05 Forward Structure
存量OI: C 44.1k / P 119.5k，今日变化ΔOI: C +13.9k / P +30.7k，平值价格ATM: C $5.46 / P $4.24 ｜ ATM IV 15.7%，净 delta 敞口 -266k shares
Top ΔOI: P 736 +6,920 ｜ C 760 +6,596 ｜ P 725 +6,330
仓位参考: Max Pain 740 ｜ Call Wall 760（+2.4%，弱）（OI 8.0k） ｜ Put Wall 725（-2.3%，弱）（OI 7.7k）
量化解读： 存量 Put 重｜ATM IV 15.7%｜历史 Rank 35%（近端代理）｜IV/RV 1.06×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 266,451 股

📆 10-06 Forward Structure
存量OI: C 18.2k / P 41.8k，今日变化ΔOI: C +2.3k / P +7.6k，平值价格ATM: C $6.50 / P $5.43 ｜ ATM IV 16.7%，净 delta 敞口 -116k shares
Top ΔOI: P 736 +3,703 ｜ C 747 +782 ｜ P 715 +417
仓位参考: Max Pain 738 ｜ Call Wall 740（-0.3%，弱）（OI 1.4k） ｜ Put Wall 736（-0.8%，弱）（OI 3.9k）
量化解读： 存量 Put 重｜ATM IV 16.7%｜历史 Rank 35%（近端代理）｜IV/RV 1.14×（近似）｜净 delta 敞口 负 115,521 股

📆 10-07 Forward Structure
存量OI: C 19.4k / P 46.6k，今日变化ΔOI: C +3.6k / P +29.4k，平值价格ATM: C $7.13 / P $5.92 ｜ ATM IV 17.3%，净 delta 敞口 -23k shares
Top ΔOI: P 675 +11,736 ｜ P 670 +4,854
仓位参考: Max Pain 739 ｜ Call Wall 740（-0.3%，弱）（OI 2.3k）
量化解读： 存量 Put 重｜ATM IV 17.3%｜历史 Rank 35%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 负 22,898 股

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 22.0% vs 10-05 15.7%（差 +6.4pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/QQQ_evening.json