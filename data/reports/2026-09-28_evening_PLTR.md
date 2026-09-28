# 期权晚报 2026-09-28（快照 16:40 ET）

📊 市场环境

SPY $765.61 ｜ QQQ $736.53
VIX 16.07 ↑8.1%（5D +8.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.24 ｜ 实际 待公布 ｜ 前值 7.271
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 54.9 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 84 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 195P ΔOI +750（距现价 +4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 186.23 → 收盘 187.48（+0.7%） ｜ 今日高 190.25 ｜ 低 185.62 ｜ 昨收 189.67 → 收盘 187.48（-1.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.60 | OI比 0.71 | ATM IV 49.6% | Skew 2.0pp | Term 0.94 | ExpMove ±4.2%（近端） | Rank 36%
量化视角： IV 中性（Rank 36%）｜期限结构正常（Term 0.94）｜保护溢价薄（Skew 2.0pp）｜存量 Call 偏重（OI比 0.71）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.71×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（4D）±4.2% ｜ 10-09（11D）±6.5% ｜ 10-16（18D）±8.1% ｜ 10-23（25D）±9.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 34,020,340 | GEX Change vs 上次快照 -5,385,086 | Flip: Primary Flip: 178.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 569 / LOW 86 / INVALID 179
结构观察区: Primary Flip 178.03（全链重定价，覆盖 100%）
Put Wall 170（弱结构｜现价高于该位 10.3%） | Call Wall 200（现价低于该位 6.3%）
最近结构参考: Flip 178（现价高于该位 5.3%）
量化视角： 正 Gamma（3402万，无历史分位）｜正 Gamma 减弱（539万）｜现价位于 Flip 上方 5.31%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Put Wall，弱结构） / 182（MaxPain，仅结算参考）；上方 200（Call Wall）。
• Gamma 区域：切换参考 178（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 197.5C — Vol 3,296 | 最新价 $0.84 | OI 6259→13208 (ΔOI +6949张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6949张（+111.0% vs前日OI），连续性待观察（方向未知）
10-02 205.0C — Vol 3,307 | 最新价 $0.23 | OI 6152→12863 (ΔOI +6711张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6711张（+109.1% vs前日OI），连续性待观察（方向未知）
10-09 105.0P — Vol 1 | 最新价 $0.02 | OI 2225→4825 (ΔOI +2600张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2600张（+116.8% vs前日OI），连续性待观察（方向未知）
10-16 190.0P — Vol 483 | 最新价 $8.71 | OI 1075→3670 (ΔOI +2595张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2595张（+241.4% vs前日OI），连续性待观察（方向未知）
10-02 207.5C — Vol 1,461 | 最新价 $0.17 | OI 7542→9738 (ΔOI +2196张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2196张（+29.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 21,051 张（Put 5,195 / Call 15,856），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +27.0k / P +11.8k ｜ Activity HIGH ｜ 4D
10-09  C +2.6k / P +6.4k ｜ Activity HIGH ｜ 11D
10-16  C -0.7k / P +6.5k ｜ Activity HIGH ｜ 18D
10-23  C +1.4k / P +1.6k ｜ Activity HIGH ｜ 25D

📆 10-02 Forward Structure
存量OI: C 100.4k / P 71.0k，今日变化ΔOI: C +27.0k / P +11.8k，平值价格ATM: C $3.94 / P $3.90 ｜ ATM IV 49.6%，净 delta 敞口 255k shares
Top ΔOI: C 197 +6,949 ｜ C 205 +6,711
仓位参考: Max Pain 182 ｜ Call Wall 200（+6.7%，弱）（OI 17.1k） ｜ Put Wall 185（-1.3%，弱）（OI 4.8k）
量化解读： 存量 Call 重｜ATM IV 49.6%｜历史 Rank 36%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 254,752 股

📆 10-09 Forward Structure
存量OI: C 24.9k / P 38.3k，今日变化ΔOI: C +2.6k / P +6.4k，平值价格ATM: C $6.19 / P $5.90 ｜ ATM IV 46.6%，净 delta 敞口 -40k shares
Top ΔOI: P 170 +772 ｜ P 195 +750
仓位参考: Max Pain 182 ｜ Call Wall 200（+6.7%，弱）（OI 3.3k） ｜ Put Wall 190（+1.3%，弱）（OI 3.9k）
量化解读： 存量 Put 重｜ATM IV 46.6%｜历史 Rank 36%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 40,447 股

📆 10-16 Forward Structure
存量OI: C 148.8k / P 168.8k，今日变化ΔOI: C -0.7k / P +6.5k，平值价格ATM: C $7.87 / P $7.30 ｜ ATM IV 46.0%，净 delta 敞口 -203k shares
Top ΔOI: P 190 +2,595 ｜ C 210 -776
仓位参考: Max Pain 165 ｜ Call Wall 170（-9.3%，弱）（OI 14.7k） ｜ Put Wall 170（-9.3%，弱）（OI 14.8k）
量化解读： 存量两侧均衡｜ATM IV 46.0%｜历史 Rank 36%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 202,954 股

📆 10-23 Forward Structure
存量OI: C 19.1k / P 11.5k，今日变化ΔOI: C +1.4k / P +1.6k，平值价格ATM: C $9.75 / P $8.60 ｜ ATM IV 45.9%，净 delta 敞口 1k shares
仓位参考: Max Pain 178 ｜ Call Wall 180（-4.0%）（OI 4.6k） ｜ Put Wall 175（-6.7%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 45.9%｜历史 Rank 36%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 正 1,494 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/PLTR_evening.json