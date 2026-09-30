# 期权晨报 2026-09-30（快照 10:20 ET）

📊 市场环境

SPY $763.60 ｜ QQQ $739.77
VIX 15.68 ↓2.2%（5D +3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-01 775C ΔOI +5,707（距现价 +0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-06 670P ΔOI +8,174 占该期限总 OI 14.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 764.20 → 今开 766.45（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 769.15 ｜ 低 766.00

Options: P/C成交量 0.78 | OI比 2.60 | ATM IV 17.0% | Skew 1.7pp | Term 0.78 | ExpMove ±0.7%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价薄（Skew 1.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 2.60×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 56% ｜ P/C OI(近端) 90%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 56%）｜近端 Put 显著偏重（P/C OI 分位 90%，历史高位区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-01（1D）±0.7% ｜ 10-02（2D）±0.9% ｜ 10-05（5D）±1.1% ｜ 10-06（6D）±1.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,769,258 | GEX Change vs 上次快照 1,105,217,372 | Flip: Primary Flip: 768.29（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 2490 / LOW 495 / INVALID 2151
结构观察区: Primary Flip 768.29（全链重定价，覆盖 90%）
Call Wall 785（现价低于该位 2.1%）
最近结构参考: Flip 768（现价高于该位 0.0%）
量化视角： 正 Gamma（177万，历史分位 56%，中性区）｜由负转正（+11.05亿）｜现价位于 Flip 上方 0.00%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 761（MaxPain，仅结算参考）；上方 785（Call Wall）。
• Gamma 区域：切换参考 768（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 745.0P — Vol 61,487 | 最新价 $4.05 | OI 1038→61466 (ΔOI +60428张) | ΔOI/Volume 98.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增60428张（+5821.6% vs前日OI），连续性待观察（方向未知）
10-23 725.0P — Vol 60,847 | 最新价 $1.89 | OI 1988→62404 (ΔOI +60416张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增60416张（+3039.0% vs前日OI），连续性待观察（方向未知）
10-09 780.0C — Vol 46,963 | 最新价 $1.21 | OI 7994→43624 (ΔOI +35630张) | ΔOI/Volume 75.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增35630张（+445.7% vs前日OI），连续性待观察（方向未知）
10-09 725.0P — Vol 32,714 | 最新价 $0.37 | OI 46452→78584 (ΔOI +32132张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增32132张（+69.2% vs前日OI），连续性待观察（方向未知）
10-09 745.0P — Vol 34,295 | 最新价 $1.43 | OI 47990→79933 (ΔOI +31943张) | ΔOI/Volume 93.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31943张（+66.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 220,549 张（Put 184,919 / Call 35,630），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $40M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 739.0k / P 1921.8k，今日成交量: C 608.5k / P 471.4k，平值价格ATM: C $1.81 / P $1.08 ｜ ATM IV 17.0%，预期波动 ±0.4%，Max Pain 761
Top ΔOI: P 761 -11,782 ｜ C 765 +10,689 ｜ C 766 +9,515

📆 Forward Expiration Structure

10-01  C +23.7k / P +24.5k ｜ Activity HIGH ｜ 1D
10-02  C +39.5k / P +24.1k ｜ Activity HIGH ｜ 2D
10-05  C +6.4k / P +11.5k ｜ Activity HIGH ｜ 5D
10-06  C +10.5k / P +16.7k ｜ Activity HIGH ｜ 6D

📆 10-01 Forward Structure
存量OI: C 97.0k / P 105.2k，今日变化ΔOI: C +23.7k / P +24.5k，平值价格ATM: C $2.89 / P $2.10 ｜ ATM IV 13.7%，净 delta 敞口 827k shares
Top ΔOI: C 775 +5,707 ｜ P 765 +4,959 ｜ P 732 +2,600
仓位参考: Max Pain 765 ｜ Call Wall 782（+1.8%）（OI 13.6k） ｜ Put Wall 765（-0.4%，弱）（OI 7.5k）
量化解读： 存量两侧均衡｜ATM IV 13.7%｜历史 Rank 74%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 827,369 股

📆 10-02 Forward Structure
存量OI: C 309.9k / P 486.1k，今日变化ΔOI: C +39.5k / P +24.1k，平值价格ATM: C $4.01 / P $2.91 ｜ ATM IV 14.2%，净 delta 敞口 1.1M shares
Top ΔOI: C 770 +5,850 ｜ P 755 +5,318 ｜ C 775 +4,099
仓位参考: Max Pain 765 ｜ Call Wall 785（+2.2%）（OI 58.6k） ｜ Put Wall 750（-2.4%，弱）（OI 18.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 14.2%｜历史 Rank 74%（近端代理）｜IV/RV 1.44×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,145,643 股

📆 10-05 Forward Structure
存量OI: C 38.1k / P 65.2k，今日变化ΔOI: C +6.4k / P +11.5k，平值价格ATM: C $4.75 / P $3.60 ｜ ATM IV 11.2%，净 delta 敞口 171k shares
Top ΔOI: P 755 +3,981 ｜ P 750 +3,942 ｜ C 770 +844
仓位参考: Max Pain 766 ｜ Call Wall 775（+0.9%，弱）（OI 2.1k） ｜ Put Wall 750（-2.4%，弱）（OI 5.5k）
量化解读： 存量 Put 重｜ATM IV 11.2%｜历史 Rank 74%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 正 170,735 股

📆 10-06 Forward Structure
存量OI: C 25.7k / P 31.6k，今日变化ΔOI: C +10.5k / P +16.7k，平值价格ATM: C $5.14 / P $4.14 ｜ ATM IV 11.5%，净 delta 敞口 227k shares
Top ΔOI: P 715 +980 ｜ C 782 +866
仓位参考: Max Pain 766 ｜ Call Wall 775（+0.9%）（OI 4.0k）
量化解读： 存量 Put 重｜ATM IV 11.5%｜历史 Rank 74%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 正 227,231 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/SPY_morning.json