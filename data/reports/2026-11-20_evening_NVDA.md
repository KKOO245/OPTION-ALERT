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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 143.57 → 收盘 125.53（-12.6%） ｜ 今日高 143.73 ｜ 低 124.51 ｜ 昨收 145.98 → 收盘 125.53（-14.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-25，窗口结束前不做对错判定）

Options: P/C成交量 1.15 | OI比 0.46 | ATM IV 163.3% | Skew 6.8pp | Term 0.49 | ExpMove ±8.0%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.49，近月 IV 高于远月）｜保护溢价显著（Skew 6.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.15×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-23（3D）±8.0% ｜ 11-25（5D）±11.7% ｜ 11-27（7D）±12.4% ｜ 11-30（10D）±13.3%
   ⇒ IV–VIX Spread: +127.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -82,061,258 | GEX Change vs 上次快照 116,351,725 | Flip: Primary Flip: 140.08（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 1029 / LOW 245 / INVALID 1032
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 140.08（全链重定价，覆盖 86%）
最近结构参考: Flip 140（现价低于该位 10.4%）
量化视角： 负 Gamma（8206万，无历史分位）｜负 Gamma 缓解（+1.16亿）｜现价位于 Flip 下方 10.39%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 160（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 140（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 2280.0C — Vol 170 | 最新价 $165.00 | OI 0→4395 (ΔOI +4395张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增4395张（前日OI缺失），值得跟踪（方向未知）
12-18 1300.0C — Vol 25 | 最新价 $385.00 | OI 0→3764 (ΔOI +3764张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增3764张（前日OI缺失），值得跟踪（方向未知）
12-18 1640.0C — Vol 5 | 最新价 $280.00 | OI 0→3193 (ΔOI +3193张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增3193张（前日OI缺失），值得跟踪（方向未知）
12-18 650.0P — Vol 4 | 最新价 $60.60 | OI 0→2038 (ΔOI +2038张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增2038张（前日OI缺失），值得跟踪（方向未知）
12-18 1940.0C — Vol 5 | 最新价 $217.00 | OI 0→1895 (ΔOI +1895张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增1895张（前日OI缺失），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 15,285 张（Put 2,038 / Call 13,247），跨 1 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-23  C +30.0k / P +5.8k ｜ Activity HIGH ｜ 3D（新行权价 C 12 / P 3）
11-25  C +15.1k / P +5.8k ｜ Activity HIGH ｜ 5D（新行权价 C 0.3k / P 36）
11-27  C +74.3k / P +10.6k ｜ Activity HIGH ｜ 7D（新行权价 C 3.4k / P 7.1k）
11-30  C N/A / P N/A ｜ Activity LOW ｜ 10D（新上架）

📆 11-23 Forward Structure
存量OI: C 103.8k / P 48.1k，今日变化ΔOI: C +30.0k / P +5.8k（新行权价 C 12 / P 3），平值价格ATM: C $5.00 / P $5.05 ｜ ATM IV 109.0%，净 delta 敞口 -333k shares
仓位参考: Max Pain 152 ｜ Put Wall 135（+7.5%，弱）（OI 5.3k）
量化解读： 存量 Call 重｜ATM IV 109.0%｜历史 Rank 100%（近端代理）｜IV/RV 2.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 332,682 股

📆 11-25 Forward Structure
存量OI: C 58.9k / P 25.6k，今日变化ΔOI: C +15.1k / P +5.8k（新行权价 C 0.3k / P 36），平值价格ATM: C $7.08 / P $7.55 ｜ ATM IV 122.1%，净 delta 敞口 -312k shares
Top ΔOI: C 160 +4,260 ｜ C 155 +3,632 ｜ P 140 +1,907
仓位参考: Max Pain 152 ｜ Put Wall 125（-0.4%，弱）（OI 3.9k）
量化解读： 存量 Call 重｜ATM IV 122.1%｜历史 Rank 100%（近端代理）｜IV/RV 2.50×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 312,162 股

📆 11-27 Forward Structure
存量OI: C 373.6k / P 186.8k，今日变化ΔOI: C +74.3k / P +10.6k（新行权价 C 3.4k / P 7.1k），平值价格ATM: C $7.85 / P $7.69 ｜ ATM IV 112.5%，净 delta 敞口 1.9M shares
Top ΔOI: C 160 +14,871 ｜ C 167 +14,078 ｜ C 162 +13,129
仓位参考: Max Pain 160 ｜ Put Wall 125（-0.4%，弱）（OI 6.5k）
量化解读： 存量 Call 重｜ATM IV 112.5%｜历史 Rank 100%（近端代理）｜IV/RV 2.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,858,414 股

11-30（Activity LOW）仓位参考: Max Pain 152 ｜ Put Wall 125（-0.4%）（OI 5.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/NVDA_evening.json