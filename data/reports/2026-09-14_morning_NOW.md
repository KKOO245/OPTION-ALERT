# 期权晨报 2026-09-14（快照 10:20 ET）

📊 市场环境

SPY $760.44 ｜ QQQ $706.04
VIX 17.27 ↑9.0%（5D +12.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.1（fear）
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
🟡 **单日价格波动**: +4.5%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## NOW

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NOW  昨收 132.53 → 今开 140.00（+5.6%） | 较昨收变动（含盘初走势） ｜ 今日高 141.15 ｜ 低 137.42

Options: P/C成交量 0.48 | OI比 0.97 | ATM IV 63.3% | Skew -0.1pp | Term 0.85 | ExpMove ±5.9%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.85，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.97×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（4D）±5.9% ｜ 09-25（11D）±11.5% ｜ 10-02（18D）±13.9% ｜ 10-09（25D）±12.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 19,202,864 | GEX Change vs 上次快照 5,855,700 | Flip: Primary Flip: 124.37（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 627 / LOW 63 / INVALID 112
结构观察区: Primary Flip 124.37（全链重定价，覆盖 100%）
Call Wall 150（弱结构｜现价低于该位 7.7%）
最近结构参考: Call Wall 150（现价低于该位 7.7%）
量化视角： 正 Gamma（1920万，无历史分位）｜正 Gamma 增强（+586万）｜现价位于 Flip 上方 11.36%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 120（MaxPain，仅结算参考）；上方 150（Call Wall，弱结构）。
• Gamma 区域：切换参考 124（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 125.0P — Vol 1,157 | 最新价 $4.80 | OI 2036→2429 (ΔOI +393张) | ΔOI/Volume 34.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增393张（+19.3% vs前日OI），连续性待观察（方向未知）
10-02 121.0P — Vol 363 | 最新价 $1.96 | OI 127→487 (ΔOI +360张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增360张（+283.5% vs前日OI），连续性待观察（方向未知）
09-25 150.0C — Vol 806 | 最新价 $0.88 | OI 821→1178 (ΔOI +357张) | ΔOI/Volume 44.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增357张（+43.5% vs前日OI），连续性待观察（方向未知）
09-18 131.0P — Vol 732 | 最新价 $2.74 | OI 312→644 (ΔOI +332张) | ΔOI/Volume 45.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增332张（+106.4% vs前日OI），连续性待观察（方向未知）
09-25 145.0C — Vol 404 | 最新价 $1.46 | OI 1803→2104 (ΔOI +301张) | ΔOI/Volume 74.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增301张（+16.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,743 张（Put 1,085 / Call 658），跨 4 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +2.3k / P +2.2k ｜ Activity HIGH ｜ 4D
09-25  C +1.0k / P +0.4k ｜ Activity HIGH ｜ 11D
10-02  C +0.2k / P +0.5k ｜ Activity MEDIUM △ ｜ 18D
10-09  C +0.1k / P +0.3k ｜ Activity MEDIUM △ ｜ 25D

📆 09-18 Forward Structure
存量OI: C 112.7k / P 108.8k，今日变化ΔOI: C +2.3k / P +2.2k，平值价格ATM: C $4.90 / P $3.23 ｜ ATM IV 63.3%，净 delta 敞口 57k shares
Top ΔOI: P 131 +332 ｜ P 129 +290 ｜ P 132 +276
仓位参考: Max Pain 120
量化解读： 存量两侧均衡｜ATM IV 63.3%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 56,739 股

📆 09-25 Forward Structure
存量OI: C 9.3k / P 8.7k，今日变化ΔOI: C +1.0k / P +0.4k，平值价格ATM: C $6.95 / P $9.00 ｜ ATM IV 56.4%，净 delta 敞口 34k shares
Top ΔOI: C 150 +357 ｜ C 145 +301 ｜ C 136 +92
仓位参考: Max Pain 132 ｜ Call Wall 145（+4.7%）（OI 2.1k）
量化解读： 存量两侧均衡｜ATM IV 56.4%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 34,402 股

10-02（MEDIUM △）Top ΔOI: 121P +360 ｜ 148C +65
10-02（MEDIUM △）仓位参考: Max Pain 131 ｜ Call Wall 150（+8.3%，弱）（OI 1.5k）

10-09（MEDIUM △）仓位参考: Max Pain 140

📅 事件差分（观察，非因果）: 09-18（4D）ATM IV 63.3% vs 09-25 56.4%（差 +6.9pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/NOW_morning.json