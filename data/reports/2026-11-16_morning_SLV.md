# 期权晨报 2026-11-16（快照 10:20 ET）

📊 市场环境

SPY $744.62 ｜ QQQ $663.96
VIX 21.57 ↑11.8%（5D +8.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 35.1（fear）
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
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-20 44P ΔOI +3,818（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-18 48C ΔOI +4,035 占该期限总 OI 11.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 44.13 → 今开 42.59（-3.5%） | 较昨收变动（含盘初走势） ｜ 今日高 42.92 ｜ 低 42.15

Options: P/C成交量 0.40 | OI比 0.60 | ATM IV 52.2% | Skew 2.5pp | Term 0.86 | ExpMove ±3.4%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价中性（Skew 2.5pp）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.40×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-18（2D）±3.4% ｜ 11-20（4D）±4.5% ｜ 11-23（7D）±5.2% ｜ 11-25（9D）±6.2%
   ⇒ IV–VIX Spread: +30.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -27,799,114 | GEX Change vs 上次快照 -21,814,714 | Flip: Primary Flip: 43.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 661 / LOW 158 / INVALID 391
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 43.68（全链重定价，覆盖 97%）
Put Wall 40（弱结构｜现价高于该位 6.3%）
最近结构参考: Flip 44（现价低于该位 2.7%）
量化视角： 负 Gamma（2780万，无历史分位）｜负 Gamma 加深（2181万）｜现价位于 Flip 下方 2.67%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 40（Put Wall，弱结构）；上方 44（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 44（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 52.0C — Vol 12,958 | 最新价 $0.32 | OI 38220→50266 (ΔOI +12046张) | ΔOI/Volume 93.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12046张（+31.5% vs前日OI），连续性待观察（方向未知）
11-18 48.0C — Vol 4,292 | 最新价 $0.03 | OI 157→4192 (ΔOI +4035张) | ΔOI/Volume 94.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4035张（+2570.1% vs前日OI），连续性待观察（方向未知）
11-20 44.5P — Vol 4,277 | 最新价 $1.19 | OI 625→4443 (ΔOI +3818张) | ΔOI/Volume 89.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3818张（+610.9% vs前日OI），连续性待观察（方向未知）
11-16 41.0P — Vol 3,832 | 最新价 $0.01 | OI 249→4050 (ΔOI +3801张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3801张（+1526.5% vs前日OI），连续性待观察（方向未知）
11-20 45.0P — Vol 5,062 | 最新价 $1.51 | OI 11528→14580 (ΔOI +3052张) | ΔOI/Volume 60.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3052张（+26.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 26,752 张（Put 10,671 / Call 16,081），跨 4 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜彩票/名义 1 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 21.8k / P 13.2k，今日成交量: C 11.9k / P 4.7k，平值价格ATM: C $0.21 / P $0.27 ｜ ATM IV 52.2%，预期波动 ±1.1%，Max Pain 44
Top ΔOI: P 41 +3,801 ｜ C 45 +1,695 ｜ C 44 +1,574

📆 Forward Expiration Structure

11-18  C +10.9k / P +3.2k ｜ Activity HIGH ｜ 2D
11-20  C -1.7k / P +9.2k ｜ Activity HIGH ｜ 4D
11-23  C +0.9k / P +0.4k ｜ Activity HIGH ｜ 7D
11-25  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 9D

📆 11-18 Forward Structure
存量OI: C 22.1k / P 12.0k，今日变化ΔOI: C +10.9k / P +3.2k，平值价格ATM: C $0.71 / P $0.72 ｜ ATM IV 53.7%，净 delta 敞口 -49k shares
仓位参考: Max Pain 45 ｜ Put Wall 40（-5.9%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 53.7%｜历史 Rank 86%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 49,040 股

📆 11-20 Forward Structure
存量OI: C 571.2k / P 156.3k，今日变化ΔOI: C -1.7k / P +9.2k，平值价格ATM: C $0.95 / P $0.98 ｜ ATM IV 53.7%，净 delta 敞口 -517k shares
Top ΔOI: P 44 +3,818 ｜ P 45 +3,052
仓位参考: Max Pain 50 ｜ Put Wall 45（+5.9%，弱）（OI 14.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 53.7%｜历史 Rank 86%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 516,805 股

📆 11-23 Forward Structure
存量OI: C 7.3k / P 1.3k，今日变化ΔOI: C +0.9k / P +0.4k，平值价格ATM: C $1.12 / P $1.07 ｜ ATM IV 47.1%，净 delta 敞口 2k shares
Top ΔOI: P 40 +236 ｜ C 44 +108
仓位参考: Max Pain 44 ｜ Call Wall 46.5（+9.4%，弱）（OI 1.9k） ｜ Put Wall 40（-5.9%）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 47.1%｜历史 Rank 86%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 正 1,793 股

11-25（MEDIUM △）Top ΔOI: 44P +159
11-25（MEDIUM △）仓位参考: Max Pain 45 ｜ Call Wall 45（+5.9%，弱）（OI 60） ｜ Put Wall 44.5（+4.7%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/SLV_morning.json