# 期权晨报 2026-11-03（快照 10:20 ET）

📊 市场环境

SPY $753.95 ｜ QQQ $685.47
VIX 21.03 ↓0.6%（5D +20.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-03

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.1 ｜ 实际 7.523 ｜ 前值 7.19　✅ 今日已公布
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔵 **期限 OI 集中**: 11-13 490C ΔOI +9,598 占该期限总 OI 18.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 453.65 → 今开 466.01（+2.7%） | 较昨收变动（含盘初走势） ｜ 今日高 471.44 ｜ 低 463.13

Options: P/C成交量 1.02 | OI比 1.37 | ATM IV 68.2% | Skew 5.3pp | Term 0.72 | ExpMove ±5.0%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价中性（Skew 5.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.02×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.37×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（3D）±5.0% ｜ 11-13（10D）±6.9% ｜ 11-20（17D）±8.0% ｜ 11-27（24D）±11.9%
   ⇒ IV–VIX Spread: +47.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -14,491,485 | GEX Change vs 上次快照 3,825,135 | Flip: Primary Flip: 487.75（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 620 / LOW 210 / INVALID 722
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 487.75（全链重定价，覆盖 100%）
最近结构参考: Flip 488（现价低于该位 4.4%）
量化视角： 负 Gamma（1449万，无历史分位）｜负 Gamma 缓解（+383万）｜现价位于 Flip 下方 4.37%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 495（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 488（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 490.0C — Vol 9,631 | 最新价 $7.50 | OI 47→9645 (ΔOI +9598张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9598张（+20421.3% vs前日OI），连续性待观察（方向未知）
11-13 415.0P — Vol 4,492 | 最新价 $6.37 | OI 512→4982 (ΔOI +4470张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4470张（+873.0% vs前日OI），连续性待观察（方向未知）
11-13 375.0P — Vol 4,494 | 最新价 $1.75 | OI 17→4482 (ΔOI +4465张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4465张（+26264.7% vs前日OI），连续性待观察（方向未知）
11-13 440.0P — Vol 3,215 | 最新价 $12.02 | OI 41→3020 (ΔOI +2979张) | ΔOI/Volume 92.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2979张（+7265.9% vs前日OI），连续性待观察（方向未知）
11-20 400.0P — Vol 5,031 | 最新价 $6.70 | OI 3776→5911 (ΔOI +2135张) | ΔOI/Volume 42.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2135张（+56.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 23,647 张（Put 14,049 / Call 9,598），跨 2 个期限｜有实质成本保护 4 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +0.8k / P +1.7k ｜ Activity MEDIUM △ ｜ 3D
11-13  C +4.5k / P +13.7k ｜ Activity HIGH ｜ 10D
11-20  C +6.0k / P +1.8k ｜ Activity MEDIUM △ ｜ 17D
11-27  C +0.2k / P +91 ｜ Activity LOW ｜ 24D

📆 11-06 Forward Structure
存量OI: C 43.4k / P 59.7k，今日变化ΔOI: C +0.8k / P +1.7k，平值价格ATM: C $12.36 / P $10.80 ｜ ATM IV 68.2%，净 delta 敞口 3k shares
Top ΔOI: P 430 +790 ｜ P 455 +494 ｜ P 450 -315
仓位参考: Max Pain 495
量化解读： 存量 Put 重｜ATM IV 68.2%｜历史 Rank 96%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,870 股

📆 11-13 Forward Structure
存量OI: C 30.2k / P 22.6k，今日变化ΔOI: C +4.5k / P +13.7k，平值价格ATM: C $14.60 / P $17.51 ｜ ATM IV 58.4%，净 delta 敞口 14k shares
Top ΔOI: C 490 +9,598 ｜ C 510 -5,379 ｜ P 415 +4,470
仓位参考: Max Pain 490 ｜ Call Wall 490（+5.1%，弱）（OI 9.6k） ｜ Put Wall 460（-1.4%，弱）（OI 3.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 58.4%｜历史 Rank 96%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 13,621 股

11-20（MEDIUM △）Top ΔOI: 400P +2,135 ｜ 495C +2,054
11-20（MEDIUM △）仓位参考: Max Pain 500 ｜ Call Wall 495（+6.1%，弱）（OI 2.1k） ｜ Put Wall 460（-1.4%，弱）（OI 7.7k）

11-27（Activity LOW）仓位参考: Max Pain 500 ｜ Put Wall 490（+5.1%，弱）（OI 1.1k）

📅 事件差分（观察，非因果）: 11-06（3D）ATM IV 68.2% vs 11-13 58.4%（差 +9.9pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/SOXX_morning.json