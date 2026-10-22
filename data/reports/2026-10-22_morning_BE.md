# 期权晨报 2026-10-22（快照 10:20 ET）

📊 市场环境

SPY $766.63 ｜ QQQ $710.95
VIX 17.91 ↑7.4%（5D +8.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 235C ΔOI +517（距现价 +2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 238.53 → 今开 228.15（-4.4%） | 较昨收变动（含盘初走势） ｜ 今日高 229.91 ｜ 低 223.30

Options: P/C成交量 0.62 | OI比 0.83 | ATM IV 199.1% | Skew 9.5pp | Term 0.42 | ExpMove ±9.1%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.42，近月 IV 高于远月）｜保护溢价显著（Skew 9.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（1D）±9.1% ｜ 10-30（8D）±12.8% ｜ 11-06（15D）±14.6% ｜ 11-13（22D）±18.3%
   ⇒ IV–VIX Spread: +181.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,700,815 | GEX Change vs 上次快照 -3,056,488 | Flip: Primary Flip: 242.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 672 / LOW 70 / INVALID 118
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 242.69（全链重定价，覆盖 100%）
最近结构参考: Flip 243（现价低于该位 5.5%）
量化视角： 负 Gamma（570万，无历史分位）｜负 Gamma 加深（306万）｜现价位于 Flip 下方 5.53%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 240（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 243（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 265.0C — Vol 1,773 | 最新价 $3.22 | OI 1212→2355 (ΔOI +1143张) | ΔOI/Volume 64.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1143张（+94.3% vs前日OI），连续性待观察（方向未知）
11-20 105.0P — Vol 1,282 | 最新价 $0.14 | OI 1350→2444 (ΔOI +1094张) | ΔOI/Volume 85.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1094张（+81.0% vs前日OI），连续性待观察（方向未知）
11-20 250.0P — Vol 1,076 | 最新价 $28.45 | OI 1998→2854 (ΔOI +856张) | ΔOI/Volume 79.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增856张（+42.8% vs前日OI），连续性待观察（方向未知）
10-23 235.0C — Vol 1,176 | 最新价 $13.49 | OI 845→1362 (ΔOI +517张) | ΔOI/Volume 44.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增517张（+61.2% vs前日OI），连续性待观察（方向未知）
10-23 235.0P — Vol 1,150 | 最新价 $9.80 | OI 1698→2143 (ΔOI +445张) | ΔOI/Volume 38.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增445张（+26.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,055 张（Put 2,395 / Call 1,660），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +4.6k / P +2.8k ｜ Activity HIGH ｜ 1D
10-30  C +1.1k / P +1.9k ｜ Activity HIGH ｜ 8D
11-06  C +0.7k / P +0.1k ｜ Activity MEDIUM △ ｜ 15D
11-13  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 22D

📆 10-23 Forward Structure
存量OI: C 57.2k / P 47.3k，今日变化ΔOI: C +4.6k / P +2.8k，平值价格ATM: C $10.15 / P $10.80 ｜ ATM IV 199.1%，净 delta 敞口 -24k shares
Top ΔOI: C 265 +1,143 ｜ C 235 +517 ｜ P 235 +445
仓位参考: Max Pain 240 ｜ Call Wall 250（+9.0%，弱）（OI 1.9k） ｜ Put Wall 230（+0.3%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 199.1%｜历史 Rank 97%（近端代理）｜IV/RV 2.60×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 23,740 股

📆 10-30 Forward Structure
存量OI: C 21.4k / P 27.9k，今日变化ΔOI: C +1.1k / P +1.9k，平值价格ATM: C $14.39 / P $14.99 ｜ ATM IV 107.5%，净 delta 敞口 -10k shares
Top ΔOI: P 205 +269
仓位参考: Max Pain 250 ｜ Call Wall 240（+4.7%，弱）（OI 1.5k） ｜ Put Wall 240（+4.7%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜ATM IV 107.5%｜历史 Rank 97%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 9,889 股

11-06（MEDIUM △）Top ΔOI: 300C +388 ｜ 250C +60
11-06（MEDIUM △）仓位参考: Max Pain 250 ｜ Call Wall 225（-1.9%，弱）（OI 1.0k） ｜ Put Wall 235（+2.5%，弱）（OI 1.8k）

11-13（MEDIUM △）Top ΔOI: 205P +142 ｜ 200P +60
11-13（MEDIUM △）仓位参考: Max Pain 250 ｜ Call Wall 240（+4.7%，弱）（OI 0.6k） ｜ Put Wall 230（+0.3%）（OI 2.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/BE_morning.json