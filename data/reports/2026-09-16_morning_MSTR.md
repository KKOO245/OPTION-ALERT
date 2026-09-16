# 期权晨报 2026-09-16（快照 11:22 ET）

📊 市场环境

SPY $760.53 ｜ QQQ $710.91
VIX 16.68 ↓3.0%（5D +1.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75　⏰ 今日
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　⏰ 今日
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　⏰ 今日
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🔴 **事件差分**: 09-18（2D）ATM IV 85.6% vs 09-25 70.1%（差 +15.6pp），覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 129.60 → 今开 129.84（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 130.42 ｜ 低 125.91

Options: P/C成交量 0.95 | OI比 0.63 | ATM IV 85.6% | Skew -6.3pp | Term 0.80 | ExpMove ±5.3%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（2D）±5.3% ｜ 09-25（9D）±8.9% ｜ 10-02（16D）±11.7% ｜ 10-09（23D）±13.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 32,309,686 | GEX Change vs 上次快照 -23,352,959 | Flip: Primary Flip: 121.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 814 / LOW 115 / INVALID 269
结构观察区: Primary Flip 121.90（全链重定价，覆盖 99%）
最近结构参考: Flip 122（现价高于该位 3.9%）
量化视角： 正 Gamma（3231万，无历史分位）｜正 Gamma 减弱（2335万）｜现价位于 Flip 上方 3.94%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 122（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 122（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 115.0P — Vol 6,760 | 最新价 $0.39 | OI 3901→8179 (ΔOI +4278张) | ΔOI/Volume 63.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4278张（+109.7% vs前日OI），连续性待观察（方向未知）
09-18 120.0P — Vol 28,189 | 最新价 $0.89 | OI 10338→14055 (ΔOI +3717张) | ΔOI/Volume 13.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3717张（+36.0% vs前日OI），连续性待观察（方向未知）
09-18 110.0P — Vol 4,899 | 最新价 $0.18 | OI 4677→6070 (ΔOI +1393张) | ΔOI/Volume 28.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1393张（+29.8% vs前日OI），连续性待观察（方向未知）
09-18 132.0C — Vol 5,795 | 最新价 $3.12 | OI 2727→3918 (ΔOI +1191张) | ΔOI/Volume 20.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1191张（+43.7% vs前日OI），连续性待观察（方向未知）
10-02 65.0P — Vol 1,129 | 最新价 $0.12 | OI 1170→2297 (ΔOI +1127张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1127张（+96.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,706 张（Put 10,515 / Call 1,191），跨 2 个期限｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +1.0k / P +11.7k ｜ Activity HIGH ｜ 2D
09-25  C +2.1k / P +4.7k ｜ Activity HIGH ｜ 9D
10-02  C +1.7k / P +4.5k ｜ Activity HIGH ｜ 16D
10-09  C +2.1k / P +4.1k ｜ Activity HIGH ｜ 23D

📆 09-18 Forward Structure
存量OI: C 475.7k / P 297.8k，今日变化ΔOI: C +1.0k / P +11.7k，平值价格ATM: C $3.15 / P $3.60 ｜ ATM IV 85.6%，净 delta 敞口 -98k shares
Top ΔOI: P 115 +4,278 ｜ P 120 +3,717
仓位参考: Max Pain 122 ｜ Call Wall 135（+6.6%，弱）（OI 24.0k） ｜ Put Wall 120（-5.3%，弱）（OI 14.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 85.6%｜历史 Rank 58%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 98,143 股

📆 09-25 Forward Structure
存量OI: C 32.1k / P 57.1k，今日变化ΔOI: C +2.1k / P +4.7k，平值价格ATM: C $5.50 / P $5.83 ｜ ATM IV 70.1%，净 delta 敞口 -87k shares
Top ΔOI: P 120 +614 ｜ C 144 +535
仓位参考: Max Pain 129 ｜ Call Wall 130（+2.6%，弱）（OI 1.4k） ｜ Put Wall 125（-1.3%，弱）（OI 2.7k）
量化解读： 存量 Put 重｜ATM IV 70.1%｜历史 Rank 58%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 86,616 股

📆 10-02 Forward Structure
存量OI: C 24.6k / P 41.1k，今日变化ΔOI: C +1.7k / P +4.5k，平值价格ATM: C $7.52 / P $7.35 ｜ ATM IV 68.7%，净 delta 敞口 -12k shares
仓位参考: Max Pain 130 ｜ Put Wall 130（+2.6%，弱）（OI 2.6k）
量化解读： 存量 Put 重｜ATM IV 68.7%｜历史 Rank 58%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 11,510 股

📆 10-09 Forward Structure
存量OI: C 8.3k / P 23.0k，今日变化ΔOI: C +2.1k / P +4.1k，平值价格ATM: C $8.80 / P $8.80 ｜ ATM IV 68.4%，净 delta 敞口 5k shares
Top ΔOI: C 150 +976 ｜ C 140 +972
仓位参考: Max Pain 135 ｜ Call Wall 130（+2.6%，弱）（OI 0.4k） ｜ Put Wall 130（+2.6%，弱）（OI 2.4k）
量化解读： 存量 Put 重｜ATM IV 68.4%｜历史 Rank 58%（近端代理）｜净 delta 敞口 正 5,378 股

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 85.6% vs 09-25 70.1%（差 +15.6pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/MSTR_morning.json