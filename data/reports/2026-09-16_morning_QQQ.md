# 期权晨报 2026-09-16（快照 11:22 ET）

📊 市场环境

SPY $760.53 ｜ QQQ $710.94
VIX 16.68 ↓3.0%（5D +1.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75　⏰ 今日
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　⏰ 今日
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　⏰ 今日
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **近现价集中开仓**: 09-17 723C ΔOI +10,032（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 704.54 → 今开 708.06（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 711.55 ｜ 低 707.65

Options: P/C成交量 1.42 | OI比 1.70 | ATM IV 40.0% | Skew 7.0pp | Term 0.45 | ExpMove ±1.1%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.45，近月 IV 高于远月）｜保护溢价显著（Skew 7.0pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.42）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.42×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.70×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 28% ｜ P/C OI(近端) 56%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 28%）｜近端持仓结构中性（P/C OI 分位 56%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-17（1D）±1.1% ｜ 09-18（2D）±1.5% ｜ 09-21（5D）±1.7% ｜ 09-22（6D）±1.9%
   ⇒ IV–VIX Spread: +23.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -343,005,405 | GEX Change vs 上次快照 695,209,660 | Flip: Primary Flip: 715.17（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3020 / LOW 391 / INVALID 2261
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 715.17（全链重定价，覆盖 96%）
Put Wall 700（弱结构｜现价高于该位 1.6%）
最近结构参考: Flip 715（现价低于该位 0.6%）
量化视角： 负 Gamma（3.43亿，历史分位 28%，中性区）｜负 Gamma 缓解（+6.95亿）｜现价位于 Flip 下方 0.59%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构） / 706（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 715（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 685.0P — Vol 37,270 | 最新价 $1.11 | OI 37543→61768 (ΔOI +24225张) | ΔOI/Volume 65.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24225张（+64.5% vs前日OI），连续性待观察（方向未知）
09-17 723.0C — Vol 10,962 | 最新价 $0.14 | OI 328→10360 (ΔOI +10032张) | ΔOI/Volume 91.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10032张（+3058.5% vs前日OI），连续性待观察（方向未知）
10-16 755.0C — Vol 10,747 | 最新价 $0.98 | OI 7605→17538 (ΔOI +9933张) | ΔOI/Volume 92.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9933张（+130.6% vs前日OI），连续性待观察（方向未知）
09-16 724.0C — Vol 10,823 | 最新价 $0.02 | OI 1178→8797 (ΔOI +7619张) | ΔOI/Volume 70.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7619张（+646.8% vs前日OI），连续性待观察（方向未知）
09-18 701.0P — Vol 9,340 | 最新价 $4.09 | OI 1571→8278 (ΔOI +6707张) | ΔOI/Volume 71.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6707张（+426.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 58,516 张（Put 30,932 / Call 27,584），跨 4 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $5M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 135.8k / P 231.4k，今日成交量: C 475.7k / P 673.5k，平值价格ATM: C $2.66 / P $3.00 ｜ ATM IV 40.0%，预期波动 ±0.8%，Max Pain 706
Top ΔOI: C 724 +7,619 ｜ P 690 +6,635 ｜ C 720 +5,845

📆 Forward Expiration Structure

09-17  C +34.7k / P +44.0k ｜ Activity HIGH ｜ 1D
09-18  C +10.6k / P +27.9k ｜ Activity HIGH ｜ 2D
09-21  C +6.4k / P +6.8k ｜ Activity HIGH ｜ 5D
09-22  C +5.4k / P +8.1k ｜ Activity HIGH ｜ 6D

📆 09-17 Forward Structure
存量OI: C 60.4k / P 119.8k，今日变化ΔOI: C +34.7k / P +44.0k，平值价格ATM: C $3.89 / P $4.13 ｜ ATM IV 24.5%，净 delta 敞口 736k shares
Top ΔOI: C 723 +10,032 ｜ P 680 +4,982
仓位参考: Max Pain 707 ｜ Call Wall 723（+1.7%）（OI 10.4k） ｜ Put Wall 650（-8.6%）（OI 9.5k）
量化解读： 存量 Put 重｜ATM IV 24.5%｜历史 Rank 97%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 735,755 股

📆 09-18 Forward Structure
存量OI: C 1126.1k / P 1559.5k，今日变化ΔOI: C +10.6k / P +27.9k，平值价格ATM: C $5.16 / P $5.20 ｜ ATM IV 23.3%，净 delta 敞口 786k shares
Top ΔOI: P 685 +24,225 ｜ P 675 -14,669 ｜ P 701 +6,707
仓位参考: Max Pain 700 ｜ Call Wall 750（+5.5%，弱）（OI 50.6k） ｜ Put Wall 700（-1.5%）（OI 115.0k）
量化解读： 存量 Put 重｜ATM IV 23.3%｜历史 Rank 97%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 786,488 股

📆 09-21 Forward Structure
存量OI: C 24.8k / P 45.5k，今日变化ΔOI: C +6.4k / P +6.8k，平值价格ATM: C $5.79 / P $6.37 ｜ ATM IV 17.6%，净 delta 敞口 97k shares
Top ΔOI: P 715 -956 ｜ C 723 +916
仓位参考: Max Pain 715 ｜ Call Wall 735（+3.4%，弱）（OI 2.1k） ｜ Put Wall 715（+0.6%）（OI 6.3k）
量化解读： 存量 Put 重｜ATM IV 17.6%｜历史 Rank 97%（近端代理）｜净 delta 敞口 正 96,930 股

📆 09-22 Forward Structure
存量OI: C 12.5k / P 22.2k，今日变化ΔOI: C +5.4k / P +8.1k，平值价格ATM: C $6.36 / P $6.95 ｜ ATM IV 17.9%，净 delta 敞口 65k shares
Top ΔOI: P 685 +932 ｜ C 725 +891 ｜ P 666 +714
仓位参考: Max Pain 710 ｜ Call Wall 725（+2.0%）（OI 1.1k） ｜ Put Wall 685（-3.7%，弱）（OI 1.7k）
量化解读： 存量 Put 重｜ATM IV 17.9%｜历史 Rank 97%（近端代理）｜净 delta 敞口 正 64,825 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/QQQ_morning.json