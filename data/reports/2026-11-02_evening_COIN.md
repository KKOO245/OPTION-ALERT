# 期权晚报 2026-11-02（快照 16:40 ET）

📊 市场环境

SPY $752.10 ｜ QQQ $681.09
VIX 21.15 ↑8.9%（5D +15.0%） ｜ Vol Regime: ELEVATED
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
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **事件差分**: 11-06 ATM IV 93.3% vs 11-13 79.3%（差 +13.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-06 142C ΔOI +8,042（距现价 +3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 140.49 → 收盘 137.83（-1.9%） ｜ 今日高 143.77 ｜ 低 135.47 ｜ 昨收 143.54 → 收盘 137.83（-4.0%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-11-05，窗口结束前不做对错判定）

Options: P/C成交量 0.92 | OI比 0.73 | ATM IV 93.3% | Skew 9.4pp | Term 0.74 | ExpMove ±8.1%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价显著（Skew 9.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.73）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.92×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（4D）±8.1% ｜ 11-13（11D）±10.8% ｜ 11-20（18D）±14.1% ｜ 11-27（25D）±13.7%
   ⇒ IV–VIX Spread: +72.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 7,863,551 | GEX Change vs 上次快照 -2,530,722 | Flip: Primary Flip: 130.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 424 / LOW 149 / INVALID 277
结构观察区: Primary Flip 130.68（全链重定价，覆盖 100%）
最近结构参考: Flip 131（现价高于该位 5.5%）
量化视角： 正 Gamma（786万，无历史分位）｜正 Gamma 减弱（253万）｜现价位于 Flip 上方 5.47%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 141（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 131（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 148.0C — Vol 448 | 最新价 $1.80 | OI 1→8235 (ΔOI +8234张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8234张（+823400.0% vs前日OI），连续性待观察（方向未知）
11-06 142.0C — Vol 887 | 最新价 $3.60 | OI 1→8043 (ΔOI +8042张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8042张（+804200.0% vs前日OI），连续性待观察（方向未知）
11-06 143.0C — Vol 740 | 最新价 $3.24 | OI 0→7963 (ΔOI +7963张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增7963张（前日OI缺失），值得跟踪（方向未知）
11-06 149.0C — Vol 474 | 最新价 $1.56 | OI 32→7666 (ΔOI +7634张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7634张（+23856.2% vs前日OI），连续性待观察（方向未知）
11-06 141.0C — Vol 577 | 最新价 $3.86 | OI 2→6171 (ΔOI +6169张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6169张（+308450.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 38,042 张（Put 0 / Call 38,042），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +48.5k / P +23.9k ｜ Activity HIGH ｜ 4D
11-13  C +2.0k / P +6.5k ｜ Activity HIGH ｜ 11D
11-20  C +2.7k / P +1.6k ｜ Activity HIGH ｜ 18D
11-27  C +0.3k / P +1.3k ｜ Activity HIGH ｜ 25D

📆 11-06 Forward Structure
存量OI: C 62.7k / P 45.9k，今日变化ΔOI: C +48.5k / P +23.9k，平值价格ATM: C $5.31 / P $5.80 ｜ ATM IV 93.3%，净 delta 敞口 1.2M shares
Top ΔOI: C 148 +8,234 ｜ C 142 +8,042 ｜ C 143 +7,963
仓位参考: Max Pain 141 ｜ Call Wall 148（+7.4%，弱）（OI 8.2k）
量化解读： 存量 Call 重｜ATM IV 93.3%｜历史 Rank 83%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,188,775 股

📆 11-13 Forward Structure
存量OI: C 10.4k / P 17.8k，今日变化ΔOI: C +2.0k / P +6.5k，平值价格ATM: C $7.25 / P $7.64 ｜ ATM IV 79.3%，净 delta 敞口 -60k shares
Top ΔOI: P 155 +983
仓位参考: Max Pain 162 ｜ Call Wall 150（+8.8%，弱）（OI 0.5k） ｜ Put Wall 130（-5.7%，弱）（OI 1.0k）
量化解读： 存量 Put 重｜ATM IV 79.3%｜历史 Rank 83%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 60,188 股

📆 11-20 Forward Structure
存量OI: C 72.8k / P 50.8k，今日变化ΔOI: C +2.7k / P +1.6k，平值价格ATM: C $8.52 / P $10.95 ｜ ATM IV 75.4%，净 delta 敞口 124k shares
Top ΔOI: C 140 +719
仓位参考: Max Pain 170 ｜ Put Wall 150（+8.8%，弱）（OI 3.3k）
量化解读： 存量 Call 重｜ATM IV 75.4%｜历史 Rank 83%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 124,432 股

📆 11-27 Forward Structure
存量OI: C 3.0k / P 3.3k，今日变化ΔOI: C +0.3k / P +1.3k，平值价格ATM: C $6.40 / P $12.50 ｜ ATM IV 74.5%，净 delta 敞口 -15k shares
Top ΔOI: P 110 +386 ｜ P 120 +281
仓位参考: Max Pain 160 ｜ Call Wall 150（+8.8%，弱）（OI 0.1k） ｜ Put Wall 125（-9.3%，弱）（OI 0.3k）
量化解读： 存量两侧均衡｜ATM IV 74.5%｜历史 Rank 83%（近端代理）｜IV/RV 1.21×（近似）｜净 delta 敞口 负 15,202 股

📅 事件差分（观察，非因果）: 11-06（4D）ATM IV 93.3% vs 11-13 79.3%（差 +13.9pp）——覆盖 ISM 制造业 PMI、Midterm Elections 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/COIN_evening.json