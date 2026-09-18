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
🟡 **近现价集中开仓**: 09-25 150P ΔOI +8,037（距现价 -1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 146.1）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 154.66 → 收盘 152.71（-1.3%） ｜ 今日高 156.60 ｜ 低 149.93 ｜ 昨收 154.81 → 收盘 152.71（-1.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.44 | OI比 0.97 | ATM IV 55.5% | Skew -3.2pp | Term 0.87 | ExpMove ±5.1%（近端） | Rank 23%
量化视角： IV 历史低位（Rank 23%，期权偏便宜）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.97×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（7D）±5.1% ｜ 10-02（14D）±7.5% ｜ 10-09（21D）±9.1% ｜ 10-16（28D）±10.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 54,880,536 | GEX Change vs 上次快照 12,894,267 | Flip: Candidates 146.15 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 77%（带内） ｜ IV 有效性: VALID 505 / LOW 107 / INVALID 462
结构观察区: ≈146（全链重定价，覆盖 77%，CONDITIONAL）
Call Wall 160（弱结构｜现价低于该位 4.6%）
最近结构参考: Flip 146（现价高于该位 4.5%）
量化视角： 正 Gamma（5488万，无历史分位）｜正 Gamma 增强（+1289万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（MaxPain，仅结算参考）；上方 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 146（全链重定价，覆盖 77%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +10.3k / P +19.5k ｜ Activity HIGH ｜ 7D
10-02  C +4.4k / P +2.7k ｜ Activity HIGH ｜ 14D
10-09  C +3.0k / P +2.0k ｜ Activity HIGH ｜ 21D
10-16  C +23.7k / P +65.1k ｜ Activity HIGH ｜ 28D

📆 09-25 Forward Structure
存量OI: C 99.7k / P 138.7k，今日变化ΔOI: C +10.3k / P +19.5k，平值价格ATM: C $4.10 / P $3.75 ｜ ATM IV 46.4%，净 delta 敞口 -409k shares
Top ΔOI: P 150 +8,037 ｜ P 142 +3,186
仓位参考: Max Pain 150 ｜ Call Wall 160（+4.8%，弱）（OI 10.2k） ｜ Put Wall 140（-8.3%，弱）（OI 12.8k）
量化解读： 存量 Put 重｜ATM IV 46.4%｜历史 Rank 23%（近端代理）｜净 delta 敞口 负 409,439 股

📆 10-02 Forward Structure
存量OI: C 39.5k / P 49.5k，今日变化ΔOI: C +4.4k / P +2.7k，平值价格ATM: C $5.91 / P $5.50 ｜ ATM IV 47.4%，净 delta 敞口 -81k shares
Top ΔOI: C 160 +1,410 ｜ P 133 -1,025 ｜ P 155 +1,007
仓位参考: Max Pain 150 ｜ Call Wall 160（+4.8%，弱）（OI 3.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 47.4%｜历史 Rank 23%（近端代理）｜净 delta 敞口 负 80,877 股

📆 10-09 Forward Structure
存量OI: C 19.7k / P 19.7k，今日变化ΔOI: C +3.0k / P +2.0k，平值价格ATM: C $6.97 / P $6.91 ｜ ATM IV 47.4%，净 delta 敞口 -22k shares
Top ΔOI: C 160 +518 ｜ P 157 +480
仓位参考: Max Pain 149 ｜ Call Wall 165（+8.0%，弱）（OI 1.9k） ｜ Put Wall 140（-8.3%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 47.4%｜历史 Rank 23%（近端代理）｜净 delta 敞口 负 21,989 股

📆 10-16 Forward Structure
存量OI: C 308.2k / P 346.0k，今日变化ΔOI: C +23.7k / P +65.1k，平值价格ATM: C $7.25 / P $9.25 ｜ ATM IV 48.2%，净 delta 敞口 -240k shares
Top ΔOI: P 155 +33,799 ｜ P 135 +24,296 ｜ C 115 +6,469
仓位参考: Max Pain 145 ｜ Call Wall 160（+4.8%，弱）（OI 32.7k） ｜ Put Wall 155（+1.5%，弱）（OI 35.5k）
量化解读： 存量两侧均衡｜ATM IV 48.2%｜历史 Rank 23%（近端代理）｜净 delta 敞口 负 239,555 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/SPCX_evening.json