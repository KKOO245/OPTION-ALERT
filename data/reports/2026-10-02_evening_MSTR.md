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
🟡 **近现价集中开仓**: 10-09 165C ΔOI +2,577（距现价 +3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 142.3）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 165.85 → 收盘 160.01（-3.5%） ｜ 今日高 170.17 ｜ 低 155.89 ｜ 昨收 160.50 → 收盘 160.01（-0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.31 | OI比 0.79 | ATM IV 35.9% | Skew 7.3pp | Term 1.72 | ExpMove ±6.3%（近端） | Rank 0%
量化视角： IV 历史低位（Rank 0%，期权偏便宜）｜期限结构正常偏陡（Term 1.72）｜保护溢价显著（Skew 7.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.31×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±6.3% ｜ 10-16（14D）±9.2% ｜ 10-23（21D）±11.8% ｜ 10-30（28D）±14.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 77,651,171 | GEX Change vs 上次快照 -44,364,274 | Flip: Candidates 142.33 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 74%（带内） ｜ IV 有效性: VALID 533 / LOW 101 / INVALID 416
结构观察区: ≈142（全链重定价，覆盖 74%，CONDITIONAL）
Call Wall 165（弱结构｜现价低于该位 3.0%）
最近结构参考: Call Wall 165（现价低于该位 3.0%）
量化视角： 正 Gamma（7765万，无历史分位）｜正 Gamma 减弱（4436万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 152（MaxPain，仅结算参考）；上方 165（Call Wall，弱结构）。
• Gamma 区域：切换参考 142（全链重定价，覆盖 74%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +13.4k / P +9.6k ｜ Activity HIGH ｜ 7D
10-16  C +4.0k / P +7.9k ｜ Activity HIGH ｜ 14D
10-23  C +5.9k / P +5.1k ｜ Activity HIGH ｜ 21D
10-30  C +0.6k / P +2.1k ｜ Activity HIGH ｜ 28D

📆 10-09 Forward Structure
存量OI: C 65.1k / P 73.9k，今日变化ΔOI: C +13.4k / P +9.6k，平值价格ATM: C $5.05 / P $5.00 ｜ ATM IV 56.5%，净 delta 敞口 169k shares
Top ΔOI: C 165 +2,577 ｜ C 172 +2,083
仓位参考: Max Pain 150 ｜ Call Wall 165（+3.1%，弱）（OI 8.1k） ｜ Put Wall 155（-3.1%，弱）（OI 3.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 56.5%｜历史 Rank 0%（近端代理）｜IV/RV 0.74×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 168,706 股

📆 10-16 Forward Structure
存量OI: C 179.3k / P 153.7k，今日变化ΔOI: C +4.0k / P +7.9k，平值价格ATM: C $7.40 / P $7.40 ｜ ATM IV 58.5%，净 delta 敞口 93k shares
Top ΔOI: C 200 -2,556 ｜ C 172 +1,788 ｜ P 150 +1,698
仓位参考: Max Pain 125 ｜ Call Wall 155（-3.1%，弱）（OI 10.4k） ｜ Put Wall 150（-6.3%，弱）（OI 6.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 58.5%｜历史 Rank 0%（近端代理）｜IV/RV 0.77×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 93,074 股

📆 10-23 Forward Structure
存量OI: C 26.6k / P 32.3k，今日变化ΔOI: C +5.9k / P +5.1k，平值价格ATM: C $9.30 / P $9.51 ｜ ATM IV 59.5%，净 delta 敞口 154k shares
Top ΔOI: C 172 +5,676
仓位参考: Max Pain 160 ｜ Call Wall 172.5（+7.8%）（OI 5.8k） ｜ Put Wall 155（-3.1%，弱）（OI 2.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 59.5%｜历史 Rank 0%（近端代理）｜IV/RV 0.78×（近似）｜净 delta 敞口 正 153,823 股

📆 10-30 Forward Structure
存量OI: C 15.6k / P 22.6k，今日变化ΔOI: C +0.6k / P +2.1k，平值价格ATM: C $11.10 / P $11.29 ｜ ATM IV 61.9%，净 delta 敞口 -36k shares
Top ΔOI: P 155 +281
仓位参考: Max Pain 160 ｜ Call Wall 165（+3.1%，弱）（OI 1.0k） ｜ Put Wall 160（-0.0%，弱）（OI 2.4k）
量化解读： 存量 Put 重｜ATM IV 61.9%｜历史 Rank 0%（近端代理）｜IV/RV 0.81×（近似）｜净 delta 敞口 负 36,215 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/MSTR_evening.json