# 期权晨报 2026-10-13（快照 10:20 ET）

📊 市场环境

SPY $777.22 ｜ QQQ $743.49
VIX 15.31 ↑0.7%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 46.0（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.95 ｜ 实际 3.99 ｜ 前值 3.93　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 156C ΔOI +656（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 151.40 → 今开 150.52（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 150.84 ｜ 低 148.28

Options: P/C成交量 0.78 | OI比 1.69 | ATM IV 34.1% | Skew 6.3pp | Term 0.93 | ExpMove ±3.9%（近端） | Rank 56%
量化视角： IV 中性（Rank 56%）｜期限结构正常（Term 0.93）｜保护溢价显著（Skew 6.3pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.69×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-16（3D）±3.9% ｜ 10-23（10D）±6.4% ｜ 10-30（17D）±10.5% ｜ 11-06（24D）±11.2%
   ⇒ IV–VIX Spread: +18.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -66,547,776 | GEX Change vs 上次快照 2,837,102 | Flip: Primary Flip: 161.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 402 / LOW 84 / INVALID 286
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 161.63（全链重定价，覆盖 94%）
Put Wall 150（现价低于该位 0.5%）
最近结构参考: Put Wall 150（现价低于该位 0.5%）
量化视角： 负 Gamma（6655万，无历史分位）｜负 Gamma 缓解（+284万）｜现价位于 Flip 下方 7.63%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（Put Wall） / 156（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 162（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 156.0C — Vol 739 | 最新价 $0.54 | OI 325→981 (ΔOI +656张) | ΔOI/Volume 88.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增656张（+201.8% vs前日OI），连续性待观察（方向未知）
10-16 153.0C — Vol 520 | 最新价 $1.43 | OI 120→490 (ΔOI +370张) | ΔOI/Volume 71.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增370张（+308.3% vs前日OI），连续性待观察（方向未知）
10-16 160.0C — Vol 389 | 最新价 $0.14 | OI 1530→1625 (ΔOI +95张) | ΔOI/Volume 24.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增95张（+6.2% vs前日OI），连续性待观察（方向未知）
10-16 151.0P — Vol 200 | 最新价 $1.83 | OI 776→847 (ΔOI +71张) | ΔOI/Volume 35.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增71张（+9.2% vs前日OI），连续性待观察（方向未知）
10-16 150.0P — Vol 14 | 最新价 $1.37 | OI 23576→23606 (ΔOI +30张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增30张（量数据缺失），以日内换手为主
量化视角： 5 个事件合计 ΔOI ≈ 1,222 张（Put 101 / Call 1,121），跨 1 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +0.3k / P -1.6k ｜ Activity MEDIUM △ ｜ 3D
10-23  C +77 / P +6 ｜ Activity LOW ｜ 10D
10-30  C +27 / P -0.2k ｜ Activity LOW ｜ 17D
11-06  C +22 / P +10 ｜ Activity LOW ｜ 24D

📆 10-16 Forward Structure
存量OI: C 44.8k / P 75.6k，今日变化ΔOI: C +0.3k / P -1.6k，平值价格ATM: C $3.69 / P $2.10 ｜ ATM IV 34.1%，净 delta 敞口 162k shares
Top ΔOI: P 165 -1,096 ｜ C 162 -762 ｜ C 156 +656
仓位参考: Max Pain 156 ｜ Call Wall 155（+3.8%，弱）（OI 2.5k） ｜ Put Wall 150（+0.5%）（OI 23.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 34.1%｜历史 Rank 56%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 162,361 股

10-23（Activity LOW）仓位参考: Max Pain 154 ｜ Call Wall 155（+3.8%，弱）（OI 0.3k） ｜ Put Wall 140（-6.2%，弱）（OI 0.7k）

10-30（Activity LOW）仓位参考: Max Pain 153 ｜ Call Wall 155（+3.8%）（OI 1.4k） ｜ Put Wall 150（+0.5%，弱）（OI 7.2k）

11-06（Activity LOW）仓位参考: Max Pain 155 ｜ Call Wall 150（+0.5%，弱）（OI 35） ｜ Put Wall 143（-4.2%）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=50 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=50）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/XBI_morning.json