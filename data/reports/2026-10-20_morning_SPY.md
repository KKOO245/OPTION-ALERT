# 期权晨报 2026-10-20（快照 10:20 ET）

📊 市场环境

SPY $768.68 ｜ QQQ $720.29
VIX 18.12 ↓1.7%（5D +18.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 25.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-21 766P ΔOI +2,556（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 766.48 → 今开 765.86（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 770.05 ｜ 低 764.26

Options: P/C成交量 0.81 | OI比 1.77 | ATM IV 17.6% | Skew 2.7pp | Term 0.80 | ExpMove ±0.7%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价中性（Skew 2.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.81×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.77×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 32% ｜ P/C OI(近端) 44%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 32%）｜近端持仓结构中性（P/C OI 分位 44%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-21（1D）±0.7% ｜ 10-22（2D）±0.9% ｜ 10-23（3D）±1.1% ｜ 10-26（6D）±1.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,061,694,020 | GEX Change vs 上次快照 2,840,231 | Flip: Primary Flip: 773.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 2904 / LOW 281 / INVALID 1547
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 773.61（全链重定价，覆盖 98%）
最近结构参考: Flip 774（现价低于该位 0.7%）
量化视角： 负 Gamma（10.62亿，历史分位 32%，中性区）｜负 Gamma 缓解（+284万）｜现价位于 Flip 下方 0.75%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 768（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 774（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 760.0P — Vol 64,354 | 最新价 $4.86 | OI 73154→130192 (ΔOI +57038张) | ΔOI/Volume 88.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增57038张（+78.0% vs前日OI），连续性待观察（方向未知）
10-30 745.0P — Vol 58,232 | 最新价 $2.26 | OI 74291→124939 (ΔOI +50648张) | ΔOI/Volume 87.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增50648张（+68.2% vs前日OI），连续性待观察（方向未知）
10-23 762.0P — Vol 15,924 | 最新价 $2.79 | OI 1898→15333 (ΔOI +13435张) | ΔOI/Volume 84.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13435张（+707.9% vs前日OI），连续性待观察（方向未知）
10-20 745.0P — Vol 15,700 | 最新价 $0.05 | OI 1591→14779 (ΔOI +13188张) | ΔOI/Volume 84.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13188张（+828.9% vs前日OI），连续性待观察（方向未知）
11-20 730.0P — Vol 37,070 | 最新价 $4.10 | OI 48212→60031 (ΔOI +11819张) | ΔOI/Volume 31.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11819张（+24.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 146,128 张（Put 146,128 / Call 0），跨 4 个期限｜近端保护（5 档，距现价 ≤5%，权利金合计约 $48M，买/卖方向不可观测）｜彩票/名义 1 档（价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 167.8k / P 297.4k，今日成交量: C 697.1k / P 566.3k，平值价格ATM: C $1.42 / P $1.50 ｜ ATM IV 17.6%，预期波动 ±0.4%，Max Pain 768
Top ΔOI: P 745 +13,188 ｜ C 771 +9,462 ｜ P 765 +8,756

📆 Forward Expiration Structure

10-21  C +12.7k / P +22.3k ｜ Activity HIGH ｜ 1D
10-22  C +6.5k / P +14.3k ｜ Activity HIGH ｜ 2D
10-23  C +9.5k / P +71.9k ｜ Activity HIGH ｜ 3D
10-26  C +21.6k / P +24.5k ｜ Activity HIGH ｜ 6D

📆 10-21 Forward Structure
存量OI: C 94.1k / P 213.4k，今日变化ΔOI: C +12.7k / P +22.3k，平值价格ATM: C $2.70 / P $2.69 ｜ ATM IV 14.9%，净 delta 敞口 -34k shares
Top ΔOI: P 766 +2,556 ｜ C 769 +1,667 ｜ P 754 +1,557
仓位参考: Max Pain 769 ｜ Call Wall 778（+1.3%，弱）（OI 4.1k） ｜ Put Wall 746（-2.8%，弱）（OI 11.1k）
量化解读： 存量 Put 重｜ATM IV 14.9%｜历史 Rank 78%（近端代理）｜IV/RV 1.79×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 33,789 股

📆 10-22 Forward Structure
存量OI: C 77.4k / P 89.4k，今日变化ΔOI: C +6.5k / P +14.3k，平值价格ATM: C $3.58 / P $3.45 ｜ ATM IV 14.6%，净 delta 敞口 53k shares
Top ΔOI: P 735 +2,016 ｜ P 737 +1,594 ｜ C 801 +1,423
仓位参考: Max Pain 770 ｜ Call Wall 780（+1.6%，弱）（OI 6.2k） ｜ Put Wall 749（-2.5%，弱）（OI 3.6k）
量化解读： 存量两侧均衡｜ATM IV 14.6%｜历史 Rank 78%（近端代理）｜IV/RV 1.76×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 52,835 股

📆 10-23 Forward Structure
存量OI: C 287.1k / P 572.7k，今日变化ΔOI: C +9.5k / P +71.9k，平值价格ATM: C $4.42 / P $4.10 ｜ ATM IV 14.6%，净 delta 敞口 -696k shares
Top ΔOI: P 762 +13,435 ｜ P 740 +10,158
仓位参考: Max Pain 770 ｜ Call Wall 790（+2.9%）（OI 36.7k） ｜ Put Wall 745（-3.0%，弱）（OI 37.7k）
量化解读： 存量 Put 重｜ATM IV 14.6%｜历史 Rank 78%（近端代理）｜IV/RV 1.75×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 696,001 股

📆 10-26 Forward Structure
存量OI: C 62.8k / P 68.3k，今日变化ΔOI: C +21.6k / P +24.5k，平值价格ATM: C $5.14 / P $4.68 ｜ ATM IV 12.2%，净 delta 敞口 -315k shares
Top ΔOI: P 762 +9,709 ｜ C 805 +6,105 ｜ C 807 +6,058
仓位参考: Max Pain 769 ｜ Call Wall 780（+1.6%，弱）（OI 4.8k） ｜ Put Wall 762（-0.8%）（OI 10.3k）
量化解读： 存量两侧均衡｜ATM IV 12.2%｜历史 Rank 78%（近端代理）｜IV/RV 1.47×（近似）｜净 delta 敞口 负 314,752 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/SPY_morning.json