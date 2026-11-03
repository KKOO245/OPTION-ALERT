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
🟡 **事件差分**: 11-06 ATM IV 100.4% vs 11-13 85.6%（差 +14.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-20 1150P ΔOI +980（距现价 +2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-27 1300C ΔOI +2,082 占该期限总 OI 10.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,150.89 → 今开 1,158.50（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 1159.31 ｜ 低 1115.26

Options: P/C成交量 0.80 | OI比 0.83 | ATM IV 100.4% | Skew 6.1pp | Term 0.74 | ExpMove ±8.6%（近端） | Rank 57%
量化视角： IV 中性（Rank 57%）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价显著（Skew 6.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（4D）±8.6% ｜ 11-13（11D）±12.4% ｜ 11-20（18D）±14.5% ｜ 11-27（25D）±17.1%
   ⇒ IV–VIX Spread: +81.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,443,640 | GEX Change vs 上次快照 1,722,324 | Flip: Primary Flip: 1219.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1747 / LOW 431 / INVALID 978
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1219.18（全链重定价，覆盖 100%）
最近结构参考: Flip 1219（现价低于该位 7.7%）
量化视角： 负 Gamma（344万，无历史分位）｜负 Gamma 缓解（+172万）｜现价位于 Flip 下方 7.65%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,250（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1219（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 630.0P — Vol 3,422 | 最新价 $0.40 | OI 496→3024 (ΔOI +2528张) | ΔOI/Volume 73.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2528张（+509.7% vs前日OI），连续性待观察（方向未知）
11-27 1300.0C — Vol 2,397 | 最新价 $43.00 | OI 71→2153 (ΔOI +2082张) | ΔOI/Volume 86.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2082张（+2932.4% vs前日OI），连续性待观察（方向未知）
11-27 1270.0C — Vol 2,073 | 最新价 $50.80 | OI 22→2049 (ΔOI +2027张) | ΔOI/Volume 97.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2027张（+9213.6% vs前日OI），连续性待观察（方向未知）
11-27 1290.0C — Vol 2,033 | 最新价 $44.54 | OI 13→2021 (ΔOI +2008张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2008张（+15446.1% vs前日OI），连续性待观察（方向未知）
11-06 1050.0P — Vol 1,687 | 最新价 $18.59 | OI 236→1275 (ΔOI +1039张) | ΔOI/Volume 61.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1039张（+440.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,684 张（Put 3,567 / Call 6,117），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +11.0k / P +11.0k ｜ Activity HIGH ｜ 4D
11-13  C +2.7k / P +0.6k ｜ Activity HIGH ｜ 11D
11-20  C +4.4k / P +2.2k ｜ Activity MEDIUM △ ｜ 18D
11-27  C +7.0k / P +0.8k ｜ Activity HIGH ｜ 25D

📆 11-06 Forward Structure
存量OI: C 32.4k / P 26.9k，今日变化ΔOI: C +11.0k / P +11.0k，平值价格ATM: C $47.70 / P $49.40 ｜ ATM IV 100.4%，净 delta 敞口 46k shares
Top ΔOI: P 1050 +1,039 ｜ C 1200 +912
仓位参考: Max Pain 1,250 ｜ Call Wall 1200（+6.6%，弱）（OI 1.0k） ｜ Put Wall 1100（-2.3%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 100.4%｜历史 Rank 57%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 45,997 股

📆 11-13 Forward Structure
存量OI: C 9.2k / P 8.5k，今日变化ΔOI: C +2.7k / P +0.6k，平值价格ATM: C $70.20 / P $69.00 ｜ ATM IV 85.6%，净 delta 敞口 23k shares
Top ΔOI: C 1220 +370 ｜ C 1500 +203
仓位参考: Max Pain 1,370 ｜ Call Wall 1220（+8.4%，弱）（OI 0.4k） ｜ Put Wall 1100（-2.3%，弱）（OI 0.2k）
量化解读： 存量两侧均衡｜ATM IV 85.6%｜历史 Rank 57%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 23,131 股

11-20（MEDIUM △）Top ΔOI: 1150P +980 ｜ 1600C +650
11-20（MEDIUM △）仓位参考: Max Pain 1,430 ｜ Put Wall 1150（+2.1%，弱）（OI 1.6k）

📆 11-27 Forward Structure
存量OI: C 11.7k / P 7.7k，今日变化ΔOI: C +7.0k / P +0.8k，平值价格ATM: C $103.33 / P $88.95 ｜ ATM IV 77.2%，净 delta 敞口 167k shares
Top ΔOI: C 1300 +2,082 ｜ C 1270 +2,027 ｜ C 1290 +2,008
仓位参考: Max Pain 1,270 ｜ Put Wall 1150（+2.1%）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 77.2%｜历史 Rank 57%（近端代理）｜IV/RV 0.95×（近似）｜净 delta 敞口 正 167,411 股

📅 事件差分（观察，非因果）: 11-06（4D）ATM IV 100.4% vs 11-13 85.6%（差 +14.9pp）——覆盖 ISM 制造业 PMI、Midterm Elections 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=72 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=72）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/SNDK_morning.json