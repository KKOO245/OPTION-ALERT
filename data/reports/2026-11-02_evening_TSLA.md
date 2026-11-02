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
🟡 **近现价集中开仓**: 11-04 397P ΔOI +2,387（距现价 -1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 404.74 → 收盘 403.82（-0.2%） ｜ 今日高 414.23 ｜ 低 397.61 ｜ 昨收 399.81 → 收盘 403.82（+1.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.93 | OI比 0.74 | ATM IV 31.6% | Skew 8.9pp | Term 1.42 | ExpMove ±3.9%（近端） | Rank 4%
量化视角： IV 历史低位（Rank 4%，期权偏便宜）｜期限结构正常偏陡（Term 1.42）｜保护溢价显著（Skew 8.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.93×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-04（2D）±3.9% ｜ 11-06（4D）±5.1% ｜ 11-09（7D）±5.7% ｜ 11-11（9D）±6.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 83,999,077 | GEX Change vs 上次快照 70,878 | Flip: Primary Flip: 376.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 1224 / LOW 126 / INVALID 966
结构观察区: Primary Flip 376.91（全链重定价，覆盖 92%）
Call Wall 400（现价高于该位 1.0%）
最近结构参考: Call Wall 400（现价高于该位 1.0%）
量化视角： 正 Gamma（8400万，无历史分位）｜正 Gamma 增强（+7万）｜现价位于 Flip 上方 7.14%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 398（MaxPain，仅结算参考） / 400（Call Wall）。
• Gamma 区域：切换参考 377（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 240.0P — Vol 92 | 最新价 $0.03 | OI 2345→25767 (ΔOI +23422张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23422张（+998.8% vs前日OI），连续性待观察（方向未知）
11-06 140.0P — Vol 2,033 | 最新价 $0.01 | OI 1926→22318 (ΔOI +20392张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20392张（+1058.8% vs前日OI），连续性待观察（方向未知）
11-06 220.0P — Vol 1,684 | 最新价 $0.01 | OI 1709→16242 (ΔOI +14533张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14533张（+850.4% vs前日OI），连续性待观察（方向未知）
11-06 150.0P — Vol 10,446 | 最新价 $0.01 | OI 4895→15218 (ΔOI +10323张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10323张（+210.9% vs前日OI），连续性待观察（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 68,670 张（Put 68,670 / Call 0），跨 1 个期限｜远端彩票/名义（4 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-04  C +8.7k / P +13.6k ｜ Activity HIGH ｜ 2D
11-06  C +39.6k / P +102.3k ｜ Activity HIGH ｜ 4D
11-09  C +2.5k / P +1.8k ｜ Activity HIGH ｜ 7D
11-11  C +2.5k / P +1.0k ｜ Activity HIGH ｜ 9D

📆 11-04 Forward Structure
存量OI: C 22.5k / P 26.6k，今日变化ΔOI: C +8.7k / P +13.6k，平值价格ATM: C $7.21 / P $8.40 ｜ ATM IV 64.5%，净 delta 敞口 153k shares
Top ΔOI: P 397 +2,387 ｜ P 395 +1,381
仓位参考: Max Pain 398 ｜ Call Wall 420（+4.0%，弱）（OI 1.9k） ｜ Put Wall 397.5（-1.6%，弱）（OI 2.7k）
量化解读： 存量两侧均衡｜ATM IV 64.5%｜历史 Rank 4%（近端代理）｜IV/RV 1.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 153,217 股

📆 11-06 Forward Structure
存量OI: C 122.4k / P 205.8k，今日变化ΔOI: C +39.6k / P +102.3k，平值价格ATM: C $9.71 / P $10.91 ｜ ATM IV 60.3%，净 delta 敞口 1.1M shares
Top ΔOI: P 240 +23,422
仓位参考: Max Pain 390 ｜ Call Wall 410（+1.5%，弱）（OI 9.7k） ｜ Put Wall 380（-5.9%，弱）（OI 6.8k）
量化解读： 存量 Put 重｜ATM IV 60.3%｜历史 Rank 4%（近端代理）｜IV/RV 1.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,108,918 股

📆 11-09 Forward Structure
存量OI: C 5.5k / P 5.9k，今日变化ΔOI: C +2.5k / P +1.8k，平值价格ATM: C $10.80 / P $12.25 ｜ ATM IV 50.8%，净 delta 敞口 77k shares
Top ΔOI: C 400 +749 ｜ P 367 +332 ｜ P 372 +310
仓位参考: Max Pain 395 ｜ Call Wall 400（-0.9%，弱）（OI 1.0k） ｜ Put Wall 380（-5.9%）（OI 1.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 50.8%｜历史 Rank 4%（近端代理）｜IV/RV 1.53×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 76,820 股

📆 11-11 Forward Structure
存量OI: C 4.8k / P 2.8k，今日变化ΔOI: C +2.5k / P +1.0k，平值价格ATM: C $12.60 / P $13.50 ｜ ATM IV 49.9%，净 delta 敞口 41k shares
Top ΔOI: C 450 +738
仓位参考: Max Pain 395 ｜ Call Wall 405（+0.3%，弱）（OI 0.7k） ｜ Put Wall 395（-2.2%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 49.9%｜历史 Rank 4%（近端代理）｜IV/RV 1.50×（近似）｜净 delta 敞口 正 40,718 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/TSLA_evening.json