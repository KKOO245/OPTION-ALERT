# 期权晨报 2026-10-01（快照 10:20 ET）

📊 市场环境

SPY $763.99 ｜ QQQ $742.03
VIX 17.57 ↑7.5%（5D +12.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-01

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 54.5 ｜ 前值 54.6　✅ 今日已公布
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 10-02（1D）ATM IV 59.0% vs 10-05 39.8%（差 +19.2pp），覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-02 352P ΔOI +3,125（距现价 -0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-05 377C ΔOI +15,379 占该期限总 OI 18.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 354.81 → 今开 356.81（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 358.40 ｜ 低 353.80

Options: P/C成交量 0.41 | OI比 0.99 | ATM IV 59.0% | Skew -2.8pp | Term 0.78 | ExpMove ±2.8%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.41×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.99×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（1D）±2.8% ｜ 10-05（4D）±3.5% ｜ 10-07（6D）±4.2% ｜ 10-09（8D）±5.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 51,926,789 | GEX Change vs 上次快照 24,325,916 | Flip: Primary Flip: 348.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1202 / LOW 119 / INVALID 539
结构观察区: Primary Flip 348.14（全链重定价，覆盖 99%）
最近结构参考: Flip 348（现价高于该位 1.8%）
量化视角： 正 Gamma（5193万，无历史分位）｜正 Gamma 增强（+2433万）｜现价位于 Flip 上方 1.81%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 360（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 348（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-05 377.5C — Vol 19,636 | 最新价 $0.98 | OI 379→15758 (ΔOI +15379张) | ΔOI/Volume 78.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15379张（+4057.8% vs前日OI），连续性待观察（方向未知）
10-02 550.0C — Vol 3,533 | 最新价 $0.01 | OI 651→4150 (ΔOI +3499张) | ΔOI/Volume 99.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3499张（+537.5% vs前日OI），连续性待观察（方向未知）
10-02 352.5P — Vol 17,203 | 最新价 $4.20 | OI 1885→5010 (ΔOI +3125张) | ΔOI/Volume 18.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3125张（+165.8% vs前日OI），连续性待观察（方向未知）
10-02 360.0C — Vol 29,387 | 最新价 $3.20 | OI 14373→17468 (ΔOI +3095张) | ΔOI/Volume 10.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3095张（+21.5% vs前日OI），连续性待观察（方向未知）
10-02 350.0C — Vol 34,396 | 最新价 $7.95 | OI 1837→4894 (ΔOI +3057张) | ΔOI/Volume 8.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3057张（+166.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 28,155 张（Put 3,125 / Call 25,030），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +28.8k / P +19.3k ｜ Activity HIGH ｜ 1D
10-05  C +21.9k / P +8.3k ｜ Activity HIGH ｜ 4D
10-07  C +2.5k / P +2.2k ｜ Activity HIGH ｜ 6D
10-09  C +12.1k / P +12.7k ｜ Activity HIGH ｜ 8D

📆 10-02 Forward Structure
存量OI: C 275.3k / P 273.3k，今日变化ΔOI: C +28.8k / P +19.3k，平值价格ATM: C $5.22 / P $4.75 ｜ ATM IV 59.0%，净 delta 敞口 810k shares
Top ΔOI: P 352 +3,125 ｜ C 360 +3,095
仓位参考: Max Pain 360 ｜ Call Wall 360（+1.6%，弱）（OI 17.5k） ｜ Put Wall 350（-1.3%，弱）（OI 7.3k）
量化解读： 存量两侧均衡｜ATM IV 59.0%｜历史 Rank 70%（近端代理）｜IV/RV 2.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 810,394 股

📆 10-05 Forward Structure
存量OI: C 56.9k / P 24.3k，今日变化ΔOI: C +21.9k / P +8.3k，平值价格ATM: C $6.50 / P $5.90 ｜ ATM IV 39.8%，净 delta 敞口 290k shares
Top ΔOI: C 377 +15,379 ｜ C 355 +1,157
仓位参考: Max Pain 355 ｜ Call Wall 377.5（+6.5%）（OI 15.8k） ｜ Put Wall 325（-8.3%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 39.8%｜历史 Rank 70%（近端代理）｜IV/RV 1.45×（近似）｜净 delta 敞口 正 290,436 股

📆 10-07 Forward Structure
存量OI: C 11.6k / P 5.4k，今日变化ΔOI: C +2.5k / P +2.2k，平值价格ATM: C $7.88 / P $6.85 ｜ ATM IV 40.9%，净 delta 敞口 53k shares
Top ΔOI: C 350 +298 ｜ C 370 +269
仓位参考: Max Pain 355 ｜ Call Wall 375（+5.8%，弱）（OI 1.1k） ｜ Put Wall 360（+1.6%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 40.9%｜历史 Rank 70%（近端代理）｜IV/RV 1.49×（近似）｜净 delta 敞口 正 52,700 股

📆 10-09 Forward Structure
存量OI: C 71.8k / P 59.0k，今日变化ΔOI: C +12.1k / P +12.7k，平值价格ATM: C $9.15 / P $8.50 ｜ ATM IV 41.3%，净 delta 敞口 221k shares
仓位参考: Max Pain 355 ｜ Call Wall 370（+4.4%，弱）（OI 3.7k） ｜ Put Wall 350（-1.3%，弱）（OI 2.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 41.3%｜历史 Rank 70%（近端代理）｜IV/RV 1.51×（近似）｜净 delta 敞口 正 220,735 股

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 59.0% vs 10-05 39.8%（差 +19.2pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/TSLA_morning.json