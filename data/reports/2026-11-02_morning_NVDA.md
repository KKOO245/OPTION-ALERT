# 期权晨报 2026-11-02（快照 10:20 ET）

📊 市场环境

SPY $760.66 ｜ QQQ $699.03
VIX 18.83 ↓3.0%（5D +2.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.4（fear）
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
🟡 **近现价集中开仓**: 11-04 200P ΔOI +5,798（距现价 -3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-11 190P ΔOI +2,572 占该期限总 OI 17.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 204.64 → 今开 207.59（+1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 209.03 ｜ 低 206.73

Options: P/C成交量 0.40 | OI比 1.33 | ATM IV 50.2% | Skew 5.3pp | Term 0.85 | ExpMove ±3.1%（近端） | Rank 73%
量化视角： IV 中性（Rank 73%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价中性（Skew 5.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.40×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.33×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-04（2D）±3.1% ｜ 11-06（4D）±3.9% ｜ 11-09（7D）±4.4% ｜ 11-11（9D）±5.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 120,540,486 | GEX Change vs 上次快照 185,996,609 | Flip: Primary Flip: 203.30（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 725 / LOW 188 / INVALID 517
结构观察区: Primary Flip 203.30（全链重定价，覆盖 98%）
Put Wall 190（弱结构｜现价高于该位 9.4%）
最近结构参考: Flip 203（现价高于该位 2.2%）
量化视角： 正 Gamma（1.21亿，无历史分位）｜由负转正（+1.86亿）｜现价位于 Flip 上方 2.25%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（Put Wall，弱结构） / 208（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 203（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 215.0C — Vol 44,347 | 最新价 $5.34 | OI 14664→52891 (ΔOI +38227张) | ΔOI/Volume 86.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增38227张（+260.7% vs前日OI），连续性待观察（方向未知）
11-06 220.0C — Vol 48,923 | 最新价 $0.46 | OI 10363→46241 (ΔOI +35878张) | ΔOI/Volume 73.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增35878张（+346.2% vs前日OI），连续性待观察（方向未知）
11-20 237.5C — Vol 39,256 | 最新价 $0.92 | OI 2139→37199 (ΔOI +35060张) | ΔOI/Volume 89.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增35060张（+1639.1% vs前日OI），连续性待观察（方向未知）
11-06 212.5C — Vol 48,175 | 最新价 $1.72 | OI 2499→36302 (ΔOI +33803张) | ΔOI/Volume 70.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33803张（+1352.7% vs前日OI），连续性待观察（方向未知）
11-06 207.5C — Vol 30,775 | 最新价 $3.45 | OI 327→24072 (ΔOI +23745张) | ΔOI/Volume 77.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23745张（+7261.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 166,713 张（Put 0 / Call 166,713），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 77.9k / P 103.8k，今日成交量: C 189.2k / P 75.9k，平值价格ATM: C $1.35 / P $0.93 ｜ ATM IV 50.2%，预期波动 ±1.1%，Max Pain 208
Top ΔOI: C 210 +8,067 ｜ P 200 +7,348 ｜ C 205 +6,109

📆 Forward Expiration Structure

11-04  C +24.0k / P +24.0k ｜ Activity HIGH ｜ 2D
11-06  C +146.6k / P +81.2k ｜ Activity HIGH ｜ 4D
11-09  C +3.3k / P +3.4k ｜ Activity HIGH ｜ 7D
11-11  C +2.4k / P +5.6k ｜ Activity HIGH ｜ 9D

📆 11-04 Forward Structure
存量OI: C 44.1k / P 41.6k，今日变化ΔOI: C +24.0k / P +24.0k，平值价格ATM: C $3.40 / P $2.96 ｜ ATM IV 48.2%，净 delta 敞口 366k shares
Top ΔOI: P 200 +5,798
仓位参考: Max Pain 208 ｜ Call Wall 220（+5.8%，弱）（OI 4.1k） ｜ Put Wall 200（-3.8%，弱）（OI 7.2k）
量化解读： 存量两侧均衡｜ATM IV 48.2%｜历史 Rank 73%（近端代理）｜IV/RV 1.61×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 365,612 股

📆 11-06 Forward Structure
存量OI: C 312.2k / P 246.0k，今日变化ΔOI: C +146.6k / P +81.2k，平值价格ATM: C $4.38 / P $3.82 ｜ ATM IV 45.6%，净 delta 敞口 4.5M shares
Top ΔOI: C 220 +35,878 ｜ C 212 +33,803 ｜ C 207 +23,745
仓位参考: Max Pain 210 ｜ Call Wall 220（+5.8%，弱）（OI 46.2k） ｜ Put Wall 200（-3.8%，弱）（OI 19.0k）
量化解读： 存量 Call 重｜ATM IV 45.6%｜历史 Rank 73%（近端代理）｜IV/RV 1.52×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,487,421 股

📆 11-09 Forward Structure
存量OI: C 6.6k / P 5.7k，今日变化ΔOI: C +3.3k / P +3.4k，平值价格ATM: C $4.90 / P $4.30 ｜ ATM IV 39.4%，净 delta 敞口 40k shares
Top ΔOI: P 187 +835 ｜ C 210 +393
仓位参考: Max Pain 210 ｜ Call Wall 220（+5.8%，弱）（OI 0.8k） ｜ Put Wall 187.5（-9.8%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 39.4%｜历史 Rank 73%（近端代理）｜IV/RV 1.31×（近似）｜净 delta 敞口 正 40,053 股

📆 11-11 Forward Structure
存量OI: C 4.7k / P 10.4k，今日变化ΔOI: C +2.4k / P +5.6k，平值价格ATM: C $5.60 / P $5.60 ｜ ATM IV 39.8%，净 delta 敞口 13k shares
Top ΔOI: P 190 +2,572 ｜ C 222 +694
仓位参考: Max Pain 210 ｜ Call Wall 225（+8.2%，弱）（OI 0.8k） ｜ Put Wall 190（-8.6%）（OI 4.8k）
量化解读： 存量 Put 重｜ATM IV 39.8%｜历史 Rank 73%（近端代理）｜IV/RV 1.33×（近似）｜净 delta 敞口 正 12,613 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/NVDA_morning.json