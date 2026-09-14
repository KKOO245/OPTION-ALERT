# 期权晚报 2026-09-14（快照 16:48 ET）

📊 市场环境

SPY $760.88 ｜ QQQ $709.18
VIX 17.10 ↑8.0%（5D +11.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.9 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 703.29 → 收盘 709.18（+0.8%） ｜ 今日高 712.95 ｜ 低 702.75 ｜ 昨收 714.88 → 收盘 709.18（-0.8%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-17，窗口结束前不做对错判定）

Options: P/C成交量 1.21 | OI比 2.41 | ATM IV 12.4% | Skew 1.0pp | Term 1.52 | ExpMove ±0.7%（近端） | Rank 17%
量化视角： IV 历史低位（Rank 17%，期权偏便宜）｜期限结构正常偏陡（Term 1.52）｜保护溢价薄（Skew 1.0pp）｜当日成交偏 Put（P/C量 1.21）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.21×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.41×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 9% ｜ P/C OI(近端) 90%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 9%）｜近端 Put 显著偏重（P/C OI 分位 90%，历史高位区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-15（1D）±0.7% ｜ 09-16（2D）±1.2% ｜ 09-17（3D）±1.5% ｜ 09-18（4D）±1.8%
   ⇒ IV–VIX Spread: -4.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -874,114,686 | GEX Change vs 上次快照 166,677,079 | Flip: Primary Flip: 720.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2904 / LOW 559 / INVALID 2309
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 720.14（全链重定价，覆盖 94%）
Put Wall 700（弱结构｜现价高于该位 1.3%） | Call Wall 750（弱结构｜现价低于该位 5.4%）
最近结构参考: Put Wall 700（现价高于该位 1.3%）
量化视角： 负 Gamma（8.74亿，历史分位偏负区，比 91% 的交易日更负）｜负 Gamma 缓解（+1.67亿）｜现价位于 Flip 下方 1.52%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 715（MaxPain，仅结算参考） / 750（Call Wall，弱结构）。
• Gamma 区域：切换参考 720（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 690.0P — Vol 1,531 | 最新价 $5.71 | OI 796→21860 (ΔOI +21064张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21064张（+2646.2% vs前日OI），连续性待观察（方向未知）
09-15 710.0P — Vol 83,226 | 最新价 $2.63 | OI 1373→17534 (ΔOI +16161张) | ΔOI/Volume 19.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16161张（+1177.1% vs前日OI），连续性待观察（方向未知）
09-25 485.0P — Vol 13,000（Yahoo补） | 最新价 $0.04 | OI 95→13095 (ΔOI +13000张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13000张（+13684.2% vs前日OI），连续性待观察（方向未知）
09-14 714.0P — Vol 38,211 | 最新价 $4.42 | OI 82→11575 (ΔOI +11493张) | ΔOI/Volume 30.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11493张（+14015.9% vs前日OI），连续性待观察（方向未知）
09-15 500.0P — Vol 0 | 最新价 $0.01 | OI 0→10000 (ΔOI +10000张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增10000张（前日OI缺失），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 71,718 张（Put 71,718 / Call 0），跨 4 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $21M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-15  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-16  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-17  C +0 / P +0 ｜ Activity LOW ｜ 3D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 4D

📆 09-15 Forward Structure
存量OI: C 35.1k / P 143.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.85 / P $2.20 ｜ ATM IV 16.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 715 ｜ Call Wall 730（+2.9%，弱）（OI 5.4k） ｜ Put Wall 710（+0.1%，弱）（OI 17.5k）
量化解读： 存量 Put 重｜ATM IV 16.8%｜历史 Rank 17%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

09-16（Activity LOW）仓位参考: Max Pain 715 ｜ Call Wall 740（+4.3%，弱）（OI 2.0k） ｜ Put Wall 677（-4.5%，弱）（OI 3.5k）

09-17（Activity LOW）仓位参考: Max Pain 715 ｜ Call Wall 725（+2.2%）（OI 1.6k） ｜ Put Wall 650（-8.3%，弱）（OI 6.5k）

09-18（Activity LOW）仓位参考: Max Pain 700 ｜ Call Wall 750（+5.8%，弱）（OI 51.0k） ｜ Put Wall 700（-1.3%）（OI 116.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=16 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=16）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/QQQ_evening.json