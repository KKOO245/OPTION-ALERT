# 期权晨报 2026-10-08（快照 10:20 ET）

📊 市场环境

SPY $774.21 ｜ QQQ $747.58
VIX 15.43 ↑2.3%（5D -5.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-09 760C ΔOI +4,234（距现价 +0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 757.73 → 今开 753.94（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 755.40 ｜ 低 752.11

Options: P/C成交量 1.07 | OI比 2.30 | ATM IV 18.9% | Skew 1.5pp | Term 0.99 | ExpMove ±0.8%（近端） | Rank 53%
量化视角： IV 中性（Rank 53%）｜期限结构正常（Term 0.99）｜保护溢价薄（Skew 1.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.07×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.30×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 40% ｜ P/C OI(近端) 88%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 40%）｜近端持仓结构中性（P/C OI 分位 88%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-09（1D）±0.8% ｜ 10-12（4D）±1.1% ｜ 10-13（5D）±1.3% ｜ 10-14（6D）±1.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -160,648,338 | GEX Change vs 上次快照 -395,582,489 | Flip: Primary Flip: 755.04（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 2800 / LOW 288 / INVALID 1962
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 755.04（全链重定价，覆盖 97%）
Call Wall 760（现价低于该位 0.9%）
最近结构参考: Flip 755（现价低于该位 0.2%）
量化视角： 负 Gamma（1.61亿，历史分位 40%，中性区）｜由正转负（3.96亿）｜现价位于 Flip 下方 0.24%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 757（MaxPain，仅结算参考） / 760（Call Wall）。
• Gamma 区域：切换参考 755（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 730.0P — Vol 21,021 | 最新价 $2.69 | OI 2520→22173 (ΔOI +19653张) | ΔOI/Volume 93.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19653张（+779.9% vs前日OI），连续性待观察（方向未知）
10-12 450.0P — Vol 15,000 | 最新价 $0.01 | OI 110→15110 (ΔOI +15000张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15000张（+13636.4% vs前日OI），连续性待观察（方向未知）
10-08 750.0P — Vol 52,742 | 最新价 $0.30 | OI 1469→13710 (ΔOI +12241张) | ΔOI/Volume 23.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12241张（+833.3% vs前日OI），连续性待观察（方向未知）
11-06 717.0P — Vol 10,107 | 最新价 $4.84 | OI 106→10144 (ΔOI +10038张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10038张（+9469.8% vs前日OI），连续性待观察（方向未知）
11-06 680.0P — Vol 10,069 | 最新价 $1.67 | OI 3059→13089 (ΔOI +10030张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10030张（+327.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 66,962 张（Put 66,962 / Call 0），跨 4 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $12M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 97.2k / P 223.8k，今日成交量: C 352.2k / P 378.3k，平值价格ATM: C $1.94 / P $1.17 ｜ ATM IV 18.9%，预期波动 ±0.4%，Max Pain 757
Top ΔOI: P 750 +12,241 ｜ C 765 +9,621 ｜ P 748 +8,557

📆 Forward Expiration Structure

10-09  C +15.7k / P +39.5k ｜ Activity HIGH ｜ 1D
10-12  C +4.6k / P +32.6k ｜ Activity HIGH ｜ 4D
10-13  C +3.0k / P +8.1k ｜ Activity HIGH ｜ 5D
10-14  C +3.1k / P +9.8k ｜ Activity HIGH ｜ 6D

📆 10-09 Forward Structure
存量OI: C 202.3k / P 394.8k，今日变化ΔOI: C +15.7k / P +39.5k，平值价格ATM: C $3.53 / P $2.44 ｜ ATM IV 16.7%，净 delta 敞口 -278k shares
Top ΔOI: C 760 +4,234 ｜ P 738 +3,297
仓位参考: Max Pain 751 ｜ Call Wall 754（+0.1%，弱）（OI 20.2k） ｜ Put Wall 754（+0.1%，弱）（OI 21.6k）
量化解读： 存量 Put 重｜ATM IV 16.7%｜历史 Rank 53%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 278,243 股

📆 10-12 Forward Structure
存量OI: C 30.8k / P 126.8k，今日变化ΔOI: C +4.6k / P +32.6k，平值价格ATM: C $4.69 / P $3.57 ｜ ATM IV 12.6%，净 delta 敞口 -172k shares
Top ΔOI: P 742 +6,162 ｜ P 755 +1,545
仓位参考: Max Pain 754 ｜ Call Wall 765（+1.6%，弱）（OI 1.8k） ｜ Put Wall 738（-2.0%，弱）（OI 12.7k）
量化解读： 存量 Put 重｜ATM IV 12.6%｜历史 Rank 53%（近端代理）｜IV/RV 0.95×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 172,255 股

📆 10-13 Forward Structure
存量OI: C 17.3k / P 77.1k，今日变化ΔOI: C +3.0k / P +8.1k，平值价格ATM: C $5.48 / P $4.30 ｜ ATM IV 13.5%，净 delta 敞口 -7k shares
Top ΔOI: P 726 +2,321 ｜ C 773 +600
仓位参考: Max Pain 753 ｜ Call Wall 772（+2.5%，弱）（OI 1.3k） ｜ Put Wall 740（-1.8%，弱）（OI 11.1k）
量化解读： 存量 Put 重｜ATM IV 13.5%｜历史 Rank 53%（近端代理）｜IV/RV 1.02×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 6,779 股

📆 10-14 Forward Structure
存量OI: C 14.7k / P 36.1k，今日变化ΔOI: C +3.1k / P +9.8k，平值价格ATM: C $6.16 / P $5.40 ｜ ATM IV 14.9%，净 delta 敞口 -104k shares
Top ΔOI: P 730 +1,948 ｜ P 720 +1,468 ｜ C 771 +1,167
仓位参考: Max Pain 753 ｜ Call Wall 755（+0.2%，弱）（OI 2.3k） ｜ Put Wall 742（-1.5%，弱）（OI 1.5k）
量化解读： 存量 Put 重｜ATM IV 14.9%｜历史 Rank 53%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 负 103,658 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/QQQ_morning.json