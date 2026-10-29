# 期权晨报 2026-10-29（快照 10:20 ET）

📊 市场环境

SPY $765.98 ｜ QQQ $715.34
VIX 16.74 ↓1.0%（5D -12.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览
🟡 **事件差分**: 10-30 ATM IV 45.6% vs 11-02 33.1%（差 +12.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-30 410C ΔOI +2,974（距现价 +1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 404.22 → 今开 405.93（+0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 406.43 ｜ 低 400.56

Options: P/C成交量 0.93 | OI比 1.22 | ATM IV 45.6% | Skew 1.2pp | Term 0.82 | ExpMove ±2.1%（近端） | Rank 27%
量化视角： IV 中性（Rank 27%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价薄（Skew 1.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.93×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.22×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±2.1% ｜ 11-02（4D）±2.9% ｜ 11-04（6D）±4.0% ｜ 11-06（8D）±4.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 133,379,205 | GEX Change vs 上次快照 8,630,376 | Flip: Primary Flip: 381.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1295 / LOW 90 / INVALID 857
结构观察区: Primary Flip 381.18（全链重定价，覆盖 98%）
Call Wall 420（弱结构｜现价低于该位 3.9%）
最近结构参考: Call Wall 420（现价低于该位 3.9%）
量化视角： 正 Gamma（1.33亿，无历史分位）｜正 Gamma 增强（+863万）｜现价位于 Flip 上方 5.87%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 382（MaxPain，仅结算参考）；上方 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 381（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 150.0P — Vol 6,864 | 最新价 $0.01 | OI 25693→32492 (ΔOI +6799张) | ΔOI/Volume 99.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6799张（+26.5% vs前日OI），连续性待观察（方向未知）
11-20 470.0C — Vol 7,127 | 最新价 $1.26 | OI 2558→8749 (ΔOI +6191张) | ΔOI/Volume 86.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6191张（+242.0% vs前日OI），连续性待观察（方向未知）
11-20 140.0P — Vol 5,097 | 最新价 $0.02 | OI 761→5790 (ΔOI +5029张) | ΔOI/Volume 98.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5029张（+660.8% vs前日OI），连续性待观察（方向未知）
11-02 325.0P — Vol 3,515 | 最新价 $0.05 | OI 785→4204 (ΔOI +3419张) | ΔOI/Volume 97.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3419张（+435.5% vs前日OI），连续性待观察（方向未知）
10-30 410.0C — Vol 30,105 | 最新价 $2.71 | OI 7817→10791 (ΔOI +2974张) | ΔOI/Volume 9.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2974张（+38.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 24,412 张（Put 15,247 / Call 9,165），跨 3 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +19.0k / P +19.3k ｜ Activity HIGH ｜ 1D
11-02  C +11.4k / P +5.7k ｜ Activity HIGH ｜ 4D
11-04  C +2.2k / P +2.6k ｜ Activity HIGH ｜ 6D
11-06  C +3.3k / P +16.1k ｜ Activity HIGH ｜ 8D

📆 10-30 Forward Structure
存量OI: C 223.6k / P 272.7k，今日变化ΔOI: C +19.0k / P +19.3k，平值价格ATM: C $5.08 / P $3.60 ｜ ATM IV 45.6%，净 delta 敞口 183k shares
Top ΔOI: C 410 +2,974 ｜ C 405 +2,969
仓位参考: Max Pain 382 ｜ Call Wall 420（+4.1%）（OI 24.1k） ｜ Put Wall 380（-5.8%，弱）（OI 9.2k）
量化解读： 存量 Put 重｜ATM IV 45.6%｜历史 Rank 27%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 183,275 股

📆 11-02 Forward Structure
存量OI: C 49.6k / P 21.7k，今日变化ΔOI: C +11.4k / P +5.7k，平值价格ATM: C $6.60 / P $5.15 ｜ ATM IV 33.1%，净 delta 敞口 123k shares
Top ΔOI: C 410 +2,320
仓位参考: Max Pain 395 ｜ Call Wall 410（+1.6%，弱）（OI 3.5k） ｜ Put Wall 400（-0.9%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 33.1%｜历史 Rank 27%（近端代理）｜IV/RV 1.00×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 122,524 股

📆 11-04 Forward Structure
存量OI: C 11.1k / P 9.9k，今日变化ΔOI: C +2.2k / P +2.6k，平值价格ATM: C $9.08 / P $7.25 ｜ ATM IV 38.2%，净 delta 敞口 -22k shares
Top ΔOI: P 400 +1,422 ｜ C 440 +317 ｜ P 390 +308
仓位参考: Max Pain 400 ｜ Call Wall 410（+1.6%，弱）（OI 1.5k） ｜ Put Wall 400（-0.9%）（OI 2.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 38.2%｜历史 Rank 27%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 负 22,192 股

📆 11-06 Forward Structure
存量OI: C 61.2k / P 81.1k，今日变化ΔOI: C +3.3k / P +16.1k，平值价格ATM: C $10.53 / P $8.75 ｜ ATM IV 39.6%，净 delta 敞口 14k shares
Top ΔOI: P 400 +1,491
仓位参考: Max Pain 385 ｜ Call Wall 420（+4.1%，弱）（OI 4.8k） ｜ Put Wall 400（-0.9%，弱）（OI 3.4k）
量化解读： 存量 Put 重｜ATM IV 39.6%｜历史 Rank 27%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 正 14,415 股

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 45.6% vs 11-02 33.1%（差 +12.4pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/TSLA_morning.json