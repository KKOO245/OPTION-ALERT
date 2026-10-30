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
🟡 **近现价集中开仓**: 11-06 160P ΔOI +1,452（距现价 +0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 171.99 → 今开 157.05（-8.7%） | 较昨收变动（含盘初走势） ｜ 今日高 161.42 ｜ 低 156.33

Options: P/C成交量 0.47 | OI比 0.49 | ATM IV 128.9% | Skew -2.6pp | Term 0.75 | ExpMove ±10.6%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.49）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（7D）±10.6% ｜ 11-13（14D）±18.1% ｜ 11-20（21D）±20.1% ｜ 11-27（28D）±22.1%
   ⇒ IV–VIX Spread: +110.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,058,398 | GEX Change vs 上次快照 -7,494,538 | Flip: Primary Flip: 164.98（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 577 / LOW 88 / INVALID 193
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 164.98（全链重定价，覆盖 100%）
Put Wall 150（弱结构｜现价高于该位 6.3%）
最近结构参考: Flip 165（现价低于该位 3.3%）
量化视角： 负 Gamma（606万，无历史分位）｜由正转负（749万）｜现价位于 Flip 下方 3.35%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall，弱结构）；上方 170（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 165（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 165.0P — Vol 5,125 | 最新价 $1.02 | OI 2139→3638 (ΔOI +1499张) | ΔOI/Volume 29.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1499张（+70.1% vs前日OI），连续性待观察（方向未知）
11-06 160.0P — Vol 2,346 | 最新价 $4.18 | OI 1309→2761 (ΔOI +1452张) | ΔOI/Volume 61.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1452张（+110.9% vs前日OI），连续性待观察（方向未知）
10-30 180.0C — Vol 9,797 | 最新价 $1.05 | OI 3944→5097 (ΔOI +1153张) | ΔOI/Volume 11.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1153张（+29.2% vs前日OI），连续性待观察（方向未知）
11-06 200.0C — Vol 2,700 | 最新价 $1.86 | OI 2485→3418 (ΔOI +933张) | ΔOI/Volume 34.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增933张（+37.5% vs前日OI），连续性待观察（方向未知）
11-13 95.0P — Vol 870 | 最新价 $0.26 | OI 180→978 (ΔOI +798张) | ΔOI/Volume 91.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增798张（+443.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,835 张（Put 3,749 / Call 2,086），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 96.7k / P 47.9k，今日成交量: C 15.0k / P 7.0k，平值价格ATM: C $2.33 / P $2.12 ｜ ATM IV 128.9%，预期波动 ±2.8%，Max Pain 170
Top ΔOI: P 165 +1,499 ｜ P 200 -1,485 ｜ C 180 +1,153

📆 Forward Expiration Structure

11-06  C +4.0k / P +4.3k ｜ Activity HIGH ｜ 7D
11-13  C +1.3k / P +2.0k ｜ Activity HIGH ｜ 14D
11-20  C +0.8k / P +0.4k ｜ Activity HIGH ｜ 21D
11-27  C +0.1k / P +0.1k ｜ Activity MEDIUM △ ｜ 28D

📆 11-06 Forward Structure
存量OI: C 52.4k / P 35.5k，今日变化ΔOI: C +4.0k / P +4.3k，平值价格ATM: C $8.30 / P $8.65 ｜ ATM IV 93.9%，净 delta 敞口 -98k shares
Top ΔOI: P 160 +1,452 ｜ C 200 +933 ｜ P 175 +480
仓位参考: Max Pain 190 ｜ Call Wall 170（+6.6%，弱）（OI 2.5k） ｜ Put Wall 160（+0.3%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 93.9%｜历史 Rank 81%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 负 98,412 股

📆 11-13 Forward Structure
存量OI: C 21.1k / P 20.1k，今日变化ΔOI: C +1.3k / P +2.0k，平值价格ATM: C $14.60 / P $14.18 ｜ ATM IV 111.4%，净 delta 敞口 -31k shares
Top ΔOI: C 230 +504 ｜ C 185 +175
仓位参考: Max Pain 190 ｜ Call Wall 175（+9.8%，弱）（OI 1.1k） ｜ Put Wall 165（+3.5%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 111.4%｜历史 Rank 81%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 30,775 股

📆 11-20 Forward Structure
存量OI: C 92.7k / P 106.8k，今日变化ΔOI: C +0.8k / P +0.4k，平值价格ATM: C $16.27 / P $15.75 ｜ ATM IV 104.1%，净 delta 敞口 22k shares
Top ΔOI: C 190 +513 ｜ C 230 +367
仓位参考: Max Pain 190 ｜ Call Wall 170（+6.6%，弱）（OI 3.0k） ｜ Put Wall 150（-5.9%，弱）（OI 7.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 104.1%｜历史 Rank 81%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 22,304 股

11-27（MEDIUM △）Top ΔOI: 150P +49 ｜ 180P -48
11-27（MEDIUM △）仓位参考: Max Pain 180 ｜ Call Wall 170（+6.6%，弱）（OI 0.5k） ｜ Put Wall 155（-2.8%）（OI 1.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/NBIS_morning.json