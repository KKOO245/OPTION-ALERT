# 期权晨报 2026-10-16（快照 10:20 ET）

📊 市场环境

SPY $763.25 ｜ QQQ $nan
VIX 15.93 ↓3.2%（5D +7.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 17.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-06 43C ΔOI +688（距现价 +3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 41.61 → 今开 41.30（-0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 42.20 ｜ 低 41.02

Options: P/C成交量 2.27 | OI比 0.49 | ATM IV 87.2% | Skew -13.5pp | Term 0.82 | ExpMove ±6.4%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜Put 保护异常便宜（Skew -13.5pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.49）+ 当日成交偏 Put（P/C量 2.27）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 2.27×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（7D）±6.4% ｜ 10-30（14D）±9.2% ｜ 11-06（21D）±14.0% ｜ 11-13（28D）±14.9%
   ⇒ IV–VIX Spread: +71.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 904,476 | GEX Change vs 上次快照 4,055,955 | Flip: Primary Flip: 40.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 270 / LOW 73 / INVALID 103
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 40.68（全链重定价，覆盖 85%）
Put Wall 45（现价低于该位 7.4%）
最近结构参考: Flip 41（现价高于该位 2.4%）
量化视角： 正 Gamma（90万，无历史分位）｜由负转正（+406万）｜现价位于 Flip 上方 2.43%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 45（Put Wall） / 45（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 41（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 50.0C — Vol 1,336 | 最新价 $0.99 | OI 1911→3112 (ΔOI +1201张) | ΔOI/Volume 89.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1201张（+62.9% vs前日OI），连续性待观察（方向未知）
10-16 55.0C — Vol 842 | 最新价 $0.01 | OI 2372→3111 (ΔOI +739张) | ΔOI/Volume 87.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增739张（+31.2% vs前日OI），连续性待观察（方向未知）
11-06 43.0C — Vol 696 | 最新价 $2.23 | OI 25→713 (ΔOI +688张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增688张（+2752.0% vs前日OI），连续性待观察（方向未知）
10-16 43.5C — Vol 762 | 最新价 $0.12 | OI 323→886 (ΔOI +563张) | ΔOI/Volume 73.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增563张（+174.3% vs前日OI），连续性待观察（方向未知）
10-16 46.0C — Vol 522 | 最新价 $0.02 | OI 442→911 (ΔOI +469张) | ΔOI/Volume 89.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增469张（+106.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,660 张（Put 0 / Call 3,660），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 27.2k / P 13.2k，今日成交量: C 1.7k / P 0.7k，平值价格ATM: C $0.55 / P $0.28 ｜ ATM IV 87.2%，预期波动 ±2.0%，Max Pain 45
Top ΔOI: C 55 +739 ｜ C 43 +563 ｜ C 46 +469

📆 Forward Expiration Structure

10-23  C +0.5k / P +0.4k ｜ Activity MEDIUM △ ｜ 7D
10-30  C +71 / P +53 ｜ Activity MEDIUM △ ｜ 14D
11-06  C +1.6k / P +0.4k ｜ Activity HIGH ｜ 21D
11-13  C +59 / P +0.2k ｜ Activity MEDIUM △ ｜ 28D

📆 10-23 Forward Structure
存量OI: C 5.2k / P 3.9k，今日变化ΔOI: C +0.5k / P +0.4k，平值价格ATM: C $1.51 / P $1.15 ｜ ATM IV 59.1%，净 delta 敞口 5k shares
Top ΔOI: C 45 +105 ｜ P 47 +99 ｜ C 42 +94
仓位参考: Max Pain 45 ｜ Call Wall 45（+8.0%，弱）（OI 0.3k） ｜ Put Wall 42（+0.8%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 59.1%｜历史 Rank 83%（近端代理）｜IV/RV 1.19×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 5,219 股

10-30（MEDIUM △）Top ΔOI: 41C +27 ｜ 44P +24
10-30（MEDIUM △）仓位参考: Max Pain 45 ｜ Call Wall 45（+8.0%，弱）（OI 0.3k） ｜ Put Wall 44（+5.6%）（OI 1.7k）

📆 11-06 Forward Structure
存量OI: C 4.9k / P 3.4k，今日变化ΔOI: C +1.6k / P +0.4k，平值价格ATM: C $2.60 / P $3.25 ｜ ATM IV 71.1%，净 delta 敞口 54k shares
Top ΔOI: C 43 +688 ｜ C 45 +437 ｜ C 44 +214
仓位参考: Max Pain 43 ｜ Call Wall 45（+8.0%，弱）（OI 0.7k） ｜ Put Wall 38（-8.8%）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 71.1%｜历史 Rank 83%（近端代理）｜IV/RV 1.43×（近似）｜净 delta 敞口 正 53,540 股

11-13（MEDIUM △）Top ΔOI: 42P +50 ｜ 39P +34
11-13（MEDIUM △）仓位参考: Max Pain 50 ｜ Put Wall 39（-6.4%）（OI 0.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/MP_morning.json