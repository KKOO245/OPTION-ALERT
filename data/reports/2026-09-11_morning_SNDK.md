# 期权晨报 2026-09-11（快照 10:40 ET）

📊 市场环境

SPY $764.27 ｜ QQQ $714.88
VIX 15.78 ↓11.6%（5D +8.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.2　✅ 今日已公布
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 3.4 ｜ 前值 3.4　✅ 今日已公布
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 0.4 ｜ 前值 0.1　✅ 今日已公布
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 2.4 ｜ 前值 2.5　✅ 今日已公布
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 47.8 ｜ 前值 51.7　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: -2.6%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-18 1700C ΔOI +384（距现价 +3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,692.59 → 今开 1,713.00（+1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 1720.33 ｜ 低 1616.80

Options: P/C成交量 0.62 | OI比 0.91 | ATM IV 94.5% | Skew -1.8pp | Term 0.75 | ExpMove ±7.4%（近端） | Rank 44%
量化视角： IV 中性（Rank 44%）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.91×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（7D）±7.4% ｜ 09-25（14D）±11.2% ｜ 10-02（21D）±13.6% ｜ 10-09（28D）±16.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 1,180,499 | GEX Change vs 上次快照 -671,742 | Flip: Primary Flip: 1641.85（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 1995 / LOW 567 / INVALID 900
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1641.85（全链重定价，覆盖 94%）
Put Wall 1,500（弱结构｜现价高于该位 9.9%）
最近结构参考: Flip 1642（现价高于该位 0.4%）
量化视角： 正 Gamma（118万，无历史分位）｜正 Gamma 减弱（67万）｜现价位于 Flip 上方 0.43%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,500（Put Wall，弱结构）；上方 1,680（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1642（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 1600.0P — Vol 6,636 | 最新价 $2.80 | OI 2251→3626 (ΔOI +1375张) | ΔOI/Volume 20.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1375张（+61.1% vs前日OI），连续性待观察（方向未知）
09-11 1800.0C — Vol 10,998 | 最新价 $2.95 | OI 2970→3835 (ΔOI +865张) | ΔOI/Volume 7.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增865张（+29.1% vs前日OI），连续性待观察（方向未知）
09-11 2250.0C — Vol 732 | 最新价 $0.05 | OI 207→830 (ΔOI +623张) | ΔOI/Volume 85.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增623张（+301.0% vs前日OI），连续性待观察（方向未知）
09-11 1700.0C — Vol 7,395 | 最新价 $24.52 | OI 1064→1676 (ΔOI +612张) | ΔOI/Volume 8.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增612张（+57.5% vs前日OI），连续性待观察（方向未知）
09-11 1835.0C — Vol 817 | 最新价 $1.40 | OI 101→692 (ΔOI +591张) | ΔOI/Volume 72.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增591张（+585.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,066 张（Put 1,375 / Call 2,691），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +2.9k / P +3.4k ｜ Activity HIGH ｜ 7D
09-25  C +0.4k / P +0.5k ｜ Activity HIGH ｜ 14D
10-02  C +0.5k / P +0.4k ｜ Activity HIGH ｜ 21D
10-09  C +0.6k / P +0.2k ｜ Activity HIGH ｜ 28D

📆 09-18 Forward Structure
存量OI: C 69.8k / P 83.9k，今日变化ΔOI: C +2.9k / P +3.4k，平值价格ATM: C $61.22 / P $60.10 ｜ ATM IV 64.9%，净 delta 敞口 -30k shares
Top ΔOI: C 1700 +384 ｜ P 1600 +322
仓位参考: Max Pain 1,500
量化解读： 存量 Put 重｜ATM IV 64.9%｜历史 Rank 44%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 29,558 股

📆 09-25 Forward Structure
存量OI: C 8.5k / P 15.9k，今日变化ΔOI: C +0.4k / P +0.5k，平值价格ATM: C $87.00 / P $97.32 ｜ ATM IV 65.9%，净 delta 敞口 -4k shares
Top ΔOI: C 1700 +134 ｜ P 1700 +77 ｜ P 1535 +59
仓位参考: Max Pain 1,600
量化解读： 存量 Put 重｜ATM IV 65.9%｜历史 Rank 44%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 3,519 股

📆 10-02 Forward Structure
存量OI: C 6.8k / P 8.2k，今日变化ΔOI: C +0.5k / P +0.4k，平值价格ATM: C $114.54 / P $110.19 ｜ ATM IV 69.8%，净 delta 敞口 812 shares
Top ΔOI: P 1690 +108 ｜ C 1700 +86 ｜ C 1705 +54
仓位参考: Max Pain 1,590 ｜ Call Wall 1600（-3.0%，弱）（OI 0.3k） ｜ Put Wall 1500（-9.0%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 69.8%｜历史 Rank 44%（近端代理）｜净 delta 敞口 正 812 股

📆 10-09 Forward Structure
存量OI: C 2.2k / P 2.8k，今日变化ΔOI: C +0.6k / P +0.2k，平值价格ATM: C $132.80 / P $133.71 ｜ ATM IV 71.1%，净 delta 敞口 16k shares
Top ΔOI: C 1750 +77 ｜ C 1700 +69 ｜ C 1600 +48
仓位参考: Max Pain 1,650 ｜ Call Wall 1750（+6.1%，弱）（OI 0.1k） ｜ Put Wall 1500（-9.0%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 71.1%｜历史 Rank 44%（近端代理）｜净 delta 敞口 正 16,310 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/SNDK_morning.json