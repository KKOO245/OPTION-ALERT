# 期权晨报 2026-10-22（快照 10:20 ET）

📊 市场环境

SPY $764.28 ｜ QQQ $704.47
VIX 17.91 ↑7.4%（5D +8.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 19.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 769P ΔOI -6,478（距现价 +0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-27 767P ΔOI +36,716 占该期限总 OI 23.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 773.09 → 今开 766.37（-0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 767.71 ｜ 低 765.06

Options: P/C成交量 0.93 | OI比 1.09 | ATM IV 19.8% | Skew 1.3pp | Term 0.71 | ExpMove ±0.8%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜保护溢价薄（Skew 1.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.93×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.09×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 28% ｜ P/C OI(近端) 4%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 28%）｜近端持仓极端 Call 重（P/C OI 分位 4%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-23（1D）±0.8% ｜ 10-26（4D）±1.0% ｜ 10-27（5D）±1.2% ｜ 10-28（6D）±1.4%
   ⇒ IV–VIX Spread: +1.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,290,245,220 | GEX Change vs 上次快照 -977,289,545 | Flip: Primary Flip: 774.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 2985 / LOW 312 / INVALID 2001
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 774.35（全链重定价，覆盖 97%）
最近结构参考: Flip 774（现价低于该位 0.9%）
量化视角： 负 Gamma（12.90亿，历史分位 28%，中性区）｜负 Gamma 加深（9.77亿）｜现价位于 Flip 下方 0.87%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 771（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 774（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-27 767.0P — Vol 40,138 | 最新价 $2.03 | OI 525→37241 (ΔOI +36716张) | ΔOI/Volume 91.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增36716张（+6993.5% vs前日OI），连续性待观察（方向未知）
11-20 800.0C — Vol 36,660 | 最新价 $2.63 | OI 53958→81279 (ΔOI +27321张) | ΔOI/Volume 74.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27321张（+50.6% vs前日OI），连续性待观察（方向未知）
11-20 400.0P — Vol 22,162 | 最新价 $0.03 | OI 77947→97843 (ΔOI +19896张) | ΔOI/Volume 89.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19896张（+25.5% vs前日OI），连续性待观察（方向未知）
11-20 736.0P — Vol 22,264 | 最新价 $3.16 | OI 26656→42953 (ΔOI +16297张) | ΔOI/Volume 73.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16297张（+61.1% vs前日OI），连续性待观察（方向未知）
10-22 776.0C — Vol 47,975 | 最新价 $0.90 | OI 1600→17145 (ΔOI +15545张) | ΔOI/Volume 32.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15545张（+971.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 115,775 张（Put 72,909 / Call 42,866），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $13M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 181.1k / P 198.2k，今日成交量: C 562.5k / P 522.2k，平值价格ATM: C $1.38 / P $1.92 ｜ ATM IV 19.8%，预期波动 ±0.4%，Max Pain 771
Top ΔOI: C 776 +15,545 ｜ C 782 +7,819 ｜ P 770 +6,147

📆 Forward Expiration Structure

10-23  C +12.0k / P -5.8k ｜ Activity MEDIUM △ ｜ 1D
10-26  C +5.8k / P +20.4k ｜ Activity HIGH ｜ 4D
10-27  C +9.3k / P +60.4k ｜ Activity HIGH ｜ 5D
10-28  C +4.2k / P +13.5k ｜ Activity HIGH ｜ 6D

📆 10-23 Forward Structure
存量OI: C 339.8k / P 568.5k，今日变化ΔOI: C +12.0k / P -5.8k，平值价格ATM: C $2.76 / P $3.03 ｜ ATM IV 15.9%，净 delta 敞口 -432k shares
Top ΔOI: P 769 -6,478 ｜ P 774 +4,911 ｜ C 780 +4,046
仓位参考: Max Pain 770 ｜ Call Wall 790（+2.9%，弱）（OI 34.6k） ｜ Put Wall 745（-2.9%，弱）（OI 37.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 15.9%｜历史 Rank 85%（近端代理）｜IV/RV 1.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 431,547 股

📆 10-26 Forward Structure
存量OI: C 75.4k / P 127.5k，今日变化ΔOI: C +5.8k / P +20.4k，平值价格ATM: C $3.84 / P $3.99 ｜ ATM IV 11.8%，净 delta 敞口 -482k shares
Top ΔOI: P 766 +5,005 ｜ P 757 +2,368 ｜ P 767 +1,981
仓位参考: Max Pain 769 ｜ Call Wall 780（+1.6%，弱）（OI 3.6k） ｜ Put Wall 766（-0.2%，弱）（OI 25.1k）
量化解读： 存量 Put 重｜ATM IV 11.8%｜历史 Rank 85%（近端代理）｜IV/RV 1.44×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 481,575 股

📆 10-27 Forward Structure
存量OI: C 50.8k / P 103.4k，今日变化ΔOI: C +9.3k / P +60.4k，平值价格ATM: C $4.54 / P $4.65 ｜ ATM IV 12.3%，净 delta 敞口 -1.9M shares
Top ΔOI: P 767 +36,716
仓位参考: Max Pain 769 ｜ Call Wall 790（+2.9%，弱）（OI 2.4k） ｜ Put Wall 767（-0.1%）（OI 37.2k）
量化解读： 存量 Put 重｜ATM IV 12.3%｜历史 Rank 85%（近端代理）｜IV/RV 1.51×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,879,057 股

📆 10-28 Forward Structure
存量OI: C 37.7k / P 59.0k，今日变化ΔOI: C +4.2k / P +13.5k，平值价格ATM: C $5.48 / P $5.58 ｜ ATM IV 13.8%，净 delta 敞口 -187k shares
Top ΔOI: P 760 +2,257 ｜ P 740 +1,934 ｜ P 715 +1,000
仓位参考: Max Pain 770 ｜ Call Wall 785（+2.3%，弱）（OI 2.6k） ｜ Put Wall 760（-1.0%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 13.8%｜历史 Rank 85%（近端代理）｜IV/RV 1.69×（近似）｜净 delta 敞口 负 186,867 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/SPY_morning.json