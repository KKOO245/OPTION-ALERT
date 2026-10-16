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
🟡 **近现价集中开仓**: 10-19 731P ΔOI +17,363（距现价 -4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-19 655P ΔOI +57,154 占该期限总 OI 14.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 773.24 → 收盘 763.25（-1.3%） ｜ 今日高 773.23 ｜ 低 760.64 ｜ 昨收 771.79 → 收盘 763.25（-1.1%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-21，窗口结束前不做对错判定）

Options: P/C成交量 1.29 | OI比 3.03 | ATM IV 20.7% | Skew 0.8pp | Term 0.70 | ExpMove ±0.8%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价薄（Skew 0.8pp）｜当日成交偏 Put（P/C量 1.29）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.29×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 3.03×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 20% ｜ P/C OI(近端) 96%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 20%）｜近端 Put 显著偏重（P/C OI 分位 96%，历史高位区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-19（3D）±0.8% ｜ 10-20（4D）±1.1% ｜ 10-21（5D）±1.2% ｜ 10-22（6D）±1.4%
   ⇒ IV–VIX Spread: +0.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,730,713,205 | GEX Change vs 上次快照 -919,855,855 | Flip: Primary Flip: 777.79（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 80%（带内） ｜ IV 有效性: VALID 2613 / LOW 392 / INVALID 1803
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 777.79（全链重定价，覆盖 80%）
最近结构参考: Flip 778（现价低于该位 1.9%）
量化视角： 负 Gamma（17.31亿，历史分位偏负区，比 80% 的交易日更负）｜负 Gamma 加深（9.20亿）｜现价位于 Flip 下方 1.87%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 770（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 778（全链重定价，覆盖 80%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-19  C +26.2k / P +201.9k ｜ Activity HIGH ｜ 3D
10-20  C +17.8k / P +45.5k ｜ Activity HIGH ｜ 4D
10-21  C +17.8k / P +43.8k ｜ Activity HIGH ｜ 5D
10-22  C +12.5k / P +10.6k ｜ Activity HIGH ｜ 6D

📆 10-19 Forward Structure
存量OI: C 94.1k / P 295.8k，今日变化ΔOI: C +26.2k / P +201.9k，平值价格ATM: C $3.07 / P $3.16 ｜ ATM IV 11.2%，净 delta 敞口 -1.6M shares
Top ΔOI: P 655 +57,154 ｜ P 660 +52,180 ｜ P 731 +17,363
仓位参考: Max Pain 773 ｜ Call Wall 782（+2.5%，弱）（OI 6.8k）
量化解读： 存量 Put 重｜ATM IV 11.2%｜历史 Rank 87%（近端代理）｜IV/RV 1.43×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,622,174 股

📆 10-20 Forward Structure
存量OI: C 62.3k / P 132.5k，今日变化ΔOI: C +17.8k / P +45.5k，平值价格ATM: C $4.03 / P $4.03 ｜ ATM IV 12.6%，净 delta 敞口 -364k shares
Top ΔOI: P 731 +19,240 ｜ P 695 +8,642 ｜ C 784 +4,584
仓位参考: Max Pain 773 ｜ Call Wall 784（+2.7%，弱）（OI 5.9k） ｜ Put Wall 751（-1.6%，弱）（OI 12.4k）
量化解读： 存量 Put 重｜ATM IV 12.6%｜历史 Rank 87%（近端代理）｜IV/RV 1.60×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 364,349 股

📆 10-21 Forward Structure
存量OI: C 57.5k / P 123.1k，今日变化ΔOI: C +17.8k / P +43.8k，平值价格ATM: C $4.75 / P $4.76 ｜ ATM IV 13.3%，净 delta 敞口 -529k shares
Top ΔOI: P 746 +9,044 ｜ P 748 +7,995 ｜ P 670 +3,725
仓位参考: Max Pain 771 ｜ Call Wall 773（+1.3%，弱）（OI 2.3k） ｜ Put Wall 746（-2.3%，弱）（OI 10.5k）
量化解读： 存量 Put 重｜ATM IV 13.3%｜历史 Rank 87%（近端代理）｜IV/RV 1.70×（近似）｜净 delta 敞口 负 528,807 股

📆 10-22 Forward Structure
存量OI: C 32.6k / P 31.9k，今日变化ΔOI: C +12.5k / P +10.6k，平值价格ATM: C $5.49 / P $5.31 ｜ ATM IV 13.7%，净 delta 敞口 -119k shares
Top ΔOI: C 804 +2,065 ｜ P 734 +1,617 ｜ C 802 +1,405
仓位参考: Max Pain 774 ｜ Call Wall 775（+1.5%，弱）（OI 1.3k） ｜ Put Wall 759（-0.6%，弱）（OI 1.5k）
量化解读： 存量两侧均衡｜ATM IV 13.7%｜历史 Rank 87%（近端代理）｜IV/RV 1.75×（近似）｜净 delta 敞口 负 119,283 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/SPY_evening.json