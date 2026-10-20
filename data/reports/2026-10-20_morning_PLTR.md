# 期权晨报 2026-10-20（快照 10:20 ET）

📊 市场环境

SPY $769.68 ｜ QQQ $718.12
VIX 18.12 ↓1.7%（5D +18.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 190P ΔOI +2,683（距现价 -1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 194.15 → 今开 192.18（-1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 194.90 ｜ 低 189.42

Options: P/C成交量 1.04 | OI比 0.91 | ATM IV 56.0% | Skew 5.4pp | Term 1.13 | ExpMove ±4.2%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构正常（Term 1.13）｜保护溢价中性（Skew 5.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.04×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.91×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（3D）±4.2% ｜ 10-30（10D）±6.7% ｜ 11-06（17D）±12.7% ｜ 11-13（24D）±13.9%
   ⇒ IV–VIX Spread: +37.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 33,851,462 | GEX Change vs 上次快照 -5,431,139 | Flip: Primary Flip: 185.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 675 / LOW 59 / INVALID 178
结构观察区: Primary Flip 185.34（全链重定价，覆盖 100%）
Put Wall 190（弱结构｜现价高于该位 1.8%） | Call Wall 200（弱结构｜现价低于该位 3.3%）
最近结构参考: Put Wall 190（现价高于该位 1.8%）
量化视角： 正 Gamma（3385万，无历史分位）｜正 Gamma 减弱（543万）｜现价位于 Flip 上方 4.31%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（Put Wall，弱结构） / 190（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 185（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 205.0C — Vol 21,128 | 最新价 $0.85 | OI 7831→16138 (ΔOI +8307张) | ΔOI/Volume 39.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8307张（+106.1% vs前日OI），连续性待观察（方向未知）
10-23 207.5C — Vol 15,074 | 最新价 $0.55 | OI 5833→13715 (ΔOI +7882张) | ΔOI/Volume 52.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7882张（+135.1% vs前日OI），连续性待观察（方向未知）
10-30 167.5P — Vol 6,883 | 最新价 $0.69 | OI 789→5779 (ΔOI +4990张) | ΔOI/Volume 72.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4990张（+632.5% vs前日OI），连续性待观察（方向未知）
10-30 165.0P — Vol 6,861 | 最新价 $0.59 | OI 2245→6956 (ΔOI +4711张) | ΔOI/Volume 68.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4711张（+209.8% vs前日OI），连续性待观察（方向未知）
10-30 162.5P — Vol 5,069 | 最新价 $0.52 | OI 811→5354 (ΔOI +4543张) | ΔOI/Volume 89.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4543张（+560.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 30,433 张（Put 14,244 / Call 16,189），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +20.3k / P +14.7k ｜ Activity HIGH ｜ 3D
10-30  C +3.1k / P +27.7k ｜ Activity HIGH ｜ 10D
11-06  C +2.4k / P +3.0k ｜ Activity MEDIUM △ ｜ 17D
11-13  C +0.5k / P +1.9k ｜ Activity HIGH ｜ 24D

📆 10-23 Forward Structure
存量OI: C 127.6k / P 115.7k，今日变化ΔOI: C +20.3k / P +14.7k，平值价格ATM: C $4.19 / P $3.95 ｜ ATM IV 56.0%，净 delta 敞口 -165k shares
Top ΔOI: C 205 +8,307 ｜ C 207 +7,882 ｜ P 190 +2,683
仓位参考: Max Pain 190 ｜ Call Wall 205（+6.0%，弱）（OI 16.1k） ｜ Put Wall 190（-1.7%，弱）（OI 6.4k）
量化解读： 存量两侧均衡｜ATM IV 56.0%｜历史 Rank 87%（近端代理）｜IV/RV 1.36×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 164,715 股

📆 10-30 Forward Structure
存量OI: C 48.4k / P 76.3k，今日变化ΔOI: C +3.1k / P +27.7k，平值价格ATM: C $6.75 / P $6.16 ｜ ATM IV 50.5%，净 delta 敞口 -189k shares
Top ΔOI: P 167 +4,990 ｜ P 165 +4,711 ｜ P 162 +4,543
仓位参考: Max Pain 190 ｜ Call Wall 200（+3.5%，弱）（OI 3.7k） ｜ Put Wall 190（-1.7%，弱）（OI 6.9k）
量化解读： 存量 Put 重｜ATM IV 50.5%｜历史 Rank 87%（近端代理）｜IV/RV 1.23×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 188,548 股

11-06（MEDIUM △）Top ΔOI: 145P +570 ｜ 165P +356
11-06（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 205（+6.0%，弱）（OI 1.6k） ｜ Put Wall 190（-1.7%，弱）（OI 3.0k）

📆 11-13 Forward Structure
存量OI: C 9.7k / P 12.5k，今日变化ΔOI: C +0.5k / P +1.9k，平值价格ATM: C $14.00 / P $12.95 ｜ ATM IV 67.3%，净 delta 敞口 -15k shares
Top ΔOI: P 145 +373 ｜ P 150 +326
仓位参考: Max Pain 192 ｜ Call Wall 210（+8.6%，弱）（OI 1.0k） ｜ Put Wall 180（-6.9%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 67.3%｜历史 Rank 87%（近端代理）｜IV/RV 1.64×（近似）｜净 delta 敞口 负 15,369 股

📅 事件差分（观察，非因果）: 10-23（3D）ATM IV 56.0% vs 10-30 50.5%（差 +5.4pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/PLTR_morning.json