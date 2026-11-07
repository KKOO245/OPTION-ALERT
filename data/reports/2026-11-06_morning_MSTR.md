# 期权晨报 2026-11-06（快照 10:20 ET）

📊 市场环境

SPY $735.29 ｜ QQQ $656.10
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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 129.30 → 今开 127.83（-1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 130.64 ｜ 低 125.59

Options: P/C成交量 0.32 | OI比 0.58 | ATM IV 152.5% | Skew 17.4pp | Term 0.51 | ExpMove ±10.2%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.51，近月 IV 高于远月）｜保护溢价显著（Skew 17.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.32×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（7D）±10.2% ｜ 11-20（14D）±13.2% ｜ 11-27（21D）±16.8% ｜ 12-04（28D）±17.9%
   ⇒ IV–VIX Spread: +127.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 37,839,922 | GEX Change vs 上次快照 3,772,941 | Flip: Primary Flip: 120.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 445 / LOW 124 / INVALID 275
结构观察区: Primary Flip 120.43（全链重定价，覆盖 94%）
Call Wall 135（现价低于该位 6.0%）
最近结构参考: Flip 120（现价高于该位 5.4%）
量化视角： 正 Gamma（3784万，无历史分位）｜正 Gamma 增强（+377万）｜现价位于 Flip 上方 5.39%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 131（MaxPain，仅结算参考） / 135（Call Wall）。
• Gamma 区域：切换参考 120（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 135.0C — Vol 6,669 | 最新价 $4.67 | OI 347→6301 (ΔOI +5954张) | ΔOI/Volume 89.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5954张（+1715.8% vs前日OI），连续性待观察（方向未知）
11-06 140.0C — Vol 12,791 | 最新价 $0.39 | OI 11805→14694 (ΔOI +2889张) | ΔOI/Volume 22.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2889张（+24.5% vs前日OI），连续性待观察（方向未知）
11-13 141.0C — Vol 2,734 | 最新价 $2.84 | OI 575→3133 (ΔOI +2558张) | ΔOI/Volume 93.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2558张（+444.9% vs前日OI），连续性待观察（方向未知）
11-13 142.0C — Vol 2,793 | 最新价 $2.60 | OI 620→3170 (ΔOI +2550张) | ΔOI/Volume 91.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2550张（+411.3% vs前日OI），连续性待观察（方向未知）
11-06 120.0P — Vol 15,719 | 最新价 $0.78 | OI 3618→5808 (ΔOI +2190张) | ΔOI/Volume 13.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2190张（+60.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 16,141 张（Put 2,190 / Call 13,951），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 247.8k / P 144.2k，今日成交量: C 44.4k / P 14.2k，平值价格ATM: C $1.61 / P $2.67 ｜ ATM IV 152.5%，预期波动 ±3.4%，Max Pain 131
Top ΔOI: C 146 -4,213 ｜ C 140 +2,889 ｜ C 150 -2,397

📆 Forward Expiration Structure

11-13  C +16.1k / P +8.8k ｜ Activity HIGH ｜ 7D
11-20  C +1.4k / P +0.6k ｜ Activity HIGH ｜ 14D
11-27  C +1.5k / P +3.6k ｜ Activity MEDIUM △ ｜ 21D
12-04  C +0.8k / P +2.4k ｜ Activity MEDIUM △ ｜ 28D

📆 11-13 Forward Structure
存量OI: C 51.4k / P 91.3k，今日变化ΔOI: C +16.1k / P +8.8k，平值价格ATM: C $6.34 / P $6.63 ｜ ATM IV 87.5%，净 delta 敞口 186k shares
Top ΔOI: C 135 +5,954 ｜ C 141 +2,558 ｜ C 142 +2,550
仓位参考: Max Pain 142 ｜ Call Wall 135（+6.4%）（OI 6.3k） ｜ Put Wall 125（-1.5%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 87.5%｜历史 Rank 96%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 185,971 股

📆 11-20 Forward Structure
存量OI: C 156.1k / P 140.2k，今日变化ΔOI: C +1.4k / P +0.6k，平值价格ATM: C $7.93 / P $8.80 ｜ ATM IV 83.3%，净 delta 敞口 194k shares
Top ΔOI: P 135 -1,199 ｜ P 95 +962 ｜ C 150 +753
仓位参考: Max Pain 135 ｜ Call Wall 135（+6.4%）（OI 43.0k） ｜ Put Wall 120（-5.5%，弱）（OI 7.3k）
量化解读： 存量两侧均衡｜ATM IV 83.3%｜历史 Rank 96%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 193,511 股

11-27（MEDIUM △）Top ΔOI: 120P +1,535 ｜ 100P +1,456
11-27（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 130（+2.4%，弱）（OI 0.6k） ｜ Put Wall 120（-5.5%，弱）（OI 2.5k）

12-04（MEDIUM △）Top ΔOI: 95P +419
12-04（MEDIUM △）仓位参考: Max Pain 150 ｜ Put Wall 135（+6.4%，弱）（OI 1.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/MSTR_morning.json