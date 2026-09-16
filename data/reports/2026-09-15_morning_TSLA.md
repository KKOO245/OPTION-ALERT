# 期权晨报 2026-09-15（快照 11:20 ET）

📊 市场环境

SPY $757.39 ｜ QQQ $nan
VIX 17.68 ↑3.4%（5D +12.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-16 360C ΔOI +3,567（距现价 +0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 358.97 → 今开 358.73（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 362.11 ｜ 低 354.63

Options: P/C成交量 0.84 | OI比 0.65 | ATM IV 47.3% | Skew -1.4pp | Term 0.86 | ExpMove ±2.2%（近端） | Rank 30%
量化视角： IV 中性（Rank 30%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.65×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-16（1D）±2.2% ｜ 09-18（3D）±3.5% ｜ 09-21（6D）±4.0% ｜ 09-23（8D）±4.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 20,416,152 | GEX Change vs 上次快照 12,626,957 | Flip: Primary Flip: 355.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1195 / LOW 120 / INVALID 689
结构观察区: Primary Flip 355.41（全链重定价，覆盖 99%）
最近结构参考: Flip 355（现价高于该位 0.6%）
量化视角： 正 Gamma（2042万，无历史分位）｜正 Gamma 增强（+1263万）｜现价位于 Flip 上方 0.64%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 360（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 355（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 377.5C — Vol 7,585 | 最新价 $1.43 | OI 3252→7934 (ΔOI +4682张) | ΔOI/Volume 61.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4682张（+144.0% vs前日OI），连续性待观察（方向未知）
09-18 275.0P — Vol 5,012 | 最新价 $0.08 | OI 3243→7914 (ΔOI +4671张) | ΔOI/Volume 93.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4671张（+144.0% vs前日OI），连续性待观察（方向未知）
09-16 380.0C — Vol 10,935 | 最新价 $0.37 | OI 1293→4871 (ΔOI +3578张) | ΔOI/Volume 32.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3578张（+276.7% vs前日OI），连续性待观察（方向未知）
09-16 360.0C — Vol 28,254 | 最新价 $4.40 | OI 837→4404 (ΔOI +3567张) | ΔOI/Volume 12.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3567张（+426.2% vs前日OI），连续性待观察（方向未知）
09-18 290.0P — Vol 5,527 | 最新价 $0.09 | OI 10490→13554 (ΔOI +3064张) | ΔOI/Volume 55.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3064张（+29.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 19,562 张（Put 7,735 / Call 11,827），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-16  C +30.4k / P +20.5k ｜ Activity HIGH ｜ 1D
09-18  C +25.0k / P +12.5k ｜ Activity HIGH ｜ 3D
09-21  C +4.1k / P +4.0k ｜ Activity HIGH ｜ 6D
09-23  C +2.0k / P +1.1k ｜ Activity HIGH ｜ 8D

📆 09-16 Forward Structure
存量OI: C 56.3k / P 36.8k，今日变化ΔOI: C +30.4k / P +20.5k，平值价格ATM: C $4.30 / P $3.58 ｜ ATM IV 47.3%，净 delta 敞口 44k shares
Top ΔOI: C 380 +3,578 ｜ C 360 +3,567
仓位参考: Max Pain 360 ｜ Call Wall 370（+3.4%，弱）（OI 5.2k） ｜ Put Wall 340（-4.9%）（OI 4.1k）
量化解读： 存量 Call 重｜ATM IV 47.3%｜历史 Rank 30%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 44,489 股

📆 09-18 Forward Structure
存量OI: C 575.9k / P 480.0k，今日变化ΔOI: C +25.0k / P +12.5k，平值价格ATM: C $6.65 / P $5.80 ｜ ATM IV 46.2%，净 delta 敞口 879k shares
Top ΔOI: C 377 +4,682
仓位参考: Max Pain 360 ｜ Call Wall 370（+3.4%，弱）（OI 20.2k） ｜ Put Wall 350（-2.1%，弱）（OI 17.8k）
量化解读： 存量 Call 重｜ATM IV 46.2%｜历史 Rank 30%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 878,547 股

📆 09-21 Forward Structure
存量OI: C 10.0k / P 9.0k，今日变化ΔOI: C +4.1k / P +4.0k，平值价格ATM: C $7.65 / P $6.70 ｜ ATM IV 38.5%，净 delta 敞口 -13k shares
Top ΔOI: P 360 +1,103 ｜ C 380 +649 ｜ C 357 +458
仓位参考: Max Pain 362 ｜ Call Wall 380（+6.2%）（OI 1.5k） ｜ Put Wall 360（+0.6%）（OI 1.6k）
量化解读： 存量两侧均衡｜ATM IV 38.5%｜历史 Rank 30%（近端代理）｜IV/RV 0.78×（近似）｜净 delta 敞口 负 12,575 股

📆 09-23 Forward Structure
存量OI: C 6.5k / P 3.6k，今日变化ΔOI: C +2.0k / P +1.1k，平值价格ATM: C $8.90 / P $8.05 ｜ ATM IV 39.7%，净 delta 敞口 24k shares
Top ΔOI: C 375 +250 ｜ C 365 +210 ｜ C 360 +168
仓位参考: Max Pain 365 ｜ Call Wall 380（+6.2%，弱）（OI 0.6k） ｜ Put Wall 382.5（+6.9%）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 39.7%｜历史 Rank 30%（近端代理）｜IV/RV 0.81×（近似）｜净 delta 敞口 正 23,860 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/TSLA_morning.json