# 期权晨报 2026-11-25（快照 10:20 ET）

📊 市场环境

SPY $720.30 ｜ QQQ $633.93
VIX 31.62 ↑19.9%（5D +28.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.2（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 0.6　✅ 今日已公布
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.7 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 4.3 ｜ 前值 1.5　✅ 今日已公布
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 0.2 ｜ 前值 1.8　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 638.10 → 今开 617.10（-3.3%） | 较昨收变动（含盘初走势） ｜ 今日高 619.38 ｜ 低 607.76

Options: P/C成交量 1.23 | OI比 0.91 | ATM IV 66.2% | Skew 4.8pp | Term 0.56 | ExpMove ±2.6%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.56，近月 IV 高于远月）｜保护溢价中性（Skew 4.8pp）｜当日成交偏 Put（P/C量 1.23）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.23×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.91×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 16% ｜ P/C OI(近端) 3%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 16%）｜近端持仓极端 Call 重（P/C OI 分位 3%，历史极低区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-27（2D）±2.6% ｜ 11-30（5D）±3.7% ｜ 12-01（6D）±4.3% ｜ 12-02（7D）±4.7%
   ⇒ IV–VIX Spread: +34.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -596,367,856 | GEX Change vs 上次快照 -196,612,118 | Flip: Primary Flip: 646.94（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3128 / LOW 547 / INVALID 2071
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 646.94（全链重定价，覆盖 96%）
最近结构参考: Flip 647（现价低于该位 4.6%）
量化视角： 负 Gamma（5.96亿，历史分位偏负区，比 84% 的交易日更负）｜负 Gamma 加深（1.97亿）｜现价位于 Flip 下方 4.58%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 638（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 647（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 690.0C — Vol 34,956 | 最新价 $2.99 | OI 32268→63129 (ΔOI +30861张) | ΔOI/Volume 88.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30861张（+95.6% vs前日OI），连续性待观察（方向未知）
12-18 510.0P — Vol 31,958 | 最新价 $1.66 | OI 9379→38758 (ΔOI +29379张) | ΔOI/Volume 91.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29379张（+313.2% vs前日OI），连续性待观察（方向未知）
12-18 605.0P — Vol 33,276 | 最新价 $11.10 | OI 22469→43649 (ΔOI +21180张) | ΔOI/Volume 63.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21180张（+94.3% vs前日OI），连续性待观察（方向未知）
12-18 580.0P — Vol 15,141 | 最新价 $6.65 | OI 56597→67327 (ΔOI +10730张) | ΔOI/Volume 70.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10730张（+19.0% vs前日OI），连续性待观察（方向未知）
12-18 550.0P — Vol 21,543 | 最新价 $3.65 | OI 57278→67818 (ΔOI +10540张) | ΔOI/Volume 48.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10540张（+18.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 102,690 张（Put 71,829 / Call 30,861），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $39M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 180.0k / P 163.5k，今日成交量: C 561.9k / P 688.0k，平值价格ATM: C $4.80 / P $4.05 ｜ ATM IV 66.2%，预期波动 ±1.4%，Max Pain 638
Top ΔOI: C 650 +5,880 ｜ C 645 +5,700 ｜ C 655 +4,746

📆 Forward Expiration Structure

11-27  C +24.6k / P +6.7k ｜ Activity HIGH ｜ 2D
11-30  C +22.9k / P -1.2k ｜ Activity HIGH ｜ 5D
12-01  C +8.5k / P +4.9k ｜ Activity HIGH ｜ 6D
12-02  C +9.9k / P +10.8k ｜ Activity HIGH ｜ 7D

📆 11-27 Forward Structure
存量OI: C 291.5k / P 263.7k，今日变化ΔOI: C +24.6k / P +6.7k，平值价格ATM: C $8.66 / P $7.51 ｜ ATM IV 42.9%，净 delta 敞口 2.3M shares
Top ΔOI: P 690 -9,361 ｜ P 680 -9,316 ｜ C 650 +6,870
仓位参考: Max Pain 644 ｜ Put Wall 600（-2.8%，弱）（OI 14.1k）
量化解读： 存量两侧均衡｜ATM IV 42.9%｜历史 Rank 99%（近端代理）｜IV/RV 0.93×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,326,734 股

📆 11-30 Forward Structure
存量OI: C 358.8k / P 344.8k，今日变化ΔOI: C +22.9k / P -1.2k，平值价格ATM: C $12.13 / P $10.50 ｜ ATM IV 38.5%，净 delta 敞口 1.5M shares
Top ΔOI: P 575 +7,861 ｜ P 690 -6,681 ｜ C 650 +5,412
仓位参考: Max Pain 660 ｜ Call Wall 630（+2.1%，弱）（OI 6.6k） ｜ Put Wall 600（-2.8%，弱）（OI 15.5k）
量化解读： 存量两侧均衡｜ATM IV 38.5%｜历史 Rank 99%（近端代理）｜IV/RV 0.83×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,505,377 股

📆 12-01 Forward Structure
存量OI: C 29.4k / P 46.0k，今日变化ΔOI: C +8.5k / P +4.9k，平值价格ATM: C $15.18 / P $11.70 ｜ ATM IV 40.7%，净 delta 敞口 -71k shares
Top ΔOI: P 585 +1,276
仓位参考: Max Pain 640 ｜ Call Wall 630（+2.1%，弱）（OI 1.0k） ｜ Put Wall 600（-2.8%，弱）（OI 3.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 40.7%｜历史 Rank 99%（近端代理）｜IV/RV 0.88×（近似）｜净 delta 敞口 负 71,070 股

📆 12-02 Forward Structure
存量OI: C 21.3k / P 19.4k，今日变化ΔOI: C +9.9k / P +10.8k，平值价格ATM: C $15.25 / P $13.82 ｜ ATM IV 41.2%，净 delta 敞口 -106k shares
Top ΔOI: P 510 +3,296 ｜ P 575 +2,106 ｜ C 660 +1,914
仓位参考: Max Pain 643 ｜ Put Wall 600（-2.8%，弱）（OI 1.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 41.2%｜历史 Rank 99%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 负 105,635 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/QQQ_morning.json