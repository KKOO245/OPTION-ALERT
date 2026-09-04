# 期权晚报 2026-09-04（快照 17:18 ET）

📊 市场环境

SPY $770.19 ｜ QQQ $718.96
VIX 14.53 ↑1.5%（5D +0.7%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **单日价格波动**: +5.0%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🔵 **Flip 状态**: CONDITIONAL（Candidates: 1539.4）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,585.59 → 收盘 1,740.00（+9.7%） ｜ 今日高 1740.00 ｜ 低 1581.00 ｜ 昨收 1,554.99 → 收盘 1,740.00（+11.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.77 | OI比 1.06 | ATM IV 46.7% | Skew 7.8pp | Term 1.62 | ExpMove ±8.0%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常偏陡（Term 1.62）｜保护溢价显著（Skew 7.8pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.06×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（7D）±8.0% ｜ 09-18（14D）±11.6% ｜ 09-25（21D）±14.5% ｜ 10-02（28D）±16.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 13,359,807 | GEX Change vs 上次快照 -3,042,770 | Flip: Candidates 1539.35 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 68%（带内） ｜ IV 有效性: VALID 1691 / LOW 486 / INVALID 1345
结构观察区: ≈1539（全链重定价，覆盖 68%，CONDITIONAL）
Call Wall 1,700（弱结构｜现价高于该位 2.4%）
最近结构参考: Call Wall 1700（现价高于该位 2.4%）
量化视角： 正 Gamma（1336万，无历史分位）｜正 Gamma 减弱（304万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,500（MaxPain，仅结算参考） / 1,700（Call Wall，弱结构）。
• Gamma 区域：切换参考 1539（全链重定价，覆盖 68%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 1390.0C — Vol 2 | 最新价 $284.85 | OI 11→1535 (ΔOI +1524张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1524张（+13854.5% vs前日OI），连续性待观察（方向未知）
09-04 1700.0C — Vol 21,505 | 最新价 $40.00 | OI 2704→4045 (ΔOI +1341张) | ΔOI/Volume 6.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1341张（+49.6% vs前日OI），连续性待观察（方向未知）
09-04 1580.0C — Vol 1,351 | 最新价 $159.00 | OI 533→1275 (ΔOI +742张) | ΔOI/Volume 54.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增742张（+139.2% vs前日OI），连续性待观察（方向未知）
09-04 1650.0C — Vol 9,210 | 最新价 $89.62 | OI 1650→2321 (ΔOI +671张) | ΔOI/Volume 7.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增671张（+40.7% vs前日OI），连续性待观察（方向未知）
09-04 1595.0C — Vol 631 | 最新价 $117.04 | OI 176→846 (ΔOI +670张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增670张（+380.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,948 张（Put 0 / Call 4,948），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 14D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 21D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 15.1k / P 16.3k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 69.40 / P 69.10
隐含波动率 ATM IV:  71.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 1,500（结算参考）
量化解读： 存量两侧均衡｜ATM IV 71.9%｜历史 Rank 3%（近端代理）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 1,430（结算参考）

09-25（Activity LOW）仓位参考: Max Pain 1,535（结算参考）

10-02（Activity LOW）仓位参考: Max Pain 1,505（结算参考） ｜ Call Wall 1800（+3.4%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/SNDK_evening.json