# 期权晚报 2026-09-15（快照 18:31 ET）

📊 市场环境

SPY $757.39 ｜ QQQ $nan
VIX 17.20 ↑0.6%（5D +9.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 50.47 → 收盘 49.17（-2.6%） ｜ 今日高 51.18 ｜ 低 48.88 ｜ 昨收 50.68 → 收盘 49.17（-3.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-18，窗口结束前不做对错判定）

Options: P/C成交量 1.01 | OI比 0.79 | ATM IV 66.4% | Skew -7.3pp | Term 0.92 | ExpMove ±5.0%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -7.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.01×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（3D）±5.0% ｜ 09-25（10D）±8.4% ｜ 10-02（17D）±11.2% ｜ 10-09（24D）±11.4%
   ⇒ IV–VIX Spread: +49.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,659,282 | GEX Change vs 上次快照 -1,029,137 | Flip: Primary Flip: 52.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 257 / LOW 49 / INVALID 112
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 52.93（全链重定价，覆盖 98%）
最近结构参考: Flip 53（现价低于该位 7.1%）
量化视角： 负 Gamma（666万，无历史分位）｜负 Gamma 加深（103万）｜现价位于 Flip 下方 7.10%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 55（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 53（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 55.0P — Vol 45 | 最新价 $7.27 | OI 789→4060 (ΔOI +3271张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3271张（+414.6% vs前日OI），连续性待观察（方向未知）
10-16 60.0C — Vol 394 | 最新价 $0.90 | OI 1865→2300 (ΔOI +435张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增435张（+23.3% vs前日OI），值得跟踪（方向未知）
09-18 53.0C — Vol 137 | 最新价 $0.47 | OI 363→744 (ΔOI +381张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增381张（+105.0% vs前日OI），值得跟踪（方向未知）
09-18 55.0C — Vol 556 | 最新价 $0.16 | OI 4803→5173 (ΔOI +370张) | ΔOI/Volume 66.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增370张（+7.7% vs前日OI），连续性待观察（方向未知）
09-18 54.0C — Vol 223 | 最新价 $0.26 | OI 1417→1761 (ΔOI +344张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增344张（+24.3% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,801 张（Put 3,271 / Call 1,530），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 3D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 10D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 17D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 09-18 Forward Structure
存量OI: C 54.0k / P 42.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.37 / P $1.11 ｜ ATM IV 66.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 55 ｜ Call Wall 54（+9.8%，弱）（OI 1.8k） ｜ Put Wall 45（-8.5%，弱）（OI 6.7k）
量化解读： 存量 Call 重｜ATM IV 66.4%｜历史 Rank 48%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 54 ｜ Call Wall 45（-8.5%，弱）（OI 0.3k） ｜ Put Wall 50（+1.7%，弱）（OI 0.5k）

10-02（Activity LOW）仓位参考: Max Pain 58 ｜ Put Wall 50（+1.7%）（OI 1.2k）

10-09（Activity LOW）仓位参考: Max Pain 52 ｜ Put Wall 47（-4.4%）（OI 1.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=22 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=22）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/MP_evening.json