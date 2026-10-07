# 期权晨报 2026-10-06（快照 10:20 ET）

📊 市场环境

SPY $779.09 ｜ QQQ $759.66
VIX 15.48 ↓0.3%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.4（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-07 235P ΔOI +17,943（距现价 -2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 238.90 → 今开 242.08（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 243.37 ｜ 低 240.76

Options: P/C成交量 0.53 | OI比 1.20 | ATM IV 31.1% | Skew 1.1pp | Term 0.94 | ExpMove ±1.5%（近端） | Rank 9%
量化视角： IV 历史低位（Rank 9%，期权偏便宜）｜期限结构正常（Term 0.94）｜保护溢价薄（Skew 1.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.20×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-07（1D）±1.5% ｜ 10-09（3D）±2.3% ｜ 10-12（6D）±2.8% ｜ 10-14（8D）±3.2%
   ⇒ IV–VIX Spread: +15.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 673,730,642 | GEX Change vs 上次快照 99,465,806 | Flip: Primary Flip: 226.23（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 717 / LOW 156 / INVALID 601
结构观察区: Primary Flip 226.23（全链重定价，覆盖 100%）
Put Wall 220（弱结构｜现价高于该位 9.9%） | Call Wall 240（弱结构｜现价高于该位 0.8%）
最近结构参考: Call Wall 240（现价高于该位 0.8%）
量化视角： 正 Gamma（6.74亿，无历史分位）｜正 Gamma 增强（+9947万）｜现价位于 Flip 上方 6.90%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（Put Wall，弱结构） / 235（MaxPain，仅结算参考） / 240（Call Wall，弱结构）。
• Gamma 区域：切换参考 226（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-07 235.0P — Vol 73,178 | 最新价 $0.71 | OI 2761→20704 (ΔOI +17943张) | ΔOI/Volume 24.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17943张（+649.9% vs前日OI），连续性待观察（方向未知）
10-09 217.5P — Vol 19,702 | 最新价 $0.10 | OI 6890→21091 (ΔOI +14201张) | ΔOI/Volume 72.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14201张（+206.1% vs前日OI），连续性待观察（方向未知）
10-09 230.0P — Vol 39,547 | 最新价 $0.52 | OI 26454→40181 (ΔOI +13727张) | ΔOI/Volume 34.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13727张（+51.9% vs前日OI），连续性待观察（方向未知）
10-09 247.5C — Vol 37,029 | 最新价 $0.50 | OI 33368→45470 (ΔOI +12102张) | ΔOI/Volume 32.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12102张（+36.3% vs前日OI），连续性待观察（方向未知）
10-09 252.5C — Vol 28,579 | 最新价 $0.16 | OI 4593→16136 (ΔOI +11543张) | ΔOI/Volume 40.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11543张（+251.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 69,516 张（Put 45,871 / Call 23,645），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-07  C +47.0k / P +85.8k ｜ Activity HIGH ｜ 1D
10-09  C +53.7k / P +64.2k ｜ Activity HIGH ｜ 3D
10-12  C +12.3k / P +10.2k ｜ Activity HIGH ｜ 6D
10-14  C +5.3k / P +2.4k ｜ Activity HIGH ｜ 8D

📆 10-07 Forward Structure
存量OI: C 106.4k / P 127.4k，今日变化ΔOI: C +47.0k / P +85.8k，平值价格ATM: C $1.58 / P $1.96 ｜ ATM IV 31.1%，净 delta 敞口 1.0M shares
Top ΔOI: P 235 +17,943 ｜ C 245 +8,359 ｜ C 250 +7,461
仓位参考: Max Pain 235 ｜ Call Wall 250（+3.4%，弱）（OI 14.8k） ｜ Put Wall 235（-2.8%，弱）（OI 20.7k）
量化解读： 存量 Put 重｜ATM IV 31.1%｜历史 Rank 9%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,023,377 股

📆 10-09 Forward Structure
存量OI: C 395.9k / P 421.0k，今日变化ΔOI: C +53.7k / P +64.2k，平值价格ATM: C $2.64 / P $2.91 ｜ ATM IV 30.2%，净 delta 敞口 748k shares
Top ΔOI: P 217 +14,201 ｜ P 230 +13,727 ｜ C 247 +12,102
仓位参考: Max Pain 230 ｜ Call Wall 240（-0.8%，弱）（OI 77.3k） ｜ Put Wall 230（-4.9%，弱）（OI 40.2k）
量化解读： 存量两侧均衡｜ATM IV 30.2%｜历史 Rank 9%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 747,965 股

📆 10-12 Forward Structure
存量OI: C 25.6k / P 18.2k，今日变化ΔOI: C +12.3k / P +10.2k，平值价格ATM: C $3.20 / P $3.45 ｜ ATM IV 25.7%，净 delta 敞口 232k shares
Top ΔOI: P 237 +2,884 ｜ C 237 +2,139 ｜ C 257 +1,728
仓位参考: Max Pain 235 ｜ Call Wall 240（-0.8%）（OI 6.2k） ｜ Put Wall 237.5（-1.8%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 25.7%｜历史 Rank 9%（近端代理）｜IV/RV 1.18×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 231,805 股

📆 10-14 Forward Structure
存量OI: C 11.3k / P 5.6k，今日变化ΔOI: C +5.3k / P +2.4k，平值价格ATM: C $3.90 / P $3.75 ｜ ATM IV 27.2%，净 delta 敞口 94k shares
Top ΔOI: C 260 +1,165 ｜ P 237 +856
仓位参考: Max Pain 235 ｜ Call Wall 250（+3.4%，弱）（OI 1.6k） ｜ Put Wall 237.5（-1.8%）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 27.2%｜历史 Rank 9%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 正 94,376 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/NVDA_morning.json