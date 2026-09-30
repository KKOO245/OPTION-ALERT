# 期权晨报 2026-09-29（快照 10:20 ET）

📊 市场环境

SPY $764.20 ｜ QQQ $nan
VIX 15.96 ↓0.7%（5D +12.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-01 782C ΔOI +12,642（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-05 670P ΔOI +9,636 占该期限总 OI 11.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 765.61 → 今开 766.83（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 766.95 ｜ 低 764.60

Options: P/C成交量 1.13 | OI比 1.20 | ATM IV 17.5% | Skew 1.0pp | Term 0.76 | ExpMove ±0.7%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价薄（Skew 1.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.13×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.20×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 38% ｜ P/C OI(近端) 7%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 38%）｜近端持仓极端 Call 重（P/C OI 分位 7%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-30（1D）±0.7% ｜ 10-01（2D）±0.9% ｜ 10-02（3D）±1.1% ｜ 10-05（6D）±1.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -810,584,327 | GEX Change vs 上次快照 66,932,811 | Flip: Primary Flip: 768.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2987 / LOW 479 / INVALID 1678
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 768.88（全链重定价，覆盖 94%）
Call Wall 785（现价低于该位 2.5%）
最近结构参考: Flip 769（现价低于该位 0.5%）
量化视角： 负 Gamma（8.11亿，历史分位 38%，中性区）｜负 Gamma 缓解（+6693万）｜现价位于 Flip 下方 0.47%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 766（MaxPain，仅结算参考） / 785（Call Wall）。
• Gamma 区域：切换参考 769（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 745.0P — Vol 64,866 | 最新价 $0.42 | OI 7078→67934 (ΔOI +60856张) | ΔOI/Volume 93.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增60856张（+859.8% vs前日OI），连续性待观察（方向未知）
10-02 730.0P — Vol 61,462 | 最新价 $0.13 | OI 7691→67749 (ΔOI +60058张) | ΔOI/Volume 97.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增60058张（+780.9% vs前日OI），连续性待观察（方向未知）
10-09 745.0P — Vol 46,939 | 最新价 $1.56 | OI 1942→47990 (ΔOI +46048张) | ΔOI/Volume 98.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增46048张（+2371.2% vs前日OI），连续性待观察（方向未知）
10-09 725.0P — Vol 45,347 | 最新价 $0.48 | OI 1481→46452 (ΔOI +44971张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增44971张（+3036.5% vs前日OI），连续性待观察（方向未知）
10-16 732.0P — Vol 31,034 | 最新价 $1.66 | OI 52776→72155 (ΔOI +19379张) | ΔOI/Volume 62.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19379张（+36.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 231,312 张（Put 231,312 / Call 0），跨 3 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $10M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 172.2k / P 206.9k，今日成交量: C 472.8k / P 532.2k，平值价格ATM: C $1.40 / P $1.50 ｜ ATM IV 17.5%，预期波动 ±0.4%，Max Pain 766
Top ΔOI: C 768 +13,680 ｜ C 770 +11,556 ｜ C 767 +10,714

📆 Forward Expiration Structure

09-30  C +21.6k / P +13.7k ｜ Activity HIGH ｜ 1D
10-01  C +25.3k / P +21.1k ｜ Activity HIGH ｜ 2D
10-02  C +32.3k / P +135.7k ｜ Activity HIGH ｜ 3D
10-05  C +9.4k / P +26.3k ｜ Activity HIGH ｜ 6D

📆 09-30 Forward Structure
存量OI: C 647.1k / P 1857.7k，今日变化ΔOI: C +21.6k / P +13.7k，平值价格ATM: C $2.68 / P $2.66 ｜ ATM IV 14.8%，净 delta 敞口 1.1M shares
Top ΔOI: P 761 -5,775
仓位参考: Max Pain 761 ｜ Call Wall 786（+2.7%，弱）（OI 23.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 14.8%｜历史 Rank 76%（近端代理）｜IV/RV 1.50×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,062,342 股

📆 10-01 Forward Structure
存量OI: C 73.3k / P 80.7k，今日变化ΔOI: C +25.3k / P +21.1k，平值价格ATM: C $3.48 / P $3.36 ｜ ATM IV 14.2%，净 delta 敞口 -133k shares
Top ΔOI: C 782 +12,642 ｜ P 764 +4,085 ｜ P 752 +2,743
仓位参考: Max Pain 765 ｜ Call Wall 782（+2.2%）（OI 13.6k） ｜ Put Wall 764（-0.2%，弱）（OI 4.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 14.2%｜历史 Rank 76%（近端代理）｜IV/RV 1.44×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 132,641 股

📆 10-02 Forward Structure
存量OI: C 270.4k / P 461.9k，今日变化ΔOI: C +32.3k / P +135.7k，平值价格ATM: C $4.43 / P $4.06 ｜ ATM IV 14.5%，净 delta 敞口 70k shares
Top ΔOI: P 745 +60,856 ｜ P 730 +60,058 ｜ P 744 -10,880
仓位参考: Max Pain 765 ｜ Call Wall 785（+2.6%）（OI 61.9k） ｜ Put Wall 745（-2.6%，弱）（OI 67.9k）
量化解读： 存量 Put 重｜ATM IV 14.5%｜历史 Rank 76%（近端代理）｜IV/RV 1.47×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 69,985 股

📆 10-05 Forward Structure
存量OI: C 31.7k / P 53.6k，今日变化ΔOI: C +9.4k / P +26.3k，平值价格ATM: C $5.06 / P $4.60 ｜ ATM IV 12.0%，净 delta 敞口 171k shares
仓位参考: Max Pain 767 ｜ Call Wall 775（+1.3%，弱）（OI 1.7k）
量化解读： 存量 Put 重｜ATM IV 12.0%｜历史 Rank 76%（近端代理）｜IV/RV 1.22×（近似）｜净 delta 敞口 正 170,919 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/SPY_morning.json