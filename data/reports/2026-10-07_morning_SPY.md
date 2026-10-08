# 期权晨报 2026-10-07（快照 10:20 ET）

📊 市场环境

SPY $777.22 ｜ QQQ $757.73
VIX 15.79 ↑5.2%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　✅ 今日已公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-08 749P ΔOI +3,072（距现价 -3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-13 700P ΔOI +9,772 占该期限总 OI 12.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 779.09 → 今开 775.77（-0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 776.15 ｜ 低 774.03

Options: P/C成交量 1.58 | OI比 1.30 | ATM IV 15.1% | Skew 1.7pp | Term 0.86 | ExpMove ±0.6%（近端） | Rank 65%
量化视角： IV 中性（Rank 65%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价薄（Skew 1.7pp）｜当日成交偏 Put（P/C量 1.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.58×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.30×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 51% ｜ P/C OI(近端) 11%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 51%）｜近端持仓结构中性（P/C OI 分位 11%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-08（1D）±0.6% ｜ 10-09（2D）±0.8% ｜ 10-12（5D）±0.9% ｜ 10-13（6D）±1.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -221,481,057 | GEX Change vs 上次快照 -1,499,270,787 | Flip: Primary Flip: 775.46（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 2646 / LOW 414 / INVALID 1850
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 775.46（全链重定价，覆盖 96%）
Call Wall 785（弱结构｜现价低于该位 1.3%）
最近结构参考: Flip 775（现价低于该位 0.1%）
量化视角： 负 Gamma（2.21亿，历史分位 51%，中性区）｜由正转负（14.99亿）｜现价位于 Flip 下方 0.10%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 778（MaxPain，仅结算参考） / 785（Call Wall，弱结构）。
• Gamma 区域：切换参考 775（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 740.0P — Vol 78,223 | 最新价 $1.55 | OI 7830→81801 (ΔOI +73971张) | ΔOI/Volume 94.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增73971张（+944.7% vs前日OI），连续性待观察（方向未知）
10-14 790.0C — Vol 89,733 | 最新价 $1.12 | OI 801→71215 (ΔOI +70414张) | ΔOI/Volume 78.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增70414张（+8790.8% vs前日OI），连续性待观察（方向未知）
10-16 750.0P — Vol 22,326 | 最新价 $0.49 | OI 59283→73195 (ΔOI +13912张) | ΔOI/Volume 62.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13912张（+23.5% vs前日OI），连续性待观察（方向未知）
10-07 742.0P — Vol 40,118 | 最新价 $0.01 | OI 8631→21870 (ΔOI +13239张) | ΔOI/Volume 33.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13239张（+153.4% vs前日OI），连续性待观察（方向未知）
10-07 780.0C — Vol 125,449 | 最新价 $1.28 | OI 3511→14120 (ΔOI +10609张) | ΔOI/Volume 8.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10609张（+302.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 182,145 张（Put 101,122 / Call 81,023），跨 4 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $11M，买/卖方向不可观测）｜彩票/名义 1 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 235.2k / P 306.9k，今日成交量: C 465.4k / P 736.7k，平值价格ATM: C $1.08 / P $1.50 ｜ ATM IV 15.1%，预期波动 ±0.3%，Max Pain 778
Top ΔOI: P 742 +13,239 ｜ C 780 +10,609 ｜ P 779 +9,750

📆 Forward Expiration Structure

10-08  C +18.6k / P +28.6k ｜ Activity HIGH ｜ 1D
10-09  C +20.5k / P +64.5k ｜ Activity HIGH ｜ 2D
10-12  C +10.7k / P +26.9k ｜ Activity HIGH ｜ 5D
10-13  C +9.8k / P +26.2k ｜ Activity HIGH ｜ 6D

📆 10-08 Forward Structure
存量OI: C 82.3k / P 113.2k，今日变化ΔOI: C +18.6k / P +28.6k，平值价格ATM: C $2.07 / P $2.39 ｜ ATM IV 12.2%，净 delta 敞口 -1.0M shares
Top ΔOI: C 816 +4,407 ｜ P 749 +3,072 ｜ C 792 +2,596
仓位参考: Max Pain 775 ｜ Call Wall 796（+2.8%，弱）（OI 7.0k） ｜ Put Wall 770（-0.6%，弱）（OI 4.0k）
量化解读： 存量 Put 重｜ATM IV 12.2%｜历史 Rank 65%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,015,364 股

📆 10-09 Forward Structure
存量OI: C 520.4k / P 629.0k，今日变化ΔOI: C +20.5k / P +64.5k，平值价格ATM: C $2.87 / P $2.93 ｜ ATM IV 11.7%，净 delta 敞口 -2.8M shares
Top ΔOI: P 779 +6,542 ｜ P 767 +5,974 ｜ P 780 +5,470
仓位参考: Max Pain 772 ｜ Call Wall 785（+1.3%）（OI 123.0k） ｜ Put Wall 767（-1.0%，弱）（OI 70.5k）
量化解读： 存量 Put 重｜ATM IV 11.7%｜历史 Rank 65%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 2,772,506 股

📆 10-12 Forward Structure
存量OI: C 47.8k / P 99.2k，今日变化ΔOI: C +10.7k / P +26.9k，平值价格ATM: C $3.50 / P $3.55 ｜ ATM IV 9.4%，净 delta 敞口 -539k shares
Top ΔOI: P 734 +8,277 ｜ P 739 +4,003 ｜ P 729 +3,832
仓位参考: Max Pain 775 ｜ Call Wall 785（+1.3%，弱）（OI 3.1k） ｜ Put Wall 770（-0.6%，弱）（OI 3.5k）
量化解读： 存量 Put 重｜ATM IV 9.4%｜历史 Rank 65%（近端代理）｜IV/RV 1.01×（近似）｜净 delta 敞口 负 539,408 股

📆 10-13 Forward Structure
存量OI: C 27.9k / P 52.3k，今日变化ΔOI: C +9.8k / P +26.2k，平值价格ATM: C $4.03 / P $3.99 ｜ ATM IV 9.8%，净 delta 敞口 -370k shares
Top ΔOI: P 700 +9,772 ｜ P 710 +2,260
仓位参考: Max Pain 775 ｜ Call Wall 780（+0.7%，弱）（OI 1.5k）
量化解读： 存量 Put 重｜ATM IV 9.8%｜历史 Rank 65%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 负 370,411 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/SPY_morning.json