# 期权晨报 2026-11-12（快照 10:20 ET）

📊 市场环境

SPY $757.88 ｜ QQQ $688.17
VIX 18.45 ↑5.5%（5D -34.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **事件差分**: 11-13（1D）ATM IV 103.8% vs 11-20 83.8%（差 +20.1pp），覆盖 成屋销售、PPI 生产者物价 MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 122.35 → 今开 114.07（-6.8%） | 较昨收变动（含盘初走势） ｜ 今日高 115.00 ｜ 低 112.32

Options: P/C成交量 0.19 | OI比 0.62 | ATM IV 103.8% | Skew 3.6pp | Term 0.75 | ExpMove ±4.8%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜保护溢价中性（Skew 3.6pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.19×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±4.8% ｜ 11-20（8D）±10.2% ｜ 11-27（15D）±12.6% ｜ 12-04（22D）±15.4%
   ⇒ IV–VIX Spread: +85.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -36,665,624 | GEX Change vs 上次快照 -36,219,359 | Flip: Primary Flip: 120.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 512 / LOW 191 / INVALID 289
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 120.35（全链重定价，覆盖 99%）
最近结构参考: Flip 120（现价低于该位 5.8%）
量化视角： 负 Gamma（3667万，无历史分位）｜负 Gamma 加深（3622万）｜现价位于 Flip 下方 5.76%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 125（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 120（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 139.0C — Vol 4,893 | 最新价 $0.11 | OI 42407→44345 (ΔOI +1938张) | ΔOI/Volume 39.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1938张（+4.6% vs前日OI），连续性待观察（方向未知）
11-13 130.0C — Vol 6,680 | 最新价 $0.93 | OI 3475→5302 (ΔOI +1827张) | ΔOI/Volume 27.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1827张（+52.6% vs前日OI），连续性待观察（方向未知）
11-13 125.0C — Vol 7,471 | 最新价 $2.25 | OI 2939→4371 (ΔOI +1432张) | ΔOI/Volume 19.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1432张（+48.7% vs前日OI），连续性待观察（方向未知）
11-13 120.0P — Vol 5,942 | 最新价 $2.35 | OI 2142→3407 (ΔOI +1265张) | ΔOI/Volume 21.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1265张（+59.1% vs前日OI），连续性待观察（方向未知）
11-20 60.0P — Vol 1,614 | 最新价 $0.05 | OI 2392→3639 (ΔOI +1247张) | ΔOI/Volume 77.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1247张（+52.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,709 张（Put 2,512 / Call 5,197），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C -9.7k / P -3.3k ｜ Activity HIGH ｜ 1D
11-20  C +5.1k / P +2.8k ｜ Activity HIGH ｜ 8D
11-27  C +1.4k / P +6.0k ｜ Activity MEDIUM △ ｜ 15D
12-04  C +0.7k / P +4.9k ｜ Activity MEDIUM △ ｜ 22D

📆 11-13 Forward Structure
存量OI: C 229.7k / P 141.3k，今日变化ΔOI: C -9.7k / P -3.3k，平值价格ATM: C $3.00 / P $2.46 ｜ ATM IV 103.8%，净 delta 敞口 296k shares
仓位参考: Max Pain 125 ｜ Put Wall 110（-3.0%，弱）（OI 5.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 103.8%｜历史 Rank 84%（近端代理）｜IV/RV 1.54×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 295,786 股

📆 11-20 Forward Structure
存量OI: C 172.4k / P 160.6k，今日变化ΔOI: C +5.1k / P +2.8k，平值价格ATM: C $5.18 / P $6.36 ｜ ATM IV 83.8%，净 delta 敞口 243k shares
Top ΔOI: P 120 -798 ｜ C 130 +767
仓位参考: Max Pain 135 ｜ Put Wall 110（-3.0%，弱）（OI 15.6k）
量化解读： 存量两侧均衡｜ATM IV 83.8%｜历史 Rank 84%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 242,874 股

11-27（MEDIUM △）Top ΔOI: 100P +672 ｜ 95P +652
11-27（MEDIUM △）仓位参考: Max Pain 150 ｜ Put Wall 115（+1.4%，弱）（OI 2.0k）

12-04（MEDIUM △）Top ΔOI: 90P +693
12-04（MEDIUM △）仓位参考: Max Pain 150

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 103.8% vs 11-20 83.8%（差 +20.1pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/MSTR_morning.json