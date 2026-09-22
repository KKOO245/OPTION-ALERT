# 期权晨报 2026-09-22（快照 10:20 ET）

📊 市场环境

SPY $773.90 ｜ QQQ $745.45
VIX 14.54 ↓2.2%（5D -15.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 37.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-23 735P ΔOI +7,805（距现价 -1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 741.47 → 今开 741.01（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 746.30 ｜ 低 741.00

Options: P/C成交量 0.55 | OI比 1.45 | ATM IV 18.6% | Skew 1.1pp | Term 0.94 | ExpMove ±0.7%（近端） | Rank 51%
量化视角： IV 中性（Rank 51%）｜期限结构正常（Term 0.94）｜保护溢价薄（Skew 1.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.45×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 93% ｜ P/C OI(近端) 33%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 93%）｜近端持仓结构中性（P/C OI 分位 33%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-23（1D）±0.7% ｜ 09-24（2D）±1.0% ｜ 09-25（3D）±1.2% ｜ 09-28（6D）±1.5%
   ⇒ IV–VIX Spread: +4.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 634,963,554 | GEX Change vs 上次快照 25,893,137 | Flip: Primary Flip: 735.46（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 3112 / LOW 265 / INVALID 2145
结构观察区: Primary Flip 735.46（全链重定价，覆盖 97%）
Call Wall 750（弱结构｜现价低于该位 0.7%）
最近结构参考: Call Wall 750（现价低于该位 0.7%）
量化视角： 正 Gamma（6.35亿，历史分位偏正区，比 93% 的交易日更正）｜正 Gamma 增强（+2589万）｜现价位于 Flip 上方 1.29%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 736（MaxPain，仅结算参考）；上方 750（Call Wall，弱结构）。
• Gamma 区域：切换参考 735（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 775.0C — Vol 41,603 | 最新价 $2.80 | OI 6052→45272 (ΔOI +39220张) | ΔOI/Volume 94.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增39220张（+648.0% vs前日OI），连续性待观察（方向未知）
09-30 720.0P — Vol 34,674 | 最新价 $1.93 | OI 3963→33475 (ΔOI +29512张) | ΔOI/Volume 85.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29512张（+744.7% vs前日OI），连续性待观察（方向未知）
09-30 730.0P — Vol 36,096 | 最新价 $3.59 | OI 3210→32455 (ΔOI +29245张) | ΔOI/Volume 81.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29245张（+911.1% vs前日OI），连续性待观察（方向未知）
10-02 715.0P — Vol 34,566 | 最新价 $2.16 | OI 3674→32050 (ΔOI +28376张) | ΔOI/Volume 82.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增28376张（+772.4% vs前日OI），连续性待观察（方向未知）
10-16 760.0C — Vol 32,976 | 最新价 $6.28 | OI 8330→35550 (ΔOI +27220张) | ΔOI/Volume 82.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27220张（+326.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 153,573 张（Put 87,133 / Call 66,440），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $22M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 176.1k / P 254.6k，今日成交量: C 592.2k / P 326.9k，平值价格ATM: C $1.52 / P $1.46 ｜ ATM IV 18.6%，预期波动 ±0.4%，Max Pain 736
Top ΔOI: C 748 +17,971 ｜ P 730 +12,050 ｜ P 698 +11,812

📆 Forward Expiration Structure

09-23  C +33.2k / P +60.9k ｜ Activity HIGH ｜ 1D
09-24  C +14.9k / P +13.6k ｜ Activity HIGH ｜ 2D
09-25  C +54.9k / P +78.7k ｜ Activity HIGH ｜ 3D
09-28  C +9.2k / P +58.8k ｜ Activity HIGH ｜ 6D

📆 09-23 Forward Structure
存量OI: C 78.7k / P 110.0k，今日变化ΔOI: C +33.2k / P +60.9k，平值价格ATM: C $2.79 / P $2.70 ｜ ATM IV 15.6%，净 delta 敞口 407k shares
Top ΔOI: P 735 +7,805 ｜ C 755 +7,254 ｜ P 725 +5,497
仓位参考: Max Pain 731 ｜ Call Wall 755（+1.3%，弱）（OI 7.4k） ｜ Put Wall 735（-1.3%，弱）（OI 7.8k）
量化解读： 存量 Put 重｜ATM IV 15.6%｜历史 Rank 51%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 407,296 股

📆 09-24 Forward Structure
存量OI: C 42.1k / P 53.8k，今日变化ΔOI: C +14.9k / P +13.6k，平值价格ATM: C $3.78 / P $3.70 ｜ ATM IV 16.0%，净 delta 敞口 273k shares
Top ΔOI: C 755 +4,265 ｜ C 750 +3,311 ｜ P 735 +1,805
仓位参考: Max Pain 728 ｜ Call Wall 732（-1.7%，弱）（OI 4.5k） ｜ Put Wall 735（-1.3%，弱）（OI 1.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 16.0%｜历史 Rank 51%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 273,469 股

📆 09-25 Forward Structure
存量OI: C 175.9k / P 438.1k，今日变化ΔOI: C +54.9k / P +78.7k，平值价格ATM: C $4.76 / P $4.42 ｜ ATM IV 16.3%，净 delta 敞口 179k shares
Top ΔOI: C 755 +11,468 ｜ C 745 +7,032
仓位参考: Max Pain 726 ｜ Call Wall 755（+1.3%，弱）（OI 13.0k）
量化解读： 存量 Put 重｜ATM IV 16.3%｜历史 Rank 51%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 179,075 股

📆 09-28 Forward Structure
存量OI: C 25.0k / P 80.1k，今日变化ΔOI: C +9.2k / P +58.8k，平值价格ATM: C $5.58 / P $5.30 ｜ ATM IV 14.0%，净 delta 敞口 44k shares
Top ΔOI: P 663 +6,787
仓位参考: Max Pain 730 ｜ Call Wall 750（+0.7%，弱）（OI 1.9k） ｜ Put Wall 723（-2.9%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 14.0%｜历史 Rank 51%（近端代理）｜IV/RV 0.94×（近似）｜净 delta 敞口 正 44,134 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime RANGE | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/QQQ_morning.json