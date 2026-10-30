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
🟡 **近现价集中开仓**: 11-20 162C ΔOI +499（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 157.79 → 今开 156.68（-0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 159.76 ｜ 低 155.22

Options: P/C成交量 0.17 | OI比 5.09 | ATM IV 59.8% | Skew 5.5pp | Term 0.53 | ExpMove ±4.7%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.53，近月 IV 高于远月）｜保护溢价中性（Skew 5.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.17×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 5.09×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（7D）±4.7% ｜ 11-13（14D）±11.3% ｜ 11-20（21D）±6.5% ｜ 11-27（28D）±7.0%
   ⇒ IV–VIX Spread: +41.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -17,341,975 | GEX Change vs 上次快照 -14,233,357 | Flip: Primary Flip: 162.64（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 80%（带内） ｜ IV 有效性: VALID 369 / LOW 107 / INVALID 306
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 162.64（全链重定价，覆盖 80%）
Call Wall 165（现价低于该位 5.0%）
最近结构参考: Flip 163（现价低于该位 3.7%）
量化视角： 负 Gamma（1734万，无历史分位）｜负 Gamma 加深（1423万）｜现价位于 Flip 下方 3.65%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 155（MaxPain，仅结算参考）；上方 165（Call Wall）。
• Gamma 区域：切换参考 163（全链重定价，覆盖 80%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 158.0P — Vol 4,524 | 最新价 $1.78 | OI 27→1446 (ΔOI +1419张) | ΔOI/Volume 31.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1419张（+5255.6% vs前日OI），连续性待观察（方向未知）
11-20 170.0C — Vol 1,440 | 最新价 $1.40 | OI 1402→2557 (ΔOI +1155张) | ΔOI/Volume 80.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1155张（+82.4% vs前日OI），连续性待观察（方向未知）
10-30 157.0P — Vol 3,012 | 最新价 $1.26 | OI 11→656 (ΔOI +645张) | ΔOI/Volume 21.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增645张（+5863.6% vs前日OI），连续性待观察（方向未知）
10-30 162.0C — Vol 743 | 最新价 $0.14 | OI 199→790 (ΔOI +591张) | ΔOI/Volume 79.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增591张（+297.0% vs前日OI），连续性待观察（方向未知）
11-20 162.0C — Vol 511 | 最新价 $3.00 | OI 182→681 (ΔOI +499张) | ΔOI/Volume 97.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增499张（+274.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,309 张（Put 2,064 / Call 2,245），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 12.9k / P 65.6k，今日成交量: C 0.2k / P 7.6k，平值价格ATM: C $1.05 / P $1.01 ｜ ATM IV 59.8%，预期波动 ±1.3%，Max Pain 155
Top ΔOI: P 158 +1,419 ｜ P 157 +645 ｜ C 162 +591

📆 Forward Expiration Structure

11-06  C +0.7k / P +1.1k ｜ Activity HIGH ｜ 7D
11-13  C +0.4k / P +0.1k ｜ Activity MEDIUM △ ｜ 14D
11-20  C +1.5k / P +1.6k ｜ Activity HIGH ｜ 21D
11-27  C +7 / P +0.1k ｜ Activity MEDIUM △ ｜ 28D

📆 11-06 Forward Structure
存量OI: C 3.3k / P 6.3k，今日变化ΔOI: C +0.7k / P +1.1k，平值价格ATM: C $3.44 / P $3.85 ｜ ATM IV 33.8%，净 delta 敞口 -12k shares
Top ΔOI: P 147 +280 ｜ P 152 +269 ｜ C 159 +199
仓位参考: Max Pain 154 ｜ Call Wall 159（+1.5%，弱）（OI 0.3k） ｜ Put Wall 151（-3.6%）（OI 1.8k）
量化解读： 存量 Put 重｜ATM IV 33.8%｜历史 Rank 99%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 12,029 股

11-13（MEDIUM △）Top ΔOI: 158C +171 ｜ 154P +87
11-13（MEDIUM △）仓位参考: Max Pain 153 ｜ Call Wall 160（+2.1%）（OI 0.4k） ｜ Put Wall 148（-5.6%，弱）（OI 0.2k）

📆 11-20 Forward Structure
存量OI: C 22.3k / P 38.0k，今日变化ΔOI: C +1.5k / P +1.6k，平值价格ATM: C $5.60 / P $4.50 ｜ ATM IV 34.5%，净 delta 敞口 -7k shares
Top ΔOI: C 170 +1,155 ｜ C 162 +499 ｜ P 151 +436
仓位参考: Max Pain 154 ｜ Call Wall 165（+5.3%）（OI 7.1k） ｜ Put Wall 147（-6.2%，弱）（OI 5.2k）
量化解读： 存量 Put 重｜ATM IV 34.5%｜历史 Rank 99%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 6,730 股

11-27（MEDIUM △）Top ΔOI: 159P +53 ｜ 167P +53
11-27（MEDIUM △）仓位参考: Max Pain 158 ｜ Call Wall 158（+0.8%，弱）（OI 68） ｜ Put Wall 156（-0.4%）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/XBI_morning.json