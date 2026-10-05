# 期权晚报 2026-10-05（快照 16:51 ET）

📊 市场环境

SPY $774.83 ｜ QQQ $756.20
VIX 15.52 ↑1.4%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 43.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 10-05 10:00　【高】ISM 非制造业 PMI　预测 55 ｜ 实际 54.9 ｜ 前值 55.4　✅ 今日已公布
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 167C ΔOI +17,104（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 164.68 → 收盘 164.43（-0.2%） ｜ 今日高 166.20 ｜ 低 160.12 ｜ 昨收 160.01 → 收盘 164.43（+2.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.47 | OI比 0.75 | ATM IV 66.6% | Skew -7.6pp | Term 0.96 | ExpMove ±5.6%（近端） | Rank 22%
量化视角： IV 历史低位（Rank 22%，期权偏便宜）｜期限结构正常（Term 0.96）｜Put 保护异常便宜（Skew -7.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（4D）±5.6% ｜ 10-16（11D）±8.6% ｜ 10-23（18D）±11.1% ｜ 10-30（25D）±13.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 75,143,202 | GEX Change vs 上次快照 3,955,727 | Flip: Primary Flip: 146.49（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 661 / LOW 86 / INVALID 185
结构观察区: Primary Flip 146.49（全链重定价，覆盖 100%）
最近结构参考: Flip 146（现价高于该位 12.2%）
量化视角： 正 Gamma（7514万，无历史分位）｜正 Gamma 增强（+396万）｜现价位于 Flip 上方 12.25%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 152（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 146（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 95.0P — Vol 224 | 最新价 $0.01 | OI 4442→36356 (ΔOI +31914张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31914张（+718.5% vs前日OI），连续性待观察（方向未知）
10-09 175.0C — Vol 6,905 | 最新价 $1.52 | OI 1960→19361 (ΔOI +17401张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17401张（+887.8% vs前日OI），连续性待观察（方向未知）
10-09 167.5C — Vol 6,130 | 最新价 $3.30 | OI 975→18079 (ΔOI +17104张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17104张（+1754.3% vs前日OI），连续性待观察（方向未知）
10-09 172.5C — Vol 4,188 | 最新价 $2.00 | OI 4518→21591 (ΔOI +17073张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17073张（+377.9% vs前日OI），连续性待观察（方向未知）
10-09 165.0C — Vol 16,471 | 最新价 $4.29 | OI 8085→24569 (ΔOI +16484张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16484张（+203.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 99,976 张（Put 31,914 / Call 68,062），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +136.9k / P +76.8k ｜ Activity HIGH ｜ 4D
10-16  C -2.5k / P +8.3k ｜ Activity HIGH ｜ 11D
10-23  C -2.0k / P +2.6k ｜ Activity HIGH ｜ 18D
10-30  C +4.1k / P +2.7k ｜ Activity HIGH ｜ 25D

📆 10-09 Forward Structure
存量OI: C 202.0k / P 150.6k，今日变化ΔOI: C +136.9k / P +76.8k，平值价格ATM: C $4.29 / P $4.90 ｜ ATM IV 66.6%，净 delta 敞口 4.9M shares
Top ΔOI: C 175 +17,401 ｜ C 167 +17,104
仓位参考: Max Pain 152 ｜ Call Wall 165（+0.3%，弱）（OI 24.6k）
量化解读： 存量 Call 重｜ATM IV 66.6%｜历史 Rank 22%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,888,762 股

📆 10-16 Forward Structure
存量OI: C 176.8k / P 162.1k，今日变化ΔOI: C -2.5k / P +8.3k，平值价格ATM: C $6.90 / P $7.28 ｜ ATM IV 61.8%，净 delta 敞口 -336k shares
Top ΔOI: C 95 -3,146
仓位参考: Max Pain 130 ｜ Call Wall 155（-5.7%，弱）（OI 10.4k） ｜ Put Wall 150（-8.8%，弱）（OI 5.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 61.8%｜历史 Rank 22%（近端代理）｜IV/RV 0.84×（近似）｜净 delta 敞口 负 336,388 股

📆 10-23 Forward Structure
存量OI: C 24.6k / P 34.9k，今日变化ΔOI: C -2.0k / P +2.6k，平值价格ATM: C $9.20 / P $9.00 ｜ ATM IV 61.3%，净 delta 敞口 -126k shares
Top ΔOI: C 172 -3,218
仓位参考: Max Pain 160 ｜ Call Wall 172.5（+4.9%，弱）（OI 2.5k） ｜ Put Wall 155（-5.7%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 61.3%｜历史 Rank 22%（近端代理）｜IV/RV 0.83×（近似）｜净 delta 敞口 负 125,504 股

📆 10-30 Forward Structure
存量OI: C 19.7k / P 25.4k，今日变化ΔOI: C +4.1k / P +2.7k，平值价格ATM: C $10.70 / P $10.93 ｜ ATM IV 63.0%，净 delta 敞口 148k shares
Top ΔOI: C 162 +2,367 ｜ C 175 +368
仓位参考: Max Pain 160 ｜ Call Wall 162.5（-1.2%，弱）（OI 2.5k） ｜ Put Wall 160（-2.7%，弱）（OI 2.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 63.0%｜历史 Rank 22%（近端代理）｜IV/RV 0.85×（近似）｜净 delta 敞口 正 147,843 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/MSTR_evening.json