# 期权晨报 2026-11-06（快照 10:20 ET）

📊 市场环境

SPY $740.12 ｜ QQQ $659.81
VIX 24.90 ↓11.6%（5D +28.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
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
🟡 **近现价集中开仓**: 11-13 180C ΔOI +2,116（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-04 140P ΔOI -1,283 占该期限总 OI 11.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 167.52 → 今开 183.31（+9.4%） | 较昨收变动（含盘初走势） ｜ 今日高 186.30 ｜ 低 176.65

Options: P/C成交量 0.56 | OI比 0.45 | ATM IV 186.6% | Skew 20.7pp | Term 0.52 | ExpMove ±12.9%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.52，近月 IV 高于远月）｜保护溢价显著（Skew 20.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.45）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.45×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（7D）±12.9% ｜ 11-20（14D）±16.7% ｜ 11-27（21D）±19.6% ｜ 12-04（28D）±21.4%
   ⇒ IV–VIX Spread: +161.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -353,943 | GEX Change vs 上次快照 8,359,205 | Flip: Primary Flip: 181.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 507 / LOW 142 / INVALID 313
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 181.35（全链重定价，覆盖 97%）
最近结构参考: Flip 181（现价低于该位 0.5%）
量化视角： 负 Gamma（35万，无历史分位）｜负 Gamma 缓解（+836万）｜现价位于 Flip 下方 0.48%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 188（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 181（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 145.0P — Vol 4,185 | 最新价 $7.72 | OI 656→3424 (ΔOI +2768张) | ΔOI/Volume 66.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2768张（+421.9% vs前日OI），连续性待观察（方向未知）
11-13 180.0C — Vol 2,681 | 最新价 $8.41 | OI 41→2157 (ΔOI +2116张) | ΔOI/Volume 78.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2116张（+5161.0% vs前日OI），连续性待观察（方向未知）
11-20 140.0P — Vol 2,832 | 最新价 $6.21 | OI 1517→3449 (ΔOI +1932张) | ΔOI/Volume 68.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1932张（+127.4% vs前日OI），连续性待观察（方向未知）
11-06 155.0P — Vol 4,027 | 最新价 $2.62 | OI 569→2149 (ΔOI +1580张) | ΔOI/Volume 39.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1580张（+277.7% vs前日OI），连续性待观察（方向未知）
11-13 130.0C — Vol 1,350 | 最新价 $42.49 | OI 1→1351 (ΔOI +1350张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1350张（+135000.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,746 张（Put 6,280 / Call 3,466），跨 3 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 65.9k / P 29.6k，今日成交量: C 10.9k / P 6.2k，平值价格ATM: C $3.53 / P $3.67 ｜ ATM IV 186.6%，预期波动 ±4.0%，Max Pain 188
Top ΔOI: P 235 -1,581 ｜ P 155 +1,580 ｜ P 240 -1,390

📆 Forward Expiration Structure

11-13  C +9.4k / P +2.9k ｜ Activity HIGH ｜ 7D
11-20  C +6.7k / P +2.5k ｜ Activity MEDIUM △ ｜ 14D
11-27  C +1.3k / P -0.5k ｜ Activity MEDIUM △ ｜ 21D
12-04  C +0.3k / P -0.9k ｜ Activity MEDIUM △ ｜ 28D

📆 11-13 Forward Structure
存量OI: C 24.4k / P 17.2k，今日变化ΔOI: C +9.4k / P +2.9k，平值价格ATM: C $11.85 / P $11.53 ｜ ATM IV 115.8%，净 delta 敞口 664k shares
Top ΔOI: C 180 +2,116 ｜ C 130 +1,350 ｜ C 140 +1,262
仓位参考: Max Pain 185 ｜ Call Wall 180（-0.3%）（OI 2.2k） ｜ Put Wall 165（-8.6%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 115.8%｜历史 Rank 96%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 664,004 股

11-20（MEDIUM △）Top ΔOI: 145P +2,768 ｜ 140P +1,932
11-20（MEDIUM △）仓位参考: Max Pain 220 ｜ Call Wall 190（+5.3%，弱）（OI 2.2k） ｜ Put Wall 170（-5.8%，弱）（OI 4.2k）

11-27（MEDIUM △）Top ΔOI: 200P -774 ｜ 200C +355
11-27（MEDIUM △）仓位参考: Max Pain 220 ｜ Put Wall 190（+5.3%，弱）（OI 1.1k）

12-04（MEDIUM △）Top ΔOI: 140P -1,283 ｜ 150P +121
12-04（MEDIUM △）仓位参考: Max Pain 210 ｜ Put Wall 190（+5.3%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 11-13（7D）ATM IV 115.8% vs 11-20 107.1%（差 +8.7pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/BE_morning.json