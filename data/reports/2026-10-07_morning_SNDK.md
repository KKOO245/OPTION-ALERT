# 期权晨报 2026-10-07（快照 10:20 ET）

📊 市场环境

SPY $774.46 ｜ QQQ $754.50
VIX 15.79 ↑5.2%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　⏰ 今日
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 1600P ΔOI +467（距现价 -4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,660.46 → 今开 1,619.50（-2.5%） | 较昨收变动（含盘初走势） ｜ 今日高 1691.00 ｜ 低 1617.95

Options: P/C成交量 0.47 | OI比 1.04 | ATM IV 61.2% | Skew -2.9pp | Term 1.02 | ExpMove ±3.9%（近端） | Rank 18%
量化视角： IV 历史低位（Rank 18%，期权偏便宜）｜期限结构正常（Term 1.02）｜Put 保护异常便宜（Skew -2.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.04×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（2D）±3.9% ｜ 10-16（9D）±7.2% ｜ 10-23（16D）±9.5% ｜ 10-30（23D）±12.6%
   ⇒ IV–VIX Spread: +45.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,975,419 | GEX Change vs 上次快照 2,149,750 | Flip: Primary Flip: 1692.75（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1569 / LOW 422 / INVALID 1175
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1692.75（全链重定价，覆盖 100%）
最近结构参考: Flip 1693（现价低于该位 1.4%）
量化视角： 负 Gamma（398万，无历史分位）｜负 Gamma 缓解（+215万）｜现价位于 Flip 下方 1.38%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,695（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1693（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 900.0P — Vol 1,000 | 最新价 $0.09 | OI 2135→3105 (ΔOI +970张) | ΔOI/Volume 97.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增970张（+45.4% vs前日OI），连续性待观察（方向未知）
10-16 1900.0C — Vol 1,086 | 最新价 $8.60 | OI 1327→1867 (ΔOI +540张) | ΔOI/Volume 49.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增540张（+40.7% vs前日OI），连续性待观察（方向未知）
10-09 1800.0C — Vol 3,768 | 最新价 $3.65 | OI 1911→2451 (ΔOI +540张) | ΔOI/Volume 14.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增540张（+28.3% vs前日OI），连续性待观察（方向未知）
10-09 1895.0C — Vol 560 | 最新价 $1.00 | OI 350→849 (ΔOI +499张) | ΔOI/Volume 89.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增499张（+142.6% vs前日OI），连续性待观察（方向未知）
10-16 1685.0C — Vol 665 | 最新价 $50.80 | OI 18→489 (ΔOI +471张) | ΔOI/Volume 70.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增471张（+2616.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,020 张（Put 970 / Call 2,050），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +5.7k / P +5.0k ｜ Activity HIGH ｜ 2D
10-16  C +3.1k / P +3.1k ｜ Activity HIGH ｜ 9D
10-23  C +1.3k / P +0.7k ｜ Activity MEDIUM △ ｜ 16D
10-30  C +1.1k / P +1.2k ｜ Activity MEDIUM △ ｜ 23D

📆 10-09 Forward Structure
存量OI: C 38.6k / P 40.0k，今日变化ΔOI: C +5.7k / P +5.0k，平值价格ATM: C $34.00 / P $31.00 ｜ ATM IV 61.2%，净 delta 敞口 67k shares
Top ΔOI: C 1800 +540 ｜ P 1600 +467
仓位参考: Max Pain 1,695 ｜ Call Wall 1800（+7.8%，弱）（OI 2.5k） ｜ Put Wall 1600（-4.2%，弱）（OI 2.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 61.2%｜历史 Rank 18%（近端代理）｜IV/RV 1.03×（近似）｜净 delta 敞口 正 66,735 股

📆 10-16 Forward Structure
存量OI: C 45.7k / P 54.7k，今日变化ΔOI: C +3.1k / P +3.1k，平值价格ATM: C $62.40 / P $57.77 ｜ ATM IV 56.4%，净 delta 敞口 38k shares
Top ΔOI: C 1900 +540 ｜ C 1685 +471
仓位参考: Max Pain 1,675 ｜ Call Wall 1800（+7.8%，弱）（OI 1.5k） ｜ Put Wall 1600（-4.2%，弱）（OI 1.5k）
量化解读： 存量 Put 重｜ATM IV 56.4%｜历史 Rank 18%（近端代理）｜IV/RV 0.95×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 38,179 股

10-23（MEDIUM △）Top ΔOI: 1800C +170 ｜ 1670C +144
10-23（MEDIUM △）仓位参考: Max Pain 1,700 ｜ Call Wall 1800（+7.8%）（OI 0.5k） ｜ Put Wall 1650（-1.2%，弱）（OI 0.4k）

10-30（MEDIUM △）Top ΔOI: 1500P +142 ｜ 1700C +114
10-30（MEDIUM △）仓位参考: Max Pain 1,700 ｜ Call Wall 1700（+1.8%，弱）（OI 0.4k） ｜ Put Wall 1600（-4.2%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/SNDK_morning.json