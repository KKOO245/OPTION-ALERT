# 期权晨报 2026-10-22（快照 10:20 ET）

📊 市场环境

SPY $766.63 ｜ QQQ $710.90
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
🟡 **近现价集中开仓**: 10-23 500P ΔOI -884（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 510.36 → 今开 489.73（-4.0%） | 较昨收变动（含盘初走势） ｜ 今日高 494.00 ｜ 低 487.28

Options: P/C成交量 1.18 | OI比 1.30 | ATM IV 55.5% | Skew 17.2pp | Term 0.77 | ExpMove ±2.9%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价显著（Skew 17.2pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.18）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.18×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.30×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-23（1D）±2.9% ｜ 10-30（8D）±4.3% ｜ 11-06（15D）±2.6% ｜ 11-13（22D）±0.0%
   ⇒ IV–VIX Spread: +37.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -34,141,876 | GEX Change vs 上次快照 -9,437,754 | Flip: Primary Flip: 534.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 609 / LOW 306 / INVALID 639
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 534.87（全链重定价，覆盖 98%）
Call Wall 520（现价低于该位 5.2%）
最近结构参考: Call Wall 520（现价低于该位 5.2%）
量化视角： 负 Gamma（3414万，无历史分位）｜负 Gamma 加深（944万）｜现价位于 Flip 下方 7.79%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 512（MaxPain，仅结算参考） / 520（Call Wall）。
• Gamma 区域：切换参考 535（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 512.5C — Vol 900 | 最新价 $6.05 | OI 810→1518 (ΔOI +708张) | ΔOI/Volume 78.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增708张（+87.4% vs前日OI），连续性待观察（方向未知）
10-23 520.0C — Vol 702 | 最新价 $3.18 | OI 641→1181 (ΔOI +540张) | ΔOI/Volume 76.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增540张（+84.2% vs前日OI），连续性待观察（方向未知）
10-30 502.5P — Vol 281 | 最新价 $12.00 | OI 26→296 (ΔOI +270张) | ΔOI/Volume 96.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增270张（+1038.5% vs前日OI），连续性待观察（方向未知）
10-23 550.0C — Vol 316 | 最新价 $0.20 | OI 1395→1649 (ΔOI +254张) | ΔOI/Volume 80.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增254张（+18.2% vs前日OI），连续性待观察（方向未知）
10-23 505.0P — Vol 356 | 最新价 $4.80 | OI 121→338 (ΔOI +217张) | ΔOI/Volume 61.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增217张（+179.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,989 张（Put 487 / Call 1,502），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +1.6k / P -0.8k ｜ Activity HIGH ｜ 1D
10-30  C -0.6k / P -2.1k ｜ Activity HIGH ｜ 8D
11-06  C -0.3k / P -36 ｜ Activity LOW ｜ 15D
11-13  C +0.2k / P +0.4k ｜ Activity MEDIUM △ ｜ 22D

📆 10-23 Forward Structure
存量OI: C 14.8k / P 19.4k，今日变化ΔOI: C +1.6k / P -0.8k，平值价格ATM: C $6.72 / P $7.80 ｜ ATM IV 55.5%，净 delta 敞口 69k shares
Top ΔOI: P 500 -884 ｜ C 512 +708 ｜ C 520 +540
仓位参考: Max Pain 512 ｜ Call Wall 515（+4.4%，弱）（OI 2.2k） ｜ Put Wall 510（+3.4%）（OI 3.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 55.5%｜历史 Rank 90%（近端代理）｜IV/RV 1.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 69,447 股

📆 10-30 Forward Structure
存量OI: C 21.0k / P 145.7k，今日变化ΔOI: C -0.6k / P -2.1k，平值价格ATM: C $14.00 / P $7.05 ｜ ATM IV 49.1%，净 delta 敞口 126k shares
Top ΔOI: P 500 -2,542 ｜ P 475 -361 ｜ P 485 -280
仓位参考: Max Pain 530 ｜ Call Wall 525（+6.4%）（OI 2.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 49.1%｜历史 Rank 90%（近端代理）｜IV/RV 1.60×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 126,271 股

11-06（Activity LOW）仓位参考: Max Pain 538 ｜ Put Wall 495（+0.4%，弱）（OI 1.0k）

11-13（MEDIUM △）Top ΔOI: 510P +166 ｜ 512P +56
11-13（MEDIUM △）仓位参考: Max Pain 520 ｜ Call Wall 520（+5.4%，弱）（OI 6.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/SOXX_morning.json