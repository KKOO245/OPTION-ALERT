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
🟡 **事件差分**: 10-02 ATM IV 76.8% vs 10-09 63.3%（差 +13.5pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-02 162P ΔOI -3,487（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 153.77 → 收盘 160.50（+4.4%） ｜ 今日高 161.58 ｜ 低 152.84 ｜ 昨收 153.09 → 收盘 160.50（+4.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.52 | OI比 0.75 | ATM IV 76.8% | Skew -9.3pp | Term 0.86 | ExpMove ±3.2%（近端） | Rank 42%
量化视角： IV 中性（Rank 42%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -9.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±3.2% ｜ 10-09（8D）±7.5% ｜ 10-16（15D）±10.5% ｜ 10-23（22D）±12.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 97,888,272 | GEX Change vs 上次快照 36,686,129 | Flip: Primary Flip: 151.46（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 660 / LOW 135 / INVALID 255
结构观察区: Primary Flip 151.46（全链重定价，覆盖 98%）
Call Wall 170（弱结构｜现价低于该位 5.6%）
最近结构参考: Call Wall 170（现价低于该位 5.6%）
量化视角： 正 Gamma（9789万，无历史分位）｜正 Gamma 增强（+3669万）｜现价位于 Flip 上方 5.97%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 152（MaxPain，仅结算参考）；上方 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 151（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +10.5k / P -6.8k ｜ Activity MEDIUM △ ｜ 1D
10-09  C +8.6k / P +5.6k ｜ Activity HIGH ｜ 8D
10-16  C +2.4k / P +1.5k ｜ Activity MEDIUM △ ｜ 15D
10-23  C -2.0k / P +2.1k ｜ Activity HIGH ｜ 22D

📆 10-02 Forward Structure
存量OI: C 251.2k / P 187.6k，今日变化ΔOI: C +10.5k / P -6.8k，平值价格ATM: C $2.87 / P $2.30 ｜ ATM IV 76.8%，净 delta 敞口 674k shares
Top ΔOI: P 162 -3,487 ｜ C 170 -2,721
仓位参考: Max Pain 152 ｜ Call Wall 170（+5.9%，弱）（OI 38.3k） ｜ Put Wall 150（-6.5%，弱）（OI 9.2k）
量化解读： 存量 Call 重｜ATM IV 76.8%｜历史 Rank 42%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 673,702 股

📆 10-09 Forward Structure
存量OI: C 51.7k / P 64.3k，今日变化ΔOI: C +8.6k / P +5.6k，平值价格ATM: C $6.38 / P $5.68 ｜ ATM IV 63.3%，净 delta 敞口 251k shares
Top ΔOI: C 160 +2,138 ｜ C 170 +1,842 ｜ P 140 +1,786
仓位参考: Max Pain 150 ｜ Call Wall 160（-0.3%，弱）（OI 6.6k） ｜ Put Wall 155（-3.4%，弱）（OI 2.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 63.3%｜历史 Rank 42%（近端代理）｜IV/RV 0.82×（近似）｜净 delta 敞口 正 250,813 股

10-16（MEDIUM △）Top ΔOI: 150P +746 ｜ 160C +579
10-16（MEDIUM △）仓位参考: Max Pain 120 ｜ Call Wall 155（-3.4%，弱）（OI 10.3k） ｜ Put Wall 160（-0.3%，弱）（OI 4.5k）

📆 10-23 Forward Structure
存量OI: C 20.6k / P 27.2k，今日变化ΔOI: C -2.0k / P +2.1k，平值价格ATM: C $10.53 / P $9.36 ｜ ATM IV 63.9%，净 delta 敞口 -137k shares
Top ΔOI: C 165 -3,140 ｜ C 160 +584 ｜ P 150 +571
仓位参考: Max Pain 160 ｜ Call Wall 165（+2.8%，弱）（OI 2.0k） ｜ Put Wall 155（-3.4%，弱）（OI 2.4k）
量化解读： 存量 Put 重｜ATM IV 63.9%｜历史 Rank 42%（近端代理）｜IV/RV 0.83×（近似）｜净 delta 敞口 负 136,577 股

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 76.8% vs 10-09 63.3%（差 +13.5pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/MSTR_evening.json