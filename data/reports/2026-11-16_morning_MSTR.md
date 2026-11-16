# 期权晨报 2026-11-16（快照 10:20 ET）

📊 市场环境

SPY $744.62 ｜ QQQ $664.07
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
🔴 **事件差分**: 11-20（4D）ATM IV 107.8% vs 11-27 87.9%（差 +19.9pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-27 100P ΔOI +904（距现价 -4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 111.62 → 今开 103.74（-7.1%） | 较昨收变动（含盘初走势） ｜ 今日高 105.79 ｜ 低 102.22

Options: P/C成交量 0.72 | OI比 0.60 | ATM IV 107.8% | Skew 14.1pp | Term 0.78 | ExpMove ±9.3%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价显著（Skew 14.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.72×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（4D）±9.3% ｜ 11-27（11D）±12.2% ｜ 12-04（18D）±15.7% ｜ 12-11（25D）±18.4%
   ⇒ IV–VIX Spread: +86.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,539,398 | GEX Change vs 上次快照 762,497 | Flip: Primary Flip: 105.65（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 429 / LOW 171 / INVALID 350
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 105.65（全链重定价，覆盖 100%）
Put Wall 100（弱结构｜现价高于该位 4.5%）
最近结构参考: Flip 106（现价低于该位 1.1%）
量化视角： 负 Gamma（454万，无历史分位）｜负 Gamma 缓解（+76万）｜现价位于 Flip 下方 1.08%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 100（Put Wall，弱结构）；上方 116（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 106（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 65.0P — Vol 22,356 | 最新价 $0.06 | OI 3177→23097 (ΔOI +19920张) | ΔOI/Volume 89.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19920张（+627.0% vs前日OI），连续性待观察（方向未知）
11-20 114.0C — Vol 17,738 | 最新价 $3.76 | OI 0→17304 (ΔOI +17304张) | ΔOI/Volume 97.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17304张（前日OI缺失），连续性待观察（方向未知）
11-20 112.0C — Vol 18,674 | 最新价 $4.55 | OI 0→13943 (ΔOI +13943张) | ΔOI/Volume 74.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13943张（前日OI缺失），连续性待观察（方向未知）
11-20 117.0C — Vol 13,948 | 最新价 $2.61 | OI 112→13635 (ΔOI +13523张) | ΔOI/Volume 97.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13523张（+12074.1% vs前日OI），连续性待观察（方向未知）
11-20 119.0C — Vol 12,676 | 最新价 $1.97 | OI 1428→12819 (ΔOI +11391张) | ΔOI/Volume 89.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11391张（+797.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 76,081 张（Put 19,920 / Call 56,161），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +71.4k / P +42.2k ｜ Activity HIGH ｜ 4D
11-27  C +9.0k / P +6.6k ｜ Activity HIGH ｜ 11D
12-04  C +1.3k / P +6.2k ｜ Activity MEDIUM △ ｜ 18D
12-11  C +0.2k / P +4.1k ｜ Activity MEDIUM △ ｜ 25D

📆 11-20 Forward Structure
存量OI: C 328.5k / P 198.0k，今日变化ΔOI: C +71.4k / P +42.2k，平值价格ATM: C $4.45 / P $5.30 ｜ ATM IV 107.8%，净 delta 敞口 1.5M shares
Top ΔOI: P 65 +19,920 ｜ C 114 +17,304 ｜ C 112 +13,943
仓位参考: Max Pain 116 ｜ Call Wall 114（+9.1%，弱）（OI 17.3k） ｜ Put Wall 100（-4.3%，弱）（OI 17.9k）
量化解读： 存量 Call 重｜ATM IV 107.8%｜历史 Rank 86%（近端代理）｜IV/RV 1.69×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,514,947 股

📆 11-27 Forward Structure
存量OI: C 29.8k / P 61.9k，今日变化ΔOI: C +9.0k / P +6.6k，平值价格ATM: C $6.00 / P $6.71 ｜ ATM IV 87.9%，净 delta 敞口 536k shares
Top ΔOI: C 40 +5,965 ｜ P 100 +904 ｜ P 90 +872
仓位参考: Max Pain 135 ｜ Put Wall 95（-9.1%，弱）（OI 6.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 87.9%｜历史 Rank 86%（近端代理）｜IV/RV 1.38×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 536,247 股

12-04（MEDIUM △）Top ΔOI: 105P +1,273 ｜ 85P +682
12-04（MEDIUM △）仓位参考: Max Pain 145 ｜ Put Wall 100（-4.3%，弱）（OI 2.3k）

12-11（MEDIUM △）Top ΔOI: 70P +563 ｜ 80P +542
12-11（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 100（-4.3%，弱）（OI 0.1k） ｜ Put Wall 100（-4.3%，弱）（OI 1.2k）

📅 事件差分（观察，非因果）: 11-20（4D）ATM IV 107.8% vs 11-27 87.9%（差 +19.9pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/MSTR_morning.json