# 期权晨报 2026-10-02（快照 10:20 ET）

📊 市场环境

SPY $769.72 ｜ QQQ $749.58
VIX 15.56 ↓5.1%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 13.80 → 今开 14.08（+2.0%） | 较昨收变动（含盘初走势） ｜ 今日高 14.08 ｜ 低 13.57

Options: P/C成交量 0.38 | OI比 0.27 | ATM IV 101.0% | Skew 8.2pp | Term 0.67 | ExpMove ±7.4%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构倒挂（Term 0.67，近月 IV 高于远月）｜保护溢价显著（Skew 8.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.27）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.27×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±7.4% ｜ 10-16（14D）±10.6% ｜ 10-23（21D）±13.0% ｜ 10-30（28D）±14.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 373,729 | GEX Change vs 上次快照 2,440,569 | Flip: Primary Flip: 13.60（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 180 / LOW 74 / INVALID 150
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 13.60（全链重定价，覆盖 90%）
Put Wall 15（弱结构｜现价低于该位 8.5%）
最近结构参考: Flip 14（现价高于该位 0.9%）
量化视角： 正 Gamma（37万，无历史分位）｜由负转正（+244万）｜现价位于 Flip 上方 0.93%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 15（Put Wall，弱结构） / 15（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 14（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 15.5P — Vol 514 | 最新价 $1.90 | OI 338→846 (ΔOI +508张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增508张（+150.3% vs前日OI），连续性待观察（方向未知）
10-16 13.5P — Vol 495 | 最新价 $0.57 | OI 217→678 (ΔOI +461张) | ΔOI/Volume 93.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增461张（+212.4% vs前日OI），连续性待观察（方向未知）
10-30 12.5P — Vol 433 | 最新价 $0.48 | OI 199→624 (ΔOI +425张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增425张（+213.6% vs前日OI），连续性待观察（方向未知）
10-02 14.0C — Vol 1,192 | 最新价 $0.14 | OI 705→1102 (ΔOI +397张) | ΔOI/Volume 33.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增397张（+56.3% vs前日OI），连续性待观察（方向未知）
10-09 13.5P — Vol 440 | 最新价 $0.35 | OI 298→666 (ΔOI +368张) | ΔOI/Volume 83.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增368张（+123.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,159 张（Put 1,762 / Call 397），跨 4 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 27.4k / P 7.4k，今日成交量: C 0.8k / P 0.3k，平值价格ATM: C $0.29 / P $0.07 ｜ ATM IV 101.0%，预期波动 ±2.5%，Max Pain 15
Top ΔOI: P 16 -1,649 ｜ P 15 -773 ｜ P 16 -730

📆 Forward Expiration Structure

10-09  C +0.5k / P +0.1k ｜ Activity HIGH ｜ 7D
10-16  C -0.5k / P +0.7k ｜ Activity MEDIUM △ ｜ 14D
10-23  C -17 / P +0.6k ｜ Activity MEDIUM △ ｜ 21D
10-30  C -0.3k / P +0.9k ｜ Activity MEDIUM △ ｜ 28D

📆 10-09 Forward Structure
存量OI: C 10.8k / P 6.7k，今日变化ΔOI: C +0.5k / P +0.1k，平值价格ATM: C $0.60 / P $0.42 ｜ ATM IV 64.4%，净 delta 敞口 36k shares
Top ΔOI: P 15 -441 ｜ P 13 +368 ｜ C 15 +237
仓位参考: Max Pain 16 ｜ Call Wall 15（+9.3%，弱）（OI 1.1k） ｜ Put Wall 14（+2.0%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 64.4%｜历史 Rank 26%（近端代理）｜IV/RV 1.17×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 35,803 股

10-16（MEDIUM △）Top ΔOI: 15P +508 ｜ 13P +461
10-16（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 15（+9.3%）（OI 5.6k）

10-23（MEDIUM △）Top ΔOI: 16P +359 ｜ 14P +61
10-23（MEDIUM △）仓位参考: Max Pain 17 ｜ Put Wall 15（+9.3%，弱）（OI 0.5k）

10-30（MEDIUM △）Top ΔOI: 12P +425 ｜ 17P +153
10-30（MEDIUM △）仓位参考: Max Pain 16 ｜ Call Wall 15（+9.3%，弱）（OI 0.3k） ｜ Put Wall 14（+2.0%）（OI 2.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/USAR_morning.json