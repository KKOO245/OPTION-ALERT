# 期权晚报 2026-09-21（快照 16:40 ET）

📊 市场环境

SPY $773.50 ｜ QQQ $741.47
VIX 14.87 ↑0.4%（5D -13.0%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 33.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **事件差分**: 09-25 ATM IV 88.5% vs 10-02 77.8%（差 +10.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-25 16C ΔOI +635（距现价 -1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 16.68 → 收盘 16.78（+0.6%） ｜ 今日高 17.04 ｜ 低 16.28 ｜ 昨收 15.37 → 收盘 16.78（+9.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.41 | OI比 0.49 | ATM IV 88.5% | Skew 3.5pp | Term 0.85 | ExpMove ±7.6%（近端） | Rank 12%
量化视角： IV 历史低位（Rank 12%，期权偏便宜）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价中性（Skew 3.5pp）｜存量 Call 偏重（OI比 0.49）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.41×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（4D）±7.6% ｜ 10-02（11D）±11.1% ｜ 10-09（18D）±14.6% ｜ 10-16（25D）±15.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,263,328 | GEX Change vs 上次快照 478,066 | Flip: Primary Flip: 15.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 252 / LOW 57 / INVALID 127
结构观察区: Primary Flip 15.44（全链重定价，覆盖 100%）
最近结构参考: Flip 15（现价高于该位 8.7%）
量化视角： 正 Gamma（426万，无历史分位）｜正 Gamma 增强（+48万）｜现价位于 Flip 上方 8.67%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 16（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 15（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 21.0C — Vol 71 | 最新价 $0.44 | OI 32→5019 (ΔOI +4987张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4987张（+15584.4% vs前日OI），连续性待观察（方向未知）
09-25 16.5C — Vol 2,281 | 最新价 $0.80 | OI 1393→2028 (ΔOI +635张) | ΔOI/Volume 27.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增635张（+45.6% vs前日OI），连续性待观察（方向未知）
10-16 15.0P — Vol 463 | 最新价 $0.50 | OI 4655→5290 (ΔOI +635张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增635张（+13.6% vs前日OI），值得跟踪（方向未知）
09-25 14.5P — Vol 621 | 最新价 $0.03 | OI 975→1419 (ΔOI +444张) | ΔOI/Volume 71.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增444张（+45.5% vs前日OI），连续性待观察（方向未知）
09-25 15.0P — Vol 842 | 最新价 $0.06 | OI 1179→1608 (ΔOI +429张) | ΔOI/Volume 51.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增429张（+36.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,130 张（Put 1,508 / Call 5,622），跨 3 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +2.0k / P +1.9k ｜ Activity HIGH ｜ 4D
10-02  C +0.4k / P +0.4k ｜ Activity MEDIUM △ ｜ 11D
10-09  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 18D
10-16  C -1.7k / P +0.9k ｜ Activity HIGH ｜ 25D

📆 09-25 Forward Structure
存量OI: C 20.2k / P 9.8k，今日变化ΔOI: C +2.0k / P +1.9k，平值价格ATM: C $0.58 / P $0.70 ｜ ATM IV 88.5%，净 delta 敞口 95k shares
Top ΔOI: C 16 +635
仓位参考: Max Pain 16 ｜ Call Wall 18（+7.3%，弱）（OI 2.3k） ｜ Put Wall 16.5（-1.7%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 88.5%｜历史 Rank 12%（近端代理）｜IV/RV 1.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 95,238 股

10-02（MEDIUM △）Top ΔOI: 17P +192 ｜ 15C +145
10-02（MEDIUM △）仓位参考: Max Pain 17 ｜ Put Wall 17（+1.3%）（OI 1.4k）

10-09（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 16（-4.6%）（OI 1.2k）

📆 10-16 Forward Structure
存量OI: C 29.1k / P 12.7k，今日变化ΔOI: C -1.7k / P +0.9k，平值价格ATM: C $1.30 / P $1.34 ｜ ATM IV 73.4%，净 delta 敞口 -14k shares
Top ΔOI: C 18 +194
仓位参考: Max Pain 17 ｜ Call Wall 18（+7.3%，弱）（OI 4.5k） ｜ Put Wall 17（+1.3%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 73.4%｜历史 Rank 12%（近端代理）｜IV/RV 1.50×（近似）｜净 delta 敞口 负 13,590 股

📅 事件差分（观察，非因果）: 09-25（4D）ATM IV 88.5% vs 10-02 77.8%（差 +10.6pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/USAR_evening.json