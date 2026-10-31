# 期权晨报 2026-10-30（快照 10:20 ET）

📊 市场环境

SPY $755.72 ｜ QQQ $690.49
VIX 18.77 ↑9.1%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-20 205P ΔOI +667（距现价 -3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-27 190P ΔOI -2,132 占该期限总 OI 15.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 222.30 → 今开 203.48（-8.5%） | 较昨收变动（含盘初走势） ｜ 今日高 215.45 ｜ 低 202.19

Options: P/C成交量 0.65 | OI比 0.75 | ATM IV 130.0% | Skew 9.3pp | Term 0.61 | ExpMove ±10.0%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜保护溢价显著（Skew 9.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（7D）±10.0% ｜ 11-13（14D）±11.4% ｜ 11-20（21D）±16.4% ｜ 11-27（28D）±17.8%
   ⇒ IV–VIX Spread: +111.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,501,047 | GEX Change vs 上次快照 -6,924,872 | Flip: Primary Flip: 215.12（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 553 / LOW 158 / INVALID 229
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 215.12（全链重定价，覆盖 98%）
Put Wall 200（现价高于该位 5.9%）
最近结构参考: Flip 215（现价低于该位 1.5%）
量化视角： 负 Gamma（250万，无历史分位）｜由正转负（692万）｜现价位于 Flip 下方 1.50%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall）；上方 215（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 215（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 225.0P — Vol 3,094 | 最新价 $5.80 | OI 953→2246 (ΔOI +1293张) | ΔOI/Volume 41.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1293张（+135.7% vs前日OI），连续性待观察（方向未知）
12-04 200.0P — Vol 1,557 | 最新价 $11.38 | OI 1188→2331 (ΔOI +1143张) | ΔOI/Volume 73.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1143张（+96.2% vs前日OI），连续性待观察（方向未知）
11-20 205.0P — Vol 844 | 最新价 $9.05 | OI 511→1178 (ΔOI +667张) | ΔOI/Volume 79.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增667张（+130.5% vs前日OI），连续性待观察（方向未知）
10-30 227.5P — Vol 1,874 | 最新价 $7.20 | OI 523→1171 (ΔOI +648张) | ΔOI/Volume 34.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增648张（+123.9% vs前日OI），连续性待观察（方向未知）
10-30 205.0P — Vol 1,538 | 最新价 $0.27 | OI 1955→2575 (ΔOI +620张) | ΔOI/Volume 40.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增620张（+31.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,371 张（Put 4,371 / Call 0），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 67.8k / P 51.1k，今日成交量: C 11.4k / P 7.5k，平值价格ATM: C $2.75 / P $3.35 ｜ ATM IV 130.0%，预期波动 ±2.9%，Max Pain 215
Top ΔOI: P 225 +1,293 ｜ P 227 +648 ｜ P 250 -639

📆 Forward Expiration Structure

11-06  C +0.9k / P +2.0k ｜ Activity HIGH ｜ 7D
11-13  C +0.9k / P +0.4k ｜ Activity HIGH ｜ 14D
11-20  C +0.1k / P +18 ｜ Activity MEDIUM △ ｜ 21D
11-27  C +0.3k / P -1.1k ｜ Activity HIGH ｜ 28D

📆 11-06 Forward Structure
存量OI: C 20.6k / P 21.2k，今日变化ΔOI: C +0.9k / P +2.0k，平值价格ATM: C $10.10 / P $11.00 ｜ ATM IV 87.7%，净 delta 敞口 -59k shares
Top ΔOI: P 215 +375 ｜ P 200 +310
仓位参考: Max Pain 230 ｜ Call Wall 225（+6.2%，弱）（OI 1.4k） ｜ Put Wall 200（-5.6%，弱）（OI 1.1k）
量化解读： 存量两侧均衡｜ATM IV 87.7%｜历史 Rank 82%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 58,542 股

📆 11-13 Forward Structure
存量OI: C 9.6k / P 8.9k，今日变化ΔOI: C +0.9k / P +0.4k，平值价格ATM: C $13.40 / P $10.73 ｜ ATM IV 83.3%，净 delta 敞口 -3k shares
仓位参考: Max Pain 240 ｜ Call Wall 220（+3.8%，弱）（OI 0.3k） ｜ Put Wall 200（-5.6%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜ATM IV 83.3%｜历史 Rank 82%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 2,682 股

11-20（MEDIUM △）Top ΔOI: 195P -1,972 ｜ 205P +667
11-20（MEDIUM △）仓位参考: Max Pain 230 ｜ Call Wall 220（+3.8%，弱）（OI 1.8k） ｜ Put Wall 200（-5.6%，弱）（OI 5.5k）

📆 11-27 Forward Structure
存量OI: C 5.0k / P 8.9k，今日变化ΔOI: C +0.3k / P -1.1k，平值价格ATM: C $19.80 / P $18.00 ｜ ATM IV 79.7%，净 delta 敞口 28k shares
Top ΔOI: P 190 -2,132 ｜ P 200 +485 ｜ P 225 +374
仓位参考: Max Pain 230 ｜ Call Wall 225（+6.2%，弱）（OI 0.6k） ｜ Put Wall 200（-5.6%，弱）（OI 1.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 79.7%｜历史 Rank 82%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 正 27,697 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/BE_morning.json