# 期权晨报 2026-10-08（快照 10:20 ET）

📊 市场环境

SPY $775.90 ｜ QQQ $755.92
VIX 15.43 ↑2.3%（5D -5.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **事件差分**: 10-09 ATM IV 49.1% vs 10-12 36.8%（差 +12.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-09 170P ΔOI -4,221（距现价 +2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 167.60 → 今开 167.50（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 167.60 ｜ 低 165.09

Options: P/C成交量 0.66 | OI比 1.09 | ATM IV 49.1% | Skew -1.3pp | Term 0.98 | ExpMove ±2.3%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构正常（Term 0.98）｜Put 保护异常便宜（Skew -1.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.09×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（1D）±2.3% ｜ 10-12（4D）±3.2% ｜ 10-14（6D）±4.3% ｜ 10-16（8D）±5.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 63,235,986 | GEX Change vs 上次快照 -15,126,059 | Flip: Primary Flip: 161.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 750 / LOW 138 / INVALID 412
结构观察区: Primary Flip 161.53（全链重定价，覆盖 99%）
Call Wall 180（弱结构｜现价低于该位 7.8%）
最近结构参考: Flip 162（现价高于该位 2.7%）
量化视角： 正 Gamma（6324万，无历史分位）｜正 Gamma 减弱（1513万）｜现价位于 Flip 上方 2.72%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 165（MaxPain，仅结算参考）；上方 180（Call Wall，弱结构）。
• Gamma 区域：切换参考 162（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 160.0P — Vol 4,515 | 最新价 $4.20 | OI 1501→4887 (ΔOI +3386张) | ΔOI/Volume 75.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3386张（+225.6% vs前日OI），连续性待观察（方向未知）
10-09 167.5P — Vol 41,832 | 最新价 $2.32 | OI 7239→10442 (ΔOI +3203张) | ΔOI/Volume 7.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3203张（+44.2% vs前日OI），连续性待观察（方向未知）
10-30 180.0C — Vol 5,369 | 最新价 $3.50 | OI 4872→7698 (ΔOI +2826张) | ΔOI/Volume 52.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2826张（+58.0% vs前日OI），连续性待观察（方向未知）
10-16 165.0P — Vol 13,332 | 最新价 $3.34 | OI 7994→10457 (ΔOI +2463张) | ΔOI/Volume 18.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2463张（+30.8% vs前日OI），连续性待观察（方向未知）
10-09 170.0C — Vol 70,915 | 最新价 $1.45 | OI 14596→16995 (ΔOI +2399张) | ΔOI/Volume 3.4% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增2399张（+16.4% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,277 张（Put 9,052 / Call 5,225），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +6.9k / P -5.4k ｜ Activity MEDIUM △ ｜ 1D
10-12  C +7.3k / P +3.8k ｜ Activity HIGH ｜ 4D
10-14  C +2.8k / P +1.1k ｜ Activity HIGH ｜ 6D
10-16  C +0.6k / P +4.6k ｜ Activity HIGH ｜ 8D

📆 10-09 Forward Structure
存量OI: C 198.3k / P 216.5k，今日变化ΔOI: C +6.9k / P -5.4k，平值价格ATM: C $2.30 / P $1.57 ｜ ATM IV 49.1%，净 delta 敞口 60k shares
Top ΔOI: P 170 -4,221 ｜ P 167 +3,203 ｜ C 170 +2,399
仓位参考: Max Pain 165 ｜ Call Wall 180（+8.5%，弱）（OI 27.5k） ｜ Put Wall 160（-3.6%，弱）（OI 18.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 49.1%｜历史 Rank 26%（近端代理）｜IV/RV 1.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 59,982 股

📆 10-12 Forward Structure
存量OI: C 36.1k / P 19.1k，今日变化ΔOI: C +7.3k / P +3.8k，平值价格ATM: C $3.00 / P $2.26 ｜ ATM IV 36.8%，净 delta 敞口 38k shares
Top ΔOI: C 170 +2,225 ｜ C 182 +1,624
仓位参考: Max Pain 170 ｜ Call Wall 170（+2.5%，弱）（OI 5.7k） ｜ Put Wall 165（-0.6%，弱）（OI 2.9k）
量化解读： 存量 Call 重｜ATM IV 36.8%｜历史 Rank 26%（近端代理）｜IV/RV 0.77×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 38,105 股

📆 10-14 Forward Structure
存量OI: C 7.2k / P 3.8k，今日变化ΔOI: C +2.8k / P +1.1k，平值价格ATM: C $4.04 / P $3.15 ｜ ATM IV 40.9%，净 delta 敞口 46k shares
Top ΔOI: C 170 +546 ｜ C 175 +452 ｜ P 160 +366
仓位参考: Max Pain 170 ｜ Call Wall 175（+5.5%，弱）（OI 1.2k） ｜ Put Wall 165（-0.6%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 40.9%｜历史 Rank 26%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 正 45,544 股

📆 10-16 Forward Structure
存量OI: C 348.8k / P 376.5k，今日变化ΔOI: C +0.6k / P +4.6k，平值价格ATM: C $4.65 / P $3.85 ｜ ATM IV 42.5%，净 delta 敞口 -695k shares
Top ΔOI: C 160 -6,328 ｜ P 165 +2,463
仓位参考: Max Pain 150 ｜ Call Wall 160（-3.6%，弱）（OI 26.6k） ｜ Put Wall 150（-9.6%，弱）（OI 24.1k）
量化解读： 存量两侧均衡｜ATM IV 42.5%｜历史 Rank 26%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 负 695,282 股

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 49.1% vs 10-12 36.8%（差 +12.2pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/SPCX_morning.json