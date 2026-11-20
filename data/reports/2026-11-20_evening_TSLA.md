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
🟡 **近现价集中开仓**: 11-23 342P ΔOI +703（距现价 -1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 370.22 → 收盘 345.82（-6.6%） ｜ 今日高 373.88 ｜ 低 344.33 ｜ 昨收 374.41 → 收盘 345.82（-7.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-25，窗口结束前不做对错判定）

Options: P/C成交量 0.94 | OI比 1.41 | ATM IV 107.1% | Skew 12.2pp | Term 0.60 | ExpMove ±4.9%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.60，近月 IV 高于远月）｜保护溢价显著（Skew 12.2pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.94×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.41×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-23（3D）±4.9% ｜ 11-25（5D）±7.1% ｜ 11-27（7D）±0.0% ｜ 11-30（10D）±8.6%
   ⇒ IV–VIX Spread: +71.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -33,844,475 | GEX Change vs 上次快照 19,866,631 | Flip: Primary Flip: 364.59（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 1109 / LOW 258 / INVALID 1189
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 364.59（全链重定价，覆盖 86%）
最近结构参考: Flip 365（现价低于该位 5.1%）
量化视角： 负 Gamma（3384万，无历史分位）｜负 Gamma 缓解（+1987万）｜现价位于 Flip 下方 5.15%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 375（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 365（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 105.0C — Vol 8 | 最新价 $268.05 | OI 4913→4921 (ΔOI +8张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增8张（+0.2% vs前日OI），值得跟踪（方向未知）
量化视角： 1 个事件合计 ΔOI ≈ 8 张（Put 0 / Call 8），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-23  C +6.1k / P +4.1k ｜ Activity HIGH ｜ 3D（新行权价 C 0.1k / P 3.5k）
11-25  C +2.9k / P +1.8k ｜ Activity HIGH ｜ 5D（新行权价 C 79 / P 0.2k）
11-27  C +21.7k / P +6.0k ｜ Activity HIGH ｜ 7D（新行权价 C 11）
11-30  C N/A / P N/A ｜ Activity LOW ｜ 10D（新上架）

📆 11-23 Forward Structure
存量OI: C 32.4k / P 21.1k，今日变化ΔOI: C +6.1k / P +4.1k（新行权价 C 0.1k / P 3.5k），平值价格ATM: C $9.10 / P $7.75 ｜ ATM IV 67.0%，净 delta 敞口 -207k shares
Top ΔOI: P 342 +703
仓位参考: Max Pain 380 ｜ Put Wall 312.5（-9.6%）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 67.0%｜历史 Rank 97%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 206,532 股

📆 11-25 Forward Structure
存量OI: C 8.0k / P 9.2k，今日变化ΔOI: C +2.9k / P +1.8k（新行权价 C 79 / P 0.2k），平值价格ATM: C $12.48 / P $12.20 ｜ ATM IV 74.7%，净 delta 敞口 -75k shares
Top ΔOI: P 330 +393
仓位参考: Max Pain 385 ｜ Call Wall 380（+9.9%，弱）（OI 0.3k） ｜ Put Wall 320（-7.5%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 74.7%｜历史 Rank 97%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 75,262 股

📆 11-27 Forward Structure
存量OI: C 87.2k / P 66.4k，今日变化ΔOI: C +21.7k / P +6.0k（新行权价 C 11），平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 0.0%，净 delta 敞口 57k shares
Top ΔOI: C 380 +4,390 ｜ C 390 +4,304 ｜ C 395 +4,238
仓位参考: Max Pain 375 ｜ Call Wall 380（+9.9%，弱）（OI 5.7k） ｜ Put Wall 325（-6.0%，弱）（OI 3.5k）
量化解读： 存量 Call 重｜净 delta 敞口 正 57,045 股

11-30（Activity LOW）仓位参考: Max Pain 395 ｜ Put Wall 325（-6.0%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/TSLA_evening.json