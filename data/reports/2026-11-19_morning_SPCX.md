# 期权晨报 2026-11-19（快照 10:20 ET）

📊 市场环境

SPY $714.27 ｜ QQQ $645.04
VIX 22.66 ↓7.7%（5D +21.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 18.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 145P ΔOI +5,839（距现价 +0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 143.50 → 今开 144.91（+1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 147.29 ｜ 低 142.67

Options: P/C成交量 0.50 | OI比 0.79 | ATM IV 73.7% | Skew 6.3pp | Term 0.71 | ExpMove ±3.5%（近端） | Rank 79%
量化视角： IV 历史高位（Rank 79%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜保护溢价显著（Skew 6.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±3.5% ｜ 11-23（4D）±4.5% ｜ 11-25（6D）±6.0% ｜ 11-27（8D）±6.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 75,111,095 | GEX Change vs 上次快照 27,892,934 | Flip: Primary Flip: 141.28（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 752 / LOW 217 / INVALID 431
结构观察区: Primary Flip 141.28（全链重定价，覆盖 99%）
Put Wall 140（弱结构｜现价高于该位 3.2%）
最近结构参考: Flip 141（现价高于该位 2.3%）
量化视角： 正 Gamma（7511万，无历史分位）｜正 Gamma 增强（+2789万）｜现价位于 Flip 上方 2.28%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（Put Wall，弱结构） / 144（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 141（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 145.0P — Vol 24,777 | 最新价 $3.98 | OI 15744→21583 (ΔOI +5839张) | ΔOI/Volume 23.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5839张（+37.1% vs前日OI），连续性待观察（方向未知）
11-20 150.0C — Vol 50,229 | 最新价 $0.84 | OI 47889→51696 (ΔOI +3807张) | ΔOI/Volume 7.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3807张（+8.0% vs前日OI），连续性待观察（方向未知）
11-20 155.0C — Vol 8,741 | 最新价 $0.22 | OI 44807→48258 (ΔOI +3451张) | ΔOI/Volume 39.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3451张（+7.7% vs前日OI），连续性待观察（方向未知）
11-20 152.5C — Vol 7,701 | 最新价 $0.44 | OI 8097→11274 (ΔOI +3177张) | ΔOI/Volume 41.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3177张（+39.2% vs前日OI），连续性待观察（方向未知）
11-20 141.0P — Vol 18,195 | 最新价 $2.13 | OI 1760→3939 (ΔOI +2179张) | ΔOI/Volume 12.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2179张（+123.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 18,453 张（Put 8,018 / Call 10,435），跨 1 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +18.5k / P -1.5k ｜ Activity HIGH ｜ 1D
11-23  C +2.3k / P +2.2k ｜ Activity HIGH ｜ 4D
11-25  C +1.9k / P +1.1k ｜ Activity HIGH ｜ 6D
11-27  C +2.7k / P +5.1k ｜ Activity HIGH ｜ 8D

📆 11-20 Forward Structure
存量OI: C 552.8k / P 437.9k，今日变化ΔOI: C +18.5k / P -1.5k，平值价格ATM: C $2.61 / P $2.39 ｜ ATM IV 73.7%，净 delta 敞口 852k shares
Top ΔOI: P 145 +5,839 ｜ P 165 -4,016 ｜ C 150 +3,807
仓位参考: Max Pain 144 ｜ Call Wall 150（+3.8%，弱）（OI 51.7k） ｜ Put Wall 135（-6.6%，弱）（OI 42.8k）
量化解读： 存量 Call 重｜ATM IV 73.7%｜历史 Rank 79%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 852,481 股

📆 11-23 Forward Structure
存量OI: C 13.1k / P 9.7k，今日变化ΔOI: C +2.3k / P +2.2k，平值价格ATM: C $3.40 / P $3.10 ｜ ATM IV 53.1%，净 delta 敞口 -20k shares
Top ΔOI: C 152 +579 ｜ P 135 +392 ｜ C 155 +266
仓位参考: Max Pain 142 ｜ Call Wall 150（+3.8%）（OI 2.7k） ｜ Put Wall 140（-3.1%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 53.1%｜历史 Rank 79%（近端代理）｜IV/RV 0.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 19,594 股

📆 11-25 Forward Structure
存量OI: C 5.7k / P 4.0k，今日变化ΔOI: C +1.9k / P +1.1k，平值价格ATM: C $4.65 / P $4.00 ｜ ATM IV 55.9%，净 delta 敞口 30k shares
Top ΔOI: C 155 +257 ｜ C 143 +221
仓位参考: Max Pain 140 ｜ Call Wall 150（+3.8%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 55.9%｜历史 Rank 79%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 29,887 股

📆 11-27 Forward Structure
存量OI: C 130.5k / P 62.5k，今日变化ΔOI: C +2.7k / P +5.1k，平值价格ATM: C $4.76 / P $4.35 ｜ ATM IV 52.1%，净 delta 敞口 -82k shares
Top ΔOI: P 134 +508
仓位参考: Max Pain 142 ｜ Call Wall 150（+3.8%，弱）（OI 9.8k） ｜ Put Wall 135（-6.6%，弱）（OI 3.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 52.1%｜历史 Rank 79%（近端代理）｜IV/RV 0.84×（近似）｜净 delta 敞口 负 81,797 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/SPCX_morning.json