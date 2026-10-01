# 期权晨报 2026-10-01（快照 10:20 ET）

📊 市场环境

SPY $764.48 ｜ QQQ $742.03
VIX 17.57 ↑7.5%（5D +12.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-01

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 54.5 ｜ 前值 54.6　✅ 今日已公布
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 755C ΔOI +10,517（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-07 675P ΔOI +11,736 占该期限总 OI 17.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 739.77 → 今开 742.51（+0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 743.92 ｜ 低 737.61

Options: P/C成交量 0.95 | OI比 1.12 | ATM IV 30.8% | Skew 2.0pp | Term 0.66 | ExpMove ±1.2%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜保护溢价薄（Skew 2.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.12×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 42% ｜ P/C OI(近端) 11%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 42%）｜近端持仓结构中性（P/C OI 分位 11%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-02（1D）±1.2% ｜ 10-05（4D）±1.6% ｜ 10-06（5D）±1.8% ｜ 10-07（6D）±2.0%
   ⇒ IV–VIX Spread: +13.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -136,055,881 | GEX Change vs 上次快照 -259,938,154 | Flip: Primary Flip: 740.37（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 3057 / LOW 352 / INVALID 1555
结构观察区: Primary Flip 740.37（全链重定价，覆盖 98%）
Call Wall 760（现价低于该位 2.8%）
最近结构参考: Flip 740（现价低于该位 0.2%）
量化视角： 负 Gamma（1.36亿，历史分位 42%，中性区）｜由正转负（2.60亿）｜现价位于 Flip 下方 0.23%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 740（MaxPain，仅结算参考） / 760（Call Wall）。
• Gamma 区域：切换参考 740（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 715.0P — Vol 21,524 | 最新价 $8.10 | OI 2500→21867 (ΔOI +19367张) | ΔOI/Volume 90.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19367张（+774.7% vs前日OI），连续性待观察（方向未知）
10-01 740.0P — Vol 64,190 | 最新价 $3.02 | OI 5057→19328 (ΔOI +14271张) | ΔOI/Volume 22.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14271张（+282.2% vs前日OI），连续性待观察（方向未知）
10-07 675.0P — Vol 12,624 | 最新价 $0.13 | OI 857→12593 (ΔOI +11736张) | ΔOI/Volume 93.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11736张（+1369.4% vs前日OI），连续性待观察（方向未知）
10-02 755.0C — Vol 19,458 | 最新价 $0.46 | OI 8336→18853 (ΔOI +10517张) | ΔOI/Volume 54.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10517张（+126.2% vs前日OI），连续性待观察（方向未知）
10-09 730.0P — Vol 15,092 | 最新价 $4.50 | OI 9494→19610 (ΔOI +10116张) | ΔOI/Volume 67.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10116张（+106.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 66,007 张（Put 55,490 / Call 10,517），跨 5 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $25M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 158.9k / P 177.9k，今日成交量: C 427.6k / P 408.4k，平值价格ATM: C $3.68 / P $1.56 ｜ ATM IV 30.8%，预期波动 ±0.7%，Max Pain 740
Top ΔOI: P 740 +14,271 ｜ C 750 +9,619 ｜ C 745 +9,229

📆 Forward Expiration Structure

10-02  C +15.6k / P +21.8k ｜ Activity HIGH ｜ 1D
10-05  C +13.9k / P +30.7k ｜ Activity HIGH ｜ 4D
10-06  C +2.3k / P +7.6k ｜ Activity HIGH ｜ 5D
10-07  C +3.6k / P +29.4k ｜ Activity HIGH ｜ 6D

📆 10-02 Forward Structure
存量OI: C 257.6k / P 483.6k，今日变化ΔOI: C +15.6k / P +21.8k，平值价格ATM: C $5.69 / P $3.27 ｜ ATM IV 24.9%，净 delta 敞口 -1.5M shares
Top ΔOI: P 690 -17,505 ｜ C 755 +10,517 ｜ P 736 +7,424
仓位参考: Max Pain 735 ｜ Call Wall 725（-1.9%）（OI 35.1k） ｜ Put Wall 730（-1.2%，弱）（OI 48.9k）
量化解读： 存量 Put 重｜ATM IV 24.9%｜历史 Rank 91%（近端代理）｜IV/RV 1.69×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,456,584 股

📆 10-05 Forward Structure
存量OI: C 44.1k / P 119.5k，今日变化ΔOI: C +13.9k / P +30.7k，平值价格ATM: C $7.48 / P $4.52 ｜ ATM IV 17.6%，净 delta 敞口 -369k shares
Top ΔOI: P 736 +6,920 ｜ C 760 +6,596 ｜ P 725 +6,330
仓位参考: Max Pain 740 ｜ Call Wall 760（+2.9%，弱）（OI 8.0k） ｜ Put Wall 725（-1.9%，弱）（OI 7.7k）
量化解读： 存量 Put 重｜ATM IV 17.6%｜历史 Rank 91%（近端代理）｜IV/RV 1.20×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 368,654 股

📆 10-06 Forward Structure
存量OI: C 18.2k / P 41.8k，今日变化ΔOI: C +2.3k / P +7.6k，平值价格ATM: C $8.10 / P $5.10 ｜ ATM IV 18.3%，净 delta 敞口 -150k shares
Top ΔOI: P 736 +3,703 ｜ C 747 +782 ｜ P 715 +417
仓位参考: Max Pain 738 ｜ Call Wall 740（+0.2%，弱）（OI 1.4k） ｜ Put Wall 736（-0.4%，弱）（OI 3.9k）
量化解读： 存量 Put 重｜ATM IV 18.3%｜历史 Rank 91%（近端代理）｜IV/RV 1.24×（近似）｜净 delta 敞口 负 149,885 股

📆 10-07 Forward Structure
存量OI: C 19.4k / P 46.6k，今日变化ΔOI: C +3.6k / P +29.4k，平值价格ATM: C $9.55 / P $5.29 ｜ ATM IV 18.8%，净 delta 敞口 -60k shares
Top ΔOI: P 675 +11,736 ｜ P 670 +4,854
仓位参考: Max Pain 739 ｜ Call Wall 740（+0.2%，弱）（OI 2.3k） ｜ Put Wall 717（-2.9%，弱）（OI 2.9k）
量化解读： 存量 Put 重｜ATM IV 18.8%｜历史 Rank 91%（近端代理）｜IV/RV 1.28×（近似）｜净 delta 敞口 负 59,908 股

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 24.9% vs 10-05 17.6%（差 +7.3pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/QQQ_morning.json