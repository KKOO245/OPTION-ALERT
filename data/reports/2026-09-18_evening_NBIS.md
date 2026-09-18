# 期权晚报 2026-09-18（快照 16:40 ET）

📊 市场环境

SPY $761.69 ｜ QQQ $721.45
VIX 14.81 ↓4.1%（5D -6.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 29.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-25 230C ΔOI +1,643（距现价 +2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 213.2）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 218.15 → 收盘 223.54（+2.5%） ｜ 今日高 224.65 ｜ 低 210.30 ｜ 昨收 217.99 → 收盘 223.54（+2.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.49 | OI比 1.21 | ATM IV 91.4% | Skew 1.2pp | Term 0.85 | ExpMove ±8.1%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价薄（Skew 1.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.21×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（7D）±8.1% ｜ 10-02（14D）±12.1% ｜ 10-09（21D）±15.3% ｜ 10-16（28D）±17.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,935,237 | GEX Change vs 上次快照 14,021,222 | Flip: Candidates 213.19 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 75%（带内） ｜ IV 有效性: VALID 461 / LOW 57 / INVALID 284
结构观察区: ≈213（全链重定价，覆盖 75%，CONDITIONAL）
最近结构参考: Flip 213（现价高于该位 4.9%）
量化视角： 正 Gamma（694万，无历史分位）｜由负转正（+1402万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 215（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 213（全链重定价，覆盖 75%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +10.4k / P +5.1k ｜ Activity HIGH ｜ 7D
10-02  C +1.9k / P +0.9k ｜ Activity HIGH ｜ 14D
10-09  C +1.1k / P +0.7k ｜ Activity HIGH ｜ 21D
10-16  C +3.2k / P +6.7k ｜ Activity HIGH ｜ 28D

📆 09-25 Forward Structure
存量OI: C 35.6k / P 32.9k，今日变化ΔOI: C +10.4k / P +5.1k，平值价格ATM: C $9.65 / P $8.51 ｜ ATM IV 74.1%，净 delta 敞口 340k shares
Top ΔOI: C 250 +2,084 ｜ C 230 +1,643 ｜ C 215 +1,578
仓位参考: Max Pain 212 ｜ Call Wall 227.5（+1.8%，弱）（OI 3.3k） ｜ Put Wall 205（-8.3%，弱）（OI 2.1k）
量化解读： 存量两侧均衡｜ATM IV 74.1%｜历史 Rank 26%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 正 339,720 股

📆 10-02 Forward Structure
存量OI: C 11.6k / P 12.2k，今日变化ΔOI: C +1.9k / P +0.9k，平值价格ATM: C $14.00 / P $13.10 ｜ ATM IV 75.5%，净 delta 敞口 49k shares
Top ΔOI: C 275 +329
仓位参考: Max Pain 215 ｜ Call Wall 230（+2.9%，弱）（OI 0.4k） ｜ Put Wall 210（-6.1%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 75.5%｜历史 Rank 26%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 正 48,534 股

📆 10-09 Forward Structure
存量OI: C 8.0k / P 8.0k，今日变化ΔOI: C +1.1k / P +0.7k，平值价格ATM: C $15.90 / P $18.42 ｜ ATM IV 78.7%，净 delta 敞口 25k shares
Top ΔOI: P 170 +526
仓位参考: Max Pain 215 ｜ Call Wall 240（+7.4%）（OI 1.7k） ｜ Put Wall 210（-6.1%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 78.7%｜历史 Rank 26%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 24,888 股

📆 10-16 Forward Structure
存量OI: C 42.7k / P 66.9k，今日变化ΔOI: C +3.2k / P +6.7k，平值价格ATM: C $21.09 / P $16.90 ｜ ATM IV 77.4%，净 delta 敞口 97k shares
Top ΔOI: C 240 +709 ｜ C 250 +644
仓位参考: Max Pain 210 ｜ Call Wall 240（+7.4%，弱）（OI 4.3k） ｜ Put Wall 210（-6.1%，弱）（OI 2.8k）
量化解读： 存量 Put 重｜ATM IV 77.4%｜历史 Rank 26%（近端代理）｜IV/RV 1.20×（近似）｜净 delta 敞口 正 97,186 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/NBIS_evening.json