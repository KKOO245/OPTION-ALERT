# 期权晨报 2026-10-30（快照 10:20 ET）

📊 市场环境

SPY $756.15 ｜ QQQ $690.49
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
🟡 **近现价集中开仓**: 11-06 125P ΔOI +3,709（距现价 -3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 141.62 → 今开 131.52（-7.1%） | 较昨收变动（含盘初走势） ｜ 今日高 131.56 ｜ 低 124.22

Options: P/C成交量 0.29 | OI比 0.63 | ATM IV 139.1% | Skew -1.1pp | Term 0.52 | ExpMove ±9.3%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.52，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.29×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（7D）±9.3% ｜ 11-13（14D）±12.4% ｜ 11-20（21D）±15.2% ｜ 11-27（28D）±15.8%
   ⇒ IV–VIX Spread: +120.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -28,483 | GEX Change vs 上次快照 -31,046,972 | Flip: Primary Flip: 128.82（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 572 / LOW 111 / INVALID 255
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 128.82（全链重定价，覆盖 98%）
Call Wall 135（弱结构｜现价低于该位 4.6%）
最近结构参考: Flip 129（现价低于该位 0.0%）
量化视角： 负 Gamma（3万，无历史分位）｜由正转负（3105万）｜现价位于 Flip 下方 0.01%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 141（MaxPain，仅结算参考） / 135（Call Wall，弱结构）。
• Gamma 区域：切换参考 129（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 125.0P — Vol 4,379 | 最新价 $1.23 | OI 2398→6107 (ΔOI +3709张) | ΔOI/Volume 84.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3709张（+154.7% vs前日OI），连续性待观察（方向未知）
11-06 118.0P — Vol 3,312 | 最新价 $0.58 | OI 1194→4435 (ΔOI +3241张) | ΔOI/Volume 97.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3241张（+271.4% vs前日OI），连续性待观察（方向未知）
11-06 152.5C — Vol 3,882 | 最新价 $2.79 | OI 1068→3732 (ΔOI +2664张) | ΔOI/Volume 68.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2664张（+249.4% vs前日OI），连续性待观察（方向未知）
11-06 146.0C — Vol 2,359 | 最新价 $4.80 | OI 457→2300 (ΔOI +1843张) | ΔOI/Volume 78.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1843张（+403.3% vs前日OI），连续性待观察（方向未知）
11-06 170.0C — Vol 1,988 | 最新价 $0.62 | OI 1321→3060 (ΔOI +1739张) | ΔOI/Volume 87.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1739张（+131.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 13,196 张（Put 6,950 / Call 6,246），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 251.3k / P 158.2k，今日成交量: C 158.2k / P 45.8k，平值价格ATM: C $1.77 / P $2.07 ｜ ATM IV 139.1%，预期波动 ±3.0%，Max Pain 141
Top ΔOI: P 160 -2,546 ｜ P 165 -1,563 ｜ C 157 +1,488

📆 Forward Expiration Structure

11-06  C +13.9k / P +14.3k ｜ Activity HIGH ｜ 7D
11-13  C +0.9k / P +4.5k ｜ Activity HIGH ｜ 14D
11-20  C +0.5k / P +2.8k ｜ Activity HIGH ｜ 21D
11-27  C +0.3k / P +2.4k ｜ Activity MEDIUM △ ｜ 28D

📆 11-06 Forward Structure
存量OI: C 43.0k / P 80.3k，今日变化ΔOI: C +13.9k / P +14.3k，平值价格ATM: C $5.90 / P $6.10 ｜ ATM IV 81.9%，净 delta 敞口 -341k shares
Top ΔOI: P 125 +3,709 ｜ P 118 +3,241 ｜ C 152 +2,664
仓位参考: Max Pain 150 ｜ Put Wall 125（-3.0%，弱）（OI 6.1k）
量化解读： 存量 Put 重｜ATM IV 81.9%｜历史 Rank 95%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 340,782 股

📆 11-13 Forward Structure
存量OI: C 21.6k / P 51.3k，今日变化ΔOI: C +0.9k / P +4.5k，平值价格ATM: C $8.00 / P $8.00 ｜ ATM IV 78.3%，净 delta 敞口 -86k shares
Top ΔOI: P 105 +534 ｜ P 110 +531
仓位参考: Max Pain 160 ｜ Put Wall 140（+8.7%，弱）（OI 1.7k）
量化解读： 存量 Put 重｜ATM IV 78.3%｜历史 Rank 95%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 86,324 股

📆 11-20 Forward Structure
存量OI: C 148.3k / P 117.2k，今日变化ΔOI: C +0.5k / P +2.8k，平值价格ATM: C $10.10 / P $9.45 ｜ ATM IV 76.6%，净 delta 敞口 -56k shares
Top ΔOI: P 100 +556 ｜ P 105 +533 ｜ P 95 +492
仓位参考: Max Pain 135 ｜ Call Wall 135（+4.8%）（OI 42.4k） ｜ Put Wall 120（-6.8%，弱）（OI 6.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 76.6%｜历史 Rank 95%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 56,256 股

11-27（MEDIUM △）Top ΔOI: 95P +395 ｜ 100P +349
11-27（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 140（+8.7%，弱）（OI 0.3k） ｜ Put Wall 140（+8.7%，弱）（OI 2.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/MSTR_morning.json