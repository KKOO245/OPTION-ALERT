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
🟡 **近现价集中开仓**: 09-14 58P ΔOI +1,578（距现价 -1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-16 58P ΔOI +3,582 占该期限总 OI 21.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 57.50 → 今开 58.73（+2.1%） | 较昨收变动（含盘初走势） ｜ 今日高 58.96 ｜ 低 58.26

Options: P/C成交量 0.76 | OI比 0.64 | ATM IV 48.8% | Skew 1.2pp | Term 0.86 | ExpMove ±2.5%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价薄（Skew 1.2pp）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.76×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-14（3D）±2.5% ｜ 09-16（5D）±4.0% ｜ 09-18（7D）±4.7% ｜ 09-21（10D）±5.3%
   ⇒ IV–VIX Spread: +33.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 74,867,267 | GEX Change vs 上次快照 38,631,481 | Flip: Primary Flip: 56.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 954 / LOW 228 / INVALID 278
结构观察区: Primary Flip 56.63（全链重定价，覆盖 97%）
最近结构参考: Flip 57（现价高于该位 3.5%）
量化视角： 正 Gamma（7487万，无历史分位）｜正 Gamma 增强（+3863万）｜现价位于 Flip 上方 3.53%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 59（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 57（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 64.0C — Vol 12,411 | 最新价 $1.27 | OI 32244→44281 (ΔOI +12037张) | ΔOI/Volume 97.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12037张（+37.3% vs前日OI），连续性待观察（方向未知）
09-30 53.0P — Vol 11,128 | 最新价 $0.69 | OI 1316→11129 (ΔOI +9813张) | ΔOI/Volume 88.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9813张（+745.7% vs前日OI），连续性待观察（方向未知）
10-02 50.0P — Vol 6,887 | 最新价 $0.32 | OI 619→7090 (ΔOI +6471张) | ΔOI/Volume 94.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6471张（+1045.4% vs前日OI），连续性待观察（方向未知）
09-16 58.0P — Vol 3,776 | 最新价 $1.69 | OI 341→3923 (ΔOI +3582张) | ΔOI/Volume 94.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3582张（+1050.4% vs前日OI），连续性待观察（方向未知）
09-30 50.0P — Vol 3,845 | 最新价 $0.30 | OI 3418→6788 (ΔOI +3370张) | ΔOI/Volume 87.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3370张（+98.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 35,273 张（Put 23,236 / Call 12,037），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-14  C +5.9k / P +3.0k ｜ Activity HIGH ｜ 3D
09-16  C +1.4k / P +5.1k ｜ Activity HIGH ｜ 5D
09-18  C -5.4k / P -2.1k ｜ Activity HIGH ｜ 7D
09-21  C +0.4k / P +0.8k ｜ Activity HIGH ｜ 10D

📆 09-14 Forward Structure
存量OI: C 16.5k / P 7.9k，今日变化ΔOI: C +5.9k / P +3.0k，平值价格ATM: C $0.50 / P $0.94 ｜ ATM IV 30.4%，净 delta 敞口 39k shares
Top ΔOI: P 58 +1,578 ｜ C 63 +1,257
仓位参考: Max Pain 59 ｜ Put Wall 58（-1.1%）（OI 2.5k）
量化解读： 存量 Call 重｜ATM IV 30.4%｜历史 Rank 81%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 39,384 股

📆 09-16 Forward Structure
存量OI: C 7.5k / P 8.8k，今日变化ΔOI: C +1.4k / P +5.1k，平值价格ATM: C $0.95 / P $1.41 ｜ ATM IV 39.6%，净 delta 敞口 -116k shares
Top ΔOI: P 58 +3,582 ｜ P 57 +524
仓位参考: Max Pain 60 ｜ Call Wall 64（+9.2%）（OI 1.8k） ｜ Put Wall 58（-1.1%）（OI 3.9k）
量化解读： 存量两侧均衡｜ATM IV 39.6%｜历史 Rank 81%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 116,049 股

📆 09-18 Forward Structure
存量OI: C 962.1k / P 461.2k，今日变化ΔOI: C -5.4k / P -2.1k，平值价格ATM: C $1.45 / P $1.30 ｜ ATM IV 41.8%，净 delta 敞口 706k shares
Top ΔOI: C 63 -10,084 ｜ P 80 -3,877 ｜ C 60 +2,999
仓位参考: Max Pain 60
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 41.8%｜历史 Rank 81%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 706,097 股

📆 09-21 Forward Structure
存量OI: C 1.3k / P 1.2k，今日变化ΔOI: C +0.4k / P +0.8k，平值价格ATM: C $1.34 / P $1.79 ｜ ATM IV 38.9%，净 delta 敞口 -23k shares
Top ΔOI: P 59 +298 ｜ P 57 +219 ｜ C 60 +97
仓位参考: Max Pain 59 ｜ Put Wall 59（+0.6%，弱）（OI 0.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 38.9%｜历史 Rank 81%（近端代理）｜净 delta 敞口 负 23,315 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/SLV_morning.json