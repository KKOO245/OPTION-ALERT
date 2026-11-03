# 期权晨报 2026-11-03（快照 10:20 ET）

📊 市场环境

SPY $753.95 ｜ QQQ $685.52
VIX 21.03 ↓0.6%（5D +20.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-03

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.1 ｜ 实际 7.523 ｜ 前值 7.19　✅ 今日已公布
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-04 756P ΔOI +12,398（距现价 +0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 752.10 → 今开 752.73（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 754.86 ｜ 低 752.41

Options: P/C成交量 0.67 | OI比 1.37 | ATM IV 24.5% | Skew 2.1pp | Term 0.68 | ExpMove ±1.2%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.68，近月 IV 高于远月）｜保护溢价中性（Skew 2.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.37×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 24% ｜ P/C OI(近端) 15%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 24%）｜近端持仓结构中性（P/C OI 分位 15%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-04（1D）±1.2% ｜ 11-05（2D）±1.4% ｜ 11-06（3D）±1.7% ｜ 11-09（6D）±2.0%
   ⇒ IV–VIX Spread: +3.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,490,919,296 | GEX Change vs 上次快照 -64,350,515 | Flip: Primary Flip: 768.54（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 2517 / LOW 311 / INVALID 2276
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 768.54（全链重定价，覆盖 98%）
最近结构参考: Flip 769（现价低于该位 1.9%）
量化视角： 负 Gamma（14.91亿，历史分位偏负区，比 76% 的交易日更负）｜负 Gamma 加深（6435万）｜现价位于 Flip 下方 1.93%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 756（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 769（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 740.0P — Vol 84,482 | 最新价 $7.33 | OI 57611→129312 (ΔOI +71701张) | ΔOI/Volume 84.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增71701张（+124.5% vs前日OI），连续性待观察（方向未知）
11-13 745.0P — Vol 58,619 | 最新价 $6.65 | OI 15862→72530 (ΔOI +56668张) | ΔOI/Volume 96.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增56668张（+357.3% vs前日OI），连续性待观察（方向未知）
11-13 730.0P — Vol 62,023 | 最新价 $3.47 | OI 11572→64485 (ΔOI +52913张) | ΔOI/Volume 85.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增52913张（+457.2% vs前日OI），连续性待观察（方向未知）
11-20 716.0P — Vol 33,141 | 最新价 $3.40 | OI 13441→38398 (ΔOI +24957张) | ΔOI/Volume 75.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24957张（+185.7% vs前日OI），连续性待观察（方向未知）
11-20 725.0P — Vol 36,253 | 最新价 $4.48 | OI 106617→126208 (ΔOI +19591张) | ΔOI/Volume 54.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19591张（+18.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 225,830 张（Put 225,830 / Call 0），跨 2 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $126M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 183.1k / P 251.1k，今日成交量: C 524.8k / P 351.6k，平值价格ATM: C $1.67 / P $2.38 ｜ ATM IV 24.5%，预期波动 ±0.5%，Max Pain 756
Top ΔOI: P 715 +13,897 ｜ P 736 -8,723 ｜ C 761 +8,333

📆 Forward Expiration Structure

11-04  C +29.3k / P +35.2k ｜ Activity HIGH ｜ 1D
11-05  C +17.6k / P +61.6k ｜ Activity HIGH ｜ 2D
11-06  C +27.6k / P +31.0k ｜ Activity MEDIUM △ ｜ 3D
11-09  C +7.0k / P +17.8k ｜ Activity HIGH ｜ 6D

📆 11-04 Forward Structure
存量OI: C 106.0k / P 266.3k，今日变化ΔOI: C +29.3k / P +35.2k，平值价格ATM: C $4.09 / P $4.69 ｜ ATM IV 24.7%，净 delta 敞口 -751k shares
Top ΔOI: P 756 +12,398 ｜ P 755 +5,401 ｜ P 767 -5,341
仓位参考: Max Pain 762 ｜ Call Wall 773（+2.6%，弱）（OI 6.9k） ｜ Put Wall 740（-1.8%，弱）（OI 58.6k）
量化解读： 存量 Put 重｜ATM IV 24.7%｜历史 Rank 93%（近端代理）｜IV/RV 2.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 750,590 股

📆 11-05 Forward Structure
存量OI: C 54.5k / P 91.0k，今日变化ΔOI: C +17.6k / P +61.6k，平值价格ATM: C $5.23 / P $5.68 ｜ ATM IV 22.9%，净 delta 敞口 43k shares
Top ΔOI: P 735 +12,076
仓位参考: Max Pain 755 ｜ Call Wall 765（+1.5%，弱）（OI 6.1k） ｜ Put Wall 735（-2.5%）（OI 15.2k）
量化解读： 存量 Put 重｜ATM IV 22.9%｜历史 Rank 93%（近端代理）｜IV/RV 2.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 43,331 股

11-06（MEDIUM △）Top ΔOI: 750P +4,617 ｜ 761P +4,230
11-06（MEDIUM △）仓位参考: Max Pain 762 ｜ Call Wall 770（+2.2%，弱）（OI 15.2k） ｜ Put Wall 750（-0.5%）（OI 43.2k）

📆 11-09 Forward Structure
存量OI: C 25.0k / P 46.9k，今日变化ΔOI: C +7.0k / P +17.8k，平值价格ATM: C $7.48 / P $7.34 ｜ ATM IV 18.5%，净 delta 敞口 -298k shares
Top ΔOI: P 745 +4,700 ｜ C 790 +4,032 ｜ P 755 +3,202
仓位参考: Max Pain 765 ｜ Call Wall 775（+2.8%，弱）（OI 3.8k） ｜ Put Wall 745（-1.2%）（OI 6.7k）
量化解读： 存量 Put 重｜ATM IV 18.5%｜历史 Rank 93%（近端代理）｜IV/RV 1.75×（近似）｜净 delta 敞口 负 298,389 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/SPY_morning.json