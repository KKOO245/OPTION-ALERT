# 期权晨报 2026-10-15（快照 10:20 ET）

📊 市场环境

SPY $771.79 ｜ QQQ $728.00
VIX 17.51 ↑3.8%（5D +13.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览
🟡 **事件差分**: 10-16 ATM IV 54.1% vs 10-19 40.0%（差 +14.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-19 87C ΔOI +597（距现价 +3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-19 87C ΔOI +597 占该期限总 OI 17.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 83.40 → 今开 84.78（+1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 84.90 ｜ 低 84.12

Options: P/C成交量 0.33 | OI比 0.67 | ATM IV 54.1% | Skew 1.8pp | Term 0.82 | ExpMove ±2.6%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价薄（Skew 1.8pp）｜存量 Call 偏重（OI比 0.67）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.33×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.67×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（1D）±2.6% ｜ 10-19（4D）±3.3% ｜ 10-21（6D）±4.8% ｜ 10-23（8D）±4.9%
   ⇒ IV–VIX Spread: +36.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -50,702,927 | GEX Change vs 上次快照 24,009,277 | Flip: Primary Flip: 87.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 608 / LOW 183 / INVALID 385
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 87.02（全链重定价，覆盖 90%）
Put Wall 80（弱结构｜现价高于该位 5.4%）
最近结构参考: Flip 87（现价低于该位 3.1%）
量化视角： 负 Gamma（5070万，无历史分位）｜负 Gamma 缓解（+2401万）｜现价位于 Flip 下方 3.08%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（Put Wall，弱结构）；上方 88（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 87（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 86.0C — Vol 3,278 | 最新价 $1.11 | OI 153→3316 (ΔOI +3163张) | ΔOI/Volume 96.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3163张（+2067.3% vs前日OI），连续性待观察（方向未知）
10-23 78.0P — Vol 3,258 | 最新价 $0.50 | OI 228→3370 (ΔOI +3142张) | ΔOI/Volume 96.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3142张（+1378.1% vs前日OI），连续性待观察（方向未知）
10-16 85.0C — Vol 3,458 | 最新价 $0.57 | OI 1843→3405 (ΔOI +1562张) | ΔOI/Volume 45.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1562张（+84.8% vs前日OI），连续性待观察（方向未知）
10-16 86.0C — Vol 3,082 | 最新价 $0.53 | OI 1422→2754 (ΔOI +1332张) | ΔOI/Volume 43.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1332张（+93.7% vs前日OI），连续性待观察（方向未知）
10-21 80.0P — Vol 1,263 | 最新价 $0.68 | OI 21→1133 (ΔOI +1112张) | ΔOI/Volume 88.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1112张（+5295.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 10,311 张（Put 4,254 / Call 6,057），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C -19.9k / P -13.1k ｜ Activity MEDIUM △ ｜ 1D
10-19  C +0.9k / P +0.1k ｜ Activity HIGH ｜ 4D
10-21  C +0.3k / P +1.3k ｜ Activity HIGH ｜ 6D
10-23  C +4.4k / P +4.1k ｜ Activity HIGH ｜ 8D

📆 10-16 Forward Structure
存量OI: C 172.3k / P 115.2k，今日变化ΔOI: C -19.9k / P -13.1k，平值价格ATM: C $1.37 / P $0.80 ｜ ATM IV 54.1%，净 delta 敞口 1.2M shares
Top ΔOI: C 90 -8,739 ｜ P 95 -5,099
仓位参考: Max Pain 88 ｜ Call Wall 88.5（+4.9%，弱）（OI 9.1k） ｜ Put Wall 85（+0.8%，弱）（OI 10.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 54.1%｜历史 Rank 87%（近端代理）｜IV/RV 1.42×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,242,594 股

📆 10-19 Forward Structure
存量OI: C 2.7k / P 0.8k，今日变化ΔOI: C +0.9k / P +0.1k，平值价格ATM: C $1.57 / P $1.18 ｜ ATM IV 40.0%，净 delta 敞口 22k shares
Top ΔOI: C 87 +597 ｜ C 89 +214 ｜ C 85 +129
仓位参考: Max Pain 87 ｜ Call Wall 87（+3.2%，弱）（OI 0.6k） ｜ Put Wall 89（+5.5%）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 40.0%｜历史 Rank 87%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 正 22,201 股

📆 10-21 Forward Structure
存量OI: C 2.9k / P 3.8k，今日变化ΔOI: C +0.3k / P +1.3k，平值价格ATM: C $2.20 / P $1.88 ｜ ATM IV 37.2%，净 delta 敞口 -10k shares
Top ΔOI: P 80 +1,112 ｜ C 87 +212 ｜ P 77 +126
仓位参考: Max Pain 83 ｜ Put Wall 79（-6.3%）（OI 2.4k）
量化解读： 存量 Put 重｜ATM IV 37.2%｜历史 Rank 87%（近端代理）｜IV/RV 0.98×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 10,024 股

📆 10-23 Forward Structure
存量OI: C 15.4k / P 18.0k，今日变化ΔOI: C +4.4k / P +4.1k，平值价格ATM: C $2.30 / P $1.84 ｜ ATM IV 41.7%，净 delta 敞口 168k shares
Top ΔOI: C 86 +3,163 ｜ P 78 +3,142 ｜ P 81 +565
仓位参考: Max Pain 86 ｜ Call Wall 86（+2.0%）（OI 3.3k） ｜ Put Wall 85（+0.8%，弱）（OI 1.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 41.7%｜历史 Rank 87%（近端代理）｜IV/RV 1.10×（近似）｜净 delta 敞口 正 168,419 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 54.1% vs 10-19 40.0%（差 +14.1pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/GDX_morning.json