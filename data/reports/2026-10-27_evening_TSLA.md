# 期权晚报 2026-10-27（快照 16:40 ET）

📊 市场环境

SPY $769.66 ｜ QQQ $721.25
VIX 17.52 ↓4.7%（5D +1.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 1.8 ｜ 前值 0.1　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🟡 **近现价集中开仓**: 10-28 420C ΔOI +3,656（距现价 +3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 397.80 → 收盘 407.46（+2.4%） ｜ 今日高 408.45 ｜ 低 395.25 ｜ 昨收 391.62 → 收盘 407.46（+4.0%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-10-30，窗口结束前不做对错判定）

Options: P/C成交量 0.69 | OI比 1.12 | ATM IV 41.9% | Skew 0.9pp | Term 0.90 | ExpMove ±1.8%（近端） | Rank 16%
量化视角： IV 历史低位（Rank 16%，期权偏便宜）｜期限结构正常（Term 0.90）｜保护溢价薄（Skew 0.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.69×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.12×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-28（1D）±1.8% ｜ 10-30（3D）±3.1% ｜ 11-02（6D）±3.6% ｜ 11-04（8D）±4.5%
   ⇒ IV–VIX Spread: +24.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 152,589,603 | GEX Change vs 上次快照 11,565,399 | Flip: Primary Flip: 373.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1200 / LOW 93 / INVALID 793
结构观察区: Primary Flip 373.87（全链重定价，覆盖 99%）
Call Wall 400（弱结构｜现价高于该位 1.9%）
最近结构参考: Call Wall 400（现价高于该位 1.9%）
量化视角： 正 Gamma（1.53亿，无历史分位）｜正 Gamma 增强（+1157万）｜现价位于 Flip 上方 8.99%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 388（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 374（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 230.0P — Vol 2,019 | 最新价 $0.02 | OI 2752→21935 (ΔOI +19183张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19183张（+697.1% vs前日OI），连续性待观察（方向未知）
10-30 140.0P — Vol 120 | 最新价 $0.01 | OI 804→14512 (ΔOI +13708张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13708张（+1705.0% vs前日OI），连续性待观察（方向未知）
11-06 210.0P — Vol 3,174 | 最新价 $0.04 | OI 176→7055 (ΔOI +6879张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6879张（+3908.5% vs前日OI），连续性待观察（方向未知）
11-20 380.0C — Vol 1,875 | 最新价 $23.00 | OI 5422→10009 (ΔOI +4587张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4587张（+84.6% vs前日OI），连续性待观察（方向未知）
10-30 382.5C — Vol 1,763 | 最新价 $12.76 | OI 715→5281 (ΔOI +4566张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4566张（+638.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 48,923 张（Put 39,770 / Call 9,153），跨 3 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-28  C +29.8k / P +32.0k ｜ Activity HIGH ｜ 1D
10-30  C +44.5k / P +62.1k ｜ Activity HIGH ｜ 3D
11-02  C +9.5k / P +4.6k ｜ Activity HIGH ｜ 6D
11-04  C +3.1k / P +1.9k ｜ Activity HIGH ｜ 8D

📆 10-28 Forward Structure
存量OI: C 51.4k / P 57.6k，今日变化ΔOI: C +29.8k / P +32.0k，平值价格ATM: C $3.61 / P $3.56 ｜ ATM IV 41.9%，净 delta 敞口 1.1M shares
Top ΔOI: P 210 +6,001 ｜ P 380 +3,768 ｜ C 420 +3,656
仓位参考: Max Pain 388 ｜ Call Wall 420（+3.1%，弱）（OI 4.9k） ｜ Put Wall 380（-6.7%，弱）（OI 4.3k）
量化解读： 存量两侧均衡｜ATM IV 41.9%｜历史 Rank 16%（近端代理）｜IV/RV 1.35×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,104,572 股

📆 10-30 Forward Structure
存量OI: C 189.0k / P 223.8k，今日变化ΔOI: C +44.5k / P +62.1k，平值价格ATM: C $6.40 / P $6.10 ｜ ATM IV 42.2%，净 delta 敞口 933k shares
Top ΔOI: C 420 +8,744 ｜ C 415 +3,868
仓位参考: Max Pain 378 ｜ Call Wall 420（+3.1%，弱）（OI 18.0k） ｜ Put Wall 380（-6.7%，弱）（OI 6.4k）
量化解读： 存量 Put 重｜ATM IV 42.2%｜历史 Rank 16%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 932,512 股

📆 11-02 Forward Structure
存量OI: C 32.9k / P 11.7k，今日变化ΔOI: C +9.5k / P +4.6k，平值价格ATM: C $7.42 / P $7.40 ｜ ATM IV 35.3%，净 delta 敞口 256k shares
Top ΔOI: C 395 +1,550 ｜ C 410 +731
仓位参考: Max Pain 385 ｜ Call Wall 395（-3.1%，弱）（OI 1.9k） ｜ Put Wall 380（-6.7%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 35.3%｜历史 Rank 16%（近端代理）｜IV/RV 1.14×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 255,812 股

📆 11-04 Forward Structure
存量OI: C 5.3k / P 4.2k，今日变化ΔOI: C +3.1k / P +1.9k，平值价格ATM: C $9.20 / P $9.20 ｜ ATM IV 38.4%，净 delta 敞口 100k shares
Top ΔOI: C 410 +820 ｜ P 370 +344 ｜ C 420 +299
仓位参考: Max Pain 385 ｜ Call Wall 410（+0.6%）（OI 0.9k） ｜ Put Wall 370（-9.2%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 38.4%｜历史 Rank 16%（近端代理）｜IV/RV 1.24×（近似）｜净 delta 敞口 正 100,026 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/TSLA_evening.json