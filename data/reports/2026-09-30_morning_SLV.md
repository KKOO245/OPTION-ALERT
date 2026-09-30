# 期权晨报 2026-09-30（快照 10:20 ET）

📊 市场环境

SPY $769.13 ｜ QQQ $743.48
VIX 15.68 ↓2.2%（5D +3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 55C ΔOI +823（距现价 +0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 55.48 → 今开 55.11（-0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 55.24 ｜ 低 54.89

Options: P/C成交量 1.09 | OI比 0.39 | ATM IV 40.8% | Skew 0.8pp | Term 0.86 | ExpMove ±2.6%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价薄（Skew 0.8pp）｜存量 Call 偏重（OI比 0.39）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.09×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.39×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（2D）±2.6% ｜ 10-05（5D）±3.1% ｜ 10-07（7D）±3.8% ｜ 10-09（9D）±4.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 10,207,754 | GEX Change vs 上次快照 -2,291,612 | Flip: Primary Flip: 54.76（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 751 / LOW 202 / INVALID 545
结构观察区: Primary Flip 54.76（全链重定价，覆盖 90%）
Put Wall 50（弱结构｜现价高于该位 10.0%） | Call Wall 60（弱结构｜现价低于该位 8.4%）
最近结构参考: Flip 55（现价高于该位 0.4%）
量化视角： 正 Gamma（1021万，无历史分位）｜正 Gamma 减弱（229万）｜现价位于 Flip 上方 0.42%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构） / 54（MaxPain，仅结算参考）；上方 60（Call Wall，弱结构）。
• Gamma 区域：切换参考 55（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-30 56.0C — Vol 8,162 | 最新价 $0.25 | OI 3026→6780 (ΔOI +3754张) | ΔOI/Volume 46.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3754张（+124.1% vs前日OI），连续性待观察（方向未知）
10-30 100.0C — Vol 1,847 | 最新价 $0.02 | OI 1125→2970 (ΔOI +1845张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1845张（+164.0% vs前日OI），连续性待观察（方向未知）
09-30 54.0P — Vol 3,667 | 最新价 $0.06 | OI 3853→5467 (ΔOI +1614张) | ΔOI/Volume 44.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1614张（+41.9% vs前日OI），连续性待观察（方向未知）
10-02 52.0P — Vol 2,932 | 最新价 $0.07 | OI 1698→3198 (ΔOI +1500张) | ΔOI/Volume 51.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1500张（+88.3% vs前日OI），连续性待观察（方向未知）
10-16 64.0C — Vol 2,024 | 最新价 $0.17 | OI 69139→70353 (ΔOI +1214张) | ΔOI/Volume 60.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1214张（+1.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,927 张（Put 3,114 / Call 6,813），跨 4 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 320.8k / P 125.6k，今日成交量: C 10.2k / P 11.2k，平值价格ATM: C $0.24 / P $0.24 ｜ ATM IV 40.8%，预期波动 ±0.9%，Max Pain 54
Top ΔOI: C 56 +3,754 ｜ P 54 +1,614 ｜ C 55 +869

📆 Forward Expiration Structure

10-02  C +4.2k / P +2.6k ｜ Activity HIGH ｜ 2D
10-05  C +2.3k / P +1.7k ｜ Activity HIGH ｜ 5D
10-07  C +1.0k / P +1.3k ｜ Activity HIGH ｜ 7D
10-09  C +2.4k / P +0.6k ｜ Activity MEDIUM △ ｜ 9D

📆 10-02 Forward Structure
存量OI: C 90.1k / P 46.2k，今日变化ΔOI: C +4.2k / P +2.6k，平值价格ATM: C $0.73 / P $0.72 ｜ ATM IV 40.8%，净 delta 敞口 218k shares
Top ΔOI: P 52 +1,500 ｜ C 55 +823 ｜ C 56 +798
仓位参考: Max Pain 58 ｜ Call Wall 60（+9.1%，弱）（OI 11.4k） ｜ Put Wall 50（-9.1%）（OI 7.4k）
量化解读： 存量 Call 重｜ATM IV 40.8%｜历史 Rank 68%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 217,757 股

📆 10-05 Forward Structure
存量OI: C 7.0k / P 6.0k，今日变化ΔOI: C +2.3k / P +1.7k，平值价格ATM: C $0.83 / P $0.88 ｜ ATM IV 31.9%，净 delta 敞口 8k shares
Top ΔOI: C 60 +1,019 ｜ P 52 +976 ｜ C 55 +359
仓位参考: Max Pain 57 ｜ Call Wall 60（+9.1%）（OI 1.3k） ｜ Put Wall 52（-5.4%）（OI 1.3k）
量化解读： 存量两侧均衡｜ATM IV 31.9%｜历史 Rank 68%（近端代理）｜IV/RV 0.83×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 7,599 股

📆 10-07 Forward Structure
存量OI: C 5.1k / P 5.1k，今日变化ΔOI: C +1.0k / P +1.3k，平值价格ATM: C $1.05 / P $1.02 ｜ ATM IV 33.5%，净 delta 敞口 -1k shares
Top ΔOI: P 53 +353 ｜ C 55 +300 ｜ P 51 +240
仓位参考: Max Pain 57 ｜ Call Wall 59（+7.3%，弱）（OI 0.8k） ｜ Put Wall 57（+3.7%）（OI 1.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 33.5%｜历史 Rank 68%（近端代理）｜IV/RV 0.87×（近似）｜净 delta 敞口 负 1,160 股

10-09（MEDIUM △）Top ΔOI: 52P -409 ｜ 56C +318
10-09（MEDIUM △）仓位参考: Max Pain 57 ｜ Call Wall 60（+9.1%，弱）（OI 4.1k） ｜ Put Wall 55（+0.0%，弱）（OI 2.7k）

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 40.8% vs 10-05 31.9%（差 +8.9pp）——覆盖 PCE 物价 Price Index MoM、Personal Spending MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/SLV_morning.json