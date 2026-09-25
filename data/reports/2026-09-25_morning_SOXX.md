# 期权晨报 2026-09-25（快照 10:20 ET）

📊 市场环境

SPY $769.28 ｜ QQQ $741.52
VIX 15.83 ↑1.0%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 0 ｜ 前值 0.9　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 566.07 → 今开 569.95（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 574.74 ｜ 低 567.35

Options: P/C成交量 1.61 | OI比 1.61 | ATM IV 43.6% | Skew -4.3pp | Term 0.86 | ExpMove ±3.8%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.3pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.61）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.61×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.61×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±3.8% ｜ 10-09（14D）±2.8% ｜ 10-16（21D）±2.9% ｜ 10-23（28D）±0.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 10,797,011 | GEX Change vs 上次快照 2,489,554 | Flip: Primary Flip: 556.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 572 / LOW 326 / INVALID 686
结构观察区: Primary Flip 556.68（全链重定价，覆盖 94%）
Call Wall 600（现价低于该位 4.6%）
最近结构参考: Flip 557（现价高于该位 2.8%）
量化视角： 正 Gamma（1080万，无历史分位）｜正 Gamma 增强（+249万）｜现价位于 Flip 上方 2.85%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 545（MaxPain，仅结算参考）；上方 600（Call Wall）。
• Gamma 区域：切换参考 557（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 535.0P — Vol 516 | 最新价 $9.40 | OI 356→870 (ΔOI +514张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增514张（+144.4% vs前日OI），连续性待观察（方向未知）
09-25 555.0C — Vol 125 | 最新价 $12.00 | OI 182→284 (ΔOI +102张) | ΔOI/Volume 81.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增102张（+56.0% vs前日OI），连续性待观察（方向未知）
10-16 510.0P — Vol 108 | 最新价 $4.33 | OI 5058→5159 (ΔOI +101张) | ΔOI/Volume 93.5% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增101张（+2.0% vs前日OI），值得跟踪（方向未知）
09-25 555.0P — Vol 256 | 最新价 $1.40 | OI 492→591 (ΔOI +99张) | ΔOI/Volume 38.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增99张（+20.1% vs前日OI），连续性待观察（方向未知）
10-02 550.0P — Vol 202 | 最新价 $7.05 | OI 688→787 (ΔOI +99张) | ΔOI/Volume 49.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增99张（+14.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 915 张（Put 813 / Call 102），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 11.8k / P 19.0k，今日成交量: C 0.3k / P 0.3k，平值价格ATM: C $3.08 / P $2.40 ｜ ATM IV 43.6%，预期波动 ±1.0%，Max Pain 545
Top ΔOI: P 550 -102 ｜ C 555 +102 ｜ P 555 +99

📆 Forward Expiration Structure

10-02  C +0.3k / P -0.8k ｜ Activity MEDIUM △ ｜ 7D
10-09  C +91 / P +0.1k ｜ Activity MEDIUM △ ｜ 14D
10-16  C -1.9k / P +0.4k ｜ Activity MEDIUM △ ｜ 21D
10-23  C +0.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 28D

📆 10-02 Forward Structure
存量OI: C 15.0k / P 13.8k，今日变化ΔOI: C +0.3k / P -0.8k，平值价格ATM: C $11.00 / P $11.00 ｜ ATM IV 35.9%，净 delta 敞口 23k shares
Top ΔOI: P 540 -598 ｜ P 560 -424 ｜ P 550 +99
仓位参考: Max Pain 542 ｜ Call Wall 542.5（-5.2%，弱）（OI 2.8k） ｜ Put Wall 550（-3.9%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 35.9%｜历史 Rank 78%（近端代理）｜IV/RV 0.95×（近似）｜净 delta 敞口 正 23,176 股

10-09（MEDIUM △）Top ΔOI: 560C +57 ｜ 520P +35
10-09（MEDIUM △）仓位参考: Max Pain 525 ｜ Call Wall 537.5（-6.1%，弱）（OI 0.4k） ｜ Put Wall 547.5（-4.4%，弱）（OI 87）

10-16（MEDIUM △）Top ΔOI: 600C -1,429 ｜ 535P +514
10-16（MEDIUM △）仓位参考: Max Pain 530 ｜ Call Wall 600（+4.8%）（OI 9.9k）

10-23（MEDIUM △）Top ΔOI: 410C +60 ｜ 520P +31
10-23（MEDIUM △）仓位参考: Max Pain 525 ｜ Call Wall 570（-0.4%，弱）（OI 65）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/SOXX_morning.json