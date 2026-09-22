# 期权晨报 2026-09-22（快照 10:20 ET）

📊 市场环境

SPY $774.05 ｜ QQQ $745.53
VIX 14.54 ↓2.2%（5D -15.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 37.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **事件差分**: 09-25 ATM IV 92.5% vs 10-02 81.5%（差 +11.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-25 17C ΔOI +371（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 17.10 → 今开 17.08（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 17.11 ｜ 低 16.72

Options: P/C成交量 0.18 | OI比 0.44 | ATM IV 92.5% | Skew 3.4pp | Term 0.85 | ExpMove ±7.7%（近端） | Rank 24%
量化视角： IV 历史低位（Rank 24%，期权偏便宜）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价中性（Skew 3.4pp）｜存量 Call 偏重（OI比 0.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.18×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（3D）±7.7% ｜ 10-02（10D）±12.2% ｜ 10-09（17D）±14.3% ｜ 10-16（24D）±16.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,696,257 | GEX Change vs 上次快照 444,123 | Flip: Primary Flip: 15.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 244 / LOW 74 / INVALID 138
结构观察区: Primary Flip 15.41（全链重定价，覆盖 98%）
最近结构参考: Flip 15（现价高于该位 8.8%）
量化视角： 正 Gamma（170万，无历史分位）｜正 Gamma 增强（+44万）｜现价位于 Flip 上方 8.84%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 17（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 15（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 18.0C — Vol 928 | 最新价 $0.25 | OI 339→917 (ΔOI +578张) | ΔOI/Volume 62.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增578张（+170.5% vs前日OI），连续性待观察（方向未知）
09-25 17.0C — Vol 534 | 最新价 $0.67 | OI 80→451 (ΔOI +371张) | ΔOI/Volume 69.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增371张（+463.8% vs前日OI），连续性待观察（方向未知）
09-25 17.5C — Vol 357 | 最新价 $0.40 | OI 203→454 (ΔOI +251张) | ΔOI/Volume 70.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增251张（+123.7% vs前日OI），连续性待观察（方向未知）
10-09 18.0C — Vol 255 | 最新价 $0.95 | OI 39→286 (ΔOI +247张) | ΔOI/Volume 96.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增247张（+633.3% vs前日OI），连续性待观察（方向未知）
10-02 19.0C — Vol 262 | 最新价 $0.29 | OI 42→289 (ΔOI +247张) | ΔOI/Volume 94.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增247张（+588.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,694 张（Put 0 / Call 1,694），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +1.5k / P +0.1k ｜ Activity HIGH ｜ 3D
10-02  C +0.6k / P +38 ｜ Activity HIGH ｜ 10D
10-09  C +0.5k / P +5 ｜ Activity HIGH ｜ 17D
10-16  C +0.8k / P +0.2k ｜ Activity HIGH ｜ 24D

📆 09-25 Forward Structure
存量OI: C 7.6k / P 3.3k，今日变化ΔOI: C +1.5k / P +0.1k，平值价格ATM: C $0.67 / P $0.62 ｜ ATM IV 92.5%，净 delta 敞口 41k shares
Top ΔOI: C 18 +578 ｜ C 17 +371 ｜ C 17 +251
仓位参考: Max Pain 17 ｜ Call Wall 18（+7.3%，弱）（OI 0.9k） ｜ Put Wall 17（+1.4%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 92.5%｜历史 Rank 24%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 41,103 股

📆 10-02 Forward Structure
存量OI: C 3.7k / P 1.2k，今日变化ΔOI: C +0.6k / P +38，平值价格ATM: C $1.13 / P $0.92 ｜ ATM IV 81.5%，净 delta 敞口 14k shares
Top ΔOI: C 18 +150
仓位参考: Max Pain 18 ｜ Put Wall 16（-4.6%，弱）（OI 94）
量化解读： 存量 Call 重｜ATM IV 81.5%｜历史 Rank 24%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 13,575 股

📆 10-09 Forward Structure
存量OI: C 4.8k / P 0.5k，今日变化ΔOI: C +0.5k / P +5，平值价格ATM: C $1.25 / P $1.15 ｜ ATM IV 82.0%，净 delta 敞口 19k shares
Top ΔOI: C 18 +247 ｜ C 17 +31
仓位参考: Max Pain 18 ｜ Put Wall 16（-4.6%）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 82.0%｜历史 Rank 24%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 18,661 股

📆 10-16 Forward Structure
存量OI: C 19.7k / P 6.3k，今日变化ΔOI: C +0.8k / P +0.2k，平值价格ATM: C $1.40 / P $1.34 ｜ ATM IV 78.1%，净 delta 敞口 12k shares
Top ΔOI: P 17 +246
仓位参考: Max Pain 20 ｜ Put Wall 17（+1.4%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 78.1%｜历史 Rank 24%（近端代理）｜IV/RV 1.01×（近似）｜净 delta 敞口 正 11,947 股

📅 事件差分（观察，非因果）: 09-25（3D）ATM IV 92.5% vs 10-02 81.5%（差 +11.1pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/NNE_morning.json