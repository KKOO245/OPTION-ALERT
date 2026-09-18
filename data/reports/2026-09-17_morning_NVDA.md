# 期权晨报 2026-09-17（快照 11:28 ET）

📊 市场环境

SPY $762.60 ｜ QQQ $nan
VIX 15.87 ↓10.4%（5D -11.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-18 215C ΔOI -13,729（距现价 -1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 213.90 → 今开 218.39（+2.1%） | 较昨收变动（含盘初走势） ｜ 今日高 219.87 ｜ 低 217.15

Options: P/C成交量 0.43 | OI比 0.89 | ATM IV 33.4% | Skew 2.6pp | Term 0.94 | ExpMove ±1.6%（近端） | Rank 13%
量化视角： IV 历史低位（Rank 13%，期权偏便宜）｜期限结构正常（Term 0.94）｜保护溢价中性（Skew 2.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.89×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（1D）±1.6% ｜ 09-21（4D）±2.3% ｜ 09-23（6D）±3.0% ｜ 09-25（8D）±3.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 524,250,420 | GEX Change vs 上次快照 334,566,279 | Flip: Primary Flip: 210.55（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 709 / LOW 205 / INVALID 490
结构观察区: Primary Flip 210.55（全链重定价，覆盖 98%）
Put Wall 200（现价高于该位 9.5%） | Call Wall 220（弱结构｜现价低于该位 0.4%）
最近结构参考: Call Wall 220（现价低于该位 0.4%）
量化视角： 正 Gamma（5.24亿，无历史分位）｜正 Gamma 增强（+3.35亿）｜现价位于 Flip 上方 4.06%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall） / 205（MaxPain，仅结算参考）；上方 220（Call Wall，弱结构）。
• Gamma 区域：切换参考 211（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 130.0P — Vol 71,141 | 最新价 $0.01 | OI 35318→105220 (ΔOI +69902张) | ΔOI/Volume 98.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增69902张（+197.9% vs前日OI），连续性待观察（方向未知）
10-09 215.0C — Vol 22,277 | 最新价 $6.96 | OI 2748→20210 (ΔOI +17462张) | ΔOI/Volume 78.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17462张（+635.4% vs前日OI），连续性待观察（方向未知）
09-18 225.0C — Vol 54,615 | 最新价 $0.12 | OI 78819→87269 (ΔOI +8450张) | ΔOI/Volume 15.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8450张（+10.7% vs前日OI），连续性待观察（方向未知）
09-18 217.5C — Vol 52,831 | 最新价 $1.00 | OI 10219→16497 (ΔOI +6278张) | ΔOI/Volume 11.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6278张（+61.4% vs前日OI），连续性待观察（方向未知）
09-25 220.0C — Vol 77,435 | 最新价 $2.08 | OI 35247→41145 (ΔOI +5898张) | ΔOI/Volume 7.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5898张（+16.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 107,990 张（Put 69,902 / Call 38,088），跨 3 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +5.5k / P +84.3k ｜ Activity HIGH ｜ 1D
09-21  C +5.4k / P +11.4k ｜ Activity HIGH ｜ 4D
09-23  C +2.2k / P +2.9k ｜ Activity HIGH ｜ 6D
09-25  C +16.6k / P +12.8k ｜ Activity HIGH ｜ 8D

📆 09-18 Forward Structure
存量OI: C 1350.9k / P 1208.9k，今日变化ΔOI: C +5.5k / P +84.3k，平值价格ATM: C $1.19 / P $2.32 ｜ ATM IV 33.4%，净 delta 敞口 -440k shares
Top ΔOI: P 130 +69,902 ｜ C 215 -13,729 ｜ C 225 +8,450
仓位参考: Max Pain 205 ｜ Call Wall 230（+5.0%，弱）（OI 96.1k） ｜ Put Wall 200（-8.7%，弱）（OI 59.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 33.4%｜历史 Rank 13%（近端代理）｜IV/RV 0.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 439,599 股

📆 09-21 Forward Structure
存量OI: C 40.3k / P 42.2k，今日变化ΔOI: C +5.4k / P +11.4k，平值价格ATM: C $1.93 / P $3.03 ｜ ATM IV 25.9%，净 delta 敞口 147k shares
Top ΔOI: C 217 +2,048 ｜ P 215 +1,664
仓位参考: Max Pain 212 ｜ Call Wall 240（+9.5%，弱）（OI 5.4k） ｜ Put Wall 200（-8.7%，弱）（OI 7.7k）
量化解读： 存量两侧均衡｜ATM IV 25.9%｜历史 Rank 13%（近端代理）｜IV/RV 0.71×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 146,987 股

📆 09-23 Forward Structure
存量OI: C 24.8k / P 12.1k，今日变化ΔOI: C +2.2k / P +2.9k，平值价格ATM: C $2.77 / P $3.80 ｜ ATM IV 28.6%，净 delta 敞口 94k shares
Top ΔOI: C 230 -1,923 ｜ P 205 +914 ｜ C 225 +884
仓位参考: Max Pain 215 ｜ Call Wall 230（+5.0%）（OI 6.9k） ｜ Put Wall 205（-6.4%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 28.6%｜历史 Rank 13%（近端代理）｜IV/RV 0.79×（近似）｜净 delta 敞口 正 94,377 股

📆 09-25 Forward Structure
存量OI: C 244.6k / P 171.9k，今日变化ΔOI: C +16.6k / P +12.8k，平值价格ATM: C $3.45 / P $4.40 ｜ ATM IV 29.8%，净 delta 敞口 405k shares
Top ΔOI: C 220 +5,898 ｜ C 225 +4,612 ｜ P 195 +3,461
仓位参考: Max Pain 218 ｜ Call Wall 220（+0.4%）（OI 41.1k） ｜ Put Wall 210（-4.2%，弱）（OI 16.9k）
量化解读： 存量 Call 重｜ATM IV 29.8%｜历史 Rank 13%（近端代理）｜IV/RV 0.82×（近似）｜净 delta 敞口 正 405,070 股

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 33.4% vs 09-21 25.9%（差 +7.5pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/NVDA_morning.json