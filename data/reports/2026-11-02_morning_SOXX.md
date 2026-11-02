# 期权晨报 2026-11-02（快照 10:20 ET）

📊 市场环境

SPY $753.20 ｜ QQQ $681.09
VIX 18.83 ↓3.0%（5D +2.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 22.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 11-02 10:00　【高】ISM 制造业 PMI　预测 54.6 ｜ 实际 55.5 ｜ 前值 54.5　✅ 今日已公布
- 周一 11-02 19:00　【高】Midterm Elections　实际 待公布　⏰ 今日
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.13 ｜ 实际 待公布 ｜ 前值 7.079
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48.2 ｜ 实际 待公布 ｜ 前值 48

🔍 重点速览
🟡 **近现价集中开仓**: 11-06 492P ΔOI -1,664（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-06 360P ΔOI +38,011 占该期限总 OI 37.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 471.51 → 今开 476.58（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 476.60 ｜ 低 470.81

Options: P/C成交量 0.80 | OI比 1.36 | ATM IV 57.2% | Skew 7.7pp | Term 0.78 | ExpMove ±6.8%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价显著（Skew 7.7pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.36×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（4D）±6.8% ｜ 11-13（11D）±8.6% ｜ 11-20（18D）±8.8% ｜ 11-27（25D）±10.8%
   ⇒ IV–VIX Spread: +38.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -12,115,216 | GEX Change vs 上次快照 3,616,718 | Flip: Primary Flip: 489.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 596 / LOW 206 / INVALID 750
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 489.96（全链重定价，覆盖 100%）
最近结构参考: Flip 490（现价低于该位 3.5%）
量化视角： 负 Gamma（1212万，无历史分位）｜负 Gamma 缓解（+362万）｜现价位于 Flip 下方 3.54%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 495（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 490（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 360.0P — Vol 38,031 | 最新价 $0.30 | OI 93→38104 (ΔOI +38011张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增38011张（+40872.0% vs前日OI），连续性待观察（方向未知）
11-20 500.0C — Vol 9,346 | 最新价 $10.48 | OI 1426→9557 (ΔOI +8131张) | ΔOI/Volume 87.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8131张（+570.2% vs前日OI），连续性待观察（方向未知）
11-20 425.0P — Vol 2,060 | 最新价 $8.44 | OI 222→2063 (ΔOI +1841张) | ΔOI/Volume 89.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1841张（+829.3% vs前日OI），连续性待观察（方向未知）
11-06 350.0P — Vol 1,476 | 最新价 $0.25 | OI 0→1470 (ΔOI +1470张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1470张（前日OI缺失），连续性待观察（方向未知）
11-20 440.0P — Vol 1,798 | 最新价 $10.70 | OI 1828→3222 (ΔOI +1394张) | ΔOI/Volume 77.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1394张（+76.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 50,847 张（Put 42,716 / Call 8,131），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +4.1k / P +38.7k ｜ Activity HIGH ｜ 4D
11-13  C +1.0k / P +1.0k ｜ Activity MEDIUM △ ｜ 11D
11-20  C +9.1k / P +6.6k ｜ Activity HIGH ｜ 18D
11-27  C +0.2k / P +0.6k ｜ Activity MEDIUM △ ｜ 25D

📆 11-06 Forward Structure
存量OI: C 42.6k / P 58.0k，今日变化ΔOI: C +4.1k / P +38.7k，平值价格ATM: C $12.30 / P $19.69 ｜ ATM IV 57.2%，净 delta 敞口 284k shares
Top ΔOI: P 360 +38,011 ｜ P 492 -1,664 ｜ P 460 -1,543
仓位参考: Max Pain 495
量化解读： 存量 Put 重｜ATM IV 57.2%｜历史 Rank 92%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 284,488 股

11-13（MEDIUM △）Top ΔOI: 480C +522 ｜ 415P +468
11-13（MEDIUM △）仓位参考: Max Pain 500 ｜ Put Wall 460（-2.7%）（OI 3.3k）

📆 11-20 Forward Structure
存量OI: C 50.8k / P 75.9k，今日变化ΔOI: C +9.1k / P +6.6k，平值价格ATM: C $20.08 / P $21.50 ｜ ATM IV 48.5%，净 delta 敞口 231k shares
Top ΔOI: C 500 +8,131 ｜ P 425 +1,841 ｜ P 440 +1,394
仓位参考: Max Pain 510 ｜ Call Wall 500（+5.8%）（OI 9.6k） ｜ Put Wall 460（-2.7%，弱）（OI 7.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 48.5%｜历史 Rank 92%（近端代理）｜IV/RV 0.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 231,124 股

11-27（MEDIUM △）Top ΔOI: 425P +92 ｜ 495P +92
11-27（MEDIUM △）仓位参考: Max Pain 500 ｜ Put Wall 500（+5.8%）（OI 2.1k）

📅 事件差分（观察，非因果）: 11-06（4D）ATM IV 57.2% vs 11-13 52.1%（差 +5.1pp）——覆盖 ISM 制造业 PMI、Midterm Elections 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/SOXX_morning.json