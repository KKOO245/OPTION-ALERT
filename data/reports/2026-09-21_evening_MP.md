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
🟡 **近现价集中开仓**: 09-25 52C ΔOI +1,162（距现价 +4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 48.58 → 收盘 50.00（+2.9%） ｜ 今日高 50.65 ｜ 低 48.58 ｜ 昨收 47.26 → 收盘 50.00（+5.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.42 | OI比 0.93 | ATM IV 70.0% | Skew -8.8pp | Term 0.84 | ExpMove ±5.8%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜Put 保护异常便宜（Skew -8.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.93×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（4D）±5.8% ｜ 10-02（11D）±8.2% ｜ 10-09（18D）±10.3% ｜ 10-16（25D）±12.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -169,182 | GEX Change vs 上次快照 734,437 | Flip: Primary Flip: 50.19（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 268 / LOW 51 / INVALID 165
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 50.19（全链重定价，覆盖 98%）
最近结构参考: Flip 50（现价低于该位 0.4%）
量化视角： 负 Gamma（17万，无历史分位）｜负 Gamma 缓解（+73万）｜现价位于 Flip 下方 0.39%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 51（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 50（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 52.0C — Vol 1,178 | 最新价 $0.78 | OI 296→1458 (ΔOI +1162张) | ΔOI/Volume 98.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1162张（+392.6% vs前日OI），连续性待观察（方向未知）
09-25 57.0C — Vol 328 | 最新价 $0.13 | OI 124→1123 (ΔOI +999张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增999张（+805.6% vs前日OI），连续性待观察（方向未知）
10-16 50.0P — Vol 153 | 最新价 $2.95 | OI 1838→2513 (ΔOI +675张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增675张（+36.7% vs前日OI），连续性待观察（方向未知）
09-25 46.0P — Vol 361 | 最新价 $0.16 | OI 217→718 (ΔOI +501张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增501张（+230.9% vs前日OI），连续性待观察（方向未知）
10-02 49.0C — Vol 149 | 最新价 $2.69 | OI 856→1280 (ΔOI +424张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增424张（+49.5% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,761 张（Put 1,176 / Call 2,585），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +3.3k / P +2.4k ｜ Activity HIGH ｜ 4D
10-02  C +0.8k / P +0.5k ｜ Activity HIGH ｜ 11D
10-09  C +79 / P +0.2k ｜ Activity HIGH ｜ 18D
10-16  C +0.2k / P +1.0k ｜ Activity MEDIUM △ ｜ 25D

📆 09-25 Forward Structure
存量OI: C 10.5k / P 9.7k，今日变化ΔOI: C +3.3k / P +2.4k，平值价格ATM: C $1.53 / P $1.38 ｜ ATM IV 70.0%，净 delta 敞口 58k shares
Top ΔOI: C 52 +1,162 ｜ P 46 +501
仓位参考: Max Pain 51 ｜ Call Wall 52（+4.0%，弱）（OI 1.5k） ｜ Put Wall 50（+0.0%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 70.0%｜历史 Rank 54%（近端代理）｜IV/RV 1.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 57,904 股

📆 10-02 Forward Structure
存量OI: C 5.3k / P 4.1k，今日变化ΔOI: C +0.8k / P +0.5k，平值价格ATM: C $2.16 / P $1.93 ｜ ATM IV 61.4%，净 delta 敞口 21k shares
Top ΔOI: C 49 +424 ｜ P 53 +141 ｜ C 48 +104
仓位参考: Max Pain 50 ｜ Call Wall 49（-2.0%）（OI 1.3k） ｜ Put Wall 50（+0.0%）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 61.4%｜历史 Rank 54%（近端代理）｜IV/RV 1.63×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 20,619 股

📆 10-09 Forward Structure
存量OI: C 2.9k / P 2.2k，今日变化ΔOI: C +79 / P +0.2k，平值价格ATM: C $2.78 / P $2.37 ｜ ATM IV 61.8%，净 delta 敞口 -6k shares
Top ΔOI: P 54 +58 ｜ C 55 +43 ｜ P 46 +28
仓位参考: Max Pain 52 ｜ Put Wall 47（-6.0%）（OI 1.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 61.8%｜历史 Rank 54%（近端代理）｜IV/RV 1.64×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 5,926 股

10-16（MEDIUM △）Top ΔOI: 50P +675 ｜ 45P +260
10-16（MEDIUM △）仓位参考: Max Pain 55 ｜ Call Wall 50（+0.0%，弱）（OI 2.4k） ｜ Put Wall 45（-10.0%，弱）（OI 3.2k）

📅 事件差分（观察，非因果）: 09-25（4D）ATM IV 70.0% vs 10-02 61.4%（差 +8.6pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/MP_evening.json