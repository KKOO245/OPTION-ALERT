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
🟡 **单日价格波动**: +7.6%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 140.00 → 收盘 142.35（+1.7%） ｜ 今日高 143.19 ｜ 低 137.24 ｜ 昨收 132.53 → 收盘 142.35（+7.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.45 | OI比 0.97 | ATM IV 60.8% | Skew 0.9pp | Term 0.87 | ExpMove ±5.0%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价薄（Skew 0.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.97×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（4D）±5.0% ｜ 09-25（11D）±7.6% ｜ 10-02（18D）±9.5% ｜ 10-09（25D）±11.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 21,772,908 | GEX Change vs 上次快照 2,570,043 | Flip: Primary Flip: 125.73（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 577 / LOW 79 / INVALID 146
结构观察区: Primary Flip 125.73（全链重定价，覆盖 100%）
Call Wall 150（弱结构｜现价低于该位 5.1%）
最近结构参考: Call Wall 150（现价低于该位 5.1%）
量化视角： 正 Gamma（2177万，无历史分位）｜正 Gamma 增强（+257万）｜现价位于 Flip 上方 13.22%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 120（MaxPain，仅结算参考）；上方 150（Call Wall，弱结构）。
• Gamma 区域：切换参考 126（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 125.0P — Vol 741 | 最新价 $2.43 | OI 2036→2429 (ΔOI +393张) | ΔOI/Volume 53.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增393张（+19.3% vs前日OI），连续性待观察（方向未知）
10-02 121.0P — Vol 14 | 最新价 $0.77 | OI 127→487 (ΔOI +360张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增360张（+283.5% vs前日OI），值得跟踪（方向未知）
09-25 150.0C — Vol 1,084 | 最新价 $2.72 | OI 821→1178 (ΔOI +357张) | ΔOI/Volume 32.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增357张（+43.5% vs前日OI），连续性待观察（方向未知）
09-18 131.0P — Vol 585 | 最新价 $0.46 | OI 312→644 (ΔOI +332张) | ΔOI/Volume 56.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增332张（+106.4% vs前日OI），连续性待观察（方向未知）
09-25 145.0C — Vol 4,731 | 最新价 $4.25 | OI 1803→2104 (ΔOI +301张) | ΔOI/Volume 6.4% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增301张（+16.7% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,743 张（Put 1,085 / Call 658），跨 4 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 11D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 09-18 Forward Structure
存量OI: C 112.7k / P 108.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.70 / P $3.37 ｜ ATM IV 60.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 120 ｜ Call Wall 140（-1.7%，弱）（OI 8.1k）
量化解读： 存量两侧均衡｜ATM IV 60.8%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 132 ｜ Call Wall 145（+1.9%）（OI 2.1k） ｜ Put Wall 130（-8.7%，弱）（OI 0.4k）

10-02（Activity LOW）仓位参考: Max Pain 131 ｜ Call Wall 150（+5.4%，弱）（OI 1.5k） ｜ Put Wall 130（-8.7%，弱）（OI 0.6k）

10-09（Activity LOW）仓位参考: Max Pain 140 ｜ Call Wall 150（+5.4%，弱）（OI 0.1k） ｜ Put Wall 140（-1.7%，弱）（OI 0.5k）

📅 事件差分（观察，非因果）: 09-18（4D）ATM IV 60.8% vs 09-25 54.7%（差 +6.1pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/NOW_evening.json