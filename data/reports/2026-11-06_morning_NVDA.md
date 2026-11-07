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

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-09 200C ΔOI +3,794（距现价 +3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 181.60 → 今开 191.14（+5.3%） | 较昨收变动（含盘初走势） ｜ 今日高 194.90 ｜ 低 190.00

Options: P/C成交量 0.42 | OI比 0.61 | ATM IV 99.7% | Skew 9.8pp | Term 0.55 | ExpMove ±4.0%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.55，近月 IV 高于远月）｜保护溢价显著（Skew 9.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.61）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.61×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-09（3D）±4.0% ｜ 11-11（5D）±5.6% ｜ 11-13（7D）±6.7% ｜ 11-16（10D）±7.4%
   ⇒ IV–VIX Spread: +74.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 76,417,264 | GEX Change vs 上次快照 218,377,450 | Flip: Primary Flip: 187.84（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 777 / LOW 171 / INVALID 716
结构观察区: Primary Flip 187.84（全链重定价，覆盖 98%）
Put Wall 190（弱结构｜现价高于该位 1.5%） | Call Wall 210（弱结构｜现价低于该位 8.2%）
最近结构参考: Put Wall 190（现价高于该位 1.5%）
量化视角： 正 Gamma（7642万，无历史分位）｜由负转正（+2.18亿）｜现价位于 Flip 上方 2.68%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（Put Wall，弱结构）；上方 195（MaxPain，仅结算参考） / 210（Call Wall，弱结构）。
• Gamma 区域：切换参考 188（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 200.0C — Vol 91,992 | 最新价 $4.25 | OI 31018→79586 (ΔOI +48568张) | ΔOI/Volume 52.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增48568张（+156.6% vs前日OI），连续性待观察（方向未知）
11-06 200.0C — Vol 84,303 | 最新价 $0.14 | OI 3765→22537 (ΔOI +18772张) | ΔOI/Volume 22.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18772张（+498.6% vs前日OI），连续性待观察（方向未知）
11-13 197.5C — Vol 23,268 | 最新价 $2.04 | OI 161→18094 (ΔOI +17933张) | ΔOI/Volume 77.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17933张（+11138.5% vs前日OI），连续性待观察（方向未知）
11-06 195.0C — Vol 97,957 | 最新价 $0.29 | OI 1039→17080 (ΔOI +16041张) | ΔOI/Volume 16.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16041张（+1543.9% vs前日OI），连续性待观察（方向未知）
11-13 190.0C — Vol 24,561 | 最新价 $4.20 | OI 711→15025 (ΔOI +14314张) | ΔOI/Volume 58.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14314张（+2013.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 115,628 张（Put 0 / Call 115,628），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 469.9k / P 287.7k，今日成交量: C 342.3k / P 145.4k，平值价格ATM: C $2.28 / P $1.87 ｜ ATM IV 99.7%，预期波动 ±2.2%，Max Pain 195
Top ΔOI: C 200 +18,772 ｜ C 220 -16,691 ｜ C 195 +16,041

📆 Forward Expiration Structure

11-09  C +23.8k / P +13.8k ｜ Activity HIGH ｜ 3D
11-11  C +23.9k / P +17.2k ｜ Activity HIGH ｜ 5D
11-13  C +74.3k / P +25.9k ｜ Activity HIGH ｜ 7D
11-16  C +6.5k / P +3.6k ｜ Activity HIGH ｜ 10D

📆 11-09 Forward Structure
存量OI: C 51.6k / P 44.4k，今日变化ΔOI: C +23.8k / P +13.8k，平值价格ATM: C $4.05 / P $3.60 ｜ ATM IV 52.8%，净 delta 敞口 1.2M shares
Top ΔOI: C 200 +3,794 ｜ C 190 +2,985
仓位参考: Max Pain 192 ｜ Call Wall 200（+3.7%，弱）（OI 4.2k） ｜ Put Wall 180（-6.7%，弱）（OI 5.3k）
量化解读： 存量两侧均衡｜ATM IV 52.8%｜历史 Rank 96%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 正 1,192,614 股

📆 11-11 Forward Structure
存量OI: C 40.3k / P 40.6k，今日变化ΔOI: C +23.9k / P +17.2k，平值价格ATM: C $5.65 / P $5.15 ｜ ATM IV 59.1%，净 delta 敞口 867k shares
Top ΔOI: C 195 +4,030 ｜ C 200 +3,486
仓位参考: Max Pain 192 ｜ Call Wall 195（+1.1%，弱）（OI 4.1k） ｜ Put Wall 175（-9.3%，弱）（OI 3.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 59.1%｜历史 Rank 96%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 867,145 股

📆 11-13 Forward Structure
存量OI: C 258.0k / P 215.4k，今日变化ΔOI: C +74.3k / P +25.9k，平值价格ATM: C $6.75 / P $6.25 ｜ ATM IV 59.4%，净 delta 敞口 4.2M shares
Top ΔOI: C 197 +17,933 ｜ C 190 +14,314 ｜ P 165 +12,135
仓位参考: Max Pain 198 ｜ Call Wall 197.5（+2.4%，弱）（OI 18.1k） ｜ Put Wall 205（+6.3%，弱）（OI 12.5k）
量化解读： 存量 Call 重｜ATM IV 59.4%｜历史 Rank 96%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,238,579 股

📆 11-16 Forward Structure
存量OI: C 19.7k / P 8.4k，今日变化ΔOI: C +6.5k / P +3.6k，平值价格ATM: C $7.30 / P $6.90 ｜ ATM IV 54.8%，净 delta 敞口 204k shares
Top ΔOI: C 200 +1,022 ｜ P 175 +877
仓位参考: Max Pain 190 ｜ Call Wall 210（+8.9%，弱）（OI 1.4k） ｜ Put Wall 175（-9.3%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 54.8%｜历史 Rank 96%（近端代理）｜IV/RV 1.21×（近似）｜净 delta 敞口 正 204,450 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/NVDA_morning.json