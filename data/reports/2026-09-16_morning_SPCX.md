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
🟡 **事件差分**: 09-18 ATM IV 66.8% vs 09-25 56.0%（差 +10.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-25 150C ΔOI +2,541（距现价 -1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 143.49 → 今开 144.85（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 153.00 ｜ 低 144.36

Options: P/C成交量 0.51 | OI比 0.81 | ATM IV 66.8% | Skew 0.3pp | Term 0.77 | ExpMove ±4.2%（近端） | Rank 73%
量化视角： IV 中性（Rank 73%）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价薄（Skew 0.3pp）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（2D）±4.2% ｜ 09-25（9D）±7.2% ｜ 10-02（16D）±8.9% ｜ 10-09（23D）±10.3%
   ⇒ IV–VIX Spread: +50.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 146,083,139 | GEX Change vs 上次快照 140,805,045 | Flip: Primary Flip: 143.82（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 602 / LOW 120 / INVALID 334
结构观察区: Primary Flip 143.82（全链重定价，覆盖 99%）
Call Wall 160（弱结构｜现价低于该位 5.1%）
最近结构参考: Call Wall 160（现价低于该位 5.1%）
量化视角： 正 Gamma（1.46亿，无历史分位）｜正 Gamma 增强（+1.41亿）｜现价位于 Flip 上方 5.54%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 145（MaxPain，仅结算参考）；上方 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 144（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 137.0P — Vol 27,253 | 最新价 $1.04 | OI 2593→23253 (ΔOI +20660张) | ΔOI/Volume 75.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20660张（+796.8% vs前日OI），连续性待观察（方向未知）
09-18 136.0P — Vol 22,590 | 最新价 $0.85 | OI 2532→18247 (ΔOI +15715张) | ΔOI/Volume 69.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15715张（+620.7% vs前日OI），连续性待观察（方向未知）
09-18 160.0C — Vol 38,893 | 最新价 $0.12 | OI 41289→56553 (ΔOI +15264张) | ΔOI/Volume 39.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15264张（+37.0% vs前日OI），连续性待观察（方向未知）
10-16 125.0P — Vol 16,710 | 最新价 $2.10 | OI 6440→20939 (ΔOI +14499张) | ΔOI/Volume 86.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14499张（+225.1% vs前日OI），连续性待观察（方向未知）
09-18 157.5C — Vol 29,783 | 最新价 $0.21 | OI 15861→28056 (ΔOI +12195张) | ΔOI/Volume 41.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12195张（+76.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 78,333 张（Put 50,874 / Call 27,459），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +64.0k / P +45.1k ｜ Activity HIGH ｜ 2D
09-25  C +10.7k / P +11.5k ｜ Activity HIGH ｜ 9D
10-02  C +3.3k / P +5.2k ｜ Activity HIGH ｜ 16D
10-09  C +1.4k / P +1.4k ｜ Activity HIGH ｜ 23D

📆 09-18 Forward Structure
存量OI: C 722.2k / P 582.5k，今日变化ΔOI: C +64.0k / P +45.1k，平值价格ATM: C $2.78 / P $3.55 ｜ ATM IV 66.8%，净 delta 敞口 3.1M shares
Top ΔOI: P 137 +20,660 ｜ P 136 +15,715 ｜ C 160 +15,264
仓位参考: Max Pain 145 ｜ Call Wall 155（+2.1%，弱）（OI 60.9k） ｜ Put Wall 150（-1.2%，弱）（OI 45.5k）
量化解读： 存量 Call 重｜ATM IV 66.8%｜历史 Rank 73%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,083,216 股

📆 09-25 Forward Structure
存量OI: C 81.1k / P 95.2k，今日变化ΔOI: C +10.7k / P +11.5k，平值价格ATM: C $5.15 / P $5.70 ｜ ATM IV 56.0%，净 delta 敞口 468k shares
Top ΔOI: P 140 +4,275 ｜ C 150 +2,541 ｜ C 145 +2,258
仓位参考: Max Pain 145 ｜ Call Wall 150（-1.2%，弱）（OI 6.9k） ｜ Put Wall 140（-7.8%，弱）（OI 7.5k）
量化解读： 存量两侧均衡｜ATM IV 56.0%｜历史 Rank 73%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 468,210 股

📆 10-02 Forward Structure
存量OI: C 32.3k / P 43.8k，今日变化ΔOI: C +3.3k / P +5.2k，平值价格ATM: C $6.53 / P $6.95 ｜ ATM IV 53.2%，净 delta 敞口 86k shares
Top ΔOI: P 133 +2,362 ｜ C 157 +787 ｜ C 160 +546
仓位参考: Max Pain 145 ｜ Call Wall 150（-1.2%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 53.2%｜历史 Rank 73%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 86,148 股

📆 10-09 Forward Structure
存量OI: C 14.4k / P 16.3k，今日变化ΔOI: C +1.4k / P +1.4k，平值价格ATM: C $7.70 / P $7.95 ｜ ATM IV 51.9%，净 delta 敞口 42k shares
Top ΔOI: C 165 +427 ｜ C 148 +234
仓位参考: Max Pain 146 ｜ Call Wall 165（+8.7%）（OI 1.7k） ｜ Put Wall 140（-7.8%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 51.9%｜历史 Rank 73%（近端代理）｜净 delta 敞口 正 42,231 股

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 66.8% vs 09-25 56.0%（差 +10.7pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/SPCX_morning.json