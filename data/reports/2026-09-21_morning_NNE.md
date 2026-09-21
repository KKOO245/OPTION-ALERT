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
🟡 **近现价集中开仓**: 10-02 17C ΔOI +136（距现价 +0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 15.73 → 今开 16.56（+5.3%） | 较昨收变动（含盘初走势） ｜ 今日高 17.18 ｜ 低 16.35

Options: P/C成交量 1.24 | OI比 0.52 | ATM IV 82.6% | Skew 4.6pp | Term 0.94 | ExpMove ±11.0%（近端） | Rank 10%
量化视角： IV 历史低位（Rank 10%，期权偏便宜）｜期限结构正常（Term 0.94）｜保护溢价中性（Skew 4.6pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.52）+ 当日成交偏 Put（P/C量 1.24）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.24×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.52×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（4D）±11.0% ｜ 10-02（11D）±10.0% ｜ 10-09（18D）±14.4% ｜ 10-16（25D）±18.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,711,729 | GEX Change vs 上次快照 1,058,888 | Flip: Primary Flip: 15.40（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 196 / LOW 79 / INVALID 181
结构观察区: Primary Flip 15.40（全链重定价，覆盖 97%）
最近结构参考: Flip 15（现价高于该位 10.2%）
量化视角： 正 Gamma（171万，无历史分位）｜正 Gamma 增强（+106万）｜现价位于 Flip 上方 10.15%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 17（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 15（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 14.5P — Vol 450 | 最新价 $0.20 | OI 139→576 (ΔOI +437张) | ΔOI/Volume 97.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增437张（+314.4% vs前日OI），连续性待观察（方向未知）
09-25 16.0C — Vol 362 | 最新价 $0.52 | OI 30→351 (ΔOI +321张) | ΔOI/Volume 88.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增321张（+1070.0% vs前日OI），连续性待观察（方向未知）
10-02 17.0C — Vol 155 | 最新价 $0.40 | OI 21→157 (ΔOI +136张) | ΔOI/Volume 87.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增136张（+647.6% vs前日OI），连续性待观察（方向未知）
09-25 16.0P — Vol 129 | 最新价 $0.90 | OI 103→210 (ΔOI +107张) | ΔOI/Volume 83.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增107张（+103.9% vs前日OI），连续性待观察（方向未知）
10-02 26.0P — Vol 88 | 最新价 $10.24 | OI 4→92 (ΔOI +88张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增88张（+2200.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,089 张（Put 632 / Call 457），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +0.6k / P +0.7k ｜ Activity HIGH ｜ 4D
10-02  C +0.3k / P +0.2k ｜ Activity HIGH ｜ 11D
10-09  C +45 / P +0.1k ｜ Activity HIGH ｜ 18D
10-16  C -0.7k / P +33 ｜ Activity HIGH ｜ 25D

📆 09-25 Forward Structure
存量OI: C 6.1k / P 3.2k，今日变化ΔOI: C +0.6k / P +0.7k，平值价格ATM: C $0.21 / P $1.66 ｜ ATM IV 82.6%，净 delta 敞口 4k shares
Top ΔOI: C 16 +321 ｜ P 16 +107
仓位参考: Max Pain 17 ｜ Put Wall 15.5（-8.6%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 82.6%｜历史 Rank 10%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,885 股

📆 10-02 Forward Structure
存量OI: C 3.1k / P 1.2k，今日变化ΔOI: C +0.3k / P +0.2k，平值价格ATM: C $0.40 / P $1.30 ｜ ATM IV 74.4%，净 delta 敞口 -1k shares
Top ΔOI: C 17 +136 ｜ P 26 +88
仓位参考: Max Pain 18 ｜ Put Wall 18.5（+9.1%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 74.4%｜历史 Rank 10%（近端代理）｜IV/RV 1.03×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,246 股

📆 10-09 Forward Structure
存量OI: C 4.2k / P 0.5k，今日变化ΔOI: C +45 / P +0.1k，平值价格ATM: C $0.59 / P $1.85 ｜ ATM IV 76.0%，净 delta 敞口 -4k shares
Top ΔOI: P 17 +50 ｜ C 17 +23 ｜ C 18 +21
仓位参考: Max Pain 18 ｜ Put Wall 16（-5.7%）（OI 0.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 76.0%｜历史 Rank 10%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 负 4,449 股

📆 10-16 Forward Structure
存量OI: C 18.9k / P 6.1k，今日变化ΔOI: C -0.7k / P +33，平值价格ATM: C $0.75 / P $2.30 ｜ ATM IV 78.5%，净 delta 敞口 -23k shares
Top ΔOI: C 18 -798 ｜ C 17 +43
仓位参考: Max Pain 20 ｜ Put Wall 17（+0.2%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 78.5%｜历史 Rank 10%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 负 22,578 股

📅 事件差分（观察，非因果）: 09-25（4D）ATM IV 82.6% vs 10-02 74.4%（差 +8.2pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/NNE_morning.json