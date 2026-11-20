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


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 89.91 → 收盘 79.24（-11.9%） ｜ 今日高 90.67 ｜ 低 78.25 ｜ 昨收 755.16 → 收盘 79.24（-89.5%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-27，窗口结束前不做对错判定）

Options: P/C成交量 1.49 | OI比 0.51 | ATM IV 157.2% | Skew 15.6pp | Term 0.77 | ExpMove ±15.4%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价显著（Skew 15.6pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.51）+ 当日成交偏 Put（P/C量 1.49）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.49×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（7D）±15.4% ｜ 12-04（14D）±21.2% ｜ 12-11（21D）±24.0% ｜ 12-18（28D）±27.1%
   ⇒ IV–VIX Spread: +121.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,990,240 | GEX Change vs 上次快照 -5,133,183 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 83%（带内） ｜ IV 有效性: VALID 793 / LOW 946 / INVALID 5195
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 75（现价高于该位 5.7%）
最近结构参考: Put Wall 75（现价高于该位 5.7%）
量化视角： 负 Gamma（599万，无历史分位）｜负 Gamma 加深（513万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 75（Put Wall）；上方 106（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 2560.0P — Vol 1 | 最新价 $978.80 | OI 0→53 (ΔOI +53张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增53张（量数据缺失），以日内换手为主
12-18 2080.0P — Vol 2 | 最新价 $484.80 | OI 1→33 (ΔOI +32张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增32张（+3200.0% vs前日OI），值得跟踪（方向未知）
12-18 2380.0P — Vol 1 | 最新价 $1240.00 | OI 0→27 (ΔOI +27张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增27张（量数据缺失），以日内换手为主
12-18 2260.0P — Vol 1 | 最新价 $523.00 | OI 0→26 (ΔOI +26张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增26张（量数据缺失），以日内换手为主
量化视角： 4 个事件合计 ΔOI ≈ 138 张（Put 138 / Call 0），跨 1 个期限｜有实质成本保护 4 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C -27.6k / P -13.6k ｜ Activity HIGH ｜ 7D（新行权价 C 29.2k / P 12.7k）
12-04  C -13.1k / P -7.1k ｜ Activity HIGH ｜ 14D（新行权价 C 12.7k / P 7.6k）
12-11  C -6.5k / P -4.0k ｜ Activity HIGH ｜ 21D（新行权价 C 6.2k / P 4.1k）
12-18  C -49.5k / P -48.0k ｜ Activity HIGH ｜ 28D（新行权价 C 50.7k / P 51.5k）

📆 11-27 Forward Structure
存量OI: C 29.2k / P 12.7k，今日变化ΔOI: C -27.6k / P -13.6k（新行权价 C 29.2k / P 12.7k），平值价格ATM: C $6.00 / P $6.20 ｜ ATM IV 141.6%，净 delta 敞口 0 shares
Top ΔOI: C 800 -2,121
仓位参考: Max Pain 101 ｜ Put Wall 81.25（+2.5%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 141.6%｜历史 Rank 93%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

📆 12-04 Forward Structure
存量OI: C 12.7k / P 7.6k，今日变化ΔOI: C -13.1k / P -7.1k（新行权价 C 12.7k / P 7.6k），平值价格ATM: C $8.54 / P $8.30 ｜ ATM IV 134.4%，净 delta 敞口 0 shares
Top ΔOI: C 1200 -599 ｜ P 820 -392
仓位参考: Max Pain 109 ｜ Put Wall 75（-5.4%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 134.4%｜历史 Rank 93%（近端代理）｜IV/RV 1.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

📆 12-11 Forward Structure
存量OI: C 6.2k / P 4.1k，今日变化ΔOI: C -6.5k / P -4.0k（新行权价 C 6.2k / P 4.1k），平值价格ATM: C $10.00 / P $8.99 ｜ ATM IV 129.8%，净 delta 敞口 0 shares
Top ΔOI: P 480 -272 ｜ P 830 -272
仓位参考: Max Pain 109 ｜ Put Wall 85（+7.3%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 129.8%｜历史 Rank 93%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

📆 12-18 Forward Structure
存量OI: C 69.9k / P 69.6k，今日变化ΔOI: C -49.5k / P -48.0k（新行权价 C 50.7k / P 51.5k），平值价格ATM: C $10.90 / P $10.60 ｜ ATM IV 120.6%，净 delta 敞口 579k shares
Top ΔOI: P 75 +7,983 ｜ P 600 -5,997 ｜ P 700 -3,174
仓位参考: Max Pain 124 ｜ Put Wall 75（-5.4%）（OI 8.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 120.6%｜历史 Rank 93%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 正 578,695 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/SNDK_evening.json