# 期权晨报 2026-11-16（快照 10:20 ET）

📊 市场环境

SPY $740.36 ｜ QQQ $661.75
VIX 21.57 ↑11.8%（5D +8.3%） ｜ Vol Regime: ELEVATED
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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-18 133P ΔOI +694（距现价 -3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 139.11 → 今开 138.45（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 139.98 ｜ 低 135.91

Options: P/C成交量 0.43 | OI比 0.56 | ATM IV 95.0% | Skew 2.2pp | Term 0.60 | ExpMove ±5.0%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.60，近月 IV 高于远月）｜保护溢价中性（Skew 2.2pp）｜存量 Call 偏重（OI比 0.56）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-18（2D）±5.0% ｜ 11-20（4D）±6.7% ｜ 11-23（7D）±7.0% ｜ 11-25（9D）±8.7%
   ⇒ IV–VIX Spread: +73.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -15,977,990 | GEX Change vs 上次快照 -20,301,182 | Flip: Primary Flip: 138.24（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 775 / LOW 251 / INVALID 522
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 138.24（全链重定价，覆盖 99%）
Put Wall 130（弱结构｜现价高于该位 5.6%）
最近结构参考: Flip 138（现价低于该位 0.7%）
量化视角： 负 Gamma（1598万，无历史分位）｜由正转负（2030万）｜现价位于 Flip 下方 0.73%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 130（Put Wall，弱结构）；上方 140（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 138（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-16 160.0C — Vol 63,634 | 最新价 $0.12 | OI 9440→60599 (ΔOI +51159张) | ΔOI/Volume 80.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增51159张（+541.9% vs前日OI），连续性待观察（方向未知）
11-16 124.0P — Vol 45,339 | 最新价 $0.24 | OI 107→39985 (ΔOI +39878张) | ΔOI/Volume 88.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增39878张（+37269.2% vs前日OI），连续性待观察（方向未知）
11-16 150.0C — Vol 29,393 | 最新价 $0.55 | OI 6672→23625 (ΔOI +16953张) | ΔOI/Volume 57.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16953张（+254.1% vs前日OI），连续性待观察（方向未知）
11-20 140.0P — Vol 10,796 | 最新价 $6.23 | OI 29672→36362 (ΔOI +6690张) | ΔOI/Volume 62.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6690张（+22.6% vs前日OI），连续性待观察（方向未知）
11-20 120.0P — Vol 9,090 | 最新价 $0.66 | OI 18817→25254 (ΔOI +6437张) | ΔOI/Volume 70.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6437张（+34.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 121,117 张（Put 53,005 / Call 68,112），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 146.0k / P 81.2k，今日成交量: C 63.0k / P 27.3k，平值价格ATM: C $1.35 / P $1.46 ｜ ATM IV 95.0%，预期波动 ±2.0%，Max Pain 140
Top ΔOI: C 160 +51,159 ｜ P 124 +39,878 ｜ C 150 +16,953

📆 Forward Expiration Structure

11-18  C +8.6k / P +4.5k ｜ Activity HIGH ｜ 2D
11-20  C +32.9k / P +48.1k ｜ Activity MEDIUM △ ｜ 4D
11-23  C +0.9k / P +2.0k ｜ Activity HIGH ｜ 7D
11-25  C +0.4k / P +1.4k ｜ Activity HIGH ｜ 9D

📆 11-18 Forward Structure
存量OI: C 22.6k / P 28.4k，今日变化ΔOI: C +8.6k / P +4.5k，平值价格ATM: C $3.50 / P $3.42 ｜ ATM IV 78.9%，净 delta 敞口 -4k shares
Top ΔOI: C 150 +2,112 ｜ P 133 +694
仓位参考: Max Pain 140 ｜ Call Wall 150（+9.3%）（OI 3.8k） ｜ Put Wall 135（-1.6%，弱）（OI 10.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 78.9%｜历史 Rank 94%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,640 股

11-20（MEDIUM △）Top ΔOI: 140P +6,690 ｜ 120P +6,437
11-20（MEDIUM △）仓位参考: Max Pain 145 ｜ Call Wall 145（+5.7%，弱）（OI 42.9k） ｜ Put Wall 140（+2.0%，弱）（OI 36.4k）

📆 11-23 Forward Structure
存量OI: C 4.5k / P 3.7k，今日变化ΔOI: C +0.9k / P +2.0k，平值价格ATM: C $4.80 / P $4.86 ｜ ATM IV 66.0%，净 delta 敞口 -21k shares
Top ΔOI: P 126 +1,576 ｜ C 146 +339 ｜ P 142 +101
仓位参考: Max Pain 141 ｜ Call Wall 150（+9.3%，弱）（OI 1.0k） ｜ Put Wall 126（-8.2%）（OI 1.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 66.0%｜历史 Rank 94%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 负 20,563 股

📆 11-25 Forward Structure
存量OI: C 1.8k / P 2.1k，今日变化ΔOI: C +0.4k / P +1.4k，平值价格ATM: C $7.20 / P $4.78 ｜ ATM IV 66.2%，净 delta 敞口 -35k shares
Top ΔOI: P 130 +1,301 ｜ C 140 +77
仓位参考: Max Pain 140 ｜ Call Wall 145（+5.7%，弱）（OI 0.4k） ｜ Put Wall 130（-5.3%）（OI 1.4k）
量化解读： 存量两侧均衡｜ATM IV 66.2%｜历史 Rank 94%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 负 34,676 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/SPCX_morning.json