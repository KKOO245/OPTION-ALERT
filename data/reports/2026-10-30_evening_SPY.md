# 期权晚报 2026-10-30（快照 16:40 ET）

📊 市场环境

SPY $755.72 ｜ QQQ $690.49
VIX 19.42 ↑12.9%（5D -0.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-02 775P ΔOI +9,353（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-03 665P ΔOI +19,139 占该期限总 OI 14.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 761.38 → 收盘 755.72（-0.7%） ｜ 今日高 761.46 ｜ 低 750.36 ｜ 昨收 769.36 → 收盘 755.72（-1.8%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-04，窗口结束前不做对错判定）

Options: P/C成交量 1.26 | OI比 2.24 | ATM IV 20.8% | Skew -1.6pp | Term 0.74 | ExpMove ±0.9%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.6pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.26）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.26×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.24×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 20% ｜ P/C OI(近端) 77%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 20%）｜近端持仓结构中性（P/C OI 分位 77%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-02（3D）±0.9% ｜ 11-03（4D）±1.2% ｜ 11-04（5D）±1.5% ｜ 11-05（6D）±1.7%
   ⇒ IV–VIX Spread: +1.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,752,235,153 | GEX Change vs 上次快照 124,177,439 | Flip: Primary Flip: 777.95（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 2488 / LOW 351 / INVALID 1361
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 777.95（全链重定价，覆盖 84%）
最近结构参考: Flip 778（现价低于该位 2.9%）
量化视角： 负 Gamma（17.52亿，历史分位偏负区，比 80% 的交易日更负）｜负 Gamma 缓解（+1.24亿）｜现价位于 Flip 下方 2.86%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 765（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 778（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-02  C +29.9k / P +38.5k ｜ Activity HIGH ｜ 3D
11-03  C +16.9k / P +38.4k ｜ Activity HIGH ｜ 4D
11-04  C +22.6k / P +19.5k ｜ Activity HIGH ｜ 5D
11-05  C +5.8k / P +7.6k ｜ Activity HIGH ｜ 6D

📆 11-02 Forward Structure
存量OI: C 68.4k / P 115.1k，今日变化ΔOI: C +29.9k / P +38.5k，平值价格ATM: C $3.89 / P $2.96 ｜ ATM IV 12.2%，净 delta 敞口 -1.8M shares
Top ΔOI: P 775 +9,353 ｜ C 774 +4,353 ｜ P 757 +2,872
仓位参考: Max Pain 772 ｜ Call Wall 774（+2.4%，弱）（OI 4.8k） ｜ Put Wall 775（+2.6%）（OI 15.3k）
量化解读： 存量 Put 重｜ATM IV 12.2%｜历史 Rank 86%（近端代理）｜IV/RV 1.36×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,842,337 股

📆 11-03 Forward Structure
存量OI: C 43.3k / P 87.4k，今日变化ΔOI: C +16.9k / P +38.4k，平值价格ATM: C $5.07 / P $4.04 ｜ ATM IV 14.1%，净 delta 敞口 -538k shares
Top ΔOI: P 665 +19,139 ｜ P 740 +5,519 ｜ P 754 +2,292
仓位参考: Max Pain 769 ｜ Call Wall 770（+1.9%，弱）（OI 2.7k） ｜ Put Wall 740（-2.1%，弱）（OI 6.2k）
量化解读： 存量 Put 重｜ATM IV 14.1%｜历史 Rank 86%（近端代理）｜IV/RV 1.57×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 538,300 股

📆 11-04 Forward Structure
存量OI: C 39.3k / P 86.1k，今日变化ΔOI: C +22.6k / P +19.5k，平值价格ATM: C $6.17 / P $5.21 ｜ ATM IV 15.8%，净 delta 敞口 -918k shares
Top ΔOI: P 767 +7,215 ｜ P 755 +4,047 ｜ C 776 +3,740
仓位参考: Max Pain 769 ｜ Call Wall 776（+2.7%，弱）（OI 4.0k） ｜ Put Wall 767（+1.5%）（OI 37.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 15.8%｜历史 Rank 86%（近端代理）｜IV/RV 1.75×（近似）｜净 delta 敞口 负 918,030 股

📆 11-05 Forward Structure
存量OI: C 23.7k / P 17.4k，今日变化ΔOI: C +5.8k / P +7.6k，平值价格ATM: C $7.55 / P $5.41 ｜ ATM IV 16.4%，净 delta 敞口 -153k shares
Top ΔOI: C 790 +1,748 ｜ P 710 +1,480 ｜ P 740 +1,444
仓位参考: Max Pain 765 ｜ Put Wall 760（+0.6%，弱）（OI 2.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 16.4%｜历史 Rank 86%（近端代理）｜IV/RV 1.82×（近似）｜净 delta 敞口 负 153,430 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/SPY_evening.json