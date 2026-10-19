# 期权晨报 2026-10-19（快照 10:20 ET）

📊 市场环境

SPY $766.65 ｜ QQQ $721.24
VIX 18.46 ↓7.7%（5D +21.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 22.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🔴 **事件差分**: 10-23（4D）ATM IV 81.8% vs 10-26 65.9%（差 +15.9pp），覆盖 建筑许可 Prel、新屋开工
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-26 360P ΔOI +681（距现价 -0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 354.72 → 今开 357.48（+0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 365.44 ｜ 低 354.47

Options: P/C成交量 0.51 | OI比 0.46 | ATM IV 60.9% | Skew 0.2pp | Term 0.77 | ExpMove ±7.1%（近端） | Rank 73%
量化视角： IV 中性（Rank 73%）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价薄（Skew 0.2pp）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（4D）±7.1% ｜ 10-26（7D）±7.5% ｜ 10-28（9D）±8.0% ｜ 10-30（11D）±8.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 59,542,267 | GEX Change vs 上次快照 63,837,239 | Flip: Primary Flip: 348.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1226 / LOW 89 / INVALID 705
结构观察区: Primary Flip 348.38（全链重定价，覆盖 97%）
最近结构参考: Flip 348（现价高于该位 3.7%）
量化视角： 正 Gamma（5954万，无历史分位）｜由负转正（+6384万）｜现价位于 Flip 上方 3.74%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 360（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 348（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 130.0P — Vol 23,018 | 最新价 $0.01 | OI 1545→24561 (ΔOI +23016张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23016张（+1489.7% vs前日OI），连续性待观察（方向未知）
10-23 220.0P — Vol 19,701 | 最新价 $0.14 | OI 3760→21096 (ΔOI +17336张) | ΔOI/Volume 88.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17336张（+461.1% vs前日OI），连续性待观察（方向未知）
10-23 180.0P — Vol 12,006 | 最新价 $0.04 | OI 85→12034 (ΔOI +11949张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11949张（+14057.6% vs前日OI），连续性待观察（方向未知）
10-23 210.0P — Vol 8,930 | 最新价 $0.09 | OI 157→8788 (ΔOI +8631张) | ΔOI/Volume 96.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8631张（+5497.4% vs前日OI），连续性待观察（方向未知）
10-23 370.0C — Vol 13,674 | 最新价 $7.10 | OI 1652→8267 (ΔOI +6615张) | ΔOI/Volume 48.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6615张（+400.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 67,547 张（Put 60,932 / Call 6,615），跨 1 个期限｜远端彩票/名义（4 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 140.5k / P 64.1k，今日成交量: C 268.2k / P 137.1k，平值价格ATM: C $1.54 / P $3.47 ｜ ATM IV 60.9%，预期波动 ±1.4%，Max Pain 360
Top ΔOI: C 370 +6,124 ｜ P 350 +5,206 ｜ C 425 +4,770

📆 Forward Expiration Structure

10-23  C +65.4k / P +80.7k ｜ Activity HIGH ｜ 4D
10-26  C +5.3k / P +3.6k ｜ Activity HIGH ｜ 7D
10-28  C +1.5k / P +2.5k ｜ Activity HIGH ｜ 9D
10-30  C +3.6k / P +4.3k ｜ Activity HIGH ｜ 11D

📆 10-23 Forward Structure
存量OI: C 163.6k / P 148.1k，今日变化ΔOI: C +65.4k / P +80.7k，平值价格ATM: C $12.20 / P $13.46 ｜ ATM IV 81.8%，净 delta 敞口 1.4M shares
Top ΔOI: P 220 +17,336
仓位参考: Max Pain 365 ｜ Call Wall 385（+6.5%，弱）（OI 10.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 81.8%｜历史 Rank 73%（近端代理）｜IV/RV 2.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,437,761 股

📆 10-26 Forward Structure
存量OI: C 10.3k / P 10.1k，今日变化ΔOI: C +5.3k / P +3.6k，平值价格ATM: C $12.72 / P $14.20 ｜ ATM IV 65.9%，净 delta 敞口 11k shares
Top ΔOI: P 360 +681 ｜ P 350 +519
仓位参考: Max Pain 365 ｜ Call Wall 370（+2.4%，弱）（OI 0.7k） ｜ Put Wall 360（-0.4%，弱）（OI 1.0k）
量化解读： 存量两侧均衡｜ATM IV 65.9%｜历史 Rank 73%（近端代理）｜IV/RV 2.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 10,636 股

📆 10-28 Forward Structure
存量OI: C 4.9k / P 4.8k，今日变化ΔOI: C +1.5k / P +2.5k，平值价格ATM: C $13.50 / P $15.39 ｜ ATM IV 61.7%，净 delta 敞口 -21k shares
Top ΔOI: P 350 +1,196 ｜ P 330 +370 ｜ C 377 +185
仓位参考: Max Pain 360 ｜ Call Wall 377.5（+4.5%，弱）（OI 0.2k） ｜ Put Wall 350（-3.2%）（OI 1.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 61.7%｜历史 Rank 73%（近端代理）｜IV/RV 2.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 21,089 股

📆 10-30 Forward Structure
存量OI: C 68.8k / P 56.7k，今日变化ΔOI: C +3.6k / P +4.3k，平值价格ATM: C $14.87 / P $16.00 ｜ ATM IV 59.8%，净 delta 敞口 137k shares
Top ΔOI: C 380 +1,191 ｜ P 305 +1,024 ｜ P 295 +670
仓位参考: Max Pain 370 ｜ Call Wall 380（+5.1%，弱）（OI 3.9k） ｜ Put Wall 380（+5.1%，弱）（OI 3.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 59.8%｜历史 Rank 73%（近端代理）｜IV/RV 2.07×（近似）｜净 delta 敞口 正 137,227 股

📅 事件差分（观察，非因果）: 10-23（4D）ATM IV 81.8% vs 10-26 65.9%（差 +15.9pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/TSLA_morning.json