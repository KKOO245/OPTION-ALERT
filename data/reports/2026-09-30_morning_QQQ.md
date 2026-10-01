# 期权晨报 2026-09-30（快照 10:20 ET）

📊 市场环境

SPY $762.63 ｜ QQQ $nan
VIX 15.68 ↓2.2%（5D +3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-01 757C ΔOI +5,787（距现价 +1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 737.93 → 今开 740.19（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 744.73 ｜ 低 739.76

Options: P/C成交量 0.84 | OI比 2.16 | ATM IV 25.7% | Skew 2.4pp | Term 0.75 | ExpMove ±1.0%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜保护溢价中性（Skew 2.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.16×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 80% ｜ P/C OI(近端) 84%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 80%）｜近端持仓结构中性（P/C OI 分位 84%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-01（1D）±1.0% ｜ 10-02（2D）±1.3% ｜ 10-05（5D）±1.6% ｜ 10-06（6D）±1.8%
   ⇒ IV–VIX Spread: +10.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 316,669,512 | GEX Change vs 上次快照 304,847,072 | Flip: Primary Flip: 740.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 2924 / LOW 406 / INVALID 1888
结构观察区: Primary Flip 740.34（全链重定价，覆盖 95%）
Put Wall 730（弱结构｜现价高于该位 1.9%） | Call Wall 760（现价低于该位 2.1%）
最近结构参考: Flip 740（现价高于该位 0.5%）
量化视角： 正 Gamma（3.17亿，历史分位偏正区，比 80% 的交易日更正）｜正 Gamma 增强（+3.05亿）｜现价位于 Flip 上方 0.48%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 730（Put Wall，弱结构） / 735（MaxPain，仅结算参考）；上方 760（Call Wall）。
• Gamma 区域：切换参考 740（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-30 736.0P — Vol 90,454 | 最新价 $2.15 | OI 21750→60352 (ΔOI +38602张) | ΔOI/Volume 42.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增38602张（+177.5% vs前日OI），连续性待观察（方向未知）
09-30 730.0P — Vol 89,859 | 最新价 $0.67 | OI 46520→67863 (ΔOI +21343张) | ΔOI/Volume 23.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21343张（+45.9% vs前日OI），连续性待观察（方向未知）
09-30 605.0P — Vol 10,439 | 最新价 $0.01 | OI 1579→11802 (ΔOI +10223张) | ΔOI/Volume 97.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10223张（+647.4% vs前日OI），连续性待观察（方向未知）
10-02 525.0P — Vol 11,020 | 最新价 $0.01 | OI 222→9634 (ΔOI +9412张) | ΔOI/Volume 85.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9412张（+4239.6% vs前日OI），连续性待观察（方向未知）
09-30 748.0C — Vol 16,704 | 最新价 $0.27 | OI 1907→10519 (ΔOI +8612张) | ΔOI/Volume 51.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8612张（+451.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 88,192 张（Put 79,580 / Call 8,612），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $8M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 337.8k / P 728.4k，今日成交量: C 511.7k / P 441.5k，平值价格ATM: C $2.05 / P $2.08 ｜ ATM IV 25.7%，预期波动 ±0.6%，Max Pain 735
Top ΔOI: P 736 +38,602 ｜ C 726 -26,532 ｜ P 730 +21,343

📆 Forward Expiration Structure

10-01  C +32.1k / P +20.4k ｜ Activity HIGH ｜ 1D
10-02  C +15.9k / P +19.5k ｜ Activity HIGH ｜ 2D
10-05  C +4.4k / P +5.7k ｜ Activity HIGH ｜ 5D
10-06  C +5.9k / P +16.3k ｜ Activity HIGH ｜ 6D

📆 10-01 Forward Structure
存量OI: C 80.7k / P 84.7k，今日变化ΔOI: C +32.1k / P +20.4k，平值价格ATM: C $3.73 / P $3.61 ｜ ATM IV 21.0%，净 delta 敞口 754k shares
Top ΔOI: C 757 +5,787 ｜ C 758 +3,930 ｜ C 750 +2,692
仓位参考: Max Pain 738 ｜ Call Wall 740（-0.5%，弱）（OI 7.6k） ｜ Put Wall 740（-0.5%，弱）（OI 5.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 21.0%｜历史 Rank 82%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 754,087 股

📆 10-02 Forward Structure
存量OI: C 242.0k / P 461.8k，今日变化ΔOI: C +15.9k / P +19.5k，平值价格ATM: C $5.10 / P $4.68 ｜ ATM IV 20.9%，净 delta 敞口 485k shares
Top ΔOI: P 705 -5,982 ｜ P 725 +4,462
仓位参考: Max Pain 730 ｜ Call Wall 725（-2.5%）（OI 35.2k） ｜ Put Wall 730（-1.9%，弱）（OI 49.9k）
量化解读： 存量 Put 重｜ATM IV 20.9%｜历史 Rank 82%（近端代理）｜IV/RV 1.42×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 485,435 股

📆 10-05 Forward Structure
存量OI: C 30.2k / P 88.8k，今日变化ΔOI: C +4.4k / P +5.7k，平值价格ATM: C $6.22 / P $5.56 ｜ ATM IV 16.5%，净 delta 敞口 88k shares
Top ΔOI: P 680 +874 ｜ P 675 +848 ｜ C 762 +724
仓位参考: Max Pain 739 ｜ Call Wall 755（+1.5%）（OI 8.0k）
量化解读： 存量 Put 重｜ATM IV 16.5%｜历史 Rank 82%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 正 87,632 股

📆 10-06 Forward Structure
存量OI: C 15.8k / P 34.2k，今日变化ΔOI: C +5.9k / P +16.3k，平值价格ATM: C $6.90 / P $6.20 ｜ ATM IV 16.9%，净 delta 敞口 179k shares
Top ΔOI: P 715 +1,422
仓位参考: Max Pain 738 ｜ Call Wall 740（-0.5%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜ATM IV 16.9%｜历史 Rank 82%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 正 179,168 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/QQQ_morning.json