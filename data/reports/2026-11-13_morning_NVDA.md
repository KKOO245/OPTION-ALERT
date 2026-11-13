# 期权晨报 2026-11-13（快照 10:20 ET）

📊 市场环境

SPY $750.14 ｜ QQQ $679.89
VIX 19.65 ↑5.1%（5D -23.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-16 160P ΔOI +6,723（距现价 -1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 166.19 → 今开 169.89（+2.2%） | 较昨收变动（含盘初走势） ｜ 今日高 170.00 ｜ 低 159.33

Options: P/C成交量 1.15 | OI比 0.75 | ATM IV 100.8% | Skew -0.8pp | Term 0.56 | ExpMove ±4.3%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.56，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.75）+ 当日成交偏 Put（P/C量 1.15）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.15×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-16（3D）±4.3% ｜ 11-18（5D）±9.3% ｜ 11-20（7D）±10.2% ｜ 11-23（10D）±10.6%
   ⇒ IV–VIX Spread: +81.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -8,542,633 | GEX Change vs 上次快照 93,475,301 | Flip: Primary Flip: 162.28（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1237 / LOW 276 / INVALID 707
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 162.28（全链重定价，覆盖 98%）
Put Wall 150（弱结构｜现价高于该位 8.0%）
最近结构参考: Flip 162（现价低于该位 0.2%）
量化视角： 负 Gamma（854万，无历史分位）｜负 Gamma 缓解（+9348万）｜现价位于 Flip 下方 0.22%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall，弱结构）；上方 168（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 162（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 150.0P — Vol 213,678 | 最新价 $0.16 | OI 17291→53411 (ΔOI +36120张) | ΔOI/Volume 16.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增36120张（+208.9% vs前日OI），连续性待观察（方向未知）
11-13 175.0C — Vol 173,341 | 最新价 $0.58 | OI 17745→50953 (ΔOI +33208张) | ΔOI/Volume 19.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33208张（+187.1% vs前日OI），连续性待观察（方向未知）
12-18 170.0C — Vol 40,582 | 最新价 $10.60 | OI 11584→42065 (ΔOI +30481张) | ΔOI/Volume 75.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30481张（+263.1% vs前日OI），连续性待观察（方向未知）
11-13 170.0C — Vol 243,513 | 最新价 $1.63 | OI 9217→38052 (ΔOI +28835张) | ΔOI/Volume 11.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增28835张（+312.9% vs前日OI），连续性待观察（方向未知）
11-13 165.0C — Vol 265,253 | 最新价 $3.77 | OI 3018→31509 (ΔOI +28491张) | ΔOI/Volume 10.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增28491张（+944.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 157,135 张（Put 36,120 / Call 121,015），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 758.4k / P 572.4k，今日成交量: C 379.1k / P 436.1k，平值价格ATM: C $1.73 / P $1.81 ｜ ATM IV 100.8%，预期波动 ±2.2%，Max Pain 168
Top ΔOI: P 150 +36,120 ｜ C 175 +33,208 ｜ C 170 +28,835

📆 Forward Expiration Structure

11-16  C +52.9k / P +64.1k ｜ Activity HIGH ｜ 3D
11-18  C +43.4k / P +36.9k ｜ Activity HIGH ｜ 5D
11-20  C +132.2k / P +79.7k ｜ Activity MEDIUM △ ｜ 7D
11-23  C +10.2k / P +3.8k ｜ Activity HIGH ｜ 10D

📆 11-16 Forward Structure
存量OI: C 175.2k / P 121.0k，今日变化ΔOI: C +52.9k / P +64.1k，平值价格ATM: C $3.45 / P $3.51 ｜ ATM IV 57.1%，净 delta 敞口 634k shares
Top ΔOI: P 150 +10,305 ｜ P 160 +6,723 ｜ P 140 +6,659
仓位参考: Max Pain 168 ｜ Call Wall 170（+5.0%，弱）（OI 9.0k） ｜ Put Wall 150（-7.4%，弱）（OI 13.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 57.1%｜历史 Rank 96%（近端代理）｜IV/RV 1.07×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 634,201 股

📆 11-18 Forward Structure
存量OI: C 130.6k / P 87.3k，今日变化ΔOI: C +43.4k / P +36.9k，平值价格ATM: C $7.55 / P $7.50 ｜ ATM IV 97.3%，净 delta 敞口 546k shares
Top ΔOI: C 180 +9,361 ｜ P 150 +7,905 ｜ C 170 +3,644
仓位参考: Max Pain 170 ｜ Call Wall 175（+8.1%，弱）（OI 9.4k） ｜ Put Wall 150（-7.4%）（OI 10.4k）
量化解读： 存量 Call 重｜ATM IV 97.3%｜历史 Rank 96%（近端代理）｜IV/RV 1.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 545,573 股

11-20（MEDIUM △）Top ΔOI: 172C +22,378 ｜ 180C +22,298
11-20（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 175（+8.1%，弱）（OI 35.8k） ｜ Put Wall 150（-7.4%，弱）（OI 42.1k）

📆 11-23 Forward Structure
存量OI: C 29.0k / P 16.6k，今日变化ΔOI: C +10.2k / P +3.8k，平值价格ATM: C $8.65 / P $8.55 ｜ ATM IV 78.9%，净 delta 敞口 214k shares
Top ΔOI: C 165 +1,331 ｜ C 160 +1,121 ｜ C 180 +996
仓位参考: Max Pain 168 ｜ Call Wall 170（+5.0%，弱）（OI 2.1k） ｜ Put Wall 150（-7.4%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 78.9%｜历史 Rank 96%（近端代理）｜IV/RV 1.48×（近似）｜净 delta 敞口 正 213,901 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/NVDA_morning.json