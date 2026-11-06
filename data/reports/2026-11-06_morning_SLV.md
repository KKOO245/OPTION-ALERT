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
🟡 **近现价集中开仓**: 11-09 44P ΔOI +5,433（距现价 -4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-09 44P ΔOI +5,433 占该期限总 OI 18.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 46.93 → 今开 46.37（-1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 47.07 ｜ 低 46.35

Options: P/C成交量 0.82 | OI比 0.34 | ATM IV 55.4% | Skew 0.8pp | Term 0.73 | ExpMove ±2.6%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜保护溢价薄（Skew 0.8pp）｜存量 Call 偏重（OI比 0.34）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.82×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.34×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-09（3D）±2.6% ｜ 11-11（5D）±4.0% ｜ 11-13（7D）±4.9% ｜ 11-16（10D）±5.5%
   ⇒ IV–VIX Spread: +30.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 38,701,555 | GEX Change vs 上次快照 -1,557,142 | Flip: Primary Flip: 45.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 729 / LOW 135 / INVALID 300
结构观察区: Primary Flip 45.69（全链重定价，覆盖 94%）
最近结构参考: Flip 46（现价高于该位 2.4%）
量化视角： 正 Gamma（3870万，无历史分位）｜正 Gamma 减弱（156万）｜现价位于 Flip 上方 2.42%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 47（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 46（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-11 40.0P — Vol 10,055 | 最新价 $0.42 | OI 267→10148 (ΔOI +9881张) | ΔOI/Volume 98.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9881张（+3700.8% vs前日OI），连续性待观察（方向未知）
11-20 50.0C — Vol 15,941 | 最新价 $0.61 | OI 16130→21930 (ΔOI +5800张) | ΔOI/Volume 36.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5800张（+36.0% vs前日OI），连续性待观察（方向未知）
11-09 44.5P — Vol 5,670 | 最新价 $0.18 | OI 211→5644 (ΔOI +5433张) | ΔOI/Volume 95.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5433张（+2574.9% vs前日OI），连续性待观察（方向未知）
11-27 42.0P — Vol 2,455 | 最新价 $0.48 | OI 0→2451 (ΔOI +2451张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2451张（前日OI缺失），连续性待观察（方向未知）
11-06 42.5P — Vol 2,554 | 最新价 $0.02 | OI 685→3082 (ΔOI +2397张) | ΔOI/Volume 93.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2397张（+349.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 25,962 张（Put 20,162 / Call 5,800），跨 5 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 151.7k / P 51.2k，今日成交量: C 7.6k / P 8.8k，平值价格ATM: C $0.17 / P $0.42 ｜ ATM IV 55.4%，预期波动 ±1.3%，Max Pain 47
Top ΔOI: P 42 +2,397 ｜ P 47 +1,831 ｜ P 46 +1,786

📆 Forward Expiration Structure

11-09  C +1.8k / P +7.2k ｜ Activity HIGH ｜ 3D
11-11  C +2.2k / P +3.7k ｜ Activity HIGH ｜ 5D
11-13  C +3.6k / P +3.8k ｜ Activity MEDIUM △ ｜ 7D
11-16  C +0.5k / P +0.4k ｜ Activity MEDIUM △ ｜ 10D

📆 11-09 Forward Structure
存量OI: C 11.4k / P 17.8k，今日变化ΔOI: C +1.8k / P +7.2k，平值价格ATM: C $0.50 / P $0.73 ｜ ATM IV 34.7%，净 delta 敞口 -86k shares
Top ΔOI: P 44 +5,433 ｜ C 50 +648 ｜ P 45 +438
仓位参考: Max Pain 46 ｜ Call Wall 50（+6.8%）（OI 2.4k） ｜ Put Wall 44.5（-4.9%）（OI 5.6k）
量化解读： 存量 Put 重｜ATM IV 34.7%｜历史 Rank 88%（近端代理）｜IV/RV 0.75×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 86,279 股

📆 11-11 Forward Structure
存量OI: C 15.0k / P 10.0k，今日变化ΔOI: C +2.2k / P +3.7k，平值价格ATM: C $0.86 / P $1.00 ｜ ATM IV 41.9%，净 delta 敞口 -10k shares
Top ΔOI: C 49 +551
仓位参考: Max Pain 46 ｜ Call Wall 51（+9.0%）（OI 2.9k） ｜ Put Wall 44（-6.0%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 41.9%｜历史 Rank 88%（近端代理）｜IV/RV 0.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 10,329 股

11-13（MEDIUM △）Top ΔOI: 48C +854
11-13（MEDIUM △）仓位参考: Max Pain 48 ｜ Call Wall 50（+6.8%，弱）（OI 7.0k） ｜ Put Wall 45（-3.8%，弱）（OI 3.3k）

11-16（MEDIUM △）Top ΔOI: 48C +192 ｜ 45P +126
11-16（MEDIUM △）仓位参考: Max Pain 46 ｜ Call Wall 51（+9.0%）（OI 1.1k） ｜ Put Wall 45（-3.8%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/SLV_morning.json