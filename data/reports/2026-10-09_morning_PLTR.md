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
🟡 **近现价集中开仓**: 10-16 197P ΔOI +2,714（距现价 -1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 198.78 → 今开 201.06（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 203.84 ｜ 低 198.30

Options: P/C成交量 0.30 | OI比 0.56 | ATM IV 60.3% | Skew 1.5pp | Term 0.94 | ExpMove ±4.6%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构正常（Term 0.94）｜保护溢价薄（Skew 1.5pp）｜存量 Call 偏重（OI比 0.56）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.30×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±4.6% ｜ 10-23（14D）±6.3% ｜ 10-30（21D）±8.1% ｜ 11-06（28D）±12.8%
   ⇒ IV–VIX Spread: +45.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 133,988,412 | GEX Change vs 上次快照 -4,786,500 | Flip: Primary Flip: 184.19（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 592 / LOW 91 / INVALID 135
结构观察区: Primary Flip 184.19（全链重定价，覆盖 98%）
Call Wall 205（弱结构｜现价低于该位 2.5%）
最近结构参考: Call Wall 205（现价低于该位 2.5%）
量化视角： 正 Gamma（1.34亿，无历史分位）｜正 Gamma 减弱（479万）｜现价位于 Flip 上方 8.51%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（MaxPain，仅结算参考）；上方 205（Call Wall，弱结构）。
• Gamma 区域：切换参考 184（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 205.0C — Vol 123,289 | 最新价 $0.34 | OI 22390→31030 (ΔOI +8640张) | ΔOI/Volume 7.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8640张（+38.6% vs前日OI），连续性待观察（方向未知）
10-09 202.5C — Vol 81,102 | 最新价 $0.72 | OI 13959→18932 (ΔOI +4973张) | ΔOI/Volume 6.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4973张（+35.6% vs前日OI），连续性待观察（方向未知）
10-09 210.0C — Vol 38,640 | 最新价 $0.08 | OI 3213→7495 (ΔOI +4282张) | ΔOI/Volume 11.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4282张（+133.3% vs前日OI），连续性待观察（方向未知）
10-16 150.0P — Vol 5,950 | 最新价 $0.10 | OI 5930→9761 (ΔOI +3831张) | ΔOI/Volume 64.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3831张（+64.6% vs前日OI），连续性待观察（方向未知）
10-23 105.0P — Vol 3,100 | 最新价 $0.05 | OI 56→3150 (ΔOI +3094张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3094张（+5525.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 24,820 张（Put 6,925 / Call 17,895），跨 3 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 148.7k / P 83.7k，今日成交量: C 98.7k / P 29.4k，平值价格ATM: C $0.92 / P $1.79 ｜ ATM IV 60.3%，预期波动 ±1.4%，Max Pain 190
Top ΔOI: C 205 +8,640 ｜ C 202 +4,973 ｜ C 210 +4,282

📆 Forward Expiration Structure

10-16  C +7.1k / P +15.0k ｜ Activity HIGH ｜ 7D
10-23  C +3.7k / P +7.3k ｜ Activity HIGH ｜ 14D
10-30  C +1.6k / P +2.3k ｜ Activity HIGH ｜ 21D
11-06  C +2.6k / P +1.5k ｜ Activity HIGH ｜ 28D

📆 10-16 Forward Structure
存量OI: C 169.0k / P 212.1k，今日变化ΔOI: C +7.1k / P +15.0k，平值价格ATM: C $4.25 / P $4.97 ｜ ATM IV 41.0%，净 delta 敞口 -292k shares
Top ΔOI: P 197 +2,714 ｜ C 210 +1,929
仓位参考: Max Pain 170 ｜ Call Wall 200（+0.1%，弱）（OI 16.9k） ｜ Put Wall 190（-4.9%，弱）（OI 6.1k）
量化解读： 存量 Put 重｜ATM IV 41.0%｜历史 Rank 95%（近端代理）｜IV/RV 1.99×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 291,501 股

📆 10-23 Forward Structure
存量OI: C 29.9k / P 27.6k，今日变化ΔOI: C +3.7k / P +7.3k，平值价格ATM: C $6.25 / P $6.45 ｜ ATM IV 40.8%，净 delta 敞口 -5k shares
Top ΔOI: C 220 +672 ｜ P 195 +594
仓位参考: Max Pain 180 ｜ Call Wall 180（-9.9%，弱）（OI 4.7k） ｜ Put Wall 190（-4.9%，弱）（OI 1.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 40.8%｜历史 Rank 95%（近端代理）｜IV/RV 1.97×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 5,358 股

📆 10-30 Forward Structure
存量OI: C 29.8k / P 22.4k，今日变化ΔOI: C +1.6k / P +2.3k，平值价格ATM: C $8.10 / P $8.00 ｜ ATM IV 41.7%，净 delta 敞口 -56k shares
Top ΔOI: P 190 +783 ｜ C 200 -458
仓位参考: Max Pain 185 ｜ Call Wall 192.5（-3.7%，弱）（OI 2.7k） ｜ Put Wall 190（-4.9%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 41.7%｜历史 Rank 95%（近端代理）｜IV/RV 2.02×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 55,869 股

📆 11-06 Forward Structure
存量OI: C 11.1k / P 12.4k，今日变化ΔOI: C +2.6k / P +1.5k，平值价格ATM: C $13.35 / P $12.25 ｜ ATM IV 56.9%，净 delta 敞口 37k shares
Top ΔOI: C 215 +502 ｜ C 205 +416 ｜ P 200 +377
仓位参考: Max Pain 190 ｜ Call Wall 215（+7.6%，弱）（OI 1.0k） ｜ Put Wall 190（-4.9%）（OI 3.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 56.9%｜历史 Rank 95%（近端代理）｜IV/RV 2.76×（近似）｜净 delta 敞口 正 37,401 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/PLTR_morning.json