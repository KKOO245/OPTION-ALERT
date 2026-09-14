# 期权晨报 2026-09-14（快照 10:20 ET）

📊 市场环境

SPY $761.06 ｜ QQQ $709.18
VIX 17.27 ↑9.0%（5D +12.9%） ｜ Vol Regime: NORMAL
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

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-15 710P ΔOI +16,161（距现价 +0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 714.88 → 今开 703.29（-1.6%） | 较昨收变动（含盘初走势） ｜ 今日高 707.77 ｜ 低 702.75

Options: P/C成交量 0.90 | OI比 2.41 | ATM IV 21.0% | Skew 2.9pp | Term 0.91 | ExpMove ±0.9%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构正常（Term 0.91）｜保护溢价中性（Skew 2.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.90×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.41×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 6% ｜ P/C OI(近端) 90%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 6%）｜近端 Put 显著偏重（P/C OI 分位 90%，历史高位区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-15（1D）±0.9% ｜ 09-16（2D）±1.3% ｜ 09-17（3D）±1.6% ｜ 09-18（4D）±1.8%
   ⇒ IV–VIX Spread: +3.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,040,791,765 | GEX Change vs 上次快照 -911,571,641 | Flip: Primary Flip: 719.10（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3035 / LOW 533 / INVALID 2204
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 719.10（全链重定价，覆盖 96%）
Put Wall 700（弱结构｜现价高于该位 0.9%） | Call Wall 750（弱结构｜现价低于该位 5.8%）
最近结构参考: Put Wall 700（现价高于该位 0.9%）
量化视角： 负 Gamma（10.41亿，历史分位偏负区，比 94% 的交易日更负）｜负 Gamma 加深（9.12亿）｜现价位于 Flip 下方 1.77%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 715（MaxPain，仅结算参考） / 750（Call Wall，弱结构）。
• Gamma 区域：切换参考 719（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 690.0P — Vol 21,288 | 最新价 $4.82 | OI 796→21860 (ΔOI +21064张) | ΔOI/Volume 99.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21064张（+2646.2% vs前日OI），连续性待观察（方向未知）
09-15 710.0P — Vol 20,374 | 最新价 $1.99 | OI 1373→17534 (ΔOI +16161张) | ΔOI/Volume 79.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16161张（+1177.1% vs前日OI），连续性待观察（方向未知）
09-25 485.0P — Vol 13,000 | 最新价 $0.04 | OI 95→13095 (ΔOI +13000张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13000张（+13684.2% vs前日OI），连续性待观察（方向未知）
09-14 714.0P — Vol 43,147 | 最新价 $2.25 | OI 82→11575 (ΔOI +11493张) | ΔOI/Volume 26.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11493张（+14015.9% vs前日OI），连续性待观察（方向未知）
09-15 500.0P — Vol 10,000 | 最新价 $0.01 | OI 0→10000 (ΔOI +10000张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10000张（前日OI缺失），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 71,718 张（Put 71,718 / Call 0），跨 4 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $16M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 85.6k / P 206.3k，今日成交量: C 485.9k / P 436.7k，平值价格ATM: C $1.67 / P $1.54 ｜ ATM IV 21.0%，预期波动 ±0.5%，Max Pain 715
Top ΔOI: P 714 +11,493 ｜ C 720 +7,063 ｜ P 715 +6,453

📆 Forward Expiration Structure

09-15  C +10.2k / P +65.6k ｜ Activity HIGH ｜ 1D
09-16  C +7.7k / P +16.7k ｜ Activity HIGH ｜ 2D
09-17  C +4.2k / P +25.6k ｜ Activity HIGH ｜ 3D
09-18  C +19.1k / P +2.5k ｜ Activity HIGH ｜ 4D

📆 09-15 Forward Structure
存量OI: C 35.1k / P 143.5k，今日变化ΔOI: C +10.2k / P +65.6k，平值价格ATM: C $3.20 / P $2.87 ｜ ATM IV 18.4%，净 delta 敞口 -2.2M shares
Top ΔOI: P 710 +16,161
仓位参考: Max Pain 715 ｜ Call Wall 730（+3.3%，弱）（OI 5.4k） ｜ Put Wall 710（+0.5%，弱）（OI 17.5k）
量化解读： 存量 Put 重｜ATM IV 18.4%｜历史 Rank 64%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 2,191,520 股

📆 09-16 Forward Structure
存量OI: C 25.0k / P 44.5k，今日变化ΔOI: C +7.7k / P +16.7k，平值价格ATM: C $4.82 / P $4.50 ｜ ATM IV 21.0%，净 delta 敞口 -494k shares
Top ΔOI: P 690 +1,753 ｜ C 732 +1,527 ｜ P 691 +1,365
仓位参考: Max Pain 715 ｜ Call Wall 740（+4.8%，弱）（OI 2.0k） ｜ Put Wall 677（-4.2%，弱）（OI 3.5k）
量化解读： 存量 Put 重｜ATM IV 21.0%｜历史 Rank 64%（近端代理）｜净 delta 敞口 负 494,277 股

📆 09-17 Forward Structure
存量OI: C 16.1k / P 46.9k，今日变化ΔOI: C +4.2k / P +25.6k，平值价格ATM: C $5.91 / P $5.53 ｜ ATM IV 21.3%，净 delta 敞口 -221k shares
Top ΔOI: P 650 +5,550 ｜ P 640 +4,527 ｜ P 639 +1,977
仓位参考: Max Pain 715 ｜ Call Wall 725（+2.6%）（OI 1.6k） ｜ Put Wall 650（-8.0%，弱）（OI 6.5k）
量化解读： 存量 Put 重｜ATM IV 21.3%｜历史 Rank 64%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 220,526 股

📆 09-18 Forward Structure
存量OI: C 1103.8k / P 1504.7k，今日变化ΔOI: C +19.1k / P +2.5k，平值价格ATM: C $6.75 / P $6.20 ｜ ATM IV 21.1%，净 delta 敞口 -263k shares
Top ΔOI: P 660 -5,934 ｜ P 695 -4,591 ｜ P 670 -4,577
仓位参考: Max Pain 700 ｜ Put Wall 700（-0.9%）（OI 116.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 21.1%｜历史 Rank 64%（近端代理）｜净 delta 敞口 负 263,473 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=16 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=16）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/QQQ_morning.json