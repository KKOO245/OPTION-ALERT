# 期权晨报 2026-11-04（快照 10:20 ET）

📊 市场环境

SPY $767.96 ｜ QQQ $691.95
VIX 17.01 ↓18.3%（5D +0.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-04

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 54.5 ｜ 前值 54.9　✅ 今日已公布
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **事件差分**: 11-06 ATM IV 69.3% vs 11-13 56.6%（差 +12.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-06 180C ΔOI +4,200（距现价 +3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 175.40 → 今开 165.08（-5.9%） | 较昨收变动（含盘初走势） ｜ 今日高 177.43 ｜ 低 164.60

Options: P/C成交量 0.40 | OI比 1.04 | ATM IV 69.3% | Skew 1.2pp | Term 0.72 | ExpMove ±4.3%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价薄（Skew 1.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.40×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.04×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（2D）±4.3% ｜ 11-13（9D）±7.5% ｜ 11-20（16D）±9.2% ｜ 11-27（23D）±10.7%
   ⇒ IV–VIX Spread: +52.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,764,339 | GEX Change vs 上次快照 11,542,921 | Flip: Primary Flip: 175.19（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 522 / LOW 130 / INVALID 254
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 175.19（全链重定价，覆盖 100%）
最近结构参考: Flip 175（现价低于该位 0.4%）
量化视角： 负 Gamma（276万，无历史分位）｜负 Gamma 缓解（+1154万）｜现价位于 Flip 下方 0.40%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 182（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 175（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 205.0C — Vol 5,730 | 最新价 $1.13 | OI 1232→5579 (ΔOI +4347张) | ΔOI/Volume 75.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4347张（+352.8% vs前日OI），连续性待观察（方向未知）
11-06 180.0C — Vol 39,558 | 最新价 $2.87 | OI 1584→5784 (ΔOI +4200张) | ΔOI/Volume 10.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4200张（+265.1% vs前日OI），连续性待观察（方向未知）
11-06 190.0C — Vol 16,903 | 最新价 $0.80 | OI 8759→12696 (ΔOI +3937张) | ΔOI/Volume 23.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3937张（+45.0% vs前日OI），连续性待观察（方向未知）
11-06 175.0C — Vol 21,246 | 最新价 $4.90 | OI 862→3190 (ΔOI +2328张) | ΔOI/Volume 11.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2328张（+270.1% vs前日OI），连续性待观察（方向未知）
11-06 170.0C — Vol 11,070 | 最新价 $7.95 | OI 415→2297 (ΔOI +1882张) | ΔOI/Volume 17.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1882张（+453.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 16,694 张（Put 0 / Call 16,694），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +21.0k / P -6.4k ｜ Activity HIGH ｜ 2D
11-13  C +9.0k / P +6.3k ｜ Activity HIGH ｜ 9D
11-20  C +7.1k / P +1.6k ｜ Activity HIGH ｜ 16D
11-27  C +1.9k / P +0.6k ｜ Activity HIGH ｜ 23D

📆 11-06 Forward Structure
存量OI: C 193.5k / P 201.1k，今日变化ΔOI: C +21.0k / P -6.4k，平值价格ATM: C $3.55 / P $4.00 ｜ ATM IV 69.3%，净 delta 敞口 1.0M shares
Top ΔOI: C 180 +4,200 ｜ C 190 +3,937 ｜ C 175 +2,328
仓位参考: Max Pain 182 ｜ Call Wall 187.5（+7.5%，弱）（OI 13.3k） ｜ Put Wall 170（-2.6%，弱）（OI 7.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 69.3%｜历史 Rank 91%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,036,519 股

📆 11-13 Forward Structure
存量OI: C 37.8k / P 33.7k，今日变化ΔOI: C +9.0k / P +6.3k，平值价格ATM: C $6.13 / P $6.90 ｜ ATM IV 56.6%，净 delta 敞口 153k shares
Top ΔOI: C 200 +1,784 ｜ C 175 +1,013 ｜ C 187 +690
仓位参考: Max Pain 182 ｜ Call Wall 190（+8.9%，弱）（OI 1.4k） ｜ Put Wall 180（+3.2%，弱）（OI 1.8k）
量化解读： 存量两侧均衡｜ATM IV 56.6%｜历史 Rank 91%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 153,079 股

📆 11-20 Forward Structure
存量OI: C 177.5k / P 177.9k，今日变化ΔOI: C +7.1k / P +1.6k，平值价格ATM: C $7.88 / P $8.15 ｜ ATM IV 54.5%，净 delta 敞口 192k shares
Top ΔOI: C 205 +4,347 ｜ P 150 +1,525 ｜ C 212 +1,256
仓位参考: Max Pain 175 ｜ Call Wall 165（-5.4%，弱）（OI 11.8k） ｜ Put Wall 180（+3.2%，弱）（OI 10.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 54.5%｜历史 Rank 91%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 192,261 股

📆 11-27 Forward Structure
存量OI: C 13.5k / P 14.8k，今日变化ΔOI: C +1.9k / P +0.6k，平值价格ATM: C $9.00 / P $9.60 ｜ ATM IV 51.2%，净 delta 敞口 71k shares
仓位参考: Max Pain 185 ｜ Call Wall 185（+6.0%，弱）（OI 0.5k） ｜ Put Wall 180（+3.2%，弱）（OI 1.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 51.2%｜历史 Rank 91%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 正 70,756 股

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 69.3% vs 11-13 56.6%（差 +12.6pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=83 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=83）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/PLTR_morning.json