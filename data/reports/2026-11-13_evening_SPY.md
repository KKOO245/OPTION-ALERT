# 期权晚报 2026-11-13（快照 16:40 ET）

📊 市场环境

SPY $754.37 ｜ QQQ $679.89
VIX 19.30 ↑3.2%（5D -24.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-16 769C ΔOI +9,498（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-19 635P ΔOI +7,844 占该期限总 OI 10.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 760.07 → 收盘 754.37（-0.7%） ｜ 今日高 760.12 ｜ 低 747.89 ｜ 昨收 757.12 → 收盘 754.37（-0.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-18，窗口结束前不做对错判定）

Options: P/C成交量 1.25 | OI比 1.42 | ATM IV 37.4% | Skew 10.7pp | Term 0.40 | ExpMove ±0.8%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.40，近月 IV 高于远月）｜保护溢价显著（Skew 10.7pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.25）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.25×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.42×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 40% ｜ P/C OI(近端) 18%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 40%）｜近端持仓结构中性（P/C OI 分位 18%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-16（3D）±0.8% ｜ 11-17（4D）±1.2% ｜ 11-18（5D）±1.5% ｜ 11-19（6D）±1.6%
   ⇒ IV–VIX Spread: +18.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -695,949,028 | GEX Change vs 上次快照 302,190,023 | Flip: Primary Flip: 761.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 3040 / LOW 404 / INVALID 1638
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 761.43（全链重定价，覆盖 92%）
最近结构参考: Flip 761（现价低于该位 0.9%）
量化视角： 负 Gamma（6.96亿，历史分位 40%，中性区）｜负 Gamma 缓解（+3.02亿）｜现价位于 Flip 下方 0.93%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 758（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 761（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-16  C +46.5k / P +33.0k ｜ Activity HIGH ｜ 3D
11-17  C +10.0k / P +13.5k ｜ Activity HIGH ｜ 4D
11-18  C +17.7k / P +10.6k ｜ Activity HIGH ｜ 5D
11-19  C +6.5k / P +18.5k ｜ Activity HIGH ｜ 6D

📆 11-16 Forward Structure
存量OI: C 136.7k / P 144.1k，今日变化ΔOI: C +46.5k / P +33.0k，平值价格ATM: C $2.51 / P $3.83 ｜ ATM IV 11.5%，净 delta 敞口 -1.4M shares
Top ΔOI: C 769 +9,498 ｜ P 766 +6,071 ｜ P 758 +5,397
仓位参考: Max Pain 762 ｜ Call Wall 769（+1.9%，弱）（OI 10.8k） ｜ Put Wall 763（+1.1%）（OI 17.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 11.5%｜历史 Rank 99%（近端代理）｜IV/RV 0.52×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,423,261 股

📆 11-17 Forward Structure
存量OI: C 46.0k / P 52.2k，今日变化ΔOI: C +10.0k / P +13.5k，平值价格ATM: C $3.80 / P $4.99 ｜ ATM IV 13.8%，净 delta 敞口 -289k shares
Top ΔOI: P 750 +1,660 ｜ C 770 +1,004 ｜ P 760 +985
仓位参考: Max Pain 754 ｜ Call Wall 770（+2.1%，弱）（OI 1.8k） ｜ Put Wall 750（-0.6%）（OI 3.7k）
量化解读： 存量两侧均衡｜ATM IV 13.8%｜历史 Rank 99%（近端代理）｜IV/RV 0.63×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 289,365 股

📆 11-18 Forward Structure
存量OI: C 55.9k / P 78.2k，今日变化ΔOI: C +17.7k / P +10.6k，平值价格ATM: C $4.85 / P $6.39 ｜ ATM IV 15.2%，净 delta 敞口 -280k shares
Top ΔOI: C 796 +3,524 ｜ C 797 +3,424 ｜ C 765 +1,709
仓位参考: Max Pain 756 ｜ Call Wall 764（+1.3%，弱）（OI 2.4k） ｜ Put Wall 740（-1.9%，弱）（OI 7.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 15.2%｜历史 Rank 99%（近端代理）｜IV/RV 0.69×（近似）｜净 delta 敞口 负 280,431 股

📆 11-19 Forward Structure
存量OI: C 30.0k / P 42.8k，今日变化ΔOI: C +6.5k / P +18.5k，平值价格ATM: C $5.34 / P $6.63 ｜ ATM IV 15.6%，净 delta 敞口 -139k shares
Top ΔOI: P 635 +7,844 ｜ P 700 +1,462 ｜ P 720 +1,131
仓位参考: Max Pain 755 ｜ Call Wall 769（+1.9%，弱）（OI 1.9k） ｜ Put Wall 740（-1.9%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜ATM IV 15.6%｜历史 Rank 99%（近端代理）｜IV/RV 0.71×（近似）｜净 delta 敞口 负 139,387 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/SPY_evening.json