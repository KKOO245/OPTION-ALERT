# 期权晨报 2026-09-17（快照 11:28 ET）

📊 市场环境

SPY $760.90 ｜ QQQ $715.92
VIX 15.87 ↓10.4%（5D -11.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 48.99 → 今开 50.42（+2.9%） | 较昨收变动（含盘初走势） ｜ 今日高 50.50 ｜ 低 49.22

Options: P/C成交量 0.85 | OI比 0.76 | ATM IV 73.4% | Skew -2.7pp | Term 0.81 | ExpMove ±2.6%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.76）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.85×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（1D）±2.6% ｜ 09-25（8D）±7.3% ｜ 10-02（15D）±11.2% ｜ 10-09（22D）±10.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -8,171,010 | GEX Change vs 上次快照 364,420 | Flip: Primary Flip: 52.60（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 233 / LOW 76 / INVALID 121
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 52.60（全链重定价，覆盖 89%）
最近结构参考: Flip 53（现价低于该位 6.1%）
量化视角： 负 Gamma（817万，无历史分位）｜负 Gamma 缓解（+36万）｜现价位于 Flip 下方 6.11%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 55（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 53（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 43.0P — Vol 531 | 最新价 $0.25 | OI 194→697 (ΔOI +503张) | ΔOI/Volume 94.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增503张（+259.3% vs前日OI），连续性待观察（方向未知）
10-16 50.0C — Vol 309 | 最新价 $3.20 | OI 978→1187 (ΔOI +209张) | ΔOI/Volume 67.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增209张（+21.4% vs前日OI），连续性待观察（方向未知）
10-16 60.0C — Vol 274 | 最新价 $0.75 | OI 2395→2595 (ΔOI +200张) | ΔOI/Volume 73.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增200张（+8.3% vs前日OI），连续性待观察（方向未知）
09-18 52.0C — Vol 382 | 最新价 $0.18 | OI 420→568 (ΔOI +148张) | ΔOI/Volume 38.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增148张（+35.2% vs前日OI），连续性待观察（方向未知）
09-18 49.0C — Vol 245 | 最新价 $1.01 | OI 103→247 (ΔOI +144张) | ΔOI/Volume 58.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增144张（+139.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,204 张（Put 503 / Call 701），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0.2k / P -1.4k ｜ Activity MEDIUM △ ｜ 1D
09-25  C +0.3k / P +0.9k ｜ Activity MEDIUM △ ｜ 8D
10-02  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 15D
10-09  C +43 / P +59 ｜ Activity LOW ｜ 22D

📆 09-18 Forward Structure
存量OI: C 54.3k / P 41.1k，今日变化ΔOI: C +0.2k / P -1.4k，平值价格ATM: C $0.71 / P $0.59 ｜ ATM IV 73.4%，净 delta 敞口 150k shares
Top ΔOI: P 60 -950 ｜ P 65 -165 ｜ C 52 +148
仓位参考: Max Pain 55 ｜ Call Wall 50（+1.2%，弱）（OI 1.7k） ｜ Put Wall 45（-8.9%，弱）（OI 6.7k）
量化解读： 存量 Call 重｜ATM IV 73.4%｜历史 Rank 60%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 150,017 股

09-25（MEDIUM △）Top ΔOI: 52C +83
09-25（MEDIUM △）仓位参考: Max Pain 53 ｜ Call Wall 54（+9.3%，弱）（OI 0.3k） ｜ Put Wall 50（+1.2%，弱）（OI 0.5k）

10-02（MEDIUM △）Top ΔOI: 54P +70 ｜ 50C +41
10-02（MEDIUM △）仓位参考: Max Pain 55 ｜ Put Wall 50（+1.2%）（OI 1.3k）

10-09（Activity LOW）仓位参考: Max Pain 53 ｜ Put Wall 47（-4.8%）（OI 1.1k）

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 73.4% vs 09-25 65.1%（差 +8.3pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/MP_morning.json