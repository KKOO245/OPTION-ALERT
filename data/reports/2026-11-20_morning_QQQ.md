# 期权晨报 2026-11-20（快照 10:20 ET）

📊 市场环境

SPY $709.06 ｜ QQQ $630.13
VIX 27.48 ↓3.4%（5D +42.4%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-23 660C ΔOI +4,401（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-24 560P ΔOI +11,313 占该期限总 OI 10.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 645.04 → 今开 638.81（-1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 643.28 ｜ 低 632.27

Options: P/C成交量 0.97 | OI比 0.72 | ATM IV 18.6% | Skew -21.4pp | Term 1.78 | ExpMove N/A | Rank 49%
量化视角： IV 中性（Rank 49%）｜期限结构正常偏陡（Term 1.78）｜Put 保护异常便宜（Skew -21.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.97×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 16% ｜ P/C OI(近端) 1%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 16%）｜近端持仓极端 Call 重（P/C OI 分位 1%，历史极低区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-27（7D）±4.4%
   ⇒ IV–VIX Spread: -8.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -601,446,737 | GEX Change vs 上次快照 120,524,158 | Flip: Primary Flip: 645.10（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 2786 / LOW 354 / INVALID 443
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 645.10（全链重定价，覆盖 98%）
最近结构参考: Flip 645（现价低于该位 1.7%）
量化视角： 负 Gamma（6.01亿，历史分位偏负区，比 84% 的交易日更负）｜负 Gamma 缓解（+1.21亿）｜现价位于 Flip 下方 1.70%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 670（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 645（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 720.0C — Vol 47 | 最新价 $1.66 | OI 80989→96286 (ΔOI +15297张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增15297张（+18.9% vs前日OI），值得跟踪（方向未知）
12-18 710.0C — Vol 38 | 最新价 $2.61 | OI 49618→62565 (ΔOI +12947张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12947张（+26.1% vs前日OI），连续性待观察（方向未知）
11-20 630.0P — Vol 1,420 | 最新价 $2.38 | OI 23022→35038 (ΔOI +12016张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12016张（+52.2% vs前日OI），连续性待观察（方向未知）
11-24 560.0P — Vol 6 | 最新价 $0.30 | OI 300→11613 (ΔOI +11313张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11313张（+3771.0% vs前日OI），连续性待观察（方向未知）
11-20 690.0C — Vol 51 | 最新价 $0.06 | OI 20801→31710 (ΔOI +10909张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10909张（+52.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 62,482 张（Put 23,329 / Call 39,153），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 1360.4k / P 976.9k，今日成交量: C 443.9k / P 430.7k，平值价格ATM: C N/A / P $2.41 ｜ ATM IV 18.6%，Max Pain 670
Top ΔOI: P 680 -32,243 ｜ P 700 -29,614 ｜ P 690 -21,730

📆 Forward Expiration Structure

11-23  C +24.2k / P +49.3k ｜ Activity HIGH ｜ 3D
11-24  C +7.1k / P +30.8k ｜ Activity HIGH ｜ 4D
11-25  C +12.8k / P +11.2k ｜ Activity HIGH ｜ 5D
11-27  C +21.2k / P +16.0k ｜ Activity HIGH ｜ 7D

📆 11-23 Forward Structure
存量OI: C 76.6k / P 91.9k，今日变化ΔOI: C +24.2k / P +49.3k，ATM IV 22.3%，净 delta 敞口 -982k shares
Top ΔOI: P 600 +8,551 ｜ C 660 +4,401
仓位参考: Max Pain 660 ｜ Put Wall 645（+1.7%，弱）（OI 7.3k）
量化解读： 存量 Put 重｜ATM IV 22.3%｜历史 Rank 49%（近端代理）｜IV/RV 0.64×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 981,634 股

📆 11-24 Forward Structure
存量OI: C 39.6k / P 68.0k，今日变化ΔOI: C +7.1k / P +30.8k，ATM IV 25.7%，净 delta 敞口 -230k shares
Top ΔOI: P 560 +11,313 ｜ P 540 +7,832 ｜ P 565 +6,035
仓位参考: Max Pain 665
量化解读： 存量 Put 重｜ATM IV 25.7%｜历史 Rank 49%（近端代理）｜IV/RV 0.74×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 229,620 股

📆 11-25 Forward Structure
存量OI: C 53.4k / P 34.4k，今日变化ΔOI: C +12.8k / P +11.2k，ATM IV 27.3%，净 delta 敞口 -272k shares
Top ΔOI: P 565 +4,059 ｜ C 680 +3,499 ｜ C 690 +2,525
仓位参考: Max Pain 665 ｜ Put Wall 635（+0.1%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 27.3%｜历史 Rank 49%（近端代理）｜IV/RV 0.79×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 272,219 股

📆 11-27 Forward Structure
存量OI: C 191.4k / P 141.5k，今日变化ΔOI: C +21.2k / P +16.0k，平值价格ATM: C $17.46 / P $10.17 ｜ ATM IV 36.0%，净 delta 敞口 -247k shares
Top ΔOI: C 660 +4,644 ｜ P 654 +3,979 ｜ C 670 +2,138
仓位参考: Max Pain 670 ｜ Put Wall 640（+0.9%，弱）（OI 13.1k）
量化解读： 存量 Call 重｜ATM IV 36.0%｜历史 Rank 49%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 负 246,736 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/QQQ_morning.json