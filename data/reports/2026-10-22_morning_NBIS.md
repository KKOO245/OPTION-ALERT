# 期权晨报 2026-10-22（快照 10:20 ET）

📊 市场环境

SPY $763.51 ｜ QQQ $708.70
VIX 17.91 ↑7.4%（5D +8.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 20.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 162P ΔOI +1,092（距现价 -0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 171.57 → 今开 164.89（-3.9%） | 较昨收变动（含盘初走势） ｜ 今日高 167.50 ｜ 低 159.18

Options: P/C成交量 0.66 | OI比 0.59 | ATM IV 110.8% | Skew 5.1pp | Term 0.88 | ExpMove ±5.3%（近端） | Rank 61%
量化视角： IV 中性（Rank 61%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价中性（Skew 5.1pp）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（1D）±5.3% ｜ 10-30（8D）±11.2% ｜ 11-06（15D）±15.0% ｜ 11-13（22D）±20.7%
   ⇒ IV–VIX Spread: +92.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -16,139,211 | GEX Change vs 上次快照 -11,600,341 | Flip: Primary Flip: 173.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 594 / LOW 72 / INVALID 146
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 173.96（全链重定价，覆盖 100%）
Put Wall 150（弱结构｜现价高于该位 9.1%）
最近结构参考: Flip 174（现价低于该位 5.9%）
量化视角： 负 Gamma（1614万，无历史分位）｜负 Gamma 加深（1160万）｜现价位于 Flip 下方 5.95%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall，弱结构）；上方 180（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 174（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 220.0C — Vol 2,014 | 最新价 $5.20 | OI 2958→4572 (ΔOI +1614张) | ΔOI/Volume 80.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1614张（+54.6% vs前日OI），连续性待观察（方向未知）
10-30 190.0C — Vol 3,653 | 最新价 $3.65 | OI 982→2476 (ΔOI +1494张) | ΔOI/Volume 40.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1494张（+152.1% vs前日OI），连续性待观察（方向未知）
11-20 145.0P — Vol 1,457 | 最新价 $6.98 | OI 4730→5953 (ΔOI +1223张) | ΔOI/Volume 83.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1223张（+25.9% vs前日OI），连续性待观察（方向未知）
10-23 162.5P — Vol 2,434 | 最新价 $2.06 | OI 1417→2509 (ΔOI +1092张) | ΔOI/Volume 44.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1092张（+77.1% vs前日OI），连续性待观察（方向未知）
10-23 195.0C — Vol 2,301 | 最新价 $0.42 | OI 2896→3825 (ΔOI +929张) | ΔOI/Volume 40.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增929张（+32.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,352 张（Put 2,315 / Call 4,037），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +2.1k / P -2.2k ｜ Activity MEDIUM △ ｜ 1D
10-30  C +5.0k / P +3.1k ｜ Activity HIGH ｜ 8D
11-06  C +1.5k / P +0.4k ｜ Activity MEDIUM △ ｜ 15D
11-13  C +1.0k / P +0.8k ｜ Activity HIGH ｜ 22D

📆 10-23 Forward Structure
存量OI: C 107.6k / P 63.0k，今日变化ΔOI: C +2.1k / P -2.2k，平值价格ATM: C $4.95 / P $3.80 ｜ ATM IV 110.8%，净 delta 敞口 431k shares
Top ΔOI: P 225 -1,942 ｜ P 162 +1,092 ｜ P 220 -992
仓位参考: Max Pain 180 ｜ Call Wall 175（+7.0%，弱）（OI 2.9k） ｜ Put Wall 165（+0.8%，弱）（OI 4.8k）
量化解读： 存量 Call 重｜ATM IV 110.8%｜历史 Rank 61%（近端代理）｜IV/RV 1.42×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 431,020 股

📆 10-30 Forward Structure
存量OI: C 54.8k / P 42.2k，今日变化ΔOI: C +5.0k / P +3.1k，平值价格ATM: C $9.71 / P $8.68 ｜ ATM IV 94.1%，净 delta 敞口 -24k shares
Top ΔOI: C 190 +1,494 ｜ P 150 +565
仓位参考: Max Pain 200 ｜ Call Wall 175（+7.0%，弱）（OI 1.5k） ｜ Put Wall 165（+0.8%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 94.1%｜历史 Rank 61%（近端代理）｜IV/RV 1.21×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 23,518 股

11-06（MEDIUM △）Top ΔOI: 175C +146
11-06（MEDIUM △）仓位参考: Max Pain 205 ｜ Put Wall 170（+3.9%，弱）（OI 1.6k）

📆 11-13 Forward Structure
存量OI: C 13.3k / P 16.5k，今日变化ΔOI: C +1.0k / P +0.8k，平值价格ATM: C $16.00 / P $17.93 ｜ ATM IV 103.5%，净 delta 敞口 20k shares
Top ΔOI: P 175 +236 ｜ P 215 -157
仓位参考: Max Pain 200 ｜ Call Wall 170（+3.9%，弱）（OI 0.4k） ｜ Put Wall 165（+0.8%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 103.5%｜历史 Rank 61%（近端代理）｜IV/RV 1.33×（近似）｜净 delta 敞口 正 20,016 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/NBIS_morning.json