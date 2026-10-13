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
🟡 **近现价集中开仓**: 10-16 250P ΔOI +1,081（距现价 -3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 262.28 → 今开 251.55（-4.1%） | 较昨收变动（含盘初走势） ｜ 今日高 260.94 ｜ 低 248.35

Options: P/C成交量 0.60 | OI比 1.07 | ATM IV 77.0% | Skew 0.2pp | Term 0.98 | ExpMove ±5.7%（近端） | Rank 34%
量化视角： IV 中性（Rank 34%）｜期限结构正常（Term 0.98）｜保护溢价薄（Skew 0.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.07×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（3D）±5.7% ｜ 10-23（10D）±11.6% ｜ 10-30（17D）±14.3% ｜ 11-06（24D）±16.2%
   ⇒ IV–VIX Spread: +61.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,163,082 | GEX Change vs 上次快照 -1,524,561 | Flip: Primary Flip: 263.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 608 / LOW 106 / INVALID 128
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 263.42（全链重定价，覆盖 98%）
Put Wall 240（弱结构｜现价高于该位 7.4%） | Call Wall 280（弱结构｜现价低于该位 7.9%）
最近结构参考: Flip 263（现价低于该位 2.1%）
量化视角： 负 Gamma（516万，无历史分位）｜负 Gamma 加深（152万）｜现价位于 Flip 下方 2.13%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 240（Put Wall，弱结构）；上方 268（MaxPain，仅结算参考） / 280（Call Wall，弱结构）。
• Gamma 区域：切换参考 263（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 250.0P — Vol 2,603 | 最新价 $3.14 | OI 3277→4358 (ΔOI +1081张) | ΔOI/Volume 41.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1081张（+33.0% vs前日OI），连续性待观察（方向未知）
10-16 300.0C — Vol 3,140 | 最新价 $0.52 | OI 5266→6135 (ΔOI +869张) | ΔOI/Volume 27.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增869张（+16.5% vs前日OI），连续性待观察（方向未知）
10-16 270.0C — Vol 3,176 | 最新价 $5.00 | OI 6860→7687 (ΔOI +827张) | ΔOI/Volume 26.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增827张（+12.1% vs前日OI），连续性待观察（方向未知）
10-16 280.0C — Vol 3,334 | 最新价 $2.45 | OI 6443→7099 (ΔOI +656张) | ΔOI/Volume 19.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增656张（+10.2% vs前日OI），连续性待观察（方向未知）
10-16 235.0P — Vol 1,478 | 最新价 $0.87 | OI 1731→2352 (ΔOI +621张) | ΔOI/Volume 42.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增621张（+35.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,054 张（Put 1,702 / Call 2,352），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +7.9k / P +4.0k ｜ Activity HIGH ｜ 3D
10-23  C +2.8k / P +2.7k ｜ Activity HIGH ｜ 10D
10-30  C +1.3k / P +0.7k ｜ Activity HIGH ｜ 17D
11-06  C +0.6k / P +0.5k ｜ Activity MEDIUM △ ｜ 24D

📆 10-16 Forward Structure
存量OI: C 96.9k / P 103.6k，今日变化ΔOI: C +7.9k / P +4.0k，平值价格ATM: C $7.48 / P $7.30 ｜ ATM IV 77.0%，净 delta 敞口 153k shares
Top ΔOI: P 250 +1,081 ｜ C 270 +827
仓位参考: Max Pain 268 ｜ Call Wall 270（+4.7%，弱）（OI 7.7k） ｜ Put Wall 260（+0.9%，弱）（OI 5.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 77.0%｜历史 Rank 34%（近端代理）｜IV/RV 1.02×（近似）｜净 delta 敞口 正 153,336 股

📆 10-23 Forward Structure
存量OI: C 19.7k / P 22.2k，今日变化ΔOI: C +2.8k / P +2.7k，平值价格ATM: C $14.95 / P $15.00 ｜ ATM IV 89.6%，净 delta 敞口 -53k shares
Top ΔOI: C 310 +311
仓位参考: Max Pain 270 ｜ Call Wall 280（+8.6%，弱）（OI 1.2k） ｜ Put Wall 250（-3.0%，弱）（OI 1.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 89.6%｜历史 Rank 34%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 52,507 股

📆 10-30 Forward Structure
存量OI: C 12.9k / P 20.7k，今日变化ΔOI: C +1.3k / P +0.7k，平值价格ATM: C $18.42 / P $18.37 ｜ ATM IV 80.1%，净 delta 敞口 27k shares
Top ΔOI: C 320 -506 ｜ C 280 +480 ｜ C 260 +179
仓位参考: Max Pain 280 ｜ Call Wall 280（+8.6%，弱）（OI 1.2k） ｜ Put Wall 240（-6.9%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 80.1%｜历史 Rank 34%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 27,243 股

11-06（MEDIUM △）Top ΔOI: 260C +295 ｜ 225P +164
11-06（MEDIUM △）仓位参考: Max Pain 265 ｜ Call Wall 260（+0.9%，弱）（OI 0.4k） ｜ Put Wall 235（-8.8%，弱）（OI 2.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=50 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=50）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/BE_morning.json