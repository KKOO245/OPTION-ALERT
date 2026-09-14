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
🟡 **单日价格波动**: +3.5%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 169.70 → 收盘 173.31（+2.1%） ｜ 今日高 174.36 ｜ 低 166.42 ｜ 昨收 167.23 → 收盘 173.31（+3.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.44 | OI比 0.86 | ATM IV 55.3% | Skew 1.9pp | Term 0.87 | ExpMove ±4.7%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价薄（Skew 1.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（4D）±4.7% ｜ 09-25（11D）±6.9% ｜ 10-02（18D）±8.8% ｜ 10-09（25D）±10.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 46,869,109 | GEX Change vs 上次快照 21,614,202 | Flip: Primary Flip: 162.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 596 / LOW 85 / INVALID 139
结构观察区: Primary Flip 162.93（全链重定价，覆盖 100%）
Put Wall 170（弱结构｜现价高于该位 1.9%） | Call Wall 170（弱结构｜现价高于该位 1.9%）
最近结构参考: Put Wall 170（现价高于该位 1.9%）
量化视角： 正 Gamma（4687万，无历史分位）｜正 Gamma 增强（+2161万）｜现价位于 Flip 上方 6.37%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Put Wall，弱结构） / 155（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 163（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 172.5C — Vol 12,770 | 最新价 $4.60 | OI 7563→12880 (ΔOI +5317张) | ΔOI/Volume 41.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5317张（+70.3% vs前日OI），连续性待观察（方向未知）
09-18 180.0C — Vol 40,074 | 最新价 $1.64 | OI 17353→20040 (ΔOI +2687张) | ΔOI/Volume 6.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2687张（+15.5% vs前日OI），连续性待观察（方向未知）
09-18 170.0C — Vol 19,617 | 最新价 $5.95 | OI 20305→22913 (ΔOI +2608张) | ΔOI/Volume 13.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2608张（+12.8% vs前日OI），连续性待观察（方向未知）
09-18 175.0C — Vol 22,099 | 最新价 $3.26 | OI 16367→18900 (ΔOI +2533张) | ΔOI/Volume 11.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2533张（+15.5% vs前日OI），连续性待观察（方向未知）
09-18 65.0P — Vol 2,444（Yahoo补） | 最新价 $0.01 | OI 2908→5284 (ΔOI +2376张) | ΔOI/Volume 97.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2376张（+81.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 15,521 张（Put 2,376 / Call 13,145），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 11D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 09-18 Forward Structure
存量OI: C 324.2k / P 278.4k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.60 / P $3.59 ｜ ATM IV 55.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 155 ｜ Call Wall 170（-1.9%，弱）（OI 22.9k） ｜ Put Wall 170（-1.9%，弱）（OI 14.2k）
量化解读： 存量两侧均衡｜ATM IV 55.3%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 172 ｜ Call Wall 190（+9.6%，弱）（OI 2.2k） ｜ Put Wall 170（-1.9%，弱）（OI 3.0k）

10-02（Activity LOW）仓位参考: Max Pain 172 ｜ Call Wall 180（+3.9%，弱）（OI 2.5k） ｜ Put Wall 170（-1.9%）（OI 4.6k）

10-09（Activity LOW）仓位参考: Max Pain 170 ｜ Call Wall 172.5（-0.5%，弱）（OI 0.5k） ｜ Put Wall 170（-1.9%）（OI 2.6k）

📅 事件差分（观察，非因果）: 09-18（4D）ATM IV 55.3% vs 09-25 49.5%（差 +5.9pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/PLTR_evening.json