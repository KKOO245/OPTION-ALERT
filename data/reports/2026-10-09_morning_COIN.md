# 期权晨报 2026-10-09（快照 10:20 ET）

📊 市场环境

SPY $778.69 ｜ QQQ $751.27
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
🟡 **近现价集中开仓**: 10-16 180C ΔOI +6,405（距现价 +3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 172.00 → 今开 174.80（+1.6%） | 较昨收变动（含盘初走势） ｜ 今日高 179.21 ｜ 低 171.65

Options: P/C成交量 0.60 | OI比 0.59 | ATM IV 79.4% | Skew -5.5pp | Term 0.81 | ExpMove ±6.3%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±6.3% ｜ 10-23（14D）±8.7% ｜ 10-30（21D）±11.8% ｜ 11-06（28D）±14.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 6,321,927 | GEX Change vs 上次快照 10,350,797 | Flip: Primary Flip: 171.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 403 / LOW 129 / INVALID 312
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 171.45（全链重定价，覆盖 89%）
最近结构参考: Flip 171（现价高于该位 1.6%）
量化视角： 正 Gamma（632万，无历史分位）｜由负转正（+1035万）｜现价位于 Flip 上方 1.62%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 180（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 171（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 180.0C — Vol 8,518 | 最新价 $2.94 | OI 2395→8800 (ΔOI +6405张) | ΔOI/Volume 75.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6405张（+267.4% vs前日OI），连续性待观察（方向未知）
10-16 187.5C — Vol 6,937 | 最新价 $1.60 | OI 858→6720 (ΔOI +5862张) | ΔOI/Volume 84.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5862张（+683.2% vs前日OI），连续性待观察（方向未知）
10-16 160.0P — Vol 2,873 | 最新价 $1.41 | OI 1786→3679 (ΔOI +1893张) | ΔOI/Volume 65.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1893张（+106.0% vs前日OI），连续性待观察（方向未知）
10-16 177.5C — Vol 2,076 | 最新价 $3.66 | OI 220→1678 (ΔOI +1458张) | ΔOI/Volume 70.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1458张（+662.7% vs前日OI），连续性待观察（方向未知）
10-16 190.0C — Vol 3,801 | 最新价 $1.20 | OI 2852→4240 (ΔOI +1388张) | ΔOI/Volume 36.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1388张（+48.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 17,006 张（Put 1,893 / Call 15,113），跨 1 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 62.6k / P 37.0k，今日成交量: C 5.9k / P 3.6k，平值价格ATM: C $1.61 / P $1.42 ｜ ATM IV 79.4%，预期波动 ±1.7%，Max Pain 180
Top ΔOI: C 195 -5,298 ｜ C 200 -3,079 ｜ C 192 -2,018

📆 Forward Expiration Structure

10-16  C +19.2k / P +5.6k ｜ Activity HIGH ｜ 7D
10-23  C +1.0k / P +0.3k ｜ Activity MEDIUM △ ｜ 14D
10-30  C +0.7k / P +0.7k ｜ Activity HIGH ｜ 21D
11-06  C +0.3k / P +0.1k ｜ Activity MEDIUM △ ｜ 28D

📆 10-16 Forward Structure
存量OI: C 110.5k / P 86.7k，今日变化ΔOI: C +19.2k / P +5.6k，平值价格ATM: C $5.55 / P $5.50 ｜ ATM IV 54.8%，净 delta 敞口 469k shares
Top ΔOI: C 180 +6,405 ｜ C 187 +5,862 ｜ P 160 +1,893
仓位参考: Max Pain 180 ｜ Call Wall 180（+3.3%，弱）（OI 8.8k） ｜ Put Wall 165（-5.3%，弱）（OI 3.7k）
量化解读： 存量 Call 重｜ATM IV 54.8%｜历史 Rank 60%（近端代理）｜IV/RV 0.99×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 468,657 股

10-23（MEDIUM △）Top ΔOI: 180C +214 ｜ 190C +148
10-23（MEDIUM △）仓位参考: Max Pain 188 ｜ Call Wall 190（+9.1%）（OI 1.2k） ｜ Put Wall 170（-2.4%，弱）（OI 0.7k）

📆 10-30 Forward Structure
存量OI: C 10.2k / P 8.8k，今日变化ΔOI: C +0.7k / P +0.7k，平值价格ATM: C $10.00 / P $10.55 ｜ ATM IV 63.6%，净 delta 敞口 2k shares
Top ΔOI: C 200 +307 ｜ P 150 +226 ｜ P 180 +138
仓位参考: Max Pain 185 ｜ Call Wall 185（+6.2%，弱）（OI 1.2k） ｜ Put Wall 170（-2.4%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜ATM IV 63.6%｜历史 Rank 60%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 正 2,332 股

11-06（MEDIUM △）Top ΔOI: 175C +47
11-06（MEDIUM △）仓位参考: Max Pain 180 ｜ Put Wall 170（-2.4%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/COIN_morning.json