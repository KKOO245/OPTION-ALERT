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
🟡 **近现价集中开仓**: 10-09 88C ΔOI +15,691（距现价 +0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 88C ΔOI +15,691 占该期限总 OI 13.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 87.84 → 收盘 87.42（-0.5%） ｜ 今日高 88.18 ｜ 低 85.99 ｜ 昨收 87.78 → 收盘 87.42（-0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.38 | OI比 0.35 | ATM IV 41.2% | Skew -2.2pp | Term 0.94 | ExpMove ±3.7%（近端） | Rank 61%
量化视角： IV 中性（Rank 61%）｜期限结构正常（Term 0.94）｜Put 保护异常便宜（Skew -2.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.35）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.35×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（4D）±3.7% ｜ 10-16（11D）±5.6% ｜ 10-19（14D）±5.8% ｜ 10-23（18D）±7.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 28,487,283 | GEX Change vs 上次快照 8,411,785 | Flip: Primary Flip: 85.22（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 397 / LOW 105 / INVALID 398
结构观察区: Primary Flip 85.22（全链重定价，覆盖 96%）
Put Wall 85（弱结构｜现价高于该位 2.8%） | Call Wall 90（弱结构｜现价低于该位 2.9%）
最近结构参考: Flip 85（现价高于该位 2.6%）
量化视角： 正 Gamma（2849万，无历史分位）｜正 Gamma 增强（+841万）｜现价位于 Flip 上方 2.58%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 85（Put Wall，弱结构） / 87（MaxPain，仅结算参考）；上方 90（Call Wall，弱结构）。
• Gamma 区域：切换参考 85（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 88.0C — Vol 1,367 | 最新价 $1.28 | OI 615→16306 (ΔOI +15691张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15691张（+2551.4% vs前日OI），连续性待观察（方向未知）
10-09 90.5C — Vol 100 | 最新价 $0.57 | OI 53→15093 (ΔOI +15040张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15040张（+28377.4% vs前日OI），连续性待观察（方向未知）
10-09 89.5C — Vol 86 | 最新价 $0.86 | OI 207→10141 (ΔOI +9934张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9934张（+4799.0% vs前日OI），连续性待观察（方向未知）
10-09 92.0C — Vol 1,436 | 最新价 $0.30 | OI 654→10550 (ΔOI +9896张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9896张（+1513.2% vs前日OI），连续性待观察（方向未知）
10-09 90.0C — Vol 879 | 最新价 $0.56 | OI 3462→8898 (ΔOI +5436张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5436张（+157.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 55,997 张（Put 0 / Call 55,997），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +73.2k / P +2.0k ｜ Activity HIGH ｜ 4D
10-16  C +4.3k / P +3.6k ｜ Activity HIGH ｜ 11D
10-19  C N/A / P N/A ｜ Activity LOW ｜ 14D（新上架）
10-23  C +0.4k / P +81 ｜ Activity HIGH ｜ 18D

📆 10-09 Forward Structure
存量OI: C 88.8k / P 30.7k，今日变化ΔOI: C +73.2k / P +2.0k，平值价格ATM: C $2.04 / P $1.21 ｜ ATM IV 41.2%，净 delta 敞口 2.1M shares
Top ΔOI: C 88 +15,691 ｜ C 90 +15,040 ｜ C 89 +9,934
仓位参考: Max Pain 87 ｜ Call Wall 88（+0.7%，弱）（OI 16.3k） ｜ Put Wall 82（-6.2%，弱）（OI 6.7k）
量化解读： 存量 Call 重｜ATM IV 41.2%｜历史 Rank 61%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,146,409 股

📆 10-16 Forward Structure
存量OI: C 100.8k / P 109.8k，今日变化ΔOI: C +4.3k / P +3.6k，平值价格ATM: C $2.98 / P $1.93 ｜ ATM IV 40.4%，净 delta 敞口 -3k shares
Top ΔOI: C 96 +2,018 ｜ P 85 +1,796 ｜ C 90 +1,787
仓位参考: Max Pain 92 ｜ Call Wall 90（+3.0%，弱）（OI 8.5k） ｜ Put Wall 90（+3.0%，弱）（OI 10.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 40.4%｜历史 Rank 61%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,406 股

📆 10-23 Forward Structure
存量OI: C 6.1k / P 6.9k，今日变化ΔOI: C +0.4k / P +81，平值价格ATM: C $3.30 / P $3.05 ｜ ATM IV 38.5%，净 delta 敞口 2k shares
Top ΔOI: P 86 +62 ｜ C 93 +49
仓位参考: Max Pain 94 ｜ Call Wall 90（+3.0%，弱）（OI 0.4k） ｜ Put Wall 93（+6.4%，弱）（OI 1.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 38.5%｜历史 Rank 61%（近端代理）｜IV/RV 1.10×（近似）｜净 delta 敞口 正 1,753 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/GDX_evening.json