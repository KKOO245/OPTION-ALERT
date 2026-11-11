# 期权晨报 2026-11-11（快照 10:20 ET）

📊 市场环境

SPY $759.88 ｜ QQQ $690.38
VIX 18.31 ↓5.9%（5D +10.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-12 744P ΔOI -6,176（距现价 -1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 749.92 → 今开 756.80（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 757.93 ｜ 低 754.91

Options: P/C成交量 1.00 | OI比 1.08 | ATM IV 17.6% | Skew 2.7pp | Term 0.83 | ExpMove ±0.7%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价中性（Skew 2.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.00×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.08×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 54% ｜ P/C OI(近端) 4%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 54%）｜近端持仓极端 Call 重（P/C OI 分位 4%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-12（1D）±0.7% ｜ 11-13（2D）±1.0% ｜ 11-16（5D）±1.2% ｜ 11-17（6D）±1.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -104,760,246 | GEX Change vs 上次快照 1,032,888,559 | Flip: Primary Flip: 757.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 3398 / LOW 278 / INVALID 1700
结构观察区: Primary Flip 757.05（全链重定价，覆盖 99%）
最近结构参考: Flip 757（现价低于该位 0.1%）
量化视角： 负 Gamma（1.05亿，历史分位 54%，中性区）｜负 Gamma 缓解（+10.33亿）｜现价位于 Flip 下方 0.10%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 749（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 757（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 760.0P — Vol 51,385 | 最新价 $10.19 | OI 6054→27552 (ΔOI +21498张) | ΔOI/Volume 41.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21498张（+355.1% vs前日OI），连续性待观察（方向未知）
11-30 760.0C — Vol 14,783 | 最新价 $5.91 | OI 3676→16128 (ΔOI +12452张) | ΔOI/Volume 84.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12452张（+338.7% vs前日OI），连续性待观察（方向未知）
11-30 716.0P — Vol 15,153 | 最新价 $2.49 | OI 4229→15506 (ΔOI +11277张) | ΔOI/Volume 74.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11277张（+266.7% vs前日OI），连续性待观察（方向未知）
11-11 755.0C — Vol 38,594 | 最新价 $0.68 | OI 1849→11580 (ΔOI +9731张) | ΔOI/Volume 25.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9731张（+526.3% vs前日OI），连续性待观察（方向未知）
11-11 760.0C — Vol 27,248 | 最新价 $0.10 | OI 3774→12114 (ΔOI +8340张) | ΔOI/Volume 30.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8340张（+221.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 63,298 张（Put 32,775 / Call 30,523），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $25M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 190.4k / P 206.5k，今日成交量: C 549.6k / P 550.1k，平值价格ATM: C $1.62 / P $1.27 ｜ ATM IV 17.6%，预期波动 ±0.4%，Max Pain 749
Top ΔOI: C 755 +9,731 ｜ C 760 +8,340 ｜ C 750 +8,150

📆 Forward Expiration Structure

11-12  C +23.3k / P +12.2k ｜ Activity HIGH ｜ 1D
11-13  C +48.2k / P +42.5k ｜ Activity HIGH ｜ 2D
11-16  C +17.3k / P +15.6k ｜ Activity HIGH ｜ 5D
11-17  C +7.7k / P +7.1k ｜ Activity HIGH ｜ 6D

📆 11-12 Forward Structure
存量OI: C 90.0k / P 108.4k，今日变化ΔOI: C +23.3k / P +12.2k，平值价格ATM: C $3.00 / P $2.59 ｜ ATM IV 15.7%，净 delta 敞口 911k shares
Top ΔOI: P 744 -6,176 ｜ P 748 +3,778 ｜ C 759 +2,953
仓位参考: Max Pain 748 ｜ Call Wall 775（+2.5%）（OI 6.8k） ｜ Put Wall 744（-1.6%，弱）（OI 13.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 15.7%｜历史 Rank 76%（近端代理）｜IV/RV 0.73×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 911,059 股

📆 11-13 Forward Structure
存量OI: C 364.9k / P 543.4k，今日变化ΔOI: C +48.2k / P +42.5k，平值价格ATM: C $4.12 / P $3.50 ｜ ATM IV 15.9%，净 delta 敞口 -240k shares
Top ΔOI: P 760 +21,498 ｜ P 716 +4,479 ｜ C 779 +4,240
仓位参考: Max Pain 755 ｜ Call Wall 776（+2.6%，弱）（OI 24.3k） ｜ Put Wall 745（-1.5%，弱）（OI 29.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 15.9%｜历史 Rank 76%（近端代理）｜IV/RV 0.74×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 239,542 股

📆 11-16 Forward Structure
存量OI: C 81.9k / P 81.0k，今日变化ΔOI: C +17.3k / P +15.6k，平值价格ATM: C $4.98 / P $4.28 ｜ ATM IV 12.8%，净 delta 敞口 222k shares
Top ΔOI: P 715 +4,440 ｜ P 720 +3,946 ｜ C 788 +3,368
仓位参考: Max Pain 749 ｜ Call Wall 770（+1.8%，弱）（OI 6.5k） ｜ Put Wall 740（-2.1%，弱）（OI 3.8k）
量化解读： 存量两侧均衡｜ATM IV 12.8%｜历史 Rank 76%（近端代理）｜IV/RV 0.59×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 221,846 股

📆 11-17 Forward Structure
存量OI: C 35.5k / P 32.2k，今日变化ΔOI: C +7.7k / P +7.1k，平值价格ATM: C $5.80 / P $5.03 ｜ ATM IV 13.7%，净 delta 敞口 185k shares
Top ΔOI: C 782 +1,574 ｜ P 685 +1,061 ｜ P 715 +588
仓位参考: Max Pain 749 ｜ Call Wall 774（+2.3%，弱）（OI 1.6k） ｜ Put Wall 750（-0.8%，弱）（OI 1.9k）
量化解读： 存量两侧均衡｜ATM IV 13.7%｜历史 Rank 76%（近端代理）｜IV/RV 0.64×（近似）｜净 delta 敞口 正 184,973 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/SPY_morning.json