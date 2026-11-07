# 期权晨报 2026-11-06（快照 10:20 ET）

📊 市场环境

SPY $735.29 ｜ QQQ $656.10
VIX 24.90 ↓11.6%（5D +28.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 22.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 165 ｜ 前值 60　✅ 今日已公布
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 4.1 ｜ 前值 4.2　✅ 今日已公布
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 51 ｜ 前值 46.3　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-09 350C ΔOI +1,582（距现价 -1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 343.69 → 今开 348.92（+1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 361.26 ｜ 低 347.60

Options: P/C成交量 0.38 | OI比 1.20 | ATM IV 97.4% | Skew 4.9pp | Term 0.53 | ExpMove ±3.9%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.53，近月 IV 高于远月）｜保护溢价中性（Skew 4.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.20×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-09（3D）±3.9% ｜ 11-11（5D）±5.4% ｜ 11-13（7D）±6.6% ｜ 11-16（10D）±7.1%
   ⇒ IV–VIX Spread: +72.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 19,086,170 | GEX Change vs 上次快照 80,782,408 | Flip: Primary Flip: 351.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1408 / LOW 172 / INVALID 970
结构观察区: Primary Flip 351.27（全链重定价，覆盖 99%）
最近结构参考: Flip 351（现价高于该位 1.4%）
量化视角： 正 Gamma（1909万，无历史分位）｜由负转正（+8078万）｜现价位于 Flip 上方 1.43%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 360（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 351（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 377.5C — Vol 9,720 | 最新价 $2.62 | OI 221→7368 (ΔOI +7147张) | ΔOI/Volume 73.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7147张（+3233.9% vs前日OI），连续性待观察（方向未知）
11-06 370.0C — Vol 55,404 | 最新价 $0.49 | OI 1876→8019 (ΔOI +6143张) | ΔOI/Volume 11.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6143张（+327.4% vs前日OI），连续性待观察（方向未知）
11-06 360.0C — Vol 57,834 | 最新价 $1.50 | OI 599→6496 (ΔOI +5897张) | ΔOI/Volume 10.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5897张（+984.5% vs前日OI），连续性待观察（方向未知）
11-06 200.0P — Vol 13,833 | 最新价 $0.03 | OI 1013→6038 (ΔOI +5025张) | ΔOI/Volume 36.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5025张（+496.1% vs前日OI），连续性待观察（方向未知）
11-06 345.0P — Vol 36,712 | 最新价 $7.80 | OI 1464→6367 (ΔOI +4903张) | ΔOI/Volume 13.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4903张（+334.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 29,115 张（Put 9,928 / Call 19,187），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 231.9k / P 278.0k，今日成交量: C 236.6k / P 103.7k，平值价格ATM: C $3.28 / P $4.25 ｜ ATM IV 97.4%，预期波动 ±2.1%，Max Pain 360
Top ΔOI: C 370 +6,143 ｜ C 360 +5,897 ｜ P 200 +5,025

📆 Forward Expiration Structure

11-09  C +18.3k / P +11.7k ｜ Activity HIGH ｜ 3D
11-11  C +12.0k / P +8.0k ｜ Activity HIGH ｜ 5D
11-13  C +32.1k / P +16.4k ｜ Activity HIGH ｜ 7D
11-16  C +5.2k / P +2.8k ｜ Activity HIGH ｜ 10D

📆 11-09 Forward Structure
存量OI: C 46.5k / P 35.2k，今日变化ΔOI: C +18.3k / P +11.7k，平值价格ATM: C $6.35 / P $7.57 ｜ ATM IV 50.4%，净 delta 敞口 733k shares
Top ΔOI: C 380 +2,772 ｜ C 350 +1,582
仓位参考: Max Pain 368 ｜ Call Wall 380（+6.7%，弱）（OI 3.0k） ｜ Put Wall 380（+6.7%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 50.4%｜历史 Rank 96%（近端代理）｜IV/RV 0.94×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 732,519 股

📆 11-11 Forward Structure
存量OI: C 26.6k / P 18.7k，今日变化ΔOI: C +12.0k / P +8.0k，平值价格ATM: C $9.00 / P $10.37 ｜ ATM IV 57.1%，净 delta 敞口 238k shares
Top ΔOI: C 400 +1,287 ｜ C 372 +1,140 ｜ P 300 +911
仓位参考: Max Pain 370 ｜ Call Wall 390（+9.5%，弱）（OI 1.7k） ｜ Put Wall 355（-0.4%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 57.1%｜历史 Rank 96%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 238,497 股

📆 11-13 Forward Structure
存量OI: C 88.7k / P 59.7k，今日变化ΔOI: C +32.1k / P +16.4k，平值价格ATM: C $11.40 / P $12.27 ｜ ATM IV 58.6%，净 delta 敞口 1.2M shares
Top ΔOI: C 377 +7,147 ｜ C 350 +4,887 ｜ C 362 +4,321
仓位参考: Max Pain 360 ｜ Call Wall 377.5（+6.0%，弱）（OI 7.4k） ｜ Put Wall 325（-8.8%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 58.6%｜历史 Rank 96%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,184,150 股

📆 11-16 Forward Structure
存量OI: C 9.2k / P 4.9k，今日变化ΔOI: C +5.2k / P +2.8k，平值价格ATM: C $12.20 / P $13.10 ｜ ATM IV 53.5%，净 delta 敞口 55k shares
Top ΔOI: P 300 +573 ｜ C 380 +448
仓位参考: Max Pain 370 ｜ Call Wall 380（+6.7%，弱）（OI 0.5k） ｜ Put Wall 380（+6.7%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 53.5%｜历史 Rank 96%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 正 54,588 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/TSLA_morning.json