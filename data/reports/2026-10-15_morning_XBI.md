# 期权晨报 2026-10-15（快照 10:20 ET）

📊 市场环境

SPY $770.81 ｜ QQQ $724.00
VIX 17.51 ↑3.8%（5D +13.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 150P ΔOI -7,539（距现价 +0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-23 145P ΔOI +841 占该期限总 OI 10.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 146.77 → 今开 147.71（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 150.46 ｜ 低 146.93

Options: P/C成交量 6.23 | OI比 1.25 | ATM IV 35.8% | Skew -4.2pp | Term 0.93 | ExpMove ±2.0%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构正常（Term 0.93）｜Put 保护异常便宜（Skew -4.2pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 6.23）——观察点，非方向信号
   ⇒ Put/Call Volume: 6.23×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.25×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-16（1D）±2.0% ｜ 10-23（8D）±4.5% ｜ 10-30（15D）±5.5% ｜ 11-06（22D）±5.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -54,047,471 | GEX Change vs 上次快照 16,308,047 | Flip: Primary Flip: 154.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 83%（带内） ｜ IV 有效性: VALID 345 / LOW 118 / INVALID 317
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 154.63（全链重定价，覆盖 83%）
Put Wall 150（弱结构｜现价低于该位 0.0%）
最近结构参考: Put Wall 150（现价低于该位 0.0%）
量化视角： 负 Gamma（5405万，无历史分位）｜负 Gamma 缓解（+1631万）｜现价位于 Flip 下方 3.03%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（Put Wall，弱结构） / 153（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 155（全链重定价，覆盖 83%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 145.0P — Vol 1,023 | 最新价 $2.07 | OI 396→1237 (ΔOI +841张) | ΔOI/Volume 82.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增841张（+212.4% vs前日OI），连续性待观察（方向未知）
10-23 138.0P — Vol 751 | 最新价 $0.56 | OI 18→766 (ΔOI +748张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增748张（+4155.6% vs前日OI），连续性待观察（方向未知）
10-23 155.0C — Vol 798 | 最新价 $0.89 | OI 270→969 (ΔOI +699张) | ΔOI/Volume 87.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增699张（+258.9% vs前日OI），连续性待观察（方向未知）
10-23 147.0P — Vol 442 | 最新价 $2.86 | OI 48→396 (ΔOI +348张) | ΔOI/Volume 78.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增348张（+725.0% vs前日OI），连续性待观察（方向未知）
10-30 145.0P — Vol 359 | 最新价 $2.82 | OI 282→575 (ΔOI +293张) | ΔOI/Volume 81.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增293张（+103.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,929 张（Put 2,230 / Call 699），跨 2 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C -1.0k / P -11.8k ｜ Activity MEDIUM △ ｜ 1D
10-23  C +0.7k / P +2.2k ｜ Activity HIGH ｜ 8D
10-30  C -0.4k / P -0.7k ｜ Activity MEDIUM △ ｜ 15D
11-06  C +88 / P +0.2k ｜ Activity MEDIUM △ ｜ 22D

📆 10-16 Forward Structure
存量OI: C 46.2k / P 57.6k，今日变化ΔOI: C -1.0k / P -11.8k，平值价格ATM: C $0.50 / P $2.44 ｜ ATM IV 35.8%，净 delta 敞口 948k shares
Top ΔOI: P 150 -7,539 ｜ P 160 -970 ｜ C 155 -777
仓位参考: Max Pain 153 ｜ Put Wall 150（+0.0%，弱）（OI 8.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 35.8%｜历史 Rank 64%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 947,559 股

📆 10-23 Forward Structure
存量OI: C 3.3k / P 5.0k，今日变化ΔOI: C +0.7k / P +2.2k，平值价格ATM: C $1.90 / P $4.89 ｜ ATM IV 31.9%，净 delta 敞口 -49k shares
Top ΔOI: P 145 +841 ｜ P 138 +748 ｜ C 155 +699
仓位参考: Max Pain 153 ｜ Call Wall 155（+3.4%）（OI 1.0k） ｜ Put Wall 145（-3.3%）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 31.9%｜历史 Rank 64%（近端代理）｜IV/RV 1.13×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 49,404 股

10-30（MEDIUM △）Top ΔOI: 150P -724 ｜ 155C -555
10-30（MEDIUM △）仓位参考: Max Pain 152 ｜ Call Wall 155（+3.4%）（OI 0.8k） ｜ Put Wall 150（+0.0%，弱）（OI 6.5k）

11-06（MEDIUM △）Top ΔOI: 139P +70 ｜ 141P +51
11-06（MEDIUM △）仓位参考: Max Pain 154 ｜ Call Wall 150（+0.0%，弱）（OI 33） ｜ Put Wall 143（-4.6%）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/XBI_morning.json