# 期权晨报 2026-10-01（快照 10:20 ET）

📊 市场环境

SPY $764.48 ｜ QQQ $742.03
VIX 17.57 ↑7.5%（5D +12.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-01

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 54.5 ｜ 前值 54.6　✅ 今日已公布
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 10-02 ATM IV 41.1% vs 10-05 28.9%（差 +12.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-02 57C ΔOI +2,856（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-07 71C ΔOI +6,250 占该期限总 OI 28.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 54.51 → 今开 55.11（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 55.23 ｜ 低 54.85

Options: P/C成交量 0.61 | OI比 0.45 | ATM IV 41.1% | Skew 3.7pp | Term 0.81 | ExpMove ±2.0%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价中性（Skew 3.7pp）｜存量 Call 偏重（OI比 0.45）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.45×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±2.0% ｜ 10-05（4D）±2.4% ｜ 10-07（6D）±3.3% ｜ 10-09（8D）±3.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 17,706,520 | GEX Change vs 上次快照 22,463,149 | Flip: Primary Flip: 54.30（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 720 / LOW 106 / INVALID 384
结构观察区: Primary Flip 54.30（全链重定价，覆盖 95%）
Put Wall 50（弱结构｜现价高于该位 9.8%） | Call Wall 60（弱结构｜现价低于该位 8.5%）
最近结构参考: Flip 54（现价高于该位 1.1%）
量化视角： 正 Gamma（1771万，无历史分位）｜由负转正（+2246万）｜现价位于 Flip 上方 1.14%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构）；上方 56（MaxPain，仅结算参考） / 60（Call Wall，弱结构）。
• Gamma 区域：切换参考 54（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 53.0P — Vol 10,432 | 最新价 $0.84 | OI 3452→13499 (ΔOI +10047张) | ΔOI/Volume 96.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10047张（+291.1% vs前日OI），连续性待观察（方向未知）
10-07 71.0C — Vol 6,255 | 最新价 $0.01 | OI 3→6253 (ΔOI +6250张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6250张（+208333.3% vs前日OI），连续性待观察（方向未知）
10-30 62.5C — Vol 4,168 | 最新价 $0.37 | OI 845→4848 (ΔOI +4003张) | ΔOI/Volume 96.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4003张（+473.7% vs前日OI），连续性待观察（方向未知）
10-30 60.5C — Vol 4,204 | 最新价 $0.58 | OI 535→4474 (ΔOI +3939张) | ΔOI/Volume 93.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3939张（+736.3% vs前日OI），连续性待观察（方向未知）
10-02 57.0C — Vol 4,439 | 最新价 $0.07 | OI 1901→4757 (ΔOI +2856张) | ΔOI/Volume 64.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2856张（+150.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 27,095 张（Put 10,047 / Call 17,048），跨 4 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +14.0k / P +1.1k ｜ Activity MEDIUM △ ｜ 1D
10-05  C +1.4k / P +0.5k ｜ Activity HIGH ｜ 4D
10-07  C +11.6k / P -82 ｜ Activity HIGH ｜ 6D
10-09  C +5.9k / P +0.9k ｜ Activity MEDIUM △ ｜ 8D

📆 10-02 Forward Structure
存量OI: C 104.2k / P 47.3k，今日变化ΔOI: C +14.0k / P +1.1k，平值价格ATM: C $0.65 / P $0.43 ｜ ATM IV 41.1%，净 delta 敞口 655k shares
Top ΔOI: C 57 +2,856 ｜ C 54 +2,389
仓位参考: Max Pain 56 ｜ Call Wall 60（+9.2%，弱）（OI 12.2k） ｜ Put Wall 50（-9.0%）（OI 7.4k）
量化解读： 存量 Call 重｜ATM IV 41.1%｜历史 Rank 69%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 654,559 股

📆 10-05 Forward Structure
存量OI: C 8.4k / P 6.5k，今日变化ΔOI: C +1.4k / P +0.5k，平值价格ATM: C $0.74 / P $0.59 ｜ ATM IV 28.9%，净 delta 敞口 42k shares
Top ΔOI: C 55 +451 ｜ C 54 +258
仓位参考: Max Pain 56 ｜ Call Wall 60（+9.2%）（OI 1.3k） ｜ Put Wall 52（-5.3%）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 28.9%｜历史 Rank 69%（近端代理）｜IV/RV 0.75×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 41,584 股

📆 10-07 Forward Structure
存量OI: C 16.7k / P 5.0k，今日变化ΔOI: C +11.6k / P -82，平值价格ATM: C $1.03 / P $0.78 ｜ ATM IV 30.7%，净 delta 敞口 127k shares
Top ΔOI: C 58 +2,718 ｜ C 59 +1,683
仓位参考: Max Pain 56 ｜ Call Wall 58（+5.6%，弱）（OI 2.9k） ｜ Put Wall 57（+3.8%）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 30.7%｜历史 Rank 69%（近端代理）｜IV/RV 0.79×（近似）｜净 delta 敞口 正 127,280 股

10-09（MEDIUM △）Top ΔOI: 59C +1,744 ｜ 59C +1,227
10-09（MEDIUM △）仓位参考: Max Pain 56 ｜ Call Wall 60（+9.2%，弱）（OI 4.2k） ｜ Put Wall 55（+0.1%，弱）（OI 2.8k）

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 41.1% vs 10-05 28.9%（差 +12.2pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/SLV_morning.json