# 期权晨报 2026-10-27（快照 10:20 ET）

📊 市场环境

SPY $766.09 ｜ QQQ $715.34
VIX 18.02 ↓2.0%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 1.8 ｜ 前值 0.1　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🟡 **近现价集中开仓**: 10-28 793C ΔOI +7,272（距现价 +3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 765.37 → 今开 767.34（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 768.35 ｜ 低 765.34

Options: P/C成交量 0.98 | OI比 1.48 | ATM IV 16.1% | Skew 1.3pp | Term 0.88 | ExpMove ±0.8%（近端） | Rank 71%
量化视角： IV 中性（Rank 71%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价薄（Skew 1.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.98×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.48×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 32% ｜ P/C OI(近端) 22%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 32%）｜近端持仓结构中性（P/C OI 分位 22%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-28（1D）±0.8% ｜ 10-29（2D）±1.1% ｜ 10-30（3D）±1.3% ｜ 11-02（6D）±1.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,085,228,890 | GEX Change vs 上次快照 136,098,578 | Flip: Primary Flip: 772.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 3121 / LOW 299 / INVALID 1376
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 772.45（全链重定价，覆盖 98%）
最近结构参考: Flip 772（现价低于该位 0.8%）
量化视角： 负 Gamma（10.85亿，历史分位 32%，中性区）｜负 Gamma 缓解（+1.36亿）｜现价位于 Flip 下方 0.84%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 767（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 772（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 750.0P — Vol 63,287 | 最新价 $6.52 | OI 87211→147734 (ΔOI +60523张) | ΔOI/Volume 95.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增60523张（+69.4% vs前日OI），连续性待观察（方向未知）
11-20 725.0P — Vol 56,278 | 最新价 $3.10 | OI 34795→77732 (ΔOI +42937张) | ΔOI/Volume 76.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增42937张（+123.4% vs前日OI），连续性待观察（方向未知）
10-30 750.0P — Vol 9,877 | 最新价 $1.32 | OI 48659→69005 (ΔOI +20346张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20346张（+41.8% vs前日OI），连续性待观察（方向未知）
11-20 728.0P — Vol 24,224 | 最新价 $3.36 | OI 15102→35364 (ΔOI +20262张) | ΔOI/Volume 83.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20262张（+134.2% vs前日OI），连续性待观察（方向未知）
10-29 758.0P — Vol 16,361 | 最新价 $2.14 | OI 279→15817 (ΔOI +15538张) | ΔOI/Volume 95.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15538张（+5569.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 159,606 张（Put 159,606 / Call 0），跨 3 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $66M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 148.0k / P 219.5k，今日成交量: C 555.3k / P 546.9k，平值价格ATM: C $1.33 / P $1.35 ｜ ATM IV 16.1%，预期波动 ±0.3%，Max Pain 767
Top ΔOI: P 762 +11,741 ｜ P 765 +11,413 ｜ C 775 +6,306

📆 Forward Expiration Structure

10-28  C +38.2k / P +35.4k ｜ Activity HIGH ｜ 1D
10-29  C +5.6k / P +40.8k ｜ Activity HIGH ｜ 2D
10-30  C +28.7k / P -44.4k ｜ Activity HIGH ｜ 3D
11-02  C +8.1k / P +12.2k ｜ Activity HIGH ｜ 6D

📆 10-28 Forward Structure
存量OI: C 100.0k / P 135.7k，今日变化ΔOI: C +38.2k / P +35.4k，平值价格ATM: C $3.18 / P $3.07 ｜ ATM IV 17.4%，净 delta 敞口 -45k shares
Top ΔOI: C 793 +7,272 ｜ C 792 +6,725 ｜ P 760 +3,991
仓位参考: Max Pain 767 ｜ Call Wall 780（+1.8%，弱）（OI 6.1k） ｜ Put Wall 760（-0.8%，弱）（OI 7.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 17.4%｜历史 Rank 71%（近端代理）｜IV/RV 1.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 45,244 股

📆 10-29 Forward Structure
存量OI: C 43.6k / P 120.8k，今日变化ΔOI: C +5.6k / P +40.8k，平值价格ATM: C $4.24 / P $4.03 ｜ ATM IV 17.1%，净 delta 敞口 -452k shares
Top ΔOI: P 758 +15,538 ｜ P 748 +14,873 ｜ P 715 +1,645
仓位参考: Max Pain 766 ｜ Call Wall 786（+2.6%，弱）（OI 2.8k） ｜ Put Wall 748（-2.3%，弱）（OI 17.8k）
量化解读： 存量 Put 重｜ATM IV 17.1%｜历史 Rank 71%（近端代理）｜IV/RV 1.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 451,941 股

📆 10-30 Forward Structure
存量OI: C 641.3k / P 1603.9k，今日变化ΔOI: C +28.7k / P -44.4k，平值价格ATM: C $5.09 / P $4.60 ｜ ATM IV 16.8%，净 delta 敞口 2.1M shares
Top ΔOI: P 755 -55,030 ｜ P 745 -50,387 ｜ P 750 +20,346
仓位参考: Max Pain 765 ｜ Call Wall 780（+1.8%，弱）（OI 27.1k） ｜ Put Wall 745（-2.7%，弱）（OI 107.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 16.8%｜历史 Rank 71%（近端代理）｜IV/RV 1.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,086,448 股

📆 11-02 Forward Structure
存量OI: C 27.6k / P 41.0k，今日变化ΔOI: C +8.1k / P +12.2k，平值价格ATM: C $5.81 / P $5.23 ｜ ATM IV 13.7%，净 delta 敞口 -37k shares
Top ΔOI: P 759 +2,159 ｜ P 765 +1,624 ｜ C 806 +1,488
仓位参考: Max Pain 765 ｜ Call Wall 767（+0.1%，弱）（OI 1.3k） ｜ Put Wall 750（-2.1%，弱）（OI 4.8k）
量化解读： 存量 Put 重｜ATM IV 13.7%｜历史 Rank 71%（近端代理）｜IV/RV 1.50×（近似）｜净 delta 敞口 负 37,232 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/SPY_morning.json