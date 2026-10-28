# 期权晨报 2026-10-28（快照 10:20 ET）

📊 市场环境

SPY $770.58 ｜ QQQ $721.71
VIX 17.36 ↓0.9%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　⏰ 今日
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4　⏰ 今日
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　⏰ 今日
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 420C ΔOI +3,955（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 407.46 → 今开 410.21（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 410.85 ｜ 低 397.18

Options: P/C成交量 1.47 | OI比 1.46 | ATM IV 59.2% | Skew 1.2pp | Term 0.64 | ExpMove ±2.9%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构倒挂（Term 0.64，近月 IV 高于远月）｜保护溢价薄（Skew 1.2pp）｜当日成交偏 Put（P/C量 1.47）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.47×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.46×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±2.9% ｜ 11-02（5D）±3.4% ｜ 11-04（7D）±4.5% ｜ 11-06（9D）±5.1%
   ⇒ IV–VIX Spread: +41.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 99,279,226 | GEX Change vs 上次快照 -59,553,741 | Flip: Primary Flip: 383.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1403 / LOW 134 / INVALID 899
结构观察区: Primary Flip 383.14（全链重定价，覆盖 99%）
Call Wall 400（弱结构｜现价高于该位 0.3%）
最近结构参考: Call Wall 400（现价高于该位 0.3%）
量化视角： 正 Gamma（9928万，无历史分位）｜正 Gamma 减弱（5955万）｜现价位于 Flip 上方 4.68%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 400（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 383（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-28 400.0P — Vol 75,238 | 最新价 $1.12 | OI 868→13505 (ΔOI +12637张) | ΔOI/Volume 16.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12637张（+1455.9% vs前日OI），连续性待观察（方向未知）
10-28 362.5P — Vol 11,646 | 最新价 $0.09 | OI 457→9409 (ΔOI +8952张) | ΔOI/Volume 76.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8952张（+1958.9% vs前日OI），连续性待观察（方向未知）
10-28 390.0P — Vol 33,323 | 最新价 $0.28 | OI 2850→10214 (ΔOI +7364张) | ΔOI/Volume 22.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7364张（+258.4% vs前日OI），连续性待观察（方向未知）
10-28 397.5P — Vol 32,580 | 最新价 $0.76 | OI 552→5526 (ΔOI +4974张) | ΔOI/Volume 15.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4974张（+901.1% vs前日OI），连续性待观察（方向未知）
10-28 402.5P — Vol 35,172 | 最新价 $1.70 | OI 123→4797 (ΔOI +4674张) | ΔOI/Volume 13.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4674张（+3800.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 38,601 张（Put 38,601 / Call 0），跨 1 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 90.7k / P 131.9k，今日成交量: C 167.8k / P 247.2k，平值价格ATM: C $2.31 / P $2.82 ｜ ATM IV 59.2%，预期波动 ±1.3%，Max Pain 400
Top ΔOI: P 400 +12,637 ｜ P 362 +8,952 ｜ P 390 +7,364

📆 Forward Expiration Structure

10-30  C +15.6k / P +29.5k ｜ Activity HIGH ｜ 2D
11-02  C +5.3k / P +4.3k ｜ Activity HIGH ｜ 5D
11-04  C +3.5k / P +3.2k ｜ Activity HIGH ｜ 7D
11-06  C +9.2k / P +10.3k ｜ Activity HIGH ｜ 9D

📆 10-30 Forward Structure
存量OI: C 204.5k / P 253.3k，今日变化ΔOI: C +15.6k / P +29.5k，平值价格ATM: C $5.60 / P $5.85 ｜ ATM IV 45.5%，净 delta 敞口 -865k shares
Top ΔOI: C 420 +3,955 ｜ P 390 +2,717
仓位参考: Max Pain 382 ｜ Call Wall 420（+4.7%，弱）（OI 22.0k） ｜ Put Wall 380（-5.3%，弱）（OI 8.4k）
量化解读： 存量 Put 重｜ATM IV 45.5%｜历史 Rank 70%（近端代理）｜IV/RV 1.38×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 865,089 股

📆 11-02 Forward Structure
存量OI: C 38.2k / P 16.0k，今日变化ΔOI: C +5.3k / P +4.3k，平值价格ATM: C $6.60 / P $7.01 ｜ ATM IV 35.7%，净 delta 敞口 -120k shares
Top ΔOI: C 440 +758 ｜ C 407 +716
仓位参考: Max Pain 392 ｜ Put Wall 380（-5.3%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 35.7%｜历史 Rank 70%（近端代理）｜IV/RV 1.08×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 120,034 股

📆 11-04 Forward Structure
存量OI: C 8.8k / P 7.3k，今日变化ΔOI: C +3.5k / P +3.2k，平值价格ATM: C $8.79 / P $9.10 ｜ ATM IV 39.2%，净 delta 敞口 -19k shares
Top ΔOI: C 425 +580 ｜ P 400 +574 ｜ C 410 +431
仓位参考: Max Pain 398 ｜ Call Wall 410（+2.2%，弱）（OI 1.3k） ｜ Put Wall 385（-4.0%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 39.2%｜历史 Rank 70%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 负 19,433 股

📆 11-06 Forward Structure
存量OI: C 57.9k / P 65.0k，今日变化ΔOI: C +9.2k / P +10.3k，平值价格ATM: C $10.25 / P $10.28 ｜ ATM IV 40.2%，净 delta 敞口 -32k shares
Top ΔOI: C 420 +2,048 ｜ P 400 +927
仓位参考: Max Pain 380 ｜ Call Wall 420（+4.7%，弱）（OI 4.6k）
量化解读： 存量两侧均衡｜ATM IV 40.2%｜历史 Rank 70%（近端代理）｜IV/RV 1.22×（近似）｜净 delta 敞口 负 32,490 股

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 45.5% vs 11-02 35.7%（差 +9.8pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/TSLA_morning.json