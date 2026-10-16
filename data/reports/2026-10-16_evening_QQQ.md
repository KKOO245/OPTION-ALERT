# 期权晚报 2026-10-16（快照 16:40 ET）

📊 市场环境

SPY $763.25 ｜ QQQ $709.80
VIX 19.99 ↑21.4%（5D +34.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 17.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-19 735C ΔOI +8,519（距现价 +3.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 725.48 → 收盘 709.80（-2.2%） ｜ 今日高 725.94 ｜ 低 707.23 ｜ 昨收 728.00 → 收盘 709.80（-2.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-21，窗口结束前不做对错判定）

Options: P/C成交量 0.92 | OI比 1.64 | ATM IV 21.4% | Skew 4.9pp | Term 1.06 | ExpMove ±1.4%（近端） | Rank 67%
量化视角： IV 中性（Rank 67%）｜期限结构正常（Term 1.06）｜保护溢价中性（Skew 4.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.92×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.64×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 2% ｜ P/C OI(近端) 51%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 2%）｜近端持仓结构中性（P/C OI 分位 51%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-19（3D）±1.4% ｜ 10-20（4D）±1.8% ｜ 10-21（5D）±2.1% ｜ 10-22（6D）±2.4%
   ⇒ IV–VIX Spread: +1.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,271,498,774 | GEX Change vs 上次快照 9,659,711 | Flip: Primary Flip: 742.84（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 2836 / LOW 364 / INVALID 1654
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 742.84（全链重定价，覆盖 85%）
Put Wall 700（弱结构｜现价高于该位 1.4%）
最近结构参考: Put Wall 700（现价高于该位 1.4%）
量化视角： 负 Gamma（12.71亿，历史分位偏负区，比 98% 的交易日更负）｜负 Gamma 缓解（+966万）｜现价位于 Flip 下方 4.45%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 727（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 743（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-19  C +34.7k / P +46.1k ｜ Activity HIGH ｜ 3D
10-20  C +16.5k / P +13.3k ｜ Activity HIGH ｜ 4D
10-21  C +7.9k / P +5.5k ｜ Activity HIGH ｜ 5D
10-22  C +7.9k / P +8.3k ｜ Activity HIGH ｜ 6D

📆 10-19 Forward Structure
存量OI: C 89.5k / P 132.8k，今日变化ΔOI: C +34.7k / P +46.1k，平值价格ATM: C $4.75 / P $5.14 ｜ ATM IV 19.1%，净 delta 敞口 -1.0M shares
Top ΔOI: C 735 +8,519 ｜ P 700 +6,598 ｜ P 645 +6,527
仓位参考: Max Pain 730 ｜ Call Wall 725（+2.1%，弱）（OI 2.5k） ｜ Put Wall 700（-1.4%，弱）（OI 8.4k）
量化解读： 存量 Put 重｜ATM IV 19.1%｜历史 Rank 67%（近端代理）｜IV/RV 1.61×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,043,645 股

📆 10-20 Forward Structure
存量OI: C 57.8k / P 59.4k，今日变化ΔOI: C +16.5k / P +13.3k，平值价格ATM: C $6.29 / P $6.64 ｜ ATM IV 21.6%，净 delta 敞口 -341k shares
Top ΔOI: P 705 +5,910 ｜ C 750 +3,647 ｜ C 743 +1,791
仓位参考: Max Pain 728 ｜ Put Wall 705（-0.7%，弱）（OI 6.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 21.6%｜历史 Rank 67%（近端代理）｜IV/RV 1.82×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 340,871 股

📆 10-21 Forward Structure
存量OI: C 31.5k / P 39.4k，今日变化ΔOI: C +7.9k / P +5.5k，平值价格ATM: C $7.45 / P $7.71 ｜ ATM IV 22.9%，净 delta 敞口 -5k shares
Top ΔOI: P 685 +1,349 ｜ C 740 +1,122 ｜ P 690 +1,110
仓位参考: Max Pain 733 ｜ Call Wall 730（+2.8%，弱）（OI 1.0k） ｜ Put Wall 710（+0.0%，弱）（OI 3.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 22.9%｜历史 Rank 67%（近端代理）｜IV/RV 1.93×（近似）｜净 delta 敞口 负 4,760 股

📆 10-22 Forward Structure
存量OI: C 20.6k / P 29.4k，今日变化ΔOI: C +7.9k / P +8.3k，平值价格ATM: C $8.39 / P $8.61 ｜ ATM IV 23.4%，净 delta 敞口 -196k shares
Top ΔOI: C 710 +1,346 ｜ P 710 +1,215 ｜ C 745 +984
仓位参考: Max Pain 727 ｜ Call Wall 710（+0.0%，弱）（OI 1.4k） ｜ Put Wall 705（-0.7%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 23.4%｜历史 Rank 67%（近端代理）｜IV/RV 1.97×（近似）｜净 delta 敞口 负 196,102 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/QQQ_evening.json