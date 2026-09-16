# 期权晨报 2026-09-16（快照 11:22 ET）

📊 市场环境

SPY $760.53 ｜ QQQ $710.93
VIX 16.68 ↓3.0%（5D +1.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75　⏰ 今日
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　⏰ 今日
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　⏰ 今日
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 49.17 → 今开 49.56（+0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 49.70 ｜ 低 48.60

Options: P/C成交量 0.88 | OI比 0.79 | ATM IV 74.2% | Skew -0.2pp | Term 0.84 | ExpMove ±4.8%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.88×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（2D）±4.8% ｜ 09-25（9D）±8.3% ｜ 10-02（16D）±10.7% ｜ 10-09（23D）±11.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,386,164 | GEX Change vs 上次快照 1,273,117 | Flip: Primary Flip: 51.37（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 262 / LOW 57 / INVALID 99
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 51.37（全链重定价，覆盖 85%）
最近结构参考: Flip 51（现价低于该位 4.3%）
量化视角： 负 Gamma（539万，无历史分位）｜负 Gamma 缓解（+127万）｜现价位于 Flip 下方 4.27%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 55（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 51（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 55.0C — Vol 340 | 最新价 $1.00 | OI 166→459 (ΔOI +293张) | ΔOI/Volume 86.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增293张（+176.5% vs前日OI），连续性待观察（方向未知）
09-18 48.0C — Vol 407 | 最新价 $2.15 | OI 51→218 (ΔOI +167张) | ΔOI/Volume 41.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增167张（+327.4% vs前日OI），连续性待观察（方向未知）
09-18 48.5P — Vol 194 | 最新价 $0.83 | OI 83→250 (ΔOI +167张) | ΔOI/Volume 86.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增167张（+201.2% vs前日OI），连续性待观察（方向未知）
09-25 53.0P — Vol 154 | 最新价 $4.55 | OI 249→377 (ΔOI +128张) | ΔOI/Volume 83.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增128张（+51.4% vs前日OI），连续性待观察（方向未知）
09-25 54.0P — Vol 152 | 最新价 $5.32 | OI 296→412 (ΔOI +116张) | ΔOI/Volume 76.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增116张（+39.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 871 张（Put 411 / Call 460），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +44 / P -0.4k ｜ Activity MEDIUM △ ｜ 2D
09-25  C +0.2k / P +0.5k ｜ Activity HIGH ｜ 9D
10-02  C +0.4k / P +69 ｜ Activity MEDIUM △ ｜ 16D
10-09  C +20 / P +31 ｜ Activity MEDIUM △ ｜ 23D

📆 09-18 Forward Structure
存量OI: C 54.1k / P 42.5k，今日变化ΔOI: C +44 / P -0.4k，平值价格ATM: C $1.16 / P $1.19 ｜ ATM IV 74.2%，净 delta 敞口 83k shares
Top ΔOI: P 60 -204 ｜ P 65 -172
仓位参考: Max Pain 55 ｜ Call Wall 50（+1.7%，弱）（OI 1.7k） ｜ Put Wall 45（-8.5%，弱）（OI 6.8k）
量化解读： 存量 Call 重｜ATM IV 74.2%｜历史 Rank 60%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 83,378 股

📆 09-25 Forward Structure
存量OI: C 5.8k / P 5.9k，今日变化ΔOI: C +0.2k / P +0.5k，平值价格ATM: C $2.10 / P $1.96 ｜ ATM IV 64.9%，净 delta 敞口 -21k shares
Top ΔOI: P 53 +128 ｜ P 54 +116
仓位参考: Max Pain 54 ｜ Call Wall 45（-8.5%，弱）（OI 0.3k） ｜ Put Wall 50（+1.7%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 64.9%｜历史 Rank 60%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 20,532 股

10-02（MEDIUM △）仓位参考: Max Pain 55 ｜ Put Wall 50（+1.7%）（OI 1.2k）

10-09（MEDIUM △）Top ΔOI: 47P +15 ｜ 48P +9
10-09（MEDIUM △）仓位参考: Max Pain 52 ｜ Put Wall 47（-4.4%）（OI 1.0k）

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 74.2% vs 09-25 64.9%（差 +9.3pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/MP_morning.json