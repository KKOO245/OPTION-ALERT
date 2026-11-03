# 期权晚报 2026-11-02（快照 21:00 ET）

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
- 周一 11-02 19:00　【高】Midterm Elections　实际 待公布　✅ 今日已公布
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.13 ｜ 实际 待公布 ｜ 前值 7.079
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48.2 ｜ 实际 待公布 ｜ 前值 48

🔍 重点速览
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 759.45 → 收盘 752.10（-1.0%） ｜ 今日高 763.85 ｜ 低 751.60 ｜ 昨收 755.72 → 收盘 752.10（-0.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-05，窗口结束前不做对错判定）

Options: P/C成交量 1.20 | OI比 1.50 | ATM IV 21.3% | Skew 3.2pp | Term 0.80 | ExpMove ±0.9%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价中性（Skew 3.2pp）｜当日成交偏 Put（P/C量 1.20）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.20×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.50×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 25% ｜ P/C OI(近端) 24%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 25%）｜近端持仓结构中性（P/C OI 分位 24%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-03（1D）±0.9% ｜ 11-04（2D）±1.4% ｜ 11-05（3D）±1.7% ｜ 11-06（4D）±1.9%
   ⇒ IV–VIX Spread: +0.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,426,568,781 | GEX Change vs 上次快照 -474,889,419 | Flip: Primary Flip: 770.20（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 2306 / LOW 245 / INVALID 1485
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 770.20（全链重定价，覆盖 99%）
最近结构参考: Flip 770（现价低于该位 2.4%）
量化视角： 负 Gamma（14.27亿，历史分位 25%，中性区）｜负 Gamma 加深（4.75亿）｜现价位于 Flip 下方 2.35%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 756（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 770（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-03  C +0 / P +0 ｜ Activity LOW ｜ 1D
11-04  C +0 / P +0 ｜ Activity LOW ｜ 2D
11-05  C +0 / P +0 ｜ Activity LOW ｜ 3D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 4D

📆 11-03 Forward Structure
存量OI: C 93.6k / P 140.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.00 / P $2.80 ｜ ATM IV 21.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 756 ｜ Call Wall 750（-0.3%）（OI 9.6k） ｜ Put Wall 736（-2.1%，弱）（OI 20.1k）
量化解读： 存量 Put 重｜ATM IV 21.3%｜历史 Rank 87%（近端代理）｜IV/RV 1.95×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

11-04（Activity LOW）仓位参考: Max Pain 767 ｜ Call Wall 765（+1.7%，弱）（OI 5.2k） ｜ Put Wall 740（-1.6%，弱）（OI 58.3k）

11-05（Activity LOW）仓位参考: Max Pain 765 ｜ Call Wall 770（+2.4%，弱）（OI 4.4k） ｜ Put Wall 735（-2.3%，弱）（OI 3.1k）

11-06（Activity LOW）仓位参考: Max Pain 764 ｜ Call Wall 770（+2.4%，弱）（OI 13.7k） ｜ Put Wall 750（-0.3%）（OI 38.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=72 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=72）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/SPY_evening.json