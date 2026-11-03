# 期权晨报 2026-11-02（快照 10:20 ET）

📊 市场环境

SPY $752.10 ｜ QQQ $681.09
VIX 18.83 ↓3.0%（5D +2.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 22.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 11-02 10:00　【高】ISM 制造业 PMI　预测 54.6 ｜ 实际 55.5 ｜ 前值 54.5　✅ 今日已公布
- 周一 11-02 19:00　【高】Midterm Elections　实际 待公布　✅ 今日已公布
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.13 ｜ 实际 待公布 ｜ 前值 7.079
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48.2 ｜ 实际 待公布 ｜ 前值 48

🔍 重点速览
🟡 **近现价集中开仓**: 11-03 736P ΔOI +19,177（距现价 -3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-04 740P ΔOI +56,807 占该期限总 OI 18.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 755.72 → 今开 759.45（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 761.82 ｜ 低 758.73

Options: P/C成交量 0.79 | OI比 1.82 | ATM IV 21.2% | Skew 1.5pp | Term 0.69 | ExpMove ±0.8%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价薄（Skew 1.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.79×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.82×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 35% ｜ P/C OI(近端) 49%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 35%）｜近端持仓结构中性（P/C OI 分位 49%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-03（1D）±0.8% ｜ 11-04（2D）±1.2% ｜ 11-05（3D）±1.4% ｜ 11-06（4D）±0.0%
   ⇒ IV–VIX Spread: +2.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -951,679,362 | GEX Change vs 上次快照 444,226,946 | Flip: Primary Flip: 769.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 2563 / LOW 247 / INVALID 1524
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 769.50（全链重定价，覆盖 99%）
最近结构参考: Flip 770（现价低于该位 1.2%）
量化视角： 负 Gamma（9.52亿，历史分位 35%，中性区）｜负 Gamma 缓解（+4.44亿）｜现价位于 Flip 下方 1.20%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 758（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 770（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-04 740.0P — Vol 61,954 | 最新价 $1.22 | OI 1479→58286 (ΔOI +56807张) | ΔOI/Volume 91.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增56807张（+3840.9% vs前日OI），连续性待观察（方向未知）
11-04 730.0P — Vol 59,883 | 最新价 $0.54 | OI 1416→56718 (ΔOI +55302张) | ΔOI/Volume 92.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增55302张（+3905.5% vs前日OI），连续性待观察（方向未知）
11-02 745.0P — Vol 65,643 | 最新价 $0.50 | OI 3337→41453 (ΔOI +38116张) | ΔOI/Volume 58.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增38116张（+1142.2% vs前日OI），连续性待观察（方向未知）
11-02 730.0P — Vol 41,793 | 最新价 $0.10 | OI 720→35247 (ΔOI +34527张) | ΔOI/Volume 82.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增34527张（+4795.4% vs前日OI），连续性待观察（方向未知）
11-20 718.0P — Vol 46,815 | 最新价 $3.06 | OI 1290→27079 (ΔOI +25789张) | ΔOI/Volume 55.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增25789张（+1999.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 210,541 张（Put 210,541 / Call 0），跨 3 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $15M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 163.1k / P 297.4k，今日成交量: C 449.1k / P 352.9k，平值价格ATM: C $1.92 / P $1.56 ｜ ATM IV 21.2%，预期波动 ±0.5%，Max Pain 758
Top ΔOI: P 745 +38,116 ｜ P 730 +34,527 ｜ P 775 -15,277

📆 Forward Expiration Structure

11-03  C +50.3k / P +53.3k ｜ Activity HIGH ｜ 1D
11-04  C +37.4k / P +145.0k ｜ Activity HIGH ｜ 2D
11-05  C +13.2k / P +12.1k ｜ Activity HIGH ｜ 3D
11-06  C +55.8k / P +73.1k ｜ Activity HIGH ｜ 4D

📆 11-03 Forward Structure
存量OI: C 93.6k / P 140.7k，今日变化ΔOI: C +50.3k / P +53.3k，平值价格ATM: C $3.28 / P $2.85 ｜ ATM IV 17.2%，净 delta 敞口 2.3M shares
Top ΔOI: P 736 +19,177 ｜ C 750 +9,605 ｜ C 756 +3,817
仓位参考: Max Pain 756 ｜ Call Wall 750（-1.4%）（OI 9.6k） ｜ Put Wall 740（-2.7%，弱）（OI 7.2k）
量化解读： 存量 Put 重｜ATM IV 17.2%｜历史 Rank 87%（近端代理）｜IV/RV 1.55×（近似）｜净 delta 敞口 正 2,270,791 股

📆 11-04 Forward Structure
存量OI: C 76.7k / P 231.1k，今日变化ΔOI: C +37.4k / P +145.0k，平值价格ATM: C $4.70 / P $4.21 ｜ ATM IV 18.6%，净 delta 敞口 1.7M shares
Top ΔOI: P 740 +56,807 ｜ P 730 +55,302 ｜ P 767 -18,520
仓位参考: Max Pain 767 ｜ Call Wall 780（+2.6%，弱）（OI 5.2k） ｜ Put Wall 740（-2.7%，弱）（OI 58.3k）
量化解读： 存量 Put 重｜ATM IV 18.6%｜历史 Rank 87%（近端代理）｜IV/RV 1.68×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,682,332 股

📆 11-05 Forward Structure
存量OI: C 36.8k / P 29.5k，今日变化ΔOI: C +13.2k / P +12.1k，平值价格ATM: C $5.50 / P $4.76 ｜ ATM IV 18.0%，净 delta 敞口 259k shares
Top ΔOI: C 780 +2,427 ｜ P 730 +2,424 ｜ C 770 +2,379
仓位参考: Max Pain 765 ｜ Call Wall 780（+2.6%）（OI 12.9k） ｜ Put Wall 750（-1.4%，弱）（OI 2.6k）
量化解读： 存量 Call 重｜ATM IV 18.0%｜历史 Rank 87%（近端代理）｜IV/RV 1.62×（近似）｜净 delta 敞口 正 259,330 股

📆 11-06 Forward Structure
存量OI: C 189.8k / P 388.1k，今日变化ΔOI: C +55.8k / P +73.1k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 0.0%，净 delta 敞口 1.9M shares
Top ΔOI: P 735 +12,986 ｜ P 740 +11,988 ｜ P 720 +9,910
仓位参考: Max Pain 764 ｜ Call Wall 770（+1.3%，弱）（OI 13.7k） ｜ Put Wall 750（-1.4%）（OI 38.6k）
量化解读： 存量 Put 重｜净 delta 敞口 正 1,918,534 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/SPY_morning.json