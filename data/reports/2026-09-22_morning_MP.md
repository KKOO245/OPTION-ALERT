# 期权晨报 2026-09-22（快照 10:20 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $nan
VIX 14.54 ↓2.2%（5D -15.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 09-25 ATM IV 70.1% vs 10-02 55.3%（差 +14.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-25 47P ΔOI +817（距现价 -3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 50.00 → 今开 50.68（+1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 50.83 ｜ 低 48.67

Options: P/C成交量 1.19 | OI比 0.78 | ATM IV 70.1% | Skew -9.7pp | Term 0.87 | ExpMove ±5.2%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜Put 保护异常便宜（Skew -9.7pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.78）+ 当日成交偏 Put（P/C量 1.19）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.19×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（3D）±5.2% ｜ 10-02（10D）±7.4% ｜ 10-09（17D）±11.0% ｜ 10-16（24D）±12.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 466,490 | GEX Change vs 上次快照 678,313 | Flip: Primary Flip: 48.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 281 / LOW 60 / INVALID 143
结构观察区: Primary Flip 48.61（全链重定价，覆盖 95%）
最近结构参考: Flip 49（现价高于该位 0.6%）
量化视角： 正 Gamma（47万，无历史分位）｜由负转正（+68万）｜现价位于 Flip 上方 0.62%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 50（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 49（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 57.0C — Vol 1,649 | 最新价 $0.43 | OI 60→1684 (ΔOI +1624张) | ΔOI/Volume 98.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1624张（+2706.7% vs前日OI），连续性待观察（方向未知）
09-25 55.0C — Vol 1,673 | 最新价 $0.26 | OI 922→1856 (ΔOI +934张) | ΔOI/Volume 55.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增934张（+101.3% vs前日OI），连续性待观察（方向未知）
09-25 53.0C — Vol 1,236 | 最新价 $0.51 | OI 268→1124 (ΔOI +856张) | ΔOI/Volume 69.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增856张（+319.4% vs前日OI），连续性待观察（方向未知）
09-25 47.0P — Vol 1,165 | 最新价 $0.30 | OI 549→1366 (ΔOI +817张) | ΔOI/Volume 70.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增817张（+148.8% vs前日OI），连续性待观察（方向未知）
10-16 51.0C — Vol 595 | 最新价 $2.70 | OI 0→556 (ΔOI +556张) | ΔOI/Volume 93.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增556张（前日OI缺失），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,787 张（Put 817 / Call 3,970），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +3.3k / P +1.1k ｜ Activity HIGH ｜ 3D
10-02  C +2.4k / P +0.2k ｜ Activity HIGH ｜ 10D
10-09  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 17D
10-16  C +1.9k / P +0.2k ｜ Activity MEDIUM △ ｜ 24D

📆 09-25 Forward Structure
存量OI: C 13.8k / P 10.8k，今日变化ΔOI: C +3.3k / P +1.1k，平值价格ATM: C $1.12 / P $1.40 ｜ ATM IV 70.1%，净 delta 敞口 39k shares
Top ΔOI: C 53 +856 ｜ P 47 +817
仓位参考: Max Pain 50 ｜ Call Wall 52（+6.3%，弱）（OI 1.5k） ｜ Put Wall 47（-3.9%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 70.1%｜历史 Rank 54%（近端代理）｜IV/RV 1.72×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 39,186 股

📆 10-02 Forward Structure
存量OI: C 7.8k / P 4.2k，今日变化ΔOI: C +2.4k / P +0.2k，平值价格ATM: C $2.12 / P $1.49 ｜ ATM IV 55.3%，净 delta 敞口 30k shares
Top ΔOI: C 57 +1,624 ｜ C 52 +191 ｜ C 51 +131
仓位参考: Max Pain 50 ｜ Call Wall 49（+0.2%，弱）（OI 1.2k） ｜ Put Wall 50（+2.2%）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 55.3%｜历史 Rank 54%（近端代理）｜IV/RV 1.35×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 30,190 股

10-09（MEDIUM △）Top ΔOI: 49P +59
10-09（MEDIUM △）仓位参考: Max Pain 52 ｜ Put Wall 47（-3.9%）（OI 1.1k）

10-16（MEDIUM △）Top ΔOI: 51C +556 ｜ 50C +334
10-16（MEDIUM △）仓位参考: Max Pain 55 ｜ Call Wall 50（+2.2%，弱）（OI 2.8k） ｜ Put Wall 45（-8.0%，弱）（OI 3.1k）

📅 事件差分（观察，非因果）: 09-25（3D）ATM IV 70.1% vs 10-02 55.3%（差 +14.8pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/MP_morning.json