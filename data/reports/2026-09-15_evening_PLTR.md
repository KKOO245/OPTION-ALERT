# 期权晚报 2026-09-15（快照 16:40 ET）

📊 市场环境

SPY $757.39 ｜ QQQ $704.54
VIX 17.20 ↑0.6%（5D +9.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：无更新，来源自 2026-09-14

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 170.24 → 收盘 172.56（+1.4%） ｜ 今日高 176.59 ｜ 低 169.45 ｜ 昨收 173.31 → 收盘 172.56（-0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.68 | OI比 0.79 | ATM IV 51.7% | Skew 1.1pp | Term 0.95 | ExpMove ±4.3% | Rank 29%
量化视角： IV 中性（Rank 29%）｜期限结构正常（Term 0.95）｜保护溢价薄（Skew 1.1pp）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.68×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) nan | GEX Change vs 上次快照 nan | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 待盘点 ｜ IV 有效性: VALID 632 / LOW 79 / INVALID 32
结构观察区: NO_CROSS
Put Wall 170（弱结构｜现价高于该位 1.5%） | Call Wall 180（弱结构｜现价低于该位 4.1%）
最近结构参考: Put Wall 170（现价高于该位 1.5%）
量化视角： 正 Gamma（nan万，无历史分位）｜GEX 变化（nan万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Put Wall，弱结构） / 155（MaxPain，仅结算参考）；上方 180（Call Wall，弱结构）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 180.0C — Vol 31,558 | 最新价 $1.18 | OI 20040→30400 (ΔOI +10360张) | ΔOI/Volume 32.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10360张（+51.7% vs前日OI），连续性待观察（方向未知）
09-18 182.5C — Vol 8,127 | 最新价 $0.77 | OI 2583→10891 (ΔOI +8308张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8308张（+321.6% vs前日OI），连续性待观察（方向未知）
09-25 100.0P — Vol 17 | 最新价 $0.03 | OI 3883→6572 (ΔOI +2689张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2689张（+69.2% vs前日OI），连续性待观察（方向未知）
09-18 160.0P — Vol 22,574 | 最新价 $0.49 | OI 11509→14037 (ΔOI +2528张) | ΔOI/Volume 11.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2528张（+22.0% vs前日OI），连续性待观察（方向未知）
09-18 177.5C — Vol 17,910 | 最新价 $1.79 | OI 12530→14651 (ΔOI +2121张) | ΔOI/Volume 11.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2121张（+16.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 26,006 张（Put 5,217 / Call 20,789），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/PLTR_evening.json