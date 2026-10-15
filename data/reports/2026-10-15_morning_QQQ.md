# 期权晨报 2026-10-15（快照 10:20 ET）

📊 市场环境

SPY $766.64 ｜ QQQ $720.69
VIX 17.51 ↑3.8%（5D +13.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 740C ΔOI +13,699（距现价 +3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 728.95 → 今开 718.54（-1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 721.45 ｜ 低 715.43

Options: P/C成交量 0.98 | OI比 1.50 | ATM IV 34.9% | Skew 3.2pp | Term 0.63 | ExpMove ±1.3%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.63，近月 IV 高于远月）｜保护溢价中性（Skew 3.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.98×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.50×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 2% ｜ P/C OI(近端) 38%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 2%）｜近端持仓结构中性（P/C OI 分位 38%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-16（1D）±1.3% ｜ 10-19（4D）±1.7% ｜ 10-20（5D）±2.0% ｜ 10-21（6D）±2.3%
   ⇒ IV–VIX Spread: +17.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,364,589,840 | GEX Change vs 上次快照 -336,303,720 | Flip: Primary Flip: 739.04（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3034 / LOW 371 / INVALID 1553
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 739.04（全链重定价，覆盖 96%）
Put Wall 700（弱结构｜现价高于该位 2.6%）
最近结构参考: Put Wall 700（现价高于该位 2.6%）
量化视角： 负 Gamma（13.65亿，历史分位偏负区，比 98% 的交易日更负）｜负 Gamma 加深（3.36亿）｜现价位于 Flip 下方 2.79%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 734（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 739（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 710.0P — Vol 36,944 | 最新价 $3.40 | OI 3608→34702 (ΔOI +31094张) | ΔOI/Volume 84.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31094张（+861.8% vs前日OI），连续性待观察（方向未知）
10-15 570.0P — Vol 16,447 | 最新价 $0.01 | OI 479→16641 (ΔOI +16162张) | ΔOI/Volume 98.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16162张（+3374.1% vs前日OI），连续性待观察（方向未知）
10-16 740.0C — Vol 68,569 | 最新价 $0.96 | OI 24693→38392 (ΔOI +13699张) | ΔOI/Volume 20.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13699张（+55.5% vs前日OI），连续性待观察（方向未知）
10-15 735.0C — Vol 60,207 | 最新价 $1.11 | OI 302→13148 (ΔOI +12846张) | ΔOI/Volume 21.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12846张（+4253.6% vs前日OI），连续性待观察（方向未知）
10-16 735.0C — Vol 44,775 | 最新价 $2.10 | OI 10961→21928 (ΔOI +10967张) | ΔOI/Volume 24.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10967张（+100.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 84,768 张（Put 47,256 / Call 37,512），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $11M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 153.2k / P 229.8k，今日成交量: C 442.8k / P 451.5k，平值价格ATM: C $2.00 / P $3.66 ｜ ATM IV 34.9%，预期波动 ±0.8%，Max Pain 734
Top ΔOI: P 570 +16,162 ｜ C 735 +12,846 ｜ C 740 +8,607

📆 Forward Expiration Structure

10-16  C +48.8k / P +12.6k ｜ Activity HIGH ｜ 1D
10-19  C +18.4k / P +12.2k ｜ Activity HIGH ｜ 4D
10-20  C +14.2k / P +8.9k ｜ Activity HIGH ｜ 5D
10-21  C +7.8k / P +10.9k ｜ Activity HIGH ｜ 6D

📆 10-16 Forward Structure
存量OI: C 782.5k / P 1312.7k，今日变化ΔOI: C +48.8k / P +12.6k，平值价格ATM: C $4.05 / P $5.40 ｜ ATM IV 27.8%，净 delta 敞口 2.8M shares
Top ΔOI: C 740 +13,699 ｜ C 735 +10,967
仓位参考: Max Pain 732 ｜ Call Wall 740（+3.0%，弱）（OI 38.4k） ｜ Put Wall 700（-2.6%，弱）（OI 60.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 27.8%｜历史 Rank 94%（近端代理）｜IV/RV 2.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,763,070 股

📆 10-19 Forward Structure
存量OI: C 54.8k / P 86.7k，今日变化ΔOI: C +18.4k / P +12.2k，平值价格ATM: C $5.70 / P $6.67 ｜ ATM IV 19.9%，净 delta 敞口 -190k shares
Top ΔOI: C 753 +3,822 ｜ P 720 +3,173 ｜ P 728 +3,028
仓位参考: Max Pain 740 ｜ Call Wall 740（+3.0%，弱）（OI 2.3k） ｜ Put Wall 720（+0.2%，弱）（OI 6.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 19.9%｜历史 Rank 94%（近端代理）｜IV/RV 1.61×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 189,579 股

📆 10-20 Forward Structure
存量OI: C 41.3k / P 46.1k，今日变化ΔOI: C +14.2k / P +8.9k，平值价格ATM: C $6.56 / P $7.90 ｜ ATM IV 20.6%，净 delta 敞口 -40k shares
Top ΔOI: C 733 +4,176 ｜ C 740 +1,815
仓位参考: Max Pain 733 ｜ Call Wall 733（+2.0%，弱）（OI 4.2k） ｜ Put Wall 726（+1.1%，弱）（OI 2.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 20.6%｜历史 Rank 94%（近端代理）｜IV/RV 1.67×（近似）｜净 delta 敞口 负 40,346 股

📆 10-21 Forward Structure
存量OI: C 23.6k / P 33.9k，今日变化ΔOI: C +7.8k / P +10.9k，平值价格ATM: C $7.34 / P $8.99 ｜ ATM IV 21.3%，净 delta 敞口 -173k shares
Top ΔOI: C 749 +1,263 ｜ P 650 +1,006
仓位参考: Max Pain 740 ｜ Call Wall 730（+1.6%，弱）（OI 0.8k） ｜ Put Wall 710（-1.2%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 21.3%｜历史 Rank 94%（近端代理）｜IV/RV 1.73×（近似）｜净 delta 敞口 负 172,962 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 27.8% vs 10-19 19.9%（差 +7.9pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/QQQ_morning.json