# 期权晨报 2026-10-06（快照 10:20 ET）

📊 市场环境

SPY $779.55 ｜ QQQ $759.66
VIX 15.48 ↓0.3%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.3（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-07 762C ΔOI +11,990（距现价 +0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-12 738P ΔOI +12,503 占该期限总 OI 12.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 756.20 → 今开 760.54（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 762.09 ｜ 低 759.10

Options: P/C成交量 0.92 | OI比 3.11 | ATM IV 19.4% | Skew 1.2pp | Term 0.99 | ExpMove ±0.8%（近端） | Rank 56%
量化视角： IV 中性（Rank 56%）｜期限结构正常（Term 0.99）｜保护溢价薄（Skew 1.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.92×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 3.11×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 90% ｜ P/C OI(近端) 98%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 90%）｜近端 Put 显著偏重（P/C OI 分位 98%，历史高位区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-07（1D）±0.8% ｜ 10-08（2D）±1.0% ｜ 10-09（3D）±1.3% ｜ 10-12（6D）±1.5%
   ⇒ IV–VIX Spread: +3.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 515,060,904 | GEX Change vs 上次快照 -46,354,913 | Flip: Primary Flip: 753.64（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 2928 / LOW 225 / INVALID 1977
结构观察区: Primary Flip 753.64（全链重定价，覆盖 98%）
Call Wall 760（现价高于该位 0.1%）
最近结构参考: Call Wall 760（现价高于该位 0.1%）
量化视角： 正 Gamma（5.15亿，历史分位偏正区，比 90% 的交易日更正）｜正 Gamma 减弱（4635万）｜现价位于 Flip 上方 0.94%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 754（MaxPain，仅结算参考） / 760（Call Wall）。
• Gamma 区域：切换参考 754（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-06 749.0P — Vol 183,879 | 最新价 $0.50 | OI 1334→53704 (ΔOI +52370张) | ΔOI/Volume 28.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增52370张（+3925.8% vs前日OI），连续性待观察（方向未知）
10-12 738.0P — Vol 12,737 | 最新价 $1.35 | OI 104→12607 (ΔOI +12503张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12503张（+12022.1% vs前日OI），连续性待观察（方向未知）
10-07 762.0C — Vol 14,974 | 最新价 $1.15 | OI 963→12953 (ΔOI +11990张) | ΔOI/Volume 80.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11990张（+1245.1% vs前日OI），连续性待观察（方向未知）
10-08 749.0P — Vol 14,009 | 最新价 $1.99 | OI 2204→13380 (ΔOI +11176张) | ΔOI/Volume 79.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11176张（+507.1% vs前日OI），连续性待观察（方向未知）
10-06 605.0P — Vol 11,427 | 最新价 $0.01 | OI 284→10979 (ΔOI +10695张) | ΔOI/Volume 93.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10695张（+3765.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 98,734 张（Put 86,744 / Call 11,990），跨 4 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 87.6k / P 272.6k，今日成交量: C 406.7k / P 383.6k，平值价格ATM: C $1.81 / P $1.40 ｜ ATM IV 19.4%，预期波动 ±0.4%，Max Pain 754
Top ΔOI: P 749 +52,370 ｜ P 740 -11,401 ｜ P 605 +10,695

📆 Forward Expiration Structure

10-07  C +27.7k / P +35.7k ｜ Activity HIGH ｜ 1D
10-08  C +6.2k / P +28.2k ｜ Activity HIGH ｜ 2D
10-09  C +19.2k / P +53.3k ｜ Activity HIGH ｜ 3D
10-12  C +5.3k / P +58.1k ｜ Activity HIGH ｜ 6D

📆 10-07 Forward Structure
存量OI: C 66.0k / P 113.4k，今日变化ΔOI: C +27.7k / P +35.7k，平值价格ATM: C $3.22 / P $2.75 ｜ ATM IV 16.6%，净 delta 敞口 961k shares
Top ΔOI: C 762 +11,990 ｜ P 701 +3,075 ｜ P 750 +3,019
仓位参考: Max Pain 750 ｜ Call Wall 762（+0.2%）（OI 13.0k） ｜ Put Wall 750（-1.4%，弱）（OI 3.6k）
量化解读： 存量 Put 重｜ATM IV 16.6%｜历史 Rank 56%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 960,664 股

📆 10-08 Forward Structure
存量OI: C 26.5k / P 85.7k，今日变化ΔOI: C +6.2k / P +28.2k，平值价格ATM: C $4.18 / P $3.70 ｜ ATM IV 16.6%，净 delta 敞口 205 shares
Top ΔOI: P 749 +11,176 ｜ P 726 +2,377
仓位参考: Max Pain 749 ｜ Call Wall 760（-0.1%，弱）（OI 1.8k） ｜ Put Wall 749（-1.5%）（OI 13.4k）
量化解读： 存量 Put 重｜ATM IV 16.6%｜历史 Rank 56%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 205 股

📆 10-09 Forward Structure
存量OI: C 171.1k / P 308.3k，今日变化ΔOI: C +19.2k / P +53.3k，平值价格ATM: C $5.25 / P $4.41 ｜ ATM IV 16.7%，净 delta 敞口 -145k shares
Top ΔOI: P 730 +5,958 ｜ P 750 +5,137 ｜ C 775 +4,304
仓位参考: Max Pain 747 ｜ Call Wall 754（-0.9%）（OI 21.2k） ｜ Put Wall 750（-1.4%，弱）（OI 8.6k）
量化解读： 存量 Put 重｜ATM IV 16.7%｜历史 Rank 56%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 144,629 股

📆 10-12 Forward Structure
存量OI: C 16.6k / P 80.5k，今日变化ΔOI: C +5.3k / P +58.1k，平值价格ATM: C $6.04 / P $5.40 ｜ ATM IV 14.4%，净 delta 敞口 -114k shares
Top ΔOI: P 738 +12,503 ｜ P 689 +4,808
仓位参考: Max Pain 750 ｜ Call Wall 755（-0.8%，弱）（OI 1.3k） ｜ Put Wall 738（-3.0%）（OI 12.6k）
量化解读： 存量 Put 重｜ATM IV 14.4%｜历史 Rank 56%（近端代理）｜IV/RV 1.02×（近似）｜净 delta 敞口 负 114,409 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/QQQ_morning.json