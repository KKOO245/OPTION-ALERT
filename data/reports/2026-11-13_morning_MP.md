# 期权晨报 2026-11-13（快照 10:20 ET）

📊 市场环境

SPY $750.54 ｜ QQQ $673.72
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
🟡 **近现价集中开仓**: 12-11 39C ΔOI +23（距现价 +0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-27 33P ΔOI +2,498 占该期限总 OI 22.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 37.45 → 今开 37.34（-0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 39.75 ｜ 低 37.21

Options: P/C成交量 0.20 | OI比 0.31 | ATM IV 129.3% | Skew 15.2pp | Term 0.50 | ExpMove ±10.4%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.50，近月 IV 高于远月）｜保护溢价显著（Skew 15.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.31）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.20×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.31×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±10.4% ｜ 11-27（14D）±4.1% ｜ 12-04（21D）±19.3% ｜ 12-11（28D）±16.2%
   ⇒ IV–VIX Spread: +109.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 7,144,648 | GEX Change vs 上次快照 1,479,318 | Flip: Primary Flip: 35.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 242 / LOW 99 / INVALID 151
结构观察区: Primary Flip 35.43（全链重定价，覆盖 96%）
Put Wall 35（现价高于该位 10.4%）
最近结构参考: Flip 35（现价高于该位 9.1%）
量化视角： 正 Gamma（714万，无历史分位）｜正 Gamma 增强（+148万）｜现价位于 Flip 上方 9.08%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall） / 37（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 35（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 33.0P — Vol 3,123 | 最新价 $0.30 | OI 22→2520 (ΔOI +2498张) | ΔOI/Volume 80.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2498张（+11354.5% vs前日OI），连续性待观察（方向未知）
11-27 50.0C — Vol 1,525 | 最新价 $0.12 | OI 466→1964 (ΔOI +1498张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1498张（+321.5% vs前日OI），连续性待观察（方向未知）
11-13 38.5C — Vol 1,092 | 最新价 $0.35 | OI 589→1152 (ΔOI +563张) | ΔOI/Volume 51.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增563张（+95.6% vs前日OI），连续性待观察（方向未知）
11-20 40.0C — Vol 722 | 最新价 $0.68 | OI 999→1277 (ΔOI +278张) | ΔOI/Volume 38.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增278张（+27.8% vs前日OI），连续性待观察（方向未知）
11-20 42.0C — Vol 492 | 最新价 $0.41 | OI 1416→1693 (ΔOI +277张) | ΔOI/Volume 56.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增277张（+19.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,114 张（Put 2,498 / Call 2,616），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 16.2k / P 5.1k，今日成交量: C 0.9k / P 0.2k，平值价格ATM: C $0.71 / P $0.43 ｜ ATM IV 129.3%，预期波动 ±2.9%，Max Pain 37
Top ΔOI: C 38 +563 ｜ C 38 +235 ｜ C 40 +157

📆 Forward Expiration Structure

11-20  C +0.6k / P +0.3k ｜ Activity HIGH ｜ 7D
11-27  C +1.6k / P +2.7k ｜ Activity HIGH ｜ 14D
12-04  C +73 / P +6 ｜ Activity LOW ｜ 21D
12-11  C +0.2k / P +47 ｜ Activity MEDIUM △ ｜ 28D

📆 11-20 Forward Structure
存量OI: C 26.2k / P 13.5k，今日变化ΔOI: C +0.6k / P +0.3k，平值价格ATM: C $2.08 / P $1.96 ｜ ATM IV 69.0%，净 delta 敞口 38k shares
Top ΔOI: C 40 +278 ｜ C 42 +277
仓位参考: Max Pain 40 ｜ Call Wall 39.5（+2.2%，弱）（OI 2.0k） ｜ Put Wall 35（-9.4%）（OI 3.9k）
量化解读： 存量 Call 重｜ATM IV 69.0%｜历史 Rank 98%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 38,248 股

📆 11-27 Forward Structure
存量OI: C 6.7k / P 4.3k，今日变化ΔOI: C +1.6k / P +2.7k，平值价格ATM: C $1.60 / P $0.00 ｜ ATM IV 70.9%，净 delta 敞口 -14k shares
Top ΔOI: P 33 +2,498
仓位参考: Max Pain 42
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 70.9%｜历史 Rank 98%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 14,206 股

12-04（Activity LOW）仓位参考: Max Pain 35 ｜ Call Wall 35（-9.4%）（OI 0.5k） ｜ Put Wall 35（-9.4%，弱）（OI 0.1k）

12-11（MEDIUM △）Top ΔOI: 37C +44 ｜ 39C +23
12-11（MEDIUM △）仓位参考: Max Pain 42 ｜ Call Wall 37（-4.3%，弱）（OI 71） ｜ Put Wall 42（+8.7%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/MP_morning.json