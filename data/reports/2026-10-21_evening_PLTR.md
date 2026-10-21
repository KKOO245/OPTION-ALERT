# 期权晚报 2026-10-21（快照 16:40 ET）

📊 市场环境

SPY $773.09 ｜ QQQ $725.20
VIX 16.68 ↓3.6%（5D -1.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 191.45 → 收盘 201.72（+5.4%） ｜ 今日高 202.55 ｜ 低 189.88 ｜ 昨收 192.60 → 收盘 201.72（+4.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.56 | OI比 0.95 | ATM IV 51.6% | Skew 4.1pp | Term 1.20 | ExpMove ±3.1%（近端） | Rank 61%
量化视角： IV 中性（Rank 61%）｜期限结构正常偏陡（Term 1.20）｜保护溢价中性（Skew 4.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.95×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（2D）±3.1% ｜ 10-30（9D）±6.0% ｜ 11-06（16D）±12.3% ｜ 11-13（23D）±13.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 71,383,143 | GEX Change vs 上次快照 22,905,254 | Flip: Primary Flip: 187.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 663 / LOW 76 / INVALID 173
结构观察区: Primary Flip 187.41（全链重定价，覆盖 100%）
Put Wall 190（弱结构｜现价高于该位 6.2%） | Call Wall 200（弱结构｜现价高于该位 0.9%）
最近结构参考: Call Wall 200（现价高于该位 0.9%）
量化视角： 正 Gamma（7138万，无历史分位）｜正 Gamma 增强（+2291万）｜现价位于 Flip 上方 7.63%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（Put Wall，弱结构） / 190（MaxPain，仅结算参考） / 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 187（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +4.0k / P +8.9k ｜ Activity HIGH ｜ 2D
10-30  C +2.1k / P +4.1k ｜ Activity HIGH ｜ 9D
11-06  C +1.5k / P +3.1k ｜ Activity HIGH ｜ 16D
11-13  C +0.8k / P +1.2k ｜ Activity HIGH ｜ 23D

📆 10-23 Forward Structure
存量OI: C 131.6k / P 124.7k，今日变化ΔOI: C +4.0k / P +8.9k，平值价格ATM: C $2.75 / P $3.47 ｜ ATM IV 51.6%，净 delta 敞口 126k shares
Top ΔOI: P 185 +1,778 ｜ C 212 +1,197 ｜ P 190 +1,095
仓位参考: Max Pain 190 ｜ Call Wall 205（+1.6%，弱）（OI 16.9k） ｜ Put Wall 190（-5.8%，弱）（OI 7.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 51.6%｜历史 Rank 61%（近端代理）｜IV/RV 1.26×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 126,215 股

📆 10-30 Forward Structure
存量OI: C 50.5k / P 80.4k，今日变化ΔOI: C +2.1k / P +4.1k，平值价格ATM: C $5.84 / P $6.29 ｜ ATM IV 47.4%，净 delta 敞口 117k shares
Top ΔOI: P 190 -698 ｜ P 182 +432
仓位参考: Max Pain 190 ｜ Call Wall 200（-0.9%，弱）（OI 3.9k） ｜ Put Wall 190（-5.8%，弱）（OI 6.2k）
量化解读： 存量 Put 重｜ATM IV 47.4%｜历史 Rank 61%（近端代理）｜IV/RV 1.16×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 117,231 股

📆 11-06 Forward Structure
存量OI: C 26.4k / P 27.6k，今日变化ΔOI: C +1.5k / P +3.1k，平值价格ATM: C $12.20 / P $12.55 ｜ ATM IV 73.1%，净 delta 敞口 42k shares
仓位参考: Max Pain 190 ｜ Call Wall 205（+1.6%，弱）（OI 1.8k） ｜ Put Wall 190（-5.8%，弱）（OI 3.0k）
量化解读： 存量两侧均衡｜ATM IV 73.1%｜历史 Rank 61%（近端代理）｜IV/RV 1.79×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 41,849 股

📆 11-13 Forward Structure
存量OI: C 10.5k / P 13.7k，今日变化ΔOI: C +0.8k / P +1.2k，平值价格ATM: C $13.30 / P $13.50 ｜ ATM IV 65.9%，净 delta 敞口 13k shares
Top ΔOI: C 240 +246
仓位参考: Max Pain 192 ｜ Call Wall 210（+4.1%，弱）（OI 1.1k） ｜ Put Wall 185（-8.3%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜ATM IV 65.9%｜历史 Rank 61%（近端代理）｜IV/RV 1.61×（近似）｜净 delta 敞口 正 13,320 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/PLTR_evening.json