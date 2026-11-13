# 期权晨报 2026-11-13（快照 10:20 ET）

📊 市场环境

SPY $750.54 ｜ QQQ $673.58
VIX 19.65 ↑5.1%（5D -23.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 175C ΔOI +2,017（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 171.58 → 今开 171.98（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 172.28 ｜ 低 165.34

Options: P/C成交量 1.16 | OI比 0.66 | ATM IV 73.9% | Skew 2.6pp | Term 0.67 | ExpMove ±6.1%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.67，近月 IV 高于远月）｜保护溢价中性（Skew 2.6pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.66）+ 当日成交偏 Put（P/C量 1.16）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.16×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.66×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±6.1% ｜ 11-27（14D）±8.2% ｜ 12-04（21D）±9.5% ｜ 12-11（28D）±10.8%
   ⇒ IV–VIX Spread: +54.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 40,264,645 | GEX Change vs 上次快照 -16,475,252 | Flip: Primary Flip: 161.10（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 448 / LOW 237 / INVALID 255
结构观察区: Primary Flip 161.10（全链重定价，覆盖 94%）
最近结构参考: Flip 161（现价高于该位 4.4%）
量化视角： 正 Gamma（4026万，无历史分位）｜正 Gamma 减弱（1648万）｜现价位于 Flip 上方 4.39%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 165（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 161（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 177.5C — Vol 3,141 | 最新价 $2.78 | OI 3956→6308 (ΔOI +2352张) | ΔOI/Volume 74.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2352张（+59.5% vs前日OI），连续性待观察（方向未知）
11-20 182.5C — Vol 2,850 | 最新价 $1.48 | OI 3891→5970 (ΔOI +2079张) | ΔOI/Volume 73.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2079张（+53.4% vs前日OI），连续性待观察（方向未知）
11-20 175.0C — Vol 3,954 | 最新价 $3.78 | OI 7474→9491 (ΔOI +2017张) | ΔOI/Volume 51.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2017张（+27.0% vs前日OI），连续性待观察（方向未知）
11-13 165.0P — Vol 8,753 | 最新价 $0.29 | OI 4585→6169 (ΔOI +1584张) | ΔOI/Volume 18.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1584张（+34.5% vs前日OI），连续性待观察（方向未知）
11-20 160.0P — Vol 2,540 | 最新价 $1.44 | OI 7060→8358 (ΔOI +1298张) | ΔOI/Volume 51.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1298张（+18.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,330 张（Put 2,882 / Call 6,448），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 134.7k / P 89.3k，今日成交量: C 13.9k / P 16.1k，平值价格ATM: C $1.84 / P $0.93 ｜ ATM IV 73.9%，预期波动 ±1.7%，Max Pain 165
Top ΔOI: C 167 -3,062 ｜ P 165 +1,584 ｜ C 172 -1,511

📆 Forward Expiration Structure

11-20  C +8.7k / P +3.2k ｜ Activity HIGH ｜ 7D
11-27  C +0.8k / P -0.1k ｜ Activity MEDIUM △ ｜ 14D
12-04  C +0.5k / P +0.5k ｜ Activity MEDIUM △ ｜ 21D
12-11  C +0.7k / P +0.9k ｜ Activity MEDIUM △ ｜ 28D

📆 11-20 Forward Structure
存量OI: C 194.9k / P 193.1k，今日变化ΔOI: C +8.7k / P +3.2k，平值价格ATM: C $5.41 / P $4.85 ｜ ATM IV 53.6%，净 delta 敞口 143k shares
Top ΔOI: C 177 +2,352 ｜ C 182 +2,079 ｜ C 175 +2,017
仓位参考: Max Pain 175 ｜ Call Wall 180（+7.0%，弱）（OI 11.9k） ｜ Put Wall 180（+7.0%，弱）（OI 9.7k）
量化解读： 存量两侧均衡｜ATM IV 53.6%｜历史 Rank 91%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 142,896 股

11-27（MEDIUM △）Top ΔOI: 145C +300 ｜ 210P -297
11-27（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 180（+7.0%，弱）（OI 1.4k） ｜ Put Wall 170（+1.1%，弱）（OI 1.3k）

12-04（MEDIUM △）Top ΔOI: 155P +276 ｜ 185C +139
12-04（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 175（+4.1%，弱）（OI 0.9k） ｜ Put Wall 155（-7.8%）（OI 3.1k）

12-11（MEDIUM △）Top ΔOI: 170P +374 ｜ 175C +314
12-11（MEDIUM △）仓位参考: Max Pain 170 ｜ Call Wall 180（+7.0%，弱）（OI 0.8k） ｜ Put Wall 160（-4.9%，弱）（OI 0.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/PLTR_morning.json