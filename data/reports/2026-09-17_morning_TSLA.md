# 期权晨报 2026-09-17（快照 11:28 ET）

📊 市场环境

SPY $760.90 ｜ QQQ $715.91
VIX 15.87 ↓10.4%（5D -11.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览
🟡 **事件差分**: 09-18 ATM IV 49.6% vs 09-21 36.7%（差 +12.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-18 375C ΔOI +3,231（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-21 285P ΔOI +4,542 占该期限总 OI 10.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 358.08 → 今开 367.59（+2.7%） | 较昨收变动（含盘初走势） ｜ 今日高 374.12 ｜ 低 363.22

Options: P/C成交量 0.62 | OI比 0.80 | ATM IV 49.6% | Skew -1.2pp | Term 0.85 | ExpMove ±2.3%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（1D）±2.3% ｜ 09-21（4D）±3.2% ｜ 09-23（6D）±4.2% ｜ 09-25（8D）±5.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 107,306,455 | GEX Change vs 上次快照 93,236,814 | Flip: Primary Flip: 356.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1257 / LOW 151 / INVALID 516
结构观察区: Primary Flip 356.33（全链重定价，覆盖 98%）
Call Wall 400（弱结构｜现价低于该位 8.7%）
最近结构参考: Flip 356（现价高于该位 2.5%）
量化视角： 正 Gamma（1.07亿，无历史分位）｜正 Gamma 增强（+9324万）｜现价位于 Flip 上方 2.52%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 358（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 356（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 360.0C — Vol 16,577 | 最新价 $12.50 | OI 2340→16821 (ΔOI +14481张) | ΔOI/Volume 87.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14481张（+618.9% vs前日OI），连续性待观察（方向未知）
09-21 285.0P — Vol 4,565 | 最新价 $0.11 | OI 66→4608 (ΔOI +4542张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4542张（+6881.8% vs前日OI），连续性待观察（方向未知）
09-18 375.0C — Vol 22,935 | 最新价 $0.75 | OI 11551→14782 (ΔOI +3231张) | ΔOI/Volume 14.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3231张（+28.0% vs前日OI），连续性待观察（方向未知）
09-18 382.5C — Vol 6,497 | 最新价 $0.26 | OI 10782→12935 (ΔOI +2153张) | ΔOI/Volume 33.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2153张（+20.0% vs前日OI），连续性待观察（方向未知）
09-18 365.0C — Vol 33,758 | 最新价 $2.52 | OI 6470→8494 (ΔOI +2024张) | ΔOI/Volume 6.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2024张（+31.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 26,431 张（Put 4,542 / Call 21,889），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +15.0k / P -4.2k ｜ Activity MEDIUM △ ｜ 1D
09-21  C +4.4k / P +8.0k ｜ Activity HIGH ｜ 4D
09-23  C +3.4k / P +2.4k ｜ Activity HIGH ｜ 6D
09-25  C +7.2k / P +6.3k ｜ Activity HIGH ｜ 8D

📆 09-18 Forward Structure
存量OI: C 603.9k / P 481.3k，今日变化ΔOI: C +15.0k / P -4.2k，平值价格ATM: C $4.08 / P $4.22 ｜ ATM IV 49.6%，净 delta 敞口 1.4M shares
Top ΔOI: P 400 -9,758 ｜ C 375 +3,231 ｜ C 382 +2,153
仓位参考: Max Pain 358 ｜ Call Wall 400（+9.5%，弱）（OI 24.0k） ｜ Put Wall 350（-4.2%，弱）（OI 18.1k）
量化解读： 存量 Call 重｜ATM IV 49.6%｜历史 Rank 40%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,447,019 股

📆 09-21 Forward Structure
存量OI: C 23.9k / P 20.8k，今日变化ΔOI: C +4.4k / P +8.0k，平值价格ATM: C $5.80 / P $5.73 ｜ ATM IV 36.7%，净 delta 敞口 97k shares
Top ΔOI: C 370 +875 ｜ P 340 +775
仓位参考: Max Pain 360 ｜ Call Wall 400（+9.5%）（OI 5.1k） ｜ Put Wall 360（-1.5%，弱）（OI 1.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 36.7%｜历史 Rank 40%（近端代理）｜IV/RV 0.83×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 96,735 股

📆 09-23 Forward Structure
存量OI: C 12.6k / P 9.8k，今日变化ΔOI: C +3.4k / P +2.4k，平值价格ATM: C $7.72 / P $7.60 ｜ ATM IV 40.2%，净 delta 敞口 40k shares
Top ΔOI: C 400 +673 ｜ C 365 +562 ｜ P 360 +452
仓位参考: Max Pain 362 ｜ Call Wall 400（+9.5%，弱）（OI 1.2k） ｜ Put Wall 330（-9.7%）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 40.2%｜历史 Rank 40%（近端代理）｜IV/RV 0.91×（近似）｜净 delta 敞口 正 39,720 股

📆 09-25 Forward Structure
存量OI: C 83.0k / P 77.3k，今日变化ΔOI: C +7.2k / P +6.3k，平值价格ATM: C $9.25 / P $9.15 ｜ ATM IV 42.0%，净 delta 敞口 120k shares
Top ΔOI: C 370 +1,472
仓位参考: Max Pain 358 ｜ Call Wall 385（+5.4%，弱）（OI 6.4k） ｜ Put Wall 350（-4.2%，弱）（OI 4.2k）
量化解读： 存量两侧均衡｜ATM IV 42.0%｜历史 Rank 40%（近端代理）｜IV/RV 0.95×（近似）｜净 delta 敞口 正 120,413 股

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 49.6% vs 09-21 36.7%（差 +12.9pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/TSLA_morning.json