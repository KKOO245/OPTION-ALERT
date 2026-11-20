# 期权晨报 2026-11-20（快照 10:20 ET）

📊 市场环境

SPY $709.45 ｜ QQQ $630.79
VIX 27.48 ↓3.4%（5D +42.4%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-27 141P ΔOI +204（距现价 -2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-04 141P ΔOI +2,166 占该期限总 OI 55.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 144.12 → 今开 142.88（-0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 145.48 ｜ 低 142.39

Options: P/C成交量 2.11 | OI比 1.34 | ATM IV 53.4% | Skew 2.4pp | Term 0.80 | ExpMove ±4.0%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价中性（Skew 2.4pp）｜当日成交偏 Put（P/C量 2.11）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.11×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.34×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-27（7D）±4.0% ｜ 12-18（28D）±8.1%
   ⇒ IV–VIX Spread: +25.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -42,518,895 | GEX Change vs 上次快照 -5,789,136 | Flip: Primary Flip: 148.73（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 406 / LOW 159 / INVALID 54
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 148.73（全链重定价，覆盖 89%）
Put Wall 140（弱结构｜现价高于该位 2.8%）
最近结构参考: Put Wall 140（现价高于该位 2.8%）
量化视角： 负 Gamma（4252万，无历史分位）｜负 Gamma 加深（579万）｜现价位于 Flip 下方 3.25%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（Put Wall，弱结构）；上方 149（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 149（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 150.0C — Vol 5,129 | 最新价 $0.10 | OI 4402→7055 (ΔOI +2653张) | ΔOI/Volume 51.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2653张（+60.3% vs前日OI），连续性待观察（方向未知）
12-04 141.0P — Vol 2,351 | 最新价 $2.80 | OI 4→2170 (ΔOI +2166张) | ΔOI/Volume 92.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2166张（+54150.0% vs前日OI），连续性待观察（方向未知）
11-20 151.0C — Vol 1,562 | 最新价 $0.05 | OI 174→627 (ΔOI +453张) | ΔOI/Volume 29.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增453张（+260.3% vs前日OI），连续性待观察（方向未知）
12-18 160.0C — Vol 573 | 最新价 $1.23 | OI 3749→4196 (ΔOI +447张) | ΔOI/Volume 78.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增447张（+11.9% vs前日OI），连续性待观察（方向未知）
11-27 151.0C — Vol 394 | 最新价 $0.91 | OI 52→421 (ΔOI +369张) | ΔOI/Volume 93.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增369张（+709.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,088 张（Put 2,166 / Call 3,922），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 41.3k / P 55.4k，今日成交量: C 1.9k / P 3.9k，平值价格ATM: C $1.71 / P $0.94 ｜ ATM IV 53.4%，预期波动 ±1.8%，Max Pain 149
Top ΔOI: C 150 +2,653 ｜ P 152 -1,222 ｜ P 153 -865

📆 Forward Expiration Structure

11-27  C +0.6k / P +0.2k ｜ Activity HIGH ｜ 7D
12-04  C +8 / P +2.5k ｜ Activity HIGH ｜ 14D
12-11  C +0 / P +64 ｜ Activity MEDIUM △ ｜ 21D
12-18  C +0.9k / P -7.9k ｜ Activity MEDIUM △ ｜ 28D

📆 11-27 Forward Structure
存量OI: C 2.7k / P 5.5k，今日变化ΔOI: C +0.6k / P +0.2k，平值价格ATM: C $3.04 / P $2.73 ｜ ATM IV 43.2%，净 delta 敞口 6k shares
Top ΔOI: C 151 +369 ｜ P 141 +204 ｜ P 135 -109
仓位参考: Max Pain 151 ｜ Call Wall 151（+4.9%，弱）（OI 0.4k） ｜ Put Wall 143（-0.6%，弱）（OI 1.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 43.2%｜历史 Rank 98%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,985 股

📆 12-04 Forward Structure
存量OI: C 0.4k / P 3.5k，今日变化ΔOI: C +8 / P +2.5k，ATM IV 47.7%，净 delta 敞口 -90k shares
Top ΔOI: P 141 +2,166 ｜ P 135 +200 ｜ P 145 +192
仓位参考: Max Pain 159 ｜ Put Wall 141（-2.0%）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 47.7%｜历史 Rank 98%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 89,570 股

12-11（MEDIUM △）Top ΔOI: 136P +40 ｜ 141P +23
12-11（MEDIUM △）仓位参考: Max Pain 152 ｜ Call Wall 150（+4.2%，弱）（OI 25） ｜ Put Wall 135（-6.2%，弱）（OI 0.4k）

12-18（MEDIUM △）Top ΔOI: 133P -3,143 ｜ 143P -2,566
12-18（MEDIUM △）仓位参考: Max Pain 136 ｜ Call Wall 135（-6.2%，弱）（OI 11.2k） ｜ Put Wall 150（+4.2%，弱）（OI 5.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/XBI_morning.json