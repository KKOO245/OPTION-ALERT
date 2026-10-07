# 期权晨报 2026-10-06（快照 10:20 ET）

📊 市场环境

SPY $779.09 ｜ QQQ $759.66
VIX 15.48 ↓0.3%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.4（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-07 742P ΔOI +8,072（距现价 -4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 787C ΔOI -200,738 占该期限总 OI 18.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 774.83 → 今开 778.15（+0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 780.67 ｜ 低 777.96

Options: P/C成交量 0.51 | OI比 0.92 | ATM IV 14.8% | Skew 0.9pp | Term 0.88 | ExpMove ±0.5%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价薄（Skew 0.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 84% ｜ P/C OI(近端) 1%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 84%）｜近端持仓极端 Call 重（P/C OI 分位 1%，历史极低区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-07（1D）±0.5% ｜ 10-08（2D）±0.7% ｜ 10-09（3D）±0.9% ｜ 10-12（6D）±1.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,479,564,014 | GEX Change vs 上次快照 682,828,829 | Flip: Primary Flip: 773.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 2537 / LOW 368 / INVALID 2063
结构观察区: Primary Flip 773.33（全链重定价，覆盖 96%）
Call Wall 785（现价低于该位 0.7%）
最近结构参考: Call Wall 785（现价低于该位 0.7%）
量化视角： 正 Gamma（14.80亿，历史分位偏正区，比 84% 的交易日更正）｜正 Gamma 增强（+6.83亿）｜现价位于 Flip 上方 0.82%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 772（MaxPain，仅结算参考）；上方 785（Call Wall）。
• Gamma 区域：切换参考 773（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 767.0P — Vol 24,943 | 最新价 $1.14 | OI 46642→64556 (ΔOI +17914张) | ΔOI/Volume 71.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17914张（+38.4% vs前日OI），连续性待观察（方向未知）
10-09 785.0C — Vol 242,768 | 最新价 $0.48 | OI 109589→125938 (ΔOI +16349张) | ΔOI/Volume 6.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16349张（+14.9% vs前日OI），连续性待观察（方向未知）
10-06 777.0C — Vol 67,419 | 最新价 $0.71 | OI 2141→16737 (ΔOI +14596张) | ΔOI/Volume 21.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14596张（+681.7% vs前日OI），连续性待观察（方向未知）
10-06 735.0P — Vol 48,097 | 最新价 $0.01 | OI 698→15216 (ΔOI +14518张) | ΔOI/Volume 30.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14518张（+2079.9% vs前日OI），连续性待观察（方向未知）
10-06 774.0C — Vol 77,850 | 最新价 $2.10 | OI 933→12946 (ΔOI +12013张) | ΔOI/Volume 15.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12013张（+1287.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 75,390 张（Put 32,432 / Call 42,958），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜彩票/名义 1 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 278.6k / P 256.7k，今日成交量: C 927.6k / P 476.7k，平值价格ATM: C $1.19 / P $1.29 ｜ ATM IV 14.8%，预期波动 ±0.3%，Max Pain 772
Top ΔOI: C 777 +14,596 ｜ P 735 +14,518 ｜ C 774 +12,013

📆 Forward Expiration Structure

10-07  C +23.1k / P +57.8k ｜ Activity HIGH ｜ 1D
10-08  C +16.8k / P +23.1k ｜ Activity HIGH ｜ 2D
10-09  C -155.9k / P +70.2k ｜ Activity HIGH ｜ 3D
10-12  C +14.4k / P +40.5k ｜ Activity HIGH ｜ 6D

📆 10-07 Forward Structure
存量OI: C 146.6k / P 171.3k，今日变化ΔOI: C +23.1k / P +57.8k，平值价格ATM: C $2.07 / P $2.12 ｜ ATM IV 11.5%，净 delta 敞口 713k shares
Top ΔOI: P 742 +8,072 ｜ P 743 +7,350 ｜ C 782 +4,045
仓位参考: Max Pain 771 ｜ Call Wall 802（+2.9%，弱）（OI 16.9k） ｜ Put Wall 760（-2.5%，弱）（OI 6.9k）
量化解读： 存量两侧均衡｜ATM IV 11.5%｜历史 Rank 64%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 713,356 股

📆 10-08 Forward Structure
存量OI: C 63.6k / P 84.6k，今日变化ΔOI: C +16.8k / P +23.1k，平值价格ATM: C $2.80 / P $2.72 ｜ ATM IV 11.2%，净 delta 敞口 503k shares
Top ΔOI: P 756 +2,333 ｜ P 753 +2,209 ｜ C 781 +2,205
仓位参考: Max Pain 770 ｜ Call Wall 795（+2.0%，弱）（OI 6.5k）
量化解读： 存量 Put 重｜ATM IV 11.2%｜历史 Rank 64%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 502,897 股

📆 10-09 Forward Structure
存量OI: C 499.9k / P 564.5k，今日变化ΔOI: C -155.9k / P +70.2k，平值价格ATM: C $3.50 / P $3.18 ｜ ATM IV 11.3%，净 delta 敞口 -4.1M shares
Top ΔOI: C 787 -200,738 ｜ P 767 +17,914 ｜ C 785 +16,349
仓位参考: Max Pain 770 ｜ Call Wall 785（+0.7%）（OI 125.9k） ｜ Put Wall 767（-1.6%，弱）（OI 64.6k）
量化解读： 存量两侧均衡｜ATM IV 11.3%｜历史 Rank 64%（近端代理）｜IV/RV 1.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 4,144,186 股

📆 10-12 Forward Structure
存量OI: C 37.1k / P 72.3k，今日变化ΔOI: C +14.4k / P +40.5k，平值价格ATM: C $4.18 / P $3.69 ｜ ATM IV 9.6%，净 delta 敞口 279k shares
Top ΔOI: C 793 +2,053
仓位参考: Max Pain 770 ｜ Call Wall 785（+0.7%）（OI 3.1k） ｜ Put Wall 770（-1.2%，弱）（OI 2.3k）
量化解读： 存量 Put 重｜ATM IV 9.6%｜历史 Rank 64%（近端代理）｜IV/RV 1.02×（近似）｜净 delta 敞口 正 279,141 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/SPY_morning.json