# 期权晨报 2026-11-16（快照 10:20 ET）

📊 市场环境

SPY $744.62 ｜ QQQ $664.10
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
🟡 **近现价集中开仓**: 11-17 760C ΔOI +3,749（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-19 650P ΔOI +11,458 占该期限总 OI 10.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 754.37 → 今开 749.66（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 749.82 ｜ 低 744.00

Options: P/C成交量 1.93 | OI比 1.00 | ATM IV 29.6% | Skew 3.8pp | Term 0.57 | ExpMove ±1.1%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.57，近月 IV 高于远月）｜保护溢价中性（Skew 3.8pp）｜当日成交偏 Put（P/C量 1.93）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.93×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.00×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 31% ｜ P/C OI(近端) 2%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 31%）｜近端持仓极端 Call 重（P/C OI 分位 2%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-17（1D）±1.1% ｜ 11-18（2D）±1.5% ｜ 11-19（3D）±1.7% ｜ 11-20（4D）±1.9%
   ⇒ IV–VIX Spread: +8.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,126,168,703 | GEX Change vs 上次快照 -476,203,828 | Flip: Primary Flip: 756.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 3213 / LOW 310 / INVALID 1499
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 756.33（全链重定价，覆盖 97%）
最近结构参考: Flip 756（现价低于该位 1.4%）
量化视角： 负 Gamma（11.26亿，历史分位 31%，中性区）｜负 Gamma 加深（4.76亿）｜现价位于 Flip 下方 1.41%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 753（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 756（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-16 745.0C — Vol 111,322 | 最新价 $8.68 | OI 833→17113 (ΔOI +16280张) | ΔOI/Volume 14.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16280张（+1954.4% vs前日OI），连续性待观察（方向未知）
11-19 650.0P — Vol 11,538 | 最新价 $0.08 | OI 32→11490 (ΔOI +11458张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11458张（+35806.2% vs前日OI），连续性待观察（方向未知）
11-20 635.0P — Vol 12,191 | 最新价 $0.11 | OI 9116→20526 (ΔOI +11410张) | ΔOI/Volume 93.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11410张（+125.2% vs前日OI），连续性待观察（方向未知）
12-04 675.0P — Vol 12,099 | 最新价 $1.00 | OI 1255→11776 (ΔOI +10521张) | ΔOI/Volume 87.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10521张（+838.3% vs前日OI），连续性待观察（方向未知）
11-18 731.0P — Vol 12,693 | 最新价 $0.91 | OI 570→10369 (ΔOI +9799张) | ΔOI/Volume 77.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9799张（+1719.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 59,468 张（Put 43,188 / Call 16,280），跨 5 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 251.1k / P 252.1k，今日成交量: C 429.2k / P 827.7k，平值价格ATM: C $1.92 / P $2.84 ｜ ATM IV 29.6%，预期波动 ±0.6%，Max Pain 753
Top ΔOI: C 745 +16,280 ｜ C 750 +9,273 ｜ C 763 +8,913

📆 Forward Expiration Structure

11-17  C +27.8k / P +21.1k ｜ Activity HIGH ｜ 1D
11-18  C +22.8k / P +17.2k ｜ Activity HIGH ｜ 2D
11-19  C +8.8k / P +25.3k ｜ Activity HIGH ｜ 3D
11-20  C +30.5k / P +44.1k ｜ Activity HIGH ｜ 4D

📆 11-17 Forward Structure
存量OI: C 73.8k / P 73.3k，今日变化ΔOI: C +27.8k / P +21.1k，平值价格ATM: C $3.80 / P $4.65 ｜ ATM IV 24.4%，净 delta 敞口 -422k shares
Top ΔOI: C 760 +3,749 ｜ C 765 +3,225 ｜ C 758 +2,674
仓位参考: Max Pain 753 ｜ Call Wall 760（+1.9%，弱）（OI 5.3k） ｜ Put Wall 750（+0.6%）（OI 4.3k）
量化解读： 存量两侧均衡｜ATM IV 24.4%｜历史 Rank 96%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 422,324 股

📆 11-18 Forward Structure
存量OI: C 78.7k / P 95.4k，今日变化ΔOI: C +22.8k / P +17.2k，平值价格ATM: C $5.10 / P $6.00 ｜ ATM IV 23.8%，净 delta 敞口 -168k shares
Top ΔOI: P 731 +9,799 ｜ C 762 +3,297 ｜ C 767 +3,088
仓位参考: Max Pain 755 ｜ Call Wall 767（+2.9%，弱）（OI 3.8k） ｜ Put Wall 731（-2.0%，弱）（OI 10.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 23.8%｜历史 Rank 96%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 167,593 股

📆 11-19 Forward Structure
存量OI: C 38.8k / P 68.1k，今日变化ΔOI: C +8.8k / P +25.3k，平值价格ATM: C $6.00 / P $6.88 ｜ ATM IV 22.8%，净 delta 敞口 -244k shares
Top ΔOI: P 650 +11,458 ｜ P 750 +1,712
仓位参考: Max Pain 754 ｜ Call Wall 764（+2.5%，弱）（OI 1.9k） ｜ Put Wall 750（+0.6%，弱）（OI 2.4k）
量化解读： 存量 Put 重｜ATM IV 22.8%｜历史 Rank 96%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 243,590 股

📆 11-20 Forward Structure
存量OI: C 854.9k / P 2937.3k，今日变化ΔOI: C +30.5k / P +44.1k，平值价格ATM: C $6.94 / P $7.49 ｜ ATM IV 22.3%，净 delta 敞口 -68k shares
Top ΔOI: P 635 +11,410 ｜ P 737 -8,775 ｜ P 727 +8,597
仓位参考: Max Pain 757 ｜ Put Wall 725（-2.8%，弱）（OI 66.9k）
量化解读： 存量 Put 重｜ATM IV 22.3%｜历史 Rank 96%（近端代理）｜IV/RV 1.02×（近似）｜净 delta 敞口 负 67,636 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/SPY_morning.json