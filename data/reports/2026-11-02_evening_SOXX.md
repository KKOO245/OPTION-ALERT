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
🟡 **事件差分**: 11-06 ATM IV 71.9% vs 11-13 58.7%（差 +13.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-06 460P ΔOI -1,543（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 476.58 → 收盘 453.65（-4.8%） ｜ 今日高 479.92 ｜ 低 452.20 ｜ 昨收 471.51 → 收盘 453.65（-3.8%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-05，窗口结束前不做对错判定）

Options: P/C成交量 1.67 | OI比 1.36 | ATM IV 71.9% | Skew 9.6pp | Term 0.70 | ExpMove ±6.1%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价显著（Skew 9.6pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.67）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.67×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.36×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（4D）±6.1% ｜ 11-13（11D）±3.0% ｜ 11-20（18D）±10.2% ｜ 11-27（25D）±11.2%
   ⇒ IV–VIX Spread: +50.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -16,877,419 | GEX Change vs 上次快照 -4,762,204 | Flip: Primary Flip: 487.21（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 580 / LOW 215 / INVALID 757
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 487.21（全链重定价，覆盖 99%）
最近结构参考: Flip 487（现价低于该位 6.9%）
量化视角： 负 Gamma（1688万，无历史分位）｜负 Gamma 加深（476万）｜现价位于 Flip 下方 6.89%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 495（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 487（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 360.0P — Vol 32 | 最新价 $0.05 | OI 93→38104 (ΔOI +38011张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增38011张（+40872.0% vs前日OI），连续性待观察（方向未知）
11-20 500.0C — Vol 903 | 最新价 $6.15 | OI 1426→9557 (ΔOI +8131张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8131张（+570.2% vs前日OI），连续性待观察（方向未知）
11-20 425.0P — Vol 118 | 最新价 $11.23 | OI 222→2063 (ΔOI +1841张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1841张（+829.3% vs前日OI），连续性待观察（方向未知）
11-06 350.0P — Vol 10 | 最新价 $0.10 | OI 0→1470 (ΔOI +1470张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增1470张（前日OI缺失），值得跟踪（方向未知）
11-20 440.0P — Vol 1,782 | 最新价 $16.00 | OI 1828→3222 (ΔOI +1394张) | ΔOI/Volume 78.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1394张（+76.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 50,847 张（Put 42,716 / Call 8,131），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +4.1k / P +38.7k ｜ Activity HIGH ｜ 4D
11-13  C +1.0k / P +1.0k ｜ Activity HIGH ｜ 11D
11-20  C +9.1k / P +6.6k ｜ Activity HIGH ｜ 18D
11-27  C +0.2k / P +0.6k ｜ Activity MEDIUM △ ｜ 25D

📆 11-06 Forward Structure
存量OI: C 42.6k / P 58.0k，今日变化ΔOI: C +4.1k / P +38.7k，平值价格ATM: C $15.00 / P $12.60 ｜ ATM IV 71.9%，净 delta 敞口 212k shares
Top ΔOI: P 360 +38,011 ｜ P 492 -1,664 ｜ P 460 -1,543
仓位参考: Max Pain 495
量化解读： 存量 Put 重｜ATM IV 71.9%｜历史 Rank 97%（近端代理）｜IV/RV 1.42×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 212,071 股

📆 11-13 Forward Structure
存量OI: C 25.7k / P 8.9k，今日变化ΔOI: C +1.0k / P +1.0k，平值价格ATM: C $0.00 / P $13.60 ｜ ATM IV 58.7%，净 delta 敞口 -5k shares
Top ΔOI: C 480 +522 ｜ P 415 +468 ｜ P 420 +212
仓位参考: Max Pain 500 ｜ Put Wall 460（+1.4%）（OI 3.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 58.7%｜历史 Rank 97%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 4,943 股

📆 11-20 Forward Structure
存量OI: C 50.8k / P 75.9k，今日变化ΔOI: C +9.1k / P +6.6k，平值价格ATM: C $23.60 / P $22.80 ｜ ATM IV 56.0%，净 delta 敞口 82k shares
Top ΔOI: C 500 +8,131 ｜ P 425 +1,841 ｜ P 440 +1,394
仓位参考: Max Pain 510 ｜ Put Wall 460（+1.4%，弱）（OI 7.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 56.0%｜历史 Rank 97%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 81,630 股

11-27（MEDIUM △）Top ΔOI: 425P +92 ｜ 495P +92
11-27（MEDIUM △）仓位参考: Max Pain 500

📅 事件差分（观察，非因果）: 11-06（4D）ATM IV 71.9% vs 11-13 58.7%（差 +13.3pp）——覆盖 ISM 制造业 PMI、Midterm Elections 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/SOXX_evening.json