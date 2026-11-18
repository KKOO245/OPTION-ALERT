# 期权晨报 2026-11-18（快照 10:20 ET）

📊 市场环境

SPY $731.20 ｜ QQQ $659.28
VIX 24.58 ↓3.5%（5D +40.5%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 26.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-19 707P ΔOI +18,599（距现价 -3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 732.44 → 今开 733.37（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 735.06 ｜ 低 728.58

Options: P/C成交量 1.17 | OI比 0.86 | ATM IV 36.2% | Skew 3.9pp | Term 0.54 | ExpMove ±1.4%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.54，近月 IV 高于远月）｜保护溢价中性（Skew 3.9pp）｜当日成交偏 Put（P/C量 1.17）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.17×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 20% ｜ P/C OI(近端) 1%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 20%）｜近端持仓极端 Call 重（P/C OI 分位 1%，历史极低区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-19（1D）±1.4% ｜ 11-20（2D）±1.7% ｜ 11-23（5D）±2.1% ｜ 11-24（6D）±2.3%
   ⇒ IV–VIX Spread: +11.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,725,272,057 | GEX Change vs 上次快照 220,214,011 | Flip: Primary Flip: 750.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 2949 / LOW 312 / INVALID 1571
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 750.43（全链重定价，覆盖 95%）
最近结构参考: Flip 750（现价低于该位 2.4%）
量化视角： 负 Gamma（17.25亿，历史分位偏负区，比 80% 的交易日更负）｜负 Gamma 缓解（+2.20亿）｜现价位于 Flip 下方 2.38%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 738（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 750（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 700.0P — Vol 62,692 | 最新价 $4.95 | OI 8404→67992 (ΔOI +59588张) | ΔOI/Volume 95.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增59588张（+709.0% vs前日OI），连续性待观察（方向未知）
11-27 675.0P — Vol 46,309 | 最新价 $1.35 | OI 2928→46614 (ΔOI +43686张) | ΔOI/Volume 94.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增43686张（+1492.0% vs前日OI），连续性待观察（方向未知）
12-04 675.0P — Vol 46,914 | 最新价 $2.64 | OI 11697→49804 (ΔOI +38107张) | ΔOI/Volume 81.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增38107张（+325.8% vs前日OI），连续性待观察（方向未知）
11-27 700.0P — Vol 52,537 | 最新价 $2.96 | OI 21318→53045 (ΔOI +31727张) | ΔOI/Volume 60.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31727张（+148.8% vs前日OI），连续性待观察（方向未知）
12-04 720.0P — Vol 16,467 | 最新价 $8.87 | OI 6438→28922 (ΔOI +22484张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22484张（+349.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 195,592 张（Put 195,592 / Call 0），跨 2 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $75M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 216.3k / P 186.5k，今日成交量: C 696.3k / P 814.8k，平值价格ATM: C $2.66 / P $3.08 ｜ ATM IV 36.2%，预期波动 ±0.8%，Max Pain 738
Top ΔOI: C 744 +10,982 ｜ C 740 +9,423 ｜ C 750 +8,182

📆 Forward Expiration Structure

11-19  C +41.6k / P +50.8k ｜ Activity HIGH ｜ 1D
11-20  C +79.7k / P -24.1k ｜ Activity HIGH ｜ 2D
11-23  C +23.1k / P +9.4k ｜ Activity HIGH ｜ 5D
11-24  C +11.7k / P +12.8k ｜ Activity HIGH ｜ 6D

📆 11-19 Forward Structure
存量OI: C 101.1k / P 137.0k，今日变化ΔOI: C +41.6k / P +50.8k，平值价格ATM: C $4.87 / P $5.16 ｜ ATM IV 29.2%，净 delta 敞口 501k shares
Top ΔOI: P 707 +18,599 ｜ C 748 +5,043 ｜ C 743 +2,951
仓位参考: Max Pain 740 ｜ Call Wall 748（+2.1%）（OI 5.9k）
量化解读： 存量 Put 重｜ATM IV 29.2%｜历史 Rank 98%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 500,948 股

📆 11-20 Forward Structure
存量OI: C 986.1k / P 2939.5k，今日变化ΔOI: C +79.7k / P -24.1k，平值价格ATM: C $6.27 / P $6.33 ｜ ATM IV 27.4%，净 delta 敞口 7.3M shares
Top ΔOI: P 580 +10,400 ｜ P 740 -10,326 ｜ C 730 +9,560
仓位参考: Max Pain 750 ｜ Put Wall 725（-1.0%，弱）（OI 68.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 27.4%｜历史 Rank 98%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 7,310,422 股

📆 11-23 Forward Structure
存量OI: C 69.0k / P 57.0k，今日变化ΔOI: C +23.1k / P +9.4k，平值价格ATM: C $7.68 / P $7.62 ｜ ATM IV 21.8%，净 delta 敞口 238k shares
Top ΔOI: C 798 +2,574 ｜ P 690 +2,296 ｜ C 748 +1,855
仓位参考: Max Pain 745 ｜ Call Wall 752（+2.6%，弱）（OI 2.4k） ｜ Put Wall 736（+0.5%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 21.8%｜历史 Rank 98%（近端代理）｜IV/RV 0.96×（近似）｜净 delta 敞口 正 238,233 股

📆 11-24 Forward Structure
存量OI: C 36.9k / P 34.8k，今日变化ΔOI: C +11.7k / P +12.8k，平值价格ATM: C $8.58 / P $8.54 ｜ ATM IV 22.1%，净 delta 敞口 18k shares
Top ΔOI: P 725 +2,243 ｜ P 705 +1,466 ｜ P 690 +1,050
仓位参考: Max Pain 743 ｜ Call Wall 754（+2.9%，弱）（OI 1.4k） ｜ Put Wall 725（-1.0%）（OI 3.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 22.1%｜历史 Rank 98%（近端代理）｜IV/RV 0.97×（近似）｜净 delta 敞口 正 17,950 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/SPY_morning.json