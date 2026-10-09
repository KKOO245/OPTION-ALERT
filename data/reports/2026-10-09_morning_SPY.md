# 期权晨报 2026-10-09（快照 10:20 ET）

📊 市场环境

SPY $776.00 ｜ QQQ $749.68
VIX 15.10 ↓2.0%（5D -1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 42.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 46.3 ｜ 前值 48.1　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-12 780C ΔOI +5,720（距现价 +0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-14 790C ΔOI -51,342 占该期限总 OI 29.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 773.93 → 今开 776.24（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 776.84 ｜ 低 775.14

Options: P/C成交量 1.05 | OI比 1.32 | ATM IV 13.1% | Skew 2.2pp | Term 0.94 | ExpMove ±0.5%（近端） | Rank 52%
量化视角： IV 中性（Rank 52%）｜期限结构正常（Term 0.94）｜保护溢价中性（Skew 2.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.05×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.32×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 68% ｜ P/C OI(近端) 12%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 68%）｜近端持仓结构中性（P/C OI 分位 12%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-12（3D）±0.5% ｜ 10-13（4D）±0.7% ｜ 10-14（5D）±0.9% ｜ 10-15（6D）±1.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 571,891,541 | GEX Change vs 上次快照 958,874,833 | Flip: Primary Flip: 773.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2778 / LOW 384 / INVALID 1582
结构观察区: Primary Flip 773.87（全链重定价，覆盖 94%）
Call Wall 785（现价低于该位 1.2%）
最近结构参考: Flip 774（现价高于该位 0.2%）
量化视角： 正 Gamma（5.72亿，历史分位 68%，中性区）｜由负转正（+9.59亿）｜现价位于 Flip 上方 0.22%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 772（MaxPain，仅结算参考）；上方 785（Call Wall）。
• Gamma 区域：切换参考 774（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 748.0P — Vol 31,594 | 最新价 $0.48 | OI 6066→22265 (ΔOI +16199张) | ΔOI/Volume 51.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16199张（+267.1% vs前日OI），连续性待观察（方向未知）
10-09 733.0P — Vol 53,574 | 最新价 $0.02 | OI 1456→17507 (ΔOI +16051张) | ΔOI/Volume 30.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16051张（+1102.4% vs前日OI），连续性待观察（方向未知）
10-16 795.0C — Vol 25,205 | 最新价 $0.16 | OI 24348→38398 (ΔOI +14050张) | ΔOI/Volume 55.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14050张（+57.7% vs前日OI），连续性待观察（方向未知）
10-15 690.0P — Vol 10,172 | 最新价 $0.05 | OI 26→10193 (ΔOI +10167张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10167张（+39103.8% vs前日OI），连续性待观察（方向未知）
10-09 777.0C — Vol 94,800 | 最新价 $0.75 | OI 4904→14953 (ΔOI +10049张) | ΔOI/Volume 10.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10049张（+204.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 66,516 张（Put 42,417 / Call 24,099），跨 3 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 652.4k / P 859.0k，今日成交量: C 480.9k / P 503.1k，平值价格ATM: C $0.86 / P $1.33 ｜ ATM IV 13.1%，预期波动 ±0.3%，Max Pain 772
Top ΔOI: P 733 +16,051 ｜ C 777 +10,049 ｜ C 779 +9,102

📆 Forward Expiration Structure

10-12  C +33.4k / P +38.9k ｜ Activity HIGH ｜ 3D
10-13  C +18.6k / P +20.6k ｜ Activity HIGH ｜ 4D
10-14  C -13.4k / P +11.9k ｜ Activity HIGH ｜ 5D
10-15  C +7.4k / P +20.2k ｜ Activity HIGH ｜ 6D

📆 10-12 Forward Structure
存量OI: C 98.5k / P 148.3k，今日变化ΔOI: C +33.4k / P +38.9k，平值价格ATM: C $1.80 / P $2.28 ｜ ATM IV 7.0%，净 delta 敞口 736k shares
Top ΔOI: P 728 +7,980 ｜ P 729 +6,288 ｜ C 780 +5,720
仓位参考: Max Pain 774 ｜ Call Wall 780（+0.6%，弱）（OI 9.0k） ｜ Put Wall 770（-0.7%，弱）（OI 6.9k）
量化解读： 存量 Put 重｜ATM IV 7.0%｜历史 Rank 52%（近端代理）｜IV/RV 0.76×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 736,124 股

📆 10-13 Forward Structure
存量OI: C 64.3k / P 95.1k，今日变化ΔOI: C +18.6k / P +20.6k，平值价格ATM: C $2.45 / P $2.82 ｜ ATM IV 7.8%，净 delta 敞口 200k shares
Top ΔOI: P 730 +4,851 ｜ P 731 +4,205 ｜ C 775 +2,388
仓位参考: Max Pain 775 ｜ Call Wall 790（+1.9%，弱）（OI 4.8k） ｜ Put Wall 774（-0.2%，弱）（OI 4.4k）
量化解读： 存量 Put 重｜ATM IV 7.8%｜历史 Rank 52%（近端代理）｜IV/RV 0.85×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 200,147 股

📆 10-14 Forward Structure
存量OI: C 93.2k / P 82.2k，今日变化ΔOI: C -13.4k / P +11.9k，平值价格ATM: C $3.28 / P $3.60 ｜ ATM IV 9.2%，净 delta 敞口 -9k shares
Top ΔOI: C 790 -51,342 ｜ C 803 +9,033 ｜ C 805 +7,119
仓位参考: Max Pain 775 ｜ Call Wall 790（+1.9%）（OI 28.5k） ｜ Put Wall 755（-2.7%，弱）（OI 5.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 9.2%｜历史 Rank 52%（近端代理）｜IV/RV 1.00×（近似）｜净 delta 敞口 负 8,630 股

📆 10-15 Forward Structure
存量OI: C 24.6k / P 58.5k，今日变化ΔOI: C +7.4k / P +20.2k，平值价格ATM: C $3.79 / P $4.06 ｜ ATM IV 9.6%，净 delta 敞口 165k shares
Top ΔOI: P 690 +10,167 ｜ P 772 -2,457
仓位参考: Max Pain 775 ｜ Call Wall 781（+0.7%，弱）（OI 1.6k） ｜ Put Wall 772（-0.5%，弱）（OI 4.1k）
量化解读： 存量 Put 重｜ATM IV 9.6%｜历史 Rank 52%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 正 164,893 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/SPY_morning.json