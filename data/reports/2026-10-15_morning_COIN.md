# 期权晨报 2026-10-15（快照 10:20 ET）

📊 市场环境

SPY $771.47 ｜ QQQ $728.00
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
🔴 **事件差分**: 10-16（1D）ATM IV 79.1% vs 10-23 64.0%（差 +15.1pp），覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-16 165P ΔOI -1,140（距现价 -2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 172.89 → 今开 167.84（-2.9%） | 较昨收变动（含盘初走势） ｜ 今日高 171.87 ｜ 低 165.80

Options: P/C成交量 0.36 | OI比 0.79 | ATM IV 79.1% | Skew 1.7pp | Term 0.86 | ExpMove ±4.0%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价薄（Skew 1.7pp）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（1D）±4.0% ｜ 10-23（8D）±7.9% ｜ 10-30（15D）±12.2% ｜ 11-06（22D）±14.9%
   ⇒ IV–VIX Spread: +61.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -11,645,874 | GEX Change vs 上次快照 -10,175,301 | Flip: Primary Flip: 172.22（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 438 / LOW 132 / INVALID 252
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 172.22（全链重定价，覆盖 97%）
最近结构参考: Flip 172（现价低于该位 2.1%）
量化视角： 负 Gamma（1165万，无历史分位）｜负 Gamma 加深（1018万）｜现价位于 Flip 下方 2.14%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 178（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 172（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 190.0C — Vol 4,738 | 最新价 $0.30 | OI 6106→8470 (ΔOI +2364张) | ΔOI/Volume 49.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2364张（+38.7% vs前日OI），连续性待观察（方向未知）
10-30 150.0P — Vol 523 | 最新价 $2.19 | OI 865→1261 (ΔOI +396张) | ΔOI/Volume 75.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增396张（+45.8% vs前日OI），连续性待观察（方向未知）
10-16 172.5P — Vol 1,819 | 最新价 $3.60 | OI 1155→1531 (ΔOI +376张) | ΔOI/Volume 20.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增376张（+32.5% vs前日OI），连续性待观察（方向未知）
10-23 180.0C — Vol 714 | 最新价 $3.91 | OI 428→788 (ΔOI +360张) | ΔOI/Volume 50.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增360张（+84.1% vs前日OI），连续性待观察（方向未知）
10-23 215.0C — Vol 388 | 最新价 $0.22 | OI 342→671 (ΔOI +329张) | ΔOI/Volume 84.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增329张（+96.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,825 张（Put 772 / Call 3,053），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C -96 / P -2.7k ｜ Activity HIGH ｜ 1D
10-23  C +1.8k / P +1.5k ｜ Activity HIGH ｜ 8D
10-30  C +1.1k / P +0.7k ｜ Activity HIGH ｜ 15D
11-06  C +0.7k / P +0.5k ｜ Activity MEDIUM △ ｜ 22D

📆 10-16 Forward Structure
存量OI: C 139.3k / P 110.3k，今日变化ΔOI: C -96 / P -2.7k，平值价格ATM: C $4.30 / P $2.45 ｜ ATM IV 79.1%，净 delta 敞口 163k shares
Top ΔOI: P 165 -1,140
仓位参考: Max Pain 178 ｜ Call Wall 185（+9.8%，弱）（OI 10.7k） ｜ Put Wall 165（-2.1%，弱）（OI 8.0k）
量化解读： 存量 Call 重｜ATM IV 79.1%｜历史 Rank 60%（近端代理）｜IV/RV 2.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 163,430 股

📆 10-23 Forward Structure
存量OI: C 15.4k / P 20.8k，今日变化ΔOI: C +1.8k / P +1.5k，平值价格ATM: C $7.05 / P $6.20 ｜ ATM IV 64.0%，净 delta 敞口 -5k shares
Top ΔOI: C 180 +360 ｜ P 165 +254
仓位参考: Max Pain 182 ｜ Call Wall 180（+6.8%，弱）（OI 0.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 64.0%｜历史 Rank 60%（近端代理）｜IV/RV 1.76×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 4,990 股

📆 10-30 Forward Structure
存量OI: C 13.4k / P 11.9k，今日变化ΔOI: C +1.1k / P +0.7k，平值价格ATM: C $10.58 / P $10.05 ｜ ATM IV 74.6%，净 delta 敞口 26k shares
Top ΔOI: P 150 +396 ｜ C 180 +262 ｜ C 200 +247
仓位参考: Max Pain 185 ｜ Call Wall 185（+9.8%，弱）（OI 1.4k） ｜ Put Wall 180（+6.8%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 74.6%｜历史 Rank 60%（近端代理）｜IV/RV 2.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 25,944 股

11-06（MEDIUM △）Top ΔOI: 160C +205 ｜ 175C +177
11-06（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 175（+3.8%，弱）（OI 0.2k） ｜ Put Wall 170（+0.9%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 79.1% vs 10-23 64.0%（差 +15.1pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/COIN_morning.json