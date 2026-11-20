# 期权晨报 2026-11-20（快照 10:20 ET）

📊 市场环境

SPY $692.49 ｜ QQQ $608.45
VIX 27.48 ↓3.4%（5D +42.4%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 9.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 12-18 80P ΔOI +2,500（距现价 -4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 755.16 → 今开 89.91（-88.1%） | 较昨收变动（含盘初走势） ｜ 今日高 90.67 ｜ 低 83.41

Options: P/C成交量 1.16 | OI比 0.53 | ATM IV 0.0% | Skew -14.5pp | Term 107,214.60 | ExpMove ±277.9% | Rank 0%
量化视角： IV 历史低位（Rank 0%，期权偏便宜）｜期限结构正常偏陡（Term 107214.60）｜Put 保护异常便宜（Skew -14.5pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.53）+ 当日成交偏 Put（P/C量 1.16）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.16×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.53×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 12-18（28D）±1635.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -857,057 | GEX Change vs 上次快照 5,845,233 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 129 / LOW 2343 / INVALID 535
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
量化视角： 负 Gamma（86万，无历史分位）｜负 Gamma 缓解（+585万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 845（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 600.0P — Vol 3,568 | 最新价 $27.26 | OI 5997→8577 (ΔOI +2580张) | ΔOI/Volume 72.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2580张（+43.0% vs前日OI），连续性待观察（方向未知）
12-18 80.0P — Vol 2,500 | 最新价 $0.05 | OI 1710→4210 (ΔOI +2500张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2500张（+146.2% vs前日OI），连续性待观察（方向未知）
12-18 85.0P — Vol 1,500 | 最新价 $0.05 | OI 70→1554 (ΔOI +1484张) | ΔOI/Volume 98.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1484张（+2120.0% vs前日OI），连续性待观察（方向未知）
11-20 950.0C — Vol 2,479 | 最新价 $0.08 | OI 1856→2795 (ΔOI +939张) | ΔOI/Volume 37.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增939张（+50.6% vs前日OI），连续性待观察（方向未知）
11-20 900.0C — Vol 7,713 | 最新价 $0.25 | OI 2187→3117 (ΔOI +930张) | ΔOI/Volume 12.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增930张（+42.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,433 张（Put 6,564 / Call 1,869），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $7M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 106.8k / P 56.7k，今日成交量: C 67.2k / P 77.9k，平值价格ATM: C $1.45 / P $231.85 ｜ ATM IV 0.0%，预期波动 ±277.9%，Max Pain 845
Top ΔOI: P 1000 -1,357 ｜ C 950 +939 ｜ C 900 +930

📆 Forward Expiration Structure

11-27  C +4.4k / P +0.4k ｜ Activity MEDIUM △ ｜ 7D
12-04  C +1.0k / P +0.8k ｜ Activity MEDIUM △ ｜ 14D
12-11  C +0.5k / P +0.2k ｜ Activity MEDIUM △ ｜ 21D
12-18  C +0.9k / P +4.8k ｜ Activity MEDIUM △ ｜ 28D

📆 11-27 Forward Structure
存量OI: C 32.0k / P 13.9k，今日变化ΔOI: C +4.4k / P +0.4k，ATM IV 0.0%，净 delta 敞口 -37k shares
Top ΔOI: P 1150 -1,009 ｜ C 900 +411 ｜ C 880 +340
仓位参考: Max Pain 820
量化解读： 存量 Call 重｜净 delta 敞口 负 36,800 股

12-04（MEDIUM △）Top ΔOI: 1040C +398 ｜ 570P +232
12-04（MEDIUM △）仓位参考: Max Pain 875

12-11（MEDIUM △）Top ΔOI: 1000C +120 ｜ 1050C +74
12-11（MEDIUM △）仓位参考: Max Pain 865

12-18（MEDIUM △）Top ΔOI: 600P +2,580 ｜ 80P +2,500
12-18（MEDIUM △）仓位参考: Max Pain 1,000 ｜ Call Wall 80（-4.7%，弱）（OI 1.7k） ｜ Put Wall 80（-4.7%，弱）（OI 4.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/SNDK_morning.json