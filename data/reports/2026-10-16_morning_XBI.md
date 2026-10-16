# 期权晨报 2026-10-16（快照 10:20 ET）

📊 市场环境

SPY $763.10 ｜ QQQ $709.80
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
🟡 **近现价集中开仓**: 10-23 148P ΔOI +1,974（距现价 +1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-23 148P ΔOI +1,974 占该期限总 OI 15.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 149.78 → 今开 149.89（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 150.23 ｜ 低 145.78

Options: P/C成交量 1.80 | OI比 1.21 | ATM IV 53.1% | Skew -34.1pp | Term 0.61 | ExpMove ±5.2%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜Put 保护异常便宜（Skew -34.1pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.80×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.21×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-23（7D）±5.2% ｜ 10-30（14D）±4.2% ｜ 11-06（21D）±8.0% ｜ 11-13（28D）±12.6%
   ⇒ IV–VIX Spread: +37.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -47,688,995 | GEX Change vs 上次快照 10,718,507 | Flip: Primary Flip: 157.17（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 81%（带内） ｜ IV 有效性: VALID 334 / LOW 125 / INVALID 321
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 157.17（全链重定价，覆盖 81%）
Put Wall 140（弱结构｜现价高于该位 4.6%）
最近结构参考: Put Wall 140（现价高于该位 4.6%）
量化视角： 负 Gamma（4769万，无历史分位）｜负 Gamma 缓解（+1072万）｜现价位于 Flip 下方 6.87%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（Put Wall，弱结构）；上方 153（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 157（全链重定价，覆盖 81%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 148.0P — Vol 2,029 | 最新价 $1.64 | OI 53→2027 (ΔOI +1974张) | ΔOI/Volume 97.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1974张（+3724.5% vs前日OI），连续性待观察（方向未知）
10-16 152.0C — Vol 924 | 最新价 $0.47 | OI 1139→1912 (ΔOI +773张) | ΔOI/Volume 83.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增773张（+67.9% vs前日OI），连续性待观察（方向未知）
10-23 155.0C — Vol 1,099 | 最新价 $1.07 | OI 969→1705 (ΔOI +736张) | ΔOI/Volume 67.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增736张（+76.0% vs前日OI），连续性待观察（方向未知）
10-23 138.0P — Vol 501 | 最新价 $0.18 | OI 766→1267 (ΔOI +501张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增501张（+65.4% vs前日OI），连续性待观察（方向未知）
10-23 142.0P — Vol 500 | 最新价 $0.60 | OI 23→523 (ΔOI +500张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增500张（+2173.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,484 张（Put 2,975 / Call 1,509），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 46.7k / P 56.5k，今日成交量: C 0.6k / P 1.0k，平值价格ATM: C $0.94 / P $0.76 ｜ ATM IV 53.1%，预期波动 ±1.2%，Max Pain 153
Top ΔOI: C 152 +773 ｜ P 147 -450 ｜ P 150 -407

📆 Forward Expiration Structure

10-23  C +1.2k / P +3.2k ｜ Activity HIGH ｜ 7D
10-30  C +0.3k / P -0.2k ｜ Activity MEDIUM △ ｜ 14D
11-06  C +0.3k / P +0.6k ｜ Activity HIGH ｜ 21D
11-13  C -14 / P -17 ｜ Activity LOW ｜ 28D

📆 10-23 Forward Structure
存量OI: C 4.4k / P 8.3k，今日变化ΔOI: C +1.2k / P +3.2k，平值价格ATM: C $5.30 / P $2.30 ｜ ATM IV 36.1%，净 delta 敞口 -132k shares
Top ΔOI: P 148 +1,974 ｜ C 155 +736 ｜ P 138 +501
仓位参考: Max Pain 153 ｜ Call Wall 155（+5.9%）（OI 1.7k） ｜ Put Wall 148（+1.1%）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 36.1%｜历史 Rank 97%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 131,531 股

10-30（MEDIUM △）Top ΔOI: 145P -250 ｜ 158C +168
10-30（MEDIUM △）仓位参考: Max Pain 152 ｜ Call Wall 155（+5.9%）（OI 0.8k） ｜ Put Wall 140（-4.4%，弱）（OI 6.6k）

📆 11-06 Forward Structure
存量OI: C 0.8k / P 2.0k，今日变化ΔOI: C +0.3k / P +0.6k，平值价格ATM: C $8.55 / P $3.20 ｜ ATM IV 33.0%，净 delta 敞口 -16k shares
Top ΔOI: P 145 +330 ｜ C 155 +299 ｜ P 140 +272
仓位参考: Max Pain 154 ｜ Call Wall 155（+5.9%）（OI 0.3k） ｜ Put Wall 145（-0.9%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 33.0%｜历史 Rank 97%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 15,530 股

11-13（Activity LOW）仓位参考: Max Pain 155 ｜ Call Wall 148（+1.1%，弱）（OI 15） ｜ Put Wall 153（+4.5%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/XBI_morning.json