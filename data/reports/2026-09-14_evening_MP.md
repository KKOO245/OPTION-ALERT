# 期权晚报 2026-09-14（快照 16:48 ET）

📊 市场环境

SPY $760.88 ｜ QQQ $709.18
VIX 17.10 ↑8.0%（5D +11.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.9 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 49.77 → 收盘 50.68（+1.8%） ｜ 今日高 51.74 ｜ 低 49.53 ｜ 昨收 50.51 → 收盘 50.68（+0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.12 | OI比 0.83 | ATM IV 70.6% | Skew -2.5pp | Term 0.88 | ExpMove ±5.8%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.12×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（4D）±5.8% ｜ 09-25（11D）±8.9% ｜ 10-02（18D）±10.9% ｜ 10-09（25D）±14.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,395,925 | GEX Change vs 上次快照 1,544,839 | Flip: Primary Flip: 53.65（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 258 / LOW 39 / INVALID 121
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 53.65（全链重定价，覆盖 100%）
Put Wall 55（弱结构｜现价低于该位 7.9%）
最近结构参考: Flip 54（现价低于该位 5.5%）
量化视角： 负 Gamma（440万，无历史分位）｜负 Gamma 缓解（+154万）｜现价位于 Flip 下方 5.54%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 55（Put Wall，弱结构） / 55（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 54（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 53.0P — Vol 62 | 最新价 $2.84 | OI 296→665 (ΔOI +369张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增369张（+124.7% vs前日OI），值得跟踪（方向未知）
09-18 49.0P — Vol 356 | 最新价 $0.68 | OI 280→566 (ΔOI +286张) | ΔOI/Volume 80.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增286张（+102.1% vs前日OI），连续性待观察（方向未知）
09-18 54.0P — Vol 182 | 最新价 $3.58 | OI 281→524 (ΔOI +243张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增243张（+86.5% vs前日OI），值得跟踪（方向未知）
09-18 55.0C — Vol 898 | 最新价 $0.34 | OI 4579→4803 (ΔOI +224张) | ΔOI/Volume 24.9% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增224张（+4.9% vs前日OI），值得跟踪（方向未知）
09-18 52.0C — Vol 270 | 最新价 $1.03 | OI 128→268 (ΔOI +140张) | ΔOI/Volume 51.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增140张（+109.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,262 张（Put 898 / Call 364），跨 1 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 11D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 09-18 Forward Structure
存量OI: C 52.6k / P 43.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.46 / P $1.46 ｜ ATM IV 70.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 55 ｜ Call Wall 55（+8.5%，弱）（OI 4.8k） ｜ Put Wall 55（+8.5%，弱）（OI 8.8k）
量化解读： 存量 Call 重｜ATM IV 70.6%｜历史 Rank 54%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 54 ｜ Call Wall 55（+8.5%，弱）（OI 0.3k） ｜ Put Wall 55（+8.5%，弱）（OI 0.7k）

10-02（Activity LOW）仓位参考: Max Pain 58 ｜ Call Wall 55（+8.5%，弱）（OI 0.1k） ｜ Put Wall 50（-1.3%）（OI 1.2k）

10-09（Activity LOW）仓位参考: Max Pain 52 ｜ Call Wall 55（+8.5%）（OI 1.0k） ｜ Put Wall 47（-7.3%）（OI 1.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/MP_evening.json