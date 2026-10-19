# 期权晚报 2026-10-19（快照 16:40 ET）

📊 市场环境

SPY $766.48 ｜ QQQ $718.36
VIX 18.44 ↓7.8%（5D +21.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 23.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 195C ΔOI +12,191（距现价 +0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 187.00 → 收盘 194.15（+3.8%） ｜ 今日高 196.99 ｜ 低 186.15 ｜ 昨收 186.03 → 收盘 194.15（+4.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.48 | OI比 0.94 | ATM IV 52.3% | Skew 5.2pp | Term 1.19 | ExpMove ±4.4%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构正常偏陡（Term 1.19）｜保护溢价中性（Skew 5.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.94×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（4D）±4.4% ｜ 10-30（11D）±6.8% ｜ 11-06（18D）±12.8% ｜ 11-13（25D）±13.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 36,683,244 | GEX Change vs 上次快照 6,277,753 | Flip: Primary Flip: 180.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 638 / LOW 53 / INVALID 221
结构观察区: Primary Flip 180.89（全链重定价，覆盖 100%）
Call Wall 200（弱结构｜现价低于该位 2.9%）
最近结构参考: Call Wall 200（现价低于该位 2.9%）
量化视角： 正 Gamma（3668万，无历史分位）｜正 Gamma 增强（+628万）｜现价位于 Flip 上方 7.33%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 181（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 195.0C — Vol 17,578 | 最新价 $3.93 | OI 1432→13623 (ΔOI +12191张) | ΔOI/Volume 69.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12191张（+851.3% vs前日OI），连续性待观察（方向未知）
10-23 190.0C — Vol 5,222 | 最新价 $6.85 | OI 1106→11370 (ΔOI +10264张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10264张（+928.0% vs前日OI），连续性待观察（方向未知）
10-23 120.0P — Vol 436 | 最新价 $0.01 | OI 497→7913 (ΔOI +7416张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7416张（+1492.2% vs前日OI），连续性待观察（方向未知）
10-23 200.0C — Vol 20,566 | 最新价 $1.97 | OI 4063→10685 (ΔOI +6622张) | ΔOI/Volume 32.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6622张（+163.0% vs前日OI），连续性待观察（方向未知）
10-23 197.5C — Vol 9,827 | 最新价 $2.84 | OI 549→6846 (ΔOI +6297张) | ΔOI/Volume 64.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6297张（+1147.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 42,790 张（Put 7,416 / Call 35,374），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +56.9k / P +30.3k ｜ Activity HIGH ｜ 4D
10-30  C +2.9k / P +7.7k ｜ Activity HIGH ｜ 11D
11-06  C +3.4k / P +2.7k ｜ Activity HIGH ｜ 18D
11-13  C +0.9k / P +0.5k ｜ Activity HIGH ｜ 25D

📆 10-23 Forward Structure
存量OI: C 107.3k / P 101.0k，今日变化ΔOI: C +56.9k / P +30.3k，平值价格ATM: C $3.93 / P $4.68 ｜ ATM IV 52.3%，净 delta 敞口 2.2M shares
Top ΔOI: C 195 +12,191 ｜ C 190 +10,264
仓位参考: Max Pain 190 ｜ Call Wall 195（+0.4%，弱）（OI 13.6k） ｜ Put Wall 185（-4.7%，弱）（OI 4.1k）
量化解读： 存量两侧均衡｜ATM IV 52.3%｜历史 Rank 69%（近端代理）｜IV/RV 1.36×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 2,187,512 股

📆 10-30 Forward Structure
存量OI: C 45.3k / P 48.6k，今日变化ΔOI: C +2.9k / P +7.7k，平值价格ATM: C $6.31 / P $6.90 ｜ ATM IV 49.1%，净 delta 敞口 61k shares
Top ΔOI: P 190 +1,897 ｜ P 165 +1,028
仓位参考: Max Pain 190 ｜ Call Wall 205（+5.6%，弱）（OI 3.6k） ｜ Put Wall 190（-2.1%）（OI 6.1k）
量化解读： 存量两侧均衡｜ATM IV 49.1%｜历史 Rank 69%（近端代理）｜IV/RV 1.28×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 61,107 股

📆 11-06 Forward Structure
存量OI: C 22.5k / P 21.5k，今日变化ΔOI: C +3.4k / P +2.7k，平值价格ATM: C $12.15 / P $12.70 ｜ ATM IV 71.8%，净 delta 敞口 8k shares
Top ΔOI: C 265 +1,846 ｜ P 165 +934
仓位参考: Max Pain 190 ｜ Call Wall 205（+5.6%，弱）（OI 1.6k） ｜ Put Wall 190（-2.1%）（OI 3.1k）
量化解读： 存量两侧均衡｜ATM IV 71.8%｜历史 Rank 69%（近端代理）｜IV/RV 1.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 8,036 股

📆 11-13 Forward Structure
存量OI: C 9.3k / P 10.6k，今日变化ΔOI: C +0.9k / P +0.5k，平值价格ATM: C $13.47 / P $13.45 ｜ ATM IV 65.8%，净 delta 敞口 39k shares
Top ΔOI: P 155 -396 ｜ P 180 -359 ｜ P 165 +263
仓位参考: Max Pain 192 ｜ Call Wall 210（+8.2%，弱）（OI 1.0k） ｜ Put Wall 180（-7.3%，弱）（OI 1.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 65.8%｜历史 Rank 69%（近端代理）｜IV/RV 1.72×（近似）｜净 delta 敞口 正 38,848 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/PLTR_evening.json