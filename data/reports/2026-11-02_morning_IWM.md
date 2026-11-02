# 期权晨报 2026-11-02（快照 10:20 ET）

📊 市场环境

SPY $760.66 ｜ QQQ $698.66
VIX 18.83 ↓3.0%（5D +2.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.4（fear）
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
🟡 **近现价集中开仓**: 11-03 287C ΔOI +2,847（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-04 288C ΔOI +6,085 占该期限总 OI 12.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 279.33 → 今开 281.64（+0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 283.07 ｜ 低 280.54

Options: P/C成交量 0.61 | OI比 0.39 | ATM IV 27.0% | Skew -1.0pp | Term 0.71 | ExpMove ±1.0%（近端） | Rank 73%
量化视角： IV 中性（Rank 73%）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.39）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.39×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-03（1D）±1.0% ｜ 11-04（2D）±1.5% ｜ 11-05（3D）±1.7% ｜ 11-06（4D）±2.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -163,602,828 | GEX Change vs 上次快照 324,749,024 | Flip: Primary Flip: 284.04（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1318 / LOW 122 / INVALID 870
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 284.04（全链重定价，覆盖 99%）
Put Wall 270（弱结构｜现价高于该位 4.5%） | Call Wall 285（弱结构｜现价低于该位 1.0%）
最近结构参考: Flip 284（现价低于该位 0.6%）
量化视角： 负 Gamma（1.64亿，无历史分位）｜负 Gamma 缓解（+3.25亿）｜现价位于 Flip 下方 0.64%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构） / 279（MaxPain，仅结算参考）；上方 285（Call Wall，弱结构）。
• Gamma 区域：切换参考 284（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 265.0P — Vol 93,381 | 最新价 $1.63 | OI 133696→166861 (ΔOI +33165张) | ΔOI/Volume 35.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33165张（+24.8% vs前日OI），连续性待观察（方向未知）
11-02 286.0C — Vol 19,357 | 最新价 $0.16 | OI 1776→18852 (ΔOI +17076张) | ΔOI/Volume 88.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17076张（+961.5% vs前日OI），连续性待观察（方向未知）
11-20 268.0P — Vol 58,211 | 最新价 $2.06 | OI 50934→66927 (ΔOI +15993张) | ΔOI/Volume 27.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15993张（+31.4% vs前日OI），连续性待观察（方向未知）
11-06 275.0P — Vol 20,274 | 最新价 $1.63 | OI 9783→23758 (ΔOI +13975张) | ΔOI/Volume 68.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13975张（+142.8% vs前日OI），连续性待观察（方向未知）
11-02 284.0C — Vol 17,787 | 最新价 $0.33 | OI 1201→14113 (ΔOI +12912张) | ΔOI/Volume 72.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12912张（+1075.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 93,121 张（Put 63,133 / Call 29,988），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $11M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 93.5k / P 36.2k，今日成交量: C 98.8k / P 60.4k，平值价格ATM: C $0.88 / P $0.77 ｜ ATM IV 27.0%，预期波动 ±0.6%，Max Pain 279
Top ΔOI: C 286 +17,076 ｜ C 284 +12,912 ｜ P 277 +7,187

📆 Forward Expiration Structure

11-03  C +8.6k / P +3.3k ｜ Activity HIGH ｜ 1D
11-04  C +12.6k / P +12.2k ｜ Activity HIGH ｜ 2D
11-05  C +1.3k / P +2.8k ｜ Activity HIGH ｜ 3D
11-06  C +14.1k / P +55.4k ｜ Activity HIGH ｜ 4D

📆 11-03 Forward Structure
存量OI: C 20.8k / P 20.5k，今日变化ΔOI: C +8.6k / P +3.3k，平值价格ATM: C $1.52 / P $1.35 ｜ ATM IV 21.4%，净 delta 敞口 99k shares
Top ΔOI: C 287 +2,847 ｜ C 284 +1,441 ｜ C 285 +1,297
仓位参考: Max Pain 280 ｜ Call Wall 287（+1.7%）（OI 3.4k） ｜ Put Wall 270（-4.3%，弱）（OI 2.3k）
量化解读： 存量两侧均衡｜ATM IV 21.4%｜历史 Rank 73%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 99,484 股

📆 11-04 Forward Structure
存量OI: C 21.4k / P 27.4k，今日变化ΔOI: C +12.6k / P +12.2k，平值价格ATM: C $2.29 / P $2.06 ｜ ATM IV 24.3%，净 delta 敞口 274k shares
Top ΔOI: C 288 +6,085 ｜ C 285 +3,160 ｜ P 270 +2,772
仓位参考: Max Pain 280 ｜ Call Wall 288（+2.0%）（OI 6.2k） ｜ Put Wall 272（-3.6%，弱）（OI 3.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 24.3%｜历史 Rank 73%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 274,150 股

📆 11-05 Forward Structure
存量OI: C 7.3k / P 17.5k，今日变化ΔOI: C +1.3k / P +2.8k，平值价格ATM: C $2.68 / P $2.05 ｜ ATM IV 23.2%，净 delta 敞口 48k shares
Top ΔOI: P 260 +913 ｜ P 270 +380 ｜ C 280 +235
仓位参考: Max Pain 280 ｜ Call Wall 280（-0.8%，弱）（OI 1.4k） ｜ Put Wall 260（-7.9%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 23.2%｜历史 Rank 73%（近端代理）｜净 delta 敞口 正 47,561 股

📆 11-06 Forward Structure
存量OI: C 105.0k / P 254.4k，今日变化ΔOI: C +14.1k / P +55.4k，平值价格ATM: C $3.04 / P $2.71 ｜ ATM IV 23.7%，净 delta 敞口 381k shares
Top ΔOI: P 275 +13,975 ｜ P 270 +5,622
仓位参考: Max Pain 279 ｜ Call Wall 285（+1.0%，弱）（OI 10.6k） ｜ Put Wall 275（-2.6%，弱）（OI 23.8k）
量化解读： 存量 Put 重｜ATM IV 23.7%｜历史 Rank 73%（近端代理）｜净 delta 敞口 正 381,428 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/IWM_morning.json