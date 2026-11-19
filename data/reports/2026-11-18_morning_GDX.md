# 期权晨报 2026-11-18（快照 10:20 ET）

📊 市场环境

SPY $735.61 ｜ QQQ $nan
VIX 24.58 ↓3.5%（5D +40.5%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **事件差分**: 11-20 ATM IV 62.7% vs 11-23 50.8%（差 +12.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-23 72P ΔOI +605（距现价 -4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-23 72P ΔOI +605 占该期限总 OI 28.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 79.57 → 今开 76.81（-3.5%） | 较昨收变动（含盘初走势） ｜ 今日高 76.82 ｜ 低 74.45

Options: P/C成交量 0.90 | OI比 0.96 | ATM IV 80.5% | Skew 3.3pp | Term 0.59 | ExpMove ±4.0%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.59，近月 IV 高于远月）｜保护溢价中性（Skew 3.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.90×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.96×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（2D）±4.0% ｜ 11-23（5D）±5.0% ｜ 11-25（7D）±2.3% ｜ 11-27（9D）±6.4%
   ⇒ IV–VIX Spread: +56.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -68,880,730 | GEX Change vs 上次快照 -11,892,407 | Flip: Primary Flip: 79.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 513 / LOW 236 / INVALID 541
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 79.41（全链重定价，覆盖 89%）
Put Wall 75（弱结构｜现价低于该位 0.0%）
最近结构参考: Put Wall 75（现价低于该位 0.0%）
量化视角： 负 Gamma（6888万，无历史分位）｜负 Gamma 加深（1189万）｜现价位于 Flip 下方 5.57%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 75（Put Wall，弱结构） / 80（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 79（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 81.0C — Vol 5,154 | 最新价 $0.95 | OI 931→5700 (ΔOI +4769张) | ΔOI/Volume 92.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4769张（+512.2% vs前日OI），连续性待观察（方向未知）
12-18 90.0C — Vol 5,417 | 最新价 $1.10 | OI 15433→19786 (ΔOI +4353张) | ΔOI/Volume 80.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4353张（+28.2% vs前日OI），连续性待观察（方向未知）
12-18 66.0P — Vol 2,467 | 最新价 $0.56 | OI 233→2510 (ΔOI +2277张) | ΔOI/Volume 92.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2277张（+977.2% vs前日OI），连续性待观察（方向未知）
11-18 83.0C — Vol 2,208 | 最新价 $0.08 | OI 316→2453 (ΔOI +2137张) | ΔOI/Volume 96.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2137张（+676.3% vs前日OI），连续性待观察（方向未知）
12-18 84.0C — Vol 2,817 | 最新价 $2.54 | OI 8023→9336 (ΔOI +1313张) | ΔOI/Volume 46.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1313张（+16.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,849 张（Put 2,277 / Call 12,572），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 5.8k / P 5.5k，今日成交量: C 2.0k / P 1.8k，平值价格ATM: C $0.62 / P $0.65 ｜ ATM IV 80.5%，预期波动 ±1.7%，Max Pain 80
Top ΔOI: C 83 +2,137 ｜ P 72 +551 ｜ P 78 +472

📆 Forward Expiration Structure

11-20  C +6.8k / P -1.4k ｜ Activity HIGH ｜ 2D
11-23  C +0.4k / P +0.7k ｜ Activity HIGH ｜ 5D
11-25  C +0.3k / P +26 ｜ Activity MEDIUM △ ｜ 7D
11-27  C +1.9k / P +0.2k ｜ Activity MEDIUM △ ｜ 9D

📆 11-20 Forward Structure
存量OI: C 176.9k / P 180.2k，今日变化ΔOI: C +6.8k / P -1.4k，平值价格ATM: C $1.53 / P $1.50 ｜ ATM IV 62.7%，净 delta 敞口 261k shares
Top ΔOI: C 81 +4,769 ｜ P 70 +901 ｜ P 79 -610
仓位参考: Max Pain 84 ｜ Put Wall 75（+0.0%，弱）（OI 12.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 62.7%｜历史 Rank 100%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 260,508 股

📆 11-23 Forward Structure
存量OI: C 0.9k / P 1.2k，今日变化ΔOI: C +0.4k / P +0.7k，平值价格ATM: C $2.15 / P $1.61 ｜ ATM IV 50.8%，净 delta 敞口 -16k shares
Top ΔOI: P 72 +605
仓位参考: Max Pain 83 ｜ Put Wall 72（-4.0%）（OI 0.6k）
量化解读： 存量 Put 重｜ATM IV 50.8%｜历史 Rank 100%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 16,066 股

11-25（MEDIUM △）Top ΔOI: 82C +134
11-25（MEDIUM △）仓位参考: Max Pain 83 ｜ Put Wall 78（+4.0%，弱）（OI 81）

11-27（MEDIUM △）仓位参考: Max Pain 83 ｜ Put Wall 75（+0.0%，弱）（OI 1.2k）

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 62.7% vs 11-23 50.8%（差 +12.0pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/GDX_morning.json