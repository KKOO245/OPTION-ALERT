# 期权晚报 2026-11-16（快照 16:40 ET）

📊 市场环境

SPY $739.95 ｜ QQQ $661.75
VIX 22.91 ↑18.7%（5D +15.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.8
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 44P ΔOI +3,818（距现价 +5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-18 48C ΔOI +4,035 占该期限总 OI 11.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 42.59 → 收盘 42.39（-0.5%） ｜ 今日高 42.92 ｜ 低 42.01 ｜ 昨收 44.13 → 收盘 42.39（-3.9%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-19，窗口结束前不做对错判定）

Options: P/C成交量 0.77 | OI比 0.60 | ATM IV 58.9% | Skew 8.3pp | Term 0.76 | ExpMove ±3.1%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价显著（Skew 8.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-18（2D）±3.1% ｜ 11-20（4D）±4.5% ｜ 11-23（7D）±5.0% ｜ 11-25（9D）±5.9%
   ⇒ IV–VIX Spread: +36.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -33,889,989 | GEX Change vs 上次快照 -6,090,875 | Flip: Primary Flip: 44.04（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 656 / LOW 137 / INVALID 417
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 44.04（全链重定价，覆盖 96%）
Put Wall 40（弱结构｜现价高于该位 6.0%）
最近结构参考: Flip 44（现价低于该位 3.7%）
量化视角： 负 Gamma（3389万，无历史分位）｜负 Gamma 加深（609万）｜现价位于 Flip 下方 3.74%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 40（Put Wall，弱结构）；上方 44（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 44（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 52.0C — Vol 12,857 | 最新价 $0.22 | OI 38220→50266 (ΔOI +12046张) | ΔOI/Volume 93.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12046张（+31.5% vs前日OI），连续性待观察（方向未知）
11-18 48.0C — Vol 1,576 | 最新价 $0.01 | OI 157→4192 (ΔOI +4035张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4035张（+2570.1% vs前日OI），连续性待观察（方向未知）
11-20 44.5P — Vol 199 | 最新价 $2.28 | OI 625→4443 (ΔOI +3818张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3818张（+610.9% vs前日OI），连续性待观察（方向未知）
11-20 45.0P — Vol 759 | 最新价 $2.75 | OI 11528→14580 (ΔOI +3052张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3052张（+26.5% vs前日OI），连续性待观察（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 22,951 张（Put 6,870 / Call 16,081），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-18  C +10.9k / P +3.2k ｜ Activity HIGH ｜ 2D
11-20  C -1.7k / P +9.2k ｜ Activity HIGH ｜ 4D
11-23  C +0.9k / P +0.4k ｜ Activity HIGH ｜ 7D
11-25  C +0.3k / P +0.3k ｜ Activity HIGH ｜ 9D

📆 11-18 Forward Structure
存量OI: C 22.1k / P 12.0k，今日变化ΔOI: C +10.9k / P +3.2k，平值价格ATM: C $0.61 / P $0.72 ｜ ATM IV 52.6%，净 delta 敞口 -62k shares
仓位参考: Max Pain 45 ｜ Put Wall 40（-5.6%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 52.6%｜历史 Rank 90%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 62,211 股

📆 11-20 Forward Structure
存量OI: C 571.2k / P 156.3k，今日变化ΔOI: C -1.7k / P +9.2k，平值价格ATM: C $0.90 / P $0.99 ｜ ATM IV 52.6%，净 delta 敞口 -537k shares
Top ΔOI: P 44 +3,818 ｜ P 45 +3,052
仓位参考: Max Pain 50 ｜ Put Wall 45（+6.2%，弱）（OI 14.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 52.6%｜历史 Rank 90%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 536,754 股

📆 11-23 Forward Structure
存量OI: C 7.3k / P 1.3k，今日变化ΔOI: C +0.9k / P +0.4k，平值价格ATM: C $1.05 / P $1.09 ｜ ATM IV 45.6%，净 delta 敞口 508 shares
Top ΔOI: P 40 +236 ｜ C 44 +108
仓位参考: Max Pain 44 ｜ Call Wall 46.5（+9.7%，弱）（OI 1.9k） ｜ Put Wall 40（-5.6%）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 45.6%｜历史 Rank 90%（近端代理）｜IV/RV 1.14×（近似）｜净 delta 敞口 正 508 股

📆 11-25 Forward Structure
存量OI: C 1.3k / P 1.0k，今日变化ΔOI: C +0.3k / P +0.3k，平值价格ATM: C $1.24 / P $1.25 ｜ ATM IV 47.0%，净 delta 敞口 -11k shares
Top ΔOI: P 44 +159
仓位参考: Max Pain 45 ｜ Call Wall 45（+6.2%，弱）（OI 60） ｜ Put Wall 44.5（+5.0%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 47.0%｜历史 Rank 90%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 负 10,501 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/SLV_evening.json