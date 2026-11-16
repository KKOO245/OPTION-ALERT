# 期权晨报 2026-11-16（快照 10:20 ET）

📊 市场环境

SPY $744.62 ｜ QQQ $663.93
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
🔴 **事件差分**: 11-20（4D）ATM IV 130.5% vs 11-27 102.7%（差 +27.8pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 885.01 → 今开 827.49（-6.5%） | 较昨收变动（含盘初走势） ｜ 今日高 838.48 ｜ 低 799.00

Options: P/C成交量 0.67 | OI比 0.69 | ATM IV 130.5% | Skew 7.6pp | Term 0.73 | ExpMove ±11.3%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜保护溢价显著（Skew 7.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.69）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（4D）±11.3% ｜ 11-27（11D）±15.7% ｜ 12-04（18D）±16.8% ｜ 12-11（25D）±25.0%
   ⇒ IV–VIX Spread: +108.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,557,925 | GEX Change vs 上次快照 -58,372 | Flip: Primary Flip: 866.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1626 / LOW 733 / INVALID 1137
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 866.35（全链重定价，覆盖 100%）
最近结构参考: Flip 866（现价低于该位 5.6%）
量化视角： 负 Gamma（256万，无历史分位）｜负 Gamma 加深（6万）｜现价位于 Flip 下方 5.63%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,000（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 866（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 1000.0C — Vol 4,690 | 最新价 $13.19 | OI 2263→3798 (ΔOI +1535张) | ΔOI/Volume 32.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1535张（+67.8% vs前日OI），连续性待观察（方向未知）
12-18 1300.0C — Vol 1,314 | 最新价 $9.63 | OI 1182→2241 (ΔOI +1059张) | ΔOI/Volume 80.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1059张（+89.6% vs前日OI），连续性待观察（方向未知）
12-18 1200.0C — Vol 2,261 | 最新价 $16.32 | OI 800→1706 (ΔOI +906张) | ΔOI/Volume 40.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增906张（+113.2% vs前日OI），连续性待观察（方向未知）
11-20 1060.0C — Vol 1,894 | 最新价 $6.21 | OI 153→1017 (ΔOI +864张) | ΔOI/Volume 45.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增864张（+564.7% vs前日OI），连续性待观察（方向未知）
12-18 700.0P — Vol 884 | 最新价 $26.70 | OI 1868→2564 (ΔOI +696张) | ΔOI/Volume 78.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增696张（+37.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,060 张（Put 696 / Call 4,364），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +8.3k / P +1.6k ｜ Activity HIGH ｜ 4D
11-27  C +1.5k / P +0.7k ｜ Activity HIGH ｜ 11D
12-04  C +0.7k / P +0.2k ｜ Activity MEDIUM △ ｜ 18D
12-11  C +0.4k / P +0.2k ｜ Activity MEDIUM △ ｜ 25D

📆 11-20 Forward Structure
存量OI: C 87.3k / P 60.3k，今日变化ΔOI: C +8.3k / P +1.6k，平值价格ATM: C $43.65 / P $48.65 ｜ ATM IV 130.5%，净 delta 敞口 194k shares
Top ΔOI: C 1000 +1,535 ｜ C 1060 +864
仓位参考: Max Pain 1,000 ｜ Call Wall 800（-2.1%，弱）（OI 1.1k） ｜ Put Wall 870（+6.4%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 130.5%｜历史 Rank 85%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 194,409 股

📆 11-27 Forward Structure
存量OI: C 19.6k / P 10.5k，今日变化ΔOI: C +1.5k / P +0.7k，平值价格ATM: C $67.60 / P $60.80 ｜ ATM IV 102.7%，净 delta 敞口 22k shares
Top ΔOI: P 700 +216 ｜ C 950 +208 ｜ C 900 +167
仓位参考: Max Pain 1,025 ｜ Put Wall 800（-2.1%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 102.7%｜历史 Rank 85%（近端代理）｜IV/RV 0.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 21,825 股

12-04（MEDIUM △）Top ΔOI: 620P +107 ｜ 855C +59
12-04（MEDIUM △）仓位参考: Max Pain 960 ｜ Call Wall 855（+4.6%，弱）（OI 0.1k） ｜ Put Wall 820（+0.3%，弱）（OI 0.4k）

12-11（MEDIUM △）Top ΔOI: 850P +51
12-11（MEDIUM △）仓位参考: Max Pain 940 ｜ Put Wall 830（+1.5%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 11-20（4D）ATM IV 130.5% vs 11-27 102.7%（差 +27.8pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/SNDK_morning.json