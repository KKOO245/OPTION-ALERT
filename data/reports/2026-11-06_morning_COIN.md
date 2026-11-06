# 期权晨报 2026-11-06（快照 10:20 ET）

📊 市场环境

SPY $740.12 ｜ QQQ $660.01
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
🟡 **近现价集中开仓**: 11-13 135P ΔOI +639（距现价 -1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-04 135P ΔOI +1,285 占该期限总 OI 13.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 136.82 → 今开 136.51（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 139.28 ｜ 低 133.89

Options: P/C成交量 0.16 | OI比 0.69 | ATM IV 131.2% | Skew 10.9pp | Term 0.54 | ExpMove ±8.8%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.54，近月 IV 高于远月）｜保护溢价显著（Skew 10.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.69）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.16×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（7D）±8.8% ｜ 11-20（14D）±12.4% ｜ 11-27（21D）±14.2% ｜ 12-04（28D）±15.8%
   ⇒ IV–VIX Spread: +106.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 9,917,173 | GEX Change vs 上次快照 1,870,338 | Flip: Primary Flip: 132.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 338 / LOW 163 / INVALID 367
结构观察区: Primary Flip 132.07（全链重定价，覆盖 95%）
最近结构参考: Flip 132（现价高于该位 3.4%）
量化视角： 正 Gamma（992万，无历史分位）｜正 Gamma 增强（+187万）｜现价位于 Flip 上方 3.39%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 141（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 132（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 110.0P — Vol 4,663 | 最新价 $1.49 | OI 1523→3225 (ΔOI +1702张) | ΔOI/Volume 36.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1702张（+111.8% vs前日OI），连续性待观察（方向未知）
12-04 135.0P — Vol 1,400 | 最新价 $9.50 | OI 237→1522 (ΔOI +1285张) | ΔOI/Volume 91.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1285张（+542.2% vs前日OI），连续性待观察（方向未知）
11-06 120.0P — Vol 1,343 | 最新价 $0.27 | OI 2533→3475 (ΔOI +942张) | ΔOI/Volume 70.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增942张（+37.2% vs前日OI），连续性待观察（方向未知）
11-20 157.5C — Vol 1,167 | 最新价 $2.35 | OI 719→1536 (ΔOI +817张) | ΔOI/Volume 70.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增817张（+113.6% vs前日OI），连续性待观察（方向未知）
11-13 144.0C — Vol 1,145 | 最新价 $3.89 | OI 108→859 (ΔOI +751张) | ΔOI/Volume 65.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增751张（+695.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,497 张（Put 3,929 / Call 1,568），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 76.2k / P 52.6k，今日成交量: C 20.8k / P 3.3k，平值价格ATM: C $1.56 / P $2.37 ｜ ATM IV 131.2%，预期波动 ±2.9%，Max Pain 141
Top ΔOI: P 120 +942 ｜ P 175 -747 ｜ C 160 -639

📆 Forward Expiration Structure

11-13  C +3.3k / P +2.7k ｜ Activity HIGH ｜ 7D
11-20  C +3.0k / P -1.5k ｜ Activity MEDIUM △ ｜ 14D
11-27  C +0.3k / P -0.8k ｜ Activity MEDIUM △ ｜ 21D
12-04  C +98 / P +1.2k ｜ Activity HIGH ｜ 28D

📆 11-13 Forward Structure
存量OI: C 17.9k / P 27.1k，今日变化ΔOI: C +3.3k / P +2.7k，平值价格ATM: C $5.85 / P $6.20 ｜ ATM IV 78.4%，净 delta 敞口 23k shares
Top ΔOI: C 144 +751 ｜ P 135 +639 ｜ C 152 +621
仓位参考: Max Pain 150 ｜ Call Wall 144（+5.5%，弱）（OI 0.9k） ｜ Put Wall 130（-4.8%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 78.4%｜历史 Rank 96%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 22,817 股

11-20（MEDIUM △）Top ΔOI: 200P -1,768 ｜ 110P +1,702
11-20（MEDIUM △）仓位参考: Max Pain 165 ｜ Put Wall 140（+2.5%，弱）（OI 3.4k）

11-27（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 150（+9.8%，弱）（OI 0.2k） ｜ Put Wall 140（+2.5%，弱）（OI 0.4k）

📆 12-04 Forward Structure
存量OI: C 4.2k / P 5.6k，今日变化ΔOI: C +98 / P +1.2k，平值价格ATM: C $12.28 / P $9.37 ｜ ATM IV 71.3%，净 delta 敞口 -56k shares
Top ΔOI: P 135 +1,285
仓位参考: Max Pain 140 ｜ Call Wall 140（+2.5%）（OI 1.3k） ｜ Put Wall 135（-1.1%）（OI 1.5k）
量化解读： 存量 Put 重｜ATM IV 71.3%｜历史 Rank 96%（近端代理）｜IV/RV 0.97×（近似）｜净 delta 敞口 负 56,093 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/COIN_morning.json