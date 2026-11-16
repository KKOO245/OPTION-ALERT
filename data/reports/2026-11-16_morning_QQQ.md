# 期权晨报 2026-11-16（快照 10:20 ET）

📊 市场环境

SPY $744.62 ｜ QQQ $664.17
VIX 21.57 ↑11.8%（5D +8.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 35.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.8
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-17 655P ΔOI +2,715（距现价 -1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 679.89 → 今开 671.05（-1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 672.14 ｜ 低 663.96

Options: P/C成交量 1.18 | OI比 1.38 | ATM IV 45.4% | Skew 4.8pp | Term 0.62 | ExpMove ±1.9%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.62，近月 IV 高于远月）｜保护溢价中性（Skew 4.8pp）｜当日成交偏 Put（P/C量 1.18）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.18×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.38×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 16% ｜ P/C OI(近端) 27%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 16%）｜近端持仓结构中性（P/C OI 分位 27%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-17（1D）±1.9% ｜ 11-18（2D）±2.5% ｜ 11-19（3D）±3.0% ｜ 11-20（4D）±3.3%
   ⇒ IV–VIX Spread: +23.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -600,277,319 | GEX Change vs 上次快照 -252,508,948 | Flip: Primary Flip: 685.95（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3648 / LOW 463 / INVALID 1317
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 685.95（全链重定价，覆盖 96%）
Put Wall 680（弱结构｜现价低于该位 2.0%）
最近结构参考: Put Wall 680（现价低于该位 2.0%）
量化视角： 负 Gamma（6.00亿，历史分位偏负区，比 84% 的交易日更负）｜负 Gamma 加深（2.53亿）｜现价位于 Flip 下方 2.86%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 680（Put Wall，弱结构） / 680（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 686（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-16 670.0P — Vol 40,715 | 最新价 $2.57 | OI 1778→13729 (ΔOI +11951张) | ΔOI/Volume 29.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11951张（+672.2% vs前日OI），连续性待观察（方向未知）
11-30 550.0P — Vol 10,321 | 最新价 $0.50 | OI 6387→16334 (ΔOI +9947张) | ΔOI/Volume 96.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9947张（+155.7% vs前日OI），连续性待观察（方向未知）
11-16 650.0P — Vol 18,772 | 最新价 $0.36 | OI 1092→10423 (ΔOI +9331张) | ΔOI/Volume 49.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9331张（+854.5% vs前日OI），连续性待观察（方向未知）
11-16 690.0C — Vol 26,955 | 最新价 $0.67 | OI 2174→9800 (ΔOI +7626张) | ΔOI/Volume 28.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7626张（+350.8% vs前日OI），连续性待观察（方向未知）
11-20 703.0C — Vol 7,558 | 最新价 $1.75 | OI 1498→8273 (ΔOI +6775张) | ΔOI/Volume 89.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6775张（+452.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 45,630 张（Put 31,229 / Call 14,401），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 149.6k / P 207.1k，今日成交量: C 441.9k / P 521.6k，平值价格ATM: C $3.00 / P $3.55 ｜ ATM IV 45.4%，预期波动 ±1.0%，Max Pain 680
Top ΔOI: P 670 +11,951 ｜ P 650 +9,331 ｜ C 690 +7,626

📆 Forward Expiration Structure

11-17  C +12.4k / P +21.4k ｜ Activity HIGH ｜ 1D
11-18  C +12.6k / P +15.5k ｜ Activity HIGH ｜ 2D
11-19  C +14.2k / P +15.5k ｜ Activity HIGH ｜ 3D
11-20  C +43.0k / P +59.0k ｜ Activity MEDIUM △ ｜ 4D

📆 11-17 Forward Structure
存量OI: C 55.6k / P 80.4k，今日变化ΔOI: C +12.4k / P +21.4k，平值价格ATM: C $6.18 / P $6.60 ｜ ATM IV 40.4%，净 delta 敞口 -467k shares
Top ΔOI: P 655 +2,715 ｜ P 659 +2,555 ｜ P 656 +2,480
仓位参考: Max Pain 680 ｜ Put Wall 680（+2.1%）（OI 5.6k）
量化解读： 存量 Put 重｜ATM IV 40.4%｜历史 Rank 98%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 466,980 股

📆 11-18 Forward Structure
存量OI: C 37.4k / P 78.7k，今日变化ΔOI: C +12.6k / P +15.5k，平值价格ATM: C $8.23 / P $8.61 ｜ ATM IV 40.5%，净 delta 敞口 -261k shares
Top ΔOI: P 650 +5,031 ｜ P 660 +1,637 ｜ C 700 +1,615
仓位参考: Max Pain 678 ｜ Call Wall 678（+1.8%，弱）（OI 2.0k） ｜ Put Wall 650（-2.5%，弱）（OI 5.6k）
量化解读： 存量 Put 重｜ATM IV 40.5%｜历史 Rank 98%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 261,308 股

📆 11-19 Forward Structure
存量OI: C 31.2k / P 55.0k，今日变化ΔOI: C +14.2k / P +15.5k，平值价格ATM: C $9.78 / P $10.19 ｜ ATM IV 39.8%，净 delta 敞口 -365k shares
Top ΔOI: C 705 +6,548 ｜ P 664 +4,992 ｜ C 725 +1,768
仓位参考: Max Pain 680 ｜ Put Wall 664（-0.3%，弱）（OI 5.1k）
量化解读： 存量 Put 重｜ATM IV 39.8%｜历史 Rank 98%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 365,264 股

11-20（MEDIUM △）Top ΔOI: 703C +6,775 ｜ 530P +6,569
11-20（MEDIUM △）仓位参考: Max Pain 696 ｜ Call Wall 680（+2.1%，弱）（OI 35.6k） ｜ Put Wall 680（+2.1%）（OI 86.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/QQQ_morning.json