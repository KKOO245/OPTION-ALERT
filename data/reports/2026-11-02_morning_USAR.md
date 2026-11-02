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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-20 9P ΔOI +261（距现价 -2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-13 12C ΔOI +3,921 占该期限总 OI 30.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 9.62 → 今开 9.79（+1.8%） | 较昨收变动（含盘初走势） ｜ 今日高 9.88 ｜ 低 9.55

Options: P/C成交量 0.08 | OI比 0.57 | ATM IV 106.2% | Skew 6.1pp | Term 0.83 | ExpMove ±9.4%（近端） | Rank 39%
量化视角： IV 中性（Rank 39%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价显著（Skew 6.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.57）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.08×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.57×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（4D）±9.4% ｜ 11-13（11D）±13.0% ｜ 11-20（18D）±17.3% ｜ 11-27（25D）±17.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 439,252 | GEX Change vs 上次快照 989,516 | Flip: Primary Flip: 9.46（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 201 / LOW 62 / INVALID 133
结构观察区: Primary Flip 9.46（全链重定价，覆盖 100%）
Put Wall 10（弱结构｜现价低于该位 3.1%）
最近结构参考: Flip 9（现价高于该位 2.5%）
量化视角： 正 Gamma（44万，无历史分位）｜由负转正（+99万）｜现价位于 Flip 上方 2.51%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（Put Wall，弱结构） / 10（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 9（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 12.0C — Vol 4,087 | 最新价 $0.12 | OI 418→4339 (ΔOI +3921张) | ΔOI/Volume 95.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3921张（+938.0% vs前日OI），连续性待观察（方向未知）
11-06 10.5C — Vol 1,102 | 最新价 $0.17 | OI 732→1596 (ΔOI +864张) | ΔOI/Volume 78.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增864张（+118.0% vs前日OI），连续性待观察（方向未知）
11-06 10.0C — Vol 2,342 | 最新价 $0.31 | OI 753→1151 (ΔOI +398张) | ΔOI/Volume 17.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增398张（+52.9% vs前日OI），连续性待观察（方向未知）
11-13 9.5P — Vol 311 | 最新价 $0.89 | OI 127→420 (ΔOI +293张) | ΔOI/Volume 94.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增293张（+230.7% vs前日OI），连续性待观察（方向未知）
11-20 9.5P — Vol 377 | 最新价 $0.85 | OI 479→740 (ΔOI +261张) | ΔOI/Volume 69.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增261张（+54.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,737 张（Put 554 / Call 5,183），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +1.9k / P +0.6k ｜ Activity HIGH ｜ 4D
11-13  C +4.3k / P +0.3k ｜ Activity HIGH ｜ 11D
11-20  C +0.4k / P +0.2k ｜ Activity MEDIUM △ ｜ 18D
11-27  C -19 / P +49 ｜ Activity MEDIUM △ ｜ 25D

📆 11-06 Forward Structure
存量OI: C 10.7k / P 6.1k，今日变化ΔOI: C +1.9k / P +0.6k，平值价格ATM: C $0.60 / P $0.31 ｜ ATM IV 106.2%，净 delta 敞口 58k shares
Top ΔOI: C 10 +864 ｜ C 10 +398 ｜ C 9 +219
仓位参考: Max Pain 10 ｜ Call Wall 10.5（+8.3%，弱）（OI 1.6k） ｜ Put Wall 9（-7.2%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 106.2%｜历史 Rank 39%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 57,710 股

📆 11-13 Forward Structure
存量OI: C 9.7k / P 3.0k，今日变化ΔOI: C +4.3k / P +0.3k，平值价格ATM: C $0.71 / P $0.55 ｜ ATM IV 103.6%，净 delta 敞口 68k shares
Top ΔOI: P 9 +293 ｜ C 10 +175
仓位参考: Max Pain 10 ｜ Put Wall 9（-7.2%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 103.6%｜历史 Rank 39%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 67,569 股

11-20（MEDIUM △）Top ΔOI: 9P +261
11-20（MEDIUM △）仓位参考: Max Pain 13 ｜ Call Wall 9.5（-2.0%，弱）（OI 1.5k） ｜ Put Wall 10（+3.1%，弱）（OI 6.3k）

11-27（MEDIUM △）Top ΔOI: 9P +44 ｜ 9P +31
11-27（MEDIUM △）仓位参考: Max Pain 10 ｜ Call Wall 10（+3.1%）（OI 1.6k） ｜ Put Wall 9.5（-2.0%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/USAR_morning.json