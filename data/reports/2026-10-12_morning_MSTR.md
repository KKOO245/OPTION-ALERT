# 期权晨报 2026-10-12（快照 10:20 ET）

📊 市场环境

SPY $777.91 ｜ QQQ $746.04
VIX 15.29 ↑3.0%（5D -1.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.96 ｜ 实际 待公布 ｜ 前值 3.98
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.7 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 10-16 157C ΔOI +30,663（距现价 +0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-23 100P ΔOI +20,080 占该期限总 OI 16.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 154.34 → 今开 153.22（-0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 158.40 ｜ 低 152.58

Options: P/C成交量 0.93 | OI比 0.67 | ATM IV 68.8% | Skew -4.7pp | Term 0.96 | ExpMove ±6.0%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构正常（Term 0.96）｜Put 保护异常便宜（Skew -4.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.67）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.93×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.67×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（4D）±6.0% ｜ 10-23（11D）±8.7% ｜ 10-30（18D）±11.0% ｜ 11-06（25D）±14.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 81,288,702 | GEX Change vs 上次快照 63,841,983 | Flip: Primary Flip: 141.39（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 616 / LOW 83 / INVALID 181
结构观察区: Primary Flip 141.39（全链重定价，覆盖 100%）
Call Wall 165（弱结构｜现价低于该位 4.9%）
最近结构参考: Call Wall 165（现价低于该位 4.9%）
量化视角： 正 Gamma（8129万，无历史分位）｜正 Gamma 增强（+6384万）｜现价位于 Flip 上方 11.01%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（MaxPain，仅结算参考）；上方 165（Call Wall，弱结构）。
• Gamma 区域：切换参考 141（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 165.0C — Vol 56,233 | 最新价 $1.67 | OI 10350→45374 (ΔOI +35024张) | ΔOI/Volume 62.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增35024张（+338.4% vs前日OI），连续性待观察（方向未知）
10-16 157.5C — Vol 33,974 | 最新价 $3.65 | OI 8841→39504 (ΔOI +30663张) | ΔOI/Volume 90.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30663张（+346.8% vs前日OI），连续性待观察（方向未知）
10-23 100.0P — Vol 20,676 | 最新价 $0.09 | OI 731→20811 (ΔOI +20080张) | ΔOI/Volume 97.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20080张（+2746.9% vs前日OI），连续性待观察（方向未知）
10-16 160.0C — Vol 32,825 | 最新价 $2.81 | OI 14722→31951 (ΔOI +17229张) | ΔOI/Volume 52.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17229张（+117.0% vs前日OI），连续性待观察（方向未知）
10-16 162.5C — Vol 19,703 | 最新价 $2.18 | OI 6948→20053 (ΔOI +13105张) | ΔOI/Volume 66.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13105张（+188.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 116,101 张（Put 20,080 / Call 96,021），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +123.5k / P +30.9k ｜ Activity HIGH ｜ 4D
10-23  C +4.6k / P +30.9k ｜ Activity HIGH ｜ 11D
10-30  C +3.8k / P +3.3k ｜ Activity MEDIUM △ ｜ 18D
11-06  C +0.5k / P +1.8k ｜ Activity MEDIUM △ ｜ 25D

📆 10-16 Forward Structure
存量OI: C 345.1k / P 232.7k，今日变化ΔOI: C +123.5k / P +30.9k，平值价格ATM: C $4.40 / P $4.94 ｜ ATM IV 68.8%，净 delta 敞口 4.4M shares
Top ΔOI: C 165 +35,024 ｜ C 157 +30,663 ｜ C 160 +17,229
仓位参考: Max Pain 140 ｜ Call Wall 165（+5.1%，弱）（OI 45.4k） ｜ Put Wall 142（-9.5%，弱）（OI 7.2k）
量化解读： 存量 Call 重｜ATM IV 68.8%｜历史 Rank 26%（近端代理）｜IV/RV 0.94×（近似）｜净 delta 敞口 正 4,443,223 股

📆 10-23 Forward Structure
存量OI: C 40.8k / P 83.9k，今日变化ΔOI: C +4.6k / P +30.9k，平值价格ATM: C $6.70 / P $6.95 ｜ ATM IV 62.1%，净 delta 敞口 104k shares
Top ΔOI: P 100 +20,080
仓位参考: Max Pain 158 ｜ Call Wall 172.5（+9.9%，弱）（OI 2.8k） ｜ Put Wall 160（+1.9%，弱）（OI 6.1k）
量化解读： 存量 Put 重｜ATM IV 62.1%｜历史 Rank 26%（近端代理）｜IV/RV 0.85×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 104,187 股

10-30（MEDIUM △）Top ΔOI: 160C +2,805 ｜ 125P +904
10-30（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 160（+1.9%，弱）（OI 3.8k） ｜ Put Wall 160（+1.9%，弱）（OI 3.3k）

11-06（MEDIUM △）Top ΔOI: 155C +259
11-06（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 160（+1.9%）（OI 1.2k） ｜ Put Wall 160（+1.9%，弱）（OI 2.6k）

📅 事件差分（观察，非因果）: 10-16（4D）ATM IV 68.8% vs 10-23 62.1%（差 +6.7pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/MSTR_morning.json