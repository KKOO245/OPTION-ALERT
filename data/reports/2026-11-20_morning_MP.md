# 期权晨报 2026-11-20（快照 10:20 ET）

📊 市场环境

SPY $692.49 ｜ QQQ $608.45
VIX 27.48 ↓3.4%（5D +42.4%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 9.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 12-04 37C ΔOI +19（距现价 +2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 36.66 → 今开 35.94（-2.0%） | 较昨收变动（含盘初走势） ｜ 今日高 37.59 ｜ 低 35.79

Options: P/C成交量 1.19 | OI比 0.35 | ATM IV 100.5% | Skew -63.6pp | Term 0.73 | ExpMove ±8.0%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜Put 保护异常便宜（Skew -63.6pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.35）+ 当日成交偏 Put（P/C量 1.19）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.19×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.35×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（7D）±8.0% ｜ 12-04（14D）±13.2% ｜ 12-11（21D）±14.1% ｜ 12-18（28D）±16.1%
   ⇒ IV–VIX Spread: +73.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,878,086 | GEX Change vs 上次快照 -3,296,033 | Flip: Primary Flip: 35.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 254 / LOW 84 / INVALID 26
结构观察区: Primary Flip 35.45（全链重定价，覆盖 98%）
Put Wall 35（现价高于该位 2.7%）
最近结构参考: Flip 35（现价高于该位 1.4%）
量化视角： 正 Gamma（288万，无历史分位）｜正 Gamma 减弱（330万）｜现价位于 Flip 上方 1.38%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall）；上方 37（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 35（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 34.0P — Vol 923 | 最新价 $0.52 | OI 183→975 (ΔOI +792张) | ΔOI/Volume 85.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增792张（+432.8% vs前日OI），连续性待观察（方向未知）
12-18 50.0C — Vol 662 | 最新价 $0.25 | OI 18187→18676 (ΔOI +489张) | ΔOI/Volume 73.9% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增489张（+2.7% vs前日OI），值得跟踪（方向未知）
11-20 40.0C — Vol 570 | 最新价 $0.05 | OI 2667→3012 (ΔOI +345张) | ΔOI/Volume 60.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增345张（+12.9% vs前日OI），连续性待观察（方向未知）
12-18 35.0C — Vol 296 | 最新价 $3.79 | OI 1927→2124 (ΔOI +197张) | ΔOI/Volume 66.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增197张（+10.2% vs前日OI），连续性待观察（方向未知）
11-20 38.5C — Vol 232 | 最新价 $0.16 | OI 826→1014 (ΔOI +188张) | ΔOI/Volume 81.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增188张（+22.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,011 张（Put 792 / Call 1,219），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 33.4k / P 11.5k，今日成交量: C 0.8k / P 0.9k，平值价格ATM: C $1.24 / P $0.15 ｜ ATM IV 100.5%，预期波动 ±3.9%，Max Pain 37
Top ΔOI: P 34 -524 ｜ C 40 +345 ｜ P 42 -191

📆 Forward Expiration Structure

11-27  C +0.3k / P +0.9k ｜ Activity MEDIUM △ ｜ 7D
12-04  C +75 / P +40 ｜ Activity LOW ｜ 14D
12-11  C -0.2k / P +19 ｜ Activity MEDIUM △ ｜ 21D
12-18  C -0.2k / P -1.7k ｜ Activity MEDIUM △ ｜ 28D

📆 11-27 Forward Structure
存量OI: C 12.0k / P 5.8k，今日变化ΔOI: C +0.3k / P +0.9k，平值价格ATM: C $1.80 / P $1.07 ｜ ATM IV 81.5%，净 delta 敞口 -14k shares
Top ΔOI: P 34 +792
仓位参考: Max Pain 38 ｜ Put Wall 33（-8.2%）（OI 2.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 81.5%｜历史 Rank 92%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 14,287 股

12-04（Activity LOW）仓位参考: Max Pain 38 ｜ Call Wall 35（-2.6%）（OI 0.5k） ｜ Put Wall 34（-5.4%，弱）（OI 0.2k）

12-11（MEDIUM △）Top ΔOI: 38C -268
12-11（MEDIUM △）仓位参考: Max Pain 38 ｜ Call Wall 38（+5.7%，弱）（OI 0.8k）

12-18（MEDIUM △）Top ΔOI: 60P -1,674
12-18（MEDIUM △）仓位参考: Max Pain 40 ｜ Put Wall 35（-2.6%，弱）（OI 6.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/MP_morning.json