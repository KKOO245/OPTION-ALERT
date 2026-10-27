# 期权晨报 2026-10-27（快照 10:20 ET）

📊 市场环境

SPY $769.68 ｜ QQQ $721.25
VIX 18.02 ↓2.0%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 1.8 ｜ 前值 0.1　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🟡 **近现价集中开仓**: 10-28 85C ΔOI +545（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-04 86C ΔOI +81 占该期限总 OI 10.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 81.02 → 今开 81.37（+0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 82.18 ｜ 低 81.04

Options: P/C成交量 0.54 | OI比 1.63 | ATM IV 54.4% | Skew 3.3pp | Term 0.71 | ExpMove ±2.5%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜保护溢价中性（Skew 3.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.63×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-28（1D）±2.5% ｜ 10-30（3D）±4.1% ｜ 11-02（6D）±2.5% ｜ 11-04（8D）±4.5%
   ⇒ IV–VIX Spread: +36.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 38,418,275 | GEX Change vs 上次快照 11,443,930 | Flip: Primary Flip: 79.23（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 512 / LOW 138 / INVALID 538
结构观察区: Primary Flip 79.23（全链重定价，覆盖 99%）
Put Wall 80（弱结构｜现价高于该位 2.0%） | Call Wall 85（弱结构｜现价低于该位 4.0%）
最近结构参考: Put Wall 80（现价高于该位 2.0%）
量化视角： 正 Gamma（3842万，无历史分位）｜正 Gamma 增强（+1144万）｜现价位于 Flip 上方 2.96%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（Put Wall，弱结构）；上方 84（MaxPain，仅结算参考） / 85（Call Wall，弱结构）。
• Gamma 区域：切换参考 79（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 85.0C — Vol 1,174 | 最新价 $1.08 | OI 2118→3163 (ΔOI +1045张) | ΔOI/Volume 89.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1045张（+49.3% vs前日OI），连续性待观察（方向未知）
11-20 78.0P — Vol 1,466 | 最新价 $2.04 | OI 1489→2401 (ΔOI +912张) | ΔOI/Volume 62.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增912张（+61.2% vs前日OI），连续性待观察（方向未知）
11-06 90.0C — Vol 773 | 最新价 $0.31 | OI 328→1097 (ΔOI +769张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增769张（+234.4% vs前日OI），连续性待观察（方向未知）
10-30 85.0C — Vol 1,299 | 最新价 $0.35 | OI 27547→28165 (ΔOI +618张) | ΔOI/Volume 47.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增618张（+2.2% vs前日OI），连续性待观察（方向未知）
10-30 83.0C — Vol 1,134 | 最新价 $0.83 | OI 9138→9690 (ΔOI +552张) | ΔOI/Volume 48.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增552张（+6.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,896 张（Put 912 / Call 2,984），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-28  C +1.8k / P +0.6k ｜ Activity HIGH ｜ 1D
10-30  C +2.7k / P +0.1k ｜ Activity MEDIUM △ ｜ 3D
11-02  C +0.1k / P +0.1k ｜ Activity MEDIUM △ ｜ 6D
11-04  C +0.1k / P +24 ｜ Activity MEDIUM △ ｜ 8D

📆 10-28 Forward Structure
存量OI: C 3.7k / P 6.0k，今日变化ΔOI: C +1.8k / P +0.6k，平值价格ATM: C $0.83 / P $1.21 ｜ ATM IV 54.4%，净 delta 敞口 60k shares
Top ΔOI: P 76 +549 ｜ C 85 +545 ｜ C 81 +323
仓位参考: Max Pain 84 ｜ Call Wall 85（+4.2%，弱）（OI 0.6k） ｜ Put Wall 84（+3.0%，弱）（OI 2.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 54.4%｜历史 Rank 88%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 60,062 股

10-30（MEDIUM △）Top ΔOI: 85C +618 ｜ 83C +552
10-30（MEDIUM △）仓位参考: Max Pain 81 ｜ Call Wall 85（+4.2%，弱）（OI 28.2k） ｜ Put Wall 79（-3.2%，弱）（OI 3.6k）

11-02（MEDIUM △）Top ΔOI: 76P +62 ｜ 79P +40
11-02（MEDIUM △）仓位参考: Max Pain 86 ｜ Call Wall 86（+5.4%）（OI 0.5k） ｜ Put Wall 81（-0.7%）（OI 0.3k）

11-04（MEDIUM △）Top ΔOI: 86C +81 ｜ 86P +10
11-04（MEDIUM △）仓位参考: Max Pain 82 ｜ Call Wall 83（+1.7%，弱）（OI 0.2k） ｜ Put Wall 80（-1.9%，弱）（OI 18）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/GDX_morning.json