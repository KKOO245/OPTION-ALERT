# 期权晨报 2026-09-11（快照 10:20 ET）

📊 市场环境

SPY $766.00 ｜ QQQ $716.27
VIX 15.94 ↓10.7%（5D +9.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.5（fear）
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
🟡 **近现价集中开仓**: 09-18 132P ΔOI +571（距现价 -1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NOW

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NOW  昨收 131.17 → 今开 130.50（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 134.45 ｜ 低 130.39

Options: P/C成交量 0.64 | OI比 0.81 | ATM IV 76.8% | Skew 4.0pp | Term 0.68 | ExpMove ±5.9%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.68，近月 IV 高于远月）｜保护溢价中性（Skew 4.0pp）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（7D）±5.9% ｜ 09-25（14D）±9.2% ｜ 10-02（21D）±11.1% ｜ 10-09（28D）±12.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 13,777,480 | GEX Change vs 上次快照 8,202,019 | Flip: Primary Flip: 128.78（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 523 / LOW 119 / INVALID 198
结构观察区: Primary Flip 128.78（全链重定价，覆盖 95%）
最近结构参考: Flip 129（现价高于该位 3.8%）
量化视角： 正 Gamma（1378万，无历史分位）｜正 Gamma 增强（+820万）｜现价位于 Flip 上方 3.81%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 134（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 129（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 170.0C — Vol 2,279 | 最新价 $0.83 | OI 2625→4673 (ΔOI +2048张) | ΔOI/Volume 89.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2048张（+78.0% vs前日OI），连续性待观察（方向未知）
09-11 144.0C — Vol 1,853 | 最新价 $0.05 | OI 623→1839 (ΔOI +1216张) | ΔOI/Volume 65.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1216张（+195.2% vs前日OI），连续性待观察（方向未知）
09-11 124.0P — Vol 2,268 | 最新价 $0.20 | OI 1399→2524 (ΔOI +1125张) | ΔOI/Volume 49.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1125张（+80.4% vs前日OI），连续性待观察（方向未知）
09-11 140.0C — Vol 4,110 | 最新价 $0.13 | OI 3720→4559 (ΔOI +839张) | ΔOI/Volume 20.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增839张（+22.6% vs前日OI），连续性待观察（方向未知）
09-11 134.0C — Vol 3,165 | 最新价 $0.95 | OI 739→1559 (ΔOI +820张) | ΔOI/Volume 25.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增820张（+111.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,048 张（Put 1,125 / Call 4,923），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +2.2k / P +1.8k ｜ Activity HIGH ｜ 7D
09-25  C +0.9k / P +0.3k ｜ Activity HIGH ｜ 14D
10-02  C +0.3k / P +0.3k ｜ Activity LOW ｜ 21D
10-09  C +0.1k / P +0.4k ｜ Activity MEDIUM △ ｜ 28D

📆 09-18 Forward Structure
存量OI:      C 110.3k / P 106.6k
今日变化ΔOI: C +2.2k / P +1.8k
平值价格ATM:  C 4.00 / P 3.90
隐含波动率 ATM IV:  52.4%
净 delta 敞口变化 ΔOI Δ Exposure*: -7k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 132 ｜ +571 ｜ $3.04 ｜ 名义 $173.6k* ｜ -1.3%
P 129 ｜ +408 ｜ $1.76 ｜ 名义 $71.8k* ｜ -3.5%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：132（-1.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 120（结算参考）
量化解读： 存量两侧均衡｜ATM IV 52.4%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 6,757 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 8.3k / P 8.3k
今日变化ΔOI: C +0.9k / P +0.3k
平值价格ATM:  C 5.70 / P 6.60
隐含波动率 ATM IV:  51.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 25k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 145 ｜ +391 ｜ $1.79 ｜ 名义 $70.0k* ｜ +8.5%
C 140 ｜ +195 ｜ $3.02 ｜ 名义 $58.9k* ｜ +4.7%
C 133 ｜ +91 ｜ $6.00 ｜ 名义 $54.6k* ｜ -0.5%
结构参考：145（+8.5%） / 133（-0.5%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 132（结算参考） ｜ Call Wall 145（+8.5%）（OI 1.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 51.1%｜净 delta 敞口 正 24,541 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（Activity LOW）仓位参考: Max Pain 131（结算参考）

10-09（MEDIUM △）Top ΔOI: 133C +29
10-09（MEDIUM △）仓位参考: Max Pain 140（结算参考） ｜ Put Wall 140（+4.7%，弱）（OI 0.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/NOW_morning.json