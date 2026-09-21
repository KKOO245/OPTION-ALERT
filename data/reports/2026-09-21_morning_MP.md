# 期权晨报 2026-09-21（快照 10:20 ET）

📊 市场环境

SPY $773.06 ｜ QQQ $741.47
VIX 14.85 ↑0.3%（5D -13.2%） ｜ Vol Regime: LOW
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
🟡 **事件差分**: 09-25 ATM IV 72.0% vs 10-02 60.9%（差 +11.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-02 48C ΔOI +104（距现价 -2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 47.26 → 今开 48.58（+2.8%） | 较昨收变动（含盘初走势） ｜ 今日高 49.91 ｜ 低 48.58

Options: P/C成交量 0.35 | OI比 0.93 | ATM IV 72.0% | Skew -8.3pp | Term 0.86 | ExpMove ±6.0%（近端） | Rank 57%
量化视角： IV 中性（Rank 57%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -8.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.35×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.93×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（4D）±6.0% ｜ 10-02（11D）±8.8% ｜ 10-09（18D）±9.7% ｜ 10-16（25D）±6.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -903,619 | GEX Change vs 上次快照 886,733 | Flip: Primary Flip: 50.26（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 286 / LOW 56 / INVALID 142
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 50.26（全链重定价，覆盖 100%）
最近结构参考: Flip 50（现价低于该位 2.3%）
量化视角： 负 Gamma（90万，无历史分位）｜负 Gamma 缓解（+89万）｜现价位于 Flip 下方 2.33%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 51（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 50（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 52.0C — Vol 1,716 | 最新价 $0.28 | OI 296→1458 (ΔOI +1162张) | ΔOI/Volume 67.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1162张（+392.6% vs前日OI），连续性待观察（方向未知）
09-25 57.0C — Vol 1,439 | 最新价 $0.04 | OI 124→1123 (ΔOI +999张) | ΔOI/Volume 69.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增999张（+805.6% vs前日OI），连续性待观察（方向未知）
10-16 50.0P — Vol 958 | 最新价 $4.50 | OI 1838→2513 (ΔOI +675张) | ΔOI/Volume 70.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增675张（+36.7% vs前日OI），连续性待观察（方向未知）
09-25 46.0P — Vol 897 | 最新价 $0.76 | OI 217→718 (ΔOI +501张) | ΔOI/Volume 55.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增501张（+230.9% vs前日OI），连续性待观察（方向未知）
10-02 49.0C — Vol 493 | 最新价 $1.50 | OI 856→1280 (ΔOI +424张) | ΔOI/Volume 86.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增424张（+49.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,761 张（Put 1,176 / Call 2,585），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +3.3k / P +2.4k ｜ Activity HIGH ｜ 4D
10-02  C +0.8k / P +0.5k ｜ Activity HIGH ｜ 11D
10-09  C +79 / P +0.2k ｜ Activity MEDIUM △ ｜ 18D
10-16  C +0.2k / P +1.0k ｜ Activity MEDIUM △ ｜ 25D

📆 09-25 Forward Structure
存量OI: C 10.5k / P 9.7k，今日变化ΔOI: C +3.3k / P +2.4k，平值价格ATM: C $1.60 / P $1.33 ｜ ATM IV 72.0%，净 delta 敞口 20k shares
Top ΔOI: C 52 +1,162 ｜ P 46 +501
仓位参考: Max Pain 51 ｜ Call Wall 52（+5.9%，弱）（OI 1.5k） ｜ Put Wall 50（+1.9%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 72.0%｜历史 Rank 57%（近端代理）｜IV/RV 1.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 19,567 股

📆 10-02 Forward Structure
存量OI: C 5.3k / P 4.1k，今日变化ΔOI: C +0.8k / P +0.5k，平值价格ATM: C $2.22 / P $2.08 ｜ ATM IV 60.9%，净 delta 敞口 14k shares
Top ΔOI: C 49 +424 ｜ P 53 +141 ｜ C 48 +104
仓位参考: Max Pain 50 ｜ Call Wall 49（-0.2%）（OI 1.3k） ｜ Put Wall 50（+1.9%）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 60.9%｜历史 Rank 57%（近端代理）｜IV/RV 1.62×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 13,985 股

10-09（MEDIUM △）Top ΔOI: 54P +58 ｜ 46P +28
10-09（MEDIUM △）仓位参考: Max Pain 52 ｜ Put Wall 47（-4.3%）（OI 1.1k）

10-16（MEDIUM △）Top ΔOI: 50P +675 ｜ 45P +260
10-16（MEDIUM △）仓位参考: Max Pain 55 ｜ Call Wall 50（+1.9%，弱）（OI 2.4k） ｜ Put Wall 45（-8.3%，弱）（OI 3.2k）

📅 事件差分（观察，非因果）: 09-25（4D）ATM IV 72.0% vs 10-02 60.9%（差 +11.1pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/MP_morning.json