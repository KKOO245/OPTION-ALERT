# 期权晚报 2026-10-23（快照 16:40 ET）

📊 市场环境

SPY $759.97 ｜ QQQ $704.40
VIX 19.45 ↑2.2%（5D -2.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 21.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 200P ΔOI -213（距现价 +3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 203.01 → 收盘 193.30（-4.8%） ｜ 今日高 205.99 ｜ 低 189.00 ｜ 昨收 217.77 → 收盘 193.30（-11.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-30，窗口结束前不做对错判定）

Options: P/C成交量 0.66 | OI比 0.77 | ATM IV 129.8% | Skew 23.5pp | Term 0.62 | ExpMove ±9.5%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.62，近月 IV 高于远月）｜保护溢价显著（Skew 23.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.77）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（7D）±9.5% ｜ 11-06（14D）±13.4% ｜ 11-13（21D）±15.5% ｜ 11-20（28D）±17.5%
   ⇒ IV–VIX Spread: +110.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -14,154,389 | GEX Change vs 上次快照 -517,219 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 495 / LOW 94 / INVALID 315
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 200（弱结构｜现价低于该位 3.3%）
最近结构参考: Put Wall 200（现价低于该位 3.3%）
量化视角： 负 Gamma（1415万，无历史分位）｜负 Gamma 加深（52万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 200（Put Wall，弱结构） / 230（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +13.3k / P +3.8k ｜ Activity HIGH ｜ 7D
11-06  C +2.3k / P +0.6k ｜ Activity HIGH ｜ 14D
11-13  C +0.2k / P -0.3k ｜ Activity MEDIUM △ ｜ 21D
11-20  C +2.2k / P +1.9k ｜ Activity MEDIUM △ ｜ 28D

📆 10-30 Forward Structure
存量OI: C 34.7k / P 31.8k，今日变化ΔOI: C +13.3k / P +3.8k，平值价格ATM: C $9.51 / P $8.80 ｜ ATM IV 86.0%，净 delta 敞口 55k shares
Top ΔOI: C 220 +2,599 ｜ C 217 +2,014 ｜ C 230 +735
仓位参考: Max Pain 230 ｜ Call Wall 210（+8.6%，弱）（OI 0.8k） ｜ Put Wall 190（-1.7%，弱）（OI 1.8k）
量化解读： 存量两侧均衡｜ATM IV 86.0%｜历史 Rank 82%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 54,987 股

📆 11-06 Forward Structure
存量OI: C 11.0k / P 12.4k，今日变化ΔOI: C +2.3k / P +0.6k，平值价格ATM: C $13.88 / P $11.95 ｜ ATM IV 83.0%，净 delta 敞口 -10k shares
Top ΔOI: C 210 +210
仓位参考: Max Pain 250 ｜ Put Wall 200（+3.5%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 83.0%｜历史 Rank 82%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 10,310 股

11-13（MEDIUM △）Top ΔOI: 230P -432 ｜ 200P -213
11-13（MEDIUM △）仓位参考: Max Pain 250 ｜ Put Wall 200（+3.5%，弱）（OI 0.5k）

11-20（MEDIUM △）Top ΔOI: 190P +587 ｜ 240C -447
11-20（MEDIUM △）仓位参考: Max Pain 240 ｜ Call Wall 180（-6.9%，弱）（OI 1.2k） ｜ Put Wall 200（+3.5%，弱）（OI 5.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/BE_evening.json