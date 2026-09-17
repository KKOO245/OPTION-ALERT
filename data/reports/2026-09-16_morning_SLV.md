# 期权晨报 2026-09-16（快照 11:22 ET）

📊 市场环境

SPY $754.05 ｜ QQQ $704.72
VIX 16.68 ↓3.0%（5D +1.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 3.75　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　✅ 今日已公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **事件差分**: 09-18 ATM IV 52.8% vs 09-21 40.7%（差 +12.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-21 61C ΔOI +511（距现价 +4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 57.53 → 今开 58.35（+1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 58.59 ｜ 低 57.88

Options: P/C成交量 1.09 | OI比 0.81 | ATM IV 89.7% | Skew -3.2pp | Term 0.47 | ExpMove ±3.3%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.47，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.09×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（2D）±3.3% ｜ 09-21（5D）±3.9% ｜ 09-23（7D）±5.2% ｜ 09-25（9D）±5.4%
   ⇒ IV–VIX Spread: +73.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 75,184,493 | GEX Change vs 上次快照 37,041,835 | Flip: Primary Flip: 56.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1074 / LOW 222 / INVALID 322
结构观察区: Primary Flip 56.52（全链重定价，覆盖 97%）
最近结构参考: Flip 57（现价高于该位 3.4%）
量化视角： 正 Gamma（7518万，无历史分位）｜正 Gamma 增强（+3704万）｜现价位于 Flip 上方 3.39%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 58（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 57（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 75.0C — Vol 13,536 | 最新价 $0.27 | OI 20364→28451 (ΔOI +8087张) | ΔOI/Volume 59.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8087张（+39.7% vs前日OI），连续性待观察（方向未知）
10-02 66.0C — Vol 5,564 | 最新价 $0.35 | OI 4335→9597 (ΔOI +5262张) | ΔOI/Volume 94.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5262张（+121.4% vs前日OI），连续性待观察（方向未知）
10-16 72.0C — Vol 5,646 | 最新价 $0.35 | OI 7446→12095 (ΔOI +4649张) | ΔOI/Volume 82.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4649张（+62.4% vs前日OI），连续性待观察（方向未知）
09-16 57.5C — Vol 6,150 | 最新价 $0.63 | OI 4109→8036 (ΔOI +3927张) | ΔOI/Volume 63.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3927张（+95.6% vs前日OI），连续性待观察（方向未知）
10-16 57.0P — Vol 3,665 | 最新价 $2.39 | OI 4709→8166 (ΔOI +3457张) | ΔOI/Volume 94.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3457张（+73.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 25,382 张（Put 3,457 / Call 21,925），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 35.1k / P 28.4k，今日成交量: C 17.4k / P 18.9k，平值价格ATM: C $0.47 / P $0.57 ｜ ATM IV 89.7%，预期波动 ±1.8%，Max Pain 58
Top ΔOI: C 57 +3,927 ｜ C 59 +1,131 ｜ C 59 +964

📆 Forward Expiration Structure

09-18  C +10.5k / P +1.7k ｜ Activity HIGH ｜ 2D
09-21  C +2.0k / P +1.3k ｜ Activity HIGH ｜ 5D
09-23  C +0.9k / P +1.3k ｜ Activity HIGH ｜ 7D
09-25  C +3.8k / P +3.9k ｜ Activity HIGH ｜ 9D

📆 09-18 Forward Structure
存量OI: C 978.0k / P 467.7k，今日变化ΔOI: C +10.5k / P +1.7k，平值价格ATM: C $0.92 / P $1.01 ｜ ATM IV 52.8%，净 delta 敞口 601k shares
Top ΔOI: P 55 +2,734 ｜ P 53 +2,409
仓位参考: Max Pain 59 ｜ Call Wall 60（+2.7%，弱）（OI 43.5k） ｜ Put Wall 55（-5.9%，弱）（OI 24.2k）
量化解读： 存量 Call 重｜ATM IV 52.8%｜历史 Rank 98%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 600,752 股

📆 09-21 Forward Structure
存量OI: C 8.2k / P 3.8k，今日变化ΔOI: C +2.0k / P +1.3k，平值价格ATM: C $1.11 / P $1.17 ｜ ATM IV 40.7%，净 delta 敞口 62k shares
Top ΔOI: C 61 +511 ｜ P 54 +489 ｜ C 59 +281
仓位参考: Max Pain 57 ｜ Call Wall 57（-2.4%）（OI 3.2k） ｜ Put Wall 54（-7.6%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 40.7%｜历史 Rank 98%（近端代理）｜IV/RV 1.17×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 61,949 股

📆 09-23 Forward Structure
存量OI: C 2.8k / P 5.1k，今日变化ΔOI: C +0.9k / P +1.3k，平值价格ATM: C $1.40 / P $1.65 ｜ ATM IV 42.9%，净 delta 敞口 4k shares
Top ΔOI: P 53 +469 ｜ C 61 +442 ｜ P 58 +248
仓位参考: Max Pain 59 ｜ Call Wall 61.5（+5.3%，弱）（OI 0.5k） ｜ Put Wall 55（-5.9%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 42.9%｜历史 Rank 98%（近端代理）｜IV/RV 1.23×（近似）｜净 delta 敞口 正 4,255 股

📆 09-25 Forward Structure
存量OI: C 88.6k / P 28.5k，今日变化ΔOI: C +3.8k / P +3.9k，平值价格ATM: C $1.57 / P $1.60 ｜ ATM IV 43.7%，净 delta 敞口 -58k shares
Top ΔOI: P 63 +1,810 ｜ C 61 +767
仓位参考: Max Pain 60 ｜ Put Wall 55（-5.9%，弱）（OI 5.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 43.7%｜历史 Rank 98%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 负 58,063 股

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 52.8% vs 09-21 40.7%（差 +12.1pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/SLV_morning.json