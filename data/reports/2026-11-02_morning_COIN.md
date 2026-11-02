# 期权晨报 2026-11-02（快照 10:20 ET）

📊 市场环境

SPY $753.20 ｜ QQQ $681.09
VIX 18.83 ↓3.0%（5D +2.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 22.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 11-02 10:00　【高】ISM 制造业 PMI　预测 54.6 ｜ 实际 55.5 ｜ 前值 54.5　✅ 今日已公布
- 周一 11-02 19:00　【高】Midterm Elections　实际 待公布　⏰ 今日
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.13 ｜ 实际 待公布 ｜ 前值 7.079
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48.2 ｜ 实际 待公布 ｜ 前值 48

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 11-06 ATM IV 90.2% vs 11-13 76.5%（差 +13.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-06 142C ΔOI +8,042（距现价 +0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 143.54 → 今开 140.49（-2.1%） | 较昨收变动（含盘初走势） ｜ 今日高 143.77 ｜ 低 139.11

Options: P/C成交量 0.55 | OI比 0.73 | ATM IV 90.2% | Skew 4.2pp | Term 0.76 | ExpMove ±7.9%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价中性（Skew 4.2pp）｜存量 Call 偏重（OI比 0.73）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（4D）±7.9% ｜ 11-13（11D）±10.6% ｜ 11-20（18D）±13.0% ｜ 11-27（25D）±15.1%
   ⇒ IV–VIX Spread: +71.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 10,394,273 | GEX Change vs 上次快照 15,177,687 | Flip: Primary Flip: 131.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 447 / LOW 145 / INVALID 258
结构观察区: Primary Flip 131.05（全链重定价，覆盖 100%）
最近结构参考: Flip 131（现价高于该位 7.4%）
量化视角： 正 Gamma（1039万，无历史分位）｜由负转正（+1518万）｜现价位于 Flip 上方 7.44%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 141（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 131（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 148.0C — Vol 8,308 | 最新价 $4.15 | OI 1→8235 (ΔOI +8234张) | ΔOI/Volume 99.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8234张（+823400.0% vs前日OI），连续性待观察（方向未知）
11-06 142.0C — Vol 8,364 | 最新价 $7.00 | OI 1→8043 (ΔOI +8042张) | ΔOI/Volume 96.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8042张（+804200.0% vs前日OI），连续性待观察（方向未知）
11-06 143.0C — Vol 8,162 | 最新价 $6.55 | OI 0→7963 (ΔOI +7963张) | ΔOI/Volume 97.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7963张（前日OI缺失），连续性待观察（方向未知）
11-06 149.0C — Vol 7,692 | 最新价 $3.15 | OI 32→7666 (ΔOI +7634张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7634张（+23856.2% vs前日OI），连续性待观察（方向未知）
11-06 141.0C — Vol 6,301 | 最新价 $7.35 | OI 2→6171 (ΔOI +6169张) | ΔOI/Volume 97.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6169张（+308450.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 38,042 张（Put 0 / Call 38,042），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +48.5k / P +23.9k ｜ Activity HIGH ｜ 4D
11-13  C +2.0k / P +6.5k ｜ Activity HIGH ｜ 11D
11-20  C +2.7k / P +1.6k ｜ Activity MEDIUM △ ｜ 18D
11-27  C +0.3k / P +1.3k ｜ Activity HIGH ｜ 25D

📆 11-06 Forward Structure
存量OI: C 62.7k / P 45.9k，今日变化ΔOI: C +48.5k / P +23.9k，平值价格ATM: C $5.40 / P $5.75 ｜ ATM IV 90.2%，净 delta 敞口 1.7M shares
Top ΔOI: C 148 +8,234 ｜ C 142 +8,042 ｜ C 143 +7,963
仓位参考: Max Pain 141 ｜ Call Wall 148（+5.1%，弱）（OI 8.2k）
量化解读： 存量 Call 重｜ATM IV 90.2%｜历史 Rank 80%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,679,413 股

📆 11-13 Forward Structure
存量OI: C 10.4k / P 17.8k，今日变化ΔOI: C +2.0k / P +6.5k，平值价格ATM: C $7.12 / P $7.80 ｜ ATM IV 76.5%，净 delta 敞口 -37k shares
Top ΔOI: P 90 +1,727 ｜ P 155 +983
仓位参考: Max Pain 162 ｜ Call Wall 150（+6.5%，弱）（OI 0.5k） ｜ Put Wall 130（-7.7%，弱）（OI 1.0k）
量化解读： 存量 Put 重｜ATM IV 76.5%｜历史 Rank 80%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 37,328 股

11-20（MEDIUM △）Top ΔOI: 80P +1,541 ｜ 140C +719
11-20（MEDIUM △）仓位参考: Max Pain 170 ｜ Put Wall 150（+6.5%，弱）（OI 3.3k）

📆 11-27 Forward Structure
存量OI: C 3.0k / P 3.3k，今日变化ΔOI: C +0.3k / P +1.3k，平值价格ATM: C $11.54 / P $9.65 ｜ ATM IV 68.4%，净 delta 敞口 -9k shares
Top ΔOI: P 110 +386 ｜ P 120 +281
仓位参考: Max Pain 160 ｜ Call Wall 150（+6.5%，弱）（OI 0.1k） ｜ Put Wall 140（-0.6%，弱）（OI 0.3k）
量化解读： 存量两侧均衡｜ATM IV 68.4%｜历史 Rank 80%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 负 8,623 股

📅 事件差分（观察，非因果）: 11-06（4D）ATM IV 90.2% vs 11-13 76.5%（差 +13.7pp）——覆盖 ISM 制造业 PMI、Midterm Elections 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/COIN_morning.json