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
🟡 **近现价集中开仓**: 11-03 680P ΔOI -7,899（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 695.32 → 收盘 681.09（-2.0%） ｜ 今日高 699.43 ｜ 低 680.33 ｜ 昨收 690.49 → 收盘 681.09（-1.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-05，窗口结束前不做对错判定）

Options: P/C成交量 1.06 | OI比 1.19 | ATM IV 75.0% | Skew 8.6pp | Term 0.36 | ExpMove ±1.6%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.36，近月 IV 高于远月）｜保护溢价显著（Skew 8.6pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.06×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.19×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 12% ｜ P/C OI(近端) 14%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 12%）｜近端持仓结构中性（P/C OI 分位 14%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-03（1D）±1.6% ｜ 11-04（2D）±2.5% ｜ 11-05（3D）±2.9% ｜ 11-06（4D）±3.3%
   ⇒ IV–VIX Spread: +53.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -728,678,874 | GEX Change vs 上次快照 -156,342,242 | Flip: Primary Flip: 721.16（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 2542 / LOW 191 / INVALID 1271
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 721.16（全链重定价，覆盖 96%）
Put Wall 680（弱结构｜现价高于该位 0.2%）
最近结构参考: Put Wall 680（现价高于该位 0.2%）
量化视角： 负 Gamma（7.29亿，历史分位偏负区，比 88% 的交易日更负）｜负 Gamma 加深（1.56亿）｜现价位于 Flip 下方 5.56%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 680（Put Wall，弱结构）；上方 695（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 721（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 650.0P — Vol 6,802 | 最新价 $5.15 | OI 4727→40889 (ΔOI +36162张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增36162张（+765.0% vs前日OI），连续性待观察（方向未知）
11-13 685.0P — Vol 4,437 | 最新价 $15.29 | OI 3274→39240 (ΔOI +35966张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增35966张（+1098.5% vs前日OI），连续性待观察（方向未知）
11-06 480.0P — Vol 856 | 最新价 $0.03 | OI 350→20534 (ΔOI +20184张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20184张（+5766.9% vs前日OI），连续性待观察（方向未知）
量化视角： 3 个事件合计 ΔOI ≈ 92,312 张（Put 92,312 / Call 0），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $74M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-03  C +39.0k / P +20.6k ｜ Activity HIGH ｜ 1D
11-04  C +29.6k / P +40.1k ｜ Activity HIGH ｜ 2D
11-05  C +12.0k / P +3.8k ｜ Activity HIGH ｜ 3D
11-06  C +82.0k / P +68.0k ｜ Activity HIGH ｜ 4D

📆 11-03 Forward Structure
存量OI: C 68.7k / P 112.1k，今日变化ΔOI: C +39.0k / P +20.6k，平值价格ATM: C $6.50 / P $4.20 ｜ ATM IV 37.0%，净 delta 敞口 77k shares
Top ΔOI: P 680 -7,899 ｜ C 700 +3,930 ｜ C 697 +3,079
仓位参考: Max Pain 697 ｜ Call Wall 700（+2.8%，弱）（OI 4.0k） ｜ Put Wall 680（-0.2%，弱）（OI 9.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 37.0%｜历史 Rank 100%（近端代理）｜IV/RV 1.65×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 77,226 股

📆 11-04 Forward Structure
存量OI: C 52.2k / P 78.3k，今日变化ΔOI: C +29.6k / P +40.1k，平值价格ATM: C $9.69 / P $7.26 ｜ ATM IV 41.2%，净 delta 敞口 -436k shares
Top ΔOI: P 680 +5,651 ｜ P 670 +3,281 ｜ P 685 +2,937
仓位参考: Max Pain 700 ｜ Call Wall 690（+1.3%，弱）（OI 2.2k） ｜ Put Wall 680（-0.2%）（OI 6.3k）
量化解读： 存量 Put 重｜ATM IV 41.2%｜历史 Rank 100%（近端代理）｜IV/RV 1.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 435,694 股

📆 11-05 Forward Structure
存量OI: C 26.5k / P 18.6k，今日变化ΔOI: C +12.0k / P +3.8k，平值价格ATM: C $11.59 / P $8.27 ｜ ATM IV 39.7%，净 delta 敞口 81k shares
Top ΔOI: C 720 +2,746 ｜ P 650 +2,670 ｜ C 745 +1,670
仓位参考: Max Pain 700 ｜ Call Wall 700（+2.8%，弱）（OI 2.4k） ｜ Put Wall 685（+0.6%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 39.7%｜历史 Rank 100%（近端代理）｜IV/RV 1.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 81,346 股

📆 11-06 Forward Structure
存量OI: C 293.6k / P 467.8k，今日变化ΔOI: C +82.0k / P +68.0k，平值价格ATM: C $12.53 / P $9.86 ｜ ATM IV 39.1%，净 delta 敞口 709k shares
Top ΔOI: P 480 +20,184 ｜ C 700 +12,426 ｜ P 680 +9,179
仓位参考: Max Pain 714 ｜ Call Wall 700（+2.8%，弱）（OI 13.5k） ｜ Put Wall 675（-0.9%，弱）（OI 44.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 39.1%｜历史 Rank 100%（近端代理）｜IV/RV 1.75×（近似）｜净 delta 敞口 正 708,552 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/QQQ_evening.json