# 期权晨报 2026-09-28（快照 10:20 ET）

📊 市场环境

SPY $767.62 ｜ QQQ $737.33
VIX 15.89 ↑6.9%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.24 ｜ 实际 待公布 ｜ 前值 7.271
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 54.9 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 84 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 09-30 58C ΔOI +1,363（距现价 +5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 58.14 → 今开 55.32（-4.9%） | 较昨收变动（含盘初走势） ｜ 今日高 55.83 ｜ 低 55.28

Options: P/C成交量 0.65 | OI比 0.65 | ATM IV 41.4% | Skew 0.5pp | Term 0.86 | ExpMove ±2.3%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价薄（Skew 0.5pp）｜存量 Call 偏重（OI比 0.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.65×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-30（2D）±2.3% ｜ 10-02（4D）±3.2% ｜ 10-05（7D）±3.6% ｜ 10-07（9D）±4.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 10,932,851 | GEX Change vs 上次快照 -56,643,957 | Flip: Primary Flip: 55.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 678 / LOW 211 / INVALID 411
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 55.35（全链重定价，覆盖 95%）
Call Wall 60（弱结构｜现价低于该位 7.1%）
最近结构参考: Flip 55（现价高于该位 0.7%）
量化视角： 正 Gamma（1093万，无历史分位）｜正 Gamma 减弱（5664万）｜现价位于 Flip 上方 0.68%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 58（MaxPain，仅结算参考） / 60（Call Wall，弱结构）。
• Gamma 区域：切换参考 55（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-07 57.0P — Vol 5,303 | 最新价 $0.73 | OI 248→4494 (ΔOI +4246张) | ΔOI/Volume 80.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4246张（+1712.1% vs前日OI），连续性待观察（方向未知）
09-28 57.5P — Vol 3,192 | 最新价 $0.21 | OI 291→2201 (ΔOI +1910张) | ΔOI/Volume 59.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1910张（+656.4% vs前日OI），连续性待观察（方向未知）
09-28 60.0C — Vol 3,007 | 最新价 $0.05 | OI 1510→3318 (ΔOI +1808张) | ΔOI/Volume 60.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1808张（+119.7% vs前日OI），连续性待观察（方向未知）
09-28 58.5C — Vol 3,600 | 最新价 $0.29 | OI 1474→3023 (ΔOI +1549张) | ΔOI/Volume 43.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1549张（+105.1% vs前日OI），连续性待观察（方向未知）
09-30 61.0C — Vol 1,789 | 最新价 $0.10 | OI 1510→3042 (ΔOI +1532张) | ΔOI/Volume 85.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1532张（+101.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,045 张（Put 6,156 / Call 4,889），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 22.0k / P 14.3k，今日成交量: C 12.3k / P 7.9k，平值价格ATM: C $0.29 / P $0.21 ｜ ATM IV 41.4%，预期波动 ±0.9%，Max Pain 58
Top ΔOI: P 57 +1,910 ｜ C 60 +1,808 ｜ C 58 +1,549

📆 Forward Expiration Structure

09-30  C +5.6k / P -0.9k ｜ Activity HIGH ｜ 2D
10-02  C +4.4k / P +4.3k ｜ Activity HIGH ｜ 4D
10-05  C +1.1k / P +0.4k ｜ Activity HIGH ｜ 7D
10-07  C +0.9k / P +4.7k ｜ Activity HIGH ｜ 9D

📆 09-30 Forward Structure
存量OI: C 300.0k / P 127.0k，今日变化ΔOI: C +5.6k / P -0.9k，平值价格ATM: C $0.68 / P $0.58 ｜ ATM IV 36.0%，净 delta 敞口 103k shares
Top ΔOI: C 61 +1,532 ｜ C 58 +1,363
仓位参考: Max Pain 56 ｜ Call Wall 60（+7.7%，弱）（OI 6.6k） ｜ Put Wall 53（-4.9%）（OI 13.2k）
量化解读： 存量 Call 重｜ATM IV 36.0%｜历史 Rank 69%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 102,734 股

📆 10-02 Forward Structure
存量OI: C 80.3k / P 39.2k，今日变化ΔOI: C +4.4k / P +4.3k，平值价格ATM: C $0.96 / P $0.80 ｜ ATM IV 38.1%，净 delta 敞口 -205k shares
Top ΔOI: P 59 +586
仓位参考: Max Pain 58 ｜ Call Wall 60（+7.7%，弱）（OI 12.3k） ｜ Put Wall 56（+0.5%，弱）（OI 4.1k）
量化解读： 存量 Call 重｜ATM IV 38.1%｜历史 Rank 69%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 204,986 股

📆 10-05 Forward Structure
存量OI: C 2.7k / P 2.5k，今日变化ΔOI: C +1.1k / P +0.4k，平值价格ATM: C $1.17 / P $0.86 ｜ ATM IV 32.9%，净 delta 敞口 -9k shares
Top ΔOI: P 53 +146 ｜ C 59 +141
仓位参考: Max Pain 60 ｜ Call Wall 61（+9.5%，弱）（OI 0.3k） ｜ Put Wall 59.5（+6.8%）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 32.9%｜历史 Rank 69%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 负 9,234 股

📆 10-07 Forward Structure
存量OI: C 2.2k / P 5.7k，今日变化ΔOI: C +0.9k / P +4.7k，平值价格ATM: C $1.30 / P $1.05 ｜ ATM IV 34.4%，净 delta 敞口 -291k shares
Top ΔOI: P 57 +4,246 ｜ C 57 +176
仓位参考: Max Pain 58 ｜ Call Wall 60（+7.7%）（OI 0.6k） ｜ Put Wall 57（+2.3%）（OI 4.5k）
量化解读： 存量 Put 重｜ATM IV 34.4%｜历史 Rank 69%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 负 290,981 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/SLV_morning.json