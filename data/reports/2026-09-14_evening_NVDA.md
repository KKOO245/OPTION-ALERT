# 期权晚报 2026-09-14（快照 16:48 ET）

📊 市场环境

SPY $760.88 ｜ QQQ $709.18
VIX 17.10 ↑8.0%（5D +11.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.9 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 211.08 → 收盘 210.96（-0.1%） ｜ 今日高 212.77 ｜ 低 208.93 ｜ 昨收 218.29 → 收盘 210.96（-3.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.77 | OI比 0.69 | ATM IV 41.0% | Skew 10.2pp | Term 0.82 | ExpMove ±2.3%（近端） | Rank 42%
量化视角： IV 中性（Rank 42%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价显著（Skew 10.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.69）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-16（2D）±2.3% ｜ 09-18（4D）±3.2% ｜ 09-21（7D）±3.7% ｜ 09-23（9D）±4.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 34,450,629 | GEX Change vs 上次快照 23,737,866 | Flip: Primary Flip: 209.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 674 / LOW 204 / INVALID 660
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 209.69（全链重定价，覆盖 96%）
Put Wall 200（弱结构｜现价高于该位 5.5%）
最近结构参考: Flip 210（现价高于该位 0.6%）
量化视角： 正 Gamma（3445万，无历史分位）｜正 Gamma 增强（+2374万）｜现价位于 Flip 上方 0.60%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 210（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 232.5C — Vol 4,096 | 最新价 $0.07 | OI 10792→32348 (ΔOI +21556张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21556张（+199.7% vs前日OI），连续性待观察（方向未知）
09-18 225.0C — Vol 33,523 | 最新价 $0.23 | OI 56693→77122 (ΔOI +20429张) | ΔOI/Volume 60.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20429张（+36.0% vs前日OI），连续性待观察（方向未知）
09-14 225.0C — Vol 12,115 | 最新价 $0.01 | OI 8953→24892 (ΔOI +15939张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15939张（+178.0% vs前日OI），连续性待观察（方向未知）
09-14 222.5C — Vol 6,526 | 最新价 $0.01 | OI 2416→9667 (ΔOI +7251张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7251张（+300.1% vs前日OI），连续性待观察（方向未知）
09-18 235.0C — Vol 14,683 | 最新价 $0.04 | OI 48172→55384 (ΔOI +7212张) | ΔOI/Volume 49.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7212张（+15.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 72,387 张（Put 0 / Call 72,387），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-16  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-21  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-23  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 09-16 Forward Structure
存量OI: C 56.7k / P 38.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.96 / P $1.97 ｜ ATM IV 38.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 220 ｜ Call Wall 230（+9.0%，弱）（OI 7.0k） ｜ Put Wall 215（+1.9%，弱）（OI 4.1k）
量化解读： 存量 Call 重｜ATM IV 38.6%｜历史 Rank 42%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-18（Activity LOW）仓位参考: Max Pain 205 ｜ Call Wall 230（+9.0%，弱）（OI 94.9k） ｜ Put Wall 210（-0.5%，弱）（OI 50.9k）

09-21（Activity LOW）仓位参考: Max Pain 218 ｜ Call Wall 230（+9.0%，弱）（OI 3.0k）

09-23（Activity LOW）仓位参考: Max Pain 225 ｜ Call Wall 230（+9.0%）（OI 4.4k） ｜ Put Wall 225（+6.7%）（OI 1.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/NVDA_evening.json