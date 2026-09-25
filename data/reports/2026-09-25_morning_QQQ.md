# 期权晨报 2026-09-25（快照 10:20 ET）

📊 市场环境

SPY $771.10 ｜ QQQ $744.50
VIX 15.83 ↑1.0%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 0 ｜ 前值 0.9　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-28 730P ΔOI +6,726（距现价 -1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-01 660P ΔOI +8,750 占该期限总 OI 11.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 741.10 → 今开 742.84（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 745.42 ｜ 低 739.64

Options: P/C成交量 0.84 | OI比 2.08 | ATM IV 23.2% | Skew 3.0pp | Term 0.79 | ExpMove ±0.9%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价中性（Skew 3.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.08×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 86% ｜ P/C OI(近端) 81%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 86%）｜近端持仓结构中性（P/C OI 分位 81%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-28（3D）±0.9% ｜ 09-29（4D）±1.2% ｜ 09-30（5D）±1.6% ｜ 10-01（6D）±1.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 421,408,612 | GEX Change vs 上次快照 218,148,102 | Flip: Primary Flip: 738.58（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 3487 / LOW 279 / INVALID 1562
结构观察区: Primary Flip 738.58（全链重定价，覆盖 95%）
Call Wall 760（弱结构｜现价低于该位 2.2%）
最近结构参考: Flip 739（现价高于该位 0.6%）
量化视角： 正 Gamma（4.21亿，历史分位偏正区，比 86% 的交易日更正）｜正 Gamma 增强（+2.18亿）｜现价位于 Flip 上方 0.61%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 735（MaxPain，仅结算参考）；上方 760（Call Wall，弱结构）。
• Gamma 区域：切换参考 739（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-29 730.0P — Vol 16,243 | 最新价 $1.95 | OI 553→14713 (ΔOI +14160张) | ΔOI/Volume 87.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14160张（+2560.6% vs前日OI），连续性待观察（方向未知）
10-01 660.0P — Vol 8,795 | 最新价 $0.11 | OI 43→8793 (ΔOI +8750张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8750张（+20348.8% vs前日OI），连续性待观察（方向未知）
09-25 750.0C — Vol 37,544 | 最新价 $0.24 | OI 13050→20833 (ΔOI +7783张) | ΔOI/Volume 20.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7783张（+59.6% vs前日OI），连续性待观察（方向未知）
10-16 765.0C — Vol 10,882 | 最新价 $4.13 | OI 10730→17575 (ΔOI +6845张) | ΔOI/Volume 62.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6845张（+63.8% vs前日OI），连续性待观察（方向未知）
09-28 730.0P — Vol 63,263 | 最新价 $1.34 | OI 7360→14086 (ΔOI +6726张) | ΔOI/Volume 10.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6726张（+91.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 44,264 张（Put 29,636 / Call 14,628），跨 5 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 296.9k / P 618.5k，今日成交量: C 517.9k / P 436.4k，平值价格ATM: C $1.60 / P $2.17 ｜ ATM IV 23.2%，预期波动 ±0.5%，Max Pain 735
Top ΔOI: C 750 +7,783 ｜ P 735 +6,356 ｜ C 746 +5,266

📆 Forward Expiration Structure

09-28  C +29.0k / P +21.0k ｜ Activity HIGH ｜ 3D
09-29  C +10.0k / P +26.4k ｜ Activity HIGH ｜ 4D
09-30  C +6.9k / P -2.8k ｜ Activity HIGH ｜ 5D
10-01  C +9.8k / P +17.8k ｜ Activity HIGH ｜ 6D

📆 09-28 Forward Structure
存量OI: C 76.8k / P 169.4k，今日变化ΔOI: C +29.0k / P +21.0k，平值价格ATM: C $3.30 / P $3.75 ｜ ATM IV 12.5%，净 delta 敞口 545k shares
Top ΔOI: P 730 +6,726 ｜ C 755 +4,989 ｜ C 749 +4,217
仓位参考: Max Pain 737 ｜ Call Wall 755（+1.6%）（OI 8.5k） ｜ Put Wall 727（-2.2%）（OI 31.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 12.5%｜历史 Rank 74%（近端代理）｜IV/RV 0.81×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 545,377 股

📆 09-29 Forward Structure
存量OI: C 40.9k / P 102.8k，今日变化ΔOI: C +10.0k / P +26.4k，平值价格ATM: C $4.45 / P $4.72 ｜ ATM IV 14.1%，净 delta 敞口 -46k shares
Top ΔOI: P 730 +14,160 ｜ P 712 +2,439 ｜ P 715 +1,795
仓位参考: Max Pain 735 ｜ Call Wall 751（+1.1%，弱）（OI 2.1k） ｜ Put Wall 725（-2.4%，弱）（OI 19.5k）
量化解读： 存量 Put 重｜ATM IV 14.1%｜历史 Rank 74%（近端代理）｜IV/RV 0.92×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 45,660 股

📆 09-30 Forward Structure
存量OI: C 349.9k / P 524.5k，今日变化ΔOI: C +6.9k / P -2.8k，平值价格ATM: C $5.65 / P $5.84 ｜ ATM IV 16.1%，净 delta 敞口 462k shares
Top ΔOI: C 720 +5,553 ｜ P 680 -3,514 ｜ C 740 -3,503
仓位参考: Max Pain 721 ｜ Call Wall 726（-2.3%）（OI 45.2k） ｜ Put Wall 730（-1.8%，弱）（OI 49.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 16.1%｜历史 Rank 74%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 正 462,201 股

📆 10-01 Forward Structure
存量OI: C 30.3k / P 44.1k，今日变化ΔOI: C +9.8k / P +17.8k，平值价格ATM: C $6.53 / P $6.61 ｜ ATM IV 16.8%，净 delta 敞口 229k shares
Top ΔOI: P 660 +8,750 ｜ C 740 +2,210 ｜ P 725 +1,098
仓位参考: Max Pain 738 ｜ Call Wall 740（-0.4%）（OI 6.0k） ｜ Put Wall 740（-0.4%，弱）（OI 4.2k）
量化解读： 存量 Put 重｜ATM IV 16.8%｜历史 Rank 74%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 正 229,001 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/QQQ_morning.json