# 期权晨报 2026-11-20（快照 10:20 ET）

📊 市场环境

SPY $708.79 ｜ QQQ $629.60
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
🟡 **近现价集中开仓**: 11-23 260P ΔOI +6,801（距现价 -1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-25 261P ΔOI +7,101 占该期限总 OI 14.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 264.22 → 今开 263.32（-0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 265.85 ｜ 低 262.62

Options: P/C成交量 1.11 | OI比 1.93 | ATM IV 24.1% | Skew -10.2pp | Term 1.03 | ExpMove ±1.0% | Rank 41%
量化视角： IV 中性（Rank 41%）｜期限结构正常（Term 1.03）｜Put 保护异常便宜（Skew -10.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.11×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.93×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-27（7D）±2.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,449,190,092 | GEX Change vs 上次快照 -93,555,448 | Flip: Primary Flip: 274.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 917 / LOW 240 / INVALID 135
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 274.90（全链重定价，覆盖 94%）
Put Wall 270（弱结构｜现价低于该位 2.4%）
最近结构参考: Put Wall 270（现价低于该位 2.4%）
量化视角： 负 Gamma（24.49亿，无历史分位）｜负 Gamma 加深（9356万）｜现价位于 Flip 下方 4.10%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 270（Put Wall，弱结构） / 272（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 275（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 255.0P — Vol 67,629 | 最新价 $4.59 | OI 54841→85555 (ΔOI +30714张) | ΔOI/Volume 45.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30714张（+56.0% vs前日OI），连续性待观察（方向未知）
12-18 251.0P — Vol 31,179 | 最新价 $3.64 | OI 10278→38885 (ΔOI +28607张) | ΔOI/Volume 91.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增28607张（+278.3% vs前日OI），连续性待观察（方向未知）
12-18 252.0P — Vol 53,750 | 最新价 $3.88 | OI 3334→28210 (ΔOI +24876张) | ΔOI/Volume 46.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24876张（+746.1% vs前日OI），连续性待观察（方向未知）
12-18 256.0P — Vol 34,377 | 最新价 $4.89 | OI 27191→38552 (ΔOI +11361张) | ΔOI/Volume 33.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11361张（+41.8% vs前日OI），连续性待观察（方向未知）
12-18 253.0P — Vol 25,762 | 最新价 $4.11 | OI 11682→20363 (ΔOI +8681张) | ΔOI/Volume 33.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8681张（+74.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 104,239 张（Put 104,239 / Call 0），跨 1 个期限｜近端保护（5 档，距现价 ≤5%，权利金合计约 $43M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 606.6k / P 1169.8k，今日成交量: C 120.1k / P 133.6k，平值价格ATM: C $1.67 / P $1.00 ｜ ATM IV 24.1%，预期波动 ±1.0%，Max Pain 272
Top ΔOI: P 263 -51,779 ｜ P 261 -34,648 ｜ P 275 -22,791

📆 Forward Expiration Structure

11-23  C +7.6k / P +16.4k ｜ Activity HIGH ｜ 3D
11-24  C +1.4k / P -0.6k ｜ Activity MEDIUM △ ｜ 4D
11-25  C +2.4k / P +20.3k ｜ Activity HIGH ｜ 5D
11-27  C +6.8k / P +6.6k ｜ Activity MEDIUM △ ｜ 7D

📆 11-23 Forward Structure
存量OI: C 31.0k / P 44.5k，今日变化ΔOI: C +7.6k / P +16.4k，ATM IV 16.4%，净 delta 敞口 -165k shares
Top ΔOI: P 260 +6,801 ｜ C 272 +5,439 ｜ P 255 +4,404
仓位参考: Max Pain 270 ｜ Call Wall 272（+3.2%）（OI 5.9k） ｜ Put Wall 270（+2.4%）（OI 12.2k）
量化解读： 存量 Put 重｜ATM IV 16.4%｜历史 Rank 41%（近端代理）｜IV/RV 0.63×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 165,047 股

11-24（MEDIUM △）Top ΔOI: 270C +383 ｜ 277P -328
11-24（MEDIUM △）仓位参考: Max Pain 272 ｜ Call Wall 275（+4.3%，弱）（OI 1.2k） ｜ Put Wall 270（+2.4%，弱）（OI 1.8k）

📆 11-25 Forward Structure
存量OI: C 13.9k / P 35.0k，今日变化ΔOI: C +2.4k / P +20.3k，ATM IV 18.8%，净 delta 敞口 -422k shares
Top ΔOI: P 261 +7,101 ｜ P 240 +5,953 ｜ P 260 +2,535
仓位参考: Max Pain 272 ｜ Call Wall 277（+5.1%，弱）（OI 4.3k） ｜ Put Wall 261（-1.0%，弱）（OI 7.2k）
量化解读： 存量 Put 重｜ATM IV 18.8%｜历史 Rank 41%（近端代理）｜IV/RV 0.72×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 422,030 股

11-27（MEDIUM △）Top ΔOI: 254P +1,841 ｜ 245P -1,780
11-27（MEDIUM △）仓位参考: Max Pain 275 ｜ Call Wall 275（+4.3%，弱）（OI 6.5k） ｜ Put Wall 270（+2.4%，弱）（OI 35.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/IWM_morning.json