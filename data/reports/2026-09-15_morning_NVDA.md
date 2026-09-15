# 期权晨报 2026-09-15（快照 11:20 ET）

📊 市场环境

SPY $756.82 ｜ QQQ $705.52
VIX 17.68 ↑3.4%（5D +12.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.1（fear）
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
🟡 **近现价集中开仓**: 09-16 220C ΔOI +14,243（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-23 230C ΔOI +5,240 占该期限总 OI 19.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 210.96 → 今开 213.09（+1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 213.94 ｜ 低 211.63

Options: P/C成交量 0.34 | OI比 0.85 | ATM IV 40.4% | Skew 4.0pp | Term 0.84 | ExpMove ±1.9%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价中性（Skew 4.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-16（1D）±1.9% ｜ 09-18（3D）±3.0% ｜ 09-21（6D）±3.4% ｜ 09-23（8D）±4.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 129,679,660 | GEX Change vs 上次快照 95,229,032 | Flip: Primary Flip: 209.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 754 / LOW 185 / INVALID 561
结构观察区: Primary Flip 209.11（全链重定价，覆盖 100%）
Put Wall 200（现价高于该位 6.0%）
最近结构参考: Flip 209（现价高于该位 1.4%）
量化视角： 正 Gamma（1.30亿，无历史分位）｜正 Gamma 增强（+9523万）｜现价位于 Flip 上方 1.40%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall）；上方 212（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 209（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 215.0C — Vol 75,787 | 最新价 $1.72 | OI 29558→56434 (ΔOI +26876张) | ΔOI/Volume 35.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26876张（+90.9% vs前日OI），连续性待观察（方向未知）
09-18 220.0C — Vol 56,760 | 最新价 $0.63 | OI 47698→66061 (ΔOI +18363张) | ΔOI/Volume 32.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18363张（+38.5% vs前日OI），连续性待观察（方向未知）
09-16 220.0C — Vol 28,890 | 最新价 $0.19 | OI 4867→19110 (ΔOI +14243张) | ΔOI/Volume 49.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14243张（+292.6% vs前日OI），连续性待观察（方向未知）
09-18 190.0P — Vol 19,359 | 最新价 $0.17 | OI 28748→41091 (ΔOI +12343张) | ΔOI/Volume 63.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12343张（+42.9% vs前日OI），连续性待观察（方向未知）
09-16 212.5C — Vol 37,830 | 最新价 $1.67 | OI 284→12123 (ΔOI +11839张) | ΔOI/Volume 31.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11839张（+4168.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 83,664 张（Put 12,343 / Call 71,321），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-16  C +63.8k / P +63.9k ｜ Activity HIGH ｜ 1D
09-18  C +52.1k / P +48.9k ｜ Activity HIGH ｜ 3D
09-21  C +7.3k / P +4.9k ｜ Activity HIGH ｜ 6D
09-23  C +10.2k / P +2.6k ｜ Activity HIGH ｜ 8D

📆 09-16 Forward Structure
存量OI: C 120.5k / P 102.5k，今日变化ΔOI: C +63.8k / P +63.9k，平值价格ATM: C $2.00 / P $1.96 ｜ ATM IV 40.4%，净 delta 敞口 1.3M shares
Top ΔOI: C 220 +14,243 ｜ C 212 +11,839 ｜ C 215 +11,018
仓位参考: Max Pain 212 ｜ Call Wall 220（+3.8%，弱）（OI 19.1k） ｜ Put Wall 205（-3.3%，弱）（OI 9.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 40.4%｜历史 Rank 40%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,268,320 股

📆 09-18 Forward Structure
存量OI: C 1324.3k / P 1113.7k，今日变化ΔOI: C +52.1k / P +48.9k，平值价格ATM: C $3.20 / P $3.05 ｜ ATM IV 38.8%，净 delta 敞口 2.2M shares
Top ΔOI: C 215 +26,876 ｜ C 220 +18,363 ｜ P 190 +12,343
仓位参考: Max Pain 205 ｜ Call Wall 230（+8.5%，弱）（OI 97.0k） ｜ Put Wall 210（-1.0%，弱）（OI 55.9k）
量化解读： 存量 Call 重｜ATM IV 38.8%｜历史 Rank 40%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,182,330 股

📆 09-21 Forward Structure
存量OI: C 23.6k / P 22.5k，今日变化ΔOI: C +7.3k / P +4.9k，平值价格ATM: C $3.67 / P $3.58 ｜ ATM IV 32.4%，净 delta 敞口 117k shares
Top ΔOI: C 215 +1,554 ｜ C 220 +1,424 ｜ C 230 +1,397
仓位参考: Max Pain 212 ｜ Call Wall 230（+8.5%，弱）（OI 4.4k） ｜ Put Wall 200（-5.7%，弱）（OI 2.3k）
量化解读： 存量两侧均衡｜ATM IV 32.4%｜历史 Rank 40%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 正 116,544 股

📆 09-23 Forward Structure
存量OI: C 21.3k / P 5.7k，今日变化ΔOI: C +10.2k / P +2.6k，平值价格ATM: C $4.35 / P $4.30 ｜ ATM IV 33.2%，净 delta 敞口 83k shares
Top ΔOI: C 230 +5,240 ｜ C 220 +756
仓位参考: Max Pain 218 ｜ Call Wall 230（+8.5%）（OI 9.7k） ｜ Put Wall 225（+6.1%）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 33.2%｜历史 Rank 40%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 正 83,145 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/NVDA_morning.json