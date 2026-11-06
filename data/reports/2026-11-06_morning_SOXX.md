# 期权晨报 2026-11-06（快照 10:20 ET）

📊 市场环境

SPY $740.12 ｜ QQQ $660.13
VIX 24.90 ↓11.6%（5D +28.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
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
🔵 **期限 OI 集中**: 11-13 110P ΔOI +34,313 占该期限总 OI 14.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 131.90 → 今开 139.36（+5.7%） | 较昨收变动（含盘初走势） ｜ 今日高 140.21 ｜ 低 136.10

Options: P/C成交量 3.14 | OI比 2.38 | ATM IV 120.9% | Skew 10.0pp | Term 0.50 | ExpMove ±8.0%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.50，近月 IV 高于远月）｜保护溢价显著（Skew 10.0pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 3.14）——观察点，非方向信号
   ⇒ Put/Call Volume: 3.14×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.38×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-13（7D）±8.0% ｜ 11-20（14D）±9.7% ｜ 11-27（21D）±12.5% ｜ 12-04（28D）±12.7%
   ⇒ IV–VIX Spread: +96.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -91,555,190 | GEX Change vs 上次快照 -66,945,550 | Flip: Primary Flip: 155.86（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 81%（带内） ｜ IV 有效性: VALID 395 / LOW 427 / INVALID 2228
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 155.86（全链重定价，覆盖 81%）
最近结构参考: Flip 156（现价低于该位 11.5%）
量化视角： 负 Gamma（9156万，无历史分位）｜负 Gamma 加深（6695万）｜现价位于 Flip 下方 11.50%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 151（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 156（全链重定价，覆盖 81%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 110.0P — Vol 173,158 | 最新价 $0.15 | OI 751→170710 (ΔOI +169959张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增169959张（+22631.0% vs前日OI），连续性待观察（方向未知）
11-06 120.0P — Vol 174,284 | 最新价 $0.60 | OI 38096→78096 (ΔOI +40000张) | ΔOI/Volume 22.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增40000张（+105.0% vs前日OI），连续性待观察（方向未知）
11-20 120.0P — Vol 41,504 | 最新价 $3.30 | OI 277→39004 (ΔOI +38727张) | ΔOI/Volume 93.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增38727张（+13980.9% vs前日OI），连续性待观察（方向未知）
11-20 105.0P — Vol 38,436 | 最新价 $1.25 | OI 9→38180 (ΔOI +38171张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增38171张（+424122.2% vs前日OI），连续性待观察（方向未知）
11-13 110.0P — Vol 17,354 | 最新价 $0.90 | OI 0→34313 (ΔOI +34313张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增34313张（前日OI缺失），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 321,170 张（Put 321,170 / Call 0），跨 3 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 140.9k / P 335.8k，今日成交量: C 4.1k / P 12.7k，平值价格ATM: C $1.70 / P $1.93 ｜ ATM IV 120.9%，预期波动 ±2.6%，Max Pain 151
Top ΔOI: P 110 +169,959 ｜ P 120 +40,000 ｜ C 183 +32,826

📆 Forward Expiration Structure

11-13  C +70.4k / P +102.6k ｜ Activity HIGH ｜ 7D
11-20  C +119.1k / P +248.7k ｜ Activity HIGH ｜ 14D
11-27  C +17.6k / P +15.0k ｜ Activity HIGH ｜ 21D
12-04  C +2.9k / P +5.2k ｜ Activity HIGH ｜ 28D

📆 11-13 Forward Structure
存量OI: C 103.0k / P 127.8k，今日变化ΔOI: C +70.4k / P +102.6k，平值价格ATM: C $5.60 / P $5.44 ｜ ATM IV 70.0%，净 delta 敞口 -3.1M shares
Top ΔOI: P 110 +34,313 ｜ P 125 +25,570 ｜ C 163 +19,349
仓位参考: Max Pain 153 ｜ Put Wall 138.33（+0.3%，弱）（OI 15.0k）
量化解读： 存量 Put 重｜ATM IV 70.0%｜历史 Rank 100%（近端代理）｜IV/RV 0.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,061,626 股

📆 11-20 Forward Structure
存量OI: C 177.3k / P 327.7k，今日变化ΔOI: C +119.1k / P +248.7k，平值价格ATM: C $6.60 / P $6.80 ｜ ATM IV 64.3%，净 delta 敞口 -10.3M shares
Top ΔOI: P 120 +38,727 ｜ P 105 +38,171 ｜ C 166 +22,662
仓位参考: Max Pain 165 ｜ Put Wall 133.33（-3.3%，弱）（OI 28.6k）
量化解读： 存量 Put 重｜ATM IV 64.3%｜历史 Rank 100%（近端代理）｜IV/RV 0.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 10,251,176 股

📆 11-27 Forward Structure
存量OI: C 25.9k / P 22.8k，今日变化ΔOI: C +17.6k / P +15.0k，平值价格ATM: C $7.60 / P $9.70 ｜ ATM IV 60.2%，净 delta 敞口 -860k shares
Top ΔOI: C 161 +6,893 ｜ C 183 +3,447 ｜ P 166 +2,704
仓位参考: Max Pain 162 ｜ Put Wall 146.67（+6.3%，弱）（OI 3.2k）
量化解读： 存量两侧均衡｜ATM IV 60.2%｜历史 Rank 100%（近端代理）｜IV/RV 0.14×（近似）｜净 delta 敞口 负 859,626 股

📆 12-04 Forward Structure
存量OI: C 4.1k / P 7.5k，今日变化ΔOI: C +2.9k / P +5.2k，平值价格ATM: C $9.05 / P $8.47 ｜ ATM IV 60.8%，净 delta 敞口 -274k shares
Top ΔOI: P 166 +816 ｜ P 148 +618 ｜ P 150 +600
仓位参考: Max Pain 164 ｜ Call Wall 141.67（+2.7%，弱）（OI 99） ｜ Put Wall 140（+1.5%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜ATM IV 60.8%｜历史 Rank 100%（近端代理）｜IV/RV 0.14×（近似）｜净 delta 敞口 负 273,613 股

📅 事件差分（观察，非因果）: 11-13（7D）ATM IV 70.0% vs 11-20 64.3%（差 +5.7pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/SOXX_morning.json