# 期权晚报 2026-09-04（快照 17:18 ET）

📊 市场环境

SPY $770.19 ｜ QQQ $718.96
VIX 14.53 ↑1.5%（5D +0.7%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 162.74 → 收盘 163.81（+0.7%） ｜ 今日高 164.35 ｜ 低 162.51 ｜ 昨收 164.38 → 收盘 163.81（-0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.46 | OI比 1.60 | ATM IV 21.1% | Skew -105.6pp | Term 1.52 | ExpMove ±0.5% | Rank 1%
量化视角： IV 历史低位（Rank 1%，期权偏便宜）｜期限结构正常偏陡（Term 1.52）｜Put 保护异常便宜（Skew -105.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.60×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) nan | GEX Change vs 上次快照 nan | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 待盘点 ｜ IV 有效性: VALID 362 / LOW 153 / INVALID 19
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 158（弱结构｜现价高于该位 3.7%） | Call Wall 170（弱结构｜现价低于该位 3.6%）
最近结构参考: Call Wall 170（现价低于该位 3.6%）
量化视角： 正 Gamma（nan万，无历史分位）｜GEX 变化（nan万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 158（Put Wall，弱结构）；上方 164（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 162.5P — Vol 2,004 | 最新价 $0.74 | OI 23→1004 (ΔOI +981张) | ΔOI/Volume 49.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增981张（+4265.2% vs前日OI），连续性待观察（方向未知）
09-04 168.0C — Vol 772 | 最新价 $0.17 | OI 1115→1548 (ΔOI +433张) | ΔOI/Volume 56.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增433张（+38.8% vs前日OI），连续性待观察（方向未知）
09-11 160.0P — Vol 363 | 最新价 $1.20 | OI 108→439 (ΔOI +331张) | ΔOI/Volume 91.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增331张（+306.5% vs前日OI），连续性待观察（方向未知）
09-04 170.0C — Vol 602 | 最新价 $0.03 | OI 742→986 (ΔOI +244张) | ΔOI/Volume 40.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增244张（+32.9% vs前日OI），连续性待观察（方向未知）
09-18 165.0P — Vol 187 | 最新价 $4.45 | OI 52→229 (ΔOI +177张) | ΔOI/Volume 94.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增177张（+340.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,166 张（Put 1,489 / Call 677），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/XBI_evening.json