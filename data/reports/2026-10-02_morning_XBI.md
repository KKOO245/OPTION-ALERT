# 期权晨报 2026-10-02（快照 10:20 ET）

📊 市场环境

SPY $771.73 ｜ QQQ $754.01
VIX 15.56 ↓5.1%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 155P ΔOI +3,003（距现价 -0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 148P ΔOI +3,118 占该期限总 OI 25.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 154.51 → 今开 156.41（+1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 156.73 ｜ 低 154.83

Options: P/C成交量 0.89 | OI比 1.86 | ATM IV 79.0% | Skew 1.2pp | Term 0.40 | ExpMove ±3.2%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.40，近月 IV 高于远月）｜保护溢价薄（Skew 1.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.89×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.86×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±3.2% ｜ 10-16（14D）±4.9% ｜ 10-23（21D）±5.4% ｜ 10-30（28D）±7.2%
   ⇒ IV–VIX Spread: +63.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -48,825,075 | GEX Change vs 上次快照 2,570,887 | Flip: Primary Flip: 164.70（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 330 / LOW 105 / INVALID 329
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 164.70（全链重定价，覆盖 88%）
Put Wall 150（现价高于该位 3.9%）
最近结构参考: Put Wall 150（现价高于该位 3.9%）
量化视角： 负 Gamma（4883万，无历史分位）｜负 Gamma 缓解（+257万）｜现价位于 Flip 下方 5.35%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall）；上方 156（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 165（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 140.0P — Vol 5,814 | 最新价 $0.86 | OI 708→6382 (ΔOI +5674张) | ΔOI/Volume 97.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5674张（+801.4% vs前日OI），连续性待观察（方向未知）
10-30 150.0P — Vol 5,502 | 最新价 $3.20 | OI 34→5514 (ΔOI +5480张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5480张（+16117.6% vs前日OI），连续性待观察（方向未知）
10-09 148.0P — Vol 3,121 | 最新价 $0.65 | OI 14→3132 (ΔOI +3118张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3118张（+22271.4% vs前日OI），连续性待观察（方向未知）
10-09 155.0P — Vol 3,017 | 最新价 $2.13 | OI 338→3341 (ΔOI +3003张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3003张（+888.5% vs前日OI），连续性待观察（方向未知）
10-16 155.0P — Vol 2,181 | 最新价 $4.19 | OI 1196→2578 (ΔOI +1382张) | ΔOI/Volume 63.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1382张（+115.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 18,657 张（Put 18,657 / Call 0），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 14.2k / P 26.4k，今日成交量: C 0.2k / P 0.2k，平值价格ATM: C $0.85 / P $1.09 ｜ ATM IV 79.0%，预期波动 ±1.2%，Max Pain 156
Top ΔOI: P 145 -645 ｜ C 164 +439 ｜ P 148 -354

📆 Forward Expiration Structure

10-09  C +0.7k / P +6.6k ｜ Activity HIGH ｜ 7D
10-16  C -0.6k / P +2.8k ｜ Activity MEDIUM △ ｜ 14D
10-23  C +14 / P -93 ｜ Activity LOW ｜ 21D
10-30  C +18 / P +11.1k ｜ Activity HIGH ｜ 28D

📆 10-09 Forward Structure
存量OI: C 1.8k / P 10.4k，今日变化ΔOI: C +0.7k / P +6.6k，平值价格ATM: C $2.21 / P $2.71 ｜ ATM IV 29.0%，净 delta 敞口 -202k shares
Top ΔOI: P 148 +3,118 ｜ P 155 +3,003 ｜ C 162 +254
仓位参考: Max Pain 156 ｜ Call Wall 162（+3.9%，弱）（OI 0.3k） ｜ Put Wall 155（-0.6%，弱）（OI 3.3k）
量化解读： 存量 Put 重｜ATM IV 29.0%｜历史 Rank 100%（近端代理）｜IV/RV 1.15×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 201,902 股

10-16（MEDIUM △）Top ΔOI: 155P +1,382 ｜ 154P +890
10-16（MEDIUM △）仓位参考: Max Pain 161 ｜ Call Wall 165（+5.8%，弱）（OI 3.0k） ｜ Put Wall 150（-3.8%）（OI 22.6k）

10-23（Activity LOW）仓位参考: Max Pain 155 ｜ Call Wall 154（-1.2%，弱）（OI 81） ｜ Put Wall 153（-1.9%，弱）（OI 0.4k）

📆 10-30 Forward Structure
存量OI: C 1.8k / P 14.0k，今日变化ΔOI: C +18 / P +11.1k，平值价格ATM: C $5.86 / P $5.29 ｜ ATM IV 31.7%，净 delta 敞口 -248k shares
Top ΔOI: P 140 +5,674 ｜ P 150 +5,480
仓位参考: Max Pain 159 ｜ Call Wall 161（+3.3%，弱）（OI 0.3k） ｜ Put Wall 150（-3.8%，弱）（OI 5.5k）
量化解读： 存量 Put 重｜ATM IV 31.7%｜历史 Rank 100%（近端代理）｜IV/RV 1.26×（近似）｜净 delta 敞口 负 248,030 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=39 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=39）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/XBI_morning.json