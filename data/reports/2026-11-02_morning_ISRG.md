# 期权晨报 2026-11-02（快照 10:20 ET）

📊 市场环境

SPY $752.10 ｜ QQQ $681.09
VIX 18.83 ↓3.0%（5D +2.4%） ｜ Vol Regime: NORMAL
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
🟡 **近现价集中开仓**: 11-06 432C ΔOI +115（距现价 -1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 432.01 → 今开 439.79（+1.8%） | 较昨收变动（含盘初走势） ｜ 今日高 441.87 ｜ 低 437.07

Options: P/C成交量 0.52 | OI比 0.86 | ATM IV 41.1% | Skew 9.0pp | Term 0.80 | ExpMove ±3.6%（近端） | Rank 55%
量化视角： IV 中性（Rank 55%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价显著（Skew 9.0pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（4D）±3.6% ｜ 11-13（11D）±6.2% ｜ 11-20（18D）±6.4% ｜ 11-27（25D）±5.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,690,154 | GEX Change vs 上次快照 461,442 | Flip: Primary Flip: 419.01（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 232 / LOW 128 / INVALID 552
结构观察区: Primary Flip 419.01（全链重定价，覆盖 94%）
Call Wall 420（弱结构｜现价高于该位 4.9%）
最近结构参考: Call Wall 420（现价高于该位 4.9%）
量化视角： 正 Gamma（169万，无历史分位）｜正 Gamma 增强（+46万）｜现价位于 Flip 上方 5.18%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 430（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 419（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 415.0P — Vol 250 | 最新价 $2.50 | OI 18→209 (ΔOI +191张) | ΔOI/Volume 76.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增191张（+1061.1% vs前日OI），连续性待观察（方向未知）
11-06 432.5C — Vol 145 | 最新价 $7.82 | OI 10→125 (ΔOI +115张) | ΔOI/Volume 79.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增115张（+1150.0% vs前日OI），连续性待观察（方向未知）
11-06 422.5P — Vol 103 | 最新价 $4.24 | OI 44→145 (ΔOI +101张) | ΔOI/Volume 98.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增101张（+229.6% vs前日OI），连续性待观察（方向未知）
11-06 420.0P — Vol 121 | 最新价 $2.93 | OI 180→236 (ΔOI +56张) | ΔOI/Volume 46.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增56张（+31.1% vs前日OI），连续性待观察（方向未知）
11-27 430.0C — Vol 55 | 最新价 $17.80 | OI 10→64 (ΔOI +54张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增54张（+540.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 517 张（Put 348 / Call 169），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +0.3k / P +0.5k ｜ Activity MEDIUM △ ｜ 4D
11-13  C +20 / P +0.1k ｜ Activity MEDIUM △ ｜ 11D
11-20  C +62 / P +5 ｜ Activity MEDIUM △ ｜ 18D
11-27  C +0.1k / P +18 ｜ Activity HIGH ｜ 25D

📆 11-06 Forward Structure
存量OI: C 1.8k / P 1.5k，今日变化ΔOI: C +0.3k / P +0.5k，平值价格ATM: C $7.00 / P $9.00 ｜ ATM IV 41.1%，净 delta 敞口 5k shares
Top ΔOI: P 415 +191 ｜ C 432 +115 ｜ P 422 +101
仓位参考: Max Pain 430 ｜ Call Wall 430（-2.4%，弱）（OI 0.1k） ｜ Put Wall 420（-4.7%，弱）（OI 0.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 41.1%｜历史 Rank 55%（近端代理）｜IV/RV 1.56×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,038 股

11-13（MEDIUM △）Top ΔOI: 402P +52 ｜ 405P +50
11-13（MEDIUM △）仓位参考: Max Pain 430 ｜ Call Wall 440（-0.2%，弱）（OI 0.1k） ｜ Put Wall 420（-4.7%，弱）（OI 83）

11-20（MEDIUM △）Top ΔOI: 480C +20 ｜ 455C +18
11-20（MEDIUM △）仓位参考: Max Pain 405 ｜ Call Wall 420（-4.7%，弱）（OI 0.8k） ｜ Put Wall 410（-7.0%，弱）（OI 0.5k）

📆 11-27 Forward Structure
存量OI: C 0.4k / P 0.5k，今日变化ΔOI: C +0.1k / P +18，平值价格ATM: C $13.50 / P $12.40 ｜ ATM IV 34.2%，净 delta 敞口 5k shares
Top ΔOI: C 430 +54 ｜ C 445 +38 ｜ P 425 +12
仓位参考: Max Pain 425 ｜ Call Wall 430（-2.4%，弱）（OI 64） ｜ Put Wall 410（-7.0%，弱）（OI 44）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 34.2%｜历史 Rank 55%（近端代理）｜IV/RV 1.30×（近似）｜净 delta 敞口 正 5,400 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/ISRG_morning.json