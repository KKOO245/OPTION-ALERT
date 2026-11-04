# 期权晨报 2026-11-04（快照 10:20 ET）

📊 市场环境

SPY $767.05 ｜ QQQ $696.65
VIX 17.01 ↓18.3%（5D +0.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-04

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 54.5 ｜ 前值 54.9　✅ 今日已公布
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-06 460P ΔOI +2,332（距现价 -0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-27 485C ΔOI +3,425 占该期限总 OI 22.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 465.00 → 今开 458.43（-1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 469.22 ｜ 低 452.46

Options: P/C成交量 6.61 | OI比 1.50 | ATM IV 59.5% | Skew 2.8pp | Term 0.78 | ExpMove ±4.4%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价中性（Skew 2.8pp）｜当日成交偏 Put（P/C量 6.61）——观察点，非方向信号
   ⇒ Put/Call Volume: 6.61×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.50×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±4.4% ｜ 11-13（9D）±7.5% ｜ 11-20（16D）±8.9% ｜ 11-27（23D）±11.1%
   ⇒ IV–VIX Spread: +42.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -19,505,372 | GEX Change vs 上次快照 -3,516,190 | Flip: Primary Flip: 482.94（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 620 / LOW 247 / INVALID 685
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 482.94（全链重定价，覆盖 98%）
最近结构参考: Flip 483（现价低于该位 4.4%）
量化视角： 负 Gamma（1951万，无历史分位）｜负 Gamma 加深（352万）｜现价位于 Flip 下方 4.40%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 495（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 483（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 485.0C — Vol 3,492 | 最新价 $17.10 | OI 28→3453 (ΔOI +3425张) | ΔOI/Volume 98.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3425张（+12232.1% vs前日OI），连续性待观察（方向未知）
11-06 460.0P — Vol 3,820 | 最新价 $9.70 | OI 3420→5752 (ΔOI +2332张) | ΔOI/Volume 61.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2332张（+68.2% vs前日OI），连续性待观察（方向未知）
11-20 500.0C — Vol 2,623 | 最新价 $9.00 | OI 10329→12393 (ΔOI +2064张) | ΔOI/Volume 78.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2064张（+20.0% vs前日OI），连续性待观察（方向未知）
11-20 440.0P — Vol 1,323 | 最新价 $12.20 | OI 4210→5546 (ΔOI +1336张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1336张（+31.7% vs前日OI），连续性待观察（方向未知）
11-20 490.0C — Vol 1,383 | 最新价 $12.10 | OI 1307→2529 (ΔOI +1222张) | ΔOI/Volume 88.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1222张（+93.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 10,379 张（Put 3,668 / Call 6,711），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C -0.6k / P +4.5k ｜ Activity MEDIUM △ ｜ 2D
11-13  C +0.8k / P +0.8k ｜ Activity HIGH ｜ 9D
11-20  C +4.7k / P +0.7k ｜ Activity HIGH ｜ 16D
11-27  C +3.7k / P +1.1k ｜ Activity HIGH ｜ 23D

📆 11-06 Forward Structure
存量OI: C 42.8k / P 64.2k，今日变化ΔOI: C -0.6k / P +4.5k，平值价格ATM: C $12.40 / P $8.00 ｜ ATM IV 59.5%，净 delta 敞口 -133k shares
Top ΔOI: P 460 +2,332 ｜ P 425 +800 ｜ C 500 -576
仓位参考: Max Pain 495
量化解读： 存量 Put 重｜ATM IV 59.5%｜历史 Rank 93%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 133,249 股

📆 11-13 Forward Structure
存量OI: C 31.0k / P 23.4k，今日变化ΔOI: C +0.8k / P +0.8k，平值价格ATM: C $15.10 / P $19.50 ｜ ATM IV 50.8%，净 delta 敞口 -3k shares
Top ΔOI: P 440 +192
仓位参考: Max Pain 490 ｜ Call Wall 490（+6.1%）（OI 9.7k） ｜ Put Wall 460（-0.4%，弱）（OI 3.3k）
量化解读： 存量 Call 重｜ATM IV 50.8%｜历史 Rank 93%（近端代理）｜IV/RV 0.97×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,107 股

📆 11-20 Forward Structure
存量OI: C 61.5k / P 78.4k，今日变化ΔOI: C +4.7k / P +0.7k，平值价格ATM: C $23.20 / P $17.70 ｜ ATM IV 50.6%，净 delta 敞口 131k shares
Top ΔOI: C 500 +2,064 ｜ P 440 +1,336 ｜ C 490 +1,222
仓位参考: Max Pain 500 ｜ Call Wall 490（+6.1%，弱）（OI 2.5k） ｜ Put Wall 460（-0.4%，弱）（OI 7.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 50.6%｜历史 Rank 93%（近端代理）｜IV/RV 0.97×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 131,371 股

📆 11-27 Forward Structure
存量OI: C 8.2k / P 6.8k，今日变化ΔOI: C +3.7k / P +1.1k，平值价格ATM: C $27.00 / P $24.00 ｜ ATM IV 47.1%，净 delta 敞口 90k shares
Top ΔOI: C 485 +3,425 ｜ P 450 +862 ｜ P 425 +132
仓位参考: Max Pain 490 ｜ Call Wall 485（+5.1%）（OI 3.5k） ｜ Put Wall 490（+6.1%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 47.1%｜历史 Rank 93%（近端代理）｜IV/RV 0.90×（近似）｜净 delta 敞口 正 90,142 股

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 59.5% vs 11-13 50.8%（差 +8.7pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/SOXX_morning.json