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


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 759.00 → 收盘 760.88（+0.2%） ｜ 今日高 763.52 ｜ 低 757.93 ｜ 昨收 764.29 → 收盘 760.88（-0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.15 | OI比 2.08 | ATM IV 11.8% | Skew -0.5pp | Term 1.14 | ExpMove ±0.5%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构正常（Term 1.14）｜Put 保护异常便宜（Skew -0.5pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.15）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.15×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.08×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 19% ｜ P/C OI(近端) 67%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 19%）｜近端持仓结构中性（P/C OI 分位 67%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-15（1D）±0.5% ｜ 09-16（2D）±0.9% ｜ 09-17（3D）±1.2% ｜ 09-18（4D）±1.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,799,096,772 | GEX Change vs 上次快照 47,759,387 | Flip: Primary Flip: 770.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 3367 / LOW 417 / INVALID 1846
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 770.44（全链重定价，覆盖 94%）
Call Wall 800（弱结构｜现价低于该位 4.9%）
最近结构参考: Flip 770（现价低于该位 1.2%）
量化视角： 负 Gamma（17.99亿，历史分位偏负区，比 81% 的交易日更负）｜负 Gamma 缓解（+4776万）｜现价位于 Flip 下方 1.24%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 764（MaxPain，仅结算参考） / 800（Call Wall，弱结构）。
• Gamma 区域：切换参考 770（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-14 719.0P — Vol 1 | 最新价 $0.01 | OI 52→30540 (ΔOI +30488张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30488张（+58630.8% vs前日OI），连续性待观察（方向未知）
09-25 740.0P — Vol 1,684 | 最新价 $2.46 | OI 3316→25536 (ΔOI +22220张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22220张（+670.1% vs前日OI），连续性待观察（方向未知）
09-15 760.0P — Vol 97,714 | 最新价 $1.59 | OI 21967→43115 (ΔOI +21148张) | ΔOI/Volume 21.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21148张（+96.3% vs前日OI），连续性待观察（方向未知）
09-25 785.0C — Vol 2,690 | 最新价 $0.20 | OI 3952→24898 (ΔOI +20946张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20946张（+530.0% vs前日OI），连续性待观察（方向未知）
09-18 743.0P — Vol 2,271 | 最新价 $1.37 | OI 28452→49229 (ΔOI +20777张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20777张（+73.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 115,579 张（Put 94,633 / Call 20,946），跨 4 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $12M，买/卖方向不可观测）｜彩票/名义 1 档（价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-15  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-16  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-17  C +0 / P +0 ｜ Activity LOW ｜ 3D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 4D

📆 09-15 Forward Structure
存量OI: C 50.5k / P 153.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.90 / P $2.00 ｜ ATM IV 12.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 764 ｜ Call Wall 770（+1.2%，弱）（OI 5.1k） ｜ Put Wall 760（-0.1%）（OI 43.1k）
量化解读： 存量 Put 重｜ATM IV 12.2%｜历史 Rank 40%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

09-16（Activity LOW）仓位参考: Max Pain 764 ｜ Call Wall 775（+1.9%，弱）（OI 3.5k） ｜ Put Wall 760（-0.1%，弱）（OI 4.1k）

09-17（Activity LOW）仓位参考: Max Pain 762 ｜ Call Wall 775（+1.9%，弱）（OI 4.5k） ｜ Put Wall 750（-1.4%，弱）（OI 4.7k）

09-18（Activity LOW）仓位参考: Max Pain 755 ｜ Call Wall 790（+3.8%，弱）（OI 57.7k） ｜ Put Wall 750（-1.4%，弱）（OI 135.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/SPY_evening.json