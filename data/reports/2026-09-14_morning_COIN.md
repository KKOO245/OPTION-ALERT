# 期权晨报 2026-09-14（快照 10:20 ET）

📊 市场环境

SPY $760.44 ｜ QQQ $706.09
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
🟡 **单日价格波动**: +7.6%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-18 ATM IV 83.9% vs 09-25 71.9%（差 +12.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-18 192C ΔOI +1,889（距现价 +2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 175.26 → 今开 180.98（+3.3%） | 较昨收变动（含盘初走势） ｜ 今日高 189.44 ｜ 低 180.29

Options: P/C成交量 0.29 | OI比 0.49 | ATM IV 83.9% | Skew -5.5pp | Term 0.80 | ExpMove ±7.3%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.49）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.29×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（4D）±7.3% ｜ 09-25（11D）±10.1% ｜ 10-02（18D）±12.5% ｜ 10-09（25D）±14.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 23,720,831 | GEX Change vs 上次快照 3,934,125 | Flip: Primary Flip: 162.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 542 / LOW 148 / INVALID 284
结构观察区: Primary Flip 162.91（全链重定价，覆盖 100%）
Call Wall 200（弱结构｜现价低于该位 5.7%）
最近结构参考: Call Wall 200（现价低于该位 5.7%）
量化视角： 正 Gamma（2372万，无历史分位）｜正 Gamma 增强（+393万）｜现价位于 Flip 上方 15.74%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 175（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 163（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 85.0P — Vol 3,022 | 最新价 $0.11 | OI 263→2937 (ΔOI +2674张) | ΔOI/Volume 88.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2674张（+1016.7% vs前日OI），连续性待观察（方向未知）
09-18 160.0P — Vol 3,431 | 最新价 $1.09 | OI 9844→12106 (ΔOI +2262张) | ΔOI/Volume 65.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2262张（+23.0% vs前日OI），连续性待观察（方向未知）
09-18 192.5C — Vol 3,017 | 最新价 $1.39 | OI 4457→6346 (ΔOI +1889张) | ΔOI/Volume 62.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1889张（+42.4% vs前日OI），连续性待观察（方向未知）
09-18 172.5P — Vol 1,410 | 最新价 $4.64 | OI 686→1693 (ΔOI +1007张) | ΔOI/Volume 71.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1007张（+146.8% vs前日OI），连续性待观察（方向未知）
09-18 212.5C — Vol 1,079 | 最新价 $0.24 | OI 78→971 (ΔOI +893张) | ΔOI/Volume 82.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增893张（+1144.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,725 张（Put 5,943 / Call 2,782），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +6.3k / P +6.6k ｜ Activity HIGH ｜ 4D
09-25  C +2.4k / P +1.6k ｜ Activity HIGH ｜ 11D
10-02  C +0.6k / P -0.1k ｜ Activity HIGH ｜ 18D
10-09  C +0.3k / P +0.3k ｜ Activity HIGH ｜ 25D

📆 09-18 Forward Structure
存量OI: C 209.7k / P 103.5k，今日变化ΔOI: C +6.3k / P +6.6k，平值价格ATM: C $7.50 / P $6.35 ｜ ATM IV 83.9%，净 delta 敞口 176k shares
Top ΔOI: P 160 +2,262 ｜ C 192 +1,889 ｜ P 172 +1,007
仓位参考: Max Pain 175 ｜ Call Wall 182.5（-3.2%，弱）（OI 9.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 83.9%｜历史 Rank 69%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 176,335 股

📆 09-25 Forward Structure
存量OI: C 13.9k / P 10.8k，今日变化ΔOI: C +2.4k / P +1.6k，平值价格ATM: C $10.00 / P $9.00 ｜ ATM IV 71.9%，净 delta 敞口 75k shares
Top ΔOI: C 200 +705 ｜ C 195 +320
仓位参考: Max Pain 170 ｜ Call Wall 200（+6.1%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 71.9%｜历史 Rank 69%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 75,171 股

📆 10-02 Forward Structure
存量OI: C 9.9k / P 11.5k，今日变化ΔOI: C +0.6k / P -0.1k，平值价格ATM: C $12.30 / P $11.30 ｜ ATM IV 68.6%，净 delta 敞口 27k shares
Top ΔOI: P 170 -199 ｜ C 177 +160
仓位参考: Max Pain 188 ｜ Put Wall 172.5（-8.5%，弱）（OI 1.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 68.6%｜历史 Rank 69%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 27,376 股

📆 10-09 Forward Structure
存量OI: C 2.1k / P 2.8k，今日变化ΔOI: C +0.3k / P +0.3k，平值价格ATM: C $13.35 / P $13.40 ｜ ATM IV 68.1%，净 delta 敞口 3k shares
Top ΔOI: P 180 +58 ｜ C 180 -53
仓位参考: Max Pain 182 ｜ Call Wall 185（-1.9%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 68.1%｜历史 Rank 69%（近端代理）｜净 delta 敞口 正 2,777 股

📅 事件差分（观察，非因果）: 09-18（4D）ATM IV 83.9% vs 09-25 71.9%（差 +12.0pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/COIN_morning.json