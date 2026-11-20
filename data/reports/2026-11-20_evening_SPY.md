# 期权晚报 2026-11-20（快照 16:40 ET）

📊 市场环境

SPY $689.81 ｜ QQQ $608.45
VIX 35.89 ↑26.2%（5D +86.0%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 9.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-23 695P ΔOI +9,068（距现价 +0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 713.56 → 收盘 689.81（-3.3%） ｜ 今日高 718.29 ｜ 低 686.75 ｜ 昨收 715.87 → 收盘 689.81（-3.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-25，窗口结束前不做对错判定）

Options: P/C成交量 1.51 | OI比 2.24 | ATM IV 81.8% | Skew -5.1pp | Term 0.37 | ExpMove ±2.5%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.37，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.1pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.51×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.24×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 34% ｜ P/C OI(近端) 77%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 34%）｜近端持仓结构中性（P/C OI 分位 77%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-23（3D）±2.5% ｜ 11-24（4D）±3.3% ｜ 11-25（5D）±3.8% ｜ 11-27（7D）±4.1%
   ⇒ IV–VIX Spread: +45.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -970,086,304 | GEX Change vs 上次快照 984,748,259 | Flip: Primary Flip: 735.97（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 80%（带内） ｜ IV 有效性: VALID 2646 / LOW 452 / INVALID 2048
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 735.97（全链重定价，覆盖 80%）
最近结构参考: Flip 736（现价低于该位 6.3%）
量化视角： 负 Gamma（9.70亿，历史分位 34%，中性区）｜负 Gamma 缓解（+9.85亿）｜现价位于 Flip 下方 6.27%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 730（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 736（全链重定价，覆盖 80%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-23  C +49.0k / P +41.4k ｜ Activity HIGH ｜ 3D（新行权价 C 14.5k / P 1.1k）
11-24  C +27.5k / P +14.6k ｜ Activity HIGH ｜ 4D（新行权价 C 13.1k / P 12.0k）
11-25  C +16.9k / P +21.0k ｜ Activity HIGH ｜ 5D（新行权价 C 27.2k / P 1.9k）
11-27  C -3.3k / P +9.8k ｜ Activity MEDIUM △ ｜ 7D（新行权价 C 2.3k / P 2）

📆 11-23 Forward Structure
存量OI: C 153.4k / P 113.4k，今日变化ΔOI: C +49.0k / P +41.4k（新行权价 C 14.5k / P 1.1k），平值价格ATM: C $10.13 / P $6.76 ｜ ATM IV 33.0%，净 delta 敞口 -1.8M shares
Top ΔOI: P 695 +9,068 ｜ C 720 +5,248 ｜ C 738 +4,709
仓位参考: Max Pain 728 ｜ Put Wall 695（+0.8%）（OI 10.7k）
量化解读： 存量 Call 重｜ATM IV 33.0%｜历史 Rank 100%（近端代理）｜IV/RV 1.42×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,757,684 股

📆 11-24 Forward Structure
存量OI: C 87.2k / P 70.0k，今日变化ΔOI: C +27.5k / P +14.6k（新行权价 C 13.1k / P 12.0k），平值价格ATM: C $12.97 / P $9.52 ｜ ATM IV 38.5%，净 delta 敞口 83k shares
Top ΔOI: P 600 +11,328 ｜ P 740 -2,849
仓位参考: Max Pain 732 ｜ Put Wall 690（+0.0%，弱）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 38.5%｜历史 Rank 100%（近端代理）｜IV/RV 1.66×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 83,175 股

📆 11-25 Forward Structure
存量OI: C 86.0k / P 61.3k，今日变化ΔOI: C +16.9k / P +21.0k（新行权价 C 27.2k / P 1.9k），平值价格ATM: C $14.68 / P $11.29 ｜ ATM IV 39.5%，净 delta 敞口 -1.5M shares
Top ΔOI: P 734 +11,405 ｜ P 715 +3,003 ｜ C 759 +1,297
仓位参考: Max Pain 730 ｜ Call Wall 704（+2.1%，弱）（OI 2.1k） ｜ Put Wall 680（-1.4%，弱）（OI 4.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 39.5%｜历史 Rank 100%（近端代理）｜IV/RV 1.70×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,487,096 股

11-27（MEDIUM △）Top ΔOI: 755P -5,456
11-27（MEDIUM △）仓位参考: Max Pain 737 ｜ Put Wall 700（+1.5%，弱）（OI 59.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/SPY_evening.json