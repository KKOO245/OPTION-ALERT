# 期权晨报 2026-09-11（快照 10:40 ET）

📊 市场环境

SPY $764.42 ｜ QQQ $714.88
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
🟡 **近现价集中开仓**: 09-18 17P ΔOI +67（距现价 -1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 17.36 → 今开 17.36（+0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 17.55 ｜ 低 16.85

Options: P/C成交量 2.68 | OI比 0.63 | ATM IV 97.5% | Skew -0.8pp | Term 0.88 | ExpMove ±9.4%（近端） | Rank 30%
量化视角： IV 中性（Rank 30%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.63）+ 当日成交偏 Put（P/C量 2.68）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 2.68×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（7D）±9.4% ｜ 09-25（14D）±13.3% ｜ 10-02（21D）±14.9% ｜ 10-09（28D）±6.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 756,305 | GEX Change vs 上次快照 146,217 | Flip: Primary Flip: 16.81（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 205 / LOW 96 / INVALID 149
结构观察区: Primary Flip 16.81（全链重定价，覆盖 89%）
Put Wall 16（弱结构｜现价高于该位 8.0%）
最近结构参考: Flip 17（现价高于该位 2.8%）
量化视角： 正 Gamma（76万，无历史分位）｜正 Gamma 增强（+15万）｜现价位于 Flip 上方 2.77%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 16（Put Wall，弱结构）；上方 18（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 17（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 16.0P — Vol 182 | 最新价 $0.30 | OI 513→680 (ΔOI +167张) | ΔOI/Volume 91.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增167张（+32.5% vs前日OI），连续性待观察（方向未知）
09-11 17.0P — Vol 176 | 最新价 $0.20 | OI 384→508 (ΔOI +124张) | ΔOI/Volume 70.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增124张（+32.3% vs前日OI），连续性待观察（方向未知）
09-18 17.0P — Vol 70 | 最新价 $0.60 | OI 401→468 (ΔOI +67张) | ΔOI/Volume 95.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增67张（+16.7% vs前日OI），连续性待观察（方向未知）
09-18 19.0C — Vol 68 | 最新价 $0.30 | OI 1497→1545 (ΔOI +48张) | ΔOI/Volume 70.6% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增48张（+3.2% vs前日OI），值得跟踪（方向未知）
10-09 21.5C — Vol 45 | 最新价 $0.40 | OI 20→64 (ΔOI +44张) | ΔOI/Volume 97.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增44张（+220.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 450 张（Put 358 / Call 92），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0.1k / P +0.3k ｜ Activity HIGH ｜ 7D
09-25  C +34 / P +91 ｜ Activity HIGH ｜ 14D
10-02  C +0 / P +4 ｜ Activity LOW ｜ 21D
10-09  C +44 / P +86 ｜ Activity HIGH ｜ 28D

📆 09-18 Forward Structure
存量OI:      C 7.7k / P 3.8k
今日变化ΔOI: C +0.1k / P +0.3k
平值价格ATM:  C 0.76 / P 0.86
隐含波动率 ATM IV:  83.6%
净 delta 敞口变化 ΔOI Δ Exposure*: -2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 16 ｜ +167 ｜ $0.30 ｜ 名义 $5.0k* ｜ -7.4%
P 17 ｜ +67 ｜ $0.60 ｜ 名义 $4.0k* ｜ -1.6%
C 19 ｜ +48 ｜ $0.30 ｜ 名义 $1.4k* ｜ +10.0%
结构参考：19（+10.0%） / 16（-7.4%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 19（结算参考） ｜ Call Wall 19（+10.0%，弱）（OI 1.5k） ｜ Put Wall 18（+4.2%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 83.6%｜历史 Rank 30%（近端代理）｜净 delta 敞口 负 2,408 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 4.8k / P 1.1k
今日变化ΔOI: C +34 / P +91
平值价格ATM:  C 1.20 / P 1.10
隐含波动率 ATM IV:  86.0%
净 delta 敞口变化 ΔOI Δ Exposure*: -3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 17 ｜ +25 ｜ $1.10 ｜ 名义 $2.8k* ｜ +1.3%
P 16 ｜ +17 ｜ $0.49 ｜ 名义 $833* ｜ -7.4%
P 18 ｜ +17 ｜ $1.75 ｜ 名义 $3.0k* ｜ +7.1%
结构参考：17（+1.3%） / 16（-7.4%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 19（结算参考）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 86.0%｜历史 Rank 30%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,088 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（Activity LOW）仓位参考: Max Pain 19（结算参考） ｜ Put Wall 18.5（+7.1%，弱）（OI 0.1k）

📆 10-09 Forward Structure
存量OI:      C 4.1k / P 0.2k
今日变化ΔOI: C +44 / P +86
平值价格ATM:  C 0.00 / P 1.05
隐含波动率 ATM IV:  85.7%
净 delta 敞口变化 ΔOI Δ Exposure*: -2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 16 ｜ +19 ｜ $0.80 ｜ 名义 $1.5k* ｜ -7.4%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：16（-7.4%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 19（结算参考） ｜ Put Wall 16（-7.4%）（OI 66）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 85.7%｜历史 Rank 30%（近端代理）｜净 delta 敞口 负 2,467 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/NNE_morning.json