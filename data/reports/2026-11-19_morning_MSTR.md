# 期权晨报 2026-11-19（快照 10:20 ET）

📊 市场环境

SPY $nan ｜ QQQ $nan
VIX 22.66 ↓7.7%（5D +21.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 18.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-27 97C ΔOI +5,420（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 90.32 → 今开 93.11（+3.1%） | 较昨收变动（含盘初走势） ｜ 今日高 93.82 ｜ 低 89.95

Options: P/C成交量 1.30 | OI比 0.63 | ATM IV 115.5% | Skew 8.8pp | Term 0.74 | ExpMove ±5.4%（近端） | Rank 89%
量化视角： IV 历史高位（Rank 89%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价显著（Skew 8.8pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.63）+ 当日成交偏 Put（P/C量 1.30）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.30×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±5.4% ｜ 11-27（8D）±10.5% ｜ 12-04（15D）±14.3% ｜ 12-11（22D）±16.9%
   ⇒ IV–VIX Spread: +92.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -37,654,482 | GEX Change vs 上次快照 8,207,535 | Flip: Primary Flip: 102.19（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 574 / LOW 252 / INVALID 314
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 102.19（全链重定价，覆盖 100%）
Put Wall 90（弱结构｜现价高于该位 3.1%）
最近结构参考: Put Wall 90（现价高于该位 3.1%）
量化视角： 负 Gamma（3765万，无历史分位）｜负 Gamma 缓解（+821万）｜现价位于 Flip 下方 9.16%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 90（Put Wall，弱结构）；上方 107（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 102（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 180.0C — Vol 10,632 | 最新价 $0.10 | OI 8313→18222 (ΔOI +9909张) | ΔOI/Volume 93.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9909张（+119.2% vs前日OI），连续性待观察（方向未知）
11-27 98.0C — Vol 9,041 | 最新价 $2.41 | OI 238→8788 (ΔOI +8550张) | ΔOI/Volume 94.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8550张（+3592.4% vs前日OI），连续性待观察（方向未知）
11-27 103.0C — Vol 7,924 | 最新价 $1.27 | OI 119→7844 (ΔOI +7725张) | ΔOI/Volume 97.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7725张（+6491.6% vs前日OI），连续性待观察（方向未知）
11-27 97.0C — Vol 5,575 | 最新价 $2.91 | OI 119→5539 (ΔOI +5420张) | ΔOI/Volume 97.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5420张（+4554.6% vs前日OI），连续性待观察（方向未知）
11-27 102.0C — Vol 5,632 | 最新价 $1.47 | OI 222→5436 (ΔOI +5214张) | ΔOI/Volume 92.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5214张（+2348.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 36,818 张（Put 0 / Call 36,818），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C -41.7k / P -9.9k ｜ Activity HIGH ｜ 1D
11-27  C +44.9k / P +10.9k ｜ Activity HIGH ｜ 8D
12-04  C +2.9k / P +9.8k ｜ Activity MEDIUM △ ｜ 15D
12-11  C +0.7k / P +1.9k ｜ Activity MEDIUM △ ｜ 22D

📆 11-20 Forward Structure
存量OI: C 283.6k / P 178.2k，今日变化ΔOI: C -41.7k / P -9.9k，平值价格ATM: C $2.37 / P $2.65 ｜ ATM IV 115.5%，净 delta 敞口 2.0M shares
仓位参考: Max Pain 107 ｜ Call Wall 100（+7.7%，弱）（OI 6.1k） ｜ Put Wall 90（-3.0%，弱）（OI 14.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 115.5%｜历史 Rank 89%（近端代理）｜IV/RV 1.72×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,982,064 股

📆 11-27 Forward Structure
存量OI: C 88.2k / P 102.5k，今日变化ΔOI: C +44.9k / P +10.9k，平值价格ATM: C $4.74 / P $5.03 ｜ ATM IV 88.8%，净 delta 敞口 1.6M shares
Top ΔOI: C 98 +8,550 ｜ C 103 +7,725 ｜ C 97 +5,420
仓位参考: Max Pain 98 ｜ Call Wall 98（+5.6%，弱）（OI 8.8k） ｜ Put Wall 90（-3.0%）（OI 15.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 88.8%｜历史 Rank 89%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,558,043 股

12-04（MEDIUM △）Top ΔOI: 85P +1,573 ｜ 92P +1,571
12-04（MEDIUM △）仓位参考: Max Pain 120 ｜ Call Wall 98（+5.6%，弱）（OI 1.4k） ｜ Put Wall 85（-8.4%）（OI 7.0k）

12-11（MEDIUM △）Top ΔOI: 160P -1,105 ｜ 155P -988
12-11（MEDIUM △）仓位参考: Max Pain 135 ｜ Call Wall 100（+7.7%，弱）（OI 0.2k） ｜ Put Wall 85（-8.4%，弱）（OI 2.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/MSTR_morning.json