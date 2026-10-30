# 期权晨报 2026-10-30（快照 10:20 ET）

📊 市场环境

SPY $759.94 ｜ QQQ $692.74
VIX 18.77 ↑9.1%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.5（fear）
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

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 160.59 → 今开 148.23（-7.7%） | 较昨收变动（含盘初走势） ｜ 今日高 148.50 ｜ 低 138.60

Options: P/C成交量 0.23 | OI比 0.66 | ATM IV 130.6% | Skew -0.9pp | Term 0.50 | ExpMove ±8.9%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.50，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.66）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.23×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.66×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（7D）±8.9% ｜ 11-13（14D）±11.7% ｜ 11-20（21D）±13.7% ｜ 11-27（28D）±15.0%
   ⇒ IV–VIX Spread: +111.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,391,402 | GEX Change vs 上次快照 -14,063,741 | Flip: Primary Flip: 147.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 435 / LOW 165 / INVALID 318
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 147.05（全链重定价，覆盖 87%）
最近结构参考: Flip 147（现价低于该位 2.9%）
量化视角： 负 Gamma（439万，无历史分位）｜由正转负（1406万）｜现价位于 Flip 下方 2.92%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 165（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 147（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 145.0P — Vol 3,384 | 最新价 $0.91 | OI 1182→3206 (ΔOI +2024张) | ΔOI/Volume 59.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2024张（+171.2% vs前日OI），连续性待观察（方向未知）
10-30 165.0C — Vol 2,677 | 最新价 $3.70 | OI 851→2405 (ΔOI +1554张) | ΔOI/Volume 58.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1554张（+182.6% vs前日OI），连续性待观察（方向未知）
10-30 155.0P — Vol 1,898 | 最新价 $3.19 | OI 2089→3254 (ΔOI +1165张) | ΔOI/Volume 61.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1165张（+55.8% vs前日OI），连续性待观察（方向未知）
10-30 170.0C — Vol 3,600 | 最新价 $2.16 | OI 6307→7341 (ΔOI +1034张) | ΔOI/Volume 28.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1034张（+16.4% vs前日OI），连续性待观察（方向未知）
10-30 175.0C — Vol 3,382 | 最新价 $1.18 | OI 5041→5817 (ΔOI +776张) | ΔOI/Volume 22.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增776张（+15.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,553 张（Put 3,189 / Call 3,364），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 79.5k / P 52.3k，今日成交量: C 50.2k / P 11.6k，平值价格ATM: C $1.91 / P $2.12 ｜ ATM IV 130.6%，预期波动 ±2.8%，Max Pain 165
Top ΔOI: P 145 +2,024 ｜ C 165 +1,554 ｜ P 155 +1,165

📆 Forward Expiration Structure

11-06  C +2.2k / P +1.7k ｜ Activity HIGH ｜ 7D
11-13  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 14D
11-20  C -76 / P +0.2k ｜ Activity MEDIUM △ ｜ 21D
11-27  C +0.2k / P +0.3k ｜ Activity HIGH ｜ 28D

📆 11-06 Forward Structure
存量OI: C 14.2k / P 22.0k，今日变化ΔOI: C +2.2k / P +1.7k，平值价格ATM: C $6.39 / P $6.28 ｜ ATM IV 77.1%，净 delta 敞口 -83k shares
仓位参考: Max Pain 168 ｜ Put Wall 130（-8.9%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 77.1%｜历史 Rank 96%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 82,677 股

11-13（MEDIUM △）Top ΔOI: 152P +43
11-13（MEDIUM △）仓位参考: Max Pain 172 ｜ Put Wall 155（+8.6%，弱）（OI 1.1k）

11-20（MEDIUM △）Top ΔOI: 160P -338
11-20（MEDIUM △）仓位参考: Max Pain 170 ｜ Put Wall 150（+5.1%，弱）（OI 3.3k）

📆 11-27 Forward Structure
存量OI: C 2.7k / P 1.9k，今日变化ΔOI: C +0.2k / P +0.3k，平值价格ATM: C $9.81 / P $11.60 ｜ ATM IV 65.6%，净 delta 敞口 -7k shares
Top ΔOI: P 130 +60
仓位参考: Max Pain 170 ｜ Put Wall 145（+1.6%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 65.6%｜历史 Rank 96%（近端代理）｜IV/RV 1.29×（近似）｜净 delta 敞口 负 6,919 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/COIN_morning.json