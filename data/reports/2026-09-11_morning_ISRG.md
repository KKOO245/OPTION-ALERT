# 期权晨报 2026-09-11（快照 10:40 ET）

📊 市场环境

SPY $764.35 ｜ QQQ $714.03
VIX 15.78 ↓11.6%（5D +8.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.1（fear）
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
🟡 **单日价格波动**: +2.4%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-18 362C ΔOI +72（距现价 -1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 360.46 → 今开 363.56（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 374.48 ｜ 低 363.56

Options: P/C成交量 0.26 | OI比 0.73 | ATM IV 49.0% | Skew -1.1pp | Term 0.69 | ExpMove ±4.4%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.69，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.73）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.26×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（7D）±4.4% ｜ 09-25（14D）±5.9% ｜ 10-02（21D）±7.6% ｜ 10-09（28D）±8.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 95,519 | GEX Change vs 上次快照 2,455,672 | Flip: Primary Flip: 368.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 270 / LOW 219 / INVALID 475
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 368.92（全链重定价，覆盖 92%）
Put Wall 350（弱结构｜现价高于该位 5.5%） | Call Wall 400（弱结构｜现价低于该位 7.7%）
最近结构参考: Flip 369（现价高于该位 0.1%）
量化视角： 正 Gamma（10万，无历史分位）｜由负转正（+246万）｜现价位于 Flip 上方 0.09%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 350（Put Wall，弱结构） / 355（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 369（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 375.0C — Vol 165 | 最新价 $0.20 | OI 135→271 (ΔOI +136张) | ΔOI/Volume 82.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增136张（+100.7% vs前日OI），连续性待观察（方向未知）
09-11 380.0C — Vol 142 | 最新价 $0.10 | OI 78→197 (ΔOI +119张) | ΔOI/Volume 83.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增119张（+152.6% vs前日OI），连续性待观察（方向未知）
09-11 340.0P — Vol 168 | 最新价 $0.10 | OI 206→323 (ΔOI +117张) | ΔOI/Volume 69.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增117张（+56.8% vs前日OI），连续性待观察（方向未知）
09-11 335.0P — Vol 140 | 最新价 $0.30 | OI 77→190 (ΔOI +113张) | ΔOI/Volume 80.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增113张（+146.8% vs前日OI），连续性待观察（方向未知）
09-11 365.0C — Vol 302 | 最新价 $1.90 | OI 148→258 (ΔOI +110张) | ΔOI/Volume 36.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增110张（+74.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 595 张（Put 230 / Call 365），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0.2k / P +43 ｜ Activity MEDIUM △ ｜ 7D
09-25  C +50 / P +6 ｜ Activity MEDIUM △ ｜ 14D
10-02  C +46 / P +7 ｜ Activity MEDIUM △ ｜ 21D
10-09  C +1 / P -1 ｜ Activity LOW ｜ 28D

📆 09-18 Forward Structure
存量OI:      C 15.7k / P 16.4k
今日变化ΔOI: C +0.2k / P +43
平值价格ATM:  C 3.68 / P 12.70
隐含波动率 ATM IV:  34.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 10k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 362 ｜ +72 ｜ $6.75 ｜ 名义 $48.6k* ｜ -1.8%
C 370 ｜ +58 ｜ $3.68 ｜ 名义 $21.3k* ｜ +0.2%
P 340 ｜ +42 ｜ $1.15 ｜ 名义 $4.8k* ｜ -7.9%
结构参考：370（+0.2%） / 362（-1.8%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 372（结算参考） ｜ Call Wall 400（+8.3%，弱）（OI 1.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 34.7%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 10,492 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-25（MEDIUM △）Top ΔOI: 362C +22 ｜ 357C +20
09-25（MEDIUM △）仓位参考: Max Pain 365（结算参考） ｜ Put Wall 360（-2.5%，弱）（OI 0.2k）

10-02（MEDIUM △）Top ΔOI: 370C +23 ｜ 390C +9
10-02（MEDIUM △）仓位参考: Max Pain 365（结算参考） ｜ Call Wall 405（+9.7%，弱）（OI 52） ｜ Put Wall 335（-9.3%）（OI 2.4k）

10-09（Activity LOW）仓位参考: Max Pain 350（结算参考） ｜ Call Wall 375（+1.6%，弱）（OI 54）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/ISRG_morning.json