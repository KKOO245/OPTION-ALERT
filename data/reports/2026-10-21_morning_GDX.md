# 期权晨报 2026-10-21（快照 10:20 ET）

📊 市场环境

SPY $773.28 ｜ QQQ $725.20
VIX 17.20 ↓0.6%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-26 90C ΔOI +1,090（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-26 90C ΔOI +1,090 占该期限总 OI 18.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 86.10 → 今开 86.97（+1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 87.17 ｜ 低 86.16

Options: P/C成交量 0.17 | OI比 1.13 | ATM IV 49.7% | Skew 2.4pp | Term 0.81 | ExpMove ±2.7%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价中性（Skew 2.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.17×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.13×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（2D）±2.7% ｜ 10-26（5D）±3.3% ｜ 10-28（7D）±4.8% ｜ 10-30（9D）±5.9%
   ⇒ IV–VIX Spread: +32.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 28,615,023 | GEX Change vs 上次快照 11,415,080 | Flip: Primary Flip: 85.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 596 / LOW 151 / INVALID 469
结构观察区: Primary Flip 85.03（全链重定价，覆盖 97%）
Call Wall 90（弱结构｜现价低于该位 4.1%）
最近结构参考: Flip 85（现价高于该位 1.6%）
量化视角： 正 Gamma（2862万，无历史分位）｜正 Gamma 增强（+1142万）｜现价位于 Flip 上方 1.56%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 86（MaxPain，仅结算参考）；上方 90（Call Wall，弱结构）。
• Gamma 区域：切换参考 85（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 91.0C — Vol 7,040 | 最新价 $0.94 | OI 5215→11746 (ΔOI +6531张) | ΔOI/Volume 92.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6531张（+125.2% vs前日OI），连续性待观察（方向未知）
10-30 90.0C — Vol 8,089 | 最新价 $1.06 | OI 614→7038 (ΔOI +6424张) | ΔOI/Volume 79.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6424张（+1046.2% vs前日OI），连续性待观察（方向未知）
10-30 60.0P — Vol 3,000 | 最新价 $0.02 | OI 14→3014 (ΔOI +3000张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3000张（+21428.6% vs前日OI），连续性待观察（方向未知）
11-06 70.0P — Vol 1,529 | 最新价 $0.08 | OI 37→1560 (ΔOI +1523张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1523张（+4116.2% vs前日OI），连续性待观察（方向未知）
10-21 90.0C — Vol 2,131 | 最新价 $0.02 | OI 266→1542 (ΔOI +1276张) | ΔOI/Volume 59.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1276张（+479.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 18,754 张（Put 4,523 / Call 14,231），跨 3 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 6.5k / P 7.3k，今日成交量: C 0.7k / P 0.1k，平值价格ATM: C $0.66 / P $0.32 ｜ ATM IV 49.7%，预期波动 ±1.1%，Max Pain 86
Top ΔOI: C 90 +1,276 ｜ P 84 +565 ｜ C 88 +190

📆 Forward Expiration Structure

10-23  C +1.4k / P +0.4k ｜ Activity MEDIUM △ ｜ 2D
10-26  C +1.3k / P +0.5k ｜ Activity HIGH ｜ 5D
10-28  C +0.4k / P +1.2k ｜ Activity HIGH ｜ 7D
10-30  C +13.5k / P +3.6k ｜ Activity HIGH ｜ 9D

📆 10-23 Forward Structure
存量OI: C 97.6k / P 33.4k，今日变化ΔOI: C +1.4k / P +0.4k，平值价格ATM: C $1.22 / P $1.11 ｜ ATM IV 43.5%，净 delta 敞口 35k shares
Top ΔOI: C 90 +256 ｜ C 87 +245 ｜ C 89 +214
仓位参考: Max Pain 86 ｜ Call Wall 90（+4.2%，弱）（OI 12.1k） ｜ Put Wall 85（-1.6%，弱）（OI 5.4k）
量化解读： 存量 Call 重｜ATM IV 43.5%｜历史 Rank 82%（近端代理）｜IV/RV 1.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 35,465 股

📆 10-26 Forward Structure
存量OI: C 4.3k / P 1.6k，今日变化ΔOI: C +1.3k / P +0.5k，平值价格ATM: C $1.65 / P $1.19 ｜ ATM IV 35.0%，净 delta 敞口 8k shares
Top ΔOI: C 90 +1,090 ｜ P 85 +177 ｜ C 88 +159
仓位参考: Max Pain 87 ｜ Call Wall 91（+5.4%，弱）（OI 1.8k） ｜ Put Wall 85（-1.6%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 35.0%｜历史 Rank 82%（近端代理）｜IV/RV 1.13×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 7,601 股

📆 10-28 Forward Structure
存量OI: C 0.8k / P 3.1k，今日变化ΔOI: C +0.4k / P +1.2k，平值价格ATM: C $2.43 / P $1.74 ｜ ATM IV 42.5%，净 delta 敞口 -29k shares
Top ΔOI: P 84 +1,043 ｜ C 90 +173 ｜ C 87 +70
仓位参考: Max Pain 87 ｜ Call Wall 88（+1.9%，弱）（OI 0.2k） ｜ Put Wall 84（-2.7%）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 42.5%｜历史 Rank 82%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 28,896 股

📆 10-30 Forward Structure
存量OI: C 40.0k / P 15.8k，今日变化ΔOI: C +13.5k / P +3.6k，平值价格ATM: C $2.68 / P $2.40 ｜ ATM IV 40.7%，净 delta 敞口 337k shares
Top ΔOI: C 91 +6,531 ｜ C 90 +6,424
仓位参考: Max Pain 87 ｜ Call Wall 91（+5.4%）（OI 11.7k） ｜ Put Wall 85（-1.6%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 40.7%｜历史 Rank 82%（近端代理）｜IV/RV 1.32×（近似）｜净 delta 敞口 正 336,913 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/GDX_morning.json