# 期权晨报 2026-10-15（快照 10:20 ET）

📊 市场环境

SPY $767.19 ｜ QQQ $720.54
VIX 17.51 ↑3.8%（5D +13.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 24.6（extreme fear）
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
🟡 **近现价集中开仓**: 10-23 215C ΔOI +996（距现价 -2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 239.34 → 今开 224.28（-6.3%） | 较昨收变动（含盘初走势） ｜ 今日高 227.83 ｜ 低 215.12

Options: P/C成交量 1.12 | OI比 0.97 | ATM IV 117.7% | Skew 5.3pp | Term 0.78 | ExpMove ±5.6%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价中性（Skew 5.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.12×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.97×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（1D）±5.6% ｜ 10-23（8D）±13.7% ｜ 10-30（15D）±16.6% ｜ 11-06（22D）±19.7%
   ⇒ IV–VIX Spread: +100.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -15,245,816 | GEX Change vs 上次快照 1,669,875 | Flip: Primary Flip: 245.48（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 633 / LOW 84 / INVALID 177
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 245.48（全链重定价，覆盖 96%）
Put Wall 240（弱结构｜现价低于该位 8.5%）
最近结构参考: Put Wall 240（现价低于该位 8.5%）
量化视角： 负 Gamma（1525万，无历史分位）｜负 Gamma 缓解（+167万）｜现价位于 Flip 下方 10.54%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 240（Put Wall，弱结构） / 260（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 245（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 250.0C — Vol 4,185 | 最新价 $3.20 | OI 1980→3213 (ΔOI +1233张) | ΔOI/Volume 29.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1233张（+62.3% vs前日OI），连续性待观察（方向未知）
10-30 240.0C — Vol 1,564 | 最新价 $18.35 | OI 40→1205 (ΔOI +1165张) | ΔOI/Volume 74.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1165张（+2912.5% vs前日OI），连续性待观察（方向未知）
10-23 215.0C — Vol 1,031 | 最新价 $31.31 | OI 12→1008 (ΔOI +996张) | ΔOI/Volume 96.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增996张（+8300.0% vs前日OI），连续性待观察（方向未知）
10-16 240.0P — Vol 4,118 | 最新价 $7.60 | OI 3652→4404 (ΔOI +752张) | ΔOI/Volume 18.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增752张（+20.6% vs前日OI），连续性待观察（方向未知）
10-16 257.5C — Vol 1,911 | 最新价 $1.62 | OI 468→1005 (ΔOI +537张) | ΔOI/Volume 28.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增537张（+114.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,683 张（Put 752 / Call 3,931），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +4.8k / P -3.6k ｜ Activity HIGH ｜ 1D
10-23  C +2.0k / P +1.2k ｜ Activity HIGH ｜ 8D
10-30  C +1.9k / P -0.2k ｜ Activity MEDIUM △ ｜ 15D
11-06  C +0.3k / P -54 ｜ Activity HIGH ｜ 22D

📆 10-16 Forward Structure
存量OI: C 103.5k / P 100.7k，今日变化ΔOI: C +4.8k / P -3.6k，平值价格ATM: C $5.95 / P $6.25 ｜ ATM IV 117.7%，净 delta 敞口 544k shares
Top ΔOI: P 300 -1,245 ｜ P 292 -951
仓位参考: Max Pain 260 ｜ Call Wall 240（+9.3%，弱）（OI 1.6k） ｜ Put Wall 240（+9.3%，弱）（OI 4.4k）
量化解读： 存量两侧均衡｜ATM IV 117.7%｜历史 Rank 76%（近端代理）｜IV/RV 1.44×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 544,122 股

📆 10-23 Forward Structure
存量OI: C 27.4k / P 27.3k，今日变化ΔOI: C +2.0k / P +1.2k，平值价格ATM: C $15.50 / P $14.67 ｜ ATM IV 112.5%，净 delta 敞口 31k shares
Top ΔOI: C 215 +996 ｜ C 250 +314 ｜ C 245 +308
仓位参考: Max Pain 260 ｜ Call Wall 215（-2.1%，弱）（OI 1.0k） ｜ Put Wall 230（+4.7%，弱）（OI 2.2k）
量化解读： 存量两侧均衡｜ATM IV 112.5%｜历史 Rank 76%（近端代理）｜IV/RV 1.38×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 31,169 股

10-30（MEDIUM △）Top ΔOI: 240C +1,165 ｜ 240P -636
10-30（MEDIUM △）仓位参考: Max Pain 268 ｜ Call Wall 240（+9.3%，弱）（OI 1.2k） ｜ Put Wall 230（+4.7%）（OI 3.3k）

📆 11-06 Forward Structure
存量OI: C 5.4k / P 11.3k，今日变化ΔOI: C +0.3k / P -54，平值价格ATM: C $21.00 / P $22.28 ｜ ATM IV 96.0%，净 delta 敞口 16k shares
Top ΔOI: P 240 -396 ｜ P 235 +201
仓位参考: Max Pain 270 ｜ Call Wall 240（+9.3%，弱）（OI 0.2k） ｜ Put Wall 235（+7.0%，弱）（OI 2.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 96.0%｜历史 Rank 76%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 正 15,810 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 117.7% vs 10-23 112.5%（差 +5.3pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/BE_morning.json