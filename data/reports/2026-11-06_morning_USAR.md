# 期权晨报 2026-11-06（快照 10:20 ET）

📊 市场环境

SPY $735.23 ｜ QQQ $656.10
VIX 24.90 ↓11.6%（5D +28.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 22.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 165 ｜ 前值 60　✅ 今日已公布
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 4.1 ｜ 前值 4.2　✅ 今日已公布
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 51 ｜ 前值 46.3　✅ 今日已公布

🔍 重点速览
🟡 **事件差分**: 11-13 ATM IV 122.7% vs 11-20 112.6%（差 +10.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-13 8C ΔOI +893（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 7.42 → 今开 7.77（+4.7%） | 较昨收变动（含盘初走势） ｜ 今日高 8.01 ｜ 低 7.47

Options: P/C成交量 0.17 | OI比 0.32 | ATM IV 175.1% | Skew 5.0pp | Term 0.60 | ExpMove ±14.6%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.60，近月 IV 高于远月）｜保护溢价中性（Skew 5.0pp）｜存量 Call 偏重（OI比 0.32）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.17×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.32×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（7D）±14.6% ｜ 11-20（14D）±18.3% ｜ 11-27（21D）±20.7% ｜ 12-04（28D）±22.1%
   ⇒ IV–VIX Spread: +150.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 1,174,791 | GEX Change vs 上次快照 1,581,405 | Flip: Primary Flip: 7.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 216 / LOW 62 / INVALID 136
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 7.34（全链重定价，覆盖 97%）
Put Wall 8（弱结构｜现价低于该位 1.4%）
最近结构参考: Put Wall 8（现价低于该位 1.4%）
量化视角： 正 Gamma（117万，无历史分位）｜由负转正（+158万）｜现价位于 Flip 上方 7.44%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 8（Put Wall，弱结构） / 8（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 7（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 8.0P — Vol 4,494 | 最新价 $1.09 | OI 2577→6667 (ΔOI +4090张) | ΔOI/Volume 91.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4090张（+158.7% vs前日OI），连续性待观察（方向未知）
11-20 8.0C — Vol 1,566 | 最新价 $0.52 | OI 189→1648 (ΔOI +1459张) | ΔOI/Volume 93.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1459张（+772.0% vs前日OI），连续性待观察（方向未知）
11-06 8.0C — Vol 2,080 | 最新价 $0.05 | OI 335→1727 (ΔOI +1392张) | ΔOI/Volume 66.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1392张（+415.5% vs前日OI），连续性待观察（方向未知）
11-13 7.0C — Vol 1,208 | 最新价 $0.80 | OI 8→1195 (ΔOI +1187张) | ΔOI/Volume 98.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1187张（+14837.5% vs前日OI），连续性待观察（方向未知）
11-20 7.0P — Vol 1,192 | 最新价 $0.55 | OI 581→1550 (ΔOI +969张) | ΔOI/Volume 81.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增969张（+166.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,097 张（Put 5,059 / Call 4,038），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 19.7k / P 6.3k，今日成交量: C 0.7k / P 0.1k，平值价格ATM: C $0.08 / P $0.24 ｜ ATM IV 175.1%，预期波动 ±4.1%，Max Pain 8
Top ΔOI: C 8 +1,392 ｜ P 9 -1,111 ｜ P 10 -577

📆 Forward Expiration Structure

11-13  C +2.7k / P +0.2k ｜ Activity HIGH ｜ 7D
11-20  C +1.6k / P +1.8k ｜ Activity MEDIUM △ ｜ 14D
11-27  C +0.1k / P +66 ｜ Activity LOW ｜ 21D
12-04  C +0.1k / P +0.1k ｜ Activity MEDIUM △ ｜ 28D

📆 11-13 Forward Structure
存量OI: C 13.9k / P 3.6k，今日变化ΔOI: C +2.7k / P +0.2k，平值价格ATM: C $0.47 / P $0.68 ｜ ATM IV 122.7%，净 delta 敞口 186k shares
Top ΔOI: C 7 +1,187 ｜ C 8 +893
仓位参考: Max Pain 8 ｜ Call Wall 8（+1.5%，弱）（OI 0.9k） ｜ Put Wall 8（+1.5%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 122.7%｜历史 Rank 94%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 185,764 股

11-20（MEDIUM △）Top ΔOI: 8P +4,090 ｜ 10P -2,571
11-20（MEDIUM △）仓位参考: Max Pain 11 ｜ Call Wall 8（+1.5%，弱）（OI 1.6k） ｜ Put Wall 8（+1.5%，弱）（OI 6.7k）

11-27（Activity LOW）仓位参考: Max Pain 10 ｜ Put Wall 8（+1.5%，弱）（OI 0.4k）

12-04（MEDIUM △）Top ΔOI: 7C +47
12-04（MEDIUM △）仓位参考: Max Pain 10 ｜ Put Wall 8.5（+7.8%，弱）（OI 0.1k）

📅 事件差分（观察，非因果）: 11-13（7D）ATM IV 122.7% vs 11-20 112.6%（差 +10.1pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/USAR_morning.json