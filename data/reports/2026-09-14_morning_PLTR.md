# 期权晨报 2026-09-14（快照 10:20 ET）

📊 市场环境

SPY $761.06 ｜ QQQ $709.18
VIX 17.27 ↑9.0%（5D +12.9%） ｜ Vol Regime: NORMAL
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
🟡 **近现价集中开仓**: 09-18 172C ΔOI +5,317（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 167.23 → 今开 169.70（+1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 170.20 ｜ 低 166.42

Options: P/C成交量 0.45 | OI比 0.86 | ATM IV 53.3% | Skew 3.3pp | Term 0.89 | ExpMove ±4.6%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.89，近月 IV 高于远月）｜保护溢价中性（Skew 3.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（4D）±4.6% ｜ 09-25（11D）±6.7% ｜ 10-02（18D）±8.5% ｜ 10-09（25D）±10.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 25,254,908 | GEX Change vs 上次快照 -3,731,783 | Flip: Primary Flip: 163.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 575 / LOW 56 / INVALID 189
结构观察区: Primary Flip 163.14（全链重定价，覆盖 100%）
Put Wall 170（弱结构｜现价低于该位 1.2%） | Call Wall 170（弱结构｜现价低于该位 1.2%）
最近结构参考: Put Wall 170（现价低于该位 1.2%）
量化视角： 正 Gamma（2525万，无历史分位）｜正 Gamma 减弱（373万）｜现价位于 Flip 上方 2.97%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 155（MaxPain，仅结算参考）；上方 170（Put Wall，弱结构） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 163（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 172.5C — Vol 8,472 | 最新价 $1.94 | OI 7563→12880 (ΔOI +5317张) | ΔOI/Volume 62.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5317张（+70.3% vs前日OI），连续性待观察（方向未知）
09-18 180.0C — Vol 8,585 | 最新价 $0.60 | OI 17353→20040 (ΔOI +2687张) | ΔOI/Volume 31.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2687张（+15.5% vs前日OI），连续性待观察（方向未知）
09-18 170.0C — Vol 9,796 | 最新价 $2.76 | OI 20305→22913 (ΔOI +2608张) | ΔOI/Volume 26.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2608张（+12.8% vs前日OI），连续性待观察（方向未知）
09-18 175.0C — Vol 9,378 | 最新价 $1.33 | OI 16367→18900 (ΔOI +2533张) | ΔOI/Volume 27.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2533张（+15.5% vs前日OI），连续性待观察（方向未知）
09-18 65.0P — Vol 2,444 | 最新价 $0.01 | OI 2908→5284 (ΔOI +2376张) | ΔOI/Volume 97.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2376张（+81.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 15,521 张（Put 2,376 / Call 13,145），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +18.3k / P +16.4k ｜ Activity HIGH ｜ 4D
09-25  C +1.3k / P +0.6k ｜ Activity HIGH ｜ 11D
10-02  C +0.7k / P +0.7k ｜ Activity MEDIUM △ ｜ 18D
10-09  C +0.8k / P +0.7k ｜ Activity MEDIUM △ ｜ 25D

📆 09-18 Forward Structure
存量OI: C 324.2k / P 278.4k，今日变化ΔOI: C +18.3k / P +16.4k，平值价格ATM: C $3.95 / P $3.78 ｜ ATM IV 53.3%，净 delta 敞口 312k shares
Top ΔOI: C 172 +5,317 ｜ C 180 +2,687 ｜ C 170 +2,608
仓位参考: Max Pain 155 ｜ Call Wall 170（+1.2%，弱）（OI 22.9k）
量化解读： 存量两侧均衡｜ATM IV 53.3%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 311,763 股

📆 09-25 Forward Structure
存量OI: C 25.3k / P 32.8k，今日变化ΔOI: C +1.3k / P +0.6k，平值价格ATM: C $5.85 / P $5.40 ｜ ATM IV 48.3%，净 delta 敞口 36k shares
仓位参考: Max Pain 172
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 48.3%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 35,645 股

10-02（MEDIUM △）Top ΔOI: 170P +237 ｜ 182C +158
10-02（MEDIUM △）仓位参考: Max Pain 172 ｜ Call Wall 180（+7.2%，弱）（OI 2.5k） ｜ Put Wall 170（+1.2%）（OI 4.6k）

10-09（MEDIUM △）Top ΔOI: 172C +289 ｜ 172P +227
10-09（MEDIUM △）仓位参考: Max Pain 170 ｜ Put Wall 170（+1.2%）（OI 2.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/PLTR_morning.json