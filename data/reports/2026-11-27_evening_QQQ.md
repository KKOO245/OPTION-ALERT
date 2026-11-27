# 期权晚报 2026-11-27（快照 16:40 ET）

📊 市场环境

SPY $728.32 ｜ QQQ $650.99
VIX 23.81 ↓11.2%（5D -33.7%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-30 675C ΔOI +13,863（距现价 +3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-02 630P ΔOI +15,477 占该期限总 OI 17.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 645.72 → 收盘 650.99（+0.8%） ｜ 今日高 651.34 ｜ 低 636.72 ｜ 昨收 633.93 → 收盘 650.99（+2.7%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-04，窗口结束前不做对错判定）

Options: P/C成交量 0.89 | OI比 0.87 | ATM IV 37.3% | Skew 2.8pp | Term 0.79 | ExpMove ±1.8%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价中性（Skew 2.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.89×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.87×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 52% ｜ P/C OI(近端) 2%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 52%）｜近端持仓极端 Call 重（P/C OI 分位 2%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-30（3D）±1.8% ｜ 12-01（4D）±2.4% ｜ 12-02（5D）±2.8% ｜ 12-03（6D）±3.8%
   ⇒ IV–VIX Spread: +13.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,966,253 | GEX Change vs 上次快照 228,133,653 | Flip: Primary Flip: 650.86（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 3251 / LOW 459 / INVALID 2512
结构观察区: Primary Flip 650.86（全链重定价，覆盖 94%）
最近结构参考: Flip 651（现价高于该位 0.0%）
量化视角： 正 Gamma（297万，历史分位 52%，中性区）｜由负转正（+2.28亿）｜现价位于 Flip 上方 0.02%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 635（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 651（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-30  C +51.3k / P +44.7k ｜ Activity HIGH ｜ 3D
12-01  C +10.9k / P +7.8k ｜ Activity HIGH ｜ 4D
12-02  C +7.6k / P +39.6k ｜ Activity HIGH ｜ 5D
12-03  C +11.6k / P +14.9k ｜ Activity HIGH ｜ 6D

📆 11-30 Forward Structure
存量OI: C 410.0k / P 389.4k，今日变化ΔOI: C +51.3k / P +44.7k，平值价格ATM: C $5.43 / P $6.44 ｜ ATM IV 24.4%，净 delta 敞口 2.9M shares
Top ΔOI: P 610 +22,894 ｜ C 675 +13,863 ｜ P 680 -12,556
仓位参考: Max Pain 655 ｜ Call Wall 650（-0.2%，弱）（OI 20.0k） ｜ Put Wall 650（-0.2%，弱）（OI 19.3k）
量化解读： 存量两侧均衡｜ATM IV 24.4%｜历史 Rank 93%（近端代理）｜IV/RV 0.53×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 2,934,562 股

📆 12-01 Forward Structure
存量OI: C 40.3k / P 53.8k，今日变化ΔOI: C +10.9k / P +7.8k，平值价格ATM: C $7.37 / P $8.34 ｜ ATM IV 28.4%，净 delta 敞口 413k shares
Top ΔOI: C 615 +1,462 ｜ C 715 +1,074 ｜ C 655 +922
仓位参考: Max Pain 635 ｜ Call Wall 660（+1.4%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 28.4%｜历史 Rank 93%（近端代理）｜IV/RV 0.61×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 412,750 股

📆 12-02 Forward Structure
存量OI: C 28.9k / P 58.9k，今日变化ΔOI: C +7.6k / P +39.6k，平值价格ATM: C $8.97 / P $9.46 ｜ ATM IV 30.3%，净 delta 敞口 53k shares
Top ΔOI: P 630 +15,477
仓位参考: Max Pain 635 ｜ Call Wall 650（-0.2%）（OI 4.0k）
量化解读： 存量 Put 重｜ATM IV 30.3%｜历史 Rank 93%（近端代理）｜IV/RV 0.65×（近似）｜净 delta 敞口 正 53,470 股

📆 12-03 Forward Structure
存量OI: C 25.1k / P 45.3k，今日变化ΔOI: C +11.6k / P +14.9k，平值价格ATM: C $10.20 / P $14.53 ｜ ATM IV 31.3%，净 delta 敞口 399k shares
Top ΔOI: P 535 +6,611 ｜ C 665 +3,967 ｜ C 655 +3,817
仓位参考: Max Pain 638 ｜ Call Wall 665（+2.2%，弱）（OI 4.5k）
量化解读： 存量 Put 重｜ATM IV 31.3%｜历史 Rank 93%（近端代理）｜IV/RV 0.68×（近似）｜净 delta 敞口 正 398,994 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/QQQ_evening.json