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
🟡 **近现价集中开仓**: 11-27 152P ΔOI +523（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-27 290C ΔOI +5,391 占该期限总 OI 12.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 168.11 → 今开 162.02（-3.6%） | 较昨收变动（含盘初走势） ｜ 今日高 163.38 ｜ 低 151.20

Options: P/C成交量 0.87 | OI比 0.66 | ATM IV 120.5% | Skew -56.4pp | Term 0.87 | ExpMove ±5.0% | Rank 77%
量化视角： IV 历史高位（Rank 77%，期权偏贵）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜Put 保护异常便宜（Skew -56.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.66）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.87×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.66×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 12-04（14D）±17.1% ｜ 12-11（21D）±20.1% ｜ 12-18（28D）±23.8%
   ⇒ IV–VIX Spread: +93.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -13,352,365 | GEX Change vs 上次快照 -1,810,522 | Flip: Primary Flip: 161.16（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 475 / LOW 163 / INVALID 89
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 161.16（全链重定价，覆盖 100%）
Put Wall 150（弱结构｜现价高于该位 2.0%）
最近结构参考: Put Wall 150（现价高于该位 2.0%）
量化视角： 负 Gamma（1335万，无历史分位）｜负 Gamma 加深（181万）｜现价位于 Flip 下方 5.09%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall，弱结构）；上方 180（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 161（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 290.0C — Vol 5,403 | 最新价 $0.04 | OI 762→6153 (ΔOI +5391张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5391张（+707.5% vs前日OI），连续性待观察（方向未知）
11-27 110.0P — Vol 867 | 最新价 $0.16 | OI 49→652 (ΔOI +603张) | ΔOI/Volume 69.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增603张（+1230.6% vs前日OI），连续性待观察（方向未知）
11-20 185.0C — Vol 3,836 | 最新价 $0.52 | OI 1394→1961 (ΔOI +567张) | ΔOI/Volume 14.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增567张（+40.7% vs前日OI），连续性待观察（方向未知）
12-18 170.0C — Vol 919 | 最新价 $18.20 | OI 426→961 (ΔOI +535张) | ΔOI/Volume 58.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增535张（+125.6% vs前日OI），连续性待观察（方向未知）
11-27 152.5P — Vol 550 | 最新价 $4.35 | OI 138→661 (ΔOI +523张) | ΔOI/Volume 95.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增523张（+379.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,619 张（Put 1,126 / Call 6,493），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 111.2k / P 73.2k，今日成交量: C 12.7k / P 11.0k，平值价格ATM: C $5.75 / P $1.94 ｜ ATM IV 120.5%，预期波动 ±5.0%，Max Pain 180
Top ΔOI: P 200 -2,123 ｜ P 220 -2,086 ｜ P 210 -1,241

📆 Forward Expiration Structure

11-27  C +9.4k / P +2.6k ｜ Activity HIGH ｜ 7D
12-04  C +0.7k / P +48 ｜ Activity MEDIUM △ ｜ 14D
12-11  C +0.2k / P +79 ｜ Activity MEDIUM △ ｜ 21D
12-18  C +1.4k / P +1.5k ｜ Activity HIGH ｜ 28D

📆 11-27 Forward Structure
存量OI: C 26.6k / P 16.0k，今日变化ΔOI: C +9.4k / P +2.6k，ATM IV 89.0%，净 delta 敞口 -76k shares
Top ΔOI: P 152 +523
仓位参考: Max Pain 190 ｜ Put Wall 140（-8.5%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 89.0%｜历史 Rank 77%（近端代理）｜IV/RV 0.80×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 76,410 股

12-04（MEDIUM △）Top ΔOI: 175C +82
12-04（MEDIUM △）仓位参考: Max Pain 200 ｜ Put Wall 140（-8.5%，弱）（OI 0.6k）

12-11（MEDIUM △）仓位参考: Max Pain 205 ｜ Put Wall 150（-1.9%，弱）（OI 0.3k）

📆 12-18 Forward Structure
存量OI: C 59.8k / P 76.6k，今日变化ΔOI: C +1.4k / P +1.5k，平值价格ATM: C $19.60 / P $16.85 ｜ ATM IV 104.5%，净 delta 敞口 3k shares
Top ΔOI: C 170 +535 ｜ P 120 +328 ｜ P 150 +262
仓位参考: Max Pain 210 ｜ Put Wall 150（-1.9%，弱）（OI 6.6k）
量化解读： 存量 Put 重｜ATM IV 104.5%｜历史 Rank 77%（近端代理）｜IV/RV 0.93×（近似）｜净 delta 敞口 正 2,680 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/BE_morning.json