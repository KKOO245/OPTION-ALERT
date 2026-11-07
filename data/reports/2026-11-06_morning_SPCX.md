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
🟡 **近现价集中开仓**: 11-09 130P ΔOI -2,092（距现价 -0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-09 115P ΔOI +8,326 占该期限总 OI 13.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 123.62 → 今开 131.14（+6.1%） | 较昨收变动（含盘初走势） ｜ 今日高 132.74 ｜ 低 128.57

Options: P/C成交量 0.50 | OI比 0.58 | ATM IV 116.8% | Skew 8.4pp | Term 0.53 | ExpMove ±4.7%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.53，近月 IV 高于远月）｜保护溢价显著（Skew 8.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-09（3D）±4.7% ｜ 11-11（5D）±6.8% ｜ 11-13（7D）±8.3% ｜ 11-16（10D）±9.2%
   ⇒ IV–VIX Spread: +91.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,418,813 | GEX Change vs 上次快照 68,872,245 | Flip: Primary Flip: 132.39（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 817 / LOW 181 / INVALID 582
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 132.39（全链重定价，覆盖 99%）
最近结构参考: Flip 132（现价低于该位 1.0%）
量化视角： 负 Gamma（942万，无历史分位）｜负 Gamma 缓解（+6887万）｜现价位于 Flip 下方 0.99%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 134（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 132（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 145.0C — Vol 23,745 | 最新价 $1.49 | OI 17306→34704 (ΔOI +17398张) | ΔOI/Volume 73.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17398张（+100.5% vs前日OI），连续性待观察（方向未知）
11-20 160.0C — Vol 26,204 | 最新价 $0.47 | OI 24275→40334 (ΔOI +16059张) | ΔOI/Volume 61.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16059张（+66.2% vs前日OI），连续性待观察（方向未知）
11-20 180.0C — Vol 19,657 | 最新价 $0.15 | OI 30900→44491 (ΔOI +13591张) | ΔOI/Volume 69.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13591张（+44.0% vs前日OI），连续性待观察（方向未知）
11-06 125.0C — Vol 22,578 | 最新价 $2.41 | OI 43→11093 (ΔOI +11050张) | ΔOI/Volume 48.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11050张（+25697.7% vs前日OI），连续性待观察（方向未知）
11-20 170.0C — Vol 23,356 | 最新价 $0.25 | OI 19971→29423 (ΔOI +9452张) | ΔOI/Volume 40.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9452张（+47.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 67,550 张（Put 0 / Call 67,550），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 298.1k / P 173.6k，今日成交量: C 86.9k / P 43.3k，平值价格ATM: C $1.75 / P $1.56 ｜ ATM IV 116.8%，预期波动 ±2.5%，Max Pain 134
Top ΔOI: C 125 +11,050 ｜ C 130 +7,064 ｜ P 110 +6,500

📆 Forward Expiration Structure

11-09  C +9.1k / P +14.4k ｜ Activity HIGH ｜ 3D
11-11  C +7.4k / P +5.5k ｜ Activity HIGH ｜ 5D
11-13  C +10.7k / P +6.3k ｜ Activity HIGH ｜ 7D
11-16  C +1.7k / P -89 ｜ Activity HIGH ｜ 10D

📆 11-09 Forward Structure
存量OI: C 22.4k / P 41.6k，今日变化ΔOI: C +9.1k / P +14.4k，平值价格ATM: C $3.10 / P $3.09 ｜ ATM IV 62.6%，净 delta 敞口 678k shares
Top ΔOI: P 115 +8,326 ｜ P 130 -2,092
仓位参考: Max Pain 130 ｜ Call Wall 130（-0.8%，弱）（OI 1.8k） ｜ Put Wall 120（-8.5%，弱）（OI 9.7k）
量化解读： 存量 Put 重｜ATM IV 62.6%｜历史 Rank 96%（近端代理）｜IV/RV 0.97×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 678,211 股

📆 11-11 Forward Structure
存量OI: C 14.1k / P 10.9k，今日变化ΔOI: C +7.4k / P +5.5k，平值价格ATM: C $4.43 / P $4.44 ｜ ATM IV 71.1%，净 delta 敞口 280k shares
Top ΔOI: C 127 +1,047 ｜ C 130 +980
仓位参考: Max Pain 130 ｜ Call Wall 140（+6.8%，弱）（OI 1.3k） ｜ Put Wall 120（-8.5%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 71.1%｜历史 Rank 96%（近端代理）｜IV/RV 1.10×（近似）｜净 delta 敞口 正 279,590 股

📆 11-13 Forward Structure
存量OI: C 93.3k / P 77.9k，今日变化ΔOI: C +10.7k / P +6.3k，平值价格ATM: C $5.45 / P $5.40 ｜ ATM IV 73.5%，净 delta 敞口 574k shares
Top ΔOI: P 100 +2,947 ｜ C 140 +1,882
仓位参考: Max Pain 141 ｜ Call Wall 140（+6.8%，弱）（OI 4.4k） ｜ Put Wall 125（-4.6%，弱）（OI 5.0k）
量化解读： 存量 Call 重｜ATM IV 73.5%｜历史 Rank 96%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 573,744 股

📆 11-16 Forward Structure
存量OI: C 3.2k / P 1.5k，今日变化ΔOI: C +1.7k / P -89，平值价格ATM: C $6.00 / P $6.09 ｜ ATM IV 71.4%，净 delta 敞口 122k shares
Top ΔOI: P 180 -980 ｜ C 150 +589 ｜ C 130 +357
仓位参考: Max Pain 130 ｜ Call Wall 130（-0.8%，弱）（OI 0.4k） ｜ Put Wall 130（-0.8%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 71.4%｜历史 Rank 96%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 正 121,994 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/SPCX_morning.json