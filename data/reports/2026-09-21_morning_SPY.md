# 期权晨报 2026-09-21（快照 10:20 ET）

📊 市场环境

SPY $767.46 ｜ QQQ $734.21
VIX 14.85 ↑0.3%（5D -13.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 32.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-22 745P ΔOI +10,973（距现价 -2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 761.69 → 今开 766.25（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 768.49 ｜ 低 766.03

Options: P/C成交量 0.78 | OI比 1.67 | ATM IV 10.3% | Skew 1.7pp | Term 1.18 | ExpMove ±0.5%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构正常偏陡（Term 1.18）｜保护溢价薄（Skew 1.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.67×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 66% ｜ P/C OI(近端) 36%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 66%）｜近端持仓结构中性（P/C OI 分位 36%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-22（1D）±0.5% ｜ 09-23（2D）±0.7% ｜ 09-24（3D）±0.8% ｜ 09-25（4D）±0.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 487,200,705 | GEX Change vs 上次快照 1,093,956,914 | Flip: Primary Flip: 765.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 2982 / LOW 448 / INVALID 1766
结构观察区: Primary Flip 765.31（全链重定价，覆盖 97%）
最近结构参考: Flip 765（现价高于该位 0.3%）
量化视角： 正 Gamma（4.87亿，历史分位 66%，中性区）｜由负转正（+10.94亿）｜现价位于 Flip 上方 0.28%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 761（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 765（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-22 722.0P — Vol 21,209 | 最新价 $0.06 | OI 309→21264 (ΔOI +20955张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20955张（+6781.6% vs前日OI），连续性待观察（方向未知）
09-21 723.0P — Vol 17,596 | 最新价 $0.03 | OI 1343→17915 (ΔOI +16572张) | ΔOI/Volume 94.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16572张（+1234.0% vs前日OI），连续性待观察（方向未知）
09-22 725.0P — Vol 16,103 | 最新价 $0.07 | OI 1695→17120 (ΔOI +15425张) | ΔOI/Volume 95.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15425张（+910.0% vs前日OI），连续性待观察（方向未知）
09-25 755.0P — Vol 18,291 | 最新价 $1.78 | OI 5941→19104 (ΔOI +13163张) | ΔOI/Volume 72.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13163张（+221.6% vs前日OI），连续性待观察（方向未知）
10-16 740.0P — Vol 17,167 | 最新价 $3.67 | OI 31086→43805 (ΔOI +12719张) | ΔOI/Volume 74.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12719张（+40.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 78,834 张（Put 78,834 / Call 0），跨 4 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $7M，买/卖方向不可观测）｜彩票/名义 1 档（价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 169.4k / P 283.7k，今日成交量: C 571.8k / P 443.0k，平值价格ATM: C $1.10 / P $0.64 ｜ ATM IV 10.3%，预期波动 ±0.2%，Max Pain 761
Top ΔOI: P 723 +16,572 ｜ P 720 +11,774 ｜ P 745 +11,320

📆 Forward Expiration Structure

09-22  C +24.6k / P +73.3k ｜ Activity HIGH ｜ 1D
09-23  C +22.8k / P +26.3k ｜ Activity HIGH ｜ 2D
09-24  C +9.7k / P +6.3k ｜ Activity HIGH ｜ 3D
09-25  C +37.6k / P +54.0k ｜ Activity HIGH ｜ 4D

📆 09-22 Forward Structure
存量OI: C 99.7k / P 121.7k，今日变化ΔOI: C +24.6k / P +73.3k，平值价格ATM: C $2.12 / P $1.56 ｜ ATM IV 10.2%，净 delta 敞口 1.2M shares
Top ΔOI: P 722 +20,955 ｜ P 725 +15,425 ｜ P 745 +10,973
仓位参考: Max Pain 760 ｜ Call Wall 789（+2.8%，弱）（OI 12.7k） ｜ Put Wall 745（-2.9%，弱）（OI 11.7k）
量化解读： 存量 Put 重｜ATM IV 10.2%｜历史 Rank 26%（近端代理）｜IV/RV 1.14×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,150,212 股

📆 09-23 Forward Structure
存量OI: C 67.4k / P 65.3k，今日变化ΔOI: C +22.8k / P +26.3k，平值价格ATM: C $2.83 / P $2.23 ｜ ATM IV 10.4%，净 delta 敞口 653k shares
Top ΔOI: P 755 +4,834 ｜ P 745 +4,673 ｜ C 765 +2,601
仓位参考: Max Pain 760 ｜ Call Wall 760（-1.0%，弱）（OI 4.4k） ｜ Put Wall 755（-1.6%，弱）（OI 6.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 10.4%｜历史 Rank 26%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 正 653,402 股

📆 09-24 Forward Structure
存量OI: C 43.1k / P 51.3k，今日变化ΔOI: C +9.7k / P +6.3k，平值价格ATM: C $3.47 / P $2.79 ｜ ATM IV 10.7%，净 delta 敞口 279k shares
Top ΔOI: C 771 +4,835 ｜ P 727 +2,514 ｜ C 770 +641
仓位参考: Max Pain 760 ｜ Call Wall 771（+0.5%）（OI 5.3k） ｜ Put Wall 752（-2.0%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 10.7%｜历史 Rank 26%（近端代理）｜IV/RV 1.20×（近似）｜净 delta 敞口 正 279,404 股

📆 09-25 Forward Structure
存量OI: C 263.3k / P 563.8k，今日变化ΔOI: C +37.6k / P +54.0k，平值价格ATM: C $4.11 / P $3.20 ｜ ATM IV 10.9%，净 delta 敞口 942k shares
Top ΔOI: P 755 +13,163
仓位参考: Max Pain 762 ｜ Call Wall 790（+2.9%，弱）（OI 29.7k） ｜ Put Wall 745（-2.9%，弱）（OI 152.0k）
量化解读： 存量 Put 重｜ATM IV 10.9%｜历史 Rank 26%（近端代理）｜IV/RV 1.22×（近似）｜净 delta 敞口 正 941,776 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/SPY_morning.json