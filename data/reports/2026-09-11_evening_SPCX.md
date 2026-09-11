# 期权晚报 2026-09-11（快照 17:15 ET）

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
🟡 **单日价格波动**: +2.3%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 150.07 → 收盘 151.21（+0.8%） ｜ 今日高 151.85 ｜ 低 145.92 ｜ 昨收 148.18 → 收盘 151.21（+2.0%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-18，窗口结束前不做对错判定）

Options: P/C成交量 0.48 | OI比 1.27 | ATM IV 68.7% | Skew 2.5pp | Term 0.72 | ExpMove ±5.5%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价中性（Skew 2.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.27×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（7D）±5.5% ｜ 09-25（14D）±7.8% ｜ 10-02（21D）±9.5% ｜ 10-09（28D）±11.0%
   ⇒ IV–VIX Spread: +52.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 87,884,418 | GEX Change vs 上次快照 39,534,683 | Flip: Primary Flip: 142.39（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 560 / LOW 132 / INVALID 412
结构观察区: Primary Flip 142.39（全链重定价，覆盖 88%）
Call Wall 150（弱结构｜现价高于该位 0.8%）
最近结构参考: Call Wall 150（现价高于该位 0.8%）
量化视角： 正 Gamma（8788万，无历史分位）｜正 Gamma 增强（+3953万）｜现价位于 Flip 上方 6.19%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 147（MaxPain，仅结算参考） / 150（Call Wall，弱结构）。
• Gamma 区域：切换参考 142（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 90.0P — Vol 7,483 | 最新价 $0.02 | OI 11434→19078 (ΔOI +7644张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7644张（+66.8% vs前日OI），连续性待观察（方向未知）
09-11 152.5C — Vol 74,090 | 最新价 $0.01 | OI 8898→14799 (ΔOI +5901张) | ΔOI/Volume 8.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5901张（+66.3% vs前日OI），连续性待观察（方向未知）
09-11 155.0C — Vol 35,627 | 最新价 $0.01 | OI 14669→19576 (ΔOI +4907张) | ΔOI/Volume 13.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4907张（+33.5% vs前日OI），连续性待观察（方向未知）
09-11 160.0C — Vol 23,482 | 最新价 $0.01 | OI 26419→30385 (ΔOI +3966张) | ΔOI/Volume 16.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3966张（+15.0% vs前日OI），连续性待观察（方向未知）
09-11 150.0C — Vol 115,504 | 最新价 $1.21 | OI 13765→16711 (ΔOI +2946张) | ΔOI/Volume 2.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2946张（+21.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 25,364 张（Put 7,644 / Call 17,720），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 14D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 21D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 09-18 Forward Structure
存量OI: C 595.0k / P 490.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.80 / P $3.54 ｜ ATM IV 50.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 145 ｜ Call Wall 155（+2.5%，弱）（OI 54.0k） ｜ Put Wall 150（-0.8%）（OI 46.2k）
量化解读： 存量 Call 重｜ATM IV 50.0%｜历史 Rank 72%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 144

10-02（Activity LOW）仓位参考: Max Pain 145

10-09（Activity LOW）仓位参考: Max Pain 146

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/SPCX_evening.json