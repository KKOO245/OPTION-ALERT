# 期权晨报 2026-09-22（快照 10:20 ET）

📊 市场环境

SPY $773.39 ｜ QQQ $744.89
VIX 14.54 ↓2.2%（5D -15.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 36.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-23 780C ΔOI +13,010（距现价 +0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 773.50 → 今开 774.03（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 775.14 ｜ 低 773.55

Options: P/C成交量 0.82 | OI比 1.21 | ATM IV 12.6% | Skew 0.6pp | Term 0.94 | ExpMove ±0.5%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构正常（Term 0.94）｜保护溢价薄（Skew 0.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.82×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.21×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 75% ｜ P/C OI(近端) 7%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 75%）｜近端持仓极端 Call 重（P/C OI 分位 7%，历史极低区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-23（1D）±0.5% ｜ 09-24（2D）±0.7% ｜ 09-25（3D）±0.8% ｜ 09-28（6D）±0.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 948,538,982 | GEX Change vs 上次快照 11,393,832 | Flip: Primary Flip: 769.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 3026 / LOW 333 / INVALID 1829
结构观察区: Primary Flip 769.80（全链重定价，覆盖 98%）
Call Wall 785（弱结构｜现价低于该位 1.4%）
最近结构参考: Flip 770（现价高于该位 0.5%）
量化视角： 正 Gamma（9.49亿，历史分位偏正区，比 75% 的交易日更正）｜正 Gamma 增强（+1139万）｜现价位于 Flip 上方 0.53%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 770（MaxPain，仅结算参考）；上方 785（Call Wall，弱结构）。
• Gamma 区域：切换参考 770（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 785.0C — Vol 67,337 | 最新价 $3.47 | OI 1549→67155 (ΔOI +65606张) | ΔOI/Volume 97.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增65606张（+4235.4% vs前日OI），连续性待观察（方向未知）
09-30 617.0P — Vol 27,241 | 最新价 $0.03 | OI 347→27461 (ΔOI +27114张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27114张（+7813.8% vs前日OI），连续性待观察（方向未知）
09-30 638.0P — Vol 25,192 | 最新价 $0.04 | OI 132→25239 (ΔOI +25107张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增25107张（+19020.5% vs前日OI），连续性待观察（方向未知）
09-22 775.0C — Vol 107,367 | 最新价 $0.98 | OI 2195→27110 (ΔOI +24915张) | ΔOI/Volume 23.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24915张（+1135.1% vs前日OI），连续性待观察（方向未知）
10-16 736.0P — Vol 25,360 | 最新价 $1.87 | OI 26610→51523 (ΔOI +24913张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24913张（+93.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 167,655 张（Put 77,134 / Call 90,521），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $5M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 233.3k / P 283.1k，今日成交量: C 613.6k / P 504.8k，平值价格ATM: C $1.10 / P $1.00 ｜ ATM IV 12.6%，预期波动 ±0.3%，Max Pain 770
Top ΔOI: C 775 +24,915 ｜ P 770 +13,564 ｜ C 780 +12,658

📆 Forward Expiration Structure

09-23  C +67.7k / P +58.7k ｜ Activity HIGH ｜ 1D
09-24  C +19.1k / P +15.4k ｜ Activity HIGH ｜ 2D
09-25  C +21.6k / P +60.4k ｜ Activity HIGH ｜ 3D
09-28  C +14.1k / P +27.3k ｜ Activity HIGH ｜ 6D

📆 09-23 Forward Structure
存量OI: C 135.1k / P 124.0k，今日变化ΔOI: C +67.7k / P +58.7k，平值价格ATM: C $1.94 / P $1.77 ｜ ATM IV 10.2%，净 delta 敞口 -149k shares
Top ΔOI: C 780 +13,010 ｜ C 801 +10,694 ｜ P 770 +7,362
仓位参考: Max Pain 770 ｜ Call Wall 780（+0.8%）（OI 16.6k） ｜ Put Wall 770（-0.5%，弱）（OI 7.5k）
量化解读： 存量两侧均衡｜ATM IV 10.2%｜历史 Rank 48%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 148,679 股

📆 09-24 Forward Structure
存量OI: C 62.3k / P 66.7k，今日变化ΔOI: C +19.1k / P +15.4k，平值价格ATM: C $2.63 / P $2.40 ｜ ATM IV 10.3%，净 delta 敞口 122k shares
Top ΔOI: C 778 +2,416 ｜ C 790 +2,346 ｜ C 780 +1,722
仓位参考: Max Pain 764 ｜ Call Wall 771（-0.4%）（OI 5.4k） ｜ Put Wall 752（-2.8%，弱）（OI 3.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 10.3%｜历史 Rank 48%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 121,652 股

📆 09-25 Forward Structure
存量OI: C 284.9k / P 624.2k，今日变化ΔOI: C +21.6k / P +60.4k，平值价格ATM: C $3.28 / P $2.86 ｜ ATM IV 10.4%，净 delta 敞口 -633k shares
Top ΔOI: C 790 -7,980 ｜ P 770 +4,804
仓位参考: Max Pain 766 ｜ Call Wall 772（-0.2%，弱）（OI 30.3k）
量化解读： 存量 Put 重｜ATM IV 10.4%｜历史 Rank 48%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 632,639 股

📆 09-28 Forward Structure
存量OI: C 47.8k / P 68.5k，今日变化ΔOI: C +14.1k / P +27.3k，平值价格ATM: C $3.92 / P $3.39 ｜ ATM IV 9.0%，净 delta 敞口 10k shares
Top ΔOI: P 770 +3,391
仓位参考: Max Pain 770 ｜ Call Wall 780（+0.8%）（OI 10.8k） ｜ Put Wall 770（-0.5%，弱）（OI 3.5k）
量化解读： 存量 Put 重｜ATM IV 9.0%｜历史 Rank 48%（近端代理）｜IV/RV 0.88×（近似）｜净 delta 敞口 正 10,271 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/SPY_morning.json