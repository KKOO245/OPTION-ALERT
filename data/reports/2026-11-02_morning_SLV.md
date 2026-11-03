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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-04 44C ΔOI +1,494（距现价 -4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-11 51C ΔOI +1,094 占该期限总 OI 17.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 44.60 → 今开 44.99（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 46.12 ｜ 低 45.83

Options: P/C成交量 0.37 | OI比 0.43 | ATM IV 43.8% | Skew 1.6pp | Term 0.92 | ExpMove ±3.2%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构正常（Term 0.92）｜保护溢价薄（Skew 1.6pp）｜存量 Call 偏重（OI比 0.43）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.43×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-04（2D）±3.2% ｜ 11-06（4D）±4.3% ｜ 11-09（7D）±4.8% ｜ 11-11（9D）±5.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 23,615,989 | GEX Change vs 上次快照 51,756,134 | Flip: Primary Flip: 44.59（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 673 / LOW 125 / INVALID 404
结构观察区: Primary Flip 44.59（全链重定价，覆盖 97%）
Put Wall 45（弱结构｜现价高于该位 2.2%）
最近结构参考: Put Wall 45（现价高于该位 2.2%）
量化视角： 正 Gamma（2362万，无历史分位）｜由负转正（+5176万）｜现价位于 Flip 上方 3.19%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 45（Put Wall，弱结构） / 45（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 45（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 50.0C — Vol 9,389 | 最新价 $0.06 | OI 5874→12937 (ΔOI +7063张) | ΔOI/Volume 75.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7063张（+120.2% vs前日OI），连续性待观察（方向未知）
11-20 46.0C — Vol 6,032 | 最新价 $1.27 | OI 113→5795 (ΔOI +5682张) | ΔOI/Volume 94.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5682张（+5028.3% vs前日OI），连续性待观察（方向未知）
11-02 45.0C — Vol 8,755 | 最新价 $0.39 | OI 44→5049 (ΔOI +5005张) | ΔOI/Volume 57.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5005张（+11375.0% vs前日OI），连续性待观察（方向未知）
11-20 49.0C — Vol 6,311 | 最新价 $0.47 | OI 3494→7621 (ΔOI +4127张) | ΔOI/Volume 65.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4127张（+118.1% vs前日OI），连续性待观察（方向未知）
11-02 49.0C — Vol 5,210 | 最新价 $0.01 | OI 1044→4863 (ΔOI +3819张) | ΔOI/Volume 73.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3819张（+365.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 25,696 张（Put 0 / Call 25,696），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 29.2k / P 12.4k，今日成交量: C 12.2k / P 4.5k，平值价格ATM: C $0.21 / P $0.23 ｜ ATM IV 43.8%，预期波动 ±0.9%，Max Pain 45
Top ΔOI: C 45 +5,005 ｜ C 49 +3,819 ｜ C 44 +2,700

📆 Forward Expiration Structure

11-04  C +10.0k / P +1.8k ｜ Activity HIGH ｜ 2D
11-06  C +19.2k / P +4.7k ｜ Activity MEDIUM △ ｜ 4D
11-09  C +0.9k / P +0.4k ｜ Activity HIGH ｜ 7D
11-11  C +4.0k / P +0.5k ｜ Activity HIGH ｜ 9D

📆 11-04 Forward Structure
存量OI: C 24.2k / P 9.2k，今日变化ΔOI: C +10.0k / P +1.8k，平值价格ATM: C $0.75 / P $0.71 ｜ ATM IV 50.0%，净 delta 敞口 476k shares
Top ΔOI: C 44 +1,882 ｜ C 44 +1,494 ｜ C 46 +1,089
仓位参考: Max Pain 44 ｜ Call Wall 50（+8.7%，弱）（OI 3.2k） ｜ Put Wall 44（-4.4%）（OI 2.6k）
量化解读： 存量 Call 重｜ATM IV 50.0%｜历史 Rank 72%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 475,955 股

11-06（MEDIUM △）Top ΔOI: 50C +7,063 ｜ 45P +2,582
11-06（MEDIUM △）仓位参考: Max Pain 48 ｜ Call Wall 50（+8.7%，弱）（OI 12.9k） ｜ Put Wall 45（-2.2%，弱）（OI 4.2k）

📆 11-09 Forward Structure
存量OI: C 2.8k / P 2.1k，今日变化ΔOI: C +0.9k / P +0.4k，平值价格ATM: C $1.14 / P $1.05 ｜ ATM IV 42.4%，净 delta 敞口 53k shares
Top ΔOI: C 46 +178 ｜ C 47 +116
仓位参考: Max Pain 46 ｜ Call Wall 47（+2.2%，弱）（OI 0.4k） ｜ Put Wall 43（-6.5%）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 42.4%｜历史 Rank 72%（近端代理）｜IV/RV 0.97×（近似）｜净 delta 敞口 正 53,014 股

📆 11-11 Forward Structure
存量OI: C 4.9k / P 1.5k，今日变化ΔOI: C +4.0k / P +0.5k，平值价格ATM: C $1.32 / P $1.23 ｜ ATM IV 43.4%，净 delta 敞口 74k shares
Top ΔOI: C 47 +487
仓位参考: Max Pain 45 ｜ Call Wall 50（+8.7%，弱）（OI 0.7k） ｜ Put Wall 45（-2.2%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 43.4%｜历史 Rank 72%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 正 74,153 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/SLV_morning.json