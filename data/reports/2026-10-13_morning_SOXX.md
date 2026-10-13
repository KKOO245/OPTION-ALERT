# 期权晨报 2026-10-13（快照 10:20 ET）

📊 市场环境

SPY $777.81 ｜ QQQ $743.57
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
🟡 **近现价集中开仓**: 10-16 560C ΔOI +943（距现价 +4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 544.85 → 今开 530.71（-2.6%） | 较昨收变动（含盘初走势） ｜ 今日高 538.73 ｜ 低 527.16

Options: P/C成交量 3.30 | OI比 2.62 | ATM IV 40.7% | Skew 6.0pp | Term 0.92 | ExpMove ±2.5%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构正常（Term 0.92）｜保护溢价中性（Skew 6.0pp）｜当日成交偏 Put（P/C量 3.30）——观察点，非方向信号
   ⇒ Put/Call Volume: 3.30×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.62×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-16（3D）±2.5% ｜ 10-23（10D）±9.4% ｜ 10-30（17D）±11.7% ｜ 11-06（24D）±0.0%
   ⇒ IV–VIX Spread: +25.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -29,813,117 | GEX Change vs 上次快照 -8,354,810 | Flip: Primary Flip: 565.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 666 / LOW 306 / INVALID 634
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 565.42（全链重定价，覆盖 94%）
最近结构参考: Flip 565（现价低于该位 5.0%）
量化视角： 负 Gamma（2981万，无历史分位）｜负 Gamma 加深（835万）｜现价位于 Flip 下方 5.03%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 540（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 565（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 550.0P — Vol 1,030 | 最新价 $15.10 | OI 87→1093 (ΔOI +1006张) | ΔOI/Volume 97.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1006张（+1156.3% vs前日OI），连续性待观察（方向未知）
10-23 550.0C — Vol 1,010 | 最新价 $11.40 | OI 36→1042 (ΔOI +1006张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1006张（+2794.4% vs前日OI），连续性待观察（方向未知）
10-16 560.0C — Vol 1,845 | 最新价 $3.10 | OI 588→1531 (ΔOI +943张) | ΔOI/Volume 51.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增943张（+160.4% vs前日OI），连续性待观察（方向未知）
10-30 540.0P — Vol 815 | 最新价 $14.47 | OI 152→897 (ΔOI +745张) | ΔOI/Volume 91.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增745张（+490.1% vs前日OI），连续性待观察（方向未知）
10-30 530.0P — Vol 737 | 最新价 $10.80 | OI 80→823 (ΔOI +743张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增743张（+928.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,443 张（Put 2,494 / Call 1,949），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +1.3k / P -1.5k ｜ Activity MEDIUM △ ｜ 3D
10-23  C +1.3k / P +2.0k ｜ Activity HIGH ｜ 10D
10-30  C +75 / P +2.3k ｜ Activity MEDIUM △ ｜ 17D
11-06  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 24D

📆 10-16 Forward Structure
存量OI: C 40.3k / P 105.7k，今日变化ΔOI: C +1.3k / P -1.5k，平值价格ATM: C $8.26 / P $5.00 ｜ ATM IV 40.7%，净 delta 敞口 48k shares
Top ΔOI: P 520 -1,340 ｜ C 560 +943
仓位参考: Max Pain 540 ｜ Call Wall 550（+2.4%，弱）（OI 2.3k） ｜ Put Wall 520（-3.2%，弱）（OI 5.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 40.7%｜历史 Rank 72%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 48,013 股

📆 10-23 Forward Structure
存量OI: C 3.0k / P 12.4k，今日变化ΔOI: C +1.3k / P +2.0k，平值价格ATM: C $41.34 / P $9.20 ｜ ATM IV 36.1%，净 delta 敞口 -34k shares
Top ΔOI: C 550 +1,006 ｜ P 550 +1,006
仓位参考: Max Pain 555 ｜ Call Wall 550（+2.4%）（OI 1.0k） ｜ Put Wall 510（-5.0%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 36.1%｜历史 Rank 72%（近端代理）｜IV/RV 1.24×（近似）｜净 delta 敞口 负 34,418 股

10-30（MEDIUM △）Top ΔOI: 540P +745 ｜ 530P +743
10-30（MEDIUM △）仓位参考: Max Pain 568 ｜ Put Wall 550（+2.4%，弱）（OI 3.2k）

11-06（MEDIUM △）Top ΔOI: 570P +100 ｜ 500P +40
11-06（MEDIUM △）仓位参考: Max Pain 570 ｜ Call Wall 567.5（+5.7%，弱）（OI 0.2k） ｜ Put Wall 565（+5.2%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=50 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=50）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/SOXX_morning.json