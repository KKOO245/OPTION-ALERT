# 期权晨报 2026-11-17（快照 10:20 ET）

📊 市场环境

SPY $734.29 ｜ QQQ $656.95
VIX 22.73 ↓0.8%（5D +16.8%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.8　✅ 今日已公布
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🟡 **近现价集中开仓**: 11-18 630P ΔOI +3,826（距现价 -4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 661.75 → 今开 663.05（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 663.36 ｜ 低 658.19

Options: P/C成交量 1.15 | OI比 1.40 | ATM IV 45.1% | Skew 4.4pp | Term 0.62 | ExpMove ±2.0%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.62，近月 IV 高于远月）｜保护溢价中性（Skew 4.4pp）｜当日成交偏 Put（P/C量 1.15）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.15×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.40×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 17% ｜ P/C OI(近端) 28%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 17%）｜近端持仓结构中性（P/C OI 分位 28%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-18（1D）±2.0% ｜ 11-19（2D）±2.7% ｜ 11-20（3D）±3.1% ｜ 11-23（6D）±3.4%
   ⇒ IV–VIX Spread: +22.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -580,478,865 | GEX Change vs 上次快照 44,166,571 | Flip: Primary Flip: 681.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 3562 / LOW 365 / INVALID 1253
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 681.25（全链重定价，覆盖 99%）
Put Wall 680（弱结构｜现价低于该位 2.8%）
最近结构参考: Put Wall 680（现价低于该位 2.8%）
量化视角： 负 Gamma（5.80亿，历史分位偏负区，比 83% 的交易日更负）｜负 Gamma 缓解（+4417万）｜现价位于 Flip 下方 3.00%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 680（Put Wall，弱结构） / 669（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 681（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 577.0P — Vol 24,685 | 最新价 $0.24 | OI 1277→25886 (ΔOI +24609张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24609张（+1927.1% vs前日OI），连续性待观察（方向未知）
11-20 694.0C — Vol 11,275 | 最新价 $1.28 | OI 3078→13224 (ΔOI +10146张) | ΔOI/Volume 90.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10146张（+329.6% vs前日OI），连续性待观察（方向未知）
11-30 650.0P — Vol 11,075 | 最新价 $10.34 | OI 10690→19656 (ΔOI +8966张) | ΔOI/Volume 81.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8966张（+83.9% vs前日OI），连续性待观察（方向未知）
12-18 600.0P — Vol 13,840 | 最新价 $6.26 | OI 52540→61188 (ΔOI +8648张) | ΔOI/Volume 62.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8648张（+16.5% vs前日OI），连续性待观察（方向未知）
12-18 640.0P — Vol 4,921 | 最新价 $13.84 | OI 49190→56571 (ΔOI +7381张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增7381张（+15.0% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 59,750 张（Put 49,604 / Call 10,146），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $25M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 118.8k / P 166.0k，今日成交量: C 352.2k / P 404.8k，平值价格ATM: C $3.24 / P $3.21 ｜ ATM IV 45.1%，预期波动 ±1.0%，Max Pain 669
Top ΔOI: C 669 +4,591 ｜ C 675 +4,110 ｜ P 635 +3,856

📆 Forward Expiration Structure

11-18  C +19.7k / P +19.0k ｜ Activity HIGH ｜ 1D
11-19  C +8.5k / P +5.0k ｜ Activity HIGH ｜ 2D
11-20  C +58.2k / P +13.3k ｜ Activity HIGH ｜ 3D
11-23  C +7.9k / P +6.9k ｜ Activity HIGH ｜ 6D

📆 11-18 Forward Structure
存量OI: C 57.1k / P 97.7k，今日变化ΔOI: C +19.7k / P +19.0k，平值价格ATM: C $6.81 / P $6.68 ｜ ATM IV 43.2%，净 delta 敞口 -58k shares
Top ΔOI: P 630 +3,826 ｜ P 660 +2,729 ｜ C 680 +1,690
仓位参考: Max Pain 671 ｜ Call Wall 680（+2.9%，弱）（OI 2.3k） ｜ Put Wall 650（-1.6%，弱）（OI 7.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 43.2%｜历史 Rank 98%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 58,123 股

📆 11-19 Forward Structure
存量OI: C 39.7k / P 60.0k，今日变化ΔOI: C +8.5k / P +5.0k，平值价格ATM: C $8.91 / P $8.71 ｜ ATM IV 42.2%，净 delta 敞口 40k shares
Top ΔOI: C 690 +1,074 ｜ C 725 +938 ｜ C 682 +639
仓位参考: Max Pain 675 ｜ Call Wall 680（+2.9%，弱）（OI 1.8k） ｜ Put Wall 664（+0.5%，弱）（OI 5.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 42.2%｜历史 Rank 98%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 39,865 股

📆 11-20 Forward Structure
存量OI: C 1113.2k / P 1045.7k，今日变化ΔOI: C +58.2k / P +13.3k，平值价格ATM: C $10.41 / P $10.05 ｜ ATM IV 40.8%，净 delta 敞口 5.1M shares
Top ΔOI: P 577 +24,609 ｜ P 720 -12,787 ｜ C 694 +10,146
仓位参考: Max Pain 690 ｜ Call Wall 680（+2.9%，弱）（OI 38.4k） ｜ Put Wall 680（+2.9%）（OI 89.5k）
量化解读： 存量两侧均衡｜ATM IV 40.8%｜历史 Rank 98%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,143,507 股

📆 11-23 Forward Structure
存量OI: C 36.6k / P 26.3k，今日变化ΔOI: C +7.9k / P +6.9k，平值价格ATM: C $12.14 / P $10.31 ｜ ATM IV 33.1%，净 delta 敞口 37k shares
Top ΔOI: C 666 +1,365 ｜ P 645 +942 ｜ P 620 +586
仓位参考: Max Pain 675 ｜ Put Wall 645（-2.4%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 33.1%｜历史 Rank 98%（近端代理）｜IV/RV 0.95×（近似）｜净 delta 敞口 正 37,461 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/QQQ_morning.json