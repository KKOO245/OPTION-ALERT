# 期权晨报 2026-10-06（快照 10:20 ET）

📊 市场环境

SPY $779.74 ｜ QQQ $760.82
VIX 15.48 ↓0.3%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 49.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 1600P ΔOI +620（距现价 -4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,704.16 → 今开 1,700.00（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 1716.50 ｜ 低 1665.54

Options: P/C成交量 0.65 | OI比 1.06 | ATM IV 60.2% | Skew -3.1pp | Term 1.04 | ExpMove ±4.7%（近端） | Rank 17%
量化视角： IV 历史低位（Rank 17%，期权偏便宜）｜期限结构正常（Term 1.04）｜Put 保护异常便宜（Skew -3.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.06×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（3D）±4.7% ｜ 10-16（10D）±7.4% ｜ 10-23（17D）±10.1% ｜ 10-30（24D）±12.7%
   ⇒ IV–VIX Spread: +44.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,189,507 | GEX Change vs 上次快照 -1,859,780 | Flip: Primary Flip: 1706.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1481 / LOW 427 / INVALID 1192
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1706.07（全链重定价，覆盖 100%）
最近结构参考: Flip 1706（现价低于该位 1.5%）
量化视角： 负 Gamma（319万，无历史分位）｜负 Gamma 加深（186万）｜现价位于 Flip 下方 1.54%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,700（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1706（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 1550.0P — Vol 3,383 | 最新价 $3.31 | OI 677→1389 (ΔOI +712张) | ΔOI/Volume 21.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增712张（+105.2% vs前日OI），连续性待观察（方向未知）
10-09 1900.0C — Vol 2,811 | 最新价 $3.12 | OI 1074→1783 (ΔOI +709张) | ΔOI/Volume 25.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增709张（+66.0% vs前日OI），连续性待观察（方向未知）
10-09 1600.0P — Vol 1,494 | 最新价 $8.35 | OI 999→1619 (ΔOI +620张) | ΔOI/Volume 41.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增620张（+62.1% vs前日OI），连续性待观察（方向未知）
10-09 1850.0C — Vol 1,687 | 最新价 $6.08 | OI 1415→2034 (ΔOI +619张) | ΔOI/Volume 36.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增619张（+43.8% vs前日OI），连续性待观察（方向未知）
10-09 1800.0C — Vol 2,769 | 最新价 $12.34 | OI 1391→1911 (ΔOI +520张) | ΔOI/Volume 18.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增520张（+37.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,180 张（Put 1,332 / Call 1,848），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +6.6k / P +6.3k ｜ Activity HIGH ｜ 3D
10-16  C +1.6k / P +0.8k ｜ Activity HIGH ｜ 10D
10-23  C +0.9k / P +1.2k ｜ Activity MEDIUM △ ｜ 17D
10-30  C +0.8k / P +0.9k ｜ Activity MEDIUM △ ｜ 24D

📆 10-09 Forward Structure
存量OI: C 32.8k / P 34.9k，今日变化ΔOI: C +6.6k / P +6.3k，平值价格ATM: C $44.00 / P $34.10 ｜ ATM IV 60.2%，净 delta 敞口 21k shares
Top ΔOI: P 1550 +712 ｜ C 1900 +709 ｜ P 1600 +620
仓位参考: Max Pain 1,700 ｜ Call Wall 1800（+7.2%，弱）（OI 1.9k） ｜ Put Wall 1600（-4.8%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 60.2%｜历史 Rank 17%（近端代理）｜IV/RV 0.98×（近似）｜净 delta 敞口 正 20,570 股

📆 10-16 Forward Structure
存量OI: C 42.6k / P 51.6k，今日变化ΔOI: C +1.6k / P +0.8k，平值价格ATM: C $64.35 / P $60.70 ｜ ATM IV 56.7%，净 delta 敞口 31k shares
Top ΔOI: C 2000 +297 ｜ C 1800 +249 ｜ P 1500 +192
仓位参考: Max Pain 1,670 ｜ Call Wall 1800（+7.2%，弱）（OI 1.5k） ｜ Put Wall 1600（-4.8%，弱）（OI 1.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 56.7%｜历史 Rank 17%（近端代理）｜IV/RV 0.92×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 31,251 股

10-23（MEDIUM △）Top ΔOI: 1700C +167 ｜ 1500P +127
10-23（MEDIUM △）仓位参考: Max Pain 1,710 ｜ Call Wall 1800（+7.2%，弱）（OI 0.4k） ｜ Put Wall 1650（-1.8%，弱）（OI 0.3k）

10-30（MEDIUM △）Top ΔOI: 1700C +140 ｜ 1700P +118
10-30（MEDIUM △）仓位参考: Max Pain 1,710 ｜ Call Wall 1700（+1.2%，弱）（OI 0.3k） ｜ Put Wall 1600（-4.8%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=42 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=42）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/SNDK_morning.json