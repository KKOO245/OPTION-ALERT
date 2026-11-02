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
🔴 **事件差分**: 11-06（4D）ATM IV 109.6% vs 11-13 93.8%（差 +15.8pp），覆盖 ISM 制造业 PMI、Midterm Elections 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-06 1050P ΔOI +1,039（距现价 -2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,158.50 → 收盘 1,075.08（-7.2%） ｜ 今日高 1159.31 ｜ 低 1067.40 ｜ 昨收 1,150.89 → 收盘 1,075.08（-6.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-05，窗口结束前不做对错判定）

Options: P/C成交量 0.99 | OI比 0.83 | ATM IV 109.6% | Skew 9.2pp | Term 0.73 | ExpMove ±9.2%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜保护溢价显著（Skew 9.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.99×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（4D）±9.2% ｜ 11-13（11D）±12.8% ｜ 11-20（18D）±15.3% ｜ 11-27（25D）±17.4%
   ⇒ IV–VIX Spread: +88.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,626,745 | GEX Change vs 上次快照 -1,183,105 | Flip: Primary Flip: 1216.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1796 / LOW 406 / INVALID 954
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1216.35（全链重定价，覆盖 100%）
Put Wall 1,000（弱结构｜现价高于该位 7.5%）
最近结构参考: Put Wall 1000（现价高于该位 7.5%）
量化视角： 负 Gamma（463万，无历史分位）｜负 Gamma 加深（118万）｜现价位于 Flip 下方 11.61%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,000（Put Wall，弱结构）；上方 1,250（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1216（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 630.0P — Vol 1,320 | 最新价 $0.09 | OI 496→3024 (ΔOI +2528张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2528张（+509.7% vs前日OI），连续性待观察（方向未知）
11-27 1300.0C — Vol 109 | 最新价 $25.40 | OI 71→2153 (ΔOI +2082张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2082张（+2932.4% vs前日OI），连续性待观察（方向未知）
11-27 1270.0C — Vol 5 | 最新价 $31.74 | OI 22→2049 (ΔOI +2027张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2027张（+9213.6% vs前日OI），连续性待观察（方向未知）
11-27 1290.0C — Vol 5 | 最新价 $28.40 | OI 13→2021 (ΔOI +2008张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2008张（+15446.1% vs前日OI），连续性待观察（方向未知）
11-06 1050.0P — Vol 1,199 | 最新价 $38.03 | OI 236→1275 (ΔOI +1039张) | ΔOI/Volume 86.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1039张（+440.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,684 张（Put 3,567 / Call 6,117），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +11.0k / P +11.0k ｜ Activity HIGH ｜ 4D
11-13  C +2.7k / P +0.6k ｜ Activity HIGH ｜ 11D
11-20  C +4.4k / P +2.2k ｜ Activity HIGH ｜ 18D
11-27  C +7.0k / P +0.8k ｜ Activity HIGH ｜ 25D

📆 11-06 Forward Structure
存量OI: C 32.4k / P 26.9k，今日变化ΔOI: C +11.0k / P +11.0k，平值价格ATM: C $50.00 / P $49.09 ｜ ATM IV 109.6%，净 delta 敞口 -117k shares
Top ΔOI: P 1050 +1,039 ｜ C 1200 +912
仓位参考: Max Pain 1,250 ｜ Call Wall 1180（+9.8%，弱）（OI 0.4k） ｜ Put Wall 1000（-7.0%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 109.6%｜历史 Rank 68%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 116,691 股

📆 11-13 Forward Structure
存量OI: C 9.2k / P 8.5k，今日变化ΔOI: C +2.7k / P +0.6k，平值价格ATM: C $67.77 / P $69.83 ｜ ATM IV 93.8%，净 delta 敞口 -3k shares
Top ΔOI: P 630 -726 ｜ C 1220 +370 ｜ C 1500 +203
仓位参考: Max Pain 1,370 ｜ Put Wall 1100（+2.3%，弱）（OI 0.2k）
量化解读： 存量两侧均衡｜ATM IV 93.8%｜历史 Rank 68%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,148 股

📆 11-20 Forward Structure
存量OI: C 50.0k / P 54.0k，今日变化ΔOI: C +4.4k / P +2.2k，平值价格ATM: C $80.00 / P $84.64 ｜ ATM IV 88.7%，净 delta 敞口 42k shares
Top ΔOI: P 1150 +980 ｜ C 1600 +650 ｜ C 1800 +327
仓位参考: Max Pain 1,430 ｜ Call Wall 1000（-7.0%，弱）（OI 0.6k） ｜ Put Wall 1000（-7.0%）（OI 2.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 88.7%｜历史 Rank 68%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 41,864 股

📆 11-27 Forward Structure
存量OI: C 11.7k / P 7.7k，今日变化ΔOI: C +7.0k / P +0.8k，平值价格ATM: C $91.85 / P $95.00 ｜ ATM IV 83.6%，净 delta 敞口 122k shares
Top ΔOI: C 1300 +2,082 ｜ C 1270 +2,027 ｜ C 1290 +2,008
仓位参考: Max Pain 1,270 ｜ Put Wall 1150（+7.0%）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 83.6%｜历史 Rank 68%（近端代理）｜IV/RV 1.03×（近似）｜净 delta 敞口 正 122,180 股

📅 事件差分（观察，非因果）: 11-06（4D）ATM IV 109.6% vs 11-13 93.8%（差 +15.8pp）——覆盖 ISM 制造业 PMI、Midterm Elections 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/SNDK_evening.json