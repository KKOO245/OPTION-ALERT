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

🔍 重点速览
🟡 **事件差分**: 11-27 ATM IV 71.3% vs 11-30 58.7%（差 +12.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-30 36P ΔOI +2,119（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 36.84 → 今开 35.24（-4.3%） | 较昨收变动（含盘初走势） ｜ 今日高 35.38 ｜ 低 34.49

Options: P/C成交量 1.37 | OI比 0.36 | ATM IV 85.7% | Skew 5.5pp | Term 0.69 | ExpMove ±4.3%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价中性（Skew 5.5pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.36）+ 当日成交偏 Put（P/C量 1.37）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.37×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.36×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±4.3% ｜ 11-30（5D）±6.0% ｜ 12-02（7D）±6.9% ｜ 12-04（9D）±8.1%
   ⇒ IV–VIX Spread: +54.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -17,380,270 | GEX Change vs 上次快照 4,254,765 | Flip: Primary Flip: 36.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 844 / LOW 256 / INVALID 574
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 36.34（全链重定价，覆盖 92%）
最近结构参考: Flip 36（现价低于该位 3.2%）
量化视角： 负 Gamma（1738万，无历史分位）｜负 Gamma 缓解（+425万）｜现价位于 Flip 下方 3.22%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 38（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 36（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-11 41.0C — Vol 5,016 | 最新价 $0.44 | OI 987→5224 (ΔOI +4237张) | ΔOI/Volume 84.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4237张（+429.3% vs前日OI），连续性待观察（方向未知）
12-24 46.0C — Vol 4,073 | 最新价 $0.22 | OI 5187→8351 (ΔOI +3164张) | ΔOI/Volume 77.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3164张（+61.0% vs前日OI），连续性待观察（方向未知）
11-25 37.0C — Vol 3,921 | 最新价 $0.48 | OI 214→2824 (ΔOI +2610张) | ΔOI/Volume 66.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2610张（+1219.6% vs前日OI），连续性待观察（方向未知）
11-27 40.0C — Vol 3,428 | 最新价 $0.05 | OI 6290→8510 (ΔOI +2220张) | ΔOI/Volume 64.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2220张（+35.3% vs前日OI），连续性待观察（方向未知）
11-25 38.0C — Vol 4,606 | 最新价 $0.13 | OI 688→2875 (ΔOI +2187张) | ΔOI/Volume 47.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2187张（+317.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,418 张（Put 0 / Call 14,418），跨 4 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 60.0k / P 21.7k，今日成交量: C 8.7k / P 11.9k，平值价格ATM: C $0.47 / P $0.21 ｜ ATM IV 85.7%，预期波动 ±1.9%，Max Pain 38
Top ΔOI: C 37 +2,610 ｜ C 38 +2,187 ｜ C 37 +1,470

📆 Forward Expiration Structure

11-27  C +9.3k / P -6.6k ｜ Activity HIGH ｜ 2D
11-30  C +1.8k / P +2.6k ｜ Activity HIGH ｜ 5D
12-02  C +1.5k / P +0.9k ｜ Activity HIGH ｜ 7D
12-04  C +5.4k / P -1.4k ｜ Activity HIGH ｜ 9D

📆 11-27 Forward Structure
存量OI: C 124.1k / P 37.1k，今日变化ΔOI: C +9.3k / P -6.6k，平值价格ATM: C $0.89 / P $0.63 ｜ ATM IV 71.3%，净 delta 敞口 946k shares
Top ΔOI: P 44 -2,769 ｜ P 45 -1,643
仓位参考: Max Pain 40 ｜ Call Wall 38.5（+9.5%，弱）（OI 2.6k） ｜ Put Wall 35（-0.5%，弱）（OI 2.9k）
量化解读： 存量 Call 重｜ATM IV 71.3%｜历史 Rank 97%（近端代理）｜IV/RV 1.42×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 945,635 股

📆 11-30 Forward Structure
存量OI: C 29.4k / P 13.5k，今日变化ΔOI: C +1.8k / P +2.6k，平值价格ATM: C $1.13 / P $0.97 ｜ ATM IV 58.7%，净 delta 敞口 -122k shares
Top ΔOI: P 36 +2,119
仓位参考: Max Pain 39 ｜ Put Wall 36.5（+3.8%，弱）（OI 2.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 58.7%｜历史 Rank 97%（近端代理）｜IV/RV 1.17×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 121,699 股

📆 12-02 Forward Structure
存量OI: C 10.0k / P 4.5k，今日变化ΔOI: C +1.5k / P +0.9k，平值价格ATM: C $1.29 / P $1.13 ｜ ATM IV 63.0%，净 delta 敞口 2k shares
Top ΔOI: P 35 +329 ｜ C 38 +296
仓位参考: Max Pain 38 ｜ Put Wall 37.5（+6.6%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 63.0%｜历史 Rank 97%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 正 2,474 股

📆 12-04 Forward Structure
存量OI: C 115.4k / P 21.5k，今日变化ΔOI: C +5.4k / P -1.4k，平值价格ATM: C $1.51 / P $1.32 ｜ ATM IV 64.6%，净 delta 敞口 242k shares
Top ΔOI: P 44 -945
仓位参考: Max Pain 40 ｜ Put Wall 35（-0.5%，弱）（OI 2.0k）
量化解读： 存量 Call 重｜ATM IV 64.6%｜历史 Rank 97%（近端代理）｜IV/RV 1.28×（近似）｜净 delta 敞口 正 242,257 股

📅 事件差分（观察，非因果）: 11-27（2D）ATM IV 71.3% vs 11-30 58.7%（差 +12.7pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/SLV_morning.json