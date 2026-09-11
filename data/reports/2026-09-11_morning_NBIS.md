# 期权晨报 2026-09-11（快照 10:40 ET）

📊 市场环境

SPY $764.32 ｜ QQQ $714.88
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
🟡 **近现价集中开仓**: 09-18 235C ΔOI +3,446（距现价 +1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 228.11 → 今开 234.80（+2.9%） | 较昨收变动（含盘初走势） ｜ 今日高 234.80 ｜ 低 226.37

Options: P/C成交量 0.27 | OI比 0.79 | ATM IV 108.5% | Skew -2.8pp | Term 0.74 | ExpMove ±8.7%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.27×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（7D）±8.7% ｜ 09-25（14D）±12.2% ｜ 10-02（21D）±16.1% ｜ 10-09（28D）±17.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,924,671 | GEX Change vs 上次快照 2,776,572 | Flip: Primary Flip: 227.32（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 534 / LOW 74 / INVALID 226
结构观察区: Primary Flip 227.32（全链重定价，覆盖 98%）
Put Wall 210（弱结构｜现价高于该位 10.0%） | Call Wall 250（弱结构｜现价低于该位 7.6%）
最近结构参考: Flip 227（现价高于该位 1.6%）
量化视角： 正 Gamma（392万，无历史分位）｜正 Gamma 增强（+278万）｜现价位于 Flip 上方 1.58%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 210（Put Wall，弱结构） / 225（MaxPain，仅结算参考）；上方 250（Call Wall，弱结构）。
• Gamma 区域：切换参考 227（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 250.0C — Vol 8,007 | 最新价 $0.43 | OI 3335→7398 (ΔOI +4063张) | ΔOI/Volume 50.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4063张（+121.8% vs前日OI），连续性待观察（方向未知）
09-18 235.0C — Vol 4,107 | 最新价 $8.12 | OI 235→3681 (ΔOI +3446张) | ΔOI/Volume 83.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3446张（+1466.4% vs前日OI），连续性待观察（方向未知）
09-18 227.5C — Vol 3,101 | 最新价 $11.69 | OI 215→2943 (ΔOI +2728张) | ΔOI/Volume 88.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2728张（+1268.8% vs前日OI），连续性待观察（方向未知）
09-18 197.5C — Vol 1,848 | 最新价 $33.50 | OI 31→1841 (ΔOI +1810张) | ΔOI/Volume 97.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1810张（+5838.7% vs前日OI），连续性待观察（方向未知）
09-11 217.5P — Vol 2,470 | 最新价 $1.39 | OI 543→2183 (ΔOI +1640张) | ΔOI/Volume 66.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1640张（+302.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 13,687 张（Put 1,640 / Call 12,047），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +10.8k / P +2.7k ｜ Activity HIGH ｜ 7D
09-25  C +0.3k / P +0.5k ｜ Activity HIGH ｜ 14D
10-02  C +0.2k / P +0.4k ｜ Activity MEDIUM △ ｜ 21D
10-09  C +0.3k / P +0.9k ｜ Activity HIGH ｜ 28D

📆 09-18 Forward Structure
存量OI: C 130.0k / P 168.3k，今日变化ΔOI: C +10.8k / P +2.7k，平值价格ATM: C $10.70 / P $9.35 ｜ ATM IV 76.7%，净 delta 敞口 533k shares
Top ΔOI: C 235 +3,446 ｜ C 227 +2,728 ｜ C 197 +1,810
仓位参考: Max Pain 220
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 76.7%｜历史 Rank 54%（近端代理）｜净 delta 敞口 正 532,573 股

📆 09-25 Forward Structure
存量OI: C 13.0k / P 16.1k，今日变化ΔOI: C +0.3k / P +0.5k，平值价格ATM: C $14.85 / P $13.21 ｜ ATM IV 77.1%，净 delta 敞口 411 shares
Top ΔOI: P 200 +145
仓位参考: Max Pain 220
量化解读： 存量 Put 重｜ATM IV 77.1%｜历史 Rank 54%（近端代理）｜净 delta 敞口 正 411 股

10-02（MEDIUM △）Top ΔOI: 210P +69 ｜ 250C +67
10-02（MEDIUM △）仓位参考: Max Pain 220

📆 10-09 Forward Structure
存量OI: C 3.6k / P 5.0k，今日变化ΔOI: C +0.3k / P +0.9k，平值价格ATM: C $19.67 / P $20.92 ｜ ATM IV 80.2%，净 delta 敞口 4k shares
Top ΔOI: C 235 +206
仓位参考: Max Pain 230
量化解读： 存量 Put 重｜ATM IV 80.2%｜历史 Rank 54%（近端代理）｜净 delta 敞口 正 3,738 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/NBIS_morning.json