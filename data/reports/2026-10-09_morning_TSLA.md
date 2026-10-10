# 期权晨报 2026-10-09（快照 10:20 ET）

📊 市场环境

SPY $778.57 ｜ QQQ $751.27
VIX 15.10 ↓2.0%（5D -1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 46.3 ｜ 前值 48.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-12 370P ΔOI +1,744（距现价 -3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 375.00 → 今开 382.38（+2.0%） | 较昨收变动（含盘初走势） ｜ 今日高 388.56 ｜ 低 381.24

Options: P/C成交量 0.43 | OI比 1.16 | ATM IV 53.6% | Skew -4.3pp | Term 0.82 | ExpMove ±2.1%（近端） | Rank 56%
量化视角： IV 中性（Rank 56%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.16×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-12（3D）±2.1% ｜ 10-14（5D）±3.3% ｜ 10-16（7D）±4.5% ｜ 10-19（10D）±4.9%
   ⇒ IV–VIX Spread: +38.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 186,248,551 | GEX Change vs 上次快照 82,456,482 | Flip: Primary Flip: 365.81（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1117 / LOW 163 / INVALID 444
结构观察区: Primary Flip 365.81（全链重定价，覆盖 99%）
Call Wall 400（现价低于该位 3.8%）
最近结构参考: Call Wall 400（现价低于该位 3.8%）
量化视角： 正 Gamma（1.86亿，无历史分位）｜正 Gamma 增强（+8246万）｜现价位于 Flip 上方 5.24%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 370（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 366（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 400.0C — Vol 21,669 | 最新价 $1.73 | OI 23269→31253 (ΔOI +7984张) | ΔOI/Volume 36.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7984张（+34.3% vs前日OI），连续性待观察（方向未知）
10-09 270.0P — Vol 14,579 | 最新价 $0.01 | OI 1330→8514 (ΔOI +7184张) | ΔOI/Volume 49.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7184张（+540.1% vs前日OI），连续性待观察（方向未知）
10-09 360.0P — Vol 32,331 | 最新价 $0.11 | OI 5568→11772 (ΔOI +6204张) | ΔOI/Volume 19.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6204张（+111.4% vs前日OI），连续性待观察（方向未知）
10-09 370.0P — Vol 113,331 | 最新价 $0.99 | OI 8562→14233 (ΔOI +5671张) | ΔOI/Volume 5.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5671张（+66.2% vs前日OI），连续性待观察（方向未知）
10-09 380.0C — Vol 65,941 | 最新价 $1.09 | OI 11133→14886 (ΔOI +3753张) | ΔOI/Volume 5.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3753张（+33.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 30,796 张（Put 19,059 / Call 11,737），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 219.8k / P 254.2k，今日成交量: C 518.5k / P 222.3k，平值价格ATM: C $2.14 / P $2.31 ｜ ATM IV 53.6%，预期波动 ±1.2%，Max Pain 370
Top ΔOI: P 270 +7,184 ｜ P 360 +6,204 ｜ P 370 +5,671

📆 Forward Expiration Structure

10-12  C +8.8k / P +5.3k ｜ Activity HIGH ｜ 3D
10-14  C +3.3k / P +3.1k ｜ Activity HIGH ｜ 5D
10-16  C +20.6k / P +4.4k ｜ Activity HIGH ｜ 7D
10-19  C +1.9k / P +1.2k ｜ Activity HIGH ｜ 10D

📆 10-12 Forward Structure
存量OI: C 31.7k / P 28.0k，今日变化ΔOI: C +8.8k / P +5.3k，平值价格ATM: C $3.89 / P $4.07 ｜ ATM IV 27.8%，净 delta 敞口 405k shares
Top ΔOI: P 370 +1,744 ｜ C 397 +1,640 ｜ C 372 +1,521
仓位参考: Max Pain 370 ｜ Call Wall 400（+3.9%，弱）（OI 3.1k） ｜ Put Wall 370（-3.9%，弱）（OI 3.1k）
量化解读： 存量两侧均衡｜ATM IV 27.8%｜历史 Rank 56%（近端代理）｜IV/RV 0.97×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 404,520 股

📆 10-14 Forward Structure
存量OI: C 11.6k / P 9.8k，今日变化ΔOI: C +3.3k / P +3.1k，平值价格ATM: C $6.25 / P $6.37 ｜ ATM IV 34.1%，净 delta 敞口 160k shares
Top ΔOI: C 375 +1,082 ｜ P 360 +472 ｜ P 350 +447
仓位参考: Max Pain 370 ｜ Call Wall 400（+3.9%，弱）（OI 1.7k） ｜ Put Wall 360（-6.5%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 34.1%｜历史 Rank 56%（近端代理）｜IV/RV 1.19×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 160,048 股

📆 10-16 Forward Structure
存量OI: C 336.4k / P 294.5k，今日变化ΔOI: C +20.6k / P +4.4k，平值价格ATM: C $8.58 / P $8.71 ｜ ATM IV 39.9%，净 delta 敞口 748k shares
Top ΔOI: C 400 +7,984 ｜ C 377 +3,292 ｜ C 390 +2,980
仓位参考: Max Pain 370 ｜ Call Wall 400（+3.9%）（OI 31.3k） ｜ Put Wall 380（-1.3%，弱）（OI 14.6k）
量化解读： 存量两侧均衡｜ATM IV 39.9%｜历史 Rank 56%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 748,226 股

📆 10-19 Forward Structure
存量OI: C 6.7k / P 3.1k，今日变化ΔOI: C +1.9k / P +1.2k，平值价格ATM: C $9.45 / P $9.25 ｜ ATM IV 36.6%，净 delta 敞口 69k shares
Top ΔOI: P 360 +266 ｜ C 375 +252 ｜ C 372 +219
仓位参考: Max Pain 375 ｜ Call Wall 400（+3.9%）（OI 1.7k） ｜ Put Wall 360（-6.5%）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 36.6%｜历史 Rank 56%（近端代理）｜IV/RV 1.28×（近似）｜净 delta 敞口 正 68,570 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/TSLA_morning.json