# 期权晨报 2026-10-13（快照 10:20 ET）

📊 市场环境

SPY $777.90 ｜ QQQ $743.57
VIX 15.31 ↑0.7%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.7（fear）
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
🟡 **近现价集中开仓**: 10-16 42P ΔOI +997（距现价 -1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 43.36 → 今开 42.77（-1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 43.27 ｜ 低 42.26

Options: P/C成交量 0.69 | OI比 0.90 | ATM IV 57.5% | Skew -7.4pp | Term 1.09 | ExpMove ±4.5%（近端） | Rank 32%
量化视角： IV 中性（Rank 32%）｜期限结构正常（Term 1.09）｜Put 保护异常便宜（Skew -7.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.69×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（3D）±4.5% ｜ 10-23（10D）±7.1% ｜ 10-30（17D）±6.4% ｜ 11-06（24D）±14.4%
   ⇒ IV–VIX Spread: +42.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,129,206 | GEX Change vs 上次快照 104,921 | Flip: Primary Flip: 46.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 275 / LOW 57 / INVALID 72
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 46.50（全链重定价，覆盖 96%）
Put Wall 45（现价低于该位 5.2%）
最近结构参考: Put Wall 45（现价低于该位 5.2%）
量化视角： 负 Gamma（513万，无历史分位）｜负 Gamma 缓解（+10万）｜现价位于 Flip 下方 8.22%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 45（Put Wall） / 50（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 47（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 42.0P — Vol 1,122 | 最新价 $0.48 | OI 296→1293 (ΔOI +997张) | ΔOI/Volume 88.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增997张（+336.8% vs前日OI），连续性待观察（方向未知）
10-16 42.5P — Vol 540 | 最新价 $0.69 | OI 145→575 (ΔOI +430张) | ΔOI/Volume 79.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增430张（+296.6% vs前日OI），连续性待观察（方向未知）
10-16 38.0P — Vol 318 | 最新价 $0.03 | OI 131→448 (ΔOI +317张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增317张（+242.0% vs前日OI），连续性待观察（方向未知）
10-16 43.0P — Vol 440 | 最新价 $0.90 | OI 243→533 (ΔOI +290张) | ΔOI/Volume 65.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增290张（+119.3% vs前日OI），连续性待观察（方向未知）
10-16 46.0C — Vol 340 | 最新价 $0.28 | OI 199→399 (ΔOI +200张) | ΔOI/Volume 58.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增200张（+100.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,234 张（Put 2,034 / Call 200），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +1.1k / P +0.7k ｜ Activity MEDIUM △ ｜ 3D
10-23  C +0.3k / P +0.1k ｜ Activity MEDIUM △ ｜ 10D
10-30  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 17D
11-06  C +0.2k / P +0.4k ｜ Activity MEDIUM △ ｜ 24D

📆 10-16 Forward Structure
存量OI: C 22.7k / P 20.5k，今日变化ΔOI: C +1.1k / P +0.7k，平值价格ATM: C $1.08 / P $0.85 ｜ ATM IV 57.5%，净 delta 敞口 91k shares
Top ΔOI: P 42 +997 ｜ P 55 -757 ｜ P 42 +430
仓位参考: Max Pain 50 ｜ Put Wall 45（+5.4%）（OI 4.8k）
量化解读： 存量两侧均衡｜ATM IV 57.5%｜历史 Rank 32%（近端代理）｜IV/RV 1.17×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 90,971 股

10-23（MEDIUM △）Top ΔOI: 54P -74 ｜ 41P +64
10-23（MEDIUM △）仓位参考: Max Pain 49 ｜ Call Wall 45（+5.4%，弱）（OI 99） ｜ Put Wall 45（+5.4%，弱）（OI 0.2k）

10-30（MEDIUM △）Top ΔOI: 39P +99
10-30（MEDIUM △）仓位参考: Max Pain 48 ｜ Put Wall 44（+3.1%）（OI 1.6k）

11-06（MEDIUM △）Top ΔOI: 54P +114
11-06（MEDIUM △）仓位参考: Max Pain 48 ｜ Put Wall 41（-3.9%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=50 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=50）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/MP_morning.json