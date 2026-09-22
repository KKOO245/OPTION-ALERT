# 期权晨报 2026-09-22（快照 10:20 ET）

📊 市场环境

SPY $773.39 ｜ QQQ $744.98
VIX 14.54 ↓2.2%（5D -15.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 36.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **事件差分**: 09-25 ATM IV 87.7% vs 10-02 74.9%（差 +12.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-16 16C ΔOI +435（距现价 -2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-02 20C ΔOI +2,846 占该期限总 OI 12.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 16.78 → 今开 16.90（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 16.92 ｜ 低 16.26

Options: P/C成交量 0.82 | OI比 0.51 | ATM IV 87.7% | Skew -3.2pp | Term 0.86 | ExpMove ±7.3%（近端） | Rank 11%
量化视角： IV 历史低位（Rank 11%，期权偏便宜）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.82×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（3D）±7.3% ｜ 10-02（10D）±10.5% ｜ 10-09（17D）±12.8% ｜ 10-16（24D）±15.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,493,245 | GEX Change vs 上次快照 301,575 | Flip: Primary Flip: 15.57（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 237 / LOW 64 / INVALID 141
结构观察区: Primary Flip 15.57（全链重定价，覆盖 100%）
Put Wall 15（现价高于该位 9.0%）
最近结构参考: Flip 16（现价高于该位 5.0%）
量化视角： 正 Gamma（449万，无历史分位）｜正 Gamma 增强（+30万）｜现价位于 Flip 上方 5.02%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall）；上方 17（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 21.0C — Vol 4,983 | 最新价 $0.29 | OI 4628→9230 (ΔOI +4602张) | ΔOI/Volume 92.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4602张（+99.4% vs前日OI），连续性待观察（方向未知）
10-02 20.0C — Vol 3,836 | 最新价 $0.16 | OI 1044→3890 (ΔOI +2846张) | ΔOI/Volume 74.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2846张（+272.6% vs前日OI），连续性待观察（方向未知）
09-25 18.0C — Vol 4,618 | 最新价 $0.24 | OI 2319→4868 (ΔOI +2549张) | ΔOI/Volume 55.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2549张（+109.9% vs前日OI），连续性待观察（方向未知）
09-25 15.5P — Vol 2,868 | 最新价 $0.12 | OI 837→2828 (ΔOI +1991张) | ΔOI/Volume 69.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1991张（+237.9% vs前日OI），连续性待观察（方向未知）
09-25 19.0C — Vol 2,185 | 最新价 $0.09 | OI 1200→2633 (ΔOI +1433张) | ΔOI/Volume 65.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1433张（+119.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 13,421 张（Put 1,991 / Call 11,430），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +6.8k / P +3.8k ｜ Activity HIGH ｜ 3D
10-02  C +4.1k / P +0.8k ｜ Activity HIGH ｜ 10D
10-09  C +0.5k / P +4 ｜ Activity MEDIUM △ ｜ 17D
10-16  C +6.4k / P +0.2k ｜ Activity HIGH ｜ 24D

📆 09-25 Forward Structure
存量OI: C 27.0k / P 13.6k，今日变化ΔOI: C +6.8k / P +3.8k，平值价格ATM: C $0.51 / P $0.69 ｜ ATM IV 87.7%，净 delta 敞口 -57k shares
Top ΔOI: P 15 +1,991
仓位参考: Max Pain 17 ｜ Call Wall 17（+4.0%，弱）（OI 3.5k） ｜ Put Wall 15.5（-5.2%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 87.7%｜历史 Rank 11%（近端代理）｜IV/RV 1.62×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 56,564 股

📆 10-02 Forward Structure
存量OI: C 16.9k / P 6.0k，今日变化ΔOI: C +4.1k / P +0.8k，平值价格ATM: C $0.78 / P $0.94 ｜ ATM IV 74.9%，净 delta 敞口 28k shares
Top ΔOI: C 17 +185
仓位参考: Max Pain 17 ｜ Put Wall 17（+4.0%）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 74.9%｜历史 Rank 11%（近端代理）｜IV/RV 1.38×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 27,684 股

10-09（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 16（-2.1%）（OI 1.2k）

📆 10-16 Forward Structure
存量OI: C 35.5k / P 12.9k，今日变化ΔOI: C +6.4k / P +0.2k，平值价格ATM: C $1.30 / P $1.25 ｜ ATM IV 73.4%，净 delta 敞口 104k shares
Top ΔOI: C 21 +4,602 ｜ C 16 +435
仓位参考: Max Pain 17 ｜ Put Wall 15（-8.3%）（OI 5.3k）
量化解读： 存量 Call 重｜ATM IV 73.4%｜历史 Rank 11%（近端代理）｜IV/RV 1.36×（近似）｜净 delta 敞口 正 103,629 股

📅 事件差分（观察，非因果）: 09-25（3D）ATM IV 87.7% vs 10-02 74.9%（差 +12.8pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/USAR_morning.json