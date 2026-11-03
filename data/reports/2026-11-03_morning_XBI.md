# 期权晨报 2026-11-03（快照 10:20 ET）

📊 市场环境

SPY $755.37 ｜ QQQ $685.28
VIX 21.03 ↓0.6%（5D +20.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.1（extreme fear）
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
🟡 **近现价集中开仓**: 11-06 149P ΔOI +167（距现价 -4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 152.05 → 今开 152.96（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 156.37 ｜ 低 152.83

Options: P/C成交量 0.25 | OI比 1.73 | ATM IV 47.9% | Skew 6.5pp | Term 0.79 | ExpMove ±3.5%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价显著（Skew 6.5pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.25×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.73×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（3D）±3.5% ｜ 11-13（10D）±4.4% ｜ 11-20（17D）±6.0% ｜ 11-27（24D）±7.1%
   ⇒ IV–VIX Spread: +26.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,426,196 | GEX Change vs 上次快照 5,428,446 | Flip: Primary Flip: 159.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 365 / LOW 58 / INVALID 349
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 159.56（全链重定价，覆盖 97%）
Call Wall 165（现价低于该位 5.9%）
最近结构参考: Flip 160（现价低于该位 2.7%）
量化视角： 负 Gamma（643万，无历史分位）｜负 Gamma 缓解（+543万）｜现价位于 Flip 下方 2.69%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 153（MaxPain，仅结算参考）；上方 165（Call Wall）。
• Gamma 区域：切换参考 160（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 144.0P — Vol 950 | 最新价 $1.95 | OI 652→1433 (ΔOI +781张) | ΔOI/Volume 82.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增781张（+119.8% vs前日OI），连续性待观察（方向未知）
11-06 152.0P — Vol 228 | 最新价 $2.15 | OI 24→226 (ΔOI +202张) | ΔOI/Volume 88.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增202张（+841.7% vs前日OI），连续性待观察（方向未知）
11-06 149.0P — Vol 170 | 最新价 $1.44 | OI 85→252 (ΔOI +167张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增167张（+196.5% vs前日OI），连续性待观察（方向未知）
11-20 146.0P — Vol 195 | 最新价 $2.52 | OI 389→547 (ΔOI +158张) | ΔOI/Volume 81.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增158张（+40.6% vs前日OI），连续性待观察（方向未知）
11-27 152.5C — Vol 127 | 最新价 $5.65 | OI 6→133 (ΔOI +127张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增127张（+2116.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,435 张（Put 1,308 / Call 127），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +0.2k / P +0.8k ｜ Activity MEDIUM △ ｜ 3D
11-13  C +0.3k / P +96 ｜ Activity MEDIUM △ ｜ 10D
11-20  C +0.2k / P -0.6k ｜ Activity HIGH ｜ 17D
11-27  C +0.1k / P +39 ｜ Activity MEDIUM △ ｜ 24D

📆 11-06 Forward Structure
存量OI: C 5.6k / P 9.7k，今日变化ΔOI: C +0.2k / P +0.8k，平值价格ATM: C $1.61 / P $3.80 ｜ ATM IV 47.9%，净 delta 敞口 -9k shares
Top ΔOI: P 152 +202 ｜ P 149 +167 ｜ P 150 +90
仓位参考: Max Pain 153 ｜ Call Wall 159（+2.4%，弱）（OI 0.4k） ｜ Put Wall 153（-1.5%）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 47.9%｜历史 Rank 96%（近端代理）｜IV/RV 1.57×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 9,447 股

11-13（MEDIUM △）Top ΔOI: 157C +79 ｜ 160C +41
11-13（MEDIUM △）仓位参考: Max Pain 153 ｜ Call Wall 160（+3.0%）（OI 0.5k） ｜ Put Wall 148（-4.7%，弱）（OI 0.3k）

📆 11-20 Forward Structure
存量OI: C 23.4k / P 46.0k，今日变化ΔOI: C +0.2k / P -0.6k，平值价格ATM: C $4.45 / P $4.80 ｜ ATM IV 38.9%，净 delta 敞口 12k shares
Top ΔOI: P 145 -1,299 ｜ P 144 +781
仓位参考: Max Pain 155 ｜ Call Wall 165（+6.3%）（OI 7.1k） ｜ Put Wall 147（-5.3%，弱）（OI 5.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 38.9%｜历史 Rank 96%（近端代理）｜IV/RV 1.27×（近似）｜净 delta 敞口 正 12,019 股

11-27（MEDIUM △）Top ΔOI: 152C +127 ｜ 160C +18
11-27（MEDIUM △）仓位参考: Max Pain 157 ｜ Call Wall 152.5（-1.8%，弱）（OI 0.1k） ｜ Put Wall 156（+0.5%）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/XBI_morning.json