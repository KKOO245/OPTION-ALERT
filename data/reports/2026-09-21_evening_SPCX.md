# 期权晚报 2026-09-21（快照 16:40 ET）

📊 市场环境

SPY $773.50 ｜ QQQ $741.47
VIX 14.87 ↑0.4%（5D -13.0%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 33.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 155C ΔOI +230（距现价 +2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 154.77 → 收盘 151.85（-1.9%） ｜ 今日高 158.13 ｜ 低 151.64 ｜ 昨收 152.71 → 收盘 151.85（-0.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.48 | OI比 1.10 | ATM IV 56.3% | Skew -1.7pp | Term 0.88 | ExpMove ±4.8%（近端） | Rank 33%
量化视角： IV 中性（Rank 33%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.7pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.10×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（4D）±4.8% ｜ 10-02（11D）±7.2% ｜ 10-09（18D）±8.9% ｜ 10-16（25D）±10.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,794,666 | GEX Change vs 上次快照 -27,981,338 | Flip: Primary Flip: 150.98（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 604 / LOW 98 / INVALID 288
结构观察区: Primary Flip 150.98（全链重定价，覆盖 100%）
Call Wall 160（弱结构｜现价低于该位 5.1%）
最近结构参考: Flip 151（现价高于该位 0.6%）
量化视角： 正 Gamma（679万，无历史分位）｜正 Gamma 减弱（2798万）｜现价位于 Flip 上方 0.58%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（MaxPain，仅结算参考）；上方 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 151（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 135.0P — Vol 1,700 | 最新价 $1.92 | OI 44263→64225 (ΔOI +19962张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19962张（+45.1% vs前日OI），连续性待观察（方向未知）
09-25 170.0C — Vol 25,544 | 最新价 $0.22 | OI 6699→22147 (ΔOI +15448张) | ΔOI/Volume 60.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15448张（+230.6% vs前日OI），连续性待观察（方向未知）
09-25 180.0C — Vol 2,925 | 最新价 $0.06 | OI 8211→22456 (ΔOI +14245张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14245张（+173.5% vs前日OI），连续性待观察（方向未知）
10-16 155.0P — Vol 1,061 | 最新价 $9.35 | OI 35469→49448 (ΔOI +13979张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13979张（+39.4% vs前日OI），连续性待观察（方向未知）
10-02 90.0P — Vol 144 | 最新价 $0.03 | OI 344→9574 (ΔOI +9230张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9230张（+2683.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 72,864 张（Put 43,171 / Call 29,693），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $17M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +56.8k / P +33.1k ｜ Activity HIGH ｜ 4D
10-02  C +13.1k / P +15.4k ｜ Activity HIGH ｜ 11D
10-09  C +1.0k / P +3.9k ｜ Activity HIGH ｜ 18D
10-16  C -12.6k / P +42.8k ｜ Activity HIGH ｜ 25D

📆 09-25 Forward Structure
存量OI: C 156.5k / P 171.8k，今日变化ΔOI: C +56.8k / P +33.1k，平值价格ATM: C $3.35 / P $3.90 ｜ ATM IV 56.3%，净 delta 敞口 200k shares
Top ΔOI: C 170 +15,448 ｜ C 180 +14,245 ｜ C 160 +4,754
仓位参考: Max Pain 150 ｜ Call Wall 160（+5.4%，弱）（OI 14.9k） ｜ Put Wall 140（-7.8%，弱）（OI 15.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 56.3%｜历史 Rank 33%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 200,392 股

📆 10-02 Forward Structure
存量OI: C 52.6k / P 64.9k，今日变化ΔOI: C +13.1k / P +15.4k，平值价格ATM: C $5.20 / P $5.65 ｜ ATM IV 51.9%，净 delta 敞口 99k shares
Top ΔOI: C 170 +2,077 ｜ C 180 +1,764
仓位参考: Max Pain 150 ｜ Call Wall 160（+5.4%，弱）（OI 5.3k） ｜ Put Wall 150（-1.2%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 51.9%｜历史 Rank 33%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 99,256 股

📆 10-09 Forward Structure
存量OI: C 20.6k / P 23.6k，今日变化ΔOI: C +1.0k / P +3.9k，平值价格ATM: C $6.60 / P $6.85 ｜ ATM IV 50.3%，净 delta 敞口 -17k shares
Top ΔOI: P 137 +264 ｜ C 155 +230
仓位参考: Max Pain 149 ｜ Call Wall 165（+8.7%，弱）（OI 1.9k） ｜ Put Wall 140（-7.8%，弱）（OI 1.1k）
量化解读： 存量两侧均衡｜ATM IV 50.3%｜历史 Rank 33%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 16,936 股

📆 10-16 Forward Structure
存量OI: C 295.7k / P 388.7k，今日变化ΔOI: C -12.6k / P +42.8k，平值价格ATM: C $7.80 / P $7.85 ｜ ATM IV 49.9%，净 delta 敞口 -1.3M shares
Top ΔOI: P 135 +19,962 ｜ C 200 -19,791 ｜ P 155 +13,979
仓位参考: Max Pain 150 ｜ Call Wall 160（+5.4%，弱）（OI 34.1k） ｜ Put Wall 155（+2.1%，弱）（OI 49.4k）
量化解读： 存量 Put 重｜ATM IV 49.9%｜历史 Rank 33%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 负 1,335,716 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/SPCX_evening.json