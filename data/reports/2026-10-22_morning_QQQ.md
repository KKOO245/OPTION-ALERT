# 期权晨报 2026-10-22（快照 10:20 ET）

📊 市场环境

SPY $764.28 ｜ QQQ $704.47
VIX 17.91 ↑7.4%（5D +8.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 19.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 714P ΔOI +4,383（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 725.20 → 今开 713.68（-1.6%） | 较昨收变动（含盘初走势） ｜ 今日高 715.43 ｜ 低 711.53

Options: P/C成交量 0.90 | OI比 1.33 | ATM IV 32.5% | Skew 1.3pp | Term 0.70 | ExpMove ±1.3%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价薄（Skew 1.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.90×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.33×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 6% ｜ P/C OI(近端) 23%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 6%）｜近端持仓结构中性（P/C OI 分位 23%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-23（1D）±1.3% ｜ 10-26（4D）±1.8% ｜ 10-27（5D）±2.1% ｜ 10-28（6D）±2.5%
   ⇒ IV–VIX Spread: +14.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,039,907,199 | GEX Change vs 上次快照 -729,206,543 | Flip: Primary Flip: 730.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 3217 / LOW 317 / INVALID 1616
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 730.03（全链重定价，覆盖 97%）
Put Wall 700（弱结构｜现价高于该位 2.2%）
最近结构参考: Flip 730（现价低于该位 2.0%）
量化视角： 负 Gamma（10.40亿，历史分位偏负区，比 94% 的交易日更负）｜负 Gamma 加深（7.29亿）｜现价位于 Flip 下方 2.02%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 722（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 730（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-22 731.0C — Vol 40,655 | 最新价 $0.94 | OI 728→24354 (ΔOI +23626张) | ΔOI/Volume 58.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23626张（+3245.3% vs前日OI），连续性待观察（方向未知）
10-30 696.0P — Vol 25,397 | 最新价 $2.80 | OI 1638→24347 (ΔOI +22709张) | ΔOI/Volume 89.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22709张（+1386.4% vs前日OI），连续性待观察（方向未知）
10-22 732.0C — Vol 27,019 | 最新价 $0.72 | OI 939→15804 (ΔOI +14865张) | ΔOI/Volume 55.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14865张（+1583.1% vs前日OI），连续性待观察（方向未知）
10-22 668.0P — Vol 13,198 | 最新价 $0.02 | OI 222→13151 (ΔOI +12929张) | ΔOI/Volume 98.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12929张（+5823.9% vs前日OI），连续性待观察（方向未知）
10-26 722.0P — Vol 14,100 | 最新价 $4.97 | OI 334→12767 (ΔOI +12433张) | ΔOI/Volume 88.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12433张（+3722.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 86,562 张（Put 48,071 / Call 38,491），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $13M，买/卖方向不可观测）｜彩票/名义 1 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 178.7k / P 237.1k，今日成交量: C 438.3k / P 395.1k，平值价格ATM: C $2.58 / P $2.46 ｜ ATM IV 32.5%，预期波动 ±0.7%，Max Pain 722
Top ΔOI: C 731 +23,626 ｜ C 732 +14,865 ｜ P 668 +12,929

📆 Forward Expiration Structure

10-23  C +2.3k / P +45.8k ｜ Activity HIGH ｜ 1D
10-26  C +12.4k / P +29.6k ｜ Activity HIGH ｜ 4D
10-27  C +11.8k / P +23.9k ｜ Activity HIGH ｜ 5D
10-28  C +6.4k / P +10.0k ｜ Activity HIGH ｜ 6D

📆 10-23 Forward Structure
存量OI: C 278.5k / P 466.4k，今日变化ΔOI: C +2.3k / P +45.8k，平值价格ATM: C $4.90 / P $4.52 ｜ ATM IV 28.0%，净 delta 敞口 -969k shares
Top ΔOI: P 714 +4,383
仓位参考: Max Pain 726 ｜ Call Wall 735（+2.8%）（OI 25.9k） ｜ Put Wall 710（-0.7%，弱）（OI 46.6k）
量化解读： 存量 Put 重｜ATM IV 28.0%｜历史 Rank 93%（近端代理）｜IV/RV 1.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 968,858 股

📆 10-26 Forward Structure
存量OI: C 46.4k / P 87.1k，今日变化ΔOI: C +12.4k / P +29.6k，平值价格ATM: C $6.70 / P $6.47 ｜ ATM IV 21.1%，净 delta 敞口 -984k shares
Top ΔOI: P 722 +12,433 ｜ C 736 +2,874
仓位参考: Max Pain 725 ｜ Call Wall 736（+2.9%，弱）（OI 3.2k） ｜ Put Wall 722（+0.9%）（OI 12.8k）
量化解读： 存量 Put 重｜ATM IV 21.1%｜历史 Rank 93%（近端代理）｜IV/RV 1.38×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 983,883 股

📆 10-27 Forward Structure
存量OI: C 39.4k / P 62.2k，今日变化ΔOI: C +11.8k / P +23.9k，平值价格ATM: C $7.84 / P $7.32 ｜ ATM IV 22.1%，净 delta 敞口 -60k shares
Top ΔOI: P 630 +8,774 ｜ C 742 +7,299 ｜ P 640 +6,511
仓位参考: Max Pain 728 ｜ Put Wall 722（+0.9%，弱）（OI 1.9k）
量化解读： 存量 Put 重｜ATM IV 22.1%｜历史 Rank 93%（近端代理）｜IV/RV 1.44×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 60,311 股

📆 10-28 Forward Structure
存量OI: C 20.7k / P 26.3k，今日变化ΔOI: C +6.4k / P +10.0k，平值价格ATM: C $9.30 / P $8.68 ｜ ATM IV 24.1%，净 delta 敞口 -309k shares
Top ΔOI: P 720 +2,619 ｜ C 729 +994 ｜ C 750 +944
仓位参考: Max Pain 723 ｜ Call Wall 729（+1.9%，弱）（OI 1.1k） ｜ Put Wall 720（+0.7%）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 24.1%｜历史 Rank 93%（近端代理）｜IV/RV 1.57×（近似）｜净 delta 敞口 负 308,589 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/QQQ_morning.json