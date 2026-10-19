# 期权晨报 2026-10-19（快照 10:20 ET）

📊 市场环境

SPY $766.80 ｜ QQQ $718.36
VIX 18.46 ↓7.7%（5D +21.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 23.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🟡 **近现价集中开仓**: 10-20 731P ΔOI +9,672（距现价 -4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 763.25 → 今开 767.23（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 769.04 ｜ 低 765.82

Options: P/C成交量 1.41 | OI比 2.14 | ATM IV 18.4% | Skew 2.9pp | Term 0.77 | ExpMove ±0.7%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价中性（Skew 2.9pp）｜当日成交偏 Put（P/C量 1.41）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.41×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.14×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 31% ｜ P/C OI(近端) 71%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 31%）｜近端持仓结构中性（P/C OI 分位 71%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-20（1D）±0.7% ｜ 10-21（2D）±0.9% ｜ 10-22（3D）±1.1% ｜ 10-23（4D）±1.3%
   ⇒ IV–VIX Spread: -0.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,112,995,918 | GEX Change vs 上次快照 199,265,102 | Flip: Primary Flip: 772.32（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 2866 / LOW 272 / INVALID 1598
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 772.32（全链重定价，覆盖 97%）
最近结构参考: Flip 772（现价低于该位 0.8%）
量化视角： 负 Gamma（11.13亿，历史分位 31%，中性区）｜负 Gamma 缓解（+1.99亿）｜现价位于 Flip 下方 0.81%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 766（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 772（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 750.0P — Vol 95,399 | 最新价 $4.65 | OI 28359→115566 (ΔOI +87207张) | ΔOI/Volume 91.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增87207张（+307.5% vs前日OI），连续性待观察（方向未知）
10-30 735.0P — Vol 87,352 | 最新价 $2.62 | OI 14184→95224 (ΔOI +81040张) | ΔOI/Volume 92.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增81040张（+571.4% vs前日OI），连续性待观察（方向未知）
10-30 510.0P — Vol 34,132 | 最新价 $0.12 | OI 3002→36307 (ΔOI +33305张) | ΔOI/Volume 97.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33305张（+1109.4% vs前日OI），连续性待观察（方向未知）
10-30 515.0P — Vol 29,664 | 最新价 $0.16 | OI 657→29833 (ΔOI +29176张) | ΔOI/Volume 98.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29176张（+4440.8% vs前日OI），连续性待观察（方向未知）
10-23 790.0C — Vol 39,282 | 最新价 $0.03 | OI 12800→36380 (ΔOI +23580张) | ΔOI/Volume 60.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23580张（+184.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 254,308 张（Put 230,728 / Call 23,580），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $62M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 216.1k / P 461.9k，今日成交量: C 406.9k / P 573.0k，平值价格ATM: C $1.69 / P $1.35 ｜ ATM IV 18.4%，预期波动 ±0.4%，Max Pain 766
Top ΔOI: P 734 +16,922 ｜ P 724 +12,220 ｜ C 770 +11,660

📆 Forward Expiration Structure

10-20  C +36.6k / P +55.2k ｜ Activity HIGH ｜ 1D
10-21  C +23.8k / P +68.0k ｜ Activity HIGH ｜ 2D
10-22  C +38.4k / P +43.3k ｜ Activity HIGH ｜ 3D
10-23  C +79.7k / P +136.5k ｜ Activity HIGH ｜ 4D

📆 10-20 Forward Structure
存量OI: C 98.9k / P 187.7k，今日变化ΔOI: C +36.6k / P +55.2k，平值价格ATM: C $3.01 / P $2.54 ｜ ATM IV 15.3%，净 delta 敞口 302k shares
Top ΔOI: P 625 +10,585 ｜ P 731 +9,672 ｜ P 734 +7,559
仓位参考: Max Pain 770 ｜ Call Wall 775（+1.2%，弱）（OI 6.1k） ｜ Put Wall 751（-2.0%，弱）（OI 12.3k）
量化解读： 存量 Put 重｜ATM IV 15.3%｜历史 Rank 81%（近端代理）｜IV/RV 1.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 302,431 股

📆 10-21 Forward Structure
存量OI: C 81.3k / P 191.1k，今日变化ΔOI: C +23.8k / P +68.0k，平值价格ATM: C $3.93 / P $3.36 ｜ ATM IV 15.1%，净 delta 敞口 -177k shares
Top ΔOI: P 741 +14,519 ｜ P 731 +7,844 ｜ P 705 +5,288
仓位参考: Max Pain 769 ｜ Call Wall 773（+0.9%，弱）（OI 3.2k） ｜ Put Wall 746（-2.6%，弱）（OI 10.6k）
量化解读： 存量 Put 重｜ATM IV 15.1%｜历史 Rank 81%（近端代理）｜IV/RV 1.75×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 177,374 股

📆 10-22 Forward Structure
存量OI: C 71.0k / P 75.2k，今日变化ΔOI: C +38.4k / P +43.3k，平值价格ATM: C $4.64 / P $3.99 ｜ ATM IV 14.9%，净 delta 敞口 39k shares
Top ΔOI: C 780 +5,040 ｜ C 784 +4,895 ｜ P 740 +4,766
仓位参考: Max Pain 771 ｜ Call Wall 780（+1.8%，弱）（OI 6.2k） ｜ Put Wall 745（-2.7%，弱）（OI 4.2k）
量化解读： 存量两侧均衡｜ATM IV 14.9%｜历史 Rank 81%（近端代理）｜IV/RV 1.73×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 38,507 股

📆 10-23 Forward Structure
存量OI: C 277.6k / P 500.8k，今日变化ΔOI: C +79.7k / P +136.5k，平值价格ATM: C $5.37 / P $4.54 ｜ ATM IV 14.9%，净 delta 敞口 -920k shares
Top ΔOI: C 790 +23,580 ｜ C 780 +15,472 ｜ P 769 +12,737
仓位参考: Max Pain 770 ｜ Call Wall 780（+1.8%，弱）（OI 24.1k） ｜ Put Wall 745（-2.7%，弱）（OI 38.8k）
量化解读： 存量 Put 重｜ATM IV 14.9%｜历史 Rank 81%（近端代理）｜IV/RV 1.73×（近似）｜净 delta 敞口 负 920,121 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/SPY_morning.json