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
🟡 **单日价格波动**: +2.6%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-18 182C ΔOI +4,962（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 174.05 → 收盘 175.26（+0.7%） ｜ 今日高 182.08 ｜ 低 172.80 ｜ 昨收 172.28 → 收盘 175.26（+1.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.74 | OI比 0.68 | ATM IV 69.8% | Skew 2.3pp | Term 0.93 | ExpMove ±6.9%（近端） | Rank 31%
量化视角： IV 中性（Rank 31%）｜期限结构正常（Term 0.93）｜保护溢价中性（Skew 2.3pp）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.74×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（7D）±6.9% ｜ 09-25（14D）±9.9% ｜ 10-02（21D）±13.2% ｜ 10-09（28D）±13.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 19,786,706 | GEX Change vs 上次快照 -7,939,450 | Flip: Primary Flip: 159.59（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 481 / LOW 149 / INVALID 378
结构观察区: Primary Flip 159.59（全链重定价，覆盖 88%）
Put Wall 160（弱结构｜现价高于该位 9.5%）
最近结构参考: Put Wall 160（现价高于该位 9.5%）
量化视角： 正 Gamma（1979万，无历史分位）｜正 Gamma 减弱（794万）｜现价位于 Flip 上方 9.82%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 160（Put Wall，弱结构）；上方 180（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 160（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 182.5C — Vol 1,694 | 最新价 $3.46 | OI 4373→9335 (ΔOI +4962张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4962张（+113.5% vs前日OI），连续性待观察（方向未知）
09-18 175.0C — Vol 1,608 | 最新价 $6.24 | OI 3204→8022 (ΔOI +4818张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4818张（+150.4% vs前日OI），连续性待观察（方向未知）
09-18 177.5C — Vol 2,006 | 最新价 $5.15 | OI 671→3760 (ΔOI +3089张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3089张（+460.4% vs前日OI），连续性待观察（方向未知）
09-18 190.0C — Vol 2,249 | 最新价 $1.81 | OI 7298→9029 (ΔOI +1731张) | ΔOI/Volume 77.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1731张（+23.7% vs前日OI），连续性待观察（方向未知）
09-18 187.5C — Vol 677 | 最新价 $2.28 | OI 698→1845 (ΔOI +1147张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1147张（+164.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 15,747 张（Put 0 / Call 15,747），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +15.0k / P -0.8k ｜ Activity HIGH ｜ 7D
09-25  C +0.7k / P +0.4k ｜ Activity HIGH ｜ 14D
10-02  C +91 / P +0.4k ｜ Activity MEDIUM △ ｜ 21D
10-09  C +0.1k / P +0.2k ｜ Activity HIGH ｜ 28D

📆 09-18 Forward Structure
存量OI:      C 203.4k / P 97.0k
今日变化ΔOI: C +15.0k / P -0.8k
平值价格ATM:  C 6.24 / P 5.90
隐含波动率 ATM IV:  62.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 707k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 182 ｜ +4,962 ｜ $3.46 ｜ 名义 $1.72M* ｜ +4.1%
C 175 ｜ +4,818 ｜ $6.24 ｜ 名义 $3.01M* ｜ -0.1%
C 177 ｜ +3,089 ｜ $5.15 ｜ 名义 $1.59M* ｜ +1.3%
结构参考：182（+4.1%） / 175（-0.1%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 175（结算参考） ｜ Call Wall 182.5（+4.1%，弱）（OI 9.3k） ｜ Put Wall 160（-8.7%，弱）（OI 9.8k）
量化解读： 存量 Call 重｜ATM IV 62.3%｜历史 Rank 31%（近端代理）｜净 delta 敞口 正 706,606 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 11.4k / P 9.2k
今日变化ΔOI: C +0.7k / P +0.4k
平值价格ATM:  C 8.85 / P 8.59
隐含波动率 ATM IV:  62.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 13k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 175 ｜ +108 ｜ $8.85 ｜ 名义 $95.6k* ｜ -0.1%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：175（-0.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 170（结算参考） ｜ Call Wall 185（+5.6%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 62.7%｜历史 Rank 31%（近端代理）｜净 delta 敞口 正 12,841 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（MEDIUM △）仓位参考: Max Pain 188（结算参考） ｜ Put Wall 172.5（-1.6%，弱）（OI 1.1k）

📆 10-09 Forward Structure
存量OI:      C 1.8k / P 2.5k
今日变化ΔOI: C +0.1k / P +0.2k
平值价格ATM:  C 12.08 / P 12.26
隐含波动率 ATM IV:  64.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 2k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 182（结算参考） ｜ Call Wall 185（+5.6%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜ATM IV 64.8%｜历史 Rank 31%（近端代理）｜净 delta 敞口 正 1,619 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/COIN_evening.json