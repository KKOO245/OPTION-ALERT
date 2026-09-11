# 期权晚报 2026-09-11（快照 16:40 ET）

📊 市场环境

SPY $764.29 ｜ QQQ $714.88
VIX 15.84 ↓11.2%（5D +9.0%） ｜ Vol Regime: NORMAL
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
🟡 **近现价集中开仓**: 09-14 730C ΔOI +5,291（距现价 +2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 715.44 → 收盘 714.88（-0.1%） ｜ 今日高 717.62 ｜ 低 713.65 ｜ 昨收 708.69 → 收盘 714.88（+0.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.39 | OI比 1.44 | ATM IV 7.6% | Skew 2.9pp | Term 2.31 | ExpMove ±0.7%（近端） | Rank 2%
量化视角： IV 历史低位（Rank 2%，期权偏便宜）｜期限结构正常偏陡（Term 2.31）｜保护溢价中性（Skew 2.9pp）｜当日成交偏 Put（P/C量 1.39）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.39×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.44×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 42% ｜ P/C OI(近端) 32%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 42%）｜近端持仓结构中性（P/C OI 分位 32%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-14（3D）±0.7% ｜ 09-15（4D）±1.0% ｜ 09-16（5D）±1.4% ｜ 09-17（6D）±1.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -129,220,124 | GEX Change vs 上次快照 -97,791,128 | Flip: Primary Flip: 717.29（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 2940 / LOW 536 / INVALID 2328
结构观察区: Primary Flip 717.29（全链重定价，覆盖 90%）
Put Wall 700（弱结构｜现价高于该位 2.1%） | Call Wall 750（弱结构｜现价低于该位 4.7%）
最近结构参考: Flip 717（现价低于该位 0.3%）
量化视角： 负 Gamma（1.29亿，历史分位 42%，中性区）｜负 Gamma 加深（9779万）｜现价位于 Flip 下方 0.34%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构） / 712（MaxPain，仅结算参考）；上方 750（Call Wall，弱结构）。
• Gamma 区域：切换参考 717（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 675.0P — Vol 3,703 | 最新价 $0.58 | OI 21099→43643 (ΔOI +22544张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22544张（+106.8% vs前日OI），连续性待观察（方向未知）
09-18 700.0P — Vol 21,949 | 最新价 $2.39 | OI 102500→118265 (ΔOI +15765张) | ΔOI/Volume 71.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15765张（+15.4% vs前日OI），连续性待观察（方向未知）
09-30 720.0C — Vol 1,510 | 最新价 $8.24 | OI 21240→31305 (ΔOI +10065张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10065张（+47.4% vs前日OI），连续性待观察（方向未知）
09-30 735.0C — Vol 451 | 最新价 $2.72 | OI 2310→12322 (ΔOI +10012张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10012张（+433.4% vs前日OI），连续性待观察（方向未知）
09-30 650.0P — Vol 543 | 最新价 $1.09 | OI 8664→17620 (ΔOI +8956张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8956张（+103.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 67,342 张（Put 47,265 / Call 20,077），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $5M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-14  C +23.6k / P +31.7k ｜ Activity HIGH ｜ 3D
09-15  C +11.4k / P +28.5k ｜ Activity HIGH ｜ 4D
09-16  C +9.1k / P +9.3k ｜ Activity HIGH ｜ 5D
09-17  C +6.8k / P +10.6k ｜ Activity HIGH ｜ 6D

📆 09-14 Forward Structure
存量OI:      C 42.5k / P 87.5k
今日变化ΔOI: C +23.6k / P +31.7k
平值价格ATM:  C 2.52 / P 2.65
隐含波动率 ATM IV:  9.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 529k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 730 ｜ +5,291 ｜ $0.01 ｜ 名义 $5.3k* ｜ +2.1%
C 722 ｜ +2,446 ｜ $0.26 ｜ 名义 $63.6k* ｜ +1.0%
P 684 ｜ +2,353 ｜ $0.06 ｜ 名义 $14.1k* ｜ -4.3%
结构参考：730（+2.1%） / 684（-4.3%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 711（结算参考） ｜ Call Wall 730（+2.1%）（OI 8.3k） ｜ Put Wall 655（-8.4%）（OI 11.9k）
量化解读： 存量 Put 重｜ATM IV 9.9%｜历史 Rank 2%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 528,717 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-15 Forward Structure
存量OI:      C 24.9k / P 78.0k
今日变化ΔOI: C +11.4k / P +28.5k
平值价格ATM:  C 3.55 / P 3.58
隐含波动率 ATM IV:  11.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 89k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 650 ｜ +7,307 ｜ $0.05 ｜ 名义 $36.5k* ｜ -9.1%
P 645 ｜ +5,022 ｜ $0.05 ｜ 名义 $25.1k* ｜ -9.8%
P 696 ｜ +3,056 ｜ $0.36 ｜ 名义 $110.0k* ｜ -2.6%
结构参考：650（-9.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 715（结算参考） ｜ Call Wall 730（+2.1%，弱）（OI 5.2k） ｜ Put Wall 650（-9.1%）（OI 15.7k）
量化解读： 存量 Put 重｜ATM IV 11.8%｜历史 Rank 2%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 88,794 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-16 Forward Structure
存量OI:      C 17.3k / P 27.8k
今日变化ΔOI: C +9.1k / P +9.3k
平值价格ATM:  C 5.11 / P 5.05
隐含波动率 ATM IV:  15.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 188k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 677 ｜ +3,377 ｜ $0.24 ｜ 名义 $81.0k* ｜ -5.3%
C 740 ｜ +1,035 ｜ $0.03 ｜ 名义 $3.1k* ｜ +3.5%
C 735 ｜ +713 ｜ $0.09 ｜ 名义 $6.4k* ｜ +2.8%
结构参考：740（+3.5%） / 677（-5.3%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 710（结算参考） ｜ Call Wall 740（+3.5%，弱）（OI 2.0k） ｜ Put Wall 677（-5.3%）（OI 3.4k）
量化解读： 存量 Put 重｜ATM IV 15.0%｜历史 Rank 2%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 187,888 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-17 Forward Structure
存量OI:      C 11.9k / P 21.4k
今日变化ΔOI: C +6.8k / P +10.6k
平值价格ATM:  C 5.96 / P 5.95
隐含波动率 ATM IV:  16.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 144k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 725 ｜ +1,045 ｜ $1.78 ｜ 名义 $186.0k* ｜ +1.4%
P 690 ｜ +808 ｜ $0.96 ｜ 名义 $77.6k* ｜ -3.5%
C 726 ｜ +700 ｜ $1.50 ｜ 名义 $105.0k* ｜ +1.6%
结构参考：725（+1.4%） / 690（-3.5%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 710（结算参考） ｜ Call Wall 725（+1.4%）（OI 1.7k） ｜ Put Wall 690（-3.5%，弱）（OI 1.7k）
量化解读： 存量 Put 重｜ATM IV 16.2%｜历史 Rank 2%（近端代理）｜净 delta 敞口 正 144,477 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/QQQ_evening.json