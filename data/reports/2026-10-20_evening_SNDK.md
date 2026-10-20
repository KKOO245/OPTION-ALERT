# 期权晚报 2026-10-20（快照 16:40 ET）

📊 市场环境

SPY $769.05 ｜ QQQ $717.63
VIX 17.31 ↓6.1%（5D +13.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,336.96 → 收盘 1,365.38（+2.1%） ｜ 今日高 1388.88 ｜ 低 1330.51 ｜ 昨收 1,371.12 → 收盘 1,365.38（-0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.73 | OI比 0.86 | ATM IV 76.1% | Skew 2.3pp | Term 0.97 | ExpMove ±5.6%（近端） | Rank 33%
量化视角： IV 中性（Rank 33%）｜期限结构正常（Term 0.97）｜保护溢价中性（Skew 2.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（3D）±5.6% ｜ 10-30（10D）±12.0% ｜ 11-06（17D）±14.8% ｜ 11-13（24D）±15.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,478,050 | GEX Change vs 上次快照 385,720 | Flip: Primary Flip: 1397.99（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1991 / LOW 427 / INVALID 1036
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1397.99（全链重定价，覆盖 100%）
Call Wall 1,500（现价低于该位 9.0%）
最近结构参考: Flip 1398（现价低于该位 2.3%）
量化视角： 负 Gamma（248万，无历史分位）｜负 Gamma 缓解（+39万）｜现价位于 Flip 下方 2.33%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,445（MaxPain，仅结算参考） / 1,500（Call Wall）。
• Gamma 区域：切换参考 1398（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +7.3k / P +4.0k ｜ Activity HIGH ｜ 3D
10-30  C +2.3k / P +1.2k ｜ Activity HIGH ｜ 10D
11-06  C +0.7k / P +0.3k ｜ Activity HIGH ｜ 17D
11-13  C +0.3k / P +0.3k ｜ Activity HIGH ｜ 24D

📆 10-23 Forward Structure
存量OI: C 43.4k / P 37.3k，今日变化ΔOI: C +7.3k / P +4.0k，平值价格ATM: C $38.50 / P $37.50 ｜ ATM IV 76.1%，净 delta 敞口 50k shares
Top ΔOI: C 1500 +704 ｜ C 1450 +548 ｜ P 1200 +541
仓位参考: Max Pain 1,445 ｜ Call Wall 1500（+9.9%）（OI 2.9k） ｜ Put Wall 1250（-8.5%，弱）（OI 1.2k）
量化解读： 存量两侧均衡｜ATM IV 76.1%｜历史 Rank 33%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 49,816 股

📆 10-30 Forward Structure
存量OI: C 24.7k / P 16.3k，今日变化ΔOI: C +2.3k / P +1.2k，平值价格ATM: C $83.90 / P $80.45 ｜ ATM IV 89.5%，净 delta 敞口 40k shares
Top ΔOI: C 1400 +384 ｜ C 1450 +298
仓位参考: Max Pain 1,500 ｜ Call Wall 1500（+9.9%，弱）（OI 1.4k） ｜ Put Wall 1350（-1.1%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 89.5%｜历史 Rank 33%（近端代理）｜IV/RV 1.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 39,806 股

📆 11-06 Forward Structure
存量OI: C 8.7k / P 7.3k，今日变化ΔOI: C +0.7k / P +0.3k，平值价格ATM: C $108.29 / P $93.21 ｜ ATM IV 80.3%，净 delta 敞口 3k shares
Top ΔOI: C 1465 +101
仓位参考: Max Pain 1,500 ｜ Call Wall 1400（+2.5%，弱）（OI 0.6k） ｜ Put Wall 1400（+2.5%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 80.3%｜历史 Rank 33%（近端代理）｜IV/RV 1.60×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,882 股

📆 11-13 Forward Structure
存量OI: C 3.9k / P 4.0k，今日变化ΔOI: C +0.3k / P +0.3k，平值价格ATM: C $113.20 / P $97.84 ｜ ATM IV 75.8%，净 delta 敞口 -4k shares
Top ΔOI: C 1830 +65 ｜ C 1535 +41 ｜ P 1300 +29
仓位参考: Max Pain 1,510 ｜ Call Wall 1480（+8.4%，弱）（OI 0.2k） ｜ Put Wall 1300（-4.8%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 75.8%｜历史 Rank 33%（近端代理）｜IV/RV 1.51×（近似）｜净 delta 敞口 负 3,885 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/SNDK_evening.json