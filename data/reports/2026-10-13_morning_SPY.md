# 期权晨报 2026-10-13（快照 10:20 ET）

📊 市场环境

SPY $777.81 ｜ QQQ $743.57
VIX 15.31 ↑0.7%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.95 ｜ 实际 3.99 ｜ 前值 3.93　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-14 795C ΔOI +11,350（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-15 737P ΔOI +41,243 占该期限总 OI 20.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 778.10 → 今开 777.34（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 778.75 ｜ 低 777.17

Options: P/C成交量 0.88 | OI比 1.35 | ATM IV 10.5% | Skew 1.3pp | Term 1.18 | ExpMove ±0.6%（近端） | Rank 29%
量化视角： IV 中性（Rank 29%）｜期限结构正常偏陡（Term 1.18）｜保护溢价薄（Skew 1.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.88×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.35×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 60% ｜ P/C OI(近端) 14%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 60%）｜近端持仓结构中性（P/C OI 分位 14%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-14（1D）±0.6% ｜ 10-15（2D）±0.7% ｜ 10-16（3D）±0.9% ｜ 10-19（6D）±1.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 190,163,739 | GEX Change vs 上次快照 -52,233,942 | Flip: Primary Flip: 776.95（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 2885 / LOW 391 / INVALID 1600
结构观察区: Primary Flip 776.95（全链重定价，覆盖 97%）
Call Wall 800（弱结构｜现价低于该位 2.8%）
最近结构参考: Flip 777（现价高于该位 0.1%）
量化视角： 正 Gamma（1.90亿，历史分位 60%，中性区）｜正 Gamma 减弱（5223万）｜现价位于 Flip 上方 0.09%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 777（MaxPain，仅结算参考）；上方 800（Call Wall，弱结构）。
• Gamma 区域：切换参考 777（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-15 737.0P — Vol 54,219 | 最新价 $0.06 | OI 96→41339 (ΔOI +41243张) | ΔOI/Volume 76.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增41243张（+42961.5% vs前日OI），连续性待观察（方向未知）
10-15 738.0P — Vol 42,676 | 最新价 $0.06 | OI 152→37900 (ΔOI +37748张) | ΔOI/Volume 88.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增37748张（+24834.2% vs前日OI），连续性待观察（方向未知）
10-13 747.0P — Vol 58,894 | 最新价 $0.02 | OI 70→20892 (ΔOI +20822张) | ΔOI/Volume 35.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20822张（+29745.7% vs前日OI），连续性待观察（方向未知）
10-21 620.0P — Vol 20,642 | 最新价 $0.03 | OI 5→20647 (ΔOI +20642张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20642张（+412840.0% vs前日OI），连续性待观察（方向未知）
10-21 625.0P — Vol 17,781 | 最新价 $0.03 | OI 0→17781 (ΔOI +17781张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17781张（前日OI缺失），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 138,236 张（Put 138,236 / Call 0），跨 3 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 173.1k / P 232.9k，今日成交量: C 503.5k / P 440.5k，平值价格ATM: C $0.69 / P $1.12 ｜ ATM IV 10.5%，预期波动 ±0.2%，Max Pain 777
Top ΔOI: P 747 +20,822 ｜ C 780 +11,766 ｜ C 779 +10,528

📆 Forward Expiration Structure

10-14  C +46.2k / P +75.0k ｜ Activity HIGH ｜ 1D
10-15  C +7.3k / P +92.8k ｜ Activity HIGH ｜ 2D
10-16  C +24.7k / P +37.0k ｜ Activity HIGH ｜ 3D
10-19  C +9.4k / P +12.6k ｜ Activity HIGH ｜ 6D

📆 10-14 Forward Structure
存量OI: C 136.8k / P 178.5k，今日变化ΔOI: C +46.2k / P +75.0k，平值价格ATM: C $2.00 / P $2.35 ｜ ATM IV 11.9%，净 delta 敞口 64k shares
Top ΔOI: P 733 +12,848 ｜ P 735 +12,799 ｜ C 795 +11,350
仓位参考: Max Pain 777 ｜ Call Wall 790（+1.6%）（OI 19.3k） ｜ Put Wall 770（-1.0%，弱）（OI 6.1k）
量化解读： 存量 Put 重｜ATM IV 11.9%｜历史 Rank 29%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 64,232 股

📆 10-15 Forward Structure
存量OI: C 37.9k / P 162.3k，今日变化ΔOI: C +7.3k / P +92.8k，平值价格ATM: C $2.63 / P $2.91 ｜ ATM IV 11.3%，净 delta 敞口 -117k shares
Top ΔOI: P 737 +41,243 ｜ P 738 +37,748 ｜ P 729 +4,312
仓位参考: Max Pain 777 ｜ Call Wall 781（+0.4%，弱）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 11.3%｜历史 Rank 29%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 116,525 股

📆 10-16 Forward Structure
存量OI: C 706.9k / P 2395.8k，今日变化ΔOI: C +24.7k / P +37.0k，平值价格ATM: C $3.32 / P $3.33 ｜ ATM IV 11.2%，净 delta 敞口 -916k shares
Top ΔOI: C 785 -10,411 ｜ C 812 +9,980 ｜ P 772 +9,967
仓位参考: Max Pain 770 ｜ Call Wall 785（+0.9%）（OI 63.5k）
量化解读： 存量 Put 重｜ATM IV 11.2%｜历史 Rank 29%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 916,240 股

📆 10-19 Forward Structure
存量OI: C 35.2k / P 67.2k，今日变化ΔOI: C +9.4k / P +12.6k，平值价格ATM: C $3.81 / P $3.77 ｜ ATM IV 9.2%，净 delta 敞口 -39k shares
Top ΔOI: P 747 +2,301 ｜ C 789 +2,083 ｜ P 762 +1,792
仓位参考: Max Pain 778 ｜ Call Wall 790（+1.6%，弱）（OI 4.3k） ｜ Put Wall 770（-1.0%，弱）（OI 3.4k）
量化解读： 存量 Put 重｜ATM IV 9.2%｜历史 Rank 29%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 负 38,689 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/SPY_morning.json