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

🔍 重点速览
🔴 **事件差分**: 09-18（4D）ATM IV 88.9% vs 09-25 73.8%（差 +15.2pp），覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **单日价格波动**: +9.4%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 180.98 → 收盘 191.45（+5.8%） ｜ 今日高 193.22 ｜ 低 180.29 ｜ 昨收 175.26 → 收盘 191.45（+9.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.64 | OI比 0.49 | ATM IV 88.9% | Skew -7.3pp | Term 0.77 | ExpMove ±7.5%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜Put 保护异常便宜（Skew -7.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.49）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（4D）±7.5% ｜ 09-25（11D）±10.2% ｜ 10-02（18D）±11.9% ｜ 10-09（25D）±14.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 23,522,252 | GEX Change vs 上次快照 -198,579 | Flip: Primary Flip: 163.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 564 / LOW 147 / INVALID 263
结构观察区: Primary Flip 163.50（全链重定价，覆盖 99%）
Call Wall 200（弱结构｜现价低于该位 4.3%）
最近结构参考: Call Wall 200（现价低于该位 4.3%）
量化视角： 正 Gamma（2352万，无历史分位）｜正 Gamma 减弱（20万）｜现价位于 Flip 上方 17.10%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 175（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 163（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 85.0P — Vol 7 | 最新价 $0.11 | OI 263→2937 (ΔOI +2674张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2674张（+1016.7% vs前日OI），连续性待观察（方向未知）
09-18 160.0P — Vol 12,015 | 最新价 $0.26 | OI 9844→12106 (ΔOI +2262张) | ΔOI/Volume 18.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2262张（+23.0% vs前日OI），连续性待观察（方向未知）
09-18 192.5C — Vol 2,492 | 最新价 $6.60 | OI 4457→6346 (ΔOI +1889张) | ΔOI/Volume 75.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1889张（+42.4% vs前日OI），连续性待观察（方向未知）
09-18 172.5P — Vol 659 | 最新价 $1.09 | OI 686→1693 (ΔOI +1007张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1007张（+146.8% vs前日OI），连续性待观察（方向未知）
09-18 212.5C — Vol 1,453 | 最新价 $1.74 | OI 78→971 (ΔOI +893张) | ΔOI/Volume 61.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增893张（+1144.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,725 张（Put 5,943 / Call 2,782），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 11D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 09-18 Forward Structure
存量OI: C 209.7k / P 103.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $6.60 / P $7.72 ｜ ATM IV 88.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 175 ｜ Call Wall 182.5（-4.7%，弱）（OI 9.7k） ｜ Put Wall 185（-3.4%，弱）（OI 3.2k）
量化解读： 存量 Call 重｜ATM IV 88.9%｜历史 Rank 78%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 170 ｜ Call Wall 200（+4.5%，弱）（OI 1.6k） ｜ Put Wall 190（-0.8%，弱）（OI 0.4k）

10-02（Activity LOW）仓位参考: Max Pain 188 ｜ Call Wall 187.5（-2.1%，弱）（OI 1.1k） ｜ Put Wall 172.5（-9.9%，弱）（OI 1.1k）

10-09（Activity LOW）仓位参考: Max Pain 182 ｜ Call Wall 185（-3.4%，弱）（OI 0.2k） ｜ Put Wall 182.5（-4.7%，弱）（OI 0.1k）

📅 事件差分（观察，非因果）: 09-18（4D）ATM IV 88.9% vs 09-25 73.8%（差 +15.2pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/COIN_evening.json