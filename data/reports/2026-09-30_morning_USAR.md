# 期权晨报 2026-09-30（快照 10:20 ET）

📊 市场环境

SPY $769.13 ｜ QQQ $743.65
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
🟡 **近现价集中开仓**: 10-02 15C ΔOI +861（距现价 +2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 14.07 → 今开 14.10（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 14.75 ｜ 低 14.07

Options: P/C成交量 0.51 | OI比 0.47 | ATM IV 71.0% | Skew -8.2pp | Term 0.96 | ExpMove ±5.5%（近端） | Rank 4%
量化视角： IV 历史低位（Rank 4%，期权偏便宜）｜期限结构正常（Term 0.96）｜Put 保护异常便宜（Skew -8.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.47）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.47×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（2D）±5.5% ｜ 10-09（9D）±9.1% ｜ 10-16（16D）±11.7% ｜ 10-23（23D）±13.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,989,731 | GEX Change vs 上次快照 2,205,779 | Flip: Primary Flip: 15.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 215 / LOW 69 / INVALID 120
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 15.15（全链重定价，覆盖 100%）
Put Wall 15（弱结构｜现价低于该位 2.7%）
最近结构参考: Put Wall 15（现价低于该位 2.7%）
量化视角： 负 Gamma（199万，无历史分位）｜负 Gamma 缓解（+221万）｜现价位于 Flip 下方 3.68%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 15（Put Wall，弱结构） / 16（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 15（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 15.0C — Vol 1,328 | 最新价 $0.10 | OI 805→1666 (ΔOI +861张) | ΔOI/Volume 64.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增861张（+107.0% vs前日OI），连续性待观察（方向未知）
10-09 17.0C — Vol 869 | 最新价 $0.05 | OI 249→1025 (ΔOI +776张) | ΔOI/Volume 89.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增776张（+311.6% vs前日OI），连续性待观察（方向未知）
10-16 16.0C — Vol 933 | 最新价 $0.26 | OI 1052→1546 (ΔOI +494张) | ΔOI/Volume 53.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增494张（+47.0% vs前日OI），连续性待观察（方向未知）
10-23 15.0C — Vol 617 | 最新价 $0.65 | OI 71→561 (ΔOI +490张) | ΔOI/Volume 79.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增490张（+690.1% vs前日OI），连续性待观察（方向未知）
10-02 14.0C — Vol 611 | 最新价 $0.41 | OI 116→555 (ΔOI +439张) | ΔOI/Volume 71.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增439张（+378.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,060 张（Put 0 / Call 3,060），跨 4 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +1.4k / P -70 ｜ Activity HIGH ｜ 2D
10-09  C +1.6k / P +58 ｜ Activity HIGH ｜ 9D
10-16  C +1.1k / P +0.5k ｜ Activity HIGH ｜ 16D
10-23  C +0.5k / P +0.7k ｜ Activity HIGH ｜ 23D

📆 10-02 Forward Structure
存量OI: C 25.5k / P 12.0k，今日变化ΔOI: C +1.4k / P -70，平值价格ATM: C $0.18 / P $0.62 ｜ ATM IV 71.0%，净 delta 敞口 101k shares
Top ΔOI: C 15 +861 ｜ C 14 +439 ｜ P 14 +344
仓位参考: Max Pain 16 ｜ Call Wall 15（+2.8%，弱）（OI 1.7k） ｜ Put Wall 16（+9.7%）（OI 2.5k）
量化解读： 存量 Call 重｜ATM IV 71.0%｜历史 Rank 4%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 100,889 股

📆 10-09 Forward Structure
存量OI: C 9.3k / P 6.4k，今日变化ΔOI: C +1.6k / P +58，平值价格ATM: C $0.45 / P $0.87 ｜ ATM IV 66.5%，净 delta 敞口 45k shares
Top ΔOI: P 16 -281 ｜ C 15 +257
仓位参考: Max Pain 16 ｜ Call Wall 15（+2.8%，弱）（OI 0.6k） ｜ Put Wall 15.5（+6.2%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 66.5%｜历史 Rank 4%（近端代理）｜IV/RV 1.21×（近似）｜净 delta 敞口 正 45,045 股

📆 10-16 Forward Structure
存量OI: C 42.0k / P 15.9k，今日变化ΔOI: C +1.1k / P +0.5k，平值价格ATM: C $0.64 / P $1.07 ｜ ATM IV 67.2%，净 delta 敞口 18k shares
Top ΔOI: C 16 +494 ｜ P 16 +348 ｜ P 17 -320
仓位参考: Max Pain 17 ｜ Put Wall 15（+2.8%）（OI 5.6k）
量化解读： 存量 Call 重｜ATM IV 67.2%｜历史 Rank 4%（近端代理）｜IV/RV 1.22×（近似）｜净 delta 敞口 正 18,340 股

📆 10-23 Forward Structure
存量OI: C 9.7k / P 3.7k，今日变化ΔOI: C +0.5k / P +0.7k，平值价格ATM: C $0.84 / P $1.19 ｜ ATM IV 67.9%，净 delta 敞口 -20k shares
Top ΔOI: C 15 +490 ｜ P 17 +404
仓位参考: Max Pain 17 ｜ Put Wall 15（+2.8%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 67.9%｜历史 Rank 4%（近端代理）｜IV/RV 1.23×（近似）｜净 delta 敞口 负 19,917 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/USAR_morning.json