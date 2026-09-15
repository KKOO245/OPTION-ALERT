# 期权晚报 2026-09-15（快照 16:40 ET）

📊 市场环境

SPY $757.39 ｜ QQQ $704.54
VIX 17.20 ↑0.6%（5D +9.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **事件差分**: 09-18 ATM IV 78.1% vs 09-25 67.8%（差 +10.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🔵 **期限 OI 集中**: 10-02 95P ΔOI +2,850 占该期限总 OI 10.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 183.62 → 收盘 172.11（-6.3%） ｜ 今日高 184.13 ｜ 低 168.07 ｜ 昨收 191.45 → 收盘 172.11（-10.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.30 | OI比 0.53 | ATM IV 78.1% | Skew -3.6pp | Term 0.84 | ExpMove ±5.7%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.6pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.53）+ 当日成交偏 Put（P/C量 1.30）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.30×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.53×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（3D）±5.7% ｜ 09-25（10D）±9.1% ｜ 10-02（17D）±11.8% ｜ 10-09（24D）±13.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,698,970 | GEX Change vs 上次快照 -5,327,927 | Flip: Primary Flip: 166.57（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 524 / LOW 164 / INVALID 286
结构观察区: Primary Flip 166.57（全链重定价，覆盖 100%）
Put Wall 160（弱结构｜现价高于该位 7.6%）
最近结构参考: Flip 167（现价高于该位 3.3%）
量化视角： 正 Gamma（870万，无历史分位）｜正 Gamma 减弱（533万）｜现价位于 Flip 上方 3.33%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 160（Put Wall，弱结构）；上方 178（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 167（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 95.0P — Vol 10 | 最新价 $0.06 | OI 153→3003 (ΔOI +2850张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2850张（+1862.8% vs前日OI），连续性待观察（方向未知）
09-18 205.0C — Vol 2,061 | 最新价 $0.11 | OI 891→3389 (ΔOI +2498张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2498张（+280.4% vs前日OI），连续性待观察（方向未知）
09-18 202.5C — Vol 3,516 | 最新价 $0.20 | OI 558→2603 (ΔOI +2045张) | ΔOI/Volume 58.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2045张（+366.5% vs前日OI），连续性待观察（方向未知）
09-18 185.0P — Vol 1,323 | 最新价 $13.82 | OI 3216→5024 (ΔOI +1808张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1808张（+56.2% vs前日OI），连续性待观察（方向未知）
09-18 182.5P — Vol 1,130 | 最新价 $11.76 | OI 375→2138 (ΔOI +1763张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1763张（+470.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 10,964 张（Put 6,421 / Call 4,543），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +11.1k / P +13.7k ｜ Activity HIGH ｜ 3D
09-25  C +2.6k / P +3.0k ｜ Activity HIGH ｜ 10D
10-02  C +0.9k / P +4.4k ｜ Activity HIGH ｜ 17D
10-09  C +0.4k / P +85 ｜ Activity HIGH ｜ 24D

📆 09-18 Forward Structure
存量OI: C 220.7k / P 117.3k，今日变化ΔOI: C +11.1k / P +13.7k，平值价格ATM: C $4.75 / P $5.10 ｜ ATM IV 78.1%，净 delta 敞口 -831k shares
Top ΔOI: P 185 +1,808
仓位参考: Max Pain 178 ｜ Call Wall 182.5（+6.0%，弱）（OI 9.3k） ｜ Put Wall 160（-7.0%，弱）（OI 13.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 78.1%｜历史 Rank 54%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 831,338 股

📆 09-25 Forward Structure
存量OI: C 16.4k / P 13.8k，今日变化ΔOI: C +2.6k / P +3.0k，平值价格ATM: C $7.86 / P $7.85 ｜ ATM IV 67.8%，净 delta 敞口 -71k shares
仓位参考: Max Pain 175 ｜ Call Wall 185（+7.5%，弱）（OI 1.1k） ｜ Put Wall 160（-7.0%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 67.8%｜历史 Rank 54%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 71,192 股

📆 10-02 Forward Structure
存量OI: C 10.7k / P 15.9k，今日变化ΔOI: C +0.9k / P +4.4k，平值价格ATM: C $10.05 / P $10.27 ｜ ATM IV 67.3%，净 delta 敞口 -19k shares
仓位参考: Max Pain 188 ｜ Call Wall 187.5（+8.9%，弱）（OI 1.2k） ｜ Put Wall 172.5（+0.2%，弱）（OI 1.1k）
量化解读： 存量 Put 重｜ATM IV 67.3%｜历史 Rank 54%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 18,963 股

📆 10-09 Forward Structure
存量OI: C 2.5k / P 2.9k，今日变化ΔOI: C +0.4k / P +85，平值价格ATM: C $11.78 / P $11.40 ｜ ATM IV 66.2%，净 delta 敞口 2k shares
仓位参考: Max Pain 185 ｜ Call Wall 185（+7.5%，弱）（OI 0.2k） ｜ Put Wall 160（-7.0%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 66.2%｜历史 Rank 54%（近端代理）｜净 delta 敞口 正 2,372 股

📅 事件差分（观察，非因果）: 09-18（3D）ATM IV 78.1% vs 09-25 67.8%（差 +10.3pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/COIN_evening.json