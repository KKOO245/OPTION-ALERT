# 期权晨报 2026-11-12（快照 10:20 ET）

📊 市场环境

SPY $757.88 ｜ QQQ $688.17
VIX 18.45 ↑5.5%（5D -34.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 281P ΔOI +3,969（距现价 +0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 283.09 → 今开 281.43（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 282.20 ｜ 低 278.87

Options: P/C成交量 1.62 | OI比 0.64 | ATM IV 28.7% | Skew 3.3pp | Term 0.65 | ExpMove ±1.1%（近端） | Rank 65%
量化视角： IV 中性（Rank 65%）｜期限结构倒挂（Term 0.65，近月 IV 高于远月）｜保护溢价中性（Skew 3.3pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.64）+ 当日成交偏 Put（P/C量 1.62）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.62×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±1.1% ｜ 11-16（4D）±1.4% ｜ 11-17（5D）±1.6% ｜ 11-18（6D）±2.0%
   ⇒ IV–VIX Spread: +10.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -766,577,651 | GEX Change vs 上次快照 -691,854,061 | Flip: Primary Flip: 284.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1375 / LOW 225 / INVALID 1058
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 284.05（全链重定价，覆盖 98%）
Put Wall 270（弱结构｜现价高于该位 3.4%） | Call Wall 300（弱结构｜现价低于该位 7.0%）
最近结构参考: Flip 284（现价低于该位 1.7%）
量化视角： 负 Gamma（7.67亿，无历史分位）｜负 Gamma 加深（6.92亿）｜现价位于 Flip 下方 1.73%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构）；上方 280（MaxPain，仅结算参考） / 300（Call Wall，弱结构）。
• Gamma 区域：切换参考 284（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 272.0P — Vol 32,186 | 最新价 $0.55 | OI 15760→44279 (ΔOI +28519张) | ΔOI/Volume 88.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增28519张（+181.0% vs前日OI），连续性待观察（方向未知）
11-27 266.0P — Vol 20,291 | 最新价 $0.49 | OI 302→18793 (ΔOI +18491张) | ΔOI/Volume 91.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18491张（+6122.9% vs前日OI），连续性待观察（方向未知）
11-27 276.0P — Vol 19,313 | 最新价 $1.59 | OI 1144→19213 (ΔOI +18069张) | ΔOI/Volume 93.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18069张（+1579.5% vs前日OI），连续性待观察（方向未知）
11-20 279.0P — Vol 11,537 | 最新价 $1.56 | OI 6879→16530 (ΔOI +9651张) | ΔOI/Volume 83.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9651张（+140.3% vs前日OI），连续性待观察（方向未知）
11-20 285.0C — Vol 14,497 | 最新价 $2.25 | OI 47694→53665 (ΔOI +5971张) | ΔOI/Volume 41.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5971张（+12.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 80,701 张（Put 74,730 / Call 5,971），跨 2 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 45.2k / P 28.9k，今日成交量: C 63.3k / P 102.5k，平值价格ATM: C $1.14 / P $0.64 ｜ ATM IV 28.7%，预期波动 ±0.6%，Max Pain 280
Top ΔOI: C 287 -10,533 ｜ C 286 +2,692 ｜ P 282 +2,153

📆 Forward Expiration Structure

11-13  C +5.0k / P +6.4k ｜ Activity HIGH ｜ 1D
11-16  C +1.3k / P +1.6k ｜ Activity HIGH ｜ 4D
11-17  C +1.1k / P +0.6k ｜ Activity HIGH ｜ 5D
11-18  C +1.0k / P +1.1k ｜ Activity HIGH ｜ 6D

📆 11-13 Forward Structure
存量OI: C 116.7k / P 189.6k，今日变化ΔOI: C +5.0k / P +6.4k，平值价格ATM: C $1.84 / P $1.25 ｜ ATM IV 23.1%，净 delta 敞口 -671k shares
Top ΔOI: P 281 +3,969 ｜ P 277 -2,526 ｜ P 282 +2,044
仓位参考: Max Pain 280 ｜ Call Wall 302（+8.2%，弱）（OI 13.7k） ｜ Put Wall 272（-2.6%，弱）（OI 12.6k）
量化解读： 存量 Put 重｜ATM IV 23.1%｜历史 Rank 65%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 671,002 股

📆 11-16 Forward Structure
存量OI: C 15.0k / P 20.5k，今日变化ΔOI: C +1.3k / P +1.6k，平值价格ATM: C $2.29 / P $1.65 ｜ ATM IV 16.2%，净 delta 敞口 -66k shares
Top ΔOI: P 282 +566 ｜ P 266 +333 ｜ P 281 +314
仓位参考: Max Pain 280 ｜ Call Wall 285（+2.1%，弱）（OI 2.3k） ｜ Put Wall 270（-3.3%）（OI 3.9k）
量化解读： 存量 Put 重｜ATM IV 16.2%｜历史 Rank 65%（近端代理）｜IV/RV 0.67×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 66,210 股

📆 11-17 Forward Structure
存量OI: C 7.5k / P 11.0k，今日变化ΔOI: C +1.1k / P +0.6k，平值价格ATM: C $2.57 / P $1.95 ｜ ATM IV 17.0%，净 delta 敞口 -19k shares
Top ΔOI: C 286 +315 ｜ C 292 +225 ｜ C 288 +214
仓位参考: Max Pain 279 ｜ Call Wall 289（+3.5%，弱）（OI 0.7k） ｜ Put Wall 260（-6.9%）（OI 1.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 17.0%｜历史 Rank 65%（近端代理）｜IV/RV 0.70×（近似）｜净 delta 敞口 负 19,084 股

📆 11-18 Forward Structure
存量OI: C 8.7k / P 6.7k，今日变化ΔOI: C +1.0k / P +1.1k，平值价格ATM: C $3.18 / P $2.30 ｜ ATM IV 17.6%，净 delta 敞口 -32k shares
Top ΔOI: C 287 +263 ｜ P 283 +181 ｜ C 286 +161
仓位参考: Max Pain 280 ｜ Call Wall 288（+3.2%，弱）（OI 1.5k） ｜ Put Wall 275（-1.5%）（OI 2.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 17.6%｜历史 Rank 65%（近端代理）｜IV/RV 0.73×（近似）｜净 delta 敞口 负 31,656 股

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 23.1% vs 11-16 16.2%（差 +6.9pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/IWM_morning.json