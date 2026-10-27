# 期权晨报 2026-10-27（快照 10:20 ET）

📊 市场环境

SPY $766.09 ｜ QQQ $715.38
VIX 18.02 ↓2.0%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 1.8 ｜ 前值 0.1　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 700P ΔOI -27,479（距现价 -2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 712.20 → 今开 715.10（+0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 718.19 ｜ 低 713.59

Options: P/C成交量 0.76 | OI比 1.32 | ATM IV 25.4% | Skew 2.0pp | Term 0.87 | ExpMove ±1.3%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价中性（Skew 2.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.76×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.32×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 22% ｜ P/C OI(近端) 23%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 22%）｜近端持仓结构中性（P/C OI 分位 23%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-28（1D）±1.3% ｜ 10-29（2D）±1.8% ｜ 10-30（3D）±2.1% ｜ 11-02（6D）±2.4%
   ⇒ IV–VIX Spread: +7.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -456,615,981 | GEX Change vs 上次快照 217,622,194 | Flip: Primary Flip: 724.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 2914 / LOW 292 / INVALID 1344
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 724.03（全链重定价，覆盖 98%）
最近结构参考: Flip 724（现价低于该位 1.2%）
量化视角： 负 Gamma（4.57亿，历史分位偏负区，比 78% 的交易日更负）｜负 Gamma 缓解（+2.18亿）｜现价位于 Flip 下方 1.22%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 712（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 724（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 675.0P — Vol 38,856 | 最新价 $3.02 | OI 7427→41033 (ΔOI +33606张) | ΔOI/Volume 86.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33606张（+452.5% vs前日OI），连续性待观察（方向未知）
10-30 618.0P — Vol 21,513 | 最新价 $0.09 | OI 497→21405 (ΔOI +20908张) | ΔOI/Volume 97.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20908张（+4206.8% vs前日OI），连续性待观察（方向未知）
10-28 515.0P — Vol 12,930 | 最新价 $0.01 | OI 5057→17900 (ΔOI +12843张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12843张（+254.0% vs前日OI），连续性待观察（方向未知）
10-30 720.0C — Vol 17,347 | 最新价 $4.81 | OI 7821→17121 (ΔOI +9300张) | ΔOI/Volume 53.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9300张（+118.9% vs前日OI），连续性待观察（方向未知）
11-20 760.0C — Vol 9,687 | 最新价 $2.05 | OI 39225→45196 (ΔOI +5971张) | ΔOI/Volume 61.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5971张（+15.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 82,628 张（Put 67,357 / Call 15,271），跨 4 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 143.6k / P 190.0k，今日成交量: C 515.8k / P 393.7k，平值价格ATM: C $1.96 / P $1.96 ｜ ATM IV 25.4%，预期波动 ±0.5%，Max Pain 712
Top ΔOI: P 710 +4,765 ｜ C 721 +4,146 ｜ C 720 +4,145

📆 Forward Expiration Structure

10-28  C +20.6k / P +45.1k ｜ Activity HIGH ｜ 1D
10-29  C +6.0k / P +17.7k ｜ Activity HIGH ｜ 2D
10-30  C +22.7k / P -22.4k ｜ Activity HIGH ｜ 3D
11-02  C +3.5k / P +1.1k ｜ Activity HIGH ｜ 6D

📆 10-28 Forward Structure
存量OI: C 63.0k / P 98.9k，今日变化ΔOI: C +20.6k / P +45.1k，平值价格ATM: C $4.68 / P $4.48 ｜ ATM IV 27.4%，净 delta 敞口 223k shares
仓位参考: Max Pain 715 ｜ Call Wall 715（-0.0%，弱）（OI 4.1k） ｜ Put Wall 710（-0.7%，弱）（OI 4.6k）
量化解读： 存量 Put 重｜ATM IV 27.4%｜历史 Rank 80%（近端代理）｜IV/RV 1.53×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 223,006 股

📆 10-29 Forward Structure
存量OI: C 42.0k / P 72.2k，今日变化ΔOI: C +6.0k / P +17.7k，平值价格ATM: C $6.46 / P $6.20 ｜ ATM IV 28.3%，净 delta 敞口 81k shares
Top ΔOI: P 660 +2,022
仓位参考: Max Pain 717 ｜ Call Wall 725（+1.4%，弱）（OI 2.3k） ｜ Put Wall 705（-1.4%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 28.3%｜历史 Rank 80%（近端代理）｜IV/RV 1.58×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 81,338 股

📆 10-30 Forward Structure
存量OI: C 363.3k / P 759.4k，今日变化ΔOI: C +22.7k / P -22.4k，平值价格ATM: C $7.68 / P $7.14 ｜ ATM IV 27.5%，净 delta 敞口 2.6M shares
Top ΔOI: P 700 -27,479 ｜ P 618 +20,908 ｜ P 690 -18,725
仓位参考: Max Pain 722 ｜ Call Wall 720（+0.7%，弱）（OI 17.1k） ｜ Put Wall 700（-2.1%，弱）（OI 44.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 27.5%｜历史 Rank 80%（近端代理）｜IV/RV 1.53×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,643,616 股

📆 11-02 Forward Structure
存量OI: C 60.7k / P 46.7k，今日变化ΔOI: C +3.5k / P +1.1k，平值价格ATM: C $8.77 / P $8.13 ｜ ATM IV 22.4%，净 delta 敞口 29k shares
Top ΔOI: P 675 -2,115 ｜ P 665 -1,335
仓位参考: Max Pain 714 ｜ Call Wall 720（+0.7%，弱）（OI 9.3k） ｜ Put Wall 695（-2.8%，弱）（OI 5.1k）
量化解读： 存量 Call 重｜ATM IV 22.4%｜历史 Rank 80%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 正 29,087 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/QQQ_morning.json